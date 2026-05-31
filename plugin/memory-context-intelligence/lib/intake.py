#!/usr/bin/env python3
"""Bounded memsearch intake for memory-context-intelligence.

This helper intentionally reads only explicitly configured memory roots and emits
an observational intake report. It does not generate topics, write candidates,
write /additional/, install hooks, or mutate main RULES.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

LIB_DIR = Path(__file__).resolve().parent
if str(LIB_DIR) not in os.sys.path:
    os.sys.path.insert(0, str(LIB_DIR))

from config_policy import DEFAULT_CONFIG_FILENAME, load_analysis_source_policy

PRIMARY_MEMORY_ROOT_ENV = "MEMORY_CONTEXT_INTELLIGENCE_MEMORY_ROOT"
SHORT_MEMORY_ROOT_ENV = "MCI_MEMORY_ROOT"

DAILY_SHARD_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?i)\b(api[_-]?key|token|secret|password|credential|authorization)\b\s*[:=]\s*([^\s,;]+)"
)
BEARER_RE = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+\-/]+=*")
LONG_HEX_RE = re.compile(r"(?<![A-Za-z0-9])[A-Fa-f0-9]{32,}(?![A-Za-z0-9])")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
URL_RE = re.compile(r"https?://[^\s)]+")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->")
POSIX_LOCAL_PATH_RE = re.compile(r"/(?:home|Users|tmp|var/tmp)/[^\s)]+")
WINDOWS_LOCAL_PATH_RE = re.compile(r"[A-Za-z]:\\[^\s)]+")
TIME_HEADING_RE = re.compile(r"^###\s+(\d{2}:\d{2})\s*$")
ANCHOR_RE = re.compile(r"<!--\s*session:(\S+)\s+turn:(\S+)\s+transcript:(\S+)\s*-->")
MEMORY_LINK_RE = re.compile(r"-\s+\[(?P<title>[^\]]+)\]\((?P<path>[^)]+)\)\s+—\s+(?P<hook>.+)")
MEMORY_CODE_ENTRY_RE = re.compile(r"-\s+`(?P<path>[^`]+)`\s+—\s+(?P<hook>.+)")
MEMORY_SCOPE_RE = re.compile(r"^Scope:\s*`(?P<path>[^`]+)`")
MEMORY_BASE_RE = re.compile(r"^Memory base:\s*`(?P<path>[^`]+)`")
SOURCE_CLASS_ORDER = (
    "trace_evidence",
    "recall_evidence",
    "durable_memory_context",
    "governance_context",
)


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence intake",
        description=(
            "Read a bounded subset of explicit memsearch daily markdown shards "
            "and emit an observational intake report."
        ),
    )
    parser.add_argument(
        "--memory-root",
        help=(
            "Explicit memsearch memory root. If omitted, "
            f"{PRIMARY_MEMORY_ROOT_ENV} or {SHORT_MEMORY_ROOT_ENV} may provide it. "
            "No package default is used."
        ),
    )
    parser.add_argument(
        "--config",
        help=(
            "Explicit config-policy JSON file. If omitted, "
            f"{DEFAULT_CONFIG_FILENAME} may be discovered upward from the current working directory."
        ),
    )
    parser.add_argument(
        "--scope",
        action="append",
        default=[],
        help="Case-insensitive substring filter for records. May be repeated.",
    )
    parser.add_argument(
        "--day",
        help="Select one YYYY-MM-DD shard explicitly. If omitted, default shard selection behavior applies.",
    )
    parser.add_argument(
        "--session-id",
        help="Restrict intake to one session id inside the selected day shard before any optional widening.",
    )
    parser.add_argument(
        "--lookback-minutes",
        type=int,
        default=None,
        help="Restrict records to the last N minutes inside the scoped same-day slice.",
    )
    parser.add_argument(
        "--allow-same-day-widening",
        action="store_true",
        dest="allow_same_day_widening",
        default=False,
        help="Allow same-day widening after a scoped current-session slice is insufficient.",
    )
    parser.add_argument("--max-shards", type=int, default=10, help="Daily shards to consider, capped at 10.")
    parser.add_argument("--max-records", type=int, default=8, help="Sample records to emit, capped at 50.")
    parser.add_argument("--max-chars", type=int, default=6000, help="Total emitted sample characters, capped at 20000.")
    parser.add_argument(
        "--max-shard-bytes",
        type=int,
        default=65536,
        help="Bytes read from each shard, capped at 262144.",
    )
    parser.add_argument("--max-age-days", type=int, default=30, help="Freshness threshold for latest shard.")
    return parser.parse_args(argv)


def resolve_memory_root(args: argparse.Namespace) -> tuple[str | None, str]:
    if args.memory_root:
        return args.memory_root, "cli"
    env_value = os.environ.get(PRIMARY_MEMORY_ROOT_ENV)
    if env_value:
        return env_value, f"env:{PRIMARY_MEMORY_ROOT_ENV}"
    short_env_value = os.environ.get(SHORT_MEMORY_ROOT_ENV)
    if short_env_value:
        return short_env_value, f"env:{SHORT_MEMORY_ROOT_ENV}"
    return None, "unset"


def minimize_sensitive_content(text: str) -> str:
    minimized = HTML_COMMENT_RE.sub("[metadata redacted]", text)
    minimized = SECRET_ASSIGNMENT_RE.sub(lambda m: f"{m.group(1)}=<redacted>", minimized)
    minimized = BEARER_RE.sub("Bearer <redacted>", minimized)
    minimized = EMAIL_RE.sub("<email>", minimized)
    minimized = URL_RE.sub("<url>", minimized)
    minimized = POSIX_LOCAL_PATH_RE.sub("<local-path>", minimized)
    minimized = WINDOWS_LOCAL_PATH_RE.sub("<local-path>", minimized)
    minimized = LONG_HEX_RE.sub("<redacted-token>", minimized)
    return minimized.strip()


def parse_shard_date(path: Path) -> date | None:
    try:
        return datetime.strptime(path.stem, "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_clock_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%H:%M")
    except ValueError:
        return None


def resolve_path(path: Path) -> Path:
    try:
        return path.expanduser().resolve()
    except OSError:
        return path.expanduser().absolute()


def explicit_narrow_request_active(
    *,
    day_shard: str | None,
    session_id: str | None,
    lookback_minutes: int | None,
    scope_filters: list[str],
) -> bool:
    return bool(day_shard or session_id or lookback_minutes is not None or scope_filters)


def filter_records_for_source_policy(records: list[dict[str, Any]], allowed_source_classes: list[str]) -> list[dict[str, Any]]:
    filtered: list[dict[str, Any]] = []
    allowed = set(allowed_source_classes)
    for record in records:
        source_classes = [source_class for source_class in record_source_classes(record) if source_class in allowed]
        if not source_classes:
            continue
        copied = dict(record)
        copied["source_classes"] = source_classes
        filtered.append(copied)
    return filtered


def build_source_policy_state(
    args: argparse.Namespace,
    *,
    project_dir: Path,
    scope_filters: list[str],
    active_scope_basis: str,
    max_shards: int,
    day_shard: str | None,
    session_id: str | None,
    lookback_minutes: int | None,
) -> dict[str, Any]:
    loaded_policy = load_analysis_source_policy(
        explicit_config_path=getattr(args, "config", None),
        cwd=project_dir,
    )
    explicit_narrow = explicit_narrow_request_active(
        day_shard=day_shard,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
        scope_filters=scope_filters,
    )
    requested_same_day_widening = bool(loaded_policy["requested_same_day_widening"])
    explicit_same_day_widening = bool(getattr(args, "allow_same_day_widening", False))
    effective_same_day_widening = explicit_same_day_widening or (requested_same_day_widening and not explicit_narrow)
    effective_max_historical_shards = max_shards
    if active_scope_basis == "historical-default" and loaded_policy["max_historical_shards"] is not None:
        effective_max_historical_shards = min(max_shards, int(loaded_policy["max_historical_shards"]))

    limitation_notes: list[str] = []
    if loaded_policy["enabled_source_classes"] != list(SOURCE_CLASS_ORDER):
        limitation_notes.append(
            f"Config policy limited this run to {' + '.join(loaded_policy['enabled_source_classes'])}."
        )
    if active_scope_basis == "historical-default" and loaded_policy["max_historical_shards"] is not None:
        limitation_notes.append(
            f"Historical-default shard selection was capped at {effective_max_historical_shards} shard(s)."
        )
    if requested_same_day_widening and not explicit_same_day_widening:
        if effective_same_day_widening:
            limitation_notes.append("Config policy enabled same-day widening for implicit runs.")
        else:
            limitation_notes.append("Config requested same-day widening, but this explicit narrow run stayed narrow.")

    if loaded_policy["errors"]:
        policy_note = (
            "Config file could not be loaded; runtime defaults remain active. Error: "
            + "; ".join(str(item) for item in loaded_policy["errors"])
        )
    elif not loaded_policy["loaded"]:
        policy_note = "No config file was loaded; runtime defaults remain active."
    elif limitation_notes:
        policy_note = " ".join(limitation_notes)
    else:
        policy_note = "Config file loaded without changing the active source-policy limits."

    return {
        "loaded": loaded_policy["loaded"],
        "config_path": loaded_policy["config_path"],
        "config_source": loaded_policy["config_source"],
        "effective_source_classes": list(loaded_policy["enabled_source_classes"]),
        "requested_same_day_widening": requested_same_day_widening,
        "effective_same_day_widening": effective_same_day_widening,
        "max_historical_shards": effective_max_historical_shards,
        "policy_limited": bool(limitation_notes),
        "policy_note": policy_note,
    }


def derive_memsearch_collection_name(project_dir: Path | None = None) -> str:
    resolved_dir = resolve_path(project_dir or Path.cwd())
    sanitized = re.sub(r"_+", "_", re.sub(r"[^a-z0-9]", "_", resolved_dir.name.lower())).strip("_")[:40] or "root"
    digest = hashlib.sha256(str(resolved_dir).encode("utf-8")).hexdigest()[:8]
    return f"ms_{sanitized}_{digest}"


def derive_memsearch_source_prefix(shard: Path, project_dir: Path | None = None) -> str:
    resolved_project_dir = resolve_path(project_dir or Path.cwd())
    resolved_shard = resolve_path(shard)
    try:
        return str(resolved_shard.relative_to(resolved_project_dir))
    except ValueError:
        return str(resolved_shard)


def record_source_classes(record: dict[str, Any]) -> list[str]:
    raw = record.get("source_classes")
    if isinstance(raw, list):
        values = [str(item) for item in raw if item]
        if values:
            return list(dict.fromkeys(values))
    return ["trace_evidence"]


def with_source_classes(records: list[dict[str, Any]], *source_classes: str) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    extras = [value for value in source_classes if value]
    for record in records:
        copied = dict(record)
        copied["source_classes"] = list(dict.fromkeys(record_source_classes(copied) + extras))
        enriched.append(copied)
    return enriched


def source_classes_present(records: list[dict[str, Any]]) -> list[str]:
    present: list[str] = []
    for source_class in SOURCE_CLASS_ORDER:
        if any(source_class in record_source_classes(record) for record in records):
            present.append(source_class)
    return present


def source_class_counts(records: list[dict[str, Any]]) -> dict[str, int]:
    counts = {source_class: 0 for source_class in SOURCE_CLASS_ORDER}
    for record in records:
        for source_class in record_source_classes(record):
            if source_class in counts:
                counts[source_class] += 1
    return counts


def encode_claude_project_key(project_dir: Path) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "-", str(resolve_path(project_dir))).strip("-")
    return f"-{normalized}" if normalized else "-root"


def discover_claude_memory_root(project_dir: Path | None = None) -> Path | None:
    resolved_project_dir = resolve_path(project_dir or Path.cwd())
    candidate = Path.home() / ".claude" / "projects" / encode_claude_project_key(resolved_project_dir) / "memory"
    if (candidate / "MEMORY.md").is_file():
        return candidate
    return None


def paths_share_scope(left: Path, right: Path) -> bool:
    left_resolved = resolve_path(left)
    right_resolved = resolve_path(right)
    try:
        left_resolved.relative_to(right_resolved)
        return True
    except ValueError:
        pass
    try:
        right_resolved.relative_to(left_resolved)
        return True
    except ValueError:
        return False


def markdown_preview(path: Path, max_chars: int = 480) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    lines = text.splitlines()
    preview_parts: list[str] = []
    in_frontmatter = False
    frontmatter_consumed = False
    for line in lines:
        stripped = line.strip()
        if stripped == "---" and not frontmatter_consumed:
            in_frontmatter = not in_frontmatter
            if not in_frontmatter:
                frontmatter_consumed = True
            continue
        if in_frontmatter or not stripped:
            continue
        if stripped.startswith("> **"):
            continue
        preview_parts.append(stripped.lstrip("#").strip())
        preview = minimize_sensitive_content(" ".join(preview_parts))
        if len(preview) >= max_chars:
            return preview[:max_chars].rstrip()
    return minimize_sensitive_content(" ".join(preview_parts))[:max_chars].rstrip()


def matches_scope_filters(text: str, scope_filters: list[str]) -> bool:
    if not scope_filters:
        return True
    lowered = text.lower()
    return any(scope.lower() in lowered for scope in scope_filters)


def discover_durable_memory_context_records(
    project_dir: Path | None = None,
    scope_filters: list[str] | None = None,
    max_records: int = 4,
    max_chars: int = 1200,
) -> list[dict[str, Any]]:
    resolved_project_dir = resolve_path(project_dir or Path.cwd())
    filters = scope_filters or []
    memory_root = discover_claude_memory_root(resolved_project_dir)
    if memory_root is None:
        return []

    records: list[dict[str, Any]] = []
    index_path = memory_root / "MEMORY.md"
    index_preview = markdown_preview(index_path, max_chars=min(320, max_chars))
    if index_preview:
        records.append(
            {
                "shard": "MEMORY.md",
                "section": "memory-index",
                "session_id": None,
                "turn_id": None,
                "transcript": None,
                "content": index_preview,
                "source_classes": ["durable_memory_context"],
            }
        )

    current_mode = None
    current_scope: Path | None = None
    current_memory_base: Path | None = None
    for line in index_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## GLOBAL"):
            current_mode = "global"
            current_scope = None
            current_memory_base = None
            continue
        if stripped.startswith("## PATH_SCOPE:"):
            current_mode = "path"
            current_scope = None
            current_memory_base = None
            continue
        scope_match = MEMORY_SCOPE_RE.match(stripped)
        if scope_match:
            current_scope = Path(scope_match.group("path"))
            continue
        base_match = MEMORY_BASE_RE.match(stripped)
        if base_match:
            current_memory_base = memory_root / base_match.group("path")
            continue

        entry_match = MEMORY_LINK_RE.match(stripped)
        entry_path = None
        hook = None
        if entry_match:
            entry_path = entry_match.group("path")
            hook = entry_match.group("hook")
        else:
            code_match = MEMORY_CODE_ENTRY_RE.match(stripped)
            if code_match:
                entry_path = code_match.group("path")
                hook = code_match.group("hook")
        if not entry_path or not hook:
            continue
        if current_mode == "path" and (current_scope is None or not paths_share_scope(resolved_project_dir, current_scope)):
            continue

        if current_mode == "global":
            candidate_path = memory_root / entry_path
        else:
            candidate_path = (current_memory_base or memory_root) / entry_path
        candidate_path = resolve_path(candidate_path)
        if not candidate_path.is_file():
            continue

        preview = markdown_preview(candidate_path, max_chars=min(320, max_chars))
        combined = minimize_sensitive_content(f"{hook} {preview}".strip())
        if not matches_scope_filters(f"{candidate_path} {combined}", filters):
            continue
        records.append(
            {
                "shard": candidate_path.name,
                "section": candidate_path.stem,
                "session_id": None,
                "turn_id": None,
                "transcript": None,
                "content": combined[:max_chars].rstrip(),
                "source_classes": ["durable_memory_context"],
            }
        )
        if len(records) >= max_records:
            break
    return records[:max_records]


def resolve_governance_root() -> Path | None:
    package_root = Path(__file__).resolve().parents[1]
    package_path = str(package_root)
    if "TEMPLATE/RULES/plugin/memory-context-intelligence" in package_path:
        return package_root
    template_root = package_root.parents[1]
    candidate = template_root / "RULES" / "plugin" / "memory-context-intelligence"
    if candidate.is_dir():
        return candidate
    return None


def discover_governance_context_records(
    project_dir: Path | None = None,
    scope_filters: list[str] | None = None,
    max_records: int = 5,
    max_chars: int = 1400,
) -> list[dict[str, Any]]:
    filters = scope_filters or []
    governance_root = resolve_governance_root()
    if governance_root is None:
        return []
    rules_root = governance_root.parents[1]
    candidates = [
        governance_root / "design" / "design.md",
        governance_root / "phase" / "SUMMARY.md",
        governance_root / "patch" / "memory-context-intelligence-design-only-baseline.patch.md",
        rules_root / "TODO.md",
        governance_root / "changelog" / "changelog.md",
    ]

    records: list[dict[str, Any]] = []
    for candidate_path in candidates:
        if not candidate_path.is_file():
            continue
        preview = markdown_preview(candidate_path, max_chars=min(360, max_chars))
        combined = minimize_sensitive_content(preview)
        if not combined:
            continue
        if not matches_scope_filters(f"{candidate_path} {combined}", filters):
            if filters:
                continue
        records.append(
            {
                "shard": candidate_path.name,
                "section": candidate_path.parent.name,
                "session_id": None,
                "turn_id": None,
                "transcript": None,
                "content": combined[:max_chars].rstrip(),
                "source_classes": ["governance_context"],
            }
        )
        if len(records) >= max_records:
            break
    return records


def retrieve_memsearch_backed_session_records(
    shard: Path,
    session_id: str,
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    lookback_minutes: int | None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    project_dir = resolve_path(Path.cwd())
    collection = derive_memsearch_collection_name(project_dir)
    source_prefix = derive_memsearch_source_prefix(shard, project_dir)
    metadata: dict[str, Any] = {
        "preferred_retrieval_mode": "memsearch-search-expand",
        "search_hits": 0,
        "expanded_chunks": 0,
        "fallback_used": False,
        "memsearch_error": None,
        "memsearch_collection": collection,
        "source_prefix": source_prefix,
    }
    search_command = [
        "memsearch",
        "search",
        session_id,
        "--top-k",
        str(max(1, min(max_records, 8))),
        "--json-output",
        "--collection",
        collection,
        "--source-prefix",
        source_prefix,
    ]
    try:
        search_completed = subprocess.run(
            search_command,
            cwd=str(project_dir),
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        metadata["memsearch_error"] = str(exc)
        return [], metadata
    if search_completed.returncode != 0:
        metadata["memsearch_error"] = (search_completed.stderr or search_completed.stdout).strip() or (
            f"memsearch search exited {search_completed.returncode}"
        )
        return [], metadata
    try:
        search_hits = json.loads(search_completed.stdout or "[]")
    except json.JSONDecodeError as exc:
        metadata["memsearch_error"] = f"memsearch search output was not valid JSON: {exc}"
        return [], metadata
    if not isinstance(search_hits, list):
        metadata["memsearch_error"] = "memsearch search output was not a JSON list."
        return [], metadata

    metadata["search_hits"] = len(search_hits)
    expanded_entries: list[dict[str, Any]] = []
    for hit in search_hits[: max(1, min(max_records, len(search_hits)))]:
        chunk_hash = hit.get("chunk_hash")
        if not chunk_hash:
            continue
        expand_command = ["memsearch", "expand", str(chunk_hash), "--collection", collection]
        try:
            expand_completed = subprocess.run(
                expand_command,
                cwd=str(project_dir),
                capture_output=True,
                text=True,
                timeout=15,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            if metadata["memsearch_error"] is None:
                metadata["memsearch_error"] = str(exc)
            continue
        if expand_completed.returncode != 0:
            if metadata["memsearch_error"] is None:
                metadata["memsearch_error"] = (expand_completed.stderr or expand_completed.stdout).strip() or (
                    f"memsearch expand exited {expand_completed.returncode}"
                )
            continue
        metadata["expanded_chunks"] += 1
        hit_source = hit.get("source")
        source_path = Path(hit_source) if isinstance(hit_source, str) and hit_source else shard
        expanded_entries.extend(parse_record_entries(source_path, expand_completed.stdout))

    if not expanded_entries:
        return [], metadata

    session_entries = [entry for entry in expanded_entries if entry.get("session_id") == session_id]
    session_entries = filter_entries_by_lookback(session_entries, lookback_minutes)
    records, _, _ = flatten_entries(session_entries, scope_filters, max_records, max_chars)
    return records, metadata


def availability_report(
    *,
    memory_root: str | None,
    memory_root_source: str,
    status: str,
    evidence_strength: str,
    reason: str,
) -> dict[str, Any]:
    return {
        "tool": "memory-context-intelligence",
        "mode": "intake",
        "status": status,
        "evidence_strength": evidence_strength,
        "source": {
            "kind": "memsearch-daily-markdown-shards",
            "memory_root_source": memory_root_source,
            "memory_root": memory_root,
            "available": False,
            "daily_shards_discovered": 0,
            "daily_shards_considered": [],
            "retrieval_mode": None,
            "preferred_retrieval_mode": None,
            "search_hits": 0,
            "expanded_chunks": 0,
            "fallback_used": False,
            "memsearch_error": None,
            "memsearch_collection": None,
            "source_prefix": None,
        },
        "scope": {
            "basis": None,
            "filters": [],
            "day_shard": None,
            "session_id": None,
            "lookback_minutes": None,
            "same_day_widening_allowed": False,
            "same_day_widened": False,
            "historical_shards_considered": 0,
            "bounded_subset_only": True,
        },
        "freshness": {
            "latest_shard_date": None,
            "latest_shard_mtime": None,
            "age_days": None,
            "max_age_days": None,
            "classification": "unknown",
        },
        "records": [],
        "limits": {},
        "notes": standard_notes(reason),
        "topic_generation_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def standard_notes(reason: str | None = None) -> list[str]:
    notes = [
        "Memory summaries are observational work-trace input only; they are not RULES authority or current runtime truth.",
        "Topic generation has not been performed by intake mode.",
        "/additional/ emission has not been performed by intake mode.",
        "Main RULES mutation has not been performed by intake mode.",
        "Sample content is privacy-minimized and bounded; omitted content was not evaluated.",
    ]
    if reason:
        notes.append(reason)
    return notes


def discover_daily_shards(memory_root: Path) -> list[Path]:
    return sorted(
        (path for path in memory_root.iterdir() if path.is_file() and DAILY_SHARD_RE.match(path.name)),
        key=lambda path: path.name,
        reverse=True,
    )


def scope_basis(args: argparse.Namespace) -> str:
    if getattr(args, "day", None) and getattr(args, "session_id", None):
        return "explicit-day-and-session"
    if getattr(args, "day", None):
        return "explicit-day"
    if getattr(args, "session_id", None):
        return "explicit-session"
    return "historical-default"


def select_daily_shards(shards: list[Path], args: argparse.Namespace, max_shards: int) -> list[Path]:
    day_shard = getattr(args, "day", None)
    session_id = getattr(args, "session_id", None)
    lookback_minutes = getattr(args, "lookback_minutes", None)
    allow_same_day_widening = getattr(args, "allow_same_day_widening", False)
    if day_shard:
        return [path for path in shards if path.stem == day_shard][:1]
    if session_id or lookback_minutes is not None or allow_same_day_widening:
        return shards[:1]
    return shards[:max_shards]


def read_bounded_text(path: Path, max_bytes: int) -> tuple[str, bool]:
    with path.open("rb") as handle:
        data = handle.read(max_bytes + 1)
    truncated = len(data) > max_bytes
    if truncated:
        data = data[:max_bytes]
    return data.decode("utf-8", errors="replace"), truncated


def parse_record_entries(shard: Path, text: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    current_time: str | None = None
    current_section: str | None = None
    current_session_id: str | None = None
    current_turn_id: str | None = None
    current_transcript: str | None = None
    current_bullets: list[str] = []

    def flush() -> None:
        if not current_bullets:
            return
        section = current_time or current_section or shard.stem
        entries.append(
            {
                "shard": shard.name,
                "time": current_time,
                "section": section,
                "session_id": current_session_id,
                "turn_id": current_turn_id,
                "transcript": current_transcript,
                "bullet_lines": list(current_bullets),
            }
        )

    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        time_match = TIME_HEADING_RE.match(stripped)
        if time_match:
            flush()
            current_time = time_match.group(1)
            current_section = current_time
            current_session_id = None
            current_turn_id = None
            current_transcript = None
            current_bullets = []
            continue
        if stripped.startswith("### "):
            flush()
            current_time = None
            current_section = stripped[4:].strip() or shard.stem
            current_session_id = None
            current_turn_id = None
            current_transcript = None
            current_bullets = []
            continue
        anchor_match = ANCHOR_RE.search(stripped)
        if anchor_match:
            current_session_id = anchor_match.group(1)
            current_turn_id = anchor_match.group(2)
            current_transcript = anchor_match.group(3)
            if current_time is None and current_section is None:
                current_section = shard.stem
            continue
        if stripped.startswith("- "):
            if current_time is None and current_section is None:
                current_section = shard.stem
            current_bullets.append(stripped)

    flush()
    return entries


def filter_entries_by_lookback(entries: list[dict[str, Any]], lookback_minutes: int | None) -> list[dict[str, Any]]:
    if lookback_minutes is None:
        return list(entries)
    latest_time = None
    for entry in entries:
        parsed = parse_clock_time(entry.get("time"))
        if parsed and (latest_time is None or parsed > latest_time):
            latest_time = parsed
    if latest_time is None:
        return list(entries)
    cutoff = latest_time - timedelta(minutes=max(0, lookback_minutes))
    filtered: list[dict[str, Any]] = []
    for entry in entries:
        parsed = parse_clock_time(entry.get("time"))
        if parsed is None:
            filtered.append(entry)
            continue
        if cutoff <= parsed <= latest_time:
            filtered.append(entry)
    return filtered


def flatten_entries(
    entries: list[dict[str, Any]],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
) -> tuple[list[dict[str, Any]], bool, int]:
    records: list[dict[str, Any]] = []
    truncated_by_limits = False
    emitted_chars = 0
    normalized_filters = [item.lower() for item in scope_filters if item.strip()]

    for entry in entries:
        for bullet in entry["bullet_lines"]:
            if len(records) >= max_records or emitted_chars >= max_chars:
                truncated_by_limits = True
                return records, truncated_by_limits, emitted_chars
            searchable = bullet.lower()
            if normalized_filters and not any(scope in searchable for scope in normalized_filters):
                continue
            minimized = minimize_sensitive_content(bullet)
            if not minimized:
                continue
            remaining = max_chars - emitted_chars
            if remaining <= 0:
                truncated_by_limits = True
                return records, truncated_by_limits, emitted_chars
            if len(minimized) > remaining:
                minimized = minimized[: max(0, remaining - 3)].rstrip() + "..."
                truncated_by_limits = True
            records.append(
                {
                    "shard": entry["shard"],
                    "section": entry["section"],
                    "time": entry["time"],
                    "session_id": entry["session_id"],
                    "turn_id": entry["turn_id"],
                    "transcript": entry["transcript"],
                    "content": minimized,
                }
            )
            emitted_chars += len(minimized)
    return records, truncated_by_limits, emitted_chars


def read_entries_from_shards(
    shards: list[Path],
    max_shard_bytes: int,
) -> tuple[list[dict[str, Any]], list[str], bool]:
    entries: list[dict[str, Any]] = []
    errors: list[str] = []
    truncated_by_limits = False

    for shard in shards:
        try:
            text, shard_truncated = read_bounded_text(shard, max_shard_bytes)
            truncated_by_limits = truncated_by_limits or shard_truncated
        except OSError as exc:
            errors.append(f"{shard.name}: {exc}")
            continue
        entries.extend(parse_record_entries(shard, text))

    return entries, errors, truncated_by_limits


def collect_records_from_entries(
    entries: list[dict[str, Any]],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    *,
    session_id: str | None = None,
    lookback_minutes: int | None = None,
    allow_same_day_widening: bool = False,
) -> tuple[list[dict[str, Any]], bool, int, bool]:
    primary_entries = list(entries)
    if session_id:
        primary_entries = [entry for entry in primary_entries if entry.get("session_id") == session_id]
    primary_entries = filter_entries_by_lookback(primary_entries, lookback_minutes)
    records, primary_truncated, emitted_chars = flatten_entries(primary_entries, scope_filters, max_records, max_chars)

    same_day_widened = False
    if session_id and allow_same_day_widening and not records:
        widened_entries = filter_entries_by_lookback(entries, lookback_minutes)
        records, widened_truncated, emitted_chars = flatten_entries(
            widened_entries,
            scope_filters,
            max_records,
            max_chars,
        )
        primary_truncated = primary_truncated or widened_truncated
        same_day_widened = bool(records)

    return records, primary_truncated, emitted_chars, same_day_widened


def collect_records(
    shards: list[Path],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    max_shard_bytes: int,
    *,
    session_id: str | None = None,
    lookback_minutes: int | None = None,
    allow_same_day_widening: bool = False,
) -> tuple[list[dict[str, Any]], list[str], bool, int, bool, dict[str, Any]]:
    entries, errors, truncated_by_limits = read_entries_from_shards(shards, max_shard_bytes)
    retrieval_metadata: dict[str, Any] = {
        "retrieval_mode": "raw-day-shard-scope",
        "preferred_retrieval_mode": None,
        "search_hits": 0,
        "expanded_chunks": 0,
        "fallback_used": False,
        "memsearch_error": None,
        "memsearch_collection": None,
        "source_prefix": None,
    }

    if session_id and len(shards) == 1:
        memsearch_records, memsearch_metadata = retrieve_memsearch_backed_session_records(
            shards[0],
            session_id,
            scope_filters,
            max_records,
            max_chars,
            lookback_minutes,
        )
        retrieval_metadata.update(memsearch_metadata)
        if memsearch_records:
            trace_records = with_source_classes(memsearch_records, "trace_evidence", "recall_evidence")
            retrieval_metadata["retrieval_mode"] = "memsearch-search-expand"
            emitted_chars = sum(len(record["content"]) for record in trace_records)
            return trace_records, errors, truncated_by_limits, emitted_chars, False, retrieval_metadata
        retrieval_metadata["fallback_used"] = True

    records, primary_truncated, emitted_chars, same_day_widened = collect_records_from_entries(
        entries,
        scope_filters,
        max_records,
        max_chars,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
        allow_same_day_widening=allow_same_day_widening,
    )
    truncated_by_limits = truncated_by_limits or primary_truncated
    trace_records = with_source_classes(records, "trace_evidence")
    if session_id:
        retrieval_metadata["retrieval_mode"] = "raw-same-day-widened" if same_day_widened else "raw-shard-session-filter"
    return trace_records, errors, truncated_by_limits, emitted_chars, same_day_widened, retrieval_metadata


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    memory_root_value, memory_root_source = resolve_memory_root(args)
    max_shards = clamp(args.max_shards, 1, 10)
    max_records = clamp(args.max_records, 1, 50)
    max_chars = clamp(args.max_chars, 256, 20000)
    max_shard_bytes = clamp(args.max_shard_bytes, 1024, 262144)
    max_age_days = max(0, args.max_age_days)
    scope_values = getattr(args, "scope", []) or []
    day_shard = getattr(args, "day", None)
    session_id = getattr(args, "session_id", None)
    allow_same_day_widening = getattr(args, "allow_same_day_widening", False)
    raw_lookback_minutes = getattr(args, "lookback_minutes", None)
    scope_filters = [scope.strip() for scope in scope_values if scope.strip()]
    lookback_minutes = None if raw_lookback_minutes is None else max(0, raw_lookback_minutes)
    active_scope_basis = scope_basis(args)
    project_dir = resolve_path(Path.cwd())
    source_policy_state = build_source_policy_state(
        args,
        project_dir=project_dir,
        scope_filters=scope_filters,
        active_scope_basis=active_scope_basis,
        max_shards=max_shards,
        day_shard=day_shard,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
    )
    allow_same_day_widening = source_policy_state["effective_same_day_widening"]
    effective_max_shards = int(source_policy_state["max_historical_shards"])

    if not memory_root_value:
        report = availability_report(
            memory_root=None,
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="unavailable-no-local-evidence",
            reason="No memory root was provided by --memory-root or supported environment variables.",
        )
        report["scope"].update(
            {
                "filters": scope_filters,
                "day_shard": day_shard,
                "session_id": session_id,
                "lookback_minutes": lookback_minutes,
                "same_day_widening_allowed": allow_same_day_widening,
            }
        )
        report["limits"] = {
            "max_shards": max_shards,
            "max_records": max_records,
            "max_chars": max_chars,
            "max_shard_bytes": max_shard_bytes,
        }
        report["freshness"]["max_age_days"] = max_age_days
        return report

    memory_root = Path(memory_root_value).expanduser()
    if not memory_root.is_dir():
        report = availability_report(
            memory_root=str(memory_root),
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="not-found-in-checked-scope",
            reason="The configured memory root does not exist or is not a directory.",
        )
        report["scope"].update(
            {
                "filters": scope_filters,
                "day_shard": day_shard,
                "session_id": session_id,
                "lookback_minutes": lookback_minutes,
                "same_day_widening_allowed": allow_same_day_widening,
            }
        )
        report["limits"] = {
            "max_shards": max_shards,
            "max_records": max_records,
            "max_chars": max_chars,
            "max_shard_bytes": max_shard_bytes,
        }
        report["freshness"]["max_age_days"] = max_age_days
        return report

    shards = discover_daily_shards(memory_root)
    selected_shards = select_daily_shards(shards, args, effective_max_shards)
    latest_shard = shards[0] if shards else None
    latest_date = parse_shard_date(latest_shard) if latest_shard else None
    latest_mtime = (
        datetime.fromtimestamp(latest_shard.stat().st_mtime).isoformat(timespec="seconds")
        if latest_shard
        else None
    )
    age_days = (date.today() - latest_date).days if latest_date else None
    freshness_classification = "unknown"
    if age_days is not None:
        freshness_classification = "stale" if age_days > max_age_days else "fresh"

    records, errors, truncated_by_limits, emitted_chars, same_day_widened, retrieval_metadata = collect_records(
        selected_shards,
        scope_filters,
        max_records,
        max_chars,
        max_shard_bytes,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
        allow_same_day_widening=allow_same_day_widening,
    )
    effective_source_classes = list(source_policy_state["effective_source_classes"])
    records = filter_records_for_source_policy(records, effective_source_classes)
    durable_memory_records = discover_durable_memory_context_records(
        project_dir,
        scope_filters,
        max_records=clamp(max_records, 1, 4),
        max_chars=min(max_chars, 480),
    )
    durable_memory_records = filter_records_for_source_policy(durable_memory_records, effective_source_classes)
    governance_records = discover_governance_context_records(
        project_dir,
        scope_filters,
        max_records=clamp(max_records, 1, 5),
        max_chars=min(max_chars, 520),
    )
    governance_records = filter_records_for_source_policy(governance_records, effective_source_classes)
    evidence_records = records + durable_memory_records + governance_records
    evidence_class_counts = source_class_counts(evidence_records)
    evidence_classes_present = source_classes_present(evidence_records)

    if not shards:
        status = "insufficient"
        evidence_strength = "insufficient-observed-local"
        reason = "The memory root is available, but no date-named markdown shards were discovered."
    elif day_shard and not selected_shards:
        status = "insufficient"
        evidence_strength = "insufficient-observed-local"
        reason = "The requested day shard was not found in the configured memory root."
    elif not records:
        status = "insufficient"
        evidence_strength = "insufficient-observed-local"
        if session_id and allow_same_day_widening:
            reason = "The current-session slice and same-day widening did not produce any bounded sample records for the requested scope."
        elif session_id:
            reason = "The current-session slice did not produce any bounded sample records for the requested scope."
        else:
            reason = "Daily shards were discovered, but no bounded sample records matched the requested scope."
    elif freshness_classification == "stale":
        status = "stale"
        evidence_strength = "observed-local-stale"
        reason = "The latest discovered daily shard is older than the configured freshness threshold."
    else:
        status = "available"
        evidence_strength = "observed-local-bounded"
        reason = "A bounded, privacy-minimized sample was retrieved from the configured memory root."

    notes = standard_notes(reason)
    notes.append(source_policy_state["policy_note"])
    if active_scope_basis == "historical-default":
        notes.append(
            "Historical-default scope is active; intake is reading a bounded recent cross-session shard set instead of narrowing to the current session."
        )
    if day_shard:
        notes.append(f"Selected day shard: {day_shard}.")
    elif selected_shards and (session_id or lookback_minutes is not None or allow_same_day_widening):
        notes.append(f"Selected current/latest day shard: {selected_shards[0].stem}.")
    if session_id:
        notes.append("Current-session scope was applied before deeper analysis.")
        if retrieval_metadata.get("retrieval_mode") == "memsearch-search-expand":
            notes.append("Current-session retrieval used memsearch search → expand before returning bounded records.")
        elif retrieval_metadata.get("fallback_used"):
            notes.append("Memsearch-backed current-session retrieval was unavailable or empty, so intake fell back to bounded raw day-shard filtering.")
        memsearch_error = retrieval_metadata.get("memsearch_error")
        if memsearch_error:
            notes.append(f"Memsearch retrieval note: {memsearch_error}")
    if lookback_minutes is not None:
        notes.append(f"Same-day lookback window applied: last {lookback_minutes} minute(s).")
    if same_day_widened:
        notes.append("Current-session slice was insufficient, so same-day widening was applied before returning records.")

    return {
        "tool": "memory-context-intelligence",
        "mode": "intake",
        "status": status,
        "evidence_strength": evidence_strength,
        "source": {
            "kind": "memsearch-daily-markdown-shards",
            "memory_root_source": memory_root_source,
            "memory_root": str(memory_root),
            "available": True,
            "daily_shards_discovered": len(shards),
            "daily_shards_considered": [path.name for path in selected_shards],
            "retrieval_mode": retrieval_metadata.get("retrieval_mode"),
            "preferred_retrieval_mode": retrieval_metadata.get("preferred_retrieval_mode"),
            "search_hits": retrieval_metadata.get("search_hits", 0),
            "expanded_chunks": retrieval_metadata.get("expanded_chunks", 0),
            "fallback_used": retrieval_metadata.get("fallback_used", False),
            "memsearch_error": retrieval_metadata.get("memsearch_error"),
            "memsearch_collection": retrieval_metadata.get("memsearch_collection"),
            "source_prefix": retrieval_metadata.get("source_prefix"),
            "source_classes_present": evidence_classes_present,
            "source_class_counts": evidence_class_counts,
            "policy_limited": source_policy_state["policy_limited"],
            "policy_note": source_policy_state["policy_note"],
        },
        "scope": {
            "basis": active_scope_basis,
            "filters": scope_filters,
            "day_shard": selected_shards[0].stem if len(selected_shards) == 1 else day_shard,
            "session_id": session_id,
            "lookback_minutes": lookback_minutes,
            "same_day_widening_allowed": allow_same_day_widening,
            "same_day_widened": same_day_widened,
            "historical_shards_considered": len(selected_shards),
            "bounded_subset_only": True,
        },
        "source_policy": source_policy_state,
        "freshness": {
            "latest_shard_date": latest_date.isoformat() if latest_date else None,
            "latest_shard_mtime": latest_mtime,
            "age_days": age_days,
            "max_age_days": max_age_days,
            "classification": freshness_classification,
        },
        "records": records,
        "evidence_records": evidence_records,
        "limits": {
            "max_shards": max_shards,
            "max_records": max_records,
            "max_chars": max_chars,
            "max_shard_bytes": max_shard_bytes,
            "emitted_chars": emitted_chars,
            "truncated_by_limits": truncated_by_limits,
        },
        "read_errors": errors,
        "notes": notes,
        "topic_generation_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    report = build_report(args)
    json.dump(report, fp=os.sys.stdout, ensure_ascii=False, indent=2)
    os.sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
