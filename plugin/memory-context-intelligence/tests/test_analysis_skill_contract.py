from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ANALYSIS = PACKAGE_ROOT / "skills" / "analysis" / "SKILL.md"
RUNTIME_OLD = PACKAGE_ROOT / "skills" / "memory-context-intelligence" / "SKILL.md"


def _resolve_source_root() -> Path:
    candidates = [PACKAGE_ROOT]
    candidates.extend(parent / "plugin" / "memory-context-intelligence" for parent in PACKAGE_ROOT.parents)
    candidates.extend(
        parent / "RULES" / "plugin" / "memory-context-intelligence" for parent in PACKAGE_ROOT.parents
    )
    for candidate in candidates:
        if (candidate / "skills" / "analysis" / "SKILL.md").exists():
            return candidate
    return PACKAGE_ROOT


SOURCE_ROOT = _resolve_source_root()
SOURCE_ANALYSIS = SOURCE_ROOT / "skills" / "analysis" / "SKILL.md"
SOURCE_OLD = SOURCE_ROOT / "skills" / "memory-context-intelligence" / "SKILL.md"


class AnalysisSkillContractTests(unittest.TestCase):
    def test_checkpoint_completion_is_caller_attested_not_startup_injection(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("progress.completion_command", text)
        self.assertIn("no-topics", text)
        self.assertIn("mode=catch-up", text)
        self.assertIn("progress.continuation_command", text)
        self.assertIn("Never acknowledge an unread, incomplete, failed or interrupted batch", text)
        executable = re.findall(r"```!\n(.*?)```", text, re.S)
        self.assertEqual(len(executable), 1)
        self.assertNotIn("complete --batch-id", executable[0])

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
        self.assertIn("present only candidates that pass as doctrine-level historical work-pattern review topics", text)
        self.assertIn("recommended first topic", text)
        self.assertIn("semantic human-readable titles", text)
        self.assertIn("Topic <n>", text)
        self.assertIn("doctrine-level historical work-pattern review topics", text)
        self.assertIn("Render zero or more eligible topics", text)
        self.assertIn("Never add filler topics to reach a target count", text)
        self.assertNotIn("sparse historical runs may still surface at least 3 advisory topics", text)
        self.assertIn("same repeated pattern", text)
        self.assertIn("repeated topic cards", text)
        self.assertIn("repeated recap", text)
        self.assertIn("principle or mechanism level", text)
        self.assertIn("incident details such as `404`, `python error`", text)
        self.assertIn("candidate only", text)
        self.assertIn("advisory only", text)
        self.assertIn("not approved yet", text)
        self.assertIn("do not default to package-map explanation", text)
        self.assertIn("/memory-context-intelligence:review", text)
        self.assertIn("Deferred / non-public command ideas in this wave", text)
        self.assertIn("every generated candidate is rejected by the eligibility gate", text)
        self.assertIn("one short actionable next step", text)
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
        executable = re.findall(r"^```!\s*\n(.*?)^```\s*$", text, re.MULTILINE | re.DOTALL)
        self.assertNotIn("$ARGUMENTS", "\n".join(executable))
        self.assertIn("User arguments: $ARGUMENTS", text)
        self.assertIn('"${CLAUDE_PLUGIN_ROOT}/bin/memory-context-intelligence" analysis-surface', text)

    def test_analysis_skill_interprets_natural_language_before_preparing_evidence(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("## Interpret the user request before preparation", text)
        interpretation = text.split("## Interpret the user request before preparation", 1)[1].split("## Default first response contract", 1)[0]
        for contract in [
            "natural-language instructions to Claude, not a retrieval filter",
            "desired topic count, language, detail and analysis depth",
            "only the interpreted retrieval controls",
            'pass `--arguments ""`',
            "Minimium Rules 5 topic",
            "preserve explicit day/session/lookback, literal text filters, config and mode",
            "unsupported or materially ambiguous retrieval constraint",
            "A requested minimum is a target, not permission",
            "--arguments 'session=run-42 timeout'",
            '--arguments "" --mode catch-up',
        ]:
            with self.subTest(contract=contract):
                self.assertIn(contract, interpretation)
        self.assertNotIn("--arguments` containing the user arguments above", text)

    def test_analysis_skill_preprocessing_runs_only_initial_analysis(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        commands = re.findall(r"^```!\s*\n(.*?)^```\s*$", text, re.MULTILINE | re.DOTALL)
        self.assertEqual(
            [command.strip() for command in commands],
            ['"${CLAUDE_PLUGIN_ROOT}/bin/memory-context-intelligence" analysis-surface --startup'],
        )

        with tempfile.TemporaryDirectory(prefix="mci-skill-startup-") as temp_dir:
            cwd = Path(temp_dir)
            if any((base / ".memsearch" / "memory").is_dir() for base in [cwd, *cwd.parents]):
                self.skipTest("Startup smoke requires a temporary root without ambient memsearch input.")
            result = subprocess.run(
                ["bash", "-c", commands[0]],
                cwd=cwd,
                env={
                    "PATH": os.environ["PATH"],
                    "HOME": temp_dir,
                    "CLAUDE_PLUGIN_ROOT": str(PACKAGE_ROOT),
                    "ARGUMENTS": "",
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
                capture_output=True,
                text=True,
                timeout=20,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "blocked")
        self.assertEqual(
            payload["reason"],
            "No project-scoped .memsearch/memory root was found from the current working directory upward.",
        )

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
        self.assertIn("distinguish insufficient historical evidence from candidates suppressed", text)
        self.assertIn("broader historical analysis did not find a sufficiently repeated pattern", text)
        self.assertIn("historical-first", text)
        self.assertIn("do not treat durable memory or governance context alone as enough", text)

    def test_analysis_skill_surfaces_guided_config_helper_when_no_config_is_loaded(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("config_questions", text)
        self.assertIn("guided config helper", text)
        self.assertIn("suggested_config_path", text)
        self.assertIn("user-scope default config file", text)
        self.assertNotIn("project default config file", text)
        self.assertIn("when the runtime payload says no config file is loaded", text)
        self.assertIn("/memory-context-intelligence:init", text)
        self.assertIn("~/.claude/memory-context-intelligence.config.json", text)

    def test_analysis_skill_describes_adaptive_deep_analysis_behavior(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("adaptive deep-analysis", text)
        self.assertIn("all four internal evidence sources", text)
        self.assertIn("subagent-assisted", text)
        self.assertIn("web/external research", text)
        self.assertIn("must not be treated as selected or approved", text)
        self.assertIn("supporting layer", text)
        self.assertIn("trace_evidence remains the live promotion anchor", text)
        self.assertIn("one selected topic per artifact", text)
        self.assertIn("split into separate per-topic artifacts", text)

    def test_analysis_skill_requires_bounded_deepening_when_adaptive_plan_flags_it(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("complete the eligibility gate before any adaptive deepening", text)
        self.assertIn("deepen eligible topics only", text)
        self.assertIn("required_topic_ids", text)
        self.assertIn("must say so explicitly", text)
        self.assertIn("do not silently skip", text)

    def test_analysis_skill_keeps_initial_analysis_read_only_and_requires_explicit_follow_up_selection(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")

        self.assertIn("initial analysis remains read-only and advisory", text)
        self.assertIn("explicit later selection", text)
        self.assertIn("selected_for_additional_trial=True", text)
        self.assertIn("main_rules_promotion_approved=False", text)
        self.assertIn("one independent packet and one standalone artifact per selected topic", text)
        self.assertIn("full-set preflight before any write", text)
        self.assertIn("refuse the complete set on any collision", text)
        self.assertIn("no overwrite option", text)
        self.assertIn("do not ask about template, routing, or source/runtime sync", text)
        self.assertIn("does not mutate Main RULES", text)

    def test_analysis_skill_requires_trace_entailment_and_governance_novelty_before_rendering(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        required_contract = (
            "Eligibility gate before presentation",
            "Trace-to-claim entailment",
            "actual bounded trace text",
            "active RULES",
            "completed work",
            "semantically equivalent",
            "suppress the candidate",
            "output may contain zero topics",
        )

        for clause in required_contract:
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_local_semantic_discovery_precedes_generated_seeds_even_without_workers(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        required = (
            "Local semantic discovery before generated seeds",
            "canonical `content`, not the 220-character display preview",
            "before consulting generated titles or ranks",
            "including when parallel workers are unavailable or skipped",
            "not a closed topic catalog",
            "distinct Thai or English mechanisms remain distinct",
            "same mechanism with different wording is one candidate",
            "do not inherit unrelated seed scores, confidence, or recurrence",
            "A deterministic `no-topics` result is not a semantic discovery conclusion",
        )
        for clause in required:
            with self.subTest(clause=clause):
                self.assertIn(clause, text)
        self.assertLess(text.index("Local semantic discovery before generated seeds"), text.index("Parallel viewpoint discovery before the eligibility gate"))
        self.assertLess(text.index("Local semantic discovery before generated seeds"), text.index("Eligibility gate before presentation"))

    def test_supplemental_search_requires_new_semantic_discovery_not_history_reaudit(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("perform local semantic discovery on the new canonical evidence", text)
        self.assertIn("Re-reading Recovery Contract, Scope, or Phase075 history is not fresh discovery", text)
        self.assertIn("selected, read, and sampled days", text)
        self.assertIn("bounded sampling, not all-record coverage", text)
        self.assertIn("before concluding that the requested fresh pass found no eligible topic", text)

    def test_completed_work_is_matched_by_delivered_outcome_not_filter_completion(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("candidate behavior, mechanism, and output", text)
        self.assertIn("same checked proof layer", text)
        self.assertIn("Phase075 completion proves the eligibility infrastructure", text)
        self.assertIn("not that every later candidate was fixed", text)
        self.assertIn("a genuinely distinct residual delta still needs trace support and active-RULES novelty", text)
        self.assertIn("possible material match that cannot be settled remains fail-closed", text)

    def test_analysis_skill_requires_parallel_viewpoint_discovery_before_eligibility_gate(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        required_contract = (
            "Parallel viewpoint discovery before the eligibility gate",
            "Skip any perspective that lacks a distinct trace-supported question",
            "use caller-session subagent tools to launch one independent read-only subagent per useful perspective, concurrently, capped at three",
            "topic_discovery_evidence",
            "run-local excerpt references",
            "Developer/process",
            "Security",
            "Architect",
            "same privacy-minimized set of actual bounded trace excerpts",
            "main session owns fan-in",
            "apply the complete eligibility gate to the combined candidate set",
            "This is candidate discovery, not deepening of already-ranked topics",
            "Team capability is available and enabled",
            "Do not enable Agent Teams or change settings",
        )

        for clause in required_contract:
            with self.subTest(clause=clause):
                self.assertTrue(clause in text, f"missing clause: {clause}")

    def test_analysis_skill_skips_parallel_discovery_without_independent_evidence_or_workers(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        required_contract = (
            "skip parallel discovery when only one meaningful evidence axis remains",
            "If the caller cannot keep discovery workers within the excerpt-only boundary, skip parallel discovery",
            "If parallel subagents are unavailable, continue with the bounded local candidates",
            "Worker output is evidence input, not authority",
            "Brief workers to use only the supplied excerpts",
            "Workers must not invoke file, shell, memsearch, web-research, or write tools during discovery",
            "If a worker needs more evidence or the supplied excerpt cannot support a claim, return zero candidates",
            "Do not give workers ambient corpus access, ask them to widen or repeat the selected window, or provide full transcripts",
            "The projection is bounded but is not automatically redacted: remove personal data, credentials, private paths/hosts/endpoints, and unrelated payload details before dispatch",
            "The projection is bounded but is not automatically redacted",
            "If sensitive details cannot be removed without losing the trace claim's meaning, omit that excerpt from the worker packet",
            "Each worker may return zero candidates",
            "before any deepening or presentation",
            "Suppress unsupported, covered, completed, duplicate, or materially unresolved candidates",
        )
        for clause in required_contract:
            with self.subTest(clause=clause):
                self.assertTrue(clause in text, f"missing clause: {clause}")

    def test_analysis_skill_allows_one_explicit_fresh_search_after_suppressing_old_candidates(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("explicitly asks for additional or different topics", text)
        self.assertIn("one bounded supplemental historical scan", text)
        self.assertIn("analysis_window.next_older_than_day", text)
        self.assertIn('analysis-surface --arguments "" --older-than-day', text)
        self.assertIn("--config", text)
        self.assertIn("exclusive_boundary_day", text)
        self.assertIn("supplemental_intake_status", text)
        self.assertIn("supplemental_pass_attempted", text)
        self.assertIn("strictly older than every day in the first checked window", text)
        self.assertIn("new candidate set", text)
        self.assertIn("Compare against every candidate already examined", text)
        self.assertIn("not to rescue or strengthen any previously rejected candidate", text)
        self.assertIn("supplemental_pass_used", text)
        self.assertIn("supplemental_pass_attempted", text)
        self.assertIn("without a material scope/access/policy change", text)
        self.assertIn("bounded window", text)
        self.assertIn("does not show that no topic exists in the rest of history", text)

    def test_analysis_skill_suppresses_covered_completed_and_unverifiable_topics(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("If the active owner already covers the principle, suppress the candidate", text)
        self.assertIn("If the same behavior or outcome is already recorded as delivered, suppress it", text)
        self.assertIn("A trace that appears to violate an existing rule is still suppressed", text)
        self.assertIn("relevant active RULES or completion state cannot be checked", text)
        self.assertIn("Candidate-set deduplication", text)

    def test_analysis_skill_checks_topic_eligibility_before_adaptive_deepening(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("complete the eligibility gate before any adaptive deepening", text)
        self.assertIn("deepen eligible topics only", text)
        self.assertIn("ignore `required_topic_ids` for candidates rejected by the eligibility gate", text)

    def test_analysis_skill_allows_zero_to_many_topics_and_does_not_fill_sparse_results(self) -> None:
        text = RUNTIME_ANALYSIS.read_text(encoding="utf-8")
        self.assertIn("Render zero or more eligible topics", text)
        self.assertIn("Never add filler topics to reach a target count", text)
        self.assertNotIn("sparse historical runs may still surface at least 3 advisory topics", text)

    def test_topic_design_defines_novelty_and_trace_eligibility(self) -> None:
        design = (PACKAGE_ROOT / "design" / "02-topic-list-and-choice-flow.design.md").read_text(encoding="utf-8")
        self.assertIn("Trace-to-claim entailment", design)
        self.assertIn("Active RULES novelty", design)
        self.assertIn("Completed-work novelty", design)
        self.assertIn("Fail closed", design)
        self.assertIn("zero or more eligible topics", design)
        self.assertNotIn("at least 3 advisory topics", design)


if __name__ == "__main__":
    unittest.main()
