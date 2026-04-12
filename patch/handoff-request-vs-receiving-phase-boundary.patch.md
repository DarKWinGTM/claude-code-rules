# Handoff Request vs Receiving Phase Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md) v1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that separates shared-board handoff request naming from receiving-side execution phase ownership.

Why this change matters:
- sender phase labels such as `P228 ...` can leak into cross-session handoff titles and create confusion about who owns the phase
- handoff tasks should stay visibly request-layer items first
- the receiving session should remap accepted work into its own phase/objective/task family when phase tracking is needed

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../shared-execution-coordination.md`
- `../todo-standards.md`
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the new wording must reduce phase-owner ambiguity without forcing every task title into a rigid format
- source phase/context must remain traceable without becoming the default visible owner label

---

## 3) Change Items

### Change Item 1
- **Target location:** `shared-execution-coordination` primary owner
- **Change type:** additive

**Before**
```text
The chain already defined lease, handoff, and retention semantics, but it did not yet explicitly separate request-layer naming from receiving-side execution-phase ownership.
```

**After**
```text
The chain now explicitly separates request-layer naming from execution-layer remap and makes receiving-side phase ownership explicit.
```

### Change Item 2
- **Target location:** `todo-standards` task-board naming companion
- **Change type:** additive

**Before**
```text
The chain already governed live task-list behavior, but it did not yet explicitly say that cross-session requests should avoid using the sender's phase as the default visible title label.
```

**After**
```text
The chain now explicitly says cross-session request tasks should use request/handoff naming first, keep source trace in notes when useful, and let the receiving session remap accepted work into its own execution structure.
```

### Change Item 3
- **Target location:** `phase-implementation` and repository-model companions
- **Change type:** additive

**Before**
```text
Phase and repository companions already deferred shared-board coordination to the new owner, but they did not yet explicitly reinforce that sender phase labels should not become the receiving-side default execution identity.
```

**After**
```text
The companions now explicitly reinforce that receiving-side phase ownership remains local to the execution owner and is distinct from shared-board handoff request naming.
```

---

## 4) Verification

- [x] `shared-execution-coordination` explicitly separates request-layer naming from execution-layer remap
- [x] receiving-side phase ownership is explicit
- [x] canonical handoff naming guidance is explicit
- [x] source trace is pushed into handoff notes/description instead of default visible phase labeling
- [x] touched companions now reinforce the boundary coherently
- [x] master design/README/TODO/changelog/phase surfaces record this bounded refinement coherently
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too rigid:
- keep the request-vs-execution distinction intact while narrowing the visible naming guidance before removing it entirely
- preserve the receiving-side phase ownership boundary rather than reverting to sender-phase leakage in handoff titles
- preserve the patch and phase history instead of silently erasing the refinement wave
