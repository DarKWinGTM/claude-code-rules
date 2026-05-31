# Rich topic-card explanation restoration patch

> **Current Version:** 0.1.69
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-31)
> **Status:** Phase 065 completed rich topic-card explanation restoration in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.69
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The first-pass topic cards already had compact before/after previews from phase 064, but the user then reported that the older easy-to-understand explanation quality had disappeared. The live wrapper was still rendering through `present --output-mode auto` with no reliable user-language hint, and the known doctrine-level cards were still carrying English explanation bodies even when the operator-facing surface should have stayed Thai-native.

## 2) Analysis

The repair stays inside the wrapper/presentation contract. We do not need to undo repeated topic cards, remove compact before/after previews, or weaken evidence discipline. The right move is to restore native-first rendering at the wrapper boundary and restore richer Thai explanation bodies for the known doctrine-level cards, while leaving `Evidence examples` real-preview-only and preserving the advisory bridge/stale-session boundaries.

## 3) Change items

### 3.1 Native-first wrapper rendering for the operator surface
- **Target artifact:** `../lib/analysis_surface.py`, `../tests/test_analysis_surface.py`
- **Change type:** replacement/refinement
- **Before:** the live operator wrapper still called `present --output-mode auto` with no reliable user-language hint, so compact rich topic cards could regress to English output even in the Thai-native operator flow
- **After:** the live operator wrapper now calls `present` in `native-first` mode, infers presentation language from recent user-facing context when possible, and falls back to Thai for this local operator-facing surface when no stronger language signal is available

### 3.2 Restore richer Thai explanation bodies for known doctrine-level cards
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** additive/replacement
- **Before:** some doctrine-level cards only localized labels/titles while the actual explanation bodies still stayed English, making the first-pass output feel flatter and harder to understand
- **After:** known doctrine-level cards now restore richer Thai explanation bodies for `มันคืออะไร`, `อาการ/ปัญหา`, `ก่อนปรับ`, `หลังปรับ`, and `ถ้าปรับแล้วจะดีขึ้นยังไง`, while preserving exact evidence boundaries and compact card rhythm

### 3.3 Public contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../README.md`, `../phase/SUMMARY.md`, `../phase/phase-065-rich-topic-card-explanation-restoration.md`, `../changelog/changelog.md`, `../changelog/v0.1.69-completed-rich-topic-card-explanation-restoration.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** the public/governed contract still described phase 064 as the latest presentation state and did not explicitly capture the native-first wrapper restoration or the richer Thai explanation-body restoration
- **After:** the contract now records phase 065 as the restoration wave, updates proof counts/versioning, and keeps the restored native-first topic-card explanation model aligned across governed/runtime-facing surfaces

## 4) Verification

- focused RED/GREEN proof that the analysis-surface wrapper now uses native-first rendering and carries a Thai language hint when Thai user-facing context is present
- focused RED/GREEN proof that known doctrine-level cards now restore richer Thai explanation bodies instead of English labels-only hybrids
- focused proof that compact first-pass before/after previews and conditional real `Evidence examples` remain intact
- focused suite passed with `46` checks
- full runtime/source suite passed with `90` tests
- real local source-side `analysis-surface` output showed Thai-native topic-card labels plus richer Thai explanation bodies while preserving repeated cards, `next_action_options`, and the advisory stale-session warning

## 5) Rollback approach

If this refinement is rolled back, remove the native-first wrapper/language restoration and Thai explanation-body overrides only, while leaving repeated topic cards, compact default before/after previews, conditional real `Evidence examples`, the advisory `Next action options` bridge, and the stale-session diagnostic safeguard intact unless a broader rollback is explicitly selected.
