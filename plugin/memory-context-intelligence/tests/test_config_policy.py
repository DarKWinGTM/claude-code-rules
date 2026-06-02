from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CONFIG_POLICY_PATH = PACKAGE_ROOT / "lib" / "config_policy.py"
SPEC = importlib.util.spec_from_file_location("mci_config_policy", CONFIG_POLICY_PATH)
config_policy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(config_policy)


class ConfigPolicyTests(unittest.TestCase):
    def test_default_scope_policy_is_historical_comprehensive(self) -> None:
        self.assertEqual(
            config_policy.normalize_scope_policy(None),
            {
                "default_scope_mode": "historical-comprehensive",
                "scope_day_shard": None,
                "scope_session_id": None,
                "scope_lookback_minutes": None,
            },
        )

    def test_scope_policy_day_mode_clears_other_narrow_fields(self) -> None:
        normalized = config_policy.normalize_scope_policy(
            {
                "default_scope_mode": "day",
                "scope_day_shard": "2026-06-02",
                "scope_session_id": "old-session",
                "scope_lookback_minutes": 90,
            }
        )

        self.assertEqual(
            normalized,
            {
                "default_scope_mode": "day",
                "scope_day_shard": "2026-06-02",
                "scope_session_id": None,
                "scope_lookback_minutes": None,
            },
        )

    def test_merge_analysis_config_preserves_unrelated_top_level_keys(self) -> None:
        existing = {
            "other_tool": {"enabled": True},
            "analysis": {
                "source_policy": {"max_historical_shards": 3}
            },
        }

        merged = config_policy.merge_analysis_config_document(
            existing_document=existing,
            scope_policy={
                "default_scope_mode": "historical-comprehensive",
                "scope_day_shard": None,
                "scope_session_id": None,
                "scope_lookback_minutes": None,
            },
            source_policy={
                "enabled_source_classes": [
                    "trace_evidence",
                    "recall_evidence",
                    "durable_memory_context",
                    "governance_context",
                ],
                "max_historical_shards": 10,
                "allow_same_day_widening": True,
            },
        )

        self.assertEqual(merged["other_tool"], {"enabled": True})
        self.assertEqual(merged["analysis"]["scope_policy"]["default_scope_mode"], "historical-comprehensive")
        self.assertEqual(merged["analysis"]["source_policy"]["max_historical_shards"], 10)

    def test_write_analysis_config_document_updates_existing_file_in_user_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            config_path = root / ".claude" / "memory-context-intelligence.config.json"
            config_path.parent.mkdir()
            config_path.write_text(
                json.dumps({"other_tool": {"enabled": True}}, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            config_policy.write_analysis_config_document(
                config_path=config_path,
                existing_document={"other_tool": {"enabled": True}},
                scope_policy={
                    "default_scope_mode": "session",
                    "scope_day_shard": None,
                    "scope_session_id": "session-123",
                    "scope_lookback_minutes": None,
                },
                source_policy={
                    "enabled_source_classes": ["trace_evidence", "recall_evidence"],
                    "max_historical_shards": 5,
                    "allow_same_day_widening": False,
                },
            )

            payload = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertEqual(payload["other_tool"], {"enabled": True})
        self.assertEqual(payload["analysis"]["scope_policy"]["default_scope_mode"], "session")
        self.assertEqual(payload["analysis"]["scope_policy"]["scope_session_id"], "session-123")
        self.assertEqual(payload["analysis"]["source_policy"]["max_historical_shards"], 5)

    def test_load_analysis_config_state_reads_scope_and_source_policy(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            claude_root = root / ".claude"
            claude_root.mkdir()
            config_path = claude_root / "memory-context-intelligence.config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "analysis": {
                            "scope_policy": {
                                "default_scope_mode": "lookback",
                                "scope_day_shard": None,
                                "scope_session_id": None,
                                "scope_lookback_minutes": 180,
                            },
                            "source_policy": {
                                "enabled_source_classes": ["trace_evidence", "recall_evidence"],
                                "max_historical_shards": 5,
                                "allow_same_day_widening": False,
                            },
                        }
                    },
                    ensure_ascii=False,
                ) + "\n",
                encoding="utf-8",
            )

            with mock.patch.object(config_policy.Path, "home", return_value=root):
                state = config_policy.load_analysis_config_state(explicit_config_path=None, cwd=root)

        self.assertTrue(state["loaded"])
        self.assertEqual(state["config_path"], str(config_path))
        self.assertEqual(state["scope_policy"]["default_scope_mode"], "lookback")
        self.assertEqual(state["scope_policy"]["scope_lookback_minutes"], 180)
        self.assertEqual(state["source_policy"]["effective_source_classes"], ["trace_evidence", "recall_evidence"])


if __name__ == "__main__":
    unittest.main()
