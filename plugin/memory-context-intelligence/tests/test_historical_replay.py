#!/usr/bin/env python3
"""Focused checks for phase-014 deterministic historical replay."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_REPLAY_PATH = PACKAGE_ROOT / "lib" / "historical_replay.py"
SPEC = importlib.util.spec_from_file_location("mci_historical_replay", HISTORICAL_REPLAY_PATH)
historical_replay = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(historical_replay)


def write_memory_shard(memory_root: Path, *, content: str | None = None) -> None:
    memory_root.mkdir(parents=True, exist_ok=True)
    (memory_root / "2026-05-18.md").write_text(
        content
        or "\n".join(
            (
                "# Recent Memory",
                "### feedback",
                "- Do not claim fixed before verification; report evidence limits clearly and cite checked scope.",
                "- Avoid claiming fixed before verification; keep evidence limits visible before completion wording.",
                "- Prefer source trust and governance support before strengthening candidate rule packets.",
            )
        ),
        encoding="utf-8",
    )


def write_source_fixture(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "name": "phase-014-controlled-source-fixture",
                "recorded_at": "2026-05-18",
                "sources": [
                    {
                        "id": "official-docs",
                        "title": "Official documentation on verification wording",
                        "source_type": "official_docs",
                        "freshness": "current",
                        "checked_at": "2026-05-18",
                        "supports": ["Completion wording should identify checked scope and evidence limits."],
                        "constraints": [
                            "Do not call behavior fixed without verification covering the failure scope."
                        ],
                    },
                    {
                        "id": "weak-blog",
                        "title": "Weak commentary with broad claims",
                        "source_type": "blog",
                        "freshness": "unknown",
                        "supports": ["Always use one-word completion labels."],
                        "conflicts": ["Conflicts with evidence-scope wording."],
                        "limitations": ["Anecdotal and not source-of-truth guidance."],
                    },
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def stage_map(report: dict) -> dict[str, dict]:
    return {stage["stage"]: stage for stage in report["stage_statuses"]}


class HistoricalReplayTests(unittest.TestCase):
    def test_replay_runs_full_chain_with_fixture_and_dry_run_preview(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir, tempfile.TemporaryDirectory() as additional_dir:
            memory_root = Path(memory_dir)
            additional_root = Path(additional_dir)
            fixture_path = memory_root / "sources.json"
            write_memory_shard(memory_root)
            write_source_fixture(fixture_path)

            args = historical_replay.parse_args(
                [
                    "--memory-root",
                    str(memory_root),
                    "--max-shards",
                    "1",
                    "--max-records",
                    "3",
                    "--sources-fixture",
                    str(fixture_path),
                    "--additional-root",
                    str(additional_root),
                    "--owner-domain",
                    "evidence-discipline",
                    "--main-rule-target",
                    "rules/evidence-discipline.md",
                    "--additional-name",
                    "phase-014-replay-trial",
                ]
            )

            report = historical_replay.build_replay_report(args)
            stages = stage_map(report)

            self.assertIn(report["status"], {"replay-completed", "replay-completed-with-adjustments"})
            for stage in ("intake", "signals", "present", "choose", "enrich", "orchestrate", "packet", "emit-preview"):
                self.assertTrue(stages[stage]["ok"], stage)
            self.assertEqual(stages["enrich"]["status"], "research-enriched")
            self.assertEqual(stages["enrich"]["summary"]["decision"], "research-needed")
            self.assertEqual(stages["emit-preview"]["status"], "preview")
            self.assertTrue(stages["emit-preview"]["summary"]["dry_run"])
            self.assertFalse(stages["emit-preview"]["summary"]["additional_emission_performed"])

            audit = report["no_write_authority_boundary_audit"]
            self.assertTrue(audit["authority_boundary_ok"])
            self.assertFalse(audit["approved_write_available_in_replay"])
            self.assertFalse(audit["approved_write_requested"])
            self.assertTrue(audit["emit_preview_dry_run"])
            self.assertFalse(audit["additional_emission_performed"])
            self.assertFalse(audit["main_rules_mutation_performed"])
            self.assertFalse(audit["install_or_publication_performed"])
            self.assertFalse(audit["live_web_access_performed"])
            self.assertFalse(audit["external_agent_process_spawned"])
            self.assertFalse(Path(audit["preview_destination_path"]).exists())

            packet_findings = report["candidate_packet_safety_findings"]
            self.assertTrue(packet_findings["packet_built"])
            self.assertEqual(packet_findings["emit_preview_status"], "preview")
            self.assertTrue(packet_findings["trial_stage_only"])
            self.assertEqual(report["bounded_historical_input"]["records_sampled"], 3)
            self.assertTrue(report["topic_quality_notes"])
            self.assertTrue(report["orchestration_lane_behavior_summary"])

    def test_replay_skips_research_without_fixture_instead_of_live_web(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir, tempfile.TemporaryDirectory() as additional_dir:
            memory_root = Path(memory_dir)
            write_memory_shard(memory_root)

            args = historical_replay.parse_args(
                [
                    "--memory-root",
                    str(memory_root),
                    "--max-shards",
                    "1",
                    "--max-records",
                    "3",
                    "--additional-root",
                    additional_dir,
                ]
            )

            report = historical_replay.build_replay_report(args)
            stages = stage_map(report)

            self.assertIn(stages["enrich"]["status"], {"research-skipped", "research-enriched"})
            self.assertTrue(stages["enrich"]["ok"])
            self.assertFalse(stages["enrich"]["summary"]["live_web_access_performed"])
            self.assertFalse(report["live_web_access_performed"])
            self.assertTrue(report["no_write_authority_boundary_audit"]["authority_boundary_ok"])

    def test_replay_reports_blocked_chain_when_no_topic_can_be_selected(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir:
            memory_root = Path(memory_dir)
            write_memory_shard(
                memory_root,
                content="\n".join(
                    (
                        "# Recent Memory",
                        "### feedback",
                        "- unrelated local note without matching replay scope",
                    )
                ),
            )

            args = historical_replay.parse_args(
                [
                    "--memory-root",
                    str(memory_root),
                    "--scope",
                    "memory-context-intelligence",
                    "--max-shards",
                    "1",
                    "--max-records",
                    "3",
                    "--skip-emit-preview",
                ]
            )

            report = historical_replay.build_replay_report(args)
            stages = stage_map(report)

            self.assertEqual(report["status"], "replay-blocked")
            self.assertEqual(stages["present"]["status"], "no-topics")
            self.assertFalse(stages["downstream-chain"]["ok"])
            self.assertIn("no topic candidates", stages["downstream-chain"]["summary"]["reason"])
            self.assertTrue(report["no_write_authority_boundary_audit"]["authority_boundary_ok"])
            self.assertFalse(report["additional_emission_performed"])
            self.assertFalse(report["main_rules_mutation_performed"])


if __name__ == "__main__":
    unittest.main()
