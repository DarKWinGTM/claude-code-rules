from __future__ import annotations

import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ANALYSIS = PACKAGE_ROOT / "skills" / "analysis" / "SKILL.md"
RUNTIME_OLD = PACKAGE_ROOT / "skills" / "memory-context-intelligence" / "SKILL.md"
SOURCE_ROOT = (
    PACKAGE_ROOT
    if "TEMPLATE/RULES/plugin/memory-context-intelligence" in str(PACKAGE_ROOT)
    else PACKAGE_ROOT.parents[1] / "RULES" / "plugin" / "memory-context-intelligence"
)
SOURCE_ANALYSIS = SOURCE_ROOT / "skills" / "analysis" / "SKILL.md"
SOURCE_OLD = SOURCE_ROOT / "skills" / "memory-context-intelligence" / "SKILL.md"


class AnalysisSkillContractTests(unittest.TestCase):
    def test_analysis_skill_exists_and_old_self_named_skill_is_gone(self) -> None:
        self.assertTrue(RUNTIME_ANALYSIS.exists())
        self.assertFalse(RUNTIME_OLD.exists())
        self.assertTrue(SOURCE_ANALYSIS.exists())
        self.assertFalse(SOURCE_OLD.exists())

    def test_analysis_skill_text_matches_public_contract(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("/analysis", text)
        self.assertIn("/memory-context-intelligence:analysis", text)
        self.assertIn("proposal-first format", text)
        self.assertIn("present topic candidates directly as doctrine-level historical work-pattern review topics", text)
        self.assertIn("recommended first topic", text)
        self.assertIn("semantic human-readable titles", text)
        self.assertIn("Topic <n>", text)
        self.assertIn("doctrine-level historical work-pattern review topics", text)
        self.assertIn("same repeated pattern", text)
        self.assertIn("repeated topic cards", text)
        self.assertIn("repeated recap", text)
        self.assertIn("principle or mechanism level", text)
        self.assertIn("incident details such as `404`, `python error`", text)
        self.assertIn("distinct doctrine lenses", text)
        self.assertIn("candidate only", text)
        self.assertIn("advisory only", text)
        self.assertIn("not approved yet", text)
        self.assertIn("do not default to package-map explanation", text)
        self.assertIn("/memory-context-intelligence:review", text)
        self.assertIn("Deferred / non-public command ideas in this wave", text)
        self.assertIn("broader historical analysis did not find a sufficiently repeated pattern to propose yet", text)
        self.assertIn("actionable insufficiency", text)
        self.assertIn("recommended_next_step", text)
        self.assertIn("checked registered analysis slash surface", text)
        self.assertIn("do not present bare `/analysis` as proved current runtime behavior", text)

    def test_analysis_skill_requires_native_first_rewrite_without_manual_rephrase(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("must not require a second manual rewrite pass", text)
        self.assertIn("native-first", text)
        self.assertIn("มันคืออะไร", text)
        self.assertIn("อาการ/ปัญหา", text)
        self.assertIn("Evidence examples", text)
        self.assertIn("Before behavior", text)
        self.assertIn("After behavior", text)
        self.assertIn("compact before/after preview", text)
        self.assertIn("every first-pass topic card", text)
        self.assertIn("expanded follow-up layer", text)
        self.assertIn("long-form illustrative before/after", text)
        self.assertIn("signal.records[].content_preview", text)
        self.assertIn("do not invent generic case examples", text)
        self.assertIn("ถ้าปรับแล้วจะดีขึ้นยังไง", text)
        self.assertIn("หลักฐานที่ใช้", text)
        self.assertIn("สถานะตอนนี้", text)

    def test_analysis_skill_requires_memsearch_backed_flow(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("/memory-context-intelligence:analysis", text)
        self.assertIn("checked registered analysis slash surface", text)
        self.assertIn("permission-mode bypassPermissions", text)
        self.assertIn("plain no-approval print-mode is not used as proof", text)
        self.assertIn("memsearch", text)
        self.assertIn("intake", text)
        self.assertIn("signals", text)
        self.assertIn("present", text)
        self.assertTrue("blocked" in text or "dormant" in text)

    def test_analysis_skill_defaults_to_broader_historical_scope(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("broader historical memory", text)
        self.assertIn("current-session evidence becomes supporting/provenance context", text)
        self.assertIn("historical recurring patterns", text)
        self.assertIn("historical-only", text)
        self.assertIn("current-session-confirmed", text)

    def test_analysis_skill_requires_breadth_first_historical_review_contract(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("multi-session/multi-shard", text)
        self.assertIn("single-session/single-shard", text)
        self.assertIn("historical breadth summary", text)
        self.assertIn("narrow historical", text)

    def test_analysis_skill_uses_permission_safe_runtime_wrapper(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertNotIn("python3 - <<'PY'", text)
        self.assertNotIn("$ARGUMENTS", text)
        self.assertIn("memory-context-intelligence analysis-surface", text)

    def test_analysis_skill_requires_design_grounded_review_and_visible_provenance(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("design-grounded", text)
        self.assertIn("RULES/workflow review", text)
        self.assertIn("provenance", text)
        self.assertIn("historical-only", text)
        self.assertIn("current-session-confirmed", text)

    def test_analysis_skill_requires_repeated_topic_cards_not_report_wrappers(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("Topic <n>", text)
        self.assertIn("same repeated pattern", text)
        self.assertIn("Do not use `Presentation`, `Recommendation`, `Proposal`, and `Related variants` as top-level blocks", text)
        self.assertIn("Do not split one topic across multiple sections", text)

    def test_analysis_skill_adds_compact_next_action_options_bridge(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("Next action options", text)
        self.assertIn("after the topic cards", text)
        self.assertIn("advisory bridge", text)
        self.assertIn("do not treat next-action options as approved execution", text)
        self.assertIn("choose a topic number", text)
        self.assertIn("type a direct request", text)
        self.assertIn("deep thinking / websearch / webfetch", text)

    def test_analysis_skill_treats_standalone_slash_invocation_as_the_request(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("the slash invocation itself is the request", text)
        self.assertIn("do not answer that there is no request", text)
        self.assertIn("render the corresponding `available`, `blocked`, `dormant`, or `no-topics` state instead", text)
        self.assertIn("ignore ambient session progress context", text)

    def test_analysis_skill_describes_temporary_stale_session_diagnostic_without_normalizing_bug(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("possible stale long-lived session", text)
        self.assertIn("temporary diagnostic safeguard", text)
        self.assertIn("restart this session and retry", text)
        self.assertIn("session-dependent no-response remains a bug", text)
        self.assertIn("must not turn restart into the final fix", text)

    def test_analysis_skill_explicitly_blocks_development_summary_leak(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("do not summarize ongoing implementation work", text)
        self.assertIn("ignore ambient session progress context", text)

    def test_analysis_skill_exposes_multi_source_evidence_contract(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("trace_evidence", text)
        self.assertIn("recall_evidence", text)
        self.assertIn("durable_memory_context", text)
        self.assertIn("governance_context", text)
        self.assertIn("source_mix_label", text)
        self.assertIn("source_classes_present", text)
        self.assertIn("source mix", text)
        self.assertIn("durable memory", text)
        self.assertIn("governance context", text)

    def test_analysis_skill_uses_historical_first_no_topics_wording(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("broader historical analysis did not find a sufficiently repeated pattern", text)
        self.assertIn("historical-first", text)
        self.assertIn("do not treat durable memory or governance context alone as enough", text)

    def test_analysis_skill_surfaces_guided_config_helper_when_no_config_is_loaded(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("config_questions", text)
        self.assertIn("guided config helper", text)
        self.assertIn("suggested_config_path", text)
        self.assertIn("when the runtime payload says no config file is loaded", text)

    def test_analysis_skill_describes_adaptive_deep_analysis_behavior(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("adaptive deep-analysis", text)
        self.assertIn("all four internal evidence sources", text)
        self.assertIn("subagent-assisted", text)
        self.assertIn("web/external research", text)
        self.assertIn("before the first response", text)
        self.assertIn("must not be treated as selected or approved", text)
        self.assertIn("supporting layer", text)
        self.assertIn("trace_evidence remains the live promotion anchor", text)

    def test_analysis_skill_requires_bounded_deepening_when_adaptive_plan_flags_it(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("deepening_required", text)
        self.assertIn("required_topic_ids", text)
        self.assertIn("must deepen", text)
        self.assertIn("must say so explicitly", text)
        self.assertIn("do not silently skip", text)


if __name__ == "__main__":
    unittest.main()
