# Next-Work Discovery from Execution Surfaces Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md) v1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes the assistant discover the next unfinished work from the active execution surfaces instead of waiting for the user to restate it.

Why this change matters:
- continuous execution was already owned, but the current wording still leaned too much on "obvious next step" continuation
- in real project work, the next slice is often discoverable from task / phase / TODO / design / checked implementation state even when it is not already spelled out in one short task-list line
- the user wants RULES to drive that behavior directly so execution can continue toward the designed target without unnecessary `continue` prompts

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../execution-continuity-and-mode-selection.md`
- `../todo-standards.md`
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- next-work discovery must stay bounded to the same active objective rather than silently opening a new unrelated objective
- discovery from execution surfaces must not weaken legitimate stop gates, approval-sensitive boundaries, or future-phase boundaries

---

## 3) Change Items

### Change Item 1
- **Target location:** `execution-continuity-and-mode-selection` primary owner
- **Change type:** additive

**Before**
```text
The chain already said execution should continue when the next path was clear, but it did not yet explicitly require the assistant to inspect current execution surfaces when the next unfinished slice was discoverable but not already restated by the user.
```

**After**
```text
The chain now explicitly treats active next-work discovery as part of execution continuity and requires the assistant to inspect current execution surfaces before waiting for a repeated continue prompt.
```

### Change Item 2
- **Target location:** `todo-standards` live task-list companion
- **Change type:** additive

**Before**
```text
The chain already treated the task list as the live execution surface, but it did not yet explicitly say that the task list is the first discovery surface for the next unfinished work or that broader execution surfaces should be inspected when the task list alone is insufficient.
```

**After**
```text
The chain now treats the task list as the first next-work discovery surface and explicitly allows bounded fallback to active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state when the task list alone is not enough.
```

### Change Item 3
- **Target location:** `phase-implementation` phase-work companion
- **Change type:** additive

**Before**
```text
The chain already linked live task tracking to the current phase, but it did not yet explicitly say that the phase workspace itself may be used to discover the next unfinished slice when the task list alone is incomplete.
```

**After**
```text
The chain now treats the current phase and `phase/SUMMARY.md` as bounded execution-discovery surfaces and allows checked implementation state to sharpen that discovery when phase text alone is insufficient.
```

### Change Item 4
- **Target location:** `project-documentation-standards` repository-model companion
- **Change type:** additive

**Before**
```text
The repository role model already distinguished live execution surfaces from durable history, but it did not yet explicitly recognize those surfaces as execution-discovery inputs once work was already in execution mode.
```

**After**
```text
The repository role model now explicitly recognizes design, phase, TODO, task-list, and checked implementation state as execution-discovery surfaces once execution mode is already active.
```

---

## 4) Verification

- [x] `execution-continuity-and-mode-selection` explicitly defines active next-work discovery from execution surfaces
- [x] `todo-standards` explicitly treats the task list as the first active discovery surface inside the same objective
- [x] `todo-standards` explicitly allows bounded fallback to active phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state
- [x] `phase-implementation` explicitly treats the current phase workspace as a bounded discovery surface
- [x] `project-documentation-standards` explicitly recognizes execution-discovery surfaces at the repository-model layer
- [x] master design/README/TODO/changelog/phase surfaces record wave `035` coherently
- [x] touched runtime rules are reinstalled and parity-checked
- [x] postflight review confirms the refinement stays bounded and does not weaken stop-gate or future-phase boundaries

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep execution continuity intact while narrowing discovery wording before removing it entirely
- preserve the task-list-first and current-phase-first models rather than reverting to repeated user-prompt dependence
- preserve the patch and phase history instead of silently erasing the refinement wave
- do not roll back into a state where already-discoverable unfinished work still requires a restated prompt by default
