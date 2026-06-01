#!/usr/bin/env python3
"""Focused checks for phase-013 candidate packets and gated additional emission."""

from __future__ import annotations

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_PACKET_PATH = PACKAGE_ROOT / "lib" / "candidate_packet.py"
ORCHESTRATION_PATH = PACKAGE_ROOT / "lib" / "orchestration.py"

CANDIDATE_SPEC = importlib.util.spec_from_file_location("mci_candidate_packet", CANDIDATE_PACKET_PATH)
candidate_packet = importlib.util.module_from_spec(CANDIDATE_SPEC)
assert CANDIDATE_SPEC.loader is not None
CANDIDATE_SPEC.loader.exec_module(candidate_packet)

ORCHESTRATION_SPEC = importlib.util.spec_from_file_location("mci_orchestration_for_packet_tests", ORCHESTRATION_PATH)
orchestration = importlib.util.module_from_spec(ORCHESTRATION_SPEC)
assert ORCHESTRATION_SPEC.loader is not None
ORCHESTRATION_SPEC.loader.exec_module(orchestration)


def intake_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "intake",
        "status": "available",
        "source": {"available": True, "memory_root_source": "test"},
        "scope": {"filters": ["memory-context-intelligence"], "bounded_subset_only": True},
        "freshness": {"classification": "fresh"},
        "records": [],
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "ranked_signals": [
            {
                "id": "signal-001",
                "rank": 1,
                "confidence": "medium",
                "records": [
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "content_preview": "Do not claim completion before checked verification.",
                    }
                ],
            }
        ],
        "topic_candidates": [
            {
                "rank": 1,
                "id": "topic-001",
                "title": "Strengthen completion evidence wording",
                "purpose": "Keep completion claims tied to checked verification scope.",
                "why_surfaced": "Repeated traces mentioned completion wording before verification.",
                "expected_behavior_impact": "Future packets preserve evidence limits.",
                "high_level_mechanism": "Use lane findings before candidate-packet construction.",
                "expected_output": "A bounded candidate packet for additional-stage trial material.",
                "confidence": "medium",
                "evidence_label": "bounded-repeated-observed-local",
                "source_signal_ids": ["signal-001"],
            }
        ],
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def selection_report() -> dict:
    topic = signals_report()["topic_candidates"][0]
    return {
        "tool": "memory-context-intelligence",
        "mode": "choose",
        "status": "selected",
        "selected_topic_id": topic["id"],
        "selected_topic": {
            **topic,
            "research_need": {"needed": True, "reason": "Needs source-trust support."},
            "selected": True,
            "advisory_only": False,
            "carry_forward_allowed": True,
        },
        "unselected_topics": [],
        "selection_required_before_carry_forward": False,
        "carry_forward_allowed": True,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def strong_source_fixture() -> dict:
    return {
        "name": "phase-013-strong-source-fixture",
        "recorded_at": "2026-05-18",
        "sources": [
            {
                "id": "official-docs",
                "title": "Official documentation on verification wording",
                "source_type": "official_docs",
                "freshness": "current",
                "checked_at": "2026-05-18",
                "supports": ["Completion wording should identify checked scope and evidence limits."],
                "constraints": ["Do not call behavior fixed without verification covering the failure scope."],
            }
        ],
    }


def orchestration_report() -> dict:
    return orchestration.build_orchestration(
        intake_report=intake_report(),
        signals_report=signals_report(),
        selection_report=selection_report(),
        source_fixture=strong_source_fixture(),
    )


def packet_report() -> dict:
    report = orchestration_report()
    return candidate_packet.build_candidate_packet(
        report["phase_013_candidate_input"],
        owner_domain="evidence-discipline",
        main_rule_target="rules/evidence-discipline.md",
        additional_name="completion-evidence-trial",
    )


class CandidatePacketTests(unittest.TestCase):
    def test_packet_builds_from_orchestration_result(self) -> None:
        packet = packet_report()

        self.assertEqual(packet["status"], "packet-built")
        self.assertEqual(packet["candidate_packet_model"], "phase-013-candidate-packet-v1")
        self.assertTrue(packet["candidate_packet_built"])
        self.assertFalse(packet["additional_emission_performed"])
        self.assertFalse(packet["main_rules_mutation_performed"])

        body = packet["candidate_packet"]
        self.assertEqual(body["candidate_summary"]["topic_id"], "topic-001")
        self.assertTrue(body["signal_evidence_basis"]["trace_anchors"])
        self.assertTrue(body["signal_evidence_basis"]["source_anchors"])
        self.assertEqual(body["owner_domain_mapping"]["owner_domain"], "evidence-discipline")
        self.assertEqual(body["owner_domain_mapping"]["intended_main_rule_target"], "rules/evidence-discipline.md")
        self.assertEqual(
            body["proposed_additional_rule"]["relative_path"],
            "memory-context-intelligence/completion-evidence-trial.md",
        )
        self.assertEqual(body["artifact_topic_scope"], "single-topic-only")
        self.assertEqual(body["selected_topic_count"], 1)
        self.assertFalse(body["multi_topic_combination_allowed"])
        self.assertTrue(body["trial_first_rationale"])
        self.assertTrue(body["risks"])
        self.assertTrue(body["success_criteria"])
        self.assertTrue(body["rollback_notes"])
        self.assertEqual(body["stop_gates"], [])
        self.assertTrue(body["leader_verification_needs"])

    def test_dry_run_emission_previews_without_write(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            packet = packet_report()
            preview = candidate_packet.emit_additional(packet, additional_root=temp_root)
            destination = Path(preview["destination_path"])

            self.assertEqual(preview["status"], "preview")
            self.assertTrue(preview["dry_run"])
            self.assertFalse(preview["approved_write"])
            self.assertFalse(preview["additional_emission_performed"])
            self.assertFalse(preview["main_rules_mutation_performed"])
            self.assertFalse(destination.exists())
            self.assertIn("Additional trial rule", preview["preview_material"])
            self.assertIn("## Topic scope", preview["preview_material"])
            self.assertIn("split into separate per-topic artifacts", preview["preview_material"])
            self.assertIn("## Rollback notes", preview["preview_material"])

    def test_approved_write_targets_controlled_additional_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            packet = packet_report()
            emitted = candidate_packet.emit_additional(packet, additional_root=temp_root, approved_write=True)
            destination = Path(emitted["destination_path"])

            self.assertEqual(emitted["status"], "emitted")
            self.assertFalse(emitted["dry_run"])
            self.assertTrue(emitted["approved_write"])
            self.assertTrue(emitted["additional_emission_performed"])
            self.assertFalse(emitted["main_rules_mutation_performed"])
            self.assertTrue(destination.exists())
            self.assertEqual(destination.parent.name, "memory-context-intelligence")
            material = destination.read_text(encoding="utf-8")
            self.assertIn("Trial-only additional-stage material", material)
            self.assertIn("## Topic scope", material)
            self.assertIn("must not combine multiple selected topics", material)
            self.assertIn("## Success criteria", material)
            self.assertIn("## Rollback notes", material)

    def test_overwrite_requires_explicit_allow_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            packet = packet_report()
            candidate_packet.emit_additional(packet, additional_root=temp_root, approved_write=True)

            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(packet, additional_root=temp_root, approved_write=True)

            overwritten = candidate_packet.emit_additional(
                packet,
                additional_root=temp_root,
                approved_write=True,
                allow_overwrite=True,
            )
            self.assertEqual(overwritten["status"], "emitted")

    def test_multi_topic_candidate_input_is_rejected_before_packet_build(self) -> None:
        candidate_input = copy.deepcopy(orchestration_report()["phase_013_candidate_input"])
        candidate_input["selected_topics"] = [
            candidate_input["selected_topic"],
            {**candidate_input["selected_topic"], "id": "topic-002", "title": "Another topic"},
        ]

        with self.assertRaises(candidate_packet.CandidatePacketError) as exc:
            candidate_packet.build_candidate_packet(
                candidate_input,
                owner_domain="evidence-discipline",
                main_rule_target="rules/evidence-discipline.md",
            )

        self.assertIn("split into separate per-topic artifacts", str(exc.exception))

    def test_combined_topic_packet_is_rejected_before_emit(self) -> None:
        packet = copy.deepcopy(packet_report())
        packet["candidate_packet"]["selected_topic_count"] = 2
        packet["candidate_packet"]["multi_topic_combination_allowed"] = True

        with tempfile.TemporaryDirectory() as temp_root:
            with self.assertRaises(candidate_packet.CandidatePacketError) as exc:
                candidate_packet.emit_additional(packet, additional_root=temp_root)

        self.assertIn("single selected topic", str(exc.exception))

    def test_path_safety_refuses_escape_and_main_rules_root(self) -> None:
        with self.assertRaises(candidate_packet.CandidatePacketError):
            candidate_packet.build_candidate_packet(
                orchestration_report()["phase_013_candidate_input"],
                owner_domain="evidence-discipline",
                main_rule_target="rules/evidence-discipline.md",
                additional_relative_path="../bad.md",
            )

        packet = packet_report()
        unsafe = copy.deepcopy(packet)
        unsafe["candidate_packet"]["proposed_additional_rule"]["relative_path"] = "../bad.md"
        with tempfile.TemporaryDirectory() as temp_root:
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(unsafe, additional_root=temp_root)

        with tempfile.TemporaryDirectory() as temp_parent:
            main_rules_root = Path(temp_parent) / "rules"
            main_rules_root.mkdir()
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(packet, additional_root=str(main_rules_root), approved_write=True)


if __name__ == "__main__":
    unittest.main()
