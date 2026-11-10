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
from itertools import zip_longest
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


def parse_day(value: str) -> str:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("day must use YYYY-MM-DD format") from exc
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("day must use YYYY-MM-DD format")
    return value


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
        "--older-than-day",
        type=parse_day,
        help="Select historical shards strictly older than this YYYY-MM-DD boundary.",
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
    parser.add_argument("--window-days", type=int, help="Optional calendar-day window, at most 14 days including current-day.")
    parser.add_argument("--current-day", type=parse_day, default=date.today().isoformat())
    parser.add_argument("--max-age-days", type=int, default=30, help="Freshness threshold for latest shard.")
    parser.add_argument("--progress-request", type=Path, help="MCI-owned bounded batch request; never writes progress.")
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
    older_than_day: str | None = None,
) -> bool:
    return bool(older_than_day or day_shard or session_id or lookback_minutes is not None or scope_filters)


def apply_config_default_scope(
    *,
    active_scope_basis: str,
    scope_filters: list[str],
    day_shard: str | None,
    session_id: str | None,
    lookback_minutes: int | None,
    scope_policy: dict[str, Any],
) -> tuple[str, str | None, str | None, int | None]:
    if explicit_narrow_request_active(
        day_shard=day_shard,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
        scope_filters=scope_filters,
    ):
        return active_scope_basis, day_shard, session_id, lookback_minutes

    mode = scope_policy.get("default_scope_mode")
    if mode == "day" and scope_policy.get("scope_day_shard"):
        return "config-default-day", str(scope_policy.get("scope_day_shard")), None, None
    if mode == "session" and scope_policy.get("scope_session_id"):
        return "config-default-session", None, str(scope_policy.get("scope_session_id")), None
    if mode == "lookback" and scope_policy.get("scope_lookback_minutes"):
        return "config-default-lookback", None, None, int(scope_policy.get("scope_lookback_minutes"))
    return "historical-default", day_shard, session_id, lookback_minutes


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
        older_than_day=getattr(args, "older_than_day", None),
    )
    requested_same_day_widening = bool(loaded_policy["requested_same_day_widening"])
    explicit_same_day_widening = bool(getattr(args, "allow_same_day_widening", False))
    effective_same_day_widening = explicit_same_day_widening or (requested_same_day_widening and not explicit_narrow)
    effective_max_historical_shards = max_shards
    if active_scope_basis in {"historical-default", "supplemental-historical-window"} and loaded_policy["max_historical_shards"] is not None:
        effective_max_historical_shards = min(max_shards, int(loaded_policy["max_historical_shards"]))

    limitation_notes: list[str] = []
    if loaded_policy["enabled_source_classes"] != list(SOURCE_CLASS_ORDER):
        limitation_notes.append(
            f"Config policy limited this run to {' + '.join(loaded_policy['enabled_source_classes'])}."
        )
    if active_scope_basis in {"historical-default", "supplemental-historical-window"} and loaded_policy["max_historical_shards"] is not None:
        scope_label = "Historical-default" if active_scope_basis == "historical-default" else "Supplemental historical"
        limitation_notes.append(
            f"{scope_label} shard selection was capped at {effective_max_historical_shards} shard(s)."
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
    records, sampling_limited, _ = flatten_entries(session_entries, scope_filters, max_records, max_chars)
    metadata["sampling_limited"] = sampling_limited
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
        "reason": reason,
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


def calendar_window(days: int, current_day: str) -> dict[str, Any]:
    if type(days) is not int or not 1 <= days <= 14:
        raise ValueError("Analysis window must be between 1 and 14 calendar days, including today.")
    end = date.fromisoformat(parse_day(current_day))
    return {"days": days, "start_day": (end - timedelta(days=days - 1)).isoformat(), "end_day": end.isoformat()}


def validate_calendar_scope(window: dict[str, Any], *, day: str | None = None, older_than_day: str | None = None) -> None:
    for value in [day, older_than_day]:
        if value is not None:
            if date.fromisoformat(value).isoformat() != value or not window["start_day"] <= value <= window["end_day"]:
                raise ValueError("Requested day or supplemental boundary is outside the selected calendar window.")


def discover_daily_shards(memory_root: Path, *, window: dict[str, Any] | None = None) -> list[Path]:
    return sorted(
        (
            path for path in memory_root.iterdir()
            if DAILY_SHARD_RE.fullmatch(path.name)
            and (window is None or window["start_day"] <= path.stem <= window["end_day"])
            and path.is_file()
        ),
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


def select_daily_shards(
    shards: list[Path],
    *,
    day_shard: str | None,
    session_id: str | None,
    lookback_minutes: int | None,
    allow_same_day_widening: bool,
    max_shards: int,
    older_than_day: str | None = None,
) -> list[Path]:
    if older_than_day:
        return [path for path in shards if path.stem < older_than_day][:max_shards]
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


def interleave_records(groups: list[list[dict[str, Any]]]) -> list[dict[str, Any]]:
    return [record for batch in zip_longest(*groups) for record in batch if record is not None]


def balanced_record_order(candidates: list[tuple[int, dict[str, Any]]]) -> list[dict[str, Any]]:
    days: dict[str, dict[str | None, dict[int, list[dict[str, Any]]]]] = {}
    for entry_index, record in candidates:
        sessions = days.setdefault(record["shard"], {})
        entries = sessions.setdefault(record["session_id"], {})
        entries.setdefault(entry_index, []).append(record)
    day_records: list[list[dict[str, Any]]] = []
    for sessions in days.values():
        session_records = [interleave_records(list(entries.values())) for entries in sessions.values()]
        day_records.append(interleave_records(session_records))
    return interleave_records(day_records)


def flatten_entries(
    entries: list[dict[str, Any]],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    *,
    balanced: bool = False,
) -> tuple[list[dict[str, Any]], bool, int]:
    candidates: list[tuple[int, dict[str, Any]]] = []
    normalized_filters = [item.lower() for item in scope_filters if item.strip()]
    for entry_index, entry in enumerate(entries):
        for bullet_index, bullet in enumerate(entry["bullet_lines"]):
            if normalized_filters and not any(scope in bullet.lower() for scope in normalized_filters):
                continue
            minimized = minimize_sensitive_content(bullet)
            if not minimized:
                continue
            candidates.append(
                (entry_index, {
                    "shard": entry["shard"],
                    "section": entry["section"],
                    "time": entry["time"],
                    "session_id": entry["session_id"],
                    "turn_id": entry["turn_id"],
                    "transcript": entry["transcript"],
                    "content": minimized,
                    "content_truncated": bool(entry.get("last_bullet_truncated") and bullet_index == len(entry["bullet_lines"]) - 1),
                })
            )
    ordered = balanced_record_order(candidates) if balanced else [record for _, record in candidates]
    selected = ordered[:max_records]
    records: list[dict[str, Any]] = []
    emitted_chars = 0
    truncated_by_limits = len(ordered) > len(selected)
    for index, record in enumerate(selected):
        remaining = max_chars - emitted_chars
        if remaining <= 0:
            truncated_by_limits = True
            break
        limit = remaining
        if balanced:
            # Reserve a fair share for later representatives, reclaiming their unused space.
            share = remaining // (len(selected) - index)
            reserve = sum(min(len(item["content"]), share) for item in selected[index + 1:])
            limit -= reserve
        if len(record["content"]) > limit:
            marker = "..."[:limit]
            record["content"] = record["content"][:limit - len(marker)].rstrip() + marker
            record["content_truncated"] = True
            truncated_by_limits = True
        records.append(record)
        emitted_chars += len(record["content"])
    return records, truncated_by_limits, emitted_chars


def read_entries_from_shards(
    shards: list[Path],
    max_shard_bytes: int,
) -> tuple[list[dict[str, Any]], list[str], bool, dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    errors: list[str] = []
    truncated_by_limits = False
    coverage: dict[str, Any] = {"read_days": [], "empty_days": [], "unreadable_days": [], "byte_truncated_days": []}

    for shard in shards:
        try:
            text, shard_truncated = read_bounded_text(shard, max_shard_bytes)
        except OSError as exc:
            errors.append(f"{shard.name}: {exc}")
            coverage["unreadable_days"].append(shard.stem)
            continue
        coverage["read_days"].append(shard.stem)
        shard_entries = parse_record_entries(shard, text)
        if not shard_entries:
            coverage["empty_days"].append(shard.stem)
        if shard_truncated:
            truncated_by_limits = True
            coverage["byte_truncated_days"].append(shard.stem)
            if shard_entries and not text.endswith("\n") and text.splitlines()[-1].strip().startswith("- "):
                shard_entries[-1]["last_bullet_truncated"] = True
        entries.extend(shard_entries)

    return entries, errors, truncated_by_limits, coverage


def collect_records_from_entries(
    entries: list[dict[str, Any]],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    *,
    session_id: str | None = None,
    lookback_minutes: int | None = None,
    allow_same_day_widening: bool = False,
    balanced: bool = False,
) -> tuple[list[dict[str, Any]], bool, int, bool]:
    primary_entries = list(entries)
    if session_id:
        primary_entries = [entry for entry in primary_entries if entry.get("session_id") == session_id]
    primary_entries = filter_entries_by_lookback(primary_entries, lookback_minutes)
    records, primary_truncated, emitted_chars = flatten_entries(primary_entries, scope_filters, max_records, max_chars, balanced=balanced)

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
    balanced: bool = False,
) -> tuple[list[dict[str, Any]], list[str], bool, int, bool, dict[str, Any]]:
    entries, errors, truncated_by_limits, read_coverage = read_entries_from_shards(shards, max_shard_bytes)
    retrieval_metadata: dict[str, Any] = {
        "retrieval_mode": "raw-day-shard-scope",
        "coverage": read_coverage,
        "sampling_limited": False,
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
            truncated_by_limits = truncated_by_limits or bool(retrieval_metadata["sampling_limited"])
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
        balanced=balanced,
    )
    truncated_by_limits = truncated_by_limits or primary_truncated
    retrieval_metadata["sampling_limited"] = primary_truncated
    trace_records = with_source_classes(records, "trace_evidence")
    if session_id:
        retrieval_metadata["retrieval_mode"] = "raw-same-day-widened" if same_day_widened else "raw-shard-session-filter"
    return trace_records, errors, truncated_by_limits, emitted_chars, same_day_widened, retrieval_metadata


def prefix_digest(path: Path, size: int) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        remaining = size
        while remaining:
            block = handle.read(min(65536, remaining))
            if not block:
                raise ValueError("source-changed: input was shortened before its bound endpoint.")
            digest.update(block)
            remaining -= len(block)
    return digest.hexdigest()


def progressive_endpoint(shards: list[Path]) -> dict[str, Any]:
    endpoint: dict[str, Any] = {}
    for path in sorted(shards):
        if path.is_symlink() or not DAILY_SHARD_RE.fullmatch(path.name):
            raise ValueError("Progressive input must be a regular date-named shard.")
        size = path.stat().st_size
        endpoint[path.name] = {"size": size, "digest": prefix_digest(path, size)}
    return endpoint


def validate_progressive_source(binding: dict[str, Any]) -> None:
    root = Path(binding["memory_root"])
    for name, bound in binding["prefixes"].items():
        if not DAILY_SHARD_RE.fullmatch(name) or (root / name).is_symlink():
            raise ValueError("source-changed: unsafe shard identity.")
        if prefix_digest(root / name, bound["offset"]) != bound["prefix_digest"]:
            raise ValueError("source-changed: acknowledged input was rewritten; progress was preserved.")


def collect_progressive_records(
    shards: list[Path],
    scope_filters: list[str],
    max_records: int,
    max_chars: int,
    max_shard_bytes: int,
    *,
    checkpoint: dict[str, Any] | None,
    endpoint: dict[str, Any] | None = None,
    max_shards: int = 10,
) -> dict[str, Any]:
    if scope_filters:
        raise ValueError("Filtered inspection cannot consume incremental progress.")
    paths = {path.name: path for path in shards}
    endpoint = progressive_endpoint(shards) if endpoint is None else endpoint
    completed = dict((checkpoint or {}).get("completed", {}))
    for name, bound in completed.items():
        if name not in paths or type(bound.get("offset")) is not int or bound["offset"] < 0:
            raise ValueError("source-changed: checkpoint source is missing or invalid.")
        if prefix_digest(paths[name], bound["offset"]) != bound.get("prefix_digest"):
            raise ValueError("source-changed: checkpoint prefix was rewritten.")
    records: list[dict[str, Any]] = []
    chars = 0
    selected: list[str] = []
    byte_limited: list[str] = []
    reason = None
    next_position = dict(checkpoint) if checkpoint else None
    for name, end in sorted(endpoint.items()):
        if name not in paths or not DAILY_SHARD_RE.fullmatch(name):
            raise ValueError("source-changed: snapshot source is missing.")
        path = paths[name]
        if type(end.get("size")) is not int or end["size"] < 0 or path.is_symlink():
            raise ValueError("source-changed: invalid snapshot.")
        if prefix_digest(path, end["size"]) != end.get("digest"):
            raise ValueError("source-changed: snapshot input was rewritten.")
        prior = completed.get(name, {})
        offset = prior.get("offset", 0)
        if offset > end["size"]:
            raise ValueError("Stale endpoint precedes completed progress.")
        if offset == end["size"] and name in completed:
            continue
        if len(selected) >= max_shards or len(records) >= max_records:
            break
        selected.append(name)
        heading = ""
        anchor = ""
        record_key = prior.get("record_key")
        consumed = offset
        read_digest = hashlib.sha256()
        with path.open("rb") as handle:
            # Reconstruct parser context without persisting transcript paths or raw text.
            while handle.tell() < offset:
                line = handle.readline(min(262145, offset - handle.tell()))
                if len(line) > 262144 or not line:
                    raise ValueError("Checkpoint parser context exceeds its bounds or source was shortened.")
                read_digest.update(line)
                text = line.decode("utf-8").strip()
                if text.startswith("### "):
                    heading, anchor = text, ""
                elif ANCHOR_RE.search(text):
                    anchor = text
            if prior and read_digest.hexdigest() != prior["prefix_digest"]:
                raise ValueError("source-changed: parsed cursor context was rewritten.")
            while handle.tell() < end["size"]:
                start = handle.tell()
                remaining = min(end["size"] - start, max_shard_bytes - (start - offset))
                if remaining <= 0:
                    byte_limited.append(path.stem)
                    break
                line = handle.readline(remaining)
                if not line.endswith(b"\n"):
                    byte_limited.append(path.stem)
                    reason = "Partial or oversized line remains unprocessed; finish the append or increase the byte budget."
                    break
                text = line.decode("utf-8").strip()
                if text.startswith("### "):
                    heading, anchor = text, ""
                elif ANCHOR_RE.search(text):
                    anchor = text
                elif text.startswith("- "):
                    entries = parse_record_entries(path, "\n".join([heading, anchor, text]))
                    record = entries[0]
                    content = minimize_sensitive_content(text[2:])
                    if len(records) >= max_records or chars + len(content) > max_chars:
                        if not records:
                            reason = "One record exceeds the character budget; increase the budget before acknowledging it."
                        break
                    record_key = hashlib.sha256(json.dumps([
                        name, record["session_id"], record["turn_id"], record["section"],
                        start, hashlib.sha256(line).hexdigest(),
                    ], ensure_ascii=False).encode()).hexdigest()
                    if content:
                        records.append({
                            key: record[key] for key in ["shard", "section", "time", "session_id", "turn_id", "transcript"]
                        })
                        records[-1].update({
                            "content": content, "content_truncated": False,
                            "source_position": {"shard": name, "offset": handle.tell(), "record_key": record_key},
                        })
                        chars += len(content)
                read_digest.update(line)
                consumed = handle.tell()
                if len(records) >= max_records:
                    break
        if consumed != offset or end["size"] == 0:
            completed[name] = {
                "offset": consumed, "prefix_digest": read_digest.hexdigest(), "record_key": record_key,
            }
            next_position = {"shard": name, "completed": dict(completed)}
        if consumed < end["size"] or len(records) >= max_records:
            break
    remaining = any(completed.get(name, {}).get("offset", -1) < end["size"] for name, end in endpoint.items())
    complete = bool(records) or (next_position != checkpoint and not byte_limited and reason is None)
    return {
        "records": records, "next_position": next_position, "endpoint": endpoint,
        "remaining": remaining, "reason": reason,
        "coverage": {
            "complete": complete, "selected_days": [Path(name).stem for name in selected],
            "read_days": [Path(name).stem for name in selected],
            "sampled_days": list(dict.fromkeys(Path(record["shard"]).stem for record in records)),
            "empty_days": [], "unreadable_days": [], "byte_truncated_days": byte_limited,
            "byte_limited_days": byte_limited, "bounded_sample_only": False,
            "sampling_limited": False, "content_truncated_refs": [], "unsampled_days": [],
            "contiguous_batch_only": True, "remaining_unprocessed": remaining,
        },
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    memory_root_value, memory_root_source = resolve_memory_root(args)
    max_shards = clamp(args.max_shards, 1, 10)
    max_records = clamp(args.max_records, 1, 50)
    max_chars = clamp(args.max_chars, 256, 20000)
    max_shard_bytes = clamp(args.max_shard_bytes, 1024, 262144)
    max_age_days = max(0, args.max_age_days)
    scope_values = getattr(args, "scope", []) or []
    day_shard = getattr(args, "day", None)
    older_than_day = getattr(args, "older_than_day", None)
    session_id = getattr(args, "session_id", None)
    allow_same_day_widening = getattr(args, "allow_same_day_widening", False)
    raw_lookback_minutes = getattr(args, "lookback_minutes", None)
    scope_filters = [scope.strip() for scope in scope_values if scope.strip()]
    lookback_minutes = None if raw_lookback_minutes is None else max(0, raw_lookback_minutes)
    active_scope_basis = "supplemental-historical-window" if older_than_day else scope_basis(args)
    if older_than_day and day_shard:
        return availability_report(
            memory_root=memory_root_value,
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="not-found-in-checked-scope",
            reason="--older-than-day cannot be combined with --day.",
        )
    if older_than_day and (session_id or lookback_minutes is not None or scope_filters):
        return availability_report(
            memory_root=memory_root_value,
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="not-found-in-checked-scope",
            reason="Supplemental historical search cannot widen or combine with an explicitly narrowed scope.",
        )
    project_dir = resolve_path(Path.cwd())
    stored_policy = load_analysis_source_policy(
        explicit_config_path=getattr(args, "config", None),
        cwd=project_dir,
    )
    stored_scope_policy = stored_policy.get("scope_policy", {})
    if older_than_day and stored_scope_policy.get("default_scope_mode") in {"day", "session", "lookback"}:
        return availability_report(
            memory_root=memory_root_value,
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="not-found-in-checked-scope",
            reason="Supplemental historical search is unavailable under the configured narrow scope; explicitly select a historical scope first.",
        )
    if not older_than_day:
        active_scope_basis, day_shard, session_id, lookback_minutes = apply_config_default_scope(
            active_scope_basis=active_scope_basis,
            scope_filters=scope_filters,
            day_shard=day_shard,
            session_id=session_id,
            lookback_minutes=lookback_minutes,
            scope_policy=stored_scope_policy,
        )
    window = None
    try:
        if getattr(args, "window_days", None) is not None:
            window = calendar_window(args.window_days, args.current_day)
            validate_calendar_scope(window, day=day_shard, older_than_day=older_than_day)
    except ValueError as exc:
        report = availability_report(
            memory_root=memory_root_value, memory_root_source=memory_root_source,
            status="unavailable", evidence_strength="not-found-in-checked-scope", reason=str(exc),
        )
        report["scope"]["calendar_window"] = window
        return report
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

    shards = discover_daily_shards(memory_root, window=window)
    if older_than_day and "trace_evidence" not in source_policy_state["effective_source_classes"]:
        report = availability_report(
            memory_root=str(memory_root),
            memory_root_source=memory_root_source,
            status="unavailable",
            evidence_strength="not-found-in-checked-scope",
            reason="Supplemental historical search is unavailable because source policy disables trace_evidence.",
        )
        report["source"]["available"] = True
        report["source"]["daily_shards_discovered"] = len(shards)
        report["scope"]["basis"] = active_scope_basis
        report["source_policy"] = source_policy_state
        report["scope_policy"] = stored_scope_policy
        report["limits"] = {
            "max_shards": max_shards,
            "max_records": max_records,
            "max_chars": max_chars,
            "max_shard_bytes": max_shard_bytes,
        }
        report["freshness"]["max_age_days"] = max_age_days
        return report

    progress_request = getattr(args, "progress_request", None)
    progressive_batch = None
    if progress_request:
        try:
            if active_scope_basis != "historical-default" or older_than_day or scope_filters or day_shard or session_id or lookback_minutes is not None:
                raise ValueError("Narrowed inspection cannot consume incremental progress.")
            if "trace_evidence" not in source_policy_state["effective_source_classes"] or source_policy_state.get("errors"):
                raise ValueError("Incremental progress requires a valid trace-enabled source policy.")
            with Path(progress_request).open("rb") as handle:
                request_bytes = handle.read(1048577)
            if len(request_bytes) > 1048576:
                raise ValueError("Progress request exceeds its bounded size.")
            request = json.loads(request_bytes)
            progressive_batch = collect_progressive_records(
                shards, [], max_records, max_chars, max_shard_bytes,
                checkpoint=request.get("checkpoint"), endpoint=request["endpoint"],
                max_shards=effective_max_shards,
            )
        except (OSError, ValueError, KeyError, TypeError) as exc:
            return availability_report(
                memory_root=str(memory_root), memory_root_source=memory_root_source,
                status="unavailable", evidence_strength="unavailable-incremental-input",
                reason=str(exc),
            )
    balanced_sampling = not progress_request and active_scope_basis in {"historical-default", "supplemental-historical-window"} and not (
        scope_filters or day_shard or session_id or lookback_minutes is not None
    )
    if balanced_sampling:
        effective_max_shards = min(effective_max_shards, max_records)
    selected_shards = select_daily_shards(
        shards,
        day_shard=day_shard,
        session_id=session_id,
        lookback_minutes=lookback_minutes,
        allow_same_day_widening=allow_same_day_widening,
        max_shards=effective_max_shards,
        older_than_day=older_than_day,
    )
    latest_shard = selected_shards[0] if older_than_day and selected_shards else (shards[0] if shards else None)
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

    if progressive_batch is None:
        records, errors, truncated_by_limits, emitted_chars, same_day_widened, retrieval_metadata = collect_records(
            selected_shards,
            scope_filters,
            max_records,
            max_chars,
            max_shard_bytes,
            session_id=session_id,
            lookback_minutes=lookback_minutes,
            allow_same_day_widening=allow_same_day_widening,
            balanced=balanced_sampling,
        )
    else:
        records = progressive_batch["records"]
        selected_shards = [memory_root / f"{day}.md" for day in progressive_batch["coverage"]["selected_days"]]
        errors, same_day_widened = [], False
        truncated_by_limits = progressive_batch["remaining"]
        emitted_chars = sum(len(record["content"]) for record in records)
        retrieval_metadata = {
            "coverage": progressive_batch["coverage"], "sampling_limited": False,
            "retrieval_mode": "raw-ordered-incremental", "fallback_used": False,
        }
    effective_source_classes = list(source_policy_state["effective_source_classes"])
    records = filter_records_for_source_policy(records, effective_source_classes)
    for index, record in enumerate(records, start=1):
        if "trace_evidence" in record["source_classes"]:
            record["ref"] = f"excerpt-{index:03d}"
    selected_days = [path.stem for path in selected_shards]
    sampled_days = list(dict.fromkeys(Path(record["shard"]).stem for record in records))
    coverage = dict(retrieval_metadata["coverage"])
    coverage.update({
        "selected_days": selected_days,
        "sampled_days": sampled_days,
        "unsampled_days": [day for day in coverage["read_days"] if day not in sampled_days and day not in coverage["empty_days"]],
        "sampling_limited": retrieval_metadata["sampling_limited"],
        "content_truncated_refs": [record["ref"] for record in records if record.get("ref") and record.get("content_truncated")],
        "bounded_sample_only": progressive_batch is None,
    })
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
    elif older_than_day and not selected_shards:
        status = "insufficient"
        evidence_strength = "insufficient-observed-local"
        reason = "No daily shards exist strictly older than the requested supplemental boundary."
    elif not records:
        status = "insufficient"
        evidence_strength = "insufficient-observed-local"
        if session_id and allow_same_day_widening:
            reason = "The current-session slice and same-day widening did not produce any bounded sample records for the requested scope."
        elif session_id:
            reason = "The current-session slice did not produce any bounded sample records for the requested scope."
        else:
            reason = "Daily shards were discovered, but no bounded sample records matched the requested scope."
    elif freshness_classification == "stale" and not older_than_day and progressive_batch is None:
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
            "calendar_window": window,
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
        "scope_policy": stored_scope_policy,
        "coverage": coverage,
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
        **({"progressive_batch": progressive_batch} if progressive_batch is not None else {}),
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    report = build_report(args)
    json.dump(report, fp=os.sys.stdout, ensure_ascii=False, indent=2)
    os.sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
