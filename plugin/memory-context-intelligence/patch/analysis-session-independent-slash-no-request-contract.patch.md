# Session-independent slash no-request contract patch

> **Current Version:** 0.1.66
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-30)
> **Status:** Phase 062 completed session-independent slash no-request contract in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.66
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user provided checked evidence that `/memory-context-intelligence:analysis` could still return `ยังไม่มีคำขอที่ต้องตอบครับ` in some sessions even though fresh sessions could render the expected topic cards correctly. The user also approved the topic-card presentation itself, but wanted a clearer next step after the cards.

## 2) Analysis

The strongest checked reading is not that historical analysis failed to find topics. The defect is that the operator contract could still allow a generic no-request interpretation in some session shapes even when rendered analysis context existed. The repair therefore needs to harden request ownership and render obligations, not replace the historical-first evidence model or regress back to wrapper-style presentation.

## 3) Change items

### 3.1 Compact post-topic action bridge
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** additive
- **Before:** repeated topic cards could end without a clear operator-facing bridge to the next safe action
- **After:** default operator-facing payload now appends compact advisory `next_action_options` after the repeated topic cards

### 3.2 Explicit slash-request runtime markers
- **Target artifact:** `../lib/analysis_surface.py`, `../tests/test_analysis_surface.py`
- **Change type:** replacement
- **Before:** the runtime payload could still leave the request state implicit enough that a generic no-request response remained possible in some session shapes
- **After:** the runtime payload now carries `analysis_request_present`, `invocation_mode`, `render_required_now`, and `generic_no_request_response_allowed: false` so the checked operator contract keeps the slash invocation as the active request

### 3.3 Public contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-062-session-independent-slash-no-request-contract.md`, `../changelog/changelog.md`, `../changelog/v0.1.66-completed-session-independent-slash-no-request-contract.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** active docs and runtime-facing metadata still stopped at phase 061 repeated topic cards and did not describe the explicit slash-request hardening or the post-topic advisory bridge
- **After:** active docs and runtime-facing metadata now describe the session-independent slash no-request hardening wave, the post-topic advisory bridge, and the package bump to `0.9.21`

## 4) Verification

- focused RED/GREEN proof for `next_action_options` appearing after `topic_cards`
- focused RED/GREEN proof for the explicit slash-request markers in the runtime payload
- focused RED/GREEN proof for the skill contract stating that the slash invocation itself is the request and that generic no-request fallback is disallowed when rendered analysis context exists
- focused presentation / analysis-surface / skill-contract suite passed with `31` checks
- full runtime/source suite passed with `81` tests
- local installed plugin updated from `0.9.20` to `0.9.21`
- one real installed-local `/memory-context-intelligence:analysis` run showed `Topic 1` plus `Next action options`, and the old fallback `ยังไม่มีคำขอที่ต้องตอบครับ` was absent from that proof output

## 5) Rollback approach

If this hardening is rolled back, restore the prior no-bridge / less-explicit request contract while keeping historical-first scope, doctrine-level titles, and repeated topic cards intact unless a broader rollback is explicitly selected.
