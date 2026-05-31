# Compact first-pass before/after previews patch

> **Current Version:** 0.1.68
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-31)
> **Status:** Phase 064 completed compact first-pass before/after previews in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.68
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The repeated topic-card operator surface was already stable, but the user found the deeper before/after walkthrough far easier to understand than the first-pass cards alone. The missing piece was a compact preview layer that lets the user picture the change immediately without waiting for a second prompt.

## 2) Analysis

The repair here stays in the presentation contract. We do not need to replace repeated topic cards or loosen evidence discipline. The right move is to keep `Evidence examples` tied to real bounded preview evidence, while giving every first-pass card a short, evidence-calibrated before/after preview that helps the user visualize the target change.

## 3) Change items

### 3.1 Compact before/after previews in first-pass cards
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** additive/replacement
- **Before:** `Before behavior` and `After behavior` only appeared when explicit topic data already carried them, so many first-pass cards showed no concrete before/after picture at all
- **After:** every first-pass topic card now carries compact `Before behavior` and `After behavior` previews by default, while explicit richer before/after text still wins when present

### 3.2 Conditional real evidence example preservation
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** behavior-preserving refinement
- **Before:** `Evidence examples` remained conditional, but before/after sections disappeared entirely when no preview evidence existed
- **After:** `Evidence examples` still stay conditional on real bounded preview evidence, but compact before/after previews remain available even when those examples are absent

### 3.3 Public contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../README.md`, `../phase/SUMMARY.md`, `../phase/phase-064-compact-first-pass-before-after-previews.md`, `../changelog/changelog.md`, `../changelog/v0.1.68-completed-compact-first-pass-before-after-previews.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** the public/governed contract still described before/after as effectively tied to real preview evidence only
- **After:** the contract now says compact before/after previews belong in every first-pass topic card, while long-form illustrative before/after stays in the expanded follow-up layer and `Evidence examples` remain real-preview-only

## 4) Verification

- focused RED/GREEN proof that first-pass cards now include compact `Before behavior` / `After behavior` previews by default
- focused RED/GREEN proof that `Evidence examples` remain conditional on real preview evidence
- focused RED/GREEN proof that the skill contract now distinguishes first-pass compact previews from expanded-layer long-form illustrative before/after
- focused suite passed with `36` checks
- full runtime/source suite passed with `86` tests
- real local source-side `analysis-surface` output showed Topic 1/2/3 with before/after labels while preserving `next_action_options` and the advisory stale-session warning

## 5) Rollback approach

If this refinement is rolled back, remove the compact default before/after previews only while leaving repeated topic cards, conditional real `Evidence examples`, the advisory `Next action options` bridge, and the stale-session diagnostic safeguard intact unless a broader rollback is explicitly selected.
