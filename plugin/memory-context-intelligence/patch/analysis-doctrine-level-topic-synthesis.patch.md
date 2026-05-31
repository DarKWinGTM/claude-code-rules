# Doctrine-level analysis topic synthesis patch

> **Current Version:** 0.1.62
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-29)
> **Status:** Phase 058 completed doctrine-level analysis topic synthesis in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.62
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Historical-first scope, breadth ordering, minimum-three advisory behavior, and the permission-safe analysis wrapper were already in place, but real local output still surfaced some fallback topics with wording that stayed too close to raw recurring-pattern summaries or narrow keyword suffixes.

## 2) Analysis

The remaining mismatch was no longer about whether analysis could find topics. It was about the abstraction layer of the surfaced topic title.

The patch therefore keeps the existing trace-anchored evidence model and sparse-history advisory behavior, but changes the synthesis path so:
- raw trace evidence stays the source anchor
- doctrine/mechanism lenses decide the top-level title
- incident details remain inside proposal evidence/examples rather than being promoted into the title

## 3) Change items

### 3.1 Signals doctrine lift
- **Target artifact:** `../lib/signals.py`, `../tests/test_signals.py`
- **Change type:** replacement
- **Before:** some config-investigation and recurring-pattern fallback topics could still surface narrow issue wording or raw keyword suffixes such as `404` / `private` / `task`
- **After:** signal-to-topic synthesis now lifts those traces into doctrine-level titles while preserving incident detail in evidence/example text

### 3.2 Proposal evidence/example retention
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** replacement
- **Before:** proposal output relied mainly on generic default examples unless a fixture supplied richer evidence wording manually
- **After:** proposal sections now consume doctrine-aware example/evidence fields from signal-derived topics so case-level details remain visible in the body without escaping into the title

### 3.3 Contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-058-doctrine-level-analysis-topic-synthesis.md`, `../changelog/changelog.md`, `../changelog/v0.1.62-completed-doctrine-level-analysis-topic-synthesis.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, `../.claude-plugin/plugin.json`, and this patch
- **Change type:** replacement/additive
- **Before:** active docs still stopped at semantic-human-readable wording and did not fully state that titles must stay doctrine-level while incident details remain in proposal evidence/examples
- **After:** active contract/governed surfaces now describe doctrine-level topic synthesis explicitly and record the completed wave under `0.1.62` / `0.9.17`

## 4) Verification

- focused RED/GREEN proof for doctrine-level config-investigation titles
- focused RED/GREEN proof for recurring-pattern fallback doctrine lift away from raw keyword suffixes
- focused presentation proof for incident-details-in-proposal behavior
- full runtime/source suite green
- one real local `/memory-context-intelligence:analysis` run with doctrine-level advisory topics plus provenance/confidence boundaries

## 5) Rollback approach

If this refinement is rolled back, restore the earlier topic-synthesis wording only if the user explicitly wants the pre-doctrine lift behavior back. Do not weaken the trace-anchored evidence model, do not remove sparse-history advisory coverage, and do not mutate `/additional/` unless a broader rollback is explicitly selected.
