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


def resolve_path(path: Path) -> Path:
    try:
        return path.expanduser().resolve()
    except OSError:
        return path.expanduser().absolute()


def discover_config_path(start_dir: Path) -> Path | None:
    resolved = resolve_path(start_dir)
    for base in [resolved, *resolved.parents]:
        candidate = base / DEFAULT_CONFIG_FILENAME
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


def load_analysis_source_policy(*, explicit_config_path: str | None, cwd: Path) -> dict[str, Any]:
    config_path: Path | None = None
    config_source = "none"
    errors: list[str] = []

    if explicit_config_path:
        config_path = resolve_path(Path(explicit_config_path))
        config_source = "cli"
    else:
        config_path = discover_config_path(cwd)
        if config_path is not None:
            config_source = "auto-upward"

    raw_policy: dict[str, Any] = {}
    loaded = False
    if config_path is not None:
        try:
            parsed = json.loads(config_path.read_text(encoding="utf-8"))
            if isinstance(parsed, dict):
                analysis_block = parsed.get("analysis")
                if isinstance(analysis_block, dict):
                    source_policy = analysis_block.get("source_policy")
                    if isinstance(source_policy, dict):
                        raw_policy = source_policy
            loaded = True
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(str(exc))

    return {
        "loaded": loaded,
        "config_path": None if config_path is None else str(config_path),
        "config_source": config_source,
        "errors": errors,
        "enabled_source_classes": normalize_source_classes(raw_policy.get("enabled_source_classes")),
        "requested_same_day_widening": bool(raw_policy.get("allow_same_day_widening", False)),
        "max_historical_shards": normalize_max_historical_shards(raw_policy.get("max_historical_shards")),
    }


def build_guided_config_questions(*, cwd: Path) -> dict[str, Any]:
    suggested_path = str(resolve_path(cwd) / DEFAULT_CONFIG_FILENAME)
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
