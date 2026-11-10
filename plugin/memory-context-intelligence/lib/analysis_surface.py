from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import tempfile
import uuid
from datetime import date, datetime
from pathlib import Path
from typing import Any

LIB_DIR = Path(__file__).resolve().parent
if str(LIB_DIR) not in os.sys.path:
    os.sys.path.insert(0, str(LIB_DIR))

from config_policy import build_guided_config_questions, load_analysis_source_policy
from orchestration import build_adaptive_deepening_plan
from analysis_checkpoint import CheckpointConflict, default_state_path, load_progress, prepare_batch, scope_identity
from intake import apply_config_default_scope, calendar_window, discover_daily_shards, progressive_endpoint, validate_calendar_scope

REGISTERED_OPERATOR_SURFACE = "/memory-context-intelligence:analysis"
RUNTIME_PROOF_NOTE = "not proved in checked current print-mode runtime"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_BIN = (PACKAGE_ROOT / "bin" / "memory-context-intelligence").resolve()


def parse_day(value: str) -> str:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("day must use YYYY-MM-DD format") from exc
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("day must use YYYY-MM-DD format")
    return value


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="memory-context-intelligence analysis-surface")
    parser.add_argument("--arguments", default=os.environ.get("ARGUMENTS", ""))
    parser.add_argument("--startup", action="store_true", help="Fileless discovery only; caller binds slash arguments before intake.")
    parser.add_argument("--session-id", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    parser.add_argument("--window-days", type=int, help="Selected calendar-day window, from 1 through 14 including current-day.")
    parser.add_argument("--current-day", type=parse_day, default=date.today().isoformat())
    parser.add_argument("--config", help="Use the same explicit source-policy config as the analysis window.")
    parser.add_argument("--mode", choices=["incremental", "catch-up"], default="incremental")
    parser.add_argument("--continue-run", help="Continue only after acknowledging the preceding batch of this catch-up run.")
    parser.add_argument("--state", type=Path, default=default_state_path())
    parser.add_argument("--max-records", type=int, default=8)
    parser.add_argument("--max-chars", type=int, default=6000)
    parser.add_argument("--max-shard-bytes", type=int, default=65536)
    parser.add_argument(
        "--older-than-day",
        type=parse_day,
        help="Run one bounded historical window strictly older than this day.",
    )
    return parser.parse_args(argv)


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def topic_discovery_evidence(intake: dict[str, Any]) -> list[dict[str, Any]]:
    excerpts: list[dict[str, Any]] = []
    records = intake.get("records")
    if not isinstance(records, list):
        return excerpts
    remaining = min(20000, max(0, int((intake.get("limits") or {}).get("max_chars", 6000))))
    for record in records:
        if not isinstance(record, dict):
            continue
        source_classes = record.get("source_classes")
        if not isinstance(source_classes, list) or "trace_evidence" not in source_classes:
            continue
        content = str(record.get("content") or "").strip()
        ref = record.get("ref")
        if not content or not ref:
            continue
        if remaining <= 0 or len(excerpts) >= 50:
            break
        content_truncated = bool(record.get("content_truncated"))
        if len(content) > remaining:
            marker = "..."[:remaining]
            content = content[:remaining - len(marker)].rstrip() + marker
            content_truncated = True
        excerpts.append({"ref": ref, "content": content, "content_truncated": content_truncated})
        remaining -= len(content)
    return excerpts


def find_memory_root(cwd: Path) -> Path | None:
    for base in [cwd, *cwd.parents]:
        candidate = base / ".memsearch" / "memory"
        if candidate.is_dir():
            return candidate
    return None


def parse_scope_and_narrowing(text: str) -> tuple[str | None, int | None, str | None, str | None, str | None]:
    lookback_minutes = None
    explicit_day = None
    explicit_session_id = None
    explicit_config_path = None
    if not text:
        return None, lookback_minutes, explicit_day, explicit_session_id, explicit_config_path
    try:
        tokens = shlex.split(text)
    except ValueError:
        tokens = text.split()
    scope_tokens: list[str] = []
    for token in tokens:
        lookback_match = re.fullmatch(r"(?:lookback|window)=(\d+)([mh])", token, re.IGNORECASE)
        if lookback_match:
            amount = int(lookback_match.group(1))
            unit = lookback_match.group(2).lower()
            lookback_minutes = amount * 60 if unit == "h" else amount
            continue
        day_match = re.fullmatch(r"day=(\d{4}-\d{2}-\d{2})", token)
        if day_match:
            explicit_day = day_match.group(1)
            continue
        session_match = re.fullmatch(r"session=(\S+)", token)
        if session_match:
            explicit_session_id = session_match.group(1)
            continue
        config_match = re.fullmatch(r"config=(\S+)", token)
        if config_match:
            explicit_config_path = config_match.group(1)
            continue
        scope_tokens.append(token)
    scope_text = " ".join(scope_tokens).strip()
    return scope_text or None, lookback_minutes, explicit_day, explicit_session_id, explicit_config_path


def analysis_window_report(
    intake: dict[str, Any],
    *,
    supplemental: bool,
    exclusive_boundary_day: str | None = None,
    pass_attempted: bool = False,
    pass_used: bool = False,
) -> dict[str, Any]:
    scope_report = intake.get("scope", {})
    source_report = intake.get("source", {})
    source_policy = intake.get("source_policy") or {}
    shard_names = source_report.get("daily_shards_considered") or []
    checked_days = [Path(str(name)).stem for name in shard_names if str(name)]
    basis = str(scope_report.get("basis") or "unknown")
    narrowed = bool(
        scope_report.get("filters")
        or (scope_report.get("day_shard") and basis != "historical-default")
        or scope_report.get("session_id")
        or scope_report.get("lookback_minutes") is not None
    )
    trace_enabled = "trace_evidence" in (source_policy.get("effective_source_classes") or [])
    can_continue = (
        basis == "historical-default"
        and bool(checked_days)
        and not narrowed
        and trace_enabled
        and not supplemental
    )
    report = {
        "mode": "supplemental-historical-window" if supplemental else (basis if not narrowed else "explicitly-narrowed"),
        "checked_days": checked_days,
        "next_older_than_day": min(checked_days) if can_continue else None,
        "supplemental_pass_used": pass_used,
    }
    if isinstance(intake.get("coverage"), dict):
        report["coverage"] = intake["coverage"]
    if supplemental:
        report["exclusive_boundary_day"] = exclusive_boundary_day
        report["supplemental_intake_status"] = intake.get("status")
        report["supplemental_pass_attempted"] = pass_attempted
    return report


def blocked_payload(
    reason: str,
    memory_root: Path | None,
    scope_text: str | None,
    *,
    supplemental_boundary: str | None = None,
    supplemental_intake: dict[str, Any] | None = None,
    supplemental_pass_attempted: bool = False,
    **extra: Any,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
        "bare_alias_runtime_proof": RUNTIME_PROOF_NOTE,
        "analysis_request_present": True,
        "invocation_mode": "standalone-analysis-slash",
        "render_required_now": True,
        "generic_no_request_response_allowed": False,
        "status": "blocked",
        "reason": reason,
        "memory_root": None if memory_root is None else str(memory_root),
        "scope_filter": scope_text or None,
        "topic_list": [],
    }
    payload.update(extra)
    if supplemental_boundary:
        payload["analysis_window"] = analysis_window_report(
            supplemental_intake or {},
            supplemental=True,
            exclusive_boundary_day=supplemental_boundary,
            pass_attempted=supplemental_pass_attempted,
            pass_used=bool(supplemental_intake and supplemental_intake.get("status") != "unavailable"),
        )
    return payload


def run_json_command(command: list[str]) -> tuple[subprocess.CompletedProcess[str], dict[str, Any] | None]:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return result, None
    return result, json.loads(result.stdout)


def field_value(topic: dict[str, Any], key: str) -> Any:
    for field in topic.get("fields", []):
        if field.get("key") == key:
            return field.get("value")
    return None


def parse_iso_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def read_first_timestamp_from_transcript(transcript_path: Path, *, max_lines: int = 20) -> str | None:
    if not transcript_path.is_file():
        return None
    with transcript_path.open("r", encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            if index >= max_lines:
                break
            line = line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                continue
            timestamp = payload.get("timestamp")
            if isinstance(timestamp, str) and timestamp:
                return timestamp
    return None


def contains_thai_characters(text: str) -> bool:
    return bool(re.search(r"[฀-๿]", text))


def read_recent_user_texts_from_transcript(
    transcript_path: Path | None, *, max_bytes: int = 262144, max_messages: int = 12
) -> list[str]:
    if transcript_path is None or not transcript_path.is_file():
        return []

    with transcript_path.open("rb") as handle:
        handle.seek(0, 2)
        size = handle.tell()
        read_size = min(size, max_bytes)
        handle.seek(max(0, size - read_size))
        blob = handle.read().decode("utf-8", errors="ignore")

    texts: list[str] = []
    for line in reversed(blob.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if payload.get("type") != "user":
            continue
        message = payload.get("message")
        if not isinstance(message, dict) or message.get("role") != "user":
            continue
        content = message.get("content")
        text = ""
        if isinstance(content, str):
            text = content.strip()
        elif isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, str) and item.strip():
                    parts.append(item.strip())
                    continue
                if not isinstance(item, dict):
                    continue
                if item.get("type") == "text" and isinstance(item.get("text"), str) and item.get("text").strip():
                    parts.append(item.get("text").strip())
            text = " ".join(parts).strip()
        if not text:
            continue
        texts.append(text)
        if len(texts) >= max_messages:
            break
    texts.reverse()
    return texts


def infer_presentation_language(arguments: str, transcript_path: Path | None) -> str:
    if contains_thai_characters(arguments):
        return "th"
    for text in reversed(read_recent_user_texts_from_transcript(transcript_path)):
        if contains_thai_characters(text):
            return "th"
    return "th"


def resolve_transcript_path(session_id: str | None) -> Path | None:
    override = os.environ.get("CLAUDE_CODE_TRANSCRIPT_PATH")
    if override:
        candidate = Path(override)
        if candidate.is_file():
            return candidate
    if not session_id:
        return None
    projects_root = Path.home() / ".claude" / "projects"
    if not projects_root.is_dir():
        return None
    matches = list(projects_root.rglob(f"{session_id}.jsonl"))
    if len(matches) == 1:
        return matches[0]
    return None


def select_installed_plugin_record(cwd: Path) -> dict[str, Any] | None:
    registry_path = Path.home() / ".claude" / "plugins" / "installed_plugins.json"
    if not registry_path.is_file():
        return None
    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    records = payload.get("plugins", {}).get("memory-context-intelligence@darkwingtm")
    if not isinstance(records, list) or not records:
        return None

    cwd_text = str(cwd.resolve())
    best_record: dict[str, Any] | None = None
    best_score: tuple[int, int] | None = None
    for record in records:
        if not isinstance(record, dict):
            continue
        scope = str(record.get("scope") or "")
        project_path = str(record.get("projectPath") or "")
        prefix_match = 0
        if project_path:
            try:
                project_text = str(Path(project_path).resolve())
            except OSError:
                project_text = project_path
            if cwd_text == project_text or cwd_text.startswith(project_text + os.sep):
                prefix_match = len(project_text)
        score = (1 if scope == "local" else 0, prefix_match)
        if best_score is None or score > best_score:
            best_record = record
            best_score = score
    return best_record


def build_operator_warnings(*, cwd: Path, session_id: str | None) -> list[dict[str, Any]]:
    transcript_path = resolve_transcript_path(session_id)
    transcript_first_timestamp = read_first_timestamp_from_transcript(transcript_path) if transcript_path else None
    plugin_record = select_installed_plugin_record(cwd)
    plugin_last_updated = None if plugin_record is None else plugin_record.get("lastUpdated")
    session_dt = parse_iso_timestamp(transcript_first_timestamp)
    plugin_dt = parse_iso_timestamp(plugin_last_updated if isinstance(plugin_last_updated, str) else None)
    if session_dt is None or plugin_dt is None or plugin_record is None or session_dt >= plugin_dt:
        return []

    return [
        {
            "type": "stale_long_lived_session",
            "severity": "advisory",
            "message": "Possible stale long-lived session: this session started before the installed plugin was updated. If slash behavior still differs from the installed source, restart this session and retry. This is a temporary diagnostic safeguard only; session-dependent no-response remains a bug, not acceptable normal behavior.",
            "session_id": session_id,
            "session_first_timestamp": transcript_first_timestamp,
            "plugin_version": plugin_record.get("version"),
            "plugin_last_updated": plugin_last_updated,
            "install_path": plugin_record.get("installPath"),
            "checked_scope": "transcript freshness compared with installed local plugin metadata",
        }
    ]


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    cwd = Path.cwd()
    if not args.startup and args.window_days is None:
        emit({
            "status": "awaiting-caller-scope", "analysis_request_present": True,
            "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
            "preparation_command": shlex.join([str(RUNTIME_BIN), "analysis-surface"]),
            "window_choices": [1, 3, 7, 14], "checkpoint_advanced": False,
            "reason": "Caller must resolve the calendar window and any missing topic target before preparation.",
        })
        return 0
    window = None
    if not args.startup:
        try:
            window = calendar_window(args.window_days, args.current_day)
        except ValueError as exc:
            emit(blocked_payload(str(exc), None, None))
            return 0

    def emit_result(payload: dict[str, Any]) -> None:
        report = payload.setdefault("analysis_window", {})
        report["calendar_window"] = window
        if report.get("next_older_than_day") and report["next_older_than_day"] <= window["start_day"]:
            report["next_older_than_day"] = None
        emit(payload)

    memory_root = find_memory_root(cwd)
    if args.startup:
        if memory_root is None:
            emit(blocked_payload("No project-scoped .memsearch/memory root was found from the current working directory upward.", None, None))
        else:
            emit({
                "status": "awaiting-caller-scope", "analysis_request_present": True,
                "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
                "preparation_command": shlex.join([str(RUNTIME_BIN), "analysis-surface"]),
                "checkpoint_advanced": False,
                "reason": "Caller must bind the supplied slash arguments before preparing evidence; startup reads no corpus or progress.",
            })
        return 0
    argument_text = str(args.arguments or "").strip()
    mode_tokens = re.findall(r"(?:^|\s)mode=([^\s]+)", argument_text)
    if mode_tokens and (len(mode_tokens) != 1 or mode_tokens[0] not in {"incremental", "catch-up"}):
        emit_result(blocked_payload("mode must be incremental or catch-up.", memory_root, None))
        return 0
    if mode_tokens:
        args.mode = mode_tokens[0]
        argument_text = re.sub(r"(?:^|\s)mode=[^\s]+", "", argument_text).strip()
    scope_text, lookback_minutes, explicit_day, explicit_session_id, argument_config_path = parse_scope_and_narrowing(argument_text)
    explicit_config_path = args.config or argument_config_path
    try:
        validate_calendar_scope(window, day=explicit_day, older_than_day=args.older_than_day)
    except ValueError as exc:
        emit_result(blocked_payload(str(exc), memory_root, scope_text))
        return 0
    if args.older_than_day and (explicit_day or explicit_session_id or lookback_minutes is not None or scope_text):
        emit_result(
            blocked_payload(
                "Supplemental historical search cannot widen an explicitly narrowed analysis scope.",
                None,
                scope_text,
                supplemental_boundary=args.older_than_day,
                supplemental_intake=None,
                supplemental_pass_attempted=False,
            )
        )
        return 0

    if memory_root is None:
        emit_result(
            blocked_payload(
                "No project-scoped .memsearch/memory root was found from the current working directory upward.",
                None,
                scope_text,
            )
        )
        return 0

    policy = load_analysis_source_policy(explicit_config_path=explicit_config_path, cwd=cwd)
    _, configured_day, _, _ = apply_config_default_scope(
        active_scope_basis="historical-default", scope_filters=[scope_text] if scope_text else [],
        day_shard=explicit_day, session_id=explicit_session_id, lookback_minutes=lookback_minutes,
        scope_policy=policy["scope_policy"],
    )
    try:
        validate_calendar_scope(window, day=configured_day)
    except ValueError as exc:
        emit_result(blocked_payload(str(exc), memory_root, scope_text))
        return 0
    narrow = bool(scope_text or explicit_day or explicit_session_id or lookback_minutes is not None or args.older_than_day)
    narrow = narrow or policy["scope_policy"]["default_scope_mode"] in {"day", "session", "lookback"}
    progressive = not narrow and "trace_evidence" in policy["enabled_source_classes"]
    if (args.continue_run or args.mode == "catch-up") and not progressive:
        emit_result(blocked_payload("Catch-up cannot widen narrow or trace-disabled inspection.", memory_root, scope_text))
        return 0
    progress_context = None
    if progressive and memory_root.is_dir():
        try:
            if policy["errors"]:
                raise CheckpointConflict("Source policy could not be read; progress was preserved.")
            scope_key = scope_identity(memory_root, policy["enabled_source_classes"], window=window)
            entry = load_progress(args.state, scope_key)
            if args.continue_run:
                last = entry.get("last_completed") or {}
                if entry["pending"] or last.get("run_id") != args.continue_run or last.get("mode") != "catch-up":
                    raise CheckpointConflict("Catch-up requires acknowledged progress from the same run.")
                endpoint = last["endpoint"]
                run_id, mode = args.continue_run, "catch-up"
            else:
                endpoint = progressive_endpoint(discover_daily_shards(memory_root, window=window))
                run_id, mode = uuid.uuid4().hex, args.mode
            progress_context = {
                "scope_key": scope_key, "entry": entry, "endpoint": endpoint,
                "run_id": run_id, "mode": mode,
            }
        except (CheckpointConflict, OSError, ValueError) as exc:
            emit_result(blocked_payload(str(exc), memory_root, scope_text))
            return 0
    base = Path(tempfile.mkdtemp(prefix="mci-analysis-"))

    cmd_intake = [
        "bash",
        str(RUNTIME_BIN),
        "intake",
        "--memory-root",
        str(memory_root),
        "--window-days", str(args.window_days), "--current-day", args.current_day,
    ]
    if args.older_than_day:
        cmd_intake += ["--older-than-day", args.older_than_day]
    if explicit_config_path:
        cmd_intake += ["--config", explicit_config_path]
    if explicit_day:
        cmd_intake += ["--day", explicit_day]
    if explicit_session_id:
        cmd_intake += ["--session-id", explicit_session_id]
    if lookback_minutes is not None:
        cmd_intake += ["--lookback-minutes", str(lookback_minutes)]
    if scope_text:
        cmd_intake += ["--scope", scope_text]

    if progress_context:
        request_path = base / "progress-request.json"
        request_path.write_text(json.dumps({
            "checkpoint": progress_context["entry"]["position"],
            "endpoint": progress_context["endpoint"],
        }), encoding="utf-8")
        cmd_intake += [
            "--progress-request", str(request_path), "--max-records", str(args.max_records),
            "--max-chars", str(args.max_chars), "--max-shard-bytes", str(args.max_shard_bytes),
        ]
    intake_result, intake = run_json_command(cmd_intake)
    if intake is None:
        emit_result(
            blocked_payload(
                "The intake command failed before memsearch-backed analysis could continue.",
                memory_root,
                scope_text,
                stderr=intake_result.stderr[-1200:],
            )
        )
        return 0

    intake_path = base / "intake.json"
    intake_path.write_text(intake_result.stdout, encoding="utf-8")
    batch = intake.get("progressive_batch")
    if batch and batch["next_position"] == progress_context["entry"]["position"] and not batch["remaining"]:
        emit_result({
            "status": "caught-up", "reason": "No unprocessed input remains through this invocation endpoint.",
            "analysis_request_present": True, "topic_cards": [],
            "analysis_window": {"mode": progress_context["mode"], "checked_days": [], "next_older_than_day": None},
            "progress": {"run_id": progress_context["run_id"], "checkpoint_advanced": False, "remaining": False},
        })
        return 0
    if batch and not batch["coverage"]["complete"]:
        emit_result(blocked_payload(batch.get("reason") or "No complete record batch fits the current budget.", memory_root, scope_text))
        return 0

    if intake.get("status") == "stale":
        payload = {
            "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
            "bare_alias_runtime_proof": RUNTIME_PROOF_NOTE,
            "analysis_request_present": True,
            "invocation_mode": "standalone-analysis-slash",
            "render_required_now": True,
            "generic_no_request_response_allowed": False,
            "status": "dormant",
            "reason": "The discovered memsearch input is stale, so analysis should not promote fresh proposals from it.",
            "memory_root": str(memory_root),
            "scope_filter": scope_text or None,
            "intake_status": intake.get("status"),
            "notes": intake.get("notes", []),
            "topic_list": [],
        }
        if args.older_than_day:
            payload["reason"] = intake.get("reason") or payload["reason"]
            payload["analysis_window"] = analysis_window_report(
                intake,
                supplemental=True,
                exclusive_boundary_day=args.older_than_day,
                pass_attempted=True,
                pass_used=True,
            )
        emit_result(payload)
        return 0

    if intake.get("status") == "unavailable":
        payload = {
            "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
            "bare_alias_runtime_proof": RUNTIME_PROOF_NOTE,
            "analysis_request_present": True,
            "invocation_mode": "standalone-analysis-slash",
            "render_required_now": True,
            "generic_no_request_response_allowed": False,
            "status": "blocked",
            "reason": intake.get("reason") or "The memsearch root is unavailable, so analysis cannot continue.",
            "memory_root": str(memory_root),
            "scope_filter": scope_text or None,
            "intake_status": intake.get("status"),
            "notes": intake.get("notes", []),
            "topic_list": [],
        }
        if args.older_than_day:
            payload["analysis_window"] = analysis_window_report(
                intake,
                supplemental=True,
                exclusive_boundary_day=args.older_than_day,
                pass_attempted=True,
                pass_used=False,
            )
        emit_result(payload)
        return 0

    cmd_signals = ["bash", str(RUNTIME_BIN), "signals", "--intake-report", str(intake_path)]
    signals_result, signals = run_json_command(cmd_signals)
    if signals is None:
        emit_result(
            blocked_payload(
                "The signals command failed before user-facing presentation could be built.",
                memory_root,
                scope_text,
                intake_status=intake.get("status"),
                stderr=signals_result.stderr[-1200:],
                supplemental_boundary=args.older_than_day,
                supplemental_intake=intake if args.older_than_day else None,
                supplemental_pass_attempted=bool(args.older_than_day),
            )
        )
        return 0

    signals_path = base / "signals.json"
    signals_path.write_text(signals_result.stdout, encoding="utf-8")

    transcript_path = resolve_transcript_path(args.session_id)
    present_language = infer_presentation_language(str(args.arguments or "").strip(), transcript_path)
    cmd_present = [
        "bash",
        str(RUNTIME_BIN),
        "present",
        "--signals-report",
        str(signals_path),
        "--output-mode",
        "native-first",
        "--language",
        present_language,
    ]
    present_result, present = run_json_command(cmd_present)
    if present is None:
        emit_result(
            blocked_payload(
                "The present command failed before proposal-first output could be rendered.",
                memory_root,
                scope_text,
                intake_status=intake.get("status"),
                signals_status=signals.get("status"),
                stderr=present_result.stderr[-1200:],
                supplemental_boundary=args.older_than_day,
                supplemental_intake=intake if args.older_than_day else None,
                supplemental_pass_attempted=bool(args.older_than_day),
            )
        )
        return 0

    scope_report = intake.get("scope", {})
    scope_basis = "historical-default scope"
    if scope_report.get("basis") == "explicit-day-and-session":
        scope_basis = "explicit day + session slice"
    elif scope_report.get("basis") == "explicit-session":
        scope_basis = "explicit current-session slice"
    elif scope_report.get("basis") == "explicit-day":
        scope_basis = "explicit day slice"
    elif scope_report.get("basis") == "config-default-day":
        scope_basis = "config-default-day"
    elif scope_report.get("basis") == "config-default-session":
        scope_basis = "config-default-session"
    elif scope_report.get("basis") == "config-default-lookback":
        scope_basis = "config-default-lookback"

    operator_warnings = build_operator_warnings(cwd=cwd, session_id=args.session_id)

    effective_source_classes = []
    if isinstance(intake.get("source_policy"), dict):
        raw_effective = intake.get("source_policy", {}).get("effective_source_classes") or []
        if isinstance(raw_effective, list):
            effective_source_classes = [str(item) for item in raw_effective if item]
    source_classes_present = intake.get("source", {}).get("source_classes_present")
    adaptive_deep_analysis = build_adaptive_deepening_plan(signals)
    adaptive_deep_analysis.update(
        {
            "default_internal_source_classes": effective_source_classes,
            "source_classes_present": source_classes_present,
            "all_four_internal_sources_default": effective_source_classes
            == [
                "trace_evidence",
                "recall_evidence",
                "durable_memory_context",
                "governance_context",
            ],
            "subagent_deepening_allowed": True,
            "external_research_enrichment_allowed": True,
            "trace_anchor_rule": "trace_evidence remains the live promotion anchor even when deeper analysis uses multiple internal sources and optional external support.",
            "advisory_only_before_selection": True,
            "packet_artifact_scope_after_selection": "single-topic-only",
            "multi_topic_deepening_combines_packet_output": False,
        }
    )

    payload = {
        "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
        "design_grounded_review": True,
        "namespace_runtime_detail": REGISTERED_OPERATOR_SURFACE,
        "analysis_request_present": True,
        "invocation_mode": "standalone-analysis-slash",
        "render_required_now": True,
        "generic_no_request_response_allowed": False,
        "status": present.get("status"),
        "memory_root": str(memory_root),
        "scope_filter": scope_text or None,
        "scope_basis": scope_basis,
        "analysis_window": analysis_window_report(
            intake,
            supplemental=bool(args.older_than_day),
            exclusive_boundary_day=args.older_than_day,
            pass_attempted=bool(args.older_than_day),
            pass_used=bool(args.older_than_day),
        ),
        "scope_day_shard": scope_report.get("day_shard") or args.current_day,
        "scope_session_id": args.session_id,
        "scope_lookback_minutes": lookback_minutes,
        "same_day_widened": scope_report.get("same_day_widened", False),
        "retrieval_mode": intake.get("source", {}).get("retrieval_mode"),
        "source_policy": intake.get("source_policy"),
        "scope_policy": intake.get("scope_policy"),
        "intake_status": intake.get("status"),
        "signals_status": signals.get("status"),
        "present_status": present.get("status"),
        "no_topics_message": present.get("no_topics_message"),
        "no_topics_details": present.get("no_topics_details", []),
        "recommended_next_step": present.get("recommended_next_step"),
        "source_classes_present": source_classes_present,
        "adaptive_deep_analysis": adaptive_deep_analysis,
        "topic_discovery_evidence": topic_discovery_evidence(intake),
        "topic_cards": present.get("topic_cards"),
        "next_action_options": present.get("next_action_options"),
    }
    if batch and progress_context:
        batch_id = uuid.uuid4().hex
        binding = {
            "batch_id": batch_id,
            "expected_version": progress_context["entry"]["version"],
            "expected_position": progress_context["entry"]["position"],
            "next_position": batch["next_position"],
            "coverage_complete": batch["coverage"]["complete"],
            "source_binding": {"memory_root": str(memory_root.resolve()), "prefixes": batch["next_position"]["completed"]},
            "run_id": progress_context["run_id"], "mode": progress_context["mode"],
            "endpoint": progress_context["endpoint"],
        }
        try:
            prepare_batch(args.state, progress_context["scope_key"], binding)
        except (CheckpointConflict, OSError) as exc:
            emit_result(blocked_payload(str(exc), memory_root, scope_text))
            return 0
        common = ["--state", str(args.state)] if args.state != default_state_path() else []
        payload["progress"] = {
            "batch_id": batch_id, "expected_version": binding["expected_version"],
            "run_id": binding["run_id"], "mode": binding["mode"], "remaining": batch["remaining"],
            "coverage_complete": True, "checkpoint_advanced": False,
            "completion_command": shlex.join([str(RUNTIME_BIN), "complete", "--batch-id", batch_id, "--outcome", "analyzed", *common]),
            "continuation_command": shlex.join([
                str(RUNTIME_BIN), "analysis-surface", "--arguments", "", "--continue-run", binding["run_id"],
                "--window-days", str(args.window_days), "--current-day", args.current_day,
                "--max-records", str(args.max_records), "--max-chars", str(args.max_chars),
                "--max-shard-bytes", str(args.max_shard_bytes), *common,
                *(["--config", explicit_config_path] if explicit_config_path else []),
            ]) if binding["mode"] == "catch-up" else None,
            "completion_boundary": "Caller semantic analysis and eligibility finished; preparation is not completion.",
        }
        payload["analysis_window"].update({"mode": binding["mode"], "next_older_than_day": None})
        payload["scope_basis"] = "oldest-unprocessed trace within selected calendar window"
    source_policy = payload.get("source_policy") if isinstance(payload.get("source_policy"), dict) else {}
    if source_policy.get("loaded") is False:
        payload["config_questions"] = build_guided_config_questions(cwd=cwd)
    if operator_warnings:
        payload["operator_warnings"] = operator_warnings
    emit_result(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
