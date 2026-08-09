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
                "source_classes": ["trace_evidence"],
                "records": [
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "session_id": "session-a",
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
                "candidate_entailment_basis": {
                    "candidate_title": "Strengthen completion evidence wording",
                    "source_signal_ids": ["signal-001"],
                    "trace_record_count": 1,
                    "source_keywords": ["completion", "verification", "evidence"],
                    "transferable_observed_pattern": (
                        "Completion wording repeatedly outran the verification scope that was actually checked."
                    ),
                    "supported_mechanism": (
                        "Keep completion wording bounded to the strongest verification evidence that passed."
                    ),
                },
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
        integration_anchors=["rules/accurate-communication.md"],
        additional_name="completion-evidence-trial",
        selected_for_additional_trial=True,
    )


def second_packet_report(relative_path: str = "memory-context-intelligence/second.md") -> dict:
    report = copy.deepcopy(packet_report())
    packet = report["candidate_packet"]
    packet["candidate_summary"]["topic_id"] = "topic-002"
    packet["candidate_summary"]["title"] = "Keep selected trial files independent"
    packet["trial_rule_draft"]["core_principle"] = (
        "Emit one independently understandable additional-stage artifact for each selected topic."
    )
    packet["proposed_additional_rule"]["name"] = "second"
    packet["proposed_additional_rule"]["relative_path"] = relative_path
    packet["proposed_additional_rule"]["display_path"] = f"<additional-root>/{relative_path}"
    return report


