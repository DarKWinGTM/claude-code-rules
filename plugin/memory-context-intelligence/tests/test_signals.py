#!/usr/bin/env python3
"""Focused checks for internal signal/topic generation."""

from __future__ import annotations

import importlib.util
import os
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SIGNALS_PATH = PACKAGE_ROOT / "lib" / "signals.py"
SPEC = importlib.util.spec_from_file_location("mci_signals", SIGNALS_PATH)
signals = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(signals)


def intake_report(*, status: str = "available", freshness: str = "fresh", records: list[dict] | None = None) -> dict:
    return {
        "tool": "memory-context-intelligence",
        "mode": "intake",
        "status": status,
        "evidence_strength": "observed-local-bounded" if status == "available" else "observed-local-stale",
        "source": {
            "kind": "memsearch-daily-markdown-shards",
            "memory_root_source": "test",
            "available": status != "unavailable",
        },
        "scope": {"filters": ["memory-context-intelligence"], "bounded_subset_only": True},
        "freshness": {"classification": freshness},
        "records": records or [],
        "topic_generation_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


class SignalGenerationTests(unittest.TestCase):
    def test_controlled_sample_produces_internal_signals_and_topics(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "content": "- Do not claim fixed before verification; report evidence limits clearly.",
                    },
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "content": "- Avoid claiming fixed before verification; keep evidence limits visible.",
                    },
                ]
            )
        )

        self.assertTrue(report["internal_only"])
        self.assertFalse(report["choose_flow_performed"])
        self.assertFalse(report["external_research_performed"])
        self.assertFalse(report["additional_emission_performed"])
        self.assertFalse(report["main_rules_mutation_performed"])
        self.assertGreaterEqual(len(report["ranked_signals"]), 1)
        self.assertGreaterEqual(len(report["topic_candidates"]), 1)
        topic = report["topic_candidates"][0]
        for field in (
            "purpose",
            "why_surfaced",
            "expected_behavior_impact",
            "high_level_mechanism",
            "expected_output",
        ):
            self.assertTrue(topic[field])

    def test_duplicate_and_near_duplicate_records_merge(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "content": "- Do not overstate runtime readiness before live verification.",
                    },
                    {
                        "shard": "2026-05-18.md",
                        "section": "feedback",
                        "content": "- Do not overstate runtime readiness before live verification.",
                    },
                    {
                        "shard": "2026-05-17.md",
                        "section": "feedback",
                        "content": "- Avoid overstating runtime readiness before verification evidence exists.",
                    },
                ]
            )
        )

        correction_groups = report["signal_groups"]["corrections"]
        self.assertEqual(len(correction_groups), 1)
        self.assertEqual(correction_groups[0]["record_count"], 3)
        self.assertIn(correction_groups[0]["confidence"], {"medium", "high"})

    def test_promoted_topic_is_design_grounded_review_topic_not_generic_pattern_title(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-20.md",
                        "section": "feedback",
                        "session_id": "current-session",
                        "content": "- Clarify evidence boundaries for refresh and 15s wait guidance in Claude workflow review.",
                    },
                    {
                        "shard": "2026-05-20.md",
                        "section": "feedback",
                        "session_id": "current-session",
                        "content": "- Clarify evidence boundaries for refresh and 15s wait guidance in Claude workflow review.",
                    },
                    {
                        "shard": "2026-05-19.md",
                        "section": "feedback",
                        "session_id": "current-session",
                        "content": "- Keep refresh and 15s wait guidance tied to evidence boundaries and workflow review intent.",
                    },
                ]
            )
        )

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertNotIn("Normalize recurring workflow pattern around", topic["title"])
        self.assertTrue("review" in topic["title"].lower() or "evidence" in topic["title"].lower())
        self.assertEqual(topic["source_session_ids"], ["current-session"])

    def test_surface_issue_topic_is_issue_first_not_keyword_bag(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-21.md",
                        "section": "analysis",
                        "session_id": "current-session",
                        "content": "- /memory-context-intelligence:analysis returned a development progress summary instead of operator-facing analysis output.",
                    },
                    {
                        "shard": "2026-05-21.md",
                        "section": "analysis",
                        "session_id": "current-session",
                        "content": "- /memory-context-intelligence:analysis leaked development progress summary instead of operator-facing analysis output.",
                    },
                    {
                        "shard": "2026-05-20.md",
                        "section": "analysis",
                        "session_id": "current-session",
                        "content": "- Fix the analysis surface reply contract so /memory-context-intelligence:analysis stops returning development progress summary and restores operator-facing analysis output.",
                    },
                ]
            )
        )

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(
                intake_report(
                    records=[
                        {
                            "shard": "2026-05-21.md",
                            "section": "analysis",
                            "session_id": "current-session",
                            "content": "- /memory-context-intelligence:analysis returned a development progress summary instead of operator-facing analysis output.",
                        },
                        {
                            "shard": "2026-05-21.md",
                            "section": "analysis",
                            "session_id": "current-session",
                            "content": "- /memory-context-intelligence:analysis leaked development progress summary instead of operator-facing analysis output.",
                        },
                        {
                            "shard": "2026-05-20.md",
                            "section": "analysis",
                            "session_id": "current-session",
                            "content": "- Fix the analysis surface reply contract so /memory-context-intelligence:analysis stops returning development progress summary and restores operator-facing analysis output.",
                        },
                    ]
                )
            )

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertEqual(
            topic["title"],
            "Rewrite /memory-context-intelligence:analysis first response into operator-facing proposal output",
        )
        self.assertNotIn("signal / design / claude", topic["title"].lower())

    def test_completion_claim_topic_title_is_semantic_not_token_bag(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-22.md",
                        "section": "feedback",
                        "session_id": "session-a",
                        "content": "- Do not claim completion before verification evidence exists.",
                    },
                    {
                        "shard": "2026-05-23.md",
                        "section": "feedback",
                        "session_id": "session-b",
                        "content": "- Avoid claiming completion before verification evidence exists.",
                    },
                    {
                        "shard": "2026-05-24.md",
                        "section": "feedback",
                        "session_id": "session-c",
                        "content": "- Keep completion wording behind real verification evidence.",
                    },
                ]
            )
        )

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertEqual(topic["title"], "Stop completion wording from outrunning verification")

    def test_policy_limited_context_only_run_does_not_promote_without_trace(self) -> None:
        report = signals.build_report(
            {
                "tool": "memory-context-intelligence",
                "mode": "intake",
                "status": "available",
                "evidence_strength": "observed-local-bounded",
                "source": {
                    "kind": "memsearch-daily-markdown-shards",
                    "memory_root_source": "test",
                    "available": True,
                    "source_classes_present": ["durable_memory_context", "governance_context"],
                },
                "source_policy": {
                    "loaded": True,
                    "policy_limited": True,
                    "effective_source_classes": ["durable_memory_context", "governance_context"],
                    "policy_note": "Config policy disabled trace_evidence for this run, so only durable_memory_context + governance_context remained in scope.",
                },
                "scope": {"filters": ["memory-context-intelligence"], "bounded_subset_only": True},
                "freshness": {"classification": "fresh"},
                "records": [],
                "evidence_records": [
                    {
                        "shard": "MEMORY.md",
                        "section": "feedback",
                        "content": "- Durable reminder about evidence wording.",
                        "source_classes": ["durable_memory_context"],
                    },
                    {
                        "shard": "design.md",
                        "section": "authority",
                        "content": "- Governance note about promotion boundaries.",
                        "source_classes": ["governance_context"],
                    },
                ],
                "topic_generation_performed": False,
                "additional_emission_performed": False,
                "main_rules_mutation_performed": False,
            }
        )

        self.assertEqual(report["topic_candidates"], [])
        self.assertEqual(report["advisory_fallback_topics"], [])
        self.assertTrue(report["ranked_signals"])
        self.assertEqual(report["source"]["policy_limited"], True)
        self.assertIn("Config policy disabled trace_evidence", report["source"]["policy_note"])
        self.assertIn("Config policy disabled trace_evidence", report["ranked_signals"][0]["provenance_note"])

    def test_policy_limited_recall_only_run_does_not_promote_without_trace(self) -> None:
        report = signals.build_report(
            {
                "tool": "memory-context-intelligence",
                "mode": "intake",
                "status": "available",
                "evidence_strength": "observed-local-bounded",
                "source": {
                    "kind": "memsearch-daily-markdown-shards",
                    "memory_root_source": "test",
                    "available": True,
                    "source_classes_present": ["recall_evidence"],
                },
                "source_policy": {
                    "loaded": True,
                    "policy_limited": True,
                    "effective_source_classes": ["recall_evidence"],
                    "policy_note": "Config policy disabled trace_evidence for this run, so only recall_evidence remained in scope.",
                },
                "scope": {"filters": ["memory-context-intelligence"], "bounded_subset_only": True},
                "freshness": {"classification": "fresh"},
                "records": [],
                "evidence_records": [
                    {
                        "shard": "2026-05-20.md",
                        "section": "analysis",
                        "session_id": "current-session",
                        "content": "- Recall-expanded detail about a config-policy investigation without repeated live trace support.",
                        "source_classes": ["recall_evidence"],
                    }
                ],
                "topic_generation_performed": False,
                "additional_emission_performed": False,
                "main_rules_mutation_performed": False,
            }
        )

        self.assertEqual(report["status"], "low-confidence")
        self.assertEqual(report["topic_candidates"], [])
        self.assertEqual(report["advisory_fallback_topics"], [])
        self.assertTrue(report["ranked_signals"])
        self.assertEqual(report["ranked_signals"][0]["trace_record_count"], 0)
        self.assertEqual(report["source"]["policy_limited"], True)
        self.assertIn("only recall_evidence remained in scope", report["source"]["policy_note"])
        self.assertIn("only recall_evidence remained in scope", report["ranked_signals"][0]["provenance_note"])

    def test_analysis_surface_boundary_topic_is_not_generic_plugin_harness_title(self) -> None:
        report = signals.build_report(
            intake_report(
                records=[
                    {
                        "shard": "2026-05-21.md",
                        "section": "analysis",
                        "session_id": "session-a",
                        "content": "- /memory-context-intelligence:analysis returned skill runtime context instead of operator-facing analysis output.",
                    },
                    {
                        "shard": "2026-05-21.md",
                        "section": "analysis",
                        "session_id": "session-b",
                        "content": "- /memory-context-intelligence:analysis surfaced skill runtime context instead of operator-facing analysis output.",
                    },
                    {
                        "shard": "2026-05-20.md",
                        "section": "analysis",
                        "session_id": "session-c",
                        "content": "- Clarify the analysis surface output contract so /memory-context-intelligence:analysis does not leak skill runtime context to operator-facing results.",
                    },
                ]
            )
        )

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertIn("analysis", topic["title"].lower())
        self.assertTrue("operator-facing" in topic["title"].lower() or "output contract" in topic["title"].lower() or "runtime context" in topic["title"].lower())
        self.assertNotIn("plugin/harness boundary", topic["title"].lower())

    def test_recurring_pattern_private_title_is_lifted_to_disclosure_doctrine(self) -> None:
        signal = {
            "kind": "recurring_pattern",
            "keywords": ["workflow", "private", "proposal"],
            "review_focus": "workflow-review",
            "records": [
                {
                    "content_preview": "Private/operator disclosure wording in workflow review still reads like a recurring pattern summary instead of an actionable proposal.",
                }
            ],
        }

        self.assertEqual(
            signals.topic_title(signal),
            "Keep audience disclosure boundaries explicit in surfaced proposals",
        )
        self.assertEqual(signals.advisory_focus_suffix(signal), "disclosure boundary")

    def test_recurring_pattern_task_title_is_lifted_to_decision_ready_proposal_doctrine(self) -> None:
        signal = {
            "kind": "recurring_pattern",
            "keywords": ["workflow", "task", "proposal"],
            "review_focus": "workflow-review",
            "records": [
                {
                    "content_preview": "Task-oriented workflow review wording still reads like a recurring pattern summary instead of a decision-ready proposal.",
                }
            ],
        }

        self.assertEqual(
            signals.topic_title(signal),
            "Turn recurring workflow findings into decision-ready proposals",
        )
        self.assertEqual(signals.advisory_focus_suffix(signal), "workflow owner")

    def test_historical_trace_promotes_without_current_session_confirmation(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-16.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence", "recall_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertEqual(topic["historical_strength"], "3 trace record(s) across 3 session(s) and 3 shard(s)")
        self.assertEqual(topic["latest_seen"], "2026-05-20")
        self.assertEqual(topic["current_session_confirmation"], "historical-only")

    def test_current_session_confirmation_is_a_boost_not_a_gate(self) -> None:
        historical_only = intake_report(records=[])
        historical_only["evidence_records"] = [
            {
                "shard": "2026-05-16.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
        ]

        confirmed = intake_report(records=[])
        confirmed["evidence_records"] = historical_only["evidence_records"] + [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "current-session",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence", "recall_evidence"],
            }
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            historical_report = signals.build_report(historical_only)
            confirmed_report = signals.build_report(confirmed)

        self.assertTrue(historical_report["topic_candidates"])
        self.assertTrue(confirmed_report["topic_candidates"])
        self.assertEqual(
            historical_report["topic_candidates"][0]["current_session_confirmation"],
            "historical-only",
        )
        self.assertEqual(
            confirmed_report["topic_candidates"][0]["current_session_confirmation"],
            "confirmed-in-current-session",
        )
        self.assertGreater(
            confirmed_report["ranked_signals"][0]["score"],
            historical_report["ranked_signals"][0]["score"],
        )

    def test_historical_only_single_session_single_shard_pattern_stays_too_narrow_to_promote(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        self.assertTrue(report["ranked_signals"])
        self.assertEqual(report["ranked_signals"][0]["historical_strength"], "2 trace record(s) across 1 session(s) and 1 shard(s)")
        self.assertEqual(report["ranked_signals"][0]["current_session_confirmation"], "historical-only")
        self.assertEqual(report["ranked_signals"][0]["confidence"], "low")
        self.assertEqual(report["topic_candidates"], [])

    def test_broader_multi_session_multi_shard_history_surfaces_as_stronger_candidate(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Workflow wording still reads like a recurring pattern summary instead of an actionable proposal.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Workflow wording still reads like a recurring pattern summary instead of an actionable proposal.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-16.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Do not claim completion before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Avoid claiming completion before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-d",
                "content": "Do not claim completion before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        self.assertTrue(report["topic_candidates"])
        self.assertEqual(report["topic_candidates"][0]["title"], "Stop completion wording from outrunning verification")
        self.assertEqual(report["topic_candidates"][0]["historical_strength"], "3 trace record(s) across 3 session(s) and 3 shard(s)")
        self.assertNotIn(
            "Review workflow wording so repeated patterns read like actionable proposals",
            [topic["title"] for topic in report["topic_candidates"]],
        )

    def test_sparse_history_exposes_three_advisory_fallback_topics(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not claim completion before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Do not claim completion before verification evidence exists.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-19.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Approval is still blocking this workflow step and needs a clearer stop gate.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-19.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Approval is still blocking this workflow step and needs a clearer stop gate.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Refresh and wait guidance still reads stronger than the evidence behind it.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Refresh and wait guidance still reads stronger than the evidence behind it.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        self.assertEqual(report["topic_candidates"], [])
        self.assertEqual(len(report["advisory_fallback_topics"]), 3)
        self.assertEqual(len({topic["title"] for topic in report["advisory_fallback_topics"]}), 3)
        self.assertTrue(all(topic["confidence"] == "low" for topic in report["advisory_fallback_topics"]))
        self.assertTrue(all(topic["current_session_confirmation"] == "historical-only" for topic in report["advisory_fallback_topics"]))

    def test_config_investigation_signals_are_lifted_to_doctrine_level_titles(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Claude Code said it would check whether supplierApiDomainProbe already has a config field that keeps 404 away from opera_fallback.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Claude Code read config/supplier-pricing-calculator.json and phase docs to separate retry config from probe fallback config.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-19.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Claude Code ran grep over supplierApiDomainProbe, passStatusCodes, operaProxy, proxy_misconfigured, 403, 404, and fallback before reading coordinator settings.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Claude Code concluded putting 404 in passStatusCodes would be the wrong semantic because it would turn 404 into a pass, so this needs config shape plus code path work instead of config-only change.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        self.assertEqual(report["topic_candidates"], [])
        self.assertEqual(len(report["advisory_fallback_topics"]), 3)
        titles = [topic["title"] for topic in report["advisory_fallback_topics"]]
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

    def test_config_investigation_signal_exposes_bounded_evidence_examples_and_before_after(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "feedback",
                "session_id": "session-a",
                "content": "Claude Code said it would check whether supplierApiDomainProbe already has a config field that keeps 404 away from opera_fallback.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-19.md",
                "section": "feedback",
                "session_id": "session-b",
                "content": "Claude Code ran grep over supplierApiDomainProbe, passStatusCodes, operaProxy, proxy_misconfigured, 403, 404, and fallback before reading coordinator settings.",
                "source_classes": ["trace_evidence"],
            },
            {
                "shard": "2026-05-18.md",
                "section": "feedback",
                "session_id": "session-c",
                "content": "Claude Code concluded putting 404 in passStatusCodes would be the wrong semantic because it would turn 404 into a pass, so this needs config shape plus code path work instead of config-only change.",
                "source_classes": ["trace_evidence"],
            },
        ]

        with mock.patch.dict(os.environ, {"CLAUDE_CODE_SESSION_ID": "current-session"}, clear=False):
            report = signals.build_report(report_input)

        topic = next(
            topic
            for topic in report["advisory_fallback_topics"]
            if topic["title"] == "Verify semantic fit before reusing an existing control surface"
        )
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertIn("supplierApiDomainProbe", " ".join(topic["evidence_examples"]))
        self.assertTrue(any(fragment in " ".join(topic["evidence_examples"]) for fragment in ("404", "opera_fallback", "passStatusCodes")))
        self.assertIn("404", topic["before_behavior"])
        self.assertIn("passStatusCodes", topic["before_behavior"])
        self.assertIn("keep `404` as evidence", topic["after_behavior"])

    def test_goal_scoped_recurring_pattern_exposes_before_after_and_evidence_examples(self) -> None:
        signal = {
            "id": "signal-998",
            "kind": "recurring_pattern",
            "group": "recurring_patterns",
            "record_count": 2,
            "confidence": "low",
            "evidence_label": "bounded-single-observation-low-confidence",
            "records": [{"content_preview": "Goal-oriented recurring workflow finding still reads like a trace summary instead of a decision-ready proposal."}],
            "provenance_note": "Historical trace evidence is the primary signal.",
            "source_scope_label": "historical-default",
            "source_mix_label": "trace_evidence",
            "source_classes": ["trace_evidence"],
            "source_session_ids": ["session-y"],
            "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
            "latest_seen": "2026-05-30",
            "current_session_confirmation": "historical-only",
            "keywords": ["workflow", "goal", "proposal"],
        }

        topic = signals.topic_from_signal(signal, 1, promotion_tier="advisory-fallback")
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertIn("Goal-oriented recurring workflow finding", " ".join(topic["evidence_examples"]))
        self.assertIn("decision-ready proposal", topic["before_behavior"])
        self.assertIn("user can act on immediately", topic["after_behavior"])

    def test_goal_keyword_only_recurring_pattern_still_exposes_examples_and_goal_framing(self) -> None:
        signal = {
            "id": "signal-997",
            "kind": "recurring_pattern",
            "group": "recurring_patterns",
            "record_count": 2,
            "confidence": "low",
            "evidence_label": "bounded-single-observation-low-confidence",
            "records": [{"content_preview": "Workflow finding should be carried forward as a goal-level proposal rather than left as a weak trace summary."}],
            "provenance_note": "Historical trace evidence is the primary signal.",
            "source_scope_label": "historical-default",
            "source_mix_label": "trace_evidence",
            "source_classes": ["trace_evidence"],
            "source_session_ids": ["session-y"],
            "historical_strength": "2 trace record(s) across 1 session(s) and 1 shard(s)",
            "latest_seen": "2026-05-30",
            "current_session_confirmation": "historical-only",
            "keywords": ["workflow", "goal"],
        }

        topic = signals.topic_from_signal(signal, 1, promotion_tier="advisory-fallback")
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertEqual(signals.advisory_focus_suffix(signal), "goal framing")
        self.assertIn("proposal", topic["before_behavior"].lower())
        self.assertIn("goal", topic["after_behavior"].lower())

    def test_generic_evidence_gap_signal_still_exposes_topic_specific_before_after(self) -> None:
        signal = {
            "id": "signal-999",
            "kind": "evidence_gap",
            "group": "evidence_gaps",
            "record_count": 1,
            "confidence": "low",
            "evidence_label": "bounded-single-observation-low-confidence",
            "records": [{"content_preview": "Some responses still read stronger than the evidence boundary really supports."}],
            "provenance_note": "Historical trace evidence is the primary signal.",
            "source_scope_label": "historical-default",
            "source_mix_label": "trace_evidence",
            "source_classes": ["trace_evidence"],
            "source_session_ids": ["session-z"],
            "historical_strength": "1 trace record(s) across 1 session(s) and 1 shard(s)",
            "latest_seen": "2026-05-30",
            "current_session_confirmation": "historical-only",
            "keywords": ["evidence", "claim"],
        }

        topic = signals.topic_from_signal(signal, 1, promotion_tier="advisory-fallback")
        self.assertEqual(topic["title"], "Clarify evidence wording before strong claims")
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertIn("verified fact", topic["before_behavior"])
        self.assertIn("working hypothesis", topic["before_behavior"])
        self.assertIn("verified fact", topic["after_behavior"])
        self.assertIn("inference", topic["after_behavior"])

    def test_generic_surface_boundary_signal_still_exposes_topic_specific_before_after(self) -> None:
        signal = {
            "id": "signal-998",
            "kind": "recurring_pattern",
            "group": "recurring_patterns",
            "record_count": 1,
            "confidence": "low",
            "evidence_label": "bounded-single-observation-low-confidence",
            "records": [{"content_preview": "The analysis result may drift toward a generic trace-pattern summary instead of staying clearly owned by the user-facing analysis surface."}],
            "provenance_note": "Historical trace evidence is the primary signal.",
            "source_scope_label": "historical-default",
            "source_mix_label": "trace_evidence",
            "source_classes": ["trace_evidence"],
            "source_session_ids": ["session-y"],
            "historical_strength": "1 trace record(s) across 1 session(s) and 1 shard(s)",
            "latest_seen": "2026-05-30",
            "current_session_confirmation": "historical-only",
            "keywords": ["analysis", "surface"],
            "review_focus": "surface-boundary",
        }

        topic = signals.topic_from_signal(signal, 1, promotion_tier="advisory-fallback")
        self.assertEqual(topic["title"], "Clarify which surface owns the user-facing analysis result")
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertIn("generic trace-pattern summary", topic["before_behavior"])
        self.assertIn("analysis result", topic["after_behavior"])
        self.assertIn("proposal", topic["after_behavior"])

    def test_generic_workflow_signal_still_exposes_decision_ready_before_after(self) -> None:
        signal = {
            "id": "signal-997",
            "kind": "recurring_pattern",
            "group": "recurring_patterns",
            "record_count": 1,
            "confidence": "low",
            "evidence_label": "bounded-single-observation-low-confidence",
            "records": [{"content_preview": "A workflow finding still surfaced as a blocker-shaped observation without turning into a usable next step."}],
            "provenance_note": "Historical trace evidence is the primary signal.",
            "source_scope_label": "historical-default",
            "source_mix_label": "trace_evidence",
            "source_classes": ["trace_evidence"],
            "source_session_ids": ["session-x"],
            "historical_strength": "1 trace record(s) across 1 session(s) and 1 shard(s)",
            "latest_seen": "2026-05-30",
            "current_session_confirmation": "historical-only",
            "keywords": ["workflow"],
        }

        topic = signals.topic_from_signal(signal, 1, promotion_tier="advisory-fallback")
        self.assertEqual(topic["title"], "Turn recurring workflow findings into decision-ready proposals")
        self.assertGreaterEqual(len(topic["evidence_examples"]), 1)
        self.assertIn("blocker-shaped observations", topic["before_behavior"])
        self.assertIn("decision-ready", topic["after_behavior"])
        self.assertIn("next step", topic["after_behavior"])

    def test_stale_input_stays_low_confidence_and_promotes_no_topics(self) -> None:
        report = signals.build_report(
            intake_report(
                status="stale",
                freshness="stale",
                records=[
                    {
                        "shard": "2026-01-01.md",
                        "section": "feedback",
                        "content": "- Do not claim completion without checked evidence.",
                    },
                    {
                        "shard": "2026-01-01.md",
                        "section": "feedback",
                        "content": "- Avoid claiming completion without checked evidence.",
                    },
                ],
            )
        )

        self.assertEqual(report["status"], "low-confidence")
        self.assertTrue(report["ranked_signals"])
        self.assertTrue(all(signal["confidence"] == "low" for signal in report["ranked_signals"]))
        self.assertEqual(report["topic_candidates"], [])

    def test_insufficient_input_produces_no_promoted_topics(self) -> None:
        report = signals.build_report(intake_report(status="insufficient", freshness="unknown", records=[]))

        self.assertEqual(report["status"], "insufficient")
        self.assertEqual(report["ranked_signals"], [])
        self.assertEqual(report["topic_candidates"], [])
        self.assertEqual(report["limits"]["topics_promoted"], 0)

    def test_multi_source_cluster_exposes_source_mix_but_stays_trace_anchored(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "2026-05-20.md",
                "section": "analysis",
                "session_id": "current-session",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["trace_evidence", "recall_evidence"],
            },
            {
                "shard": "MEMORY.md",
                "section": "GLOBAL",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["durable_memory_context"],
            },
            {
                "shard": "design.md",
                "section": "Authority boundary",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["governance_context"],
            },
        ]

        report = signals.build_report(report_input)

        self.assertTrue(report["topic_candidates"])
        topic = report["topic_candidates"][0]
        self.assertIn("trace_evidence", topic["source_classes"])
        self.assertIn("recall_evidence", topic["source_classes"])
        self.assertIn("durable_memory_context", topic["source_classes"])
        self.assertIn("governance_context", topic["source_classes"])
        self.assertIn("trace_evidence", topic["source_mix_label"])

    def test_context_only_cluster_does_not_promote_without_trace_evidence(self) -> None:
        report_input = intake_report(records=[])
        report_input["evidence_records"] = [
            {
                "shard": "MEMORY.md",
                "section": "GLOBAL",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["durable_memory_context"],
            },
            {
                "shard": "design.md",
                "section": "Authority boundary",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["governance_context"],
            },
            {
                "shard": "phase/SUMMARY.md",
                "section": "Boundaries",
                "content": "Do not overstate runtime readiness before verification evidence exists.",
                "source_classes": ["governance_context"],
            },
        ]

        report = signals.build_report(report_input)

        self.assertEqual(report["topic_candidates"], [])
        self.assertTrue(report["ranked_signals"])
        self.assertEqual(report["ranked_signals"][0]["confidence"], "low")


if __name__ == "__main__":
    unittest.main()
