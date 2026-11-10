from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_SURFACE_PATH = PACKAGE_ROOT / "lib" / "analysis_surface.py"
SPEC = importlib.util.spec_from_file_location("mci_analysis_surface", ANALYSIS_SURFACE_PATH)
analysis_surface = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(analysis_surface)


class AnalysisSurfacePayloadTests(unittest.TestCase):
    def test_analysis_surface_passes_explicit_config_argument_and_surfaces_loaded_source_policy(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "Historical trace evidence is the primary signal. Config policy limited this run to trace_evidence only.",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-config-test-") as temp_dir:
            temp_path = Path(temp_dir)
            config_path = temp_path / "memory-context-intelligence.config.json"
            config_path.write_text('{"analysis":{"source_policy":{"enabled_source_classes":["trace_evidence"]}}}\n', encoding="utf-8")

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "raw-day-shard-scope", "source_classes_present": ["trace_evidence"]},
                            "source_policy": {
                                "loaded": True,
                                "config_path": str(config_path),
                                "config_source": "cli",
                                "policy_limited": True,
                                "effective_source_classes": ["trace_evidence"],
                                "policy_note": "Config policy limited this run to trace_evidence only.",
                            },
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                    "--arguments",
                    f"config={config_path}",
                ])

        self.assertEqual(exit_code, 0)
        intake_command = mock_run.call_args_list[0].args[0]
        self.assertIn("--config", intake_command)
        self.assertIn(str(config_path), intake_command)
        payload = captured[0]
        self.assertTrue(payload["source_policy"]["loaded"])
        self.assertEqual(payload["source_policy"]["config_path"], str(config_path))
        self.assertIn("trace_evidence", payload["source_policy"]["policy_note"])

    def test_analysis_surface_passes_scope_policy_through_when_config_is_loaded(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-scope-policy-") as temp_dir:
            temp_path = Path(temp_dir)
            home_path = temp_path / "home"

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.object(
                analysis_surface.Path,
                "home",
                return_value=home_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "config-default-day", "day_shard": "2026-06-02", "same_day_widened": False},
                            "scope_policy": {
                                "default_scope_mode": "day",
                                "scope_day_shard": "2026-06-02",
                                "scope_session_id": None,
                                "scope_lookback_minutes": None,
                            },
                            "source": {"retrieval_mode": "raw-day-shard-scope", "source_classes_present": ["trace_evidence"]},
                            "source_policy": {
                                "loaded": True,
                                "config_path": str(home_path / ".claude" / "memory-context-intelligence.config.json"),
                                "config_source": "auto-upward",
                                "policy_limited": False,
                                "effective_source_classes": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                                "policy_note": "Config file loaded without changing the active source-policy limits.",
                            },
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-06-02",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertEqual(payload["scope_basis"], "config-default-day")
        self.assertEqual(payload["scope_day_shard"], "2026-06-02")
        self.assertEqual(payload["scope_policy"]["default_scope_mode"], "day")

    def test_analysis_surface_surfaces_guided_config_questions_when_no_config_is_loaded(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "Historical trace evidence is the primary signal.",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-guided-config-") as temp_dir:
            temp_path = Path(temp_dir)
            home_path = temp_path / "home"

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.object(
                analysis_surface.Path,
                "home",
                return_value=home_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "raw-day-shard-scope", "source_classes_present": ["trace_evidence"]},
                            "source_policy": {
                                "loaded": False,
                                "config_path": None,
                                "config_source": "none",
                                "policy_limited": False,
                                "effective_source_classes": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                                "policy_note": "No config file was loaded; runtime defaults remain active.",
                            },
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                ])

        self.assertEqual(exit_code, 0)
        intake_command = mock_run.call_args_list[0].args[0]
        self.assertNotIn("--config", intake_command)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        self.assertIn("config_questions", payload)
        self.assertTrue(payload["config_questions"]["advisory_only"])
        self.assertEqual(
            payload["config_questions"]["suggested_config_path"],
            str(home_path / ".claude" / "memory-context-intelligence.config.json"),
        )
        self.assertEqual(len(payload["config_questions"]["questions"]), 4)

    def test_analysis_surface_surfaces_adaptive_deep_analysis_plan(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "medium",
                    "evidence_summary": "Historical trace evidence is the primary signal.",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-adaptive-") as temp_dir:
            temp_path = Path(temp_dir)

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-06-01", "same_day_widened": False},
                            "source": {
                                "retrieval_mode": "raw-day-shard-scope",
                                "source_classes_present": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                            },
                            "source_policy": {
                                "loaded": False,
                                "config_path": None,
                                "config_source": "none",
                                "policy_limited": False,
                                "effective_source_classes": ["trace_evidence", "recall_evidence", "durable_memory_context", "governance_context"],
                                "policy_note": "No config file was loaded; runtime defaults remain active.",
                            },
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "ranked_signals": [
                                {
                                    "id": "signal-001",
                                    "rank": 1,
                                    "kind": "blocker",
                                    "review_focus": "evidence-boundary",
                                    "confidence": "medium",
                                    "keywords": ["verification", "policy"],
                                    "source_classes": ["trace_evidence", "governance_context"],
                                    "source_mix_label": "trace_evidence + governance_context",
                                    "trace_record_count": 2,
                                    "historical_strength": "2 trace record(s) across 2 session(s) and 2 shard(s)",
                                    "current_session_confirmation": "historical-only",
                                }
                            ],
                            "topic_candidates": [
                                {
                                    "rank": 1,
                                    "id": "topic-001",
                                    "title": "Strengthen evidence discipline around completion claims",
                                    "confidence": "medium",
                                    "promotion_tier": "promoted-candidate",
                                    "source_signal_ids": ["signal-001"],
                                }
                            ],
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-06-01",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertIn("adaptive_deep_analysis", payload)
        self.assertEqual(payload["adaptive_deep_analysis"]["strategy"], "adaptive-escalate")
        self.assertTrue(payload["adaptive_deep_analysis"]["all_four_internal_sources_default"])
        self.assertTrue(payload["adaptive_deep_analysis"]["deepening_required"])
        self.assertTrue(payload["adaptive_deep_analysis"]["must_deepen_before_first_response"])
        self.assertEqual(payload["adaptive_deep_analysis"]["required_topic_ids"], ["topic-001"])
        self.assertTrue(payload["adaptive_deep_analysis"]["tool_unavailability_requires_note"])
        self.assertIn("must perform one bounded deepening pass", payload["adaptive_deep_analysis"]["execution_contract"])
        self.assertEqual(
            payload["adaptive_deep_analysis"]["topic_deepening_candidates"][0]["recommended_mode"],
            "subagent+external-research",
        )
        self.assertTrue(payload["adaptive_deep_analysis"]["subagent_deepening_allowed"])
        self.assertTrue(payload["adaptive_deep_analysis"]["external_research_enrichment_allowed"])
        self.assertTrue(payload["adaptive_deep_analysis"]["advisory_only_before_selection"])
        self.assertEqual(payload["adaptive_deep_analysis"]["packet_artifact_scope_after_selection"], "single-topic-only")
        self.assertFalse(payload["adaptive_deep_analysis"]["multi_topic_deepening_combines_packet_output"])
        self.assertIn("trace_evidence remains the live promotion anchor", payload["adaptive_deep_analysis"]["trace_anchor_rule"])

    def test_analysis_surface_emits_advisory_stale_session_warning_when_plugin_update_is_newer_than_session(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 2 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-stale-test-") as temp_dir:
            temp_path = Path(temp_dir)
            transcript_path = temp_path / "session-123.jsonl"
            transcript_path.write_text(
                '{"timestamp":"2026-05-01T10:00:00Z"}\n',
                encoding="utf-8",
            )

            home_path = temp_path / "home"
            registry_path = home_path / ".claude" / "plugins"
            registry_path.mkdir(parents=True)
            (registry_path / "installed_plugins.json").write_text(
                """
{
  "version": 2,
  "plugins": {
    "memory-context-intelligence@darkwingtm": [
      {
        "scope": "local",
        "projectPath": "TEMP_PROJECT_PATH",
        "installPath": "/tmp/mci/0.9.21",
        "version": "0.9.21",
        "lastUpdated": "2026-05-30T15:25:41.845Z"
      }
    ]
  }
}
                """.replace("TEMP_PROJECT_PATH", temp_dir),
                encoding="utf-8",
            )

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.object(
                analysis_surface.Path,
                "home",
                return_value=home_path,
            ), patch.dict(
                analysis_surface.os.environ,
                {"CLAUDE_CODE_TRANSCRIPT_PATH": str(transcript_path)},
                clear=False,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "memsearch-search-expand", "source_classes_present": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        self.assertIn("operator_warnings", payload)
        self.assertEqual(payload["operator_warnings"][0]["type"], "stale_long_lived_session")
        self.assertEqual(payload["operator_warnings"][0]["severity"], "advisory")
        self.assertEqual(payload["operator_warnings"][0]["plugin_version"], "0.9.21")
        self.assertEqual(payload["operator_warnings"][0]["session_id"], "session-123")

    def test_analysis_surface_does_not_fabricate_stale_session_warning_without_checked_freshness_evidence(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 2 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-no-stale-proof-") as temp_dir:
            temp_path = Path(temp_dir)
            home_path = temp_path / "home"
            (home_path / ".claude" / "plugins").mkdir(parents=True)
            (home_path / ".claude" / "plugins" / "installed_plugins.json").write_text('{"version":2,"plugins":{}}', encoding="utf-8")

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.object(
                analysis_surface.Path,
                "home",
                return_value=home_path,
            ), patch.dict(
                analysis_surface.os.environ,
                {},
                clear=False,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "memsearch-search-expand", "source_classes_present": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        self.assertNotIn("operator_warnings", payload)

    def test_analysis_surface_warning_does_not_normalize_status_or_replace_topic_output(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 2 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [{"label": "What this means", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-non-normalizing-") as temp_dir:
            temp_path = Path(temp_dir)
            transcript_path = temp_path / "session-123.jsonl"
            transcript_path.write_text('{"timestamp":"2026-05-01T10:00:00Z"}\n', encoding="utf-8")
            home_path = temp_path / "home"
            registry_path = home_path / ".claude" / "plugins"
            registry_path.mkdir(parents=True)
            (registry_path / "installed_plugins.json").write_text(
                """
{
  "version": 2,
  "plugins": {
    "memory-context-intelligence@darkwingtm": [
      {
        "scope": "local",
        "projectPath": "TEMP_PROJECT_PATH",
        "installPath": "/tmp/mci/0.9.21",
        "version": "0.9.21",
        "lastUpdated": "2026-05-30T15:25:41.845Z"
      }
    ]
  }
}
                """.replace("TEMP_PROJECT_PATH", temp_dir),
                encoding="utf-8",
            )

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.object(
                analysis_surface.Path,
                "home",
                return_value=home_path,
            ), patch.dict(
                analysis_surface.os.environ,
                {"CLAUDE_CODE_TRANSCRIPT_PATH": str(transcript_path)},
                clear=False,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "memsearch-search-expand", "source_classes_present": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        self.assertEqual([card["id"] for card in payload["topic_cards"]], ["topic-001"])
        self.assertEqual(payload["next_action_options"], present_payload["next_action_options"])
        self.assertEqual(payload["operator_warnings"][0]["type"], "stale_long_lived_session")

    def test_analysis_surface_emits_related_variants_and_first_response_spine(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Turn recurring workflow findings into decision-ready proposals — goal framing",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 2 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [
                        {"label": "What this means", "value": "Convert repeated workflow findings into proposals the user can decide on immediately."},
                        {"label": "Problem", "value": "Recurring findings are being left as weak observations instead of decision-ready proposals."},
                        {"label": "Desired behavior", "value": "Turn recurring findings into a goal-level proposal with a clear next move."},
                        {"label": "Evidence examples", "value": "- Example one"},
                        {"label": "Before behavior", "value": "Old observation-only output."},
                        {"label": "After behavior", "value": "Actionable proposal output."},
                    ],
                },
                {
                    "id": "topic-002",
                    "title": "Turn recurring workflow findings into decision-ready proposals — goal framing",
                    "recommended_first": False,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 1 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [
                        {"label": "What this means", "value": "A weaker variant of the same family."},
                        {"label": "Problem", "value": "Still observation-heavy."},
                        {"label": "Desired behavior", "value": "Still move toward decision-ready output."},
                    ],
                },
                {
                    "id": "topic-003",
                    "title": "Turn recurring workflow findings into decision-ready proposals — workflow",
                    "recommended_first": False,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 1 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [
                        {"label": "What this means", "value": "A workflow-level variant."},
                        {"label": "Problem", "value": "Still observation-heavy."},
                        {"label": "Desired behavior", "value": "Still move toward decision-ready output."},
                    ],
                },
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [
                    {
                        "id": "choose-topic-number",
                        "action": "Choose Topic 1 to turn that topic into a change proposal or goal draft.",
                        "advisory_only": True,
                        "carry_forward_allowed": False,
                    },
                    {
                        "id": "type-direct-request",
                        "action": "Type a direct request in your own words and name the topic you want to adjust.",
                        "advisory_only": True,
                        "carry_forward_allowed": False,
                    },
                    {
                        "id": "deepen-with-research",
                        "action": "Ask for deep thinking, websearch, or webfetch on a topic before any adjustment.",
                        "advisory_only": True,
                        "carry_forward_allowed": False,
                    },
                ],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-test-") as temp_dir:
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=Path(temp_dir) / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=Path(temp_dir),
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{\"status\": \"available\"}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-30", "same_day_widened": False},
                            "source": {"retrieval_mode": "memsearch-search-expand", "source_classes_present": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout="{\"status\": \"available\"}", stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout="{\"status\": \"available\"}", stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-30",
                ])

        self.assertEqual(exit_code, 0)
        self.assertEqual(len(captured), 1)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        self.assertTrue(payload["analysis_request_present"])
        self.assertEqual(payload["invocation_mode"], "standalone-analysis-slash")
        self.assertTrue(payload["render_required_now"])
        self.assertFalse(payload["generic_no_request_response_allowed"])
        self.assertEqual([card["id"] for card in payload["topic_cards"]], ["topic-001", "topic-002", "topic-003"])
        self.assertTrue(payload["topic_cards"][0]["recommended_first"])
        self.assertEqual(payload["next_action_options"], present_payload["next_action_options"])
        self.assertLess(list(payload).index("topic_cards"), list(payload).index("next_action_options"))
        for forbidden_key in (
            "presentation",
            "recommendation",
            "proposal",
            "related_variants",
            "first_response_spine",
            "first_response_contract",
            "topic_list",
            "notes",
        ):
            self.assertNotIn(forbidden_key, payload)

    def test_analysis_surface_exposes_exact_initial_window_and_next_older_boundary(self) -> None:
        captured: list[dict] = []
        present_payload = {"status": "no-topics", "topic_cards": [], "next_action_options": {"options": []}}

        with tempfile.TemporaryDirectory(prefix="mci-analysis-window-") as temp_dir:
            temp_path = Path(temp_dir)
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default"},
                            "source": {
                                "daily_shards_considered": ["2026-05-20.md", "2026-05-19.md", "2026-05-18.md"],
                                "source_classes_present": ["trace_evidence"],
                            },
                            "source_policy": {"effective_source_classes": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout="{}", stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout="{}", stderr=""),
                        present_payload,
                    ),
                ]

                self.assertEqual(analysis_surface.main([]), 0)

        payload = captured[0]
        self.assertEqual(
            payload["analysis_window"],
            {
                "mode": "historical-default",
                "checked_days": ["2026-05-20", "2026-05-19", "2026-05-18"],
                "next_older_than_day": "2026-05-18",
                "supplemental_pass_used": False,
            },
        )

    def test_historical_single_day_sampling_is_not_an_explicit_day_override(self) -> None:
        coverage = {"selected_days": ["2026-05-20"], "read_days": ["2026-05-20"], "sampled_days": ["2026-05-20"], "bounded_sample_only": True}
        window = analysis_surface.analysis_window_report(
            {"scope": {"basis": "historical-default", "day_shard": "2026-05-20"}, "source": {"daily_shards_considered": ["2026-05-20.md"]}, "source_policy": {"effective_source_classes": ["trace_evidence"]}, "coverage": coverage},
            supplemental=False,
        )
        self.assertEqual(window["mode"], "historical-default")
        self.assertEqual(window["next_older_than_day"], "2026-05-20")
        self.assertEqual(window["coverage"], coverage)

    def test_analysis_wrapper_transports_ordered_canonical_evidence_in_isolation(self) -> None:
        marker = "Observed separate-account records were exposed through identity reuse."
        text = "Background description. " * 14 + marker
        with tempfile.TemporaryDirectory(prefix="mci-discovery-workflow-") as temp_dir:
            root = Path(temp_dir)
            memory = root / ".memsearch" / "memory"
            memory.mkdir(parents=True)
            home = root / "fixture-home"
            home.mkdir()
            for offset in range(10):
                day = date.today() - timedelta(days=offset)
                body = text if offset == 9 else f"Observed distinct bounded evidence for day {offset}."
                repeated = "- repeated newest-day event\n" * 12 if offset == 0 else ""
                (memory / f"{day.isoformat()}.md").write_text("### 09:00\n- " + body + "\n" + repeated, encoding="utf-8")
            env = {"HOME": str(home), "PATH": os.environ["PATH"], "TMPDIR": str(root), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
            command = ["bash", str(PACKAGE_ROOT / "bin" / "memory-context-intelligence"), "analysis-surface", "--arguments", ""]
            result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, "")
            payload = json.loads(result.stdout)
            evidence = payload["topic_discovery_evidence"]
            self.assertEqual(len(evidence), 8)
            self.assertIn(marker, evidence[0]["content"])
            window = payload["analysis_window"]
            self.assertEqual(len(window["checked_days"]), 8)
            self.assertEqual(window["coverage"]["sampled_days"], window["checked_days"])
            self.assertFalse(window["coverage"]["bounded_sample_only"])
            self.assertTrue(payload["progress"]["remaining"])
            self.assertIsNone(window["next_older_than_day"])
            self.assertFalse(any(item["content_truncated"] for item in evidence))
            evidence_refs = {item["ref"] for item in evidence}
            self.assertEqual([item["ref"] for item in evidence], [f"excerpt-{index:03d}" for index in range(1, 9)])
            self.assertTrue(payload["topic_cards"])
            for card in payload["topic_cards"]:
                self.assertTrue(card["evidence_refs"])
                self.assertTrue(set(card["evidence_refs"]) <= evidence_refs)
                self.assertFalse(card["selected_for_additional_trial"])
            result = subprocess.run(command + ["--older-than-day", (date.today() - timedelta(days=7)).isoformat()], cwd=root, env=env, capture_output=True, text=True, timeout=20)
            self.assertEqual(result.returncode, 0, result.stderr)
            supplemental = json.loads(result.stdout)
            self.assertEqual(len(supplemental["analysis_window"]["checked_days"]), 2)
            self.assertNotIn("progress", supplemental)
            self.assertTrue(supplemental["analysis_window"]["supplemental_pass_used"])
            self.assertIsNone(supplemental["analysis_window"]["next_older_than_day"])

    def test_analysis_surface_passes_source_policy_config_to_supplemental_intake(self) -> None:
        captured: list[dict] = []
        present_payload = {"status": "no-topics", "topic_cards": [], "next_action_options": {"options": []}}

        with tempfile.TemporaryDirectory(prefix="mci-analysis-supplemental-config-") as temp_dir:
            temp_path = Path(temp_dir)
            config_path = temp_path / "configured analysis.json"
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "supplemental-historical-window"},
                            "source": {"daily_shards_considered": ["2026-05-17.md"], "source_classes_present": ["trace_evidence"]},
                            "source_policy": {"effective_source_classes": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout="{}", stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout="{}", stderr=""),
                        present_payload,
                    ),
                ]

                self.assertEqual(
                    analysis_surface.main(
                        ["--arguments", "", "--config", str(config_path), "--older-than-day", "2026-05-18"]
                    ),
                    0,
                )

        intake_command = mock_run.call_args_list[0].args[0]
        self.assertIn("--config", intake_command)
        self.assertIn(str(config_path), intake_command)

    def test_analysis_surface_runs_one_internal_supplemental_window(self) -> None:
        captured: list[dict] = []
        present_payload = {"status": "no-topics", "topic_cards": [], "next_action_options": {"options": []}}

        with tempfile.TemporaryDirectory(prefix="mci-analysis-supplemental-") as temp_dir:
            temp_path = Path(temp_dir)
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "supplemental-historical-window"},
                            "source": {
                                "daily_shards_considered": ["2026-05-17.md", "2026-05-16.md"],
                                "source_classes_present": ["trace_evidence"],
                            },
                            "source_policy": {"effective_source_classes": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout="{}", stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout="{}", stderr=""),
                        present_payload,
                    ),
                ]

                self.assertEqual(
                    analysis_surface.main(["--arguments", "", "--older-than-day", "2026-05-18"]),
                    0,
                )

        self.assertEqual(mock_run.call_count, 3)
        intake_command = mock_run.call_args_list[0].args[0]
        self.assertIn("--older-than-day", intake_command)
        self.assertIn("2026-05-18", intake_command)
        self.assertEqual(
            captured[0]["analysis_window"],
            {
                "mode": "supplemental-historical-window",
                "checked_days": ["2026-05-17", "2026-05-16"],
                "next_older_than_day": None,
                "supplemental_pass_used": True,
                "exclusive_boundary_day": "2026-05-18",
                "supplemental_intake_status": "available",
                "supplemental_pass_attempted": True,
            },
        )

    def test_analysis_surface_preserves_window_metadata_when_supplemental_signals_fail(self) -> None:
        captured: list[dict] = []

        with tempfile.TemporaryDirectory(prefix="mci-analysis-supplemental-signals-fail-") as temp_dir:
            temp_path = Path(temp_dir)
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "supplemental-historical-window"},
                            "source": {"daily_shards_considered": ["2026-05-17.md"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=1, stdout="", stderr="signals failed"),
                        None,
                    ),
                ]

                self.assertEqual(
                    analysis_surface.main(["--arguments", "", "--older-than-day", "2026-05-18"]),
                    0,
                )

        window = captured[0]["analysis_window"]
        self.assertEqual(window["exclusive_boundary_day"], "2026-05-18")
        self.assertEqual(window["checked_days"], ["2026-05-17"])
        self.assertTrue(window["supplemental_pass_attempted"])

    def test_analysis_surface_preserves_supplemental_intake_unavailability_and_window(self) -> None:
        captured: list[dict] = []
        unavailable_reason = "Supplemental historical search is unavailable under configured narrow scope."

        with tempfile.TemporaryDirectory(prefix="mci-analysis-supplemental-unavailable-") as temp_dir:
            temp_path = Path(temp_dir)
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.return_value = (
                    subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                    {
                        "status": "unavailable",
                        "reason": unavailable_reason,
                        "scope": {"basis": None},
                        "source": {"daily_shards_considered": []},
                    },
                )

                self.assertEqual(
                    analysis_surface.main(["--older-than-day", "2026-05-18"]),
                    0,
                )

        self.assertEqual(mock_run.call_count, 1)
        payload = captured[0]
        self.assertEqual(payload["status"], "blocked")
        self.assertEqual(payload["reason"], unavailable_reason)
        self.assertEqual(payload["intake_status"], "unavailable")
        self.assertTrue(payload["analysis_window"]["supplemental_pass_attempted"])
        self.assertFalse(payload["analysis_window"]["supplemental_pass_used"])
        self.assertEqual(
            payload["analysis_window"],
            {
                "mode": "supplemental-historical-window",
                "checked_days": [],
                "next_older_than_day": None,
                "supplemental_pass_used": False,
                "exclusive_boundary_day": "2026-05-18",
                "supplemental_intake_status": "unavailable",
                "supplemental_pass_attempted": True,
            },
        )

    def test_analysis_surface_reports_narrow_scope_rejection_as_not_attempted_supplemental_window(self) -> None:
        captured: list[dict] = []
        with patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
            analysis_surface,
            "emit",
            side_effect=captured.append,
        ):
            self.assertEqual(
                analysis_surface.main(
                    ["--arguments", "day=2026-05-20", "--older-than-day", "2026-05-18"]
                ),
                0,
            )

        mock_run.assert_not_called()
        window = captured[0]["analysis_window"]
        self.assertEqual(window["exclusive_boundary_day"], "2026-05-18")
        self.assertFalse(window["supplemental_pass_attempted"])
        self.assertEqual(window["supplemental_intake_status"], None)

    def test_analysis_surface_does_not_widen_an_explicitly_narrowed_request(self) -> None:
        captured: list[dict] = []
        with patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
            analysis_surface,
            "emit",
            side_effect=captured.append,
        ):
            self.assertEqual(
                analysis_surface.main(
                    [
                        "--arguments",
                        "day=2026-05-20",
                        "--older-than-day",
                        "2026-05-18",
                    ]
                ),
                0,
            )

        mock_run.assert_not_called()
        self.assertEqual(captured[0]["status"], "blocked")
        self.assertIn("cannot widen", captured[0]["reason"].lower())

    def test_analysis_surface_uses_native_first_present_mode_and_infers_thai_from_recent_user_text(self) -> None:
        captured: list[dict] = []
        present_payload = {
            "status": "available",
            "topic_cards": [
                {
                    "id": "topic-001",
                    "title": "Topic title",
                    "recommended_first": True,
                    "status_line": "candidate only; advisory only; not approved yet",
                    "confidence": "low",
                    "evidence_summary": "historical-only, trace_evidence, 1 trace record(s) across 1 session(s) and 1 shard(s)",
                    "sections": [{"label": "มันคืออะไร", "value": "Example"}],
                }
            ],
            "next_action_options": {
                "heading": "Next action options",
                "status_line": "advisory only; no topic selected yet",
                "options": [],
            },
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-surface-thai-language-") as temp_dir:
            temp_path = Path(temp_dir)
            transcript_path = temp_path / "session-123.jsonl"
            transcript_path.write_text(
                "\n".join(
                    [
                        '{"type":"user","timestamp":"2026-05-31T00:00:00Z","message":{"role":"user","content":"ขอคำสั่ง goal ในการดำเนินการอัพเดท"}}',
                        '{"type":"user","timestamp":"2026-05-31T00:01:00Z","message":{"role":"user","content":"จากการทดสอบล่าสุด ฉันพบว่า การอธบิายแบบรายละเอียดเข้าใจง่าย แบบของเดิมหายไป"}}',
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ), patch.dict(
                analysis_surface.os.environ,
                {"CLAUDE_CODE_TRANSCRIPT_PATH": str(transcript_path)},
                clear=False,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default", "day_shard": "2026-05-31", "same_day_widened": False},
                            "source": {"retrieval_mode": "raw-day-shard-scope", "source_classes_present": ["trace_evidence"]},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        {"status": "available"},
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout='{"status": "available"}', stderr=""),
                        present_payload,
                    ),
                ]

                exit_code = analysis_surface.main([
                    "--session-id",
                    "session-123",
                    "--current-day",
                    "2026-05-31",
                ])

        self.assertEqual(exit_code, 0)
        payload = captured[0]
        self.assertEqual(payload["status"], "available")
        present_command = mock_run.call_args_list[2].args[0]
        self.assertEqual(present_command[:3], ["bash", str(analysis_surface.RUNTIME_BIN), "present"])
        self.assertIn("native-first", present_command)
        self.assertIn("--language", present_command)
        self.assertIn("th", present_command)

    def test_analysis_surface_projects_bounded_trace_discovery_evidence(self) -> None:
        captured: list[dict] = []
        present_payload = {"status": "available", "topic_cards": [], "next_action_options": {"options": []}}
        signal_payload = {
            "status": "available",
            "ranked_signals": [
                {
                    "id": "signal-001",
                    "records": [
                        {
                            "shard": "2026-05-20.md",
                            "section": "09:14",
                            "session_id": "session-123",
                            "source_classes": ["trace_evidence"],
                            "content_preview": "A trace-backed workflow friction excerpt.",
                            "transcript": "/private/transcript.jsonl",
                        },
                        {
                            "shard": "2026-05-20.md",
                            "section": "09:15",
                            "session_id": "session-123",
                            "source_classes": ["durable_memory_context"],
                            "content_preview": "Context-only content is not a trace discovery excerpt.",
                        },
                    ],
                }
            ],
        }

        with tempfile.TemporaryDirectory(prefix="mci-analysis-discovery-evidence-") as temp_dir:
            temp_path = Path(temp_dir)
            with patch.object(
                analysis_surface,
                "find_memory_root",
                return_value=temp_path / ".memsearch" / "memory",
            ), patch.object(analysis_surface, "run_json_command") as mock_run, patch.object(
                analysis_surface,
                "emit",
                side_effect=captured.append,
            ), patch.object(
                analysis_surface.tempfile,
                "mkdtemp",
                return_value=temp_dir,
            ), patch.object(
                analysis_surface.Path,
                "cwd",
                return_value=temp_path,
            ):
                mock_run.side_effect = [
                    (
                        subprocess.CompletedProcess(args=["intake"], returncode=0, stdout="{}", stderr=""),
                        {
                            "status": "available",
                            "scope": {"basis": "historical-default"},
                            "source": {
                                "daily_shards_considered": ["2026-05-20.md"],
                                "source_classes_present": ["trace_evidence"],
                            },
                            "source_policy": {"effective_source_classes": ["trace_evidence"]},
                            "records": [
                                {"ref": "excerpt-001", "source_classes": ["trace_evidence"], "content": "Canonical intake workflow evidence is longer than the display preview.", "content_truncated": False},
                                {"source_classes": ["durable_memory_context"], "content": "Supporting context only."},
                            ],
                            "limits": {"max_chars": 6000},
                        },
                    ),
                    (
                        subprocess.CompletedProcess(args=["signals"], returncode=0, stdout="{}", stderr=""),
                        signal_payload,
                    ),
                    (
                        subprocess.CompletedProcess(args=["present"], returncode=0, stdout="{}", stderr=""),
                        present_payload,
                    ),
                ]

                self.assertEqual(analysis_surface.main([]), 0)

        self.assertEqual(
            captured[0]["topic_discovery_evidence"],
            [
                {
                    "ref": "excerpt-001",
                    "content": "Canonical intake workflow evidence is longer than the display preview.",
                    "content_truncated": False,
                }
            ],
        )

    def test_topic_discovery_evidence_preserves_mechanism_beyond_display_preview(self) -> None:
        marker = "Observed cross-account identity reuse caused unauthorized disclosure."
        content = "Background description. " * 14 + marker
        records = [
            {"ref": "excerpt-001", "source_classes": ["trace_evidence"], "content": content, "content_truncated": False, "transcript": "/private/fixture.jsonl", "session_id": "private-session"},
            {"ref": "excerpt-002", "source_classes": ["governance_context"], "content": "Context is not occurrence proof."},
        ]
        excerpts = analysis_surface.topic_discovery_evidence({"records": records, "limits": {"max_chars": 6000}})
        self.assertEqual(excerpts, [{"ref": "excerpt-001", "content": content, "content_truncated": False}])
        self.assertIn(marker, excerpts[0]["content"])
        self.assertNotIn("private-session", str(excerpts))
        self.assertNotIn("/private/", str(excerpts))

    def test_topic_discovery_evidence_does_not_restore_missing_content_from_previews(self) -> None:
        intake_payload = {"records": [{"ref": "excerpt-001", "source_classes": ["trace_evidence"], "content_preview": "This display preview is not canonical evidence."}], "limits": {"max_chars": 6000}}
        self.assertEqual(analysis_surface.topic_discovery_evidence(intake_payload), [])
        self.assertEqual(analysis_surface.topic_discovery_evidence({"ranked_signals": [{"records": intake_payload["records"]}]}), [])

    def test_topic_discovery_evidence_retains_intake_truncation_without_inventing_missing_text(self) -> None:
        intake_payload = {"records": [{"ref": "excerpt-001", "source_classes": ["trace_evidence"], "content": "Partial observed event...", "content_truncated": True}], "limits": {"max_chars": 6000}}
        self.assertEqual(analysis_surface.topic_discovery_evidence(intake_payload), [{"ref": "excerpt-001", "content": "Partial observed event...", "content_truncated": True}])

    def test_topic_discovery_evidence_caps_record_count_and_total_intake_budget(self) -> None:
        records = [{"ref": f"excerpt-{index:03d}", "source_classes": ["trace_evidence"], "content": "x" * 240, "content_truncated": False} for index in range(1, 52)]
        excerpts = analysis_surface.topic_discovery_evidence({"records": records, "limits": {"max_chars": 20000}})
        self.assertEqual(len(excerpts), 50)
        self.assertTrue(all(len(item["content"]) == 240 for item in excerpts))
        bounded = analysis_surface.topic_discovery_evidence({"records": records, "limits": {"max_chars": 256}})
        self.assertLessEqual(sum(len(item["content"]) for item in bounded), 256)
        self.assertTrue(bounded[-1]["content_truncated"])

    def test_topic_discovery_preserves_distinct_thai_evidence_without_a_title_catalog(self) -> None:
        texts = ["ผู้ช่วยนำข้อมูลบัญชีหนึ่งไปแสดงให้อีกบัญชีโดยไม่ได้รับอนุญาต", "ผู้ช่วยถือว่าศูนย์แปลว่าไม่มีข้อมูลจึงเปลี่ยนค่าที่ทราบแล้วเป็นค่าไม่ทราบ"]
        records = [{"ref": f"excerpt-{index:03d}", "source_classes": ["trace_evidence"], "content": text, "content_truncated": False} for index, text in enumerate(texts, 1)]
        excerpts = analysis_surface.topic_discovery_evidence({"records": records, "limits": {"max_chars": 6000}})
        self.assertEqual([item["content"] for item in excerpts], texts)
        self.assertTrue(all("title" not in item and "rank" not in item for item in excerpts))


class ProgressiveWrapperTests(unittest.TestCase):
    def test_catch_up_acknowledges_each_batch_and_freezes_endpoint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            memory = project / ".memsearch" / "memory"
            memory.mkdir(parents=True)
            home = project / "home"
            home.mkdir()
            env = dict(os.environ, HOME=str(home), ARGUMENTS="", PYTHONDONTWRITEBYTECODE="1")
            state = home / ".claude" / "memory-context-intelligence" / "progress.json"
            for day in range(1, 31):
                (memory / f"2026-01-{day:02d}.md").write_text(f"### 10:00\n- evidence day {day}\n")

            def run(*arguments):
                result = subprocess.run(
                    ["bash", str(PACKAGE_ROOT / "bin" / "memory-context-intelligence"), *arguments],
                    cwd=project, env=env, capture_output=True, text=True, timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
                return json.loads(result.stdout)

            first = run("analysis-surface", "--mode", "catch-up", "--max-records", "10")
            self.assertEqual(first["analysis_window"]["checked_days"], [f"2026-01-{day:02d}" for day in range(1, 11)])
            self.assertEqual(first["progress"]["expected_version"], 0)
            self.assertIsNone(next(iter(json.loads(state.read_text())["scopes"].values()))["position"])
            run("complete", "--batch-id", first["progress"]["batch_id"], "--outcome", "no-topics")
            with (memory / "2026-01-01.md").open("a") as handle:
                handle.write("- late append to old day\n")
            (memory / "2026-01-31.md").write_text("### 10:00\n- after invocation endpoint\n")
            for start in [11, 21]:
                batch = run("analysis-surface", "--continue-run", first["progress"]["run_id"], "--max-records", "10")
                self.assertEqual(batch["analysis_window"]["checked_days"], [f"2026-01-{day:02d}" for day in range(start, start + 10)])
                run("complete", "--batch-id", batch["progress"]["batch_id"], "--outcome", "analyzed")
            caught_up = run("analysis-surface", "--continue-run", first["progress"]["run_id"])
            self.assertEqual(caught_up["status"], "caught-up")
            fresh = run("analysis-surface")
            self.assertEqual([e["content"] for e in fresh["topic_discovery_evidence"]], ["late append to old day", "after invocation endpoint"])

    def test_startup_is_fileless_before_caller_binds_slash_arguments(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            memory = project / ".memsearch/memory"
            memory.mkdir(parents=True)
            (memory / "2026-01-01.md").write_text("### 10:00\n- startup must not consume this\n")
            home = project / "home"
            home.mkdir()
            result = subprocess.run(
                ["bash", str(PACKAGE_ROOT / "bin/memory-context-intelligence"), "analysis-surface", "--startup"],
                cwd=project, env=dict(os.environ, HOME=str(home), PYTHONDONTWRITEBYTECODE="1"),
                capture_output=True, text=True, timeout=20,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["status"], "awaiting-caller-scope")
            self.assertTrue(payload["analysis_request_present"])
            self.assertFalse((home / ".claude/memory-context-intelligence").exists())
            self.assertNotIn("topic_discovery_evidence", payload)

    def test_source_rewrite_after_preparation_cannot_be_completed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            memory = project / ".memsearch" / "memory"
            memory.mkdir(parents=True)
            shard = memory / "2026-01-01.md"
            shard.write_text("### 10:00\n- checked original evidence\n")
            home = project / "home"
            home.mkdir()
            env = dict(os.environ, HOME=str(home), ARGUMENTS="", PYTHONDONTWRITEBYTECODE="1")
            command = ["bash", str(PACKAGE_ROOT / "bin" / "memory-context-intelligence")]
            prepared = subprocess.run(command + ["analysis-surface"], cwd=project, env=env, capture_output=True, text=True, timeout=30)
            self.assertEqual(prepared.returncode, 0, prepared.stderr)
            batch_id = json.loads(prepared.stdout)["progress"]["batch_id"]
            shard.write_text("### 10:00\n- different replacement evidence\n")
            result = subprocess.run(command + ["complete", "--batch-id", batch_id, "--outcome", "analyzed"], cwd=project, env=env, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertIn("source-changed", json.loads(result.stdout)["reason"])
            entry = next(iter(json.loads((home / ".claude/memory-context-intelligence/progress.json").read_text())["scopes"].values()))
            self.assertEqual(entry["version"], 0)
            self.assertIsNone(entry["position"])

    def test_explicit_inspection_never_creates_progress(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            memory = project / ".memsearch" / "memory"
            memory.mkdir(parents=True)
            (memory / "2026-01-01.md").write_text("### 10:00\n- explicit inspection\n")
            home = project / "home"
            home.mkdir()
            result = subprocess.run(
                ["bash", str(PACKAGE_ROOT / "bin" / "memory-context-intelligence"), "analysis-surface", "--arguments", "day=2026-01-01"],
                cwd=project, env=dict(os.environ, HOME=str(home), PYTHONDONTWRITEBYTECODE="1"),
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn("progress", json.loads(result.stdout))
            self.assertFalse((home / ".claude" / "memory-context-intelligence" / "progress.json").exists())


if __name__ == "__main__":
    unittest.main()
