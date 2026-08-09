#!/usr/bin/env python3
"""CLI checks for deterministic selected-topic additional emission."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PACKET_PATH = PACKAGE_ROOT / "lib" / "candidate_packet.py"
BIN_PATH = PACKAGE_ROOT / "bin" / "memory-context-intelligence"
SPEC = importlib.util.spec_from_file_location("mci_candidate_packet_cli", CANDIDATE_PACKET_PATH)
candidate_packet = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(candidate_packet)


def packet_report(topic_number: int, relative_name: str) -> dict:
    signal_id = f"signal-{topic_number:03d}"
    topic_id = f"topic-{topic_number:03d}"
    candidate_input = {
        "model_version": "test",
        "selected_topic": {
            "id": topic_id,
            "title": f"Standalone topic {topic_number}",
            "purpose": "Keep one selected topic in one independently understandable trial artifact.",
            "why_surfaced": "Bounded traces showed selected topics need independent trial artifacts.",
            "expected_behavior_impact": "Selected trial topics remain independent and reviewable.",
            "expected_output": f"One standalone trial artifact for {topic_id}.",
            "confidence": "medium",
            "evidence_label": "bounded-test-evidence",
            "source_signal_ids": [signal_id],
            "candidate_entailment_basis": {
                "candidate_title": f"Standalone topic {topic_number}",
                "source_signal_ids": [signal_id],
                "trace_record_count": 1,
                "source_keywords": ["standalone", "trial"],
                "transferable_observed_pattern": "Combined trial output obscured topic ownership.",
                "supported_mechanism": "Emit one standalone trial artifact per explicitly selected topic.",
            },
        },
        "artifact_topic_scope": "single-topic-only",
        "selected_topic_count": 1,
        "multi_topic_combination_allowed": False,
        "trace_anchors": [
            {
                "signal_id": signal_id,
                "session_id": f"session-{topic_number}",
                "shard": f"shard-{topic_number}",
                "source_classes": ["trace_evidence"],
                "content_preview": "Internal audit preview only.",
            }
        ],
        "source_anchors": [],
        "blocking_stop_gates": [],
        "conflicts_uncertainty": [],
        "leader_verification_needs": [],
    }
    return candidate_packet.build_candidate_packet(
        candidate_input,
        owner_domain="evidence-discipline",
        main_rule_target="rules/evidence-discipline.md",
        additional_relative_path=f"memory-context-intelligence/{relative_name}.md",
        selected_for_additional_trial=True,
    )


class CandidatePacketCliTests(unittest.TestCase):
    def test_emit_selected_accepts_repeated_packet_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root) / "rules" / "additional"
            root.mkdir(parents=True)
            first = Path(temp_root) / "first.json"
            second = Path(temp_root) / "second.json"
            first.write_text(json.dumps(packet_report(1, "first")), encoding="utf-8")
            second.write_text(json.dumps(packet_report(2, "second")), encoding="utf-8")

            completed = subprocess.run(
                [
                    "python3",
                    str(CANDIDATE_PACKET_PATH),
                    "emit-selected",
                    "--packet-report",
                    str(first),
                    "--packet-report",
                    str(second),
                    "--additional-root",
                    str(root),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads(completed.stdout)
            self.assertEqual(report["status"], "preview")
            self.assertEqual(len(report["items"]), 2)
            self.assertFalse(any(root.rglob("*.md")))

    def test_emit_and_shell_help_expose_no_allow_overwrite(self) -> None:
        candidate_help = subprocess.run(
            ["python3", str(CANDIDATE_PACKET_PATH), "emit", "--help"],
            check=False,
            capture_output=True,
            text=True,
        )
        shell_help = subprocess.run(
            ["bash", str(BIN_PATH), "--help"],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(candidate_help.returncode, 0)
        self.assertEqual(shell_help.returncode, 0)
        self.assertNotIn("allow-overwrite", candidate_help.stdout)
        self.assertNotIn("allow-overwrite", shell_help.stdout)
        self.assertIn("emit-selected", shell_help.stdout)

    def test_batch_cli_collision_exits_two_without_writes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root) / "rules" / "additional"
            namespace = root / "memory-context-intelligence"
            namespace.mkdir(parents=True)
            sentinel = namespace / "second.md"
            sentinel.write_bytes(b"existing-sentinel")
            first = Path(temp_root) / "first.json"
            second = Path(temp_root) / "second.json"
            first.write_text(json.dumps(packet_report(1, "first")), encoding="utf-8")
            second.write_text(json.dumps(packet_report(2, "second")), encoding="utf-8")

            completed = subprocess.run(
                [
                    "python3",
                    str(CANDIDATE_PACKET_PATH),
                    "emit-selected",
                    "--packet-report",
                    str(first),
                    "--packet-report",
                    str(second),
                    "--additional-root",
                    str(root),
                    "--approved-write",
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 2)
            self.assertFalse((namespace / "first.md").exists())
            self.assertEqual(sentinel.read_bytes(), b"existing-sentinel")

    def test_cli_report_keeps_trial_selection_separate_from_promotion(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root) / "rules" / "additional"
            root.mkdir(parents=True)
            packet_path = Path(temp_root) / "packet.json"
            packet_path.write_text(json.dumps(packet_report(1, "first")), encoding="utf-8")

            completed = subprocess.run(
                [
                    "python3",
                    str(CANDIDATE_PACKET_PATH),
                    "emit-selected",
                    "--packet-report",
                    str(packet_path),
                    "--additional-root",
                    str(root),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            report = json.loads(completed.stdout)
            self.assertTrue(report["selected_for_additional_trial"])
            self.assertFalse(report["main_rules_promotion_approved"])


if __name__ == "__main__":
    unittest.main()
