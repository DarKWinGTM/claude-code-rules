from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT_PATH = PACKAGE_ROOT / "lib" / "analysis_checkpoint.py"
SPEC = importlib.util.spec_from_file_location("mci_analysis_checkpoint", CHECKPOINT_PATH)
checkpoint = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(checkpoint)


class AnalysisCheckpointTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.state_path = Path(self.temp_dir.name) / "progress.json"
        self.scope_key = "memory-root:test-scope"
        self.binding = {
            "batch_id": "batch-001",
            "expected_version": 0,
            "expected_position": None,
            "next_position": {
                "shard": "2026-01-10.md",
                "completed": {"2026-01-10.md": {"offset": 128, "prefix_digest": "0" * 64, "record_key": "record-001"}},
            },
            "coverage_complete": True,
            "source_binding": {"endpoint": "endpoint-001", "prefix_digest": "digest-001"},
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_prepare_does_not_advance_and_zero_topic_completion_advances_once(self) -> None:
        checkpoint.prepare_batch(self.state_path, self.scope_key, self.binding)

        pending = checkpoint.load_progress(self.state_path, self.scope_key)
        self.assertEqual(pending["version"], 0)
        self.assertIsNone(pending["position"])
        self.assertEqual(pending["pending"]["batch_id"], "batch-001")

        committed = checkpoint.complete_batch(
            self.state_path,
            self.scope_key,
            "batch-001",
            "no-topics",
            source_binding=self.binding["source_binding"],
        )
        self.assertEqual(committed["version"], 1)
        self.assertEqual(committed["position"], self.binding["next_position"])
        self.assertIsNone(committed["pending"])

        duplicate = checkpoint.complete_batch(
            self.state_path,
            self.scope_key,
            "batch-001",
            "no-topics",
            source_binding=self.binding["source_binding"],
        )
        self.assertEqual(duplicate["version"], 1)
        self.assertEqual(duplicate["position"], self.binding["next_position"])
        self.assertEqual(duplicate["status"], "already-complete")

    def test_failed_or_unacknowledged_batch_keeps_progress_and_stale_completion_is_rejected(self) -> None:
        checkpoint.prepare_batch(self.state_path, self.scope_key, self.binding)

        failed = checkpoint.complete_batch(
            self.state_path,
            self.scope_key,
            "batch-001",
            "failed",
            source_binding=self.binding["source_binding"],
        )
        self.assertEqual(failed["version"], 0)
        self.assertIsNone(failed["position"])
        self.assertIsNone(failed["pending"])

        checkpoint.prepare_batch(self.state_path, self.scope_key, self.binding)
        with self.assertRaises(checkpoint.CheckpointConflict):
            checkpoint.complete_batch(
                self.state_path,
                self.scope_key,
                "batch-001",
                "analyzed",
                source_binding={"endpoint": "changed", "prefix_digest": "digest-001"},
            )

        unchanged = checkpoint.load_progress(self.state_path, self.scope_key)
        self.assertEqual(unchanged["version"], 0)
        self.assertIsNone(unchanged["position"])
        self.assertEqual(unchanged["pending"]["batch_id"], "batch-001")

    def test_incomplete_batch_cannot_be_acknowledged_as_analyzed(self) -> None:
        incomplete = dict(self.binding, batch_id="batch-002", coverage_complete=False)
        checkpoint.prepare_batch(self.state_path, self.scope_key, incomplete)

        with self.assertRaises(checkpoint.CheckpointConflict):
            checkpoint.complete_batch(
                self.state_path,
                self.scope_key,
                "batch-002",
                "analyzed",
                source_binding=incomplete["source_binding"],
            )

        unchanged = checkpoint.load_progress(self.state_path, self.scope_key)
        self.assertEqual(unchanged["version"], 0)
        self.assertIsNone(unchanged["position"])

    def test_competing_preparation_and_failed_replace_preserve_last_committed_state(self) -> None:
        checkpoint.prepare_batch(self.state_path, self.scope_key, self.binding)
        other = dict(self.binding, batch_id="batch-other")
        checkpoint.prepare_batch(self.state_path, self.scope_key, other)
        with self.assertRaises(checkpoint.CheckpointConflict):
            checkpoint.complete_batch(self.state_path, self.scope_key, "batch-001", "analyzed", source_binding=self.binding["source_binding"])
        before = self.state_path.read_bytes()
        with patch.object(checkpoint.os, "replace", side_effect=OSError("fixture interrupted replace")):
            with self.assertRaises(OSError):
                checkpoint.complete_batch(self.state_path, self.scope_key, "batch-other", "analyzed", source_binding=other["source_binding"])
        self.assertEqual(self.state_path.read_bytes(), before)
        checkpoint.complete_batch(self.state_path, self.scope_key, "batch-other", "analyzed", source_binding=other["source_binding"])
        with self.assertRaises(checkpoint.CheckpointConflict):
            checkpoint.prepare_batch(self.state_path, self.scope_key, self.binding)

    def test_corrupt_or_boolean_version_is_not_reset(self) -> None:
        malformed = {"schema_version": 1, "scopes": {self.scope_key: {
            "version": 0, "position": None, "pending": None, "last_completed": ["bad"],
        }}}
        malformed_position = {"schema_version": 1, "scopes": {self.scope_key: {
            "version": 1, "position": {"completed": []}, "pending": None, "last_completed": None,
        }}}
        missing_position = {"schema_version": 1, "scopes": {self.scope_key: {
            "version": 0, "pending": None, "last_completed": None,
        }}}
        for data in [b"not json", json.dumps({"schema_version": True, "scopes": {}}).encode(), json.dumps(malformed).encode(), json.dumps(malformed_position).encode(), json.dumps(missing_position).encode()]:
            with self.subTest(data=data):
                self.state_path.write_bytes(data)
                with self.assertRaises(checkpoint.CheckpointConflict):
                    checkpoint.load_progress(self.state_path, self.scope_key)
                self.assertEqual(self.state_path.read_bytes(), data)


if __name__ == "__main__":
    unittest.main()
