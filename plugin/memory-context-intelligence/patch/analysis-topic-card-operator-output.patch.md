# Topic-card operator output patch

> **Current Version:** 0.1.65
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-30)
> **Status:** Phase 061 completed repeated topic-card operator output in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.65
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user explicitly corrected that the latest `/memory-context-intelligence:analysis` output had become harder to read because it merged several topics into one wrapper-style explanation flow instead of showing topic-by-topic presentation in one repeated format.

## 2) Analysis

The correct repair is to change the presentation contract unit, not the evidence model.

The patch therefore keeps:
- historical-first scope
- doctrine-level titles
- trace-anchored promotion
- conditional bounded `Evidence examples` / `Before behavior` / `After behavior`

And changes:
- the default operator-facing output unit becomes repeated topic cards
- each surfaced topic keeps the same per-topic format
- legacy wrapper payload keys stop driving the operator-facing shape
- runtime output stops leaking legacy wrapper keys such as `topic_list`

## 3) Change items

### 3.1 Repeated topic-card render contract
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** replacement
- **Before:** the default operator-facing payload was organized around wrapper sections and one primary proposal expansion
- **After:** the default operator-facing payload now returns repeated `topic_cards`, each with the same per-topic structure

### 3.2 Runtime payload cleanup
- **Target artifact:** `../lib/analysis_surface.py`, `../tests/test_analysis_surface.py`
- **Change type:** replacement
- **Before:** the runtime payload still leaked legacy wrapper-era keys into the operator-facing output path
- **After:** the runtime payload now forwards `topic_cards` and removes the leaked legacy wrapper payload key path from the operator-facing result

### 3.3 Public contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-061-topic-card-operator-output.md`, `../changelog/changelog.md`, `../changelog/v0.1.65-completed-topic-card-operator-output.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** active docs still described the now-rejected wrapper-style operator surface
- **After:** active docs now describe repeated topic-card operator output as the selected contract

## 4) Verification

- focused RED/GREEN proof for missing repeated `topic_cards` in `build_presentation()`
- focused RED/GREEN proof for leaked legacy runtime payload keys in `analysis_surface.py`
- focused RED/GREEN proof for repeated topic-card public contract wording in `skills/analysis/SKILL.md`
- full runtime/source suite green
- one real local `/memory-context-intelligence:analysis` run via `--plugin-dir` showing separate repeated topic cards instead of one merged wrapper-style explanation block

## 5) Rollback approach

If this correction is rolled back, restore the wrapper-style operator surface while preserving the historical-first evidence model, doctrine-level titles, and conditional evidence-example sections unless a broader rollback is explicitly selected.
