# Phase 075 — Analysis Topic Eligibility

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 075
> **Current Version:** 0.1.83
> **Status:** Source contract, selected local-scope package update, and scoped proof completed; package `0.9.35` remains unpublished
> **Target Design:** [../design/design.md](../design/design.md) v0.1.83
> **Design References:** [Topic List and Choice Flow](../design/02-topic-list-and-choice-flow.design.md), [Memory Evidence Source Model](../design/08-memory-evidence-source-model.design.md)
> **Patch References:** none — bounded existing-skill contract correction without a separate before/after rollback boundary
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Session:** 7194487f-fe8b-4383-8756-3db4c5612392 (2026-10-02)

## Goal and Lineage

Change the existing `/memory-context-intelligence:analysis` first-response contract so it shows only topics supported by their actual trace and not already covered, completed, or semantically duplicated. This is a continuation of the same analysis surface and topic-list owner, but an independent source/document acceptance outcome after completed Phase 074; therefore use the next major phase rather than reopening Phase 074's summary-research/install gate.

The user selected strict suppression: if a trace appears to violate an active rule, suppress the topic when that rule already covers the principle. Do not emit a regression-topic exception. The initial analysis remains read-only and cannot modify RULES or create artifacts.

## Eligibility and Output Contract

Every generated candidate must pass, before deepening or display:

1. **Trace entailment:** inspect source-backed bounded trace text and confirm it supports the specific alleged problem. Signal IDs, keywords, confidence, generated title/before-after, or an evidence count are not proof. Suppress plans, precautions, compliant actions, hypotheticals, mismatched, missing, truncated-at-decision, or otherwise insufficient trace evidence.
2. **Active-rule novelty:** identify the analyzed project's active root and inspect relevant active RULES owners beyond sampled governance context. Suppress any covered or semantically equivalent principle, including a trace that appears to violate it.
3. **Completed-work novelty:** follow active phase/TODO navigation and verify completion status plus matching outcome. Suppress already-delivered behavior; title similarity alone does not establish completion.
4. **Candidate-set deduplication:** retain at most one candidate for a shared principle, behavior, or outcome.
5. **Fail closed:** suppress when the active owner, relevant RULES, completion state, or a possible semantic match cannot be resolved adequately.

The output may contain zero or more eligible topics; never fill to three. Explain whether zero output reflects insufficient evidence, suppression, or an unresolved check without conflating those states or repeating suppressed titles. Adaptive deepening applies only to candidates that pass eligibility.

## Scope and Owners

- Source owner: `skills/analysis/SKILL.md`; behavior/design owner: `design/02-topic-list-and-choice-flow.design.md`.
- Contract tests: `tests/test_analysis_skill_contract.py`; package version test: `tests/test_plugin_manifest.py`.
- Align package manifest and all public skill version metadata to `0.9.35`; align governed design/changelog to `0.1.83`.
- Sync package README, this phase, phase summary, active changelog parent/shard, and root `TODO.md`.
- Preserve all pre-existing dirty files/changes and unrelated projects. No analysis engine, service, command, corpus acquisition, additional-stage path, global RULES change, or Product behavior change.
- The user subsequently selected a local-scope update of the existing `memory-context-intelligence@darkwingtm` identity. Current-session restart/reload, commit, push, tag, publication, and model-effect evaluation remain unselected; Phase 075 is not a full RULES release wave.

## Verification and Exit Gate

- Focused analysis skill contract tests passed24 tests; manifest test passed1; related signals/presentation/orchestration suites passed27/20/6; full MCI package suite passed152. `claude plugin validate` passed before update.
- Selected version alignment, 131 current local Markdown links, scoped trailing-whitespace and `git diff --check` checks passed after status reconciliation.
- Paired fresh-context A–H interpretation passed: novel trace-supported candidate may surface; unsupported, covered, completed, unresolved, and duplicate candidates are suppressed; a covered-rule violation remains suppressed; one eligible candidate may be the only output and rejected IDs are not deepened. This is instruction interpretation only, not generated-model proof.
- Source/document checks, package tests, plugin validation, version/link/history checks, and scoped diff checks passed. The MCI `0.9.35` local update completed; install-time source/cache file path, byte, and mode comparison matched all333 files, and fresh CLI component inventory reported all3 public skills.
- Pre-update exact registry-row recheck did not pass: the assertion detected a registry-entry difference after the recovery snapshot. The shell command did not stop on that failed check and proceeded to the explicitly authorized native update. Do not claim a clean pre-update registry recheck. Post-update registry/list checks confirmed the selected identity, `local` scope, project path, `0.9.35` version, and versioned cache path; selected settings-file hashes matched the pre-update captures.
- Status documents in the source tree were reconciled after installation. Their installed-cache parity is excluded; the install-time parity statement applies to the source snapshot at update time. Restart is required to apply the package to the current session; no current-session reload, generated-model behavior, causal benefit, or publication is claimed.
