# Historical-default analysis scope redesign patch

> **Current Version:** 0.1.57
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-27)
> **Status:** Phase 053 completed historical-default analysis implementation in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.57
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user clarified that `/memory-context-intelligence:analysis` should review broader historical work patterns across sessions by default rather than defaulting to current-session-first narrowing. The implementation wave for intake, signals, presentation, and the public analysis contract was already in progress, but the governed and runtime-facing surfaces still described the older scope model.

## 2) Analysis

The redesign needed one coherent before/after review boundary:
- keep memsearch-backed `trace_evidence` as the live promotion anchor
- widen the default scope to bounded broader historical memory
- keep explicit narrow-slice controls available for `day`, `session`, and `lookback`
- re-rank promotion so historical repetition, cross-session breadth, and recency matter before current-session confirmation
- preserve current-session evidence as supporting provenance only
- sync source-authority and runtime-facing docs so the active contract no longer drifts from the implemented behavior

## 3) Change items

### 3.1 Source-authority design sync
- **Target artifact:** `../design/design.md`, `../design/00-core-concept.design.md`, `../design/01-memsearch-required-dependency.design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../design/07-recall-scoping-and-time-window.design.md`, `../design/08-memory-evidence-source-model.design.md`
- **Change type:** replacement
- **Before:** active design still described current-session-first default scope and current-session-centered promotion language
- **After:** active design now describes historical-default scope, trace-anchored but historical-first promotion, explicit narrow-slice controls, and provenance labels for `historical-only` versus `confirmed-in-current-session`

### 3.2 Governed execution/history sync
- **Target artifact:** `../README.md`, `../phase/SUMMARY.md`, `../phase/phase-053-historical-default-analysis-implementation.md`, `../changelog/changelog.md`, `../changelog/v0.1.57-completed-historical-default-analysis-implementation.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement/additive
- **Before:** top-level governed surfaces still pointed at phase 052 no-bug clarification as the latest wave
- **After:** governed surfaces now record phase 053 as the completed historical-default implementation wave

### 3.3 Runtime-facing projection sync
- **Target artifact:** `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/README.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/design/design.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/phase/SUMMARY.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/changelog/changelog.md`
- **Change type:** replacement
- **Before:** runtime-facing projection docs still described current-session-first default scope
- **After:** runtime-facing projection docs now describe the historical-default scope and provenance model that matches the implemented runtime behavior

## 4) Verification

- focused runtime intake/signals/presentation/analysis-contract tests should pass
- mirrored focused source-authority tests should pass
- one real local `intake -> signals -> present` run should prove historical-default behavior
- doc/version/phase/TODO/changelog surfaces should agree on phase 053 as the latest completed wave

## 5) Rollback approach

If this wave is rolled back, restore the earlier current-session-first governed/runtime-facing wording together with the corresponding implementation behavior. Do not mutate `/additional/`, install state, or main RULES as part of this patch rollback unless the user explicitly authorizes broader rollback scope.
