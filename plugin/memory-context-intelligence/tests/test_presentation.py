#!/usr/bin/env python3
"""Focused checks for topic presentation and choose flow."""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
PRESENTATION_PATH = PACKAGE_ROOT / "lib" / "presentation.py"
SPEC = importlib.util.spec_from_file_location("mci_presentation", PRESENTATION_PATH)
presentation = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(presentation)


def signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "topic_candidates": [
            {
                "rank": 1,
                "id": "topic-001",
                "title": "Rewrite /memory-context-intelligence:analysis first response into operator-facing proposal output",
                "purpose": "Keep DATABASE_URL, MCI_MEMORY_ROOT, and <repo-root>/plugin/memory-context-intelligence exact when discussing runtime config.",
                "why_surfaced": "2 bounded intake records referenced bash ./bin/memory-context-intelligence signals --intake-report <intake-report.json>.",
                "expected_behavior_impact": "Future responses preserve canonical identifiers instead of translating DATABASE_URL or MCI_MEMORY_ROOT.",
                "high_level_mechanism": "Render the topic list without modifying technical identifiers, file paths, commands, or env vars.",
                "expected_output": "A selected topic candidate that still contains topic-001 and the exact command text.",
                "research_need": "Not evaluated in phase 010; research enrichment is a later phase and must not start before the user selects a topic.",
                "provenance_note": "Historical trace evidence is the primary signal. 3 trace record(s) across 3 session(s) and 3 shard(s). Latest seen: 2026-05-20. Current-session confirmation: historical-only. Source mix: trace_evidence + recall_evidence + durable_memory_context + governance_context.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence + recall_evidence + durable_memory_context + governance_context",
                "historical_strength": "3 trace record(s) across 3 session(s) and 3 shard(s)",
                "latest_seen": "2026-05-20",
                "current_session_confirmation": "historical-only",
                "source_classes": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                "source_session_ids": ["current-session"],
                "same_day_widened": False,
                "confidence": "medium",
                "evidence_label": "bounded-repeated-observed-local",
                "source_signal_ids": ["signal-001"],
            },
            {
                "rank": 2,
                "id": "topic-002",
                "title": "Clarify blocker handling for missing approval",
                "purpose": "Expose stop gates before unsafe continuation.",
                "why_surfaced": "2 bounded intake records mentioned approval blockers.",
                "expected_behavior_impact": "Future workflow could ask for approval before high-impact work.",
                "high_level_mechanism": "Keep blocker-shaped topics visible but advisory until selected.",
                "expected_output": "A reviewed blocker topic candidate.",
                "confidence": "medium",
                "evidence_label": "bounded-repeated-observed-local",
                "source_signal_ids": ["signal-002"],
            },
        ],
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def no_topic_signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "source": {
            "intake_mode": "intake",
            "intake_status": "available",
            "records_received": 8,
            "bounded_subset_only": True,
        },
        "ranked_signals": [
            {
                "rank": 1,
                "id": "signal-001",
                "label": "Recurring Pattern: skill, memsearch, plugin",
                "score": 0.35,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "review_focus": "surface-boundary",
                "provenance_note": "Current-session-only evidence from session current-session; same-day widening was not used.",
                "source_scope_label": "current-session-only",
            }
        ],
        "topic_candidates": [],
        "limits": {
            "records_analyzed": 8,
            "signals_ranked": 8,
            "topics_promoted": 0,
        },
        "notes": [
            "Weak, stale, insufficient, or single-observation inputs stay low-confidence and do not produce promoted topics by default."
        ],
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def breadth_signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "ranked_signals": [
            {
                "rank": 1,
                "id": "signal-001",
                "label": "Correction: completion, verification",
                "score": 0.94,
                "confidence": "high",
                "evidence_label": "bounded-repeated-multi-shard",
                "source_scope_label": "historical-default",
                "historical_strength": "3 trace record(s) across 3 session(s) and 3 shard(s)",
                "current_session_confirmation": "historical-only",
            },
            {
                "rank": 2,
                "id": "signal-002",
                "label": "Recurring Pattern: workflow, wording",
                "score": 0.41,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "source_scope_label": "historical-default",
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "current_session_confirmation": "historical-only",
            },
        ],
        "topic_candidates": [signals_report()["topic_candidates"][0]],
        "limits": {
            "records_analyzed": 5,
            "signals_ranked": 2,
            "topics_promoted": 1,
        },
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def sparse_ranked_signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "ranked_signals": [
            {
                "rank": 1,
                "id": "signal-101",
                "kind": "correction",
                "group": "corrections",
                "label": "Correction: completion, verification",
                "score": 0.43,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "record_count": 2,
                "keywords": ["completion", "verification"],
                "review_focus": "workflow-review",
                "source_session_ids": ["session-a"],
                "source_scope_label": "historical-default",
                "source_classes": ["trace_evidence"],
                "source_mix_label": "trace_evidence",
                "trace_record_count": 2,
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-20",
                "current_session_confirmation": "historical-only",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-20. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "records": [],
            },
            {
                "rank": 2,
                "id": "signal-102",
                "kind": "blocker",
                "group": "blockers",
                "label": "Blocker: approval, stop gate",
                "score": 0.39,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "record_count": 2,
                "keywords": ["approval", "stop", "gate"],
                "review_focus": "workflow-review",
                "source_session_ids": ["session-b"],
                "source_scope_label": "historical-default",
                "source_classes": ["trace_evidence"],
                "source_mix_label": "trace_evidence",
                "trace_record_count": 2,
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-19",
                "current_session_confirmation": "historical-only",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-19. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "records": [],
            },
            {
                "rank": 3,
                "id": "signal-103",
                "kind": "evidence_gap",
                "group": "corrections",
                "label": "Evidence gap: refresh, wait guidance",
                "score": 0.37,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "record_count": 2,
                "keywords": ["refresh", "wait", "guidance"],
                "review_focus": "evidence-boundary",
                "source_session_ids": ["session-c"],
                "source_scope_label": "historical-default",
                "source_classes": ["trace_evidence"],
                "source_mix_label": "trace_evidence",
                "trace_record_count": 2,
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-18",
                "current_session_confirmation": "historical-only",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-18. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "records": [],
            },
        ],
        "topic_candidates": [],
        "advisory_fallback_topics": [
            {
                "rank": 1,
                "id": "topic-001",
                "title": "Stop completion wording from outrunning verification",
                "purpose": "Convert repeated user corrections into a candidate behavior adjustment without treating the correction as doctrine yet.",
                "why_surfaced": "2 bounded intake record(s) clustered as a correction signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Future behavior could avoid repeating the corrected mistake if the topic later becomes a vetted candidate.",
                "high_level_mechanism": "Cluster correction-shaped records, preserve evidence labels, and propose an internal topic only when the pattern is repeated enough.",
                "expected_output": "A reviewed topic candidate that can later be presented for user selection before any candidate packet is built.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-20. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-a"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-20",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-101"],
            },
            {
                "rank": 2,
                "id": "topic-002",
                "title": "Clarify stop-gate handling before approval-sensitive work",
                "purpose": "Expose recurring blockers that may need clearer workflow gates, recovery paths, or ownership boundaries.",
                "why_surfaced": "2 bounded intake record(s) clustered as a blocker signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Future workflow could surface stop gates earlier and reduce blocked or unsafe continuation.",
                "high_level_mechanism": "Cluster blocker-shaped records and map them to a possible workflow gate or recovery-path improvement.",
                "expected_output": "A reviewed topic candidate for clearer stop-gate, blocker, or recovery handling.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-19. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-b"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-19",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-102"],
            },
            {
                "rank": 3,
                "id": "topic-003",
                "title": "Clarify refresh and wait guidance before strong evidence claims",
                "purpose": "Highlight places where weak, stale, or missing evidence should keep future claims cautious.",
                "why_surfaced": "2 bounded intake record(s) clustered as a evidence gap signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Future responses could downgrade confidence sooner and ask for or gather evidence before strong claims.",
                "high_level_mechanism": "Cluster evidence-gap records and cap promotion when the source input is stale, weak, or single-observation only.",
                "expected_output": "A reviewed topic candidate for evidence discipline, confidence labeling, or recheck behavior.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-18. Current-session confirmation: historical-only. Source mix: trace_evidence.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-c"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-18",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-103"],
            },
        ],
        "limits": {
            "records_analyzed": 17,
            "signals_ranked": 15,
            "topics_promoted": 0,
        },
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def doctrine_lifted_config_signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "topic_candidates": [],
        "advisory_fallback_topics": [
            {
                "rank": 1,
                "id": "topic-001",
                "title": "Verify semantic fit before reusing an existing control surface",
                "purpose": "Review whether an existing config or control surface actually governs the intended runtime behavior before proposing reuse.",
                "why_surfaced": "Config investigation traces around supplierApiDomainProbe, passStatusCodes, and opera_fallback were lifted into a doctrine-level semantic-fit review topic.",
                "expected_behavior_impact": "Future recommendations can distinguish an available control from a semantically correct control before proposing reuse.",
                "high_level_mechanism": "Lift config-like incident traces into a semantic-boundary doctrine lens before title generation.",
                "expected_output": "A reviewed topic candidate that checks semantic fit before reusing a control surface.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-20. Current-session confirmation: historical-only. Source mix: trace_evidence. Example details: supplierApiDomainProbe, passStatusCodes, 404, opera_fallback.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-a"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-20",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-201"],
            },
            {
                "rank": 2,
                "id": "topic-002",
                "title": "Separate symptom evidence from strategic fix scope",
                "purpose": "Review whether incident symptoms are being turned into strategic fix scope too early.",
                "why_surfaced": "The same config investigation traces showed symptom-level evidence like 404 being used too directly as fix direction.",
                "expected_behavior_impact": "Future recommendations can keep symptom evidence and strategic scope selection separate until the mechanism is checked.",
                "high_level_mechanism": "Lift symptom-shaped traces into a strategic-scope doctrine lens before topic generation.",
                "expected_output": "A reviewed topic candidate that keeps symptom evidence separate from strategic fix scope.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-19. Current-session confirmation: historical-only. Source mix: trace_evidence. Example details: 404, config-only change, code path work.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-b"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-19",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-202"],
            },
            {
                "rank": 3,
                "id": "topic-003",
                "title": "Require source-backed behavior verification before choosing config-only remediation",
                "purpose": "Review whether source inspection actually proves a config-only path before a recommendation narrows there.",
                "why_surfaced": "The config investigation traces included grep, settings reads, and config/doc comparisons that should stay as evidence rather than surface-level issue wording.",
                "expected_behavior_impact": "Future recommendations can verify behavior ownership first before choosing config-only remediation.",
                "high_level_mechanism": "Lift source-check traces into an evidence-discipline doctrine lens before title generation.",
                "expected_output": "A reviewed topic candidate that requires source-backed behavior verification before config-only remediation.",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s). Latest seen: 2026-05-18. Current-session confirmation: historical-only. Source mix: trace_evidence. Example details: grep, supplierApiDomainProbe, passStatusCodes, opera_fallback.",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "source_classes": ["trace_evidence"],
                "source_session_ids": ["session-c"],
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-18",
                "current_session_confirmation": "historical-only",
                "same_day_widened": False,
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "promotion_tier": "advisory-fallback",
                "source_signal_ids": ["signal-203"],
            },
        ],
        "limits": {
            "records_analyzed": 4,
            "signals_ranked": 3,
            "topics_promoted": 0,
        },
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def same_family_signals_report() -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": "available",
        "topic_candidates": [
            {
                "rank": 1,
                "id": "topic-001",
                "title": "Turn recurring workflow findings into decision-ready proposals — goal framing",
                "purpose": "Convert repeated workflow findings into proposals the user can decide on immediately.",
                "why_surfaced": "2 bounded intake record(s) clustered as a recurring pattern signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Future workflow reviews can end with a decision-ready proposal instead of a weak summary.",
                "high_level_mechanism": "Group same-family workflow findings under one stronger primary proposal.",
                "expected_output": "A primary proposal topic for the strongest same-family candidate.",
                "evidence_examples": ["Workflow finding should be carried forward as a goal-level proposal rather than left as a weak trace summary."],
                "before_behavior": "Recurring workflow findings are summarized as observations instead of decision-ready proposals.",
                "after_behavior": "Recurring workflow findings become a goal-level proposal the user can act on immediately.",
                "evidence_summary": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s).",
                "provenance_note": "Historical trace evidence is the primary signal. 2 trace record(s) across 1 session(s) and 1 shard(s).",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-30",
                "current_session_confirmation": "historical-only",
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "source_signal_ids": ["signal-301"],
            },
            {
                "rank": 2,
                "id": "topic-002",
                "title": "Turn recurring workflow findings into decision-ready proposals — goal framing",
                "purpose": "A weaker same-family variant of the primary goal-framing topic.",
                "why_surfaced": "1 bounded intake record(s) clustered as a recurring pattern signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Same-family variant with weaker evidence.",
                "high_level_mechanism": "Same-family variant.",
                "expected_output": "A compressed related variant.",
                "provenance_note": "Historical trace evidence is the primary signal. 1 trace record(s) across 1 session(s) and 1 shard(s).",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "historical_strength": "1 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-30",
                "current_session_confirmation": "historical-only",
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "source_signal_ids": ["signal-302"],
            },
            {
                "rank": 3,
                "id": "topic-003",
                "title": "Turn recurring workflow findings into decision-ready proposals — workflow",
                "purpose": "A workflow-level variant of the same family.",
                "why_surfaced": "1 bounded intake record(s) clustered as a recurring pattern signal with evidence label bounded-single-observation-low-confidence.",
                "expected_behavior_impact": "Same-family workflow variant with weaker evidence.",
                "high_level_mechanism": "Same-family variant.",
                "expected_output": "A compressed related variant.",
                "provenance_note": "Historical trace evidence is the primary signal. 1 trace record(s) across 1 session(s) and 1 shard(s).",
                "source_scope_label": "historical-default",
                "source_mix_label": "trace_evidence",
                "historical_strength": "1 trace record(s) across 1 session(s) and 1 shard(s)",
                "latest_seen": "2026-05-30",
                "current_session_confirmation": "historical-only",
                "confidence": "low",
                "evidence_label": "bounded-single-observation-low-confidence",
                "source_signal_ids": ["signal-303"],
            },
        ],
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


