# Historical breadth and ordering correction patch

> **Current Version:** 0.1.60
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-28)
> **Status:** Phase 056 completed historical breadth and ordering correction in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.60
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user reported that the latest `/memory-context-intelligence:analysis` result felt too sparse and not orderly enough for the plugin purpose of broader historical work-pattern analysis across sessions.

The diagnosis showed that the main issue was a combination of weak promotion semantics plus presentation compression: narrow historical-only patterns could still promote as if they were broad review, and the first response hid the broader historical map behind a single proposal surface.

## 2) Analysis

The correction wave needed one coherent before/after review boundary:
- keep the historical-default broader-memory model
- keep `trace_evidence` as the promotion anchor
- stop narrow historical-only `2 trace / 1 session / 1 shard` shapes from reading like strong broader review
- prioritize broader multi-session/multi-shard history more clearly
- expose a compact historical breadth summary before the proposal block
- keep the public skill contract and governed docs synchronized to the corrected behavior

## 3) Change items

### 3.1 Signals breadth semantics
- **Target artifact:** `../lib/signals.py`, `../tests/test_signals.py`
- **Change type:** replacement
- **Before:** a narrow historical-only `2 trace / 1 session / 1 shard` pattern could still reach `medium` confidence and promote into the main topic list
- **After:** that narrow historical-only shape stays below the broader-review bar, while broader multi-session/multi-shard history remains promotable as the stronger candidate

### 3.2 Presentation ordering and breadth summary
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** replacement/additive
- **Before:** the first response collapsed directly into the topic/proposal surface without a compact historical breadth summary
- **After:** `presentation` now includes a compact `historical_breadth_summary` before the proposal block and no-topics wording explicitly names a strongest remaining narrow historical-only signal when relevant

### 3.3 Skill/runtime-facing contract sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-056-historical-breadth-and-ordering-correction.md`, `../changelog/changelog.md`, `../changelog/v0.1.60-completed-historical-breadth-and-ordering-correction.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and this patch
- **Change type:** replacement/additive
- **Before:** docs still matched the earlier broader-historical + proposal-first contract but did not yet require breadth-first ordering or narrow-historical demotion
- **After:** the public contract and governed docs now describe the breadth-first behavior explicitly

## 4) Verification

- focused signals tests must fail first, then pass after the fix
- focused presentation tests must fail first, then pass after the fix
- focused analysis skill contract tests must fail first, then pass after the sync
- one transcript-visible local run should show the updated breadth-first analysis behavior in checked scope after the updated local install

## 5) Rollback approach

If this correction wave is rolled back, restore the previous historical promotion/output behavior only if the user explicitly wants that contract back. Do not weaken the single-source installability model from phase 055 and do not mutate `/additional/` unless a broader rollback is explicitly selected.
