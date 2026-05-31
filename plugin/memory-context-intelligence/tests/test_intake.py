#!/usr/bin/env python3
"""Focused checks for scoped memsearch intake."""

from __future__ import annotations

import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
INTAKE_PATH = PACKAGE_ROOT / "lib" / "intake.py"
SPEC = importlib.util.spec_from_file_location("mci_intake", INTAKE_PATH)
intake = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(intake)


class ScopedIntakeTests(unittest.TestCase):
    def write_day_shard(self, root: Path) -> None:
        text = textwrap.dedent(
            """
            ## Session 14:08

            ### 14:08
            <!-- session:current-session turn:t1 transcript:/tmp/current.jsonl -->
            - current session old context

            ### 15:57
            <!-- session:current-session turn:t2 transcript:/tmp/current.jsonl -->
            - current session narrowing evidence

            ### 17:03
            <!-- session:current-session turn:t3 transcript:/tmp/current.jsonl -->
            - current session latest verification

            ## Session 17:05

            ### 17:05
            <!-- session:other-session turn:o1 transcript:/tmp/other.jsonl -->
            - same day other session lookback clue
            """
        ).strip() + "\n"
        (root / "2026-05-20.md").write_text(text, encoding="utf-8")

    def write_historical_shards(self, root: Path) -> None:
        shard_payloads = [
            ("2026-05-16.md", "session-a", "historical pattern from early session"),
            ("2026-05-17.md", "session-b", "historical pattern from follow-up session"),
            ("2026-05-18.md", "session-c", "historical pattern from broader memory"),
            ("2026-05-19.md", "session-d", "recent historical pattern still relevant"),
            ("2026-05-20.md", "current-session", "latest historical pattern with current-session confirmation"),
        ]
        for shard_name, session_id, content in shard_payloads:
            text = textwrap.dedent(
                f"""
                ## Session 10:00

                ### 10:00
                <!-- session:{session_id} turn:t1 transcript:/tmp/{session_id}.jsonl -->
                - {content}
                """
            ).strip() + "\n"
            (root / shard_name).write_text(text, encoding="utf-8")

    def test_historical_default_reads_multiple_recent_cross_session_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            args = intake.parse_args(["--memory-root", str(root)])
            report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["scope"]["basis"], "historical-default")
            self.assertEqual(report["scope"]["historical_shards_considered"], 5)
            self.assertEqual(
                report["source"]["daily_shards_considered"],
                [
                    "2026-05-20.md",
                    "2026-05-19.md",
                    "2026-05-18.md",
                    "2026-05-17.md",
                    "2026-05-16.md",
                ],
            )
            self.assertEqual(
                [record["session_id"] for record in report["records"]],
                ["current-session", "session-d", "session-c", "session-b", "session-a"],
            )

    def test_explicit_day_and_session_scope_stays_narrow_when_requested(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                ]
            )
            report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["scope"]["basis"], "explicit-day-and-session")
            self.assertEqual(report["scope"]["historical_shards_considered"], 1)
            self.assertEqual(report["source"]["daily_shards_considered"], ["2026-05-20.md"])
            self.assertEqual([record["session_id"] for record in report["records"]], ["current-session"])

    def test_day_session_lookback_narrows_records_before_analysis(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                    "--lookback-minutes",
                    "90",
                ]
            )
            report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["source"]["daily_shards_considered"], ["2026-05-20.md"])
            self.assertEqual(report["scope"]["day_shard"], "2026-05-20")
            self.assertEqual(report["scope"]["session_id"], "current-session")
            self.assertEqual(report["scope"]["lookback_minutes"], 90)
            self.assertFalse(report["scope"]["same_day_widened"])
            self.assertEqual([record["time"] for record in report["records"]], ["15:57", "17:03"])
            self.assertTrue(all(record["session_id"] == "current-session" for record in report["records"]))

    def test_current_session_stays_pure_by_default_when_scope_is_insufficient(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                    "--scope",
                    "lookback clue",
                ]
            )
            report = intake.build_report(args)

            self.assertEqual(report["status"], "insufficient")
            self.assertFalse(report["scope"]["same_day_widened"])
            self.assertEqual(report["records"], [])
            self.assertIn("current-session slice", " ".join(report["notes"]).lower())
            self.assertNotIn("same-day widening was applied", " ".join(report["notes"]).lower())

    def test_same_day_widening_requires_explicit_opt_in_after_session_slice_is_insufficient(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                    "--scope",
                    "lookback clue",
                ]
            )
            args.allow_same_day_widening = True
            report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertTrue(report["scope"]["same_day_widened"])
            self.assertEqual([record["session_id"] for record in report["records"]], ["other-session"])
            self.assertEqual([record["time"] for record in report["records"]], ["17:05"])
            self.assertIn("same-day widening", " ".join(report["notes"]).lower())

    def test_current_session_prefers_memsearch_backed_retrieval_when_available(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                ]
            )

            memsearch_records = [
                {
                    "shard": "2026-05-20.md",
                    "section": "15:57",
                    "time": "15:57",
                    "session_id": "current-session",
                    "turn_id": "mem-t2",
                    "transcript": "/tmp/current.jsonl",
                    "content": "current session retrieved through memsearch expand",
                }
            ]

            with mock.patch.object(
                intake,
                "retrieve_memsearch_backed_session_records",
                return_value=(memsearch_records, {"retrieval_mode": "memsearch-search-expand", "search_hits": 1, "expanded_chunks": 1}),
                create=True,
            ):
                report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["source"]["retrieval_mode"], "memsearch-search-expand")
            self.assertEqual(report["source"]["search_hits"], 1)
            self.assertEqual(report["source"]["expanded_chunks"], 1)
            self.assertEqual([record["content"] for record in report["records"]], ["current session retrieved through memsearch expand"])

    def test_memsearch_backed_trace_records_expose_trace_and_recall_classes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                ]
            )

            memsearch_records = [
                {
                    "shard": "2026-05-20.md",
                    "section": "15:57",
                    "time": "15:57",
                    "session_id": "current-session",
                    "turn_id": "mem-t2",
                    "transcript": "/tmp/current.jsonl",
                    "content": "current session retrieved through memsearch expand",
                }
            ]

            with mock.patch.object(
                intake,
                "retrieve_memsearch_backed_session_records",
                return_value=(memsearch_records, {"retrieval_mode": "memsearch-search-expand", "search_hits": 1, "expanded_chunks": 1}),
                create=True,
            ):
                report = intake.build_report(args)

            self.assertEqual(report["records"][0]["source_classes"], ["trace_evidence", "recall_evidence"])
            self.assertIn("trace_evidence", report["source"]["source_classes_present"])
            self.assertIn("recall_evidence", report["source"]["source_classes_present"])

    def test_report_can_add_durable_memory_and_governance_context_records(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_day_shard(root)

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                ]
            )

            memsearch_records = [
                {
                    "shard": "2026-05-20.md",
                    "section": "15:57",
                    "time": "15:57",
                    "session_id": "current-session",
                    "turn_id": "mem-t2",
                    "transcript": "/tmp/current.jsonl",
                    "content": "current session retrieved through memsearch expand",
                }
            ]

            durable_records = [
                {
                    "shard": "MEMORY.md",
                    "section": "GLOBAL",
                    "content": "Do not overstate runtime readiness before verification.",
                    "source_classes": ["durable_memory_context"],
                }
            ]
            governance_records = [
                {
                    "shard": "design.md",
                    "section": "Authority boundary",
                    "content": "Do not claim main RULES promotion from design-only evidence.",
                    "source_classes": ["governance_context"],
                }
            ]

            with mock.patch.object(
                intake,
                "retrieve_memsearch_backed_session_records",
                return_value=(memsearch_records, {"retrieval_mode": "memsearch-search-expand", "search_hits": 1, "expanded_chunks": 1}),
                create=True,
            ), mock.patch.object(
                intake,
                "discover_durable_memory_context_records",
                return_value=durable_records,
                create=True,
            ), mock.patch.object(
                intake,
                "discover_governance_context_records",
                return_value=governance_records,
                create=True,
            ):
                report = intake.build_report(args)

            self.assertIn("durable_memory_context", report["source"]["source_classes_present"])
            self.assertIn("governance_context", report["source"]["source_classes_present"])
            self.assertTrue(any("durable_memory_context" in record.get("source_classes", []) for record in report["evidence_records"]))
            self.assertTrue(any("governance_context" in record.get("source_classes", []) for record in report["evidence_records"]))

    def test_config_source_policy_can_limit_historical_default_sources_and_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            self.write_historical_shards(root)

            project_dir = Path(temp_dir) / "project"
            project_dir.mkdir()
            (project_dir / "memory-context-intelligence.config.json").write_text(
                textwrap.dedent(
                    """
                    {
                      "analysis": {
                        "source_policy": {
                          "enabled_source_classes": ["trace_evidence"],
                          "max_historical_shards": 3
                        }
                      }
                    }
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            args = intake.parse_args(["--memory-root", str(root)])
            with mock.patch.object(intake.Path, "cwd", return_value=project_dir):
                report = intake.build_report(args)

            self.assertTrue(report["source_policy"]["loaded"])
            self.assertEqual(report["source_policy"]["config_source"], "auto-upward")
            self.assertEqual(report["source_policy"]["effective_source_classes"], ["trace_evidence"])
            self.assertTrue(report["source_policy"]["policy_limited"])
            self.assertEqual(
                report["source"]["daily_shards_considered"],
                ["2026-05-20.md", "2026-05-19.md", "2026-05-18.md"],
            )
            self.assertEqual(report["source"]["source_classes_present"], ["trace_evidence"])
            self.assertTrue(all(record.get("source_classes") == ["trace_evidence"] for record in report["evidence_records"]))
            self.assertIn("trace_evidence", report["source_policy"]["policy_note"])
            self.assertIn("3", report["source_policy"]["policy_note"])

    def test_config_same_day_widening_does_not_override_explicit_narrow_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            self.write_day_shard(root)

            project_dir = Path(temp_dir) / "project"
            project_dir.mkdir()
            (project_dir / "memory-context-intelligence.config.json").write_text(
                textwrap.dedent(
                    """
                    {
                      "analysis": {
                        "source_policy": {
                          "allow_same_day_widening": true
                        }
                      }
                    }
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--day",
                    "2026-05-20",
                    "--session-id",
                    "current-session",
                    "--scope",
                    "lookback clue",
                ]
            )
            with mock.patch.object(intake.Path, "cwd", return_value=project_dir):
                report = intake.build_report(args)

            self.assertTrue(report["source_policy"]["loaded"])
            self.assertTrue(report["source_policy"]["requested_same_day_widening"])
            self.assertFalse(report["source_policy"]["effective_same_day_widening"])
            self.assertEqual(report["status"], "insufficient")
            self.assertEqual(report["records"], [])
            self.assertFalse(report["scope"]["same_day_widened"])
            self.assertIn("stayed narrow", report["source_policy"]["policy_note"].lower())


if __name__ == "__main__":
    unittest.main()
