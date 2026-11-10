#!/usr/bin/env python3
"""Focused checks for scoped memsearch intake."""

from __future__ import annotations

import importlib.util
import tempfile
import textwrap
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
INTAKE_PATH = PACKAGE_ROOT / "lib" / "intake.py"
SPEC = importlib.util.spec_from_file_location("mci_intake", INTAKE_PATH)
intake = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(intake)


class FrozenDate(date):
    @classmethod
    def today(cls) -> date:
        return cls(2026, 5, 20)


class ScopedIntakeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.home_temp_dir = tempfile.TemporaryDirectory()
        self.home_root = Path(self.home_temp_dir.name)
        self.home_patcher = mock.patch.object(intake.Path, "home", return_value=self.home_root)
        self.date_patcher = mock.patch.object(intake, "date", FrozenDate)
        self.home_patcher.start()
        self.date_patcher.start()

    def tearDown(self) -> None:
        self.date_patcher.stop()
        self.home_patcher.stop()
        self.home_temp_dir.cleanup()

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

    def test_historical_sampling_represents_days_before_reusing_a_busy_day(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)
            newest = root / "2026-05-20.md"
            newest.write_text(newest.read_text(encoding="utf-8") + "- repeated newest-day context\n" * 12, encoding="utf-8")
            with mock.patch.object(intake.Path, "cwd", return_value=root):
                report = intake.build_report(intake.parse_args(["--memory-root", str(root)]))

        self.assertEqual(
            [record["shard"] for record in report["records"][:5]],
            ["2026-05-20.md", "2026-05-19.md", "2026-05-18.md", "2026-05-17.md", "2026-05-16.md"],
        )
        self.assertEqual(len(report["records"]), 8)
        self.assertEqual(report["coverage"]["sampled_days"], report["coverage"]["selected_days"])
        self.assertTrue(report["coverage"]["sampling_limited"])
        refs = [record["ref"] for record in report["records"]]
        self.assertEqual(refs, [f"excerpt-{index:03d}" for index in range(1, 9)])
        self.assertTrue(all(not record["content_truncated"] for record in report["records"]))

    def test_historical_record_budget_keeps_unsampled_days_in_the_next_window(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for offset in range(12):
                day = FrozenDate.today() - timedelta(days=offset)
                bullets = "- recent repeated finding\n" * 12 if offset == 0 else f"- distinct finding from day {offset}\n"
                (root / f"{day.isoformat()}.md").write_text("### 10:00\n" + bullets, encoding="utf-8")
            with mock.patch.object(intake.Path, "cwd", return_value=root):
                report = intake.build_report(intake.parse_args(["--memory-root", str(root)]))
                days = [path[:10] for path in report["source"]["daily_shards_considered"]]
                boundary = min(days)
                supplemental = intake.build_report(
                    intake.parse_args(["--memory-root", str(root), "--older-than-day", boundary])
                )

        self.assertEqual(len(days), 8)
        self.assertEqual(boundary, "2026-05-13")
        self.assertEqual(report["coverage"]["sampled_days"], days)
        self.assertEqual(supplemental["coverage"]["selected_days"][0], "2026-05-12")
        self.assertIn("2026-05-11", supplemental["coverage"]["sampled_days"])
        self.assertFalse(set(days) & set(supplemental["coverage"]["selected_days"]))

    def test_historical_sampling_rotates_sessions_within_each_day(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "2026-05-20.md").write_text(
                "### 09:00\n<!-- session:session-a turn:a1 transcript:fixture-a.jsonl -->\n"
                "- first session finding\n- first session follow-up\n- first session extra\n"
                "### 10:00\n<!-- session:session-b turn:b1 transcript:fixture-b.jsonl -->\n"
                "- second session finding\n- second session follow-up\n",
                encoding="utf-8",
            )
            (root / "2026-05-19.md").write_text("### 09:00\n- previous day finding\n", encoding="utf-8")
            with mock.patch.object(intake.Path, "cwd", return_value=root):
                report = intake.build_report(intake.parse_args(["--memory-root", str(root), "--max-records", "4"]))

        self.assertEqual(
            [(record["shard"], record["session_id"]) for record in report["records"]],
            [("2026-05-20.md", "session-a"), ("2026-05-19.md", None), ("2026-05-20.md", "session-b"), ("2026-05-20.md", "session-a")],
        )

    def test_historical_character_budget_does_not_starve_later_days(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "2026-05-20.md").write_text("### 09:00\n- " + "x" * 800 + "\n", encoding="utf-8")
            (root / "2026-05-19.md").write_text("### 09:00\n- distinct later-day mechanism\n", encoding="utf-8")
            with mock.patch.object(intake.Path, "cwd", return_value=root):
                report = intake.build_report(intake.parse_args(["--memory-root", str(root), "--max-records", "2", "--max-chars", "256"]))

        self.assertEqual([record["shard"] for record in report["records"]], ["2026-05-20.md", "2026-05-19.md"])
        self.assertTrue(report["records"][0]["content_truncated"])
        self.assertFalse(report["records"][1]["content_truncated"])
        self.assertIn("distinct later-day mechanism", report["records"][1]["content"])
        self.assertLessEqual(report["limits"]["emitted_chars"], 256)
        self.assertEqual(report["coverage"]["content_truncated_refs"], ["excerpt-001"])

    def test_coverage_distinguishes_empty_unreadable_and_byte_limited_days(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "2026-05-20.md").write_text("### 09:00\n- " + "x" * 1600 + "\n", encoding="utf-8")
            (root / "2026-05-19.md").write_text("### 09:00\nno bullet records\n", encoding="utf-8")
            blocked = root / "2026-05-18.md"
            blocked.write_text("### 09:00\n- unreadable record\n", encoding="utf-8")
            original_read = intake.read_bounded_text

            def read_shard(path: Path, max_bytes: int) -> tuple[str, bool]:
                if path == blocked:
                    raise PermissionError("fixture permission denied")
                return original_read(path, max_bytes)

            with mock.patch.object(intake.Path, "cwd", return_value=root), mock.patch.object(intake, "read_bounded_text", side_effect=read_shard):
                report = intake.build_report(intake.parse_args(["--memory-root", str(root), "--max-shard-bytes", "1024"]))

        coverage = report["coverage"]
        self.assertEqual(coverage["selected_days"], ["2026-05-20", "2026-05-19", "2026-05-18"])
        self.assertEqual(coverage["read_days"], ["2026-05-20", "2026-05-19"])
        self.assertEqual(coverage["sampled_days"], ["2026-05-20"])
        self.assertEqual(coverage["empty_days"], ["2026-05-19"])
        self.assertEqual(coverage["unreadable_days"], ["2026-05-18"])
        self.assertEqual(coverage["byte_truncated_days"], ["2026-05-20"])
        self.assertTrue(report["records"][0]["content_truncated"])
        self.assertEqual(coverage["unsampled_days"], [])
        self.assertTrue(report["read_errors"])
        self.assertTrue(report["limits"]["truncated_by_limits"])

    def test_supplemental_window_selects_only_older_shards_within_the_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            with mock.patch.object(intake.Path, "cwd", return_value=root):
                args = intake.parse_args(
                    [
                        "--memory-root",
                        str(root),
                        "--older-than-day",
                        "2026-05-18",
                        "--max-shards",
                        "2",
                    ]
                )
                report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["scope"]["basis"], "supplemental-historical-window")
            self.assertEqual(
                report["source"]["daily_shards_considered"],
                ["2026-05-17.md", "2026-05-16.md"],
            )
            self.assertTrue(all(record["shard"] < "2026-05-18.md" for record in report["records"]))

    def test_supplemental_window_keeps_older_records_available_even_when_beyond_freshness_threshold(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            with mock.patch.object(intake.Path, "cwd", return_value=root):
                args = intake.parse_args(
                    [
                        "--memory-root",
                        str(root),
                        "--older-than-day",
                        "2026-05-19",
                        "--max-age-days",
                        "1",
                    ]
                )
                report = intake.build_report(args)

            self.assertEqual(report["status"], "available")
            self.assertEqual(report["scope"]["basis"], "supplemental-historical-window")
            self.assertEqual(report["freshness"]["classification"], "stale")
            self.assertIn("2026-05-18.md", report["source"]["daily_shards_considered"])

    def test_supplemental_window_reports_empty_window_without_claiming_global_absence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            with mock.patch.object(intake.Path, "cwd", return_value=root):
                args = intake.parse_args(
                    ["--memory-root", str(root), "--older-than-day", "2026-05-16"]
                )
                report = intake.build_report(args)

            self.assertEqual(report["status"], "insufficient")
            self.assertEqual(report["source"]["daily_shards_considered"], [])
            self.assertEqual(report["scope"]["historical_shards_considered"], 0)

    def test_supplemental_window_rejects_explicitly_narrowed_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)

            with mock.patch.object(intake.Path, "cwd", return_value=root):
                args = intake.parse_args(
                    [
                        "--memory-root",
                        str(root),
                        "--older-than-day",
                        "2026-05-18",
                        "--scope",
                        "payment",
                    ]
                )
                report = intake.build_report(args)

            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(report["source"]["daily_shards_considered"], [])
            self.assertIn("cannot widen or combine", " ".join(report["notes"]).lower())

    def test_supplemental_window_does_not_read_traces_when_policy_disables_trace_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            self.write_historical_shards(root)
            config_path = Path(temp_dir) / "analysis-config.json"
            config_path.write_text(
                '{"analysis":{"source_policy":{"enabled_source_classes":["durable_memory_context"]}}}\n',
                encoding="utf-8",
            )

            args = intake.parse_args(
                [
                    "--memory-root",
                    str(root),
                    "--config",
                    str(config_path),
                    "--older-than-day",
                    "2026-05-18",
                ]
            )
            with mock.patch.object(intake.Path, "cwd", return_value=Path(temp_dir)), mock.patch.object(
                intake,
                "collect_records",
            ) as collect_records:
                report = intake.build_report(args)

            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(report["source"]["daily_shards_considered"], [])
            self.assertEqual(report["records"], [])
            self.assertIn("disables trace_evidence", report["reason"])
            collect_records.assert_not_called()

    def test_supplemental_window_refuses_configured_narrow_default_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)
            config_dir = root / ".claude"
            config_dir.mkdir()
            (config_dir / "memory-context-intelligence.config.json").write_text(
                '{"analysis":{"scope_policy":{"default_scope_mode":"day","scope_day_shard":"2026-05-19"}}}\n',
                encoding="utf-8",
            )

            with mock.patch.object(intake.Path, "cwd", return_value=root):
                args = intake.parse_args(
                    [
                        "--memory-root",
                        str(root),
                        "--config",
                        str(config_dir / "memory-context-intelligence.config.json"),
                        "--older-than-day",
                        "2026-05-18",
                    ]
                )
                report = intake.build_report(args)

            self.assertEqual(report["status"], "unavailable")
            self.assertEqual(report["records"], [])
            self.assertIn("configured narrow scope", " ".join(report["notes"]).lower())

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

    def test_config_scope_policy_day_applies_when_no_explicit_narrowing_is_given(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)
            claude_root = root / ".claude"
            claude_root.mkdir()
            config_path = claude_root / "memory-context-intelligence.config.json"
            config_path.write_text(
                textwrap.dedent(
                    """
                    {
                      "analysis": {
                        "scope_policy": {
                          "default_scope_mode": "day",
                          "scope_day_shard": "2026-05-19",
                          "scope_session_id": null,
                          "scope_lookback_minutes": null
                        },
                        "source_policy": {
                          "enabled_source_classes": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                          "max_historical_shards": 10,
                          "allow_same_day_widening": true
                        }
                      }
                    }
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            with mock.patch.object(intake.Path, "cwd", return_value=root), mock.patch.object(intake.Path, "home", return_value=root):
                args = intake.parse_args(["--memory-root", str(root)])
                report = intake.build_report(args)

            self.assertEqual(report["scope"]["basis"], "config-default-day")
            self.assertEqual(report["scope_policy"]["default_scope_mode"], "day")
            self.assertEqual(report["scope_policy"]["scope_day_shard"], "2026-05-19")
            self.assertEqual(report["source"]["daily_shards_considered"], ["2026-05-19.md"])
            self.assertEqual([record["session_id"] for record in report["records"]], ["session-d"])

    def test_explicit_day_override_beats_config_scope_policy(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_historical_shards(root)
            claude_root = root / ".claude"
            claude_root.mkdir()
            config_path = claude_root / "memory-context-intelligence.config.json"
            config_path.write_text(
                '{"analysis":{"scope_policy":{"default_scope_mode":"day","scope_day_shard":"2026-05-19","scope_session_id":null,"scope_lookback_minutes":null}}}\n',
                encoding="utf-8",
            )

            with mock.patch.object(intake.Path, "cwd", return_value=root), mock.patch.object(intake.Path, "home", return_value=root):
                args = intake.parse_args(["--memory-root", str(root), "--day", "2026-05-20"])
                report = intake.build_report(args)

            self.assertEqual(report["scope"]["basis"], "explicit-day")
            self.assertEqual(report["source"]["daily_shards_considered"], ["2026-05-20.md"])

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
            claude_root = Path(temp_dir) / ".claude"
            claude_root.mkdir()
            (claude_root / "memory-context-intelligence.config.json").write_text(
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
            with mock.patch.object(intake.Path, "cwd", return_value=project_dir), mock.patch.object(intake.Path, "home", return_value=Path(temp_dir)):
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
            claude_root = Path(temp_dir) / ".claude"
            claude_root.mkdir()
            (claude_root / "memory-context-intelligence.config.json").write_text(
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
            with mock.patch.object(intake.Path, "cwd", return_value=project_dir), mock.patch.object(intake.Path, "home", return_value=Path(temp_dir)):
                report = intake.build_report(args)

            self.assertTrue(report["source_policy"]["loaded"])
            self.assertTrue(report["source_policy"]["requested_same_day_widening"])
            self.assertFalse(report["source_policy"]["effective_same_day_widening"])
            self.assertEqual(report["status"], "insufficient")
            self.assertEqual(report["records"], [])
            self.assertFalse(report["scope"]["same_day_widened"])
            self.assertIn("stayed narrow", report["source_policy"]["policy_note"].lower())

    def test_progressive_batches_resume_from_oldest_unprocessed_record(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            for day, session, text in [
                ("2026-05-18", "oldest", "oldest evidence"),
                ("2026-05-19", "middle", "middle evidence"),
                ("2026-05-20", "newest", "newest evidence"),
            ]:
                (root / f"{day}.md").write_text(
                    f"## Session 10:00\n\n### 10:00\n<!-- session:{session} turn:t1 transcript:/tmp/{session}.jsonl -->\n- {text}\n",
                    encoding="utf-8",
                )

            shards = intake.discover_daily_shards(root)
            first = intake.collect_progressive_records(
                shards,
                [],
                max_records=1,
                max_chars=1000,
                max_shard_bytes=65536,
                checkpoint=None,
            )
            self.assertEqual([record["content"] for record in first["records"]], ["oldest evidence"])
            self.assertEqual(first["next_position"]["shard"], "2026-05-18.md")
            self.assertTrue(first["coverage"]["complete"])

            second = intake.collect_progressive_records(
                shards,
                [],
                max_records=1,
                max_chars=1000,
                max_shard_bytes=65536,
                checkpoint=first["next_position"],
            )
            self.assertEqual([record["content"] for record in second["records"]], ["middle evidence"])

    def test_progressive_batches_continue_inside_appended_day(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            shard = root / "2026-05-20.md"
            shard.write_text(
                "## Session 10:00\n\n### 10:00\n<!-- session:s turn:t1 transcript:/tmp/s.jsonl -->\n- first\n- second\n",
                encoding="utf-8",
            )

            first = intake.collect_progressive_records(
                [shard], [], max_records=1, max_chars=1000, max_shard_bytes=65536, checkpoint=None
            )
            with shard.open("a", encoding="utf-8") as handle:
                handle.write("- appended\n")

            second = intake.collect_progressive_records(
                [shard], [], max_records=1, max_chars=1000, max_shard_bytes=65536,
                checkpoint=first["next_position"],
            )
            self.assertEqual([record["content"] for record in second["records"]], ["second"])

            third = intake.collect_progressive_records(
                [shard], [], max_records=1, max_chars=1000, max_shard_bytes=65536,
                checkpoint=second["next_position"],
            )
            self.assertEqual([record["content"] for record in third["records"]], ["appended"])

    def test_progressive_rewrite_is_blocked_and_character_budget_retains_whole_record(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            shard = root / "2026-01-01.md"
            shard.write_text("### 10:00\n- first\n- second\n")
            first = intake.collect_progressive_records([shard], [], 8, 8, 65536, checkpoint=None)
            self.assertEqual([r["content"] for r in first["records"]], ["first"])
            self.assertTrue(first["coverage"]["complete"])
            self.assertTrue(first["remaining"])
            second = intake.collect_progressive_records([shard], [], 8, 8, 65536, checkpoint=first["next_position"])
            self.assertEqual([r["content"] for r in second["records"]], ["second"])
            shard.write_text("### 10:00\n- rewritten\n- second\n")
            with self.assertRaisesRegex(ValueError, "source-changed"):
                intake.collect_progressive_records([shard], [], 8, 8, 65536, checkpoint=first["next_position"])

    def test_progressive_byte_windows_do_not_skip_split_lines_or_multibyte_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            shard = Path(temp_dir) / "2026-01-01.md"
            content = "### 10:00\n" + "".join(f"- หลักฐาน {number}\n" for number in range(25))
            shard.write_text(content, encoding="utf-8")
            position = None
            found = []
            for _ in range(30):
                batch = intake.collect_progressive_records([shard], [], 8, 1000, 95, checkpoint=position)
                found.extend(r["content"] for r in batch["records"])
                if not batch["remaining"]:
                    break
                self.assertTrue(batch["coverage"]["complete"])
                self.assertNotEqual(position, batch["next_position"])
                position = batch["next_position"]
            self.assertEqual(found, [f"หลักฐาน {number}" for number in range(25)])

    def test_progressive_cursor_digest_binds_the_bytes_actually_parsed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            shard = Path(temp_dir) / "2026-01-01.md"
            shard.write_text("### 10:00\n- original\n")
            real_digest = intake.prefix_digest
            calls = 0
            def rewrite_before_post_read_digest(path, size):
                nonlocal calls
                calls += 1
                if calls == 3:
                    shard.write_text("### 10:00\n- changed!\n")
                return real_digest(path, size)
            with mock.patch.object(intake, "prefix_digest", side_effect=rewrite_before_post_read_digest):
                batch = intake.collect_progressive_records([shard], [], 8, 1000, 65536, checkpoint=None)
            if calls < 3:
                shard.write_text("### 10:00\n- changed!\n")
            with self.assertRaisesRegex(ValueError, "source-changed"):
                intake.validate_progressive_source({"memory_root": temp_dir, "prefixes": batch["next_position"]["completed"]})

    def test_progressive_byte_limited_input_is_not_complete(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "memory-root"
            root.mkdir()
            shard = root / "2026-05-20.md"
            shard.write_text(
                "## Session 10:00\n\n### 10:00\n<!-- session:s turn:t1 transcript:/tmp/s.jsonl -->\n- a long record that crosses the byte boundary\n",
                encoding="utf-8",
            )

            batch = intake.collect_progressive_records(
                [shard], [], max_records=5, max_chars=1000, max_shard_bytes=24, checkpoint=None
            )
            self.assertFalse(batch["coverage"]["complete"])
            self.assertTrue(batch["coverage"]["byte_limited_days"])


if __name__ == "__main__":
    unittest.main()
