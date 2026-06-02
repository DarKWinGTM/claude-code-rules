from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
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


if __name__ == "__main__":
    unittest.main()
