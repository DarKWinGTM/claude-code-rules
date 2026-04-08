# RULES Compact Active Review Trigger and Memsearch-Assist Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.7
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded Wave 020A refinement that turns the compact SessionStart hook from a passive carry-forward signal into an active review trigger.

Why this change matters:
- a navigator-only signal still leaves resumed continuation too passive
- the user wants the plugin to actively tell Claude to review stored session data before continuing
- exact `session_id` continuity already exists and should now power stronger review-oriented continuation behavior
- memsearch may help later, but the core compact plugin should first work as a real local review-trigger mechanism on its own

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- `../plugin/scripts/sessionstart-compact-consume-handoff.sh`
- `../README.md`
- `../design/design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- shared runtime bridge under `../../PLUGIN/rules-compact-extension/`

Review concern:
- `additionalContext` must become an explicit review directive, not just passive summary text
- named review files must match the exact resolved source session
- fallback behavior must stay fail-closed when exact routing is unavailable
- memsearch should remain a later assist boundary, not become the core truth source in this wave

---

## 3) Change Items

### Change Item 1
- **Target location:** `plugin/scripts/sessionstart-compact-consume-handoff.sh`
- **Change type:** replacement

**Before**
```text
SessionStart injected selected carry-forward content plus a generic re-anchor reminder.
```

**After**
```text
SessionStart additionalContext now explicitly instructs Claude to review the stored session data before continuing.
```

### Change Item 2
- **Target location:** successful compact-resume additionalContext payload
- **Change type:** replacement

**Before**
```text
The resumed context saw carry-forward content, but review behavior remained implicit.
```

**After**
```text
The resumed context now names the exact review directory plus:
- precompact-context.json
- carry-forward-selected.json
- sessionstart-proof.json
and states that the carried-forward summary must not be treated as settled truth before review.
```

### Change Item 3
- **Target location:** fallback compact-resume additionalContext payload
- **Change type:** replacement

**Before**
```text
Fallback behavior injected only a generic reminder when no exact pending session matched.
```

**After**
```text
Fallback behavior now explicitly tells Claude to review index.json and re-anchor from verified local context before continuing.
```

### Change Item 4
- **Target location:** memsearch role boundary
- **Change type:** additive

**Before**
```text
The compact hook companion had no explicit patch-level statement about memsearch assist boundaries.
```

**After**
```text
This wave keeps memsearch out of the active runtime behavior and records it as a later assist-layer boundary only.
```

---

## 4) Verification

- [x] success-path `additionalContext` explicitly instructs review before continuation
- [x] success-path `additionalContext` names the exact per-session review directory and files
- [x] success-path still carries the visible `systemMessage` navigator line with `reviewRoot=` and `review=`
- [x] fallback `additionalContext` explicitly tells Claude to review `index.json` and re-anchor from verified local context
- [x] memsearch remains outside the active runtime behavior in this wave
- [x] shared `@darkwingtm` bridge behavior stays aligned with the RULES source package

---

## 5) Rollback Approach

If the active review-trigger wording proves too heavy or noisy:
- keep the exact-session routing rule
- keep the visible navigator signal
- preserve explicit file pointers in additionalContext
- reduce wording density before reverting to passive carry-forward-only behavior
- keep memsearch deferred until the core local review-trigger remains semantically strong on its own
