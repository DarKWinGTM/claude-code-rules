# Native-first analysis communication contract patch

> **Current Version:** 0.1.58
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-28)
> **Status:** Phase 054 completed native-first analysis communication contract in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.58
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user clarified that the latest readable sample was not the raw first response from `/memory-context-intelligence:analysis`; it was the result of asking AI to rewrite the first response into easier human language. The next wave therefore needed to move that rewrite behavior into the first pass instead of making the operator ask for a second manual rewrite.

## 2) Analysis

The communication-contract wave needed one coherent before/after review boundary:
- keep broader historical analysis and trace-anchored promotion from phase 053 intact
- rewrite user-facing titles into semantic human-readable wording
- separate first-pass output into `presentation / recommendation / proposal`
- keep source mix, provenance, and status visible in the expanded proposal
- preserve native-first operator-facing wording without drifting into package/pipeline narration
- sync source-authority and runtime-facing docs so the active contract no longer drifts from the implemented behavior

## 3) Change items

### 3.1 Source-authority design and execution sync
- **Target artifact:** `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-054-native-first-analysis-communication-contract.md`, `../changelog/changelog.md`, `../changelog/v0.1.58-completed-native-first-analysis-communication-contract.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement/additive
- **Before:** active source-authority docs still described the older historical-default contract as the latest completed wave
- **After:** governed source-authority docs now record phase 054 as the completed native-first communication-contract wave

### 3.2 Runtime/source implementation sync
- **Target artifact:** `../lib/signals.py`, `../lib/presentation.py`, `../skills/analysis/SKILL.md`, `../tests/test_signals.py`, `../tests/test_presentation.py`, `../tests/test_analysis_skill_contract.py`
- **Change type:** replacement
- **Before:** first-pass titles could still be keyword-bag shaped, the payload was still mainly list-first, and the skill contract did not require the new native-first first-pass rewrite behavior
- **After:** first-pass titles are semantic and human-readable, the payload separates `presentation / recommendation / proposal`, and the public skill contract now requires a native-first operator-facing first response without a second manual rewrite pass

### 3.3 Runtime-facing projection sync
- **Target artifact:** `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/design/design.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/phase/SUMMARY.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/changelog/changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/skills/analysis/SKILL.md`
- **Change type:** replacement
- **Before:** runtime-facing projection docs still described the older first-pass contract
- **After:** runtime-facing projection docs now describe the verified native-first communication contract that matches the implemented runtime behavior

## 4) Verification

- focused runtime tests should pass for `tests/test_signals.py`, `tests/test_presentation.py`, and `tests/test_analysis_skill_contract.py`
- mirrored focused source-authority tests should pass for the same files
- full runtime and source-authority suites should pass
- one real local available path plus one no-topics path should prove the first-pass communication contract and historical-first insufficiency wording
- design / changelog / TODO / phase / patch / runtime-facing docs should agree on phase 054 as the latest completed wave

## 5) Rollback approach

If this wave is rolled back, restore the older operator-facing wording and output layering while preserving the historical-default scope behavior from phase 053 unless the user explicitly selects a broader rollback. Do not mutate `/additional/`, install state, or main RULES as part of this patch rollback unless the user explicitly authorizes broader rollback scope.