#!/usr/bin/env python3
"""Focused checks for optional research enrichment."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
RESEARCH_PATH = PACKAGE_ROOT / "lib" / "research_enrichment.py"
SPEC = importlib.util.spec_from_file_location("mci_research_enrichment", RESEARCH_PATH)
research_enrichment = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(research_enrichment)


def selection_report(*, research_need: object) -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "choose",
        "status": "selected",
        "selected_topic_id": "topic-001",
        "selected_topic": {
            "rank": 1,
            "id": "topic-001",
            "title": "Strengthen evidence discipline around completion claims",
            "purpose": "Keep local memory signals separate from external best practice support.",
            "why_surfaced": "2 bounded intake records mentioned fixed/stable wording before verification.",
            "expected_behavior_impact": "Future candidate packets could carry clearer source-trust limits.",
            "high_level_mechanism": "Use a selected topic report and bounded source records before packet building.",
            "expected_output": "An enriched evidence summary that keeps weak sources from becoming constraints.",
            "confidence": "medium",
            "evidence_label": "bounded-repeated-observed-local",
            "source_signal_ids": ["signal-001"],
            "research_need": research_need,
            "selected": True,
            "advisory_only": False,
            "carry_forward_allowed": True,
        },
        "unselected_topics": [],
        "selection_required_before_carry_forward": False,
        "carry_forward_allowed": True,
        "research_enrichment_performed": False,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def source_fixture() -> dict:
    return {
        "name": "controlled-source-fixture",
        "recorded_at": "2026-05-18",
        "sources": [
            {
                "id": "official-docs",
                "title": "Official documentation on evidence-strength wording",
                "source_type": "official_docs",
                "freshness": "current",
                "checked_at": "2026-05-18",
                "supports": ["Completion wording should identify checked scope and evidence limits."],
                "constraints": ["Do not call behavior fixed without verification covering the failure scope."],
            },
            {
                "id": "engineering-guide",
                "title": "Engineering guidance on verification notes",
                "source_type": "engineering_guide",
                "freshness": "current",
                "supports": ["Verification notes should separate local checks from live provider checks."],
            },
            {
                "id": "weak-blog",
                "title": "Personal blog with broad claims",
                "source_type": "blog",
                "freshness": "unknown",
                "supports": ["Always use one-word completion labels."],
                "constraints": ["Treat every local test as production proof."],
                "conflicts": ["Conflicts with evidence-scope wording and live-provider boundaries."],
                "limitations": ["Anecdotal and not source-of-truth guidance."],
            },
        ],
    }


class ResearchEnrichmentTests(unittest.TestCase):
    def test_no_research_needed_path_skips_with_reason(self) -> None:
        report = research_enrichment.build_enrichment(
            selection_report(
                research_need={
                    "needed": False,
                    "reason": "Purely local naming and path convention topic.",
                }
            )
        )

        self.assertEqual(report["status"], "research-skipped")
        self.assertEqual(report["enrichment_decision"]["gate_result"], "skip-research")
        self.assertFalse(report["source_query_plan"]["required"])
        self.assertFalse(report["research_enrichment_performed"])
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["main_rules_mutation_performed"])

    def test_research_needed_path_uses_controlled_sources(self) -> None:
        report = research_enrichment.build_enrichment(
            selection_report(
                research_need={
                    "needed": True,
                    "reason": "The topic depends on broader source-trust and verification practice.",
                }
            ),
            source_fixture=source_fixture(),
        )

        self.assertEqual(report["status"], "research-enriched")
        self.assertEqual(report["enrichment_decision"]["gate_result"], "research-needed")
        self.assertTrue(report["source_query_plan"]["required"])
        self.assertTrue(report["research_enrichment_performed"])
        self.assertTrue(report["controlled_source_fixture_used"])
        self.assertFalse(report["live_web_access_performed"])
        self.assertFalse(report["native_agent_orchestration_performed"])
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["main_rules_mutation_performed"])
        self.assertIn("official-docs", report["source_trust_notes"]["strong_sources"])
        self.assertIn("weak-blog", report["source_trust_notes"]["weak_sources"])
        self.assertTrue(report["freshness_notes"]["source_freshness"])
        self.assertTrue(report["enriched_topic_summary"]["external_support"])

    def test_weak_and_conflicting_sources_do_not_become_hard_constraints(self) -> None:
        report = research_enrichment.build_enrichment(
            selection_report(research_need={"needed": True, "reason": "Needs broader support."}),
            source_fixture=source_fixture(),
        )

        constraints = report["enriched_topic_summary"]["hard_constraints_from_external_support"]
        constraint_text = "\n".join(item["constraint"] for item in constraints)
        self.assertIn("Do not call behavior fixed without verification", constraint_text)
        self.assertNotIn("Treat every local test as production proof", constraint_text)
        self.assertTrue(report["conflict_handling"]["conflicts_found"])
        self.assertIn("weak-blog", report["conflict_handling"]["weak_conflicting_sources"])
        self.assertIn("cannot create hard constraints", report["source_trust_notes"]["weak_source_handling"])

    def test_enrichment_does_not_write_additional(self) -> None:
        additional_path = PACKAGE_ROOT / "additional"
        before = additional_path.exists()
        report = research_enrichment.build_enrichment(
            selection_report(research_need={"needed": True, "reason": "Needs broader support."}),
            source_fixture=source_fixture(),
        )
        after = additional_path.exists()

        self.assertEqual(before, after)
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["candidate_packet_built"])
        self.assertFalse(report["main_rules_mutation_performed"])


if __name__ == "__main__":
    unittest.main()
