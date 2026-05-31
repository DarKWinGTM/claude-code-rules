from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import tempfile
from datetime import date, datetime
from pathlib import Path
from typing import Any

LIB_DIR = Path(__file__).resolve().parent
if str(LIB_DIR) not in os.sys.path:
    os.sys.path.insert(0, str(LIB_DIR))

from config_policy import build_guided_config_questions

REGISTERED_OPERATOR_SURFACE = "/memory-context-intelligence:analysis"
RUNTIME_PROOF_NOTE = "not proved in checked current print-mode runtime"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_BIN = (PACKAGE_ROOT / "bin" / "memory-context-intelligence").resolve()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="memory-context-intelligence analysis-surface")
    parser.add_argument("--arguments", default=os.environ.get("ARGUMENTS", ""))
    parser.add_argument("--session-id", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    parser.add_argument("--current-day", default=date.today().isoformat())
    return parser.parse_args(argv)


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


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


def blocked_payload(reason: str, memory_root: Path | None, scope_text: str | None, **extra: Any) -> dict[str, Any]:
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
    memory_root = find_memory_root(cwd)
    scope_text, lookback_minutes, explicit_day, explicit_session_id, explicit_config_path = parse_scope_and_narrowing(str(args.arguments or "").strip())

    if memory_root is None:
        emit(
            blocked_payload(
                "No project-scoped .memsearch/memory root was found from the current working directory upward.",
                None,
                scope_text,
            )
        )
        return 0

    base = Path(tempfile.mkdtemp(prefix="mci-analysis-"))

    cmd_intake = [
        "bash",
        str(RUNTIME_BIN),
        "intake",
        "--memory-root",
        str(memory_root),
    ]
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

    intake_result, intake = run_json_command(cmd_intake)
    if intake is None:
        emit(
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

    if intake.get("status") == "stale":
        emit(
            {
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
        )
        return 0

    if intake.get("status") == "unavailable":
        emit(
            {
                "registered_operator_surface": REGISTERED_OPERATOR_SURFACE,
                "bare_alias_runtime_proof": RUNTIME_PROOF_NOTE,
                "analysis_request_present": True,
                "invocation_mode": "standalone-analysis-slash",
                "render_required_now": True,
                "generic_no_request_response_allowed": False,
                "status": "blocked",
                "reason": "The memsearch root is unavailable, so analysis cannot continue.",
                "memory_root": str(memory_root),
                "scope_filter": scope_text or None,
                "intake_status": intake.get("status"),
                "notes": intake.get("notes", []),
                "topic_list": [],
            }
        )
        return 0

    cmd_signals = ["bash", str(RUNTIME_BIN), "signals", "--intake-report", str(intake_path)]
    signals_result, signals = run_json_command(cmd_signals)
    if signals is None:
        emit(
            blocked_payload(
                "The signals command failed before user-facing presentation could be built.",
                memory_root,
                scope_text,
                intake_status=intake.get("status"),
                stderr=signals_result.stderr[-1200:],
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
        emit(
            blocked_payload(
                "The present command failed before proposal-first output could be rendered.",
                memory_root,
                scope_text,
                intake_status=intake.get("status"),
                signals_status=signals.get("status"),
                stderr=present_result.stderr[-1200:],
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

    operator_warnings = build_operator_warnings(cwd=cwd, session_id=args.session_id)

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
        "scope_day_shard": scope_report.get("day_shard") or args.current_day,
        "scope_session_id": args.session_id,
        "scope_lookback_minutes": lookback_minutes,
        "same_day_widened": scope_report.get("same_day_widened", False),
        "retrieval_mode": intake.get("source", {}).get("retrieval_mode"),
        "source_policy": intake.get("source_policy"),
        "intake_status": intake.get("status"),
        "signals_status": signals.get("status"),
        "present_status": present.get("status"),
        "no_topics_message": present.get("no_topics_message"),
        "no_topics_details": present.get("no_topics_details", []),
        "recommended_next_step": present.get("recommended_next_step"),
        "source_classes_present": intake.get("source", {}).get("source_classes_present"),
        "topic_cards": present.get("topic_cards"),
        "next_action_options": present.get("next_action_options"),
    }
    source_policy = payload.get("source_policy") if isinstance(payload.get("source_policy"), dict) else {}
    if source_policy.get("loaded") is False:
        payload["config_questions"] = build_guided_config_questions(cwd=cwd)
    if operator_warnings:
        payload["operator_warnings"] = operator_warnings
    emit(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