def controlled_additional_root(temp_root: str) -> Path:
    root = Path(temp_root) / "rules" / "additional"
    root.mkdir(parents=True)
    return root


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

    def test_packet_records_additional_trial_selection_without_main_rules_promotion(self) -> None:
        report = candidate_packet.build_candidate_packet(
            orchestration_report()["phase_013_candidate_input"],
            owner_domain="evidence-discipline",
            main_rule_target="rules/evidence-discipline.md",
            integration_anchors=["rules/accurate-communication.md"],
            selected_for_additional_trial=True,
        )

        self.assertTrue(report["selected_for_additional_trial"])
        self.assertFalse(report["main_rules_promotion_approved"])
        self.assertTrue(report["candidate_packet"]["selected_for_additional_trial"])
        self.assertFalse(report["candidate_packet"]["main_rules_promotion_approved"])
        self.assertEqual(
            report["candidate_packet"]["owner_domain_mapping"]["integration_anchors"],
            ["rules/accurate-communication.md"],
        )
        self.assertEqual(report["candidate_packet"]["candidate_entailment"]["decision"], "retain")
        self.assertTrue(report["candidate_packet"]["normalized_evidence_basis"])
        self.assertTrue(report["candidate_packet"]["trial_rule_draft"])

    def test_packet_rejects_context_only_or_unrelated_entailment(self) -> None:
        candidate_input = copy.deepcopy(orchestration_report()["phase_013_candidate_input"])
        candidate_input["trace_anchors"] = [
            {
                "signal_id": "signal-unrelated",
                "session_id": "session-z",
                "shard": "2026-05-17.md",
                "source_classes": ["trace_evidence"],
                "content_preview": "Unrelated evidence.",
            }
        ]

        report = candidate_packet.build_candidate_packet(
            candidate_input,
            owner_domain="evidence-discipline",
            main_rule_target="rules/evidence-discipline.md",
            selected_for_additional_trial=True,
        )

        packet = report["candidate_packet"]
        self.assertEqual(packet["candidate_entailment"]["decision"], "context-only")
        self.assertFalse(packet["candidate_entailment"]["eligible_for_additional_trial"])
        self.assertTrue(packet["stop_gates"])
        self.assertEqual(report["status"], "packet-built-with-stop-gates")

    def test_packet_narrows_partially_supported_mechanism_before_render(self) -> None:
        candidate_input = copy.deepcopy(orchestration_report()["phase_013_candidate_input"])
        topic = candidate_input["selected_topic"]
        topic["high_level_mechanism"] = "Rewrite every completion and release workflow globally."
        topic["candidate_entailment_basis"]["source_signal_ids"] = ["signal-001", "signal-002"]
        topic["source_signal_ids"] = ["signal-001", "signal-002"]
        topic["candidate_entailment_basis"]["supported_mechanism"] = (
            "Keep completion wording bounded to checked verification evidence."
        )

        report = candidate_packet.build_candidate_packet(
            candidate_input,
            owner_domain="evidence-discipline",
            main_rule_target="rules/evidence-discipline.md",
            selected_for_additional_trial=True,
        )

        packet = report["candidate_packet"]
        entailment = packet["candidate_entailment"]
        self.assertEqual(entailment["decision"], "narrow")
        self.assertTrue(entailment["eligible_for_additional_trial"])
        self.assertEqual(
            packet["trial_rule_draft"]["core_principle"],
            "Keep completion wording bounded to checked verification evidence.",
        )
        self.assertNotIn("Rewrite every completion", packet["trial_rule_draft"]["core_principle"])

    def test_rendered_artifact_has_complete_standalone_schema(self) -> None:
        material = candidate_packet.render_additional_rule(packet_report())
        validation = candidate_packet.validate_standalone_artifact(material)

        self.assertTrue(validation["valid"])
        self.assertEqual(validation["missing_headings"], [])
        self.assertEqual(validation["forbidden_dependencies"], [])
        self.assertIn("## Trial rule draft", material)
        self.assertIn("### Core principle", material)
        self.assertIn("### Draft operating clauses", material)
        self.assertIn("### Before behavior", material)
        self.assertIn("### After behavior", material)
        self.assertIn("Main RULES mutation:** Not performed", material)

    def test_rendered_artifact_excludes_ephemeral_evidence_dependencies(self) -> None:
        candidate_input = copy.deepcopy(orchestration_report()["phase_013_candidate_input"])
        candidate_input["trace_anchors"][0].update(
            {
                "shard": ".memsearch/memory/2026-08-09.md",
                "content_preview": "Reconstruct from /home/node/private/file.md:390 and transcript.jsonl",
            }
        )
        candidate_input["source_anchors"] = [
            {
                "source_type": "governance_context",
                "title": "/tmp/packet-report.json",
                "content_preview": "temporary packet evidence",
            }
        ]
        report = candidate_packet.build_candidate_packet(
            candidate_input,
            owner_domain="evidence-discipline",
            main_rule_target="rules/evidence-discipline.md",
            selected_for_additional_trial=True,
        )
        material = candidate_packet.render_additional_rule(report)
        validation = candidate_packet.validate_standalone_artifact(material)

        self.assertIn(
            ".memsearch/memory/2026-08-09.md",
            str(report["candidate_packet"]["signal_evidence_basis"]["trace_anchors"]),
        )
        self.assertTrue(validation["valid"])
        self.assertEqual(validation["forbidden_dependencies"], [])
        for forbidden in (
            ".memsearch",
            "/tmp/packet-report.json",
            "transcript.jsonl",
            "/home/node/private/file.md:390",
            "content_preview",
        ):
            self.assertNotIn(forbidden, material)

    def test_dry_run_emission_previews_without_write(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            packet = packet_report()
            preview = candidate_packet.emit_additional(packet, additional_root=str(additional_root))
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
            additional_root = controlled_additional_root(temp_root)
            packet = packet_report()
            emitted = candidate_packet.emit_additional(packet, additional_root=str(additional_root), approved_write=True)
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

    def test_existing_destination_is_always_rejected_and_bytes_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            packet = packet_report()
            first = candidate_packet.emit_additional(
                packet,
                additional_root=str(additional_root),
                approved_write=True,
            )
            destination = Path(first["destination_path"])
            original_bytes = destination.read_bytes()

            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(
                    packet,
                    additional_root=str(additional_root),
                    approved_write=True,
                )

            self.assertEqual(destination.read_bytes(), original_bytes)

    def test_selected_batch_writes_one_independent_artifact_per_topic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            report = candidate_packet.emit_selected_additional(
                [packet_report(), second_packet_report()],
                additional_root=str(additional_root),
                approved_write=True,
            )

            self.assertEqual(report["status"], "emitted")
            self.assertEqual(len(report["items"]), 2)
            destinations = [Path(item["destination_path"]) for item in report["items"]]
            self.assertEqual(len(set(destinations)), 2)
            self.assertTrue(all(path.exists() for path in destinations))
            first_material, second_material = [path.read_text(encoding="utf-8") for path in destinations]
            self.assertIn("topic-001", first_material)
            self.assertNotIn("topic-002", first_material)
            self.assertIn("topic-002", second_material)
            self.assertNotIn("topic-001", second_material)

    def test_batch_collision_rejects_entire_set_before_first_write_and_preserves_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            namespace = additional_root / "memory-context-intelligence"
            sentinel = namespace / "second.md"
            sentinel.parent.mkdir(parents=True)
            sentinel.write_bytes(b"existing-sentinel")

            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_selected_additional(
                    [
                        second_packet_report("memory-context-intelligence/first.md"),
                        second_packet_report(),
                    ],
                    additional_root=str(additional_root),
                    approved_write=True,
                )

            self.assertFalse((namespace / "first.md").exists())
            self.assertEqual(sentinel.read_bytes(), b"existing-sentinel")

    def test_duplicate_batch_destinations_are_rejected_before_write(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            first = second_packet_report("memory-context-intelligence/duplicate.md")
            second = second_packet_report("memory-context-intelligence/duplicate.md")

            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_selected_additional(
                    [first, second],
                    additional_root=str(additional_root),
                    approved_write=True,
                )

            self.assertFalse((additional_root / "memory-context-intelligence" / "duplicate.md").exists())

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
            additional_root = controlled_additional_root(temp_root)
            with self.assertRaises(candidate_packet.CandidatePacketError) as exc:
                candidate_packet.emit_additional(packet, additional_root=str(additional_root))

        self.assertIn("single selected topic", str(exc.exception))

    def test_additional_root_namespace_traversal_and_symlink_escape_fail_closed(self) -> None:
        with self.assertRaises(candidate_packet.CandidatePacketError):
            candidate_packet.build_candidate_packet(
                orchestration_report()["phase_013_candidate_input"],
                owner_domain="evidence-discipline",
                main_rule_target="rules/evidence-discipline.md",
                additional_relative_path="../bad.md",
            )

        packet = packet_report()
        wrong_namespace = copy.deepcopy(packet)
        wrong_namespace["candidate_packet"]["proposed_additional_rule"]["relative_path"] = "other/bad.md"
        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(
                    wrong_namespace,
                    additional_root=str(additional_root),
                    approved_write=True,
                )

        with tempfile.TemporaryDirectory() as temp_parent:
            main_rules_root = Path(temp_parent) / "rules"
            main_rules_root.mkdir()
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(
                    packet,
                    additional_root=str(main_rules_root),
                    approved_write=True,
                )

        with tempfile.TemporaryDirectory() as temp_root:
            root_parent = Path(temp_root) / "rules"
            root_parent.mkdir()
            outside = Path(temp_root) / "outside"
            outside.mkdir()
            additional_link = root_parent / "additional"
            additional_link.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(
                    packet,
                    additional_root=str(additional_link),
                    approved_write=True,
                )
            self.assertEqual(list(outside.iterdir()), [])

        with tempfile.TemporaryDirectory() as temp_root:
            additional_root = controlled_additional_root(temp_root)
            outside = Path(temp_root) / "outside"
            outside.mkdir()
            namespace = additional_root / "memory-context-intelligence"
            namespace.symlink_to(outside, target_is_directory=True)
            with self.assertRaises(candidate_packet.CandidatePacketError):
                candidate_packet.emit_additional(
                    packet,
                    additional_root=str(additional_root),
                    approved_write=True,
                )
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