class TopicPresentationTests(unittest.TestCase):
    def test_renders_sample_topic_cards_in_each_output_mode(self) -> None:
        for mode in ("auto", "native-first", "bilingual", "fixed"):
            with self.subTest(mode=mode):
                rendered = presentation.build_presentation(signals_report(), output_mode=mode, language="th")

                self.assertEqual(rendered["mode"], "present")
                self.assertEqual(rendered["output_mode"], mode)
                self.assertEqual(rendered["active_language"], "th")
                self.assertEqual(rendered["status"], "available")
                self.assertEqual(len(rendered["topic_cards"]), 2)
                self.assertTrue(rendered["heading"])
                self.assertTrue(rendered["choice_prompt"])
                self.assertFalse(rendered["choose_flow_performed"])
                self.assertFalse(rendered["research_enrichment_performed"])
                self.assertFalse(rendered["candidate_packet_built"])
                self.assertFalse(rendered["additional_emission_performed"])
                self.assertFalse(rendered["main_rules_mutation_performed"])

    def test_preserves_canonical_identifiers_exactly(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="bilingual", language="th")
        rendered_text = json.dumps(rendered, ensure_ascii=False)

        for exact_value in (
            "DATABASE_URL",
            "MCI_MEMORY_ROOT",
            "<repo-root>/plugin/memory-context-intelligence",
            "bash ./bin/memory-context-intelligence signals --intake-report <intake-report.json>",
            "topic-001",
        ):
            self.assertIn(exact_value, rendered_text)

    def test_user_selection_required_before_carry_forward(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="native-first", language="en")

        self.assertTrue(rendered["selection_required_before_carry_forward"])
        self.assertFalse(rendered["carry_forward_allowed"])
        self.assertIsNone(rendered["selected_topic_id"])
        self.assertTrue(all(topic["advisory_only"] for topic in rendered["topic_cards"]))
        self.assertTrue(all(not topic["carry_forward_allowed"] for topic in rendered["topic_cards"]))

        selected = presentation.build_selection(signals_report(), topic_id="topic-001", output_mode="native-first", language="en")
        self.assertEqual(selected["selected_topic_id"], "topic-001")
        self.assertFalse(selected["selection_required_before_carry_forward"])
        self.assertTrue(selected["carry_forward_allowed"])
        self.assertTrue(selected["selected_topic"]["carry_forward_allowed"])

    def test_topic_cards_preserve_provenance_visibility(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="native-first", language="en")
        topic = rendered["topic_cards"][0]

        self.assertEqual(topic["current_session_confirmation"], "historical-only")
        self.assertEqual(topic["historical_strength"], "3 trace record(s) across 3 session(s) and 3 shard(s)")
        self.assertEqual(topic["latest_seen"], "2026-05-20")
        self.assertEqual(topic["source_mix_label"], "trace_evidence + recall_evidence + durable_memory_context + governance_context")
        self.assertIn("Historical trace evidence", topic["evidence_summary"])

    def test_unselected_topics_remain_advisory_only(self) -> None:
        selected = presentation.build_selection(signals_report(), topic_id="topic-001", output_mode="auto", language="en")

        self.assertTrue(selected["choose_flow_performed"])
        self.assertEqual(selected["status"], "selected")
        self.assertFalse(selected["research_enrichment_performed"])
        self.assertFalse(selected["candidate_packet_built"])
        self.assertFalse(selected["additional_emission_performed"])
        self.assertFalse(selected["main_rules_mutation_performed"])
        self.assertEqual([topic["id"] for topic in selected["unselected_topics"]], ["topic-002"])
        self.assertTrue(all(topic["advisory_only"] for topic in selected["unselected_topics"]))
        self.assertTrue(all(not topic["carry_forward_allowed"] for topic in selected["unselected_topics"]))
        self.assertFalse(selected["selected_topic"]["advisory_only"])

    def test_topic_cards_use_human_readable_sections_and_localized_title(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="native-first", language="th")

        self.assertEqual(
            rendered["topic_cards"][0]["title"],
            "ทำให้คำตอบแรกของ /memory-context-intelligence:analysis ใช้งานได้ทันที",
        )
        card_labels = [section["label"] for section in rendered["topic_cards"][0]["sections"]]
        self.assertEqual(
            card_labels,
            [
                "มันคืออะไร",
                "อาการ/ปัญหา",
                "ก่อนปรับ (Before behavior)",
                "หลังปรับ (After behavior)",
                "ถ้าปรับแล้วจะดีขึ้นยังไง",
                "หลักฐานที่ใช้",
                "สถานะตอนนี้",
            ],
        )

    def test_topic_cards_localize_known_doctrine_explanation_values_in_thai(self) -> None:
        report = {
            "tool": "memory-context-intelligence",
            "mode": "signals",
            "status": "available",
            "topic_candidates": [
                {
                    "rank": 1,
                    "id": "topic-001",
                    "title": "Clarify evidence wording before strong claims",
                    "purpose": "Highlight places where weak, stale, or missing evidence should keep future claims cautious.",
                    "why_surfaced": "1 bounded intake record(s) clustered as an evidence gap signal.",
                    "expected_behavior_impact": "Future responses could downgrade confidence sooner and ask for or gather evidence before strong claims.",
                    "before_behavior": "Let answers drift toward stronger claims before separating what is a verified fact, what is an inference, and what is still only a working hypothesis.",
                    "after_behavior": "Keep the confidence wording explicit so the user can distinguish verified fact, inference, and working hypothesis before treating the claim as settled.",
                    "confidence": "low",
                    "evidence_label": "bounded-single-observation-low-confidence",
                    "source_signal_ids": ["signal-401"],
                },
                {
                    "rank": 2,
                    "id": "topic-002",
                    "title": "Turn recurring workflow findings into decision-ready proposals",
                    "purpose": "Expose recurring blockers that may need clearer workflow gates, recovery paths, or ownership boundaries.",
                    "why_surfaced": "1 bounded intake record(s) clustered as a blocker signal.",
                    "expected_behavior_impact": "Future workflow could surface stop gates earlier and reduce blocked or unsafe continuation.",
                    "before_behavior": "Surface workflow findings as blocker-shaped observations without turning them into a decision-ready next step the user can act on immediately.",
                    "after_behavior": "Turn the workflow finding into a decision-ready proposal with a clearer gate and a more usable next step instead of leaving it as a loose observation.",
                    "confidence": "low",
                    "evidence_label": "bounded-single-observation-low-confidence",
                    "source_signal_ids": ["signal-402"],
                },
            ],
            "choose_flow_performed": False,
            "external_research_performed": False,
            "additional_emission_performed": False,
            "main_rules_mutation_performed": False,
        }

        rendered = presentation.build_presentation(report, output_mode="native-first", language="th")
        first_card_sections = {section["label"]: section["value"] for section in rendered["topic_cards"][0]["sections"]}
        second_card_sections = {section["label"]: section["value"] for section in rendered["topic_cards"][1]["sections"]}

        self.assertEqual(rendered["topic_cards"][0]["title"], "ทำให้ถ้อยคำเรื่องหลักฐานชัดก่อนสรุปแรง")
        self.assertIn("แยก fact, inference", first_card_sections["มันคืออะไร"])
        self.assertIn("ถ้อยคำแรงเกินไป", first_card_sections["อาการ/ปัญหา"])
        self.assertIn("เปิดเผยระดับความมั่นใจตั้งแต่ต้น", first_card_sections["หลังปรับ (After behavior)"])

        self.assertEqual(rendered["topic_cards"][1]["title"], "เปลี่ยน workflow finding ที่เกิดซ้ำให้เป็นข้อเสนอที่ตัดสินใจต่อได้ทันที")
        self.assertIn("ข้อเสนอที่ผู้ใช้ตัดสินใจต่อได้ทันที", second_card_sections["มันคืออะไร"])
        self.assertIn("next step หรือ proposal", second_card_sections["อาการ/ปัญหา"])
        self.assertIn("ตัดสินใจต่อได้ทันที", second_card_sections["หลังปรับ (After behavior)"])

    def test_topic_cards_render_evidence_examples_and_before_after_when_present(self) -> None:
        report = signals_report()
        report["topic_candidates"][0].update(
            {
                "evidence_examples": [
                    "Claude Code said it would check whether supplierApiDomainProbe already has a config field that keeps 404 away from opera_fallback.",
                    "Claude Code concluded putting 404 in passStatusCodes would be the wrong semantic because it would turn 404 into a pass.",
                ],
                "before_behavior": "See `passStatusCodes`, add `404`, and conclude the existing config is sufficient without first checking whether that control surface actually governs fallback eligibility.",
                "after_behavior": "Check whether the existing control surface really owns the runtime behavior; if it does not, keep `404` as evidence and lift the recommendation to control ownership or strategic fix scope instead of reusing the nearest config field.",
                "evidence_summary": "Historical trace evidence is the primary signal. Trace example: `supplierApiDomainProbe` / `passStatusCodes` was inspected while `404` and `opera_fallback` were being used to reason about fallback behavior.",
            }
        )

        rendered = presentation.build_presentation(report, output_mode="native-first", language="en")
        card_sections = rendered["topic_cards"][0]["sections"]
        section_map = {section["label"]: section["value"] for section in card_sections}

        self.assertIn("Evidence examples", section_map)
        self.assertIn("Before behavior", section_map)
        self.assertIn("After behavior", section_map)
        self.assertIn("supplierApiDomainProbe", section_map["Evidence examples"])
        self.assertIn("passStatusCodes", section_map["Before behavior"])
        self.assertIn("keep `404` as evidence", section_map["After behavior"])
        self.assertIn("Trace example:", section_map["Evidence used"])

    def test_topic_cards_add_compact_before_after_previews_even_when_preview_examples_are_absent(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="native-first", language="en")
        card_sections = rendered["topic_cards"][0]["sections"]
        card_labels = [section["label"] for section in card_sections]
        card_blob = json.dumps(card_sections, ensure_ascii=False)

        self.assertNotIn("Evidence examples", card_labels)
        self.assertIn("Before behavior", card_labels)
        self.assertIn("After behavior", card_labels)
        self.assertIn("manual rewrite", card_blob)
        self.assertIn("human-readable topic titles", card_blob)
        self.assertNotIn("supplierApiDomainProbe", card_blob)
        self.assertNotIn("opera_fallback", card_blob)

    def test_topic_cards_expose_status_provenance_and_source_mix(self) -> None:
        rendered = presentation.build_presentation(signals_report(), output_mode="native-first", language="en")
        topic_card = rendered["topic_cards"][0]

        self.assertEqual(topic_card["status_line"], "candidate only; advisory only; not approved yet")
        self.assertEqual(topic_card["source_mix_label"], "trace_evidence + recall_evidence + durable_memory_context + governance_context")
        self.assertEqual(topic_card["current_session_confirmation"], "historical-only")
        self.assertIn("Historical trace evidence", topic_card["evidence_summary"])

    def test_sparse_history_still_surfaces_three_advisory_topic_cards(self) -> None:
        rendered = presentation.build_presentation(sparse_ranked_signals_report(), output_mode="native-first", language="en")

        self.assertEqual(rendered["status"], "available")
        self.assertGreaterEqual(len(rendered["topic_cards"]), 3)
        self.assertTrue(rendered["topic_cards"][0]["recommended_first"])
        self.assertEqual(rendered["topic_cards"][0]["status_line"], "candidate only; advisory only; not approved yet")
        self.assertEqual(rendered["topic_cards"][0]["current_session_confirmation"], "historical-only")
        self.assertEqual(rendered["topic_cards"][0]["confidence"], "low")

    def test_same_family_topics_are_rendered_as_repeated_topic_cards(self) -> None:
        rendered = presentation.build_presentation(same_family_signals_report(), output_mode="native-first", language="en")

        self.assertEqual([card["id"] for card in rendered["topic_cards"]], ["topic-001", "topic-002", "topic-003"])
        self.assertTrue(rendered["topic_cards"][0]["recommended_first"])
        self.assertTrue(all(card["family_key"] == "Turn recurring workflow findings into decision-ready proposals" for card in rendered["topic_cards"]))

    def test_default_output_uses_repeated_topic_cards_instead_of_meta_wrapper_sections(self) -> None:
        rendered = presentation.build_presentation(same_family_signals_report(), output_mode="native-first", language="en")

        self.assertEqual([card["id"] for card in rendered["topic_cards"]], ["topic-001", "topic-002", "topic-003"])
        self.assertTrue(rendered["topic_cards"][0]["recommended_first"])
        for forbidden_key in (
            "presentation",
            "recommendation",
            "proposal",
            "related_variants",
            "first_response_spine",
            "first_response_contract",
            "topic_list",
        ):
            self.assertNotIn(forbidden_key, rendered)

    def test_available_output_adds_compact_next_action_options_after_topic_cards(self) -> None:
        rendered = presentation.build_presentation(same_family_signals_report(), output_mode="native-first", language="en")

        self.assertIn("next_action_options", rendered)
        self.assertLess(list(rendered).index("topic_cards"), list(rendered).index("next_action_options"))
        bridge = rendered["next_action_options"]
        self.assertEqual(bridge["heading"], "Next action options")
        self.assertEqual(bridge["status_line"], "advisory only; no topic selected yet")
        self.assertEqual(
            [option["id"] for option in bridge["options"]],
            ["choose-topic-number", "type-direct-request", "deepen-with-research"],
        )
        self.assertIn("Topic 1", bridge["options"][0]["action"])
        self.assertIn("your own words", bridge["options"][1]["action"])
        self.assertIn("deep thinking", bridge["options"][2]["action"])
        self.assertIn("websearch", bridge["options"][2]["action"])
        self.assertIn("webfetch", bridge["options"][2]["action"])
        self.assertTrue(all(option["advisory_only"] for option in bridge["options"]))
        self.assertTrue(all(not option["carry_forward_allowed"] for option in bridge["options"]))

    def test_topic_cards_preserve_conditional_evidence_examples_but_keep_before_after_on_all_cards(self) -> None:
        rendered = presentation.build_presentation(same_family_signals_report(), output_mode="native-first", language="en")

        primary_labels = [section["label"] for section in rendered["topic_cards"][0]["sections"]]
        weaker_labels = [section["label"] for section in rendered["topic_cards"][1]["sections"]]

        self.assertIn("Evidence examples", primary_labels)
        self.assertIn("Before behavior", primary_labels)
        self.assertIn("After behavior", primary_labels)
        self.assertNotIn("Evidence examples", weaker_labels)
        self.assertIn("Before behavior", weaker_labels)
        self.assertIn("After behavior", weaker_labels)

    def test_doctrine_level_titles_keep_incident_details_out_of_top_level_titles(self) -> None:
        rendered = presentation.build_presentation(doctrine_lifted_config_signals_report(), output_mode="native-first", language="en")

        titles = [card["canonical_title"] for card in rendered["topic_cards"]]
        self.assertCountEqual(
            titles,
            [
                "Verify semantic fit before reusing an existing control surface",
                "Separate symptom evidence from strategic fix scope",
                "Require source-backed behavior verification before choosing config-only remediation",
            ],
        )
        title_blob = " ".join(titles).lower()
        for forbidden in ("404", "passstatuscodes", "opera_fallback", "supplierapidomainprobe"):
            self.assertNotIn(forbidden, title_blob)
        proposal_blob = json.dumps(rendered["topic_cards"], ensure_ascii=False).lower()
        self.assertIn("404", proposal_blob)
        self.assertIn("passstatuscodes", proposal_blob)
        self.assertIn("opera_fallback", proposal_blob)

    def test_no_topics_path_explains_actionable_insufficiency(self) -> None:
        rendered = presentation.build_presentation(no_topic_signals_report(), output_mode="native-first", language="en")

        self.assertEqual(rendered["status"], "no-topics")
        self.assertIn("broader historical analysis", rendered["no_topics_message"].lower())
        self.assertIn("repeated pattern", " ".join(rendered["no_topics_details"]).lower())
        self.assertEqual(rendered["no_topics_context"]["records_analyzed"], 8)
        self.assertEqual(rendered["no_topics_context"]["signals_ranked"], 8)
        self.assertEqual(rendered["no_topics_context"]["strongest_signal_confidence"], "low")
        self.assertNotIn("same-day fallback", rendered["recommended_next_step"].lower())

    def test_no_topics_path_surfaces_policy_limit_when_trace_is_disabled(self) -> None:
        signals_report = no_topic_signals_report()
        signals_report["source"]["policy_limited"] = True
        signals_report["source"]["policy_note"] = "Config policy disabled trace_evidence for this run, so only durable_memory_context + governance_context remained in scope."

        rendered = presentation.build_presentation(signals_report, output_mode="native-first", language="en")

        self.assertEqual(rendered["status"], "no-topics")
        detail_blob = " ".join(rendered["no_topics_details"])
        self.assertIn("Config policy disabled trace_evidence", detail_blob)
        self.assertIn("durable_memory_context", detail_blob)


if __name__ == "__main__":
    unittest.main()
