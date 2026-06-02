from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_CONFIG_FILENAME = "memory-context-intelligence.config.json"
SOURCE_CLASS_ORDER = (
    "trace_evidence",
    "recall_evidence",
    "durable_memory_context",
    "governance_context",
)
DEFAULT_SCOPE_POLICY = {
    "default_scope_mode": "historical-comprehensive",
    "scope_day_shard": None,
    "scope_session_id": None,
    "scope_lookback_minutes": None,
}
SCOPE_MODE_ORDER = (
    "historical-comprehensive",
    "day",
    "session",
    "lookback",
)


def resolve_path(path: Path) -> Path:
    try:
        return path.expanduser().resolve()
    except OSError:
        return path.expanduser().absolute()


def default_user_config_path() -> Path:
    return resolve_path(Path.home() / ".claude" / DEFAULT_CONFIG_FILENAME)


def discover_config_path(start_dir: Path) -> Path | None:
    del start_dir
    candidate = default_user_config_path()
    if candidate.is_file():
        return candidate
    return None


def normalize_source_classes(raw: Any) -> list[str]:
    if not isinstance(raw, list):
        return list(SOURCE_CLASS_ORDER)
    requested = [str(item) for item in raw if str(item) in SOURCE_CLASS_ORDER]
    normalized = [source_class for source_class in SOURCE_CLASS_ORDER if source_class in requested]
    return normalized or list(SOURCE_CLASS_ORDER)


def normalize_max_historical_shards(raw: Any) -> int | None:
    if raw in (None, ""):
        return None
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return None
    return max(1, min(value, 10))


def normalize_scope_policy(raw: Any) -> dict[str, Any]:
    policy = dict(DEFAULT_SCOPE_POLICY)
    if not isinstance(raw, dict):
        return policy

    requested_mode = str(raw.get("default_scope_mode") or "historical-comprehensive")
    if requested_mode not in SCOPE_MODE_ORDER:
        requested_mode = "historical-comprehensive"
    policy["default_scope_mode"] = requested_mode

    if requested_mode == "day":
        day_value = raw.get("scope_day_shard")
        policy["scope_day_shard"] = str(day_value) if day_value else None
    elif requested_mode == "session":
        session_value = raw.get("scope_session_id")
        policy["scope_session_id"] = str(session_value) if session_value else None
    elif requested_mode == "lookback":
        try:
            lookback_value = int(raw.get("scope_lookback_minutes"))
        except (TypeError, ValueError):
            lookback_value = None
        policy["scope_lookback_minutes"] = None if lookback_value is None else max(1, lookback_value)

    return policy


def load_analysis_config_state(*, explicit_config_path: str | None, cwd: Path) -> dict[str, Any]:
    config_path: Path | None = None
    config_source = "none"
    errors: list[str] = []
    raw_source_policy: dict[str, Any] = {}
    raw_scope_policy: dict[str, Any] = {}
    loaded = False

    if explicit_config_path:
        config_path = resolve_path(Path(explicit_config_path))
        config_source = "cli"
    else:
        config_path = discover_config_path(cwd)
        if config_path is not None:
            config_source = "auto-upward"

    if config_path is not None:
        try:
            parsed = json.loads(config_path.read_text(encoding="utf-8"))
            if isinstance(parsed, dict):
                analysis_block = parsed.get("analysis")
                if isinstance(analysis_block, dict):
                    source_policy = analysis_block.get("source_policy")
                    if isinstance(source_policy, dict):
                        raw_source_policy = source_policy
                    scope_policy = analysis_block.get("scope_policy")
                    if isinstance(scope_policy, dict):
                        raw_scope_policy = scope_policy
            loaded = True
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(str(exc))

    return {
        "loaded": loaded,
        "config_path": None if config_path is None else str(config_path),
        "config_source": config_source,
        "errors": errors,
        "scope_policy": normalize_scope_policy(raw_scope_policy),
        "source_policy": {
            "effective_source_classes": normalize_source_classes(raw_source_policy.get("enabled_source_classes")),
            "requested_same_day_widening": bool(raw_source_policy.get("allow_same_day_widening", False)),
            "max_historical_shards": normalize_max_historical_shards(raw_source_policy.get("max_historical_shards")),
        },
    }


def load_analysis_source_policy(*, explicit_config_path: str | None, cwd: Path) -> dict[str, Any]:
    state = load_analysis_config_state(explicit_config_path=explicit_config_path, cwd=cwd)
    return {
        "loaded": state["loaded"],
        "config_path": state["config_path"],
        "config_source": state["config_source"],
        "errors": state["errors"],
        "enabled_source_classes": state["source_policy"]["effective_source_classes"],
        "requested_same_day_widening": state["source_policy"]["requested_same_day_widening"],
        "max_historical_shards": state["source_policy"]["max_historical_shards"],
        "scope_policy": state["scope_policy"],
    }


def merge_analysis_config_document(
    *,
    existing_document: dict[str, Any],
    scope_policy: dict[str, Any],
    source_policy: dict[str, Any],
) -> dict[str, Any]:
    merged = dict(existing_document)
    analysis_block = dict(merged.get("analysis") or {})
    analysis_block["scope_policy"] = normalize_scope_policy(scope_policy)
    analysis_block["source_policy"] = {
        "enabled_source_classes": normalize_source_classes(source_policy.get("enabled_source_classes")),
        "max_historical_shards": normalize_max_historical_shards(source_policy.get("max_historical_shards")) or 10,
        "allow_same_day_widening": bool(source_policy.get("allow_same_day_widening", False)),
    }
    merged["analysis"] = analysis_block
    return merged


def write_analysis_config_document(
    *,
    config_path: Path,
    existing_document: dict[str, Any],
    scope_policy: dict[str, Any],
    source_policy: dict[str, Any],
) -> dict[str, Any]:
    merged = merge_analysis_config_document(
        existing_document=existing_document,
        scope_policy=scope_policy,
        source_policy=source_policy,
    )
    resolved_path = resolve_path(config_path)
    resolved_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return merged


def build_guided_config_questions(*, cwd: Path) -> dict[str, Any]:
    del cwd
    suggested_path = str(default_user_config_path())
    return {
        "heading": "Config helper",
        "status_line": "advisory only; config not loaded yet",
        "advisory_only": True,
        "suggested_config_path": suggested_path,
        "questions": [
            {
                "id": "scope-mode",
                "label": "Scope mode",
                "question": "Should the default analysis scope stay historical-default, or start from a specific day / session / lookback window?",
            },
            {
                "id": "source-classes",
                "label": "Source classes",
                "question": "Which evidence classes should stay enabled by default: trace only, trace + recall, or all four classes?",
            },
            {
                "id": "same-day-widening",
                "label": "Widening rule",
                "question": "When a current-session slice is weak, should same-day widening stay off by default or be allowed only for non-explicit runs?",
            },
            {
                "id": "save-behavior",
                "label": "Save behavior",
                "question": "Should the next chosen config be saved as a project default config file or used once without writing a file?",
            },
        ],
    }
