#!/usr/bin/env python3
"""Focused checks for phase-015 bounded live additional-stage trial."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
LIVE_TRIAL_PATH = PACKAGE_ROOT / "lib" / "live_trial.py"
SPEC = importlib.util.spec_from_file_location("mci_live_trial", LIVE_TRIAL_PATH)
live_trial = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(live_trial)


def write_memory_shard(memory_root: Path) -> None:
    memory_root.mkdir(parents=True, exist_ok=True)
    (memory_root / "2026-05-18.md").write_text(
        "\n".join(
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
                "name": "phase-015-controlled-source-fixture",
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
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def stage_map(report: dict) -> dict[str, dict]:
    return {stage["stage"]: stage for stage in report["stage_statuses"]}


class LiveTrialTests(unittest.TestCase):
    def test_trial_runs_full_chain_and_writes_one_additional_file(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir, tempfile.TemporaryDirectory() as additional_dir:
            memory_root = Path(memory_dir)
            additional_root = Path(additional_dir)
            fixture_path = memory_root / "sources.json"
            write_memory_shard(memory_root)
            write_source_fixture(fixture_path)

            args = live_trial.parse_args(
                [
                    "--memory-root",
                    str(memory_root),
                    "--max-shards",
                    "1",
                    "--max-records",
                    "3",
                    "--sources-fixture",
                    str(fixture_path),
                    "--owner-domain",
                    "evidence-discipline",
                    "--main-rule-target",
                    "rules/evidence-discipline.md",
                    "--additional-root",
                    str(additional_root),
                    "--additional-relative-path",
                    "memory-context-intelligence/phase-015-live-trial-test.md",
                    "--approved-write",
                ]
            )

            report = live_trial.build_live_trial_report(args)
            stages = stage_map(report)
            destination = Path(report["emission"]["destination_path"])
            material = destination.read_text(encoding="utf-8")

            self.assertEqual(report["status"], "trial-emitted")
            self.assertEqual(report["trial_disposition"], "continue")
            for stage in ("intake", "signals", "present", "choose", "enrich", "orchestrate", "packet", "emit"):
                self.assertTrue(stages[stage]["ok"], stage)
            self.assertTrue(report["candidate_packet_approved_for_trial_write"])
            self.assertTrue(report["emission"]["approved_write"])
            self.assertTrue(report["emission"]["additional_emission_performed"])
            self.assertTrue(destination.exists())
            self.assertEqual(destination.relative_to(additional_root).as_posix(), "memory-context-intelligence/phase-015-live-trial-test.md")
            self.assertTrue(report["emission_checks"]["emitted_file_exists"])
            self.assertTrue(report["emission_checks"]["material_contains_success_criteria"])
            self.assertTrue(report["emission_checks"]["material_contains_rollback_notes"])
            self.assertIn("## Topic scope", material)
            self.assertIn("## Success criteria", material)
            self.assertIn("## Rollback notes", material)
            audit = report["live_trial_boundary_audit"]
            self.assertTrue(audit["additional_emission_performed"])
            self.assertFalse(audit["main_rules_mutation_performed"])
            self.assertFalse(audit["install_or_publication_performed"])
            self.assertFalse(audit["live_web_access_performed"])
            self.assertFalse(audit["external_agent_process_spawned"])

    def test_trial_preview_does_not_write_and_requires_revision_disposition(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir, tempfile.TemporaryDirectory() as additional_dir:
            memory_root = Path(memory_dir)
            additional_root = Path(additional_dir)
            fixture_path = memory_root / "sources.json"
            write_memory_shard(memory_root)
            write_source_fixture(fixture_path)

            args = live_trial.parse_args(
                [
                    "--memory-root",
                    str(memory_root),
                    "--max-shards",
                    "1",
                    "--max-records",
                    "3",
                    "--sources-fixture",
                    str(fixture_path),
                    "--owner-domain",
                    "evidence-discipline",
                    "--main-rule-target",
                    "rules/evidence-discipline.md",
                    "--additional-root",
                    str(additional_root),
                    "--additional-relative-path",
                    "memory-context-intelligence/phase-015-preview-test.md",
                ]
            )

            report = live_trial.build_live_trial_report(args)
            destination = Path(report["emission"]["destination_path"])

            self.assertEqual(report["status"], "trial-preview")
            self.assertEqual(report["trial_disposition"], "revise")
            self.assertFalse(report["emission"]["approved_write"])
            self.assertFalse(report["emission"]["additional_emission_performed"])
            self.assertFalse(destination.exists())
            self.assertFalse(report["emission_checks"]["emitted_file_exists"])
            self.assertTrue(report["emission_checks"]["material_contains_success_criteria"])
            self.assertTrue(report["emission_checks"]["material_contains_rollback_notes"])
            self.assertFalse(report["main_rules_mutation_performed"])


if __name__ == "__main__":
    unittest.main()
