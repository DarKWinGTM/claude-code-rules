# Universal Session-Owned Task Title Grammar Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md) v1.3
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that turns visible session ownership into a default task-list standard for session-owned work, regardless of whether the current task list is shared across several sessions or used by one session only.

Why this change matters:
- task ownership should stay scanable even when the operator is not actively thinking about whether the current board is single-session or multi-session
- visible session identity is useful outside shared-path workflows too, because it keeps ownership explicit and reduces ambiguity
- one exact title phrase should not be forced onto every state if it collapses request, held, and blocked meanings together
- the task-list model should preserve request-layer vs execution-layer clarity while still making visible ownership standard by default

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
- the new wording should standardize visible session ownership broadly enough to improve consistency without collapsing request, held, and blocked states into one ambiguous title form
- the refinement should remain a bounded ownership/model clarification rather than a new task-system doctrine chain

---

## 3) Change Items

### Change Item 1
- **Target location:** `shared-execution-coordination` primary owner
- **Change type:** additive

**Before**
```text
The coordination owner already required clearer visible session identity for session-held work, but it still treated that behavior mainly as a multi-session coordination concern and did not yet define one small state-specific grammar strongly enough to act as a universal default for session-owned work.
```

**After**
```text
The coordination owner now makes visible session ownership the default board-facing standard for session-owned work regardless of single-session or multi-session usage, and defines a small state-specific grammar that keeps request, held, and blocked task titles semantically distinct.
```

### Change Item 2
- **Target location:** `todo-standards` live task-board companion
- **Change type:** additive

**Before**
```text
The task-board companion already required visible session identity for session-held or blocked-on-session tasks, but it did not yet explicitly raise that behavior into a default task-list standard across usage modes.
```

**After**
```text
The task-board companion now explicitly says visible session ownership is a default board-facing standard for session-owned work whether the task list is used by one session or several, while preserving distinct request, held, and blocked title forms.
```

### Change Item 3
- **Target location:** `phase-implementation` phase/task linkage companion
- **Change type:** additive

**Before**
```text
The phase companion already protected receiving-side phase ownership against request-layer title leakage, but it did not yet explicitly say that phase-linked execution work should prefer held-owner forms over request-layer forms once the task is already locally owned.
```

**After**
```text
The phase companion now explicitly keeps visible session-state grammar as the default board-facing standard for session-owned work and says phase-linked execution slices should prefer held-owner forms instead of request-layer forms once the executing session already owns the task.
```

### Change Item 4
- **Target location:** `project-documentation-standards` repository-model companion
- **Change type:** additive

**Before**
```text
The repository model already deferred shared-board coordination semantics to the central coordination owner, but it did not yet explicitly raise visible session ownership into a default task-list standard that applies beyond explicit multi-session sharing mode.
```

**After**
```text
The repository model now explicitly says visible session ownership is a default task-list standard for session-owned work and keeps request-layer, held-owner, and blocked-owner title forms distinct through the central coordination owner.
```

---

## 4) Verification

- [x] `shared-execution-coordination` makes visible session ownership a default task-list standard for session-owned work
- [x] `shared-execution-coordination` defines a small state-specific title grammar instead of forcing one ambiguous phrase onto every state
- [x] `todo-standards` reinforces the same standard across one-session and multi-session usage
- [x] `phase-implementation` preserves request-layer vs held-owner distinction when the executing session already owns the task
- [x] `project-documentation-standards` records the universal ownership-standard posture at the repository-model layer
- [x] master design/README/TODO/changelog/phase surfaces record wave `039` coherently
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too rigid:
- keep universal visible session ownership intact while narrowing exact title-form prescriptions before removing the refinement entirely
- preserve request-layer vs held-owner distinction so semantic clarity is not lost during rollback
- preserve the patch and phase history instead of silently erasing the refinement wave
