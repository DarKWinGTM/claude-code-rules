# Task List Phase Context and Session Language Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.17
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that strengthens how Task List creation relates to Phase structure and to the active session language context.

Why this matters:
- current RULES already says that when an active phase exists, task-list entries should mirror it
- but real work often belongs to an already phase-shaped or staged project context before the exact next phase file exists
- task titles/descriptions should also read naturally in the active session language/register instead of defaulting to detached generic wording

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../todo-standards.md`
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should strengthen existing owners rather than creating a new doctrine chain
- phase-shaped task creation should not weaken future-phase boundary protections

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards`
- **Change type:** additive

**Before**
```text
Task-list behavior strongly mirrored an already-active phase, but it did not yet explicitly say that clearly phase-shaped project context should still shape task creation before the exact next phase file exists.
```

**After**
```text
Task-list behavior now aligns to the active phase when present and to clearly implied staged/phase context when that context is already visible from checked project/workstream state.
```

### Change Item 2
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase-linked task behavior started from the assumption that the exact current phase file already existed.
```

**After**
```text
Phase-linked task behavior now allows provisional alignment to a clearly implied current staged/phase context even before the exact next phase file exists.
```

### Change Item 3
- **Target location:** `project-documentation-standards`
- **Change type:** additive

**Before**
```text
The repository model preserved governed companions versus live execution surfaces, but it did not yet explicitly reinforce phase-shaped task creation at the repo-model layer.
```

**After**
```text
The repository model now says that where the checked repository/workstream already operates through phased or staged structure, live task creation should stay aligned to that phase-shaped execution model.
```

### Change Item 4
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master README/design/TODO/changelog/phase surfaces did not yet record this refinement wave.
```

**After**
```text
Master/history surfaces now record the task-list/phase/session-language refinement as a bounded wave and keep the same outcome visible across repo-level documentation.
```

---

## 4) Verification

- [x] task-list rules now align task creation to active phase or clearly implied staged/phase context
- [x] phase-linked task behavior can align provisionally before the exact next phase file exists
- [x] repo-level documentation model reinforces phase-shaped task creation
- [x] master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve active-phase-first task behavior
- narrow the implied-phase-context wording before removing it entirely
- do not roll back into a state where task creation must wait for an exact phase file even when phase-shaped context is already clear
