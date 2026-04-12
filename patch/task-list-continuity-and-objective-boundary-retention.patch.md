# Task-List Continuity and Objective-Boundary Retention Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.6
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that keeps the built-in task list continuous within the same active objective instead of repeatedly replacing it with a fresh task set.

Why this change matters:
- the current rules already say the task list is the live execution surface for non-trivial work
- in practice, the task list can still be recreated too often, making prior completed and in-progress slices harder to see
- the user wants continuity within the same objective, while still allowing a fresh task list when a genuinely new objective begins

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../todo-standards.md`
- `../artifact-initiation-control.md`
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- task-list continuity should improve visibility without turning the built-in task list into a permanent cross-objective history store
- a fresh task list must still be allowed when the user opens a genuinely new objective or explicitly requests a reset

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards` primary owner
- **Change type:** additive

**Before**
```text
The chain already defined the task list as the live execution surface, but it did not yet make reuse-before-recreate, append-don't-replace, and completed-task visibility explicit within the same active objective.
```

**After**
```text
The chain now explicitly requires reuse of the current task list within the same active objective, appending new real work instead of replacing the list, and keeping completed tasks visible until the objective is genuinely closed.
```

### Change Item 2
- **Target location:** `phase-implementation` phase companion
- **Change type:** additive

**Before**
```text
The chain already linked the task list to the current phase, but it did not yet explicitly say that repeated slices inside the same objective/phase should extend the existing task list instead of recreating it.
```

**After**
```text
The chain now explicitly keeps repeated work in the same active objective/phase on the same task-list surface unless a true objective-boundary reset occurs.
```

### Change Item 3
- **Target location:** `artifact-initiation-control` startup companion
- **Change type:** additive

**Before**
```text
The chain already required early live task-list initialization, but it did not yet say clearly that once initialized for the active objective, that live surface should normally be reused rather than replaced.
```

**After**
```text
The chain now treats the initialized live task list as the continuing execution surface for that active objective unless a true reset/new-objective boundary exists.
```

### Change Item 4
- **Target location:** `project-documentation-standards` repository-model companion
- **Change type:** additive

**Before**
```text
The repository role model distinguished live and durable tracking, but it did not yet explicitly describe retention and continuity of the live task-list surface within the same active objective.
```

**After**
```text
The repository role model now states that the live task list should retain continuity within the same active objective, while durable history still belongs in TODO/phase/changelog.
```

---

## 4) Verification

- [x] `todo-standards` explicitly defines reuse-before-recreate behavior within the same active objective
- [x] `todo-standards` explicitly keeps completed tasks visible until objective closure
- [x] `phase-implementation` explicitly keeps same-objective phase slices on the same task-list surface
- [x] `artifact-initiation-control` explicitly treats initialized live task lists as the continuing surface for the active objective
- [x] `project-documentation-standards` explicitly describes live task-list continuity vs durable history boundaries
- [x] master design/README/TODO/changelog/phase surfaces record the bounded refinement wave
- [x] touched runtime rules are reinstalled and parity-checked

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the live-vs-durable distinction intact
- narrow the continuity wording before removing same-objective reuse semantics entirely
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to a state where the same active objective repeatedly loses visibility just because the task list is recreated instead of extended
