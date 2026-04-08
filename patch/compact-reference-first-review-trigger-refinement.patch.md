# RULES Compact Reference-First Review Trigger Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.8
> **Session:** 4e792d4b-8876-439b-8c07-2c5d4b04af3a
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded Wave 021 refinement that turns the compact review-trigger into a reference-first model.

Why this change matters:
- the user wants compact resume to point Claude at stored session files without turning `additionalContext` into a hidden context-restore channel
- a compact flow that re-inflates old summary text too aggressively risks becoming “compact then expand back”
- the review trigger should stay instruction-first, locator-first, and bounded
- proof should show what directive was emitted without storing another long replay payload

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- `../plugin/scripts/compact-handoff-common.sh`
- `../plugin/scripts/sessionstart-compact-consume-handoff.sh`
- `../README.md`
- `../design/design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- shared runtime bridge under `../../PLUGIN/rules-compact-extension/`

Review concern:
- `systemMessage` should surface a clearer `review-required` signal
- `additionalContext` should remain minimal: instruction + file pointers + status only
- a bounded directive-proof file should capture what was emitted without becoming another context replay path
- the stored session files should remain the source of truth for full historical context, not the injected reminder text

---

## 3) Change Items

### Change Item 1
- **Target location:** success-path `systemMessage`
- **Change type:** replacement

**Before**
```text
The navigator line exposed session/objective/carry/recheck plus review pointers, but did not state review-required explicitly.
```

**After**
```text
The navigator line is now explicitly review-oriented:
- review-required
- objective status
- carry count
- recheck count
- reviewRoot
- review target
```

### Change Item 2
- **Target location:** success-path `additionalContext`
- **Change type:** replacement

**Before**
```text
The model-facing context included review instructions plus some carried-forward summary fields.
```

**After**
```text
The model-facing context is reference-first and bounded:
- one short review-required instruction
- one review directory pointer
- explicit review file list
- one short objective-status line
- one short discipline reminder not to rely on replayed old context
```

### Change Item 3
- **Target location:** fallback `additionalContext`
- **Change type:** replacement

**Before**
```text
Fallback behavior told Claude to review index.json and re-anchor, but still followed the earlier active-review wording shape.
```

**After**
```text
Fallback behavior now stays minimal and reference-first:
- review required
- no exact session match
- review root / index.json pointer
- needs-recheck status
- re-anchor from verified local context
```

### Change Item 4
- **Target location:** per-session proof surfaces
- **Change type:** additive

**Before**
```text
Only sessionstart-proof.json recorded the channel/status outcome.
```

**After**
```text
A new bounded `sessionstart-directive.json` records the emitted directive mode, status summary, review targets, and short directive text without storing a long replay of old context.
```

---

## 4) Verification

- [x] `systemMessage` now includes `review-required`
- [x] success-path `additionalContext` is limited to instruction + locator + status
- [x] success-path `additionalContext` no longer injects carried-forward objective/basis/item blocks directly
- [x] fallback `additionalContext` stays bounded and reference-first
- [x] `sessionstart-directive.json` is recorded per session as bounded directive proof
- [x] source and shared bridge package behavior stay aligned

---

## 5) Rollback Approach

If the reference-first tightening proves too sparse:
- keep the `review-required` visible signal
- keep exact file pointers
- add only tiny status cues back where strictly necessary
- do not restore long carried-forward summary injection into `additionalContext`
- preserve the bounded directive-proof file rather than reverting to opaque behavior
