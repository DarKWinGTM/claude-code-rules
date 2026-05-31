#!/usr/bin/env python3
"""Focused checks for phase-012 bounded orchestration."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATION_PATH = PACKAGE_ROOT / "lib" / "orchestration.py"
SPEC = importlib.util.spec_from_file_location("mci_orchestration", ORCHESTRATION_PATH)
orchestration = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(orchestration)


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
                "why_surfaced": "Repeated bounded traces mentioned completion wording before verification.",
                "expected_behavior_impact": "Future candidate inputs preserve evidence limits.",
                "high_level_mechanism": "Use lane findings before candidate-packet construction.",
                "expected_output": "A bounded candidate input model for later phase-013 use.",
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
            "research_need": {
                "needed": True,
                "reason": "This topic depends on broader source-trust and verification practice.",
            },
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
        "name": "phase-012-strong-source-fixture",
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


def conflicting_source_fixture() -> dict:
    fixture = strong_source_fixture()
    fixture["sources"].append(
        {
            "id": "weak-blog",
            "title": "Anecdotal blog with broad completion claims",
            "source_type": "blog",
            "freshness": "unknown",
            "supports": ["Treat local checks as production proof."],
            "constraints": ["Always call local edits fixed immediately."],
            "conflicts": ["Conflicts with evidence-scope wording and live-provider boundaries."],
            "limitations": ["Anecdotal and not source-of-truth guidance."],
        }
    )
    return fixture


class OrchestrationTests(unittest.TestCase):
    def test_trace_only_path_returns_bounded_lane_findings(self) -> None:
        report = orchestration.build_orchestration(
            intake_report=intake_report(),
            signals_report=signals_report(),
        )

        self.assertEqual(report["status"], "trace-only-orchestrated")
        self.assertEqual(report["orchestration_result_model"], "phase-012-bounded-native-agent-lanes-v1")
        self.assertEqual(report["lane_order"], list(orchestration.LANE_ORDER))
        self.assertEqual(len(report["lane_findings"]), 4)
        self.assertFalse(report["phase_013_candidate_input"]["candidate_packet_built"])
        self.assertFalse(report["phase_013_candidate_input"]["additional_emission_performed"])
        self.assertFalse(report["phase_013_candidate_input"]["main_rules_mutation_performed"])
        self.assertFalse(report["phase_013_candidate_input"]["selected_topic"])
        self.assertFalse(report["result_summary"]["phase_013_candidate_input_ready"])
        self.assertTrue(report["native_agent_orchestration_performed"])
        self.assertEqual(report["native_agent_orchestration_mode"], "runtime-local-simulation")
        self.assertFalse(report["external_agent_process_spawned"])
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["main_rules_mutation_performed"])

        trace = report["lane_findings"][0]
        self.assertEqual(trace["lane_name"], "Trace Scout")
        self.assertEqual(trace["status"], "findings-available")
        self.assertTrue(trace["checked_scope"])
        self.assertTrue(trace["anchors"])
        self.assertTrue(trace["source_basis"])
        self.assertTrue(trace["leader_verification_needs"])

    def test_selected_topic_with_enrichment_is_ready_for_phase_013_input(self) -> None:
        report = orchestration.build_orchestration(
            intake_report=intake_report(),
            signals_report=signals_report(),
            selection_report=selection_report(),
            source_fixture=strong_source_fixture(),
        )

        self.assertEqual(report["status"], "orchestrated")
        self.assertEqual(report["selected_topic_id"], "topic-001")
        self.assertTrue(report["result_summary"]["phase_013_candidate_input_ready"])
        self.assertEqual(report["result_summary"]["stop_gate_count"], 0)
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["main_rules_mutation_performed"])
        self.assertFalse(report["install_or_publication_performed"])

        lane_statuses = {lane["lane_id"]: lane["status"] for lane in report["lane_findings"]}
        self.assertEqual(lane_statuses["trace-scout"], "findings-available")
        self.assertEqual(lane_statuses["research-scout"], "research-enriched")
        self.assertEqual(lane_statuses["source-trust-reviewer"], "reviewed")
        self.assertEqual(lane_statuses["synthesis-lead"], "ready-for-phase-013-input")

        phase_013_input = report["phase_013_candidate_input"]
        self.assertEqual(phase_013_input["selected_topic"]["id"], "topic-001")
        self.assertTrue(phase_013_input["trace_anchors"])
        self.assertTrue(phase_013_input["source_anchors"])
        self.assertFalse(phase_013_input["candidate_packet_built"])

    def test_conflict_and_uncertainty_reporting_creates_stop_gate(self) -> None:
        report = orchestration.build_orchestration(
            intake_report=intake_report(),
            signals_report=signals_report(),
            selection_report=selection_report(),
            source_fixture=conflicting_source_fixture(),
        )

        self.assertEqual(report["status"], "orchestrated-with-stop-gates")
        self.assertGreater(report["result_summary"]["stop_gate_count"], 0)
        self.assertGreater(report["result_summary"]["conflict_or_uncertainty_count"], 0)

        source_trust = next(
            lane for lane in report["lane_findings"] if lane["lane_id"] == "source-trust-reviewer"
        )
        self.assertIn(
            "leader must resolve source conflicts before strengthening candidate claims",
            source_trust["stop_gates"],
        )
        self.assertTrue(
            any("Explicit source conflicts" in item for item in source_trust["conflicts_uncertainty"])
        )
        self.assertFalse(report["phase_013_candidate_input"]["candidate_packet_built"])
        self.assertFalse(report["phase_013_candidate_input"]["additional_emission_performed"])

    def test_orchestration_does_not_write_additional(self) -> None:
        additional_path = PACKAGE_ROOT / "additional"
        before = additional_path.exists()
        report = orchestration.build_orchestration(
            intake_report=intake_report(),
            signals_report=signals_report(),
            selection_report=selection_report(),
            source_fixture=strong_source_fixture(),
        )
        after = additional_path.exists()

        self.assertEqual(before, after)
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["main_rules_mutation_performed"])


if __name__ == "__main__":
    unittest.main()
