#!/usr/bin/env python3
"""Focused checks for phase-016 checked-scope readiness reporting."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
READINESS_PATH = PACKAGE_ROOT / "lib" / "readiness.py"
SPEC = importlib.util.spec_from_file_location("mci_readiness", READINESS_PATH)
readiness = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(readiness)


def write_memory_shard(memory_root: Path) -> None:
    memory_root.mkdir(parents=True, exist_ok=True)
    shard_day = date.today().isoformat()
    (memory_root / f"{shard_day}.md").write_text(
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
                "name": "phase-016-controlled-source-fixture",
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


def write_main_rules_root(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "README.md").write_text("# Main RULES checked-scope fixture\n", encoding="utf-8")
    (root / "evidence-discipline.md").write_text(
        "# Evidence Discipline fixture\n\nNo readiness command should mutate this file.\n",
        encoding="utf-8",
    )


def stage_map(report: dict) -> dict[str, dict]:
    return {stage["stage"]: stage for stage in report["stage_statuses"]}


class ReadinessTests(unittest.TestCase):
    def test_ready_runs_full_chain_and_reports_checked_scope_usability(self) -> None:
        with tempfile.TemporaryDirectory() as memory_dir, tempfile.TemporaryDirectory() as additional_dir, tempfile.TemporaryDirectory() as rules_dir:
            memory_root = Path(memory_dir)
            additional_root = Path(additional_dir) / "rules" / "additional"
            additional_root.mkdir(parents=True)
            rules_root = Path(rules_dir)
            fixture_path = memory_root / "sources.json"
            write_memory_shard(memory_root)
            write_source_fixture(fixture_path)
            write_main_rules_root(rules_root)

            args = readiness.parse_args(
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
                    "memory-context-intelligence/phase-016-readiness-test.md",
                    "--trial-approved-write",
                    "--main-rules-root",
                    str(rules_root),
                ]
            )

            report = readiness.build_readiness_report(args)
            phase_record = {item["phase"]: item for item in report["phase_007_015_evidence_record"]}
            focused = report["verification_record"]["focused_end_to_end_stages"]
            live_summary = report["live_trial_result_summary"]
            boundary = report["boundary_audit_summary"]
            destination = Path(live_summary["artifact_summary"]["artifacts"][0]["path"])

            self.assertEqual(report["status"], "usable in checked scope")
            self.assertEqual(report["final_readiness_wording_used"], "usable in checked scope")
            self.assertEqual(report["main_rules_merge_statement"], "main RULES merge has not happened")
            self.assertTrue(report["readiness_gates"]["ok"])
            self.assertEqual(report["readiness_gates"]["failed_gates"], [])
            self.assertEqual(report["readiness_gates"]["boundary_violations"], [])
            self.assertTrue(all(item["ok"] for item in phase_record.values()))
            self.assertTrue(all(focused.values()))
            self.assertEqual(report["selected_invocation_surface"]["command"], "ready")
            self.assertIn("ready", report["selected_invocation_surface"]["command_map"])
            self.assertIn("stable behavior", report["not_claimed"])
            self.assertIn("broad production readiness", report["not_claimed"])
            self.assertIn("main RULES promotion", report["not_claimed"])
            self.assertIn("main RULES merge", report["not_claimed"])
            self.assertIn(report["replay_result_summary"]["status"], {"replay-completed", "replay-completed-with-adjustments"})
            self.assertTrue(report["replay_result_summary"]["emit_preview_dry_run"])
            self.assertEqual(live_summary["status"], "trial-emitted")
            self.assertTrue(live_summary["artifact_summary"]["ok"])
            checked_artifact = live_summary["artifact_summary"]["artifacts"][0]
            self.assertTrue(checked_artifact["standalone_artifact_valid"])
            self.assertEqual(checked_artifact["forbidden_dependencies"], [])
            self.assertTrue(checked_artifact["selected_for_additional_trial"])
            self.assertFalse(checked_artifact["main_rules_promotion_approved"])
            self.assertIn("emit-selected", report["selected_invocation_surface"]["command_map"])
            self.assertTrue(destination.exists())
            self.assertEqual(
                destination.relative_to(additional_root).as_posix(),
                "memory-context-intelligence/phase-016-readiness-test.md",
            )
            self.assertEqual(boundary["main_rules_merge_status"], "main RULES merge has not happened")
            self.assertTrue(boundary["main_rules_unchanged_checked"])
            self.assertTrue(boundary["main_rules_unchanged"])
            self.assertFalse(boundary["main_rules_mutation_performed"])
            self.assertFalse(boundary["install_or_publication_performed"])
            self.assertFalse(boundary["marketplace_release_performed"])
            self.assertFalse(boundary["stable_behavior_claimed"])
            self.assertFalse(boundary["broad_production_readiness_claimed"])
            self.assertFalse(boundary["main_rules_promotion_claimed"])

    def test_ready_blocks_when_trial_artifact_evidence_is_missing(self) -> None:
        replay_report = {
            "status": "replay-completed-with-adjustments",
            "stage_statuses": [
                {"stage": stage, "status": "ok", "ok": True, "summary": {}}
                for stage in readiness.REQUIRED_REPLAY_STAGES
            ],
            "no_write_authority_boundary_audit": {
                "authority_boundary_ok": True,
                "emit_preview_dry_run": True,
            },
            "adjustments_needed_before_phase_015": [],
        }
        trial_report = {
            "status": "trial-preview",
            "stage_statuses": [
                {"stage": stage, "status": "ok", "ok": True, "summary": {}}
                for stage in readiness.REQUIRED_TRIAL_STAGES
            ],
            "emission": {"additional_emission_performed": False},
            "live_trial_boundary_audit": {
                "main_rules_mutation_performed": False,
                "install_or_publication_performed": False,
                "live_web_access_performed": False,
                "external_agent_process_spawned": False,
            },
        }

        with tempfile.TemporaryDirectory() as reports_dir, tempfile.TemporaryDirectory() as rules_dir:
            reports_root = Path(reports_dir)
            rules_root = Path(rules_dir)
            write_main_rules_root(rules_root)
            replay_path = reports_root / "replay.json"
            trial_path = reports_root / "trial.json"
            replay_path.write_text(json.dumps(replay_report), encoding="utf-8")
            trial_path.write_text(json.dumps(trial_report), encoding="utf-8")

            args = readiness.parse_args(
                [
                    "--replay-report",
                    str(replay_path),
                    "--trial-report",
                    str(trial_path),
                    "--main-rules-root",
                    str(rules_root),
                ]
            )

            report = readiness.build_readiness_report(args)
            stages = stage_map(trial_report)

            self.assertTrue(all(stages[stage]["ok"] for stage in readiness.REQUIRED_TRIAL_STAGES))
            self.assertEqual(report["status"], "readiness-blocked")
            self.assertEqual(report["final_readiness_wording_used"], "not usable in checked scope")
            self.assertIn("phase-015", report["readiness_gates"]["failed_gates"])
            self.assertFalse(report["live_trial_result_summary"]["artifact_summary"]["ok"])
            self.assertTrue(report["verification_record"]["main_rules_unchanged_audit"]["ok"])

    def test_ready_blocks_for_thin_or_ephemeral_dependent_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_root:
            root = Path(temp_root)
            thin = root / "thin.md"
            thin.write_text(
                "# Thin trial\n\n## Success criteria\n- present\n\n## Rollback notes\n- present\n",
                encoding="utf-8",
            )
            ephemeral = root / "ephemeral.md"
            ephemeral.write_text(
                "\n".join(
                    [
                        "# Additional trial rule: Invalid dependency",
                        "> **Main RULES mutation:** Not performed",
                        "This additional-stage artifact is scoped to one selected topic per artifact.",
                        *readiness.candidate_packet.REQUIRED_STANDALONE_HEADINGS,
                        "Evidence must be reconstructed from .memsearch/memory/2026-08-09.md.",
                    ]
                ),
                encoding="utf-8",
            )

            thin_check = readiness.path_contains_markers(thin)
            ephemeral_check = readiness.path_contains_markers(ephemeral)

            self.assertFalse(thin_check["standalone_artifact_valid"])
            self.assertTrue(thin_check["missing_headings"])
            self.assertFalse(ephemeral_check["standalone_artifact_valid"])
            self.assertTrue(ephemeral_check["forbidden_dependencies"])


if __name__ == "__main__":
    unittest.main()
