# Phase-First Task-Shaping Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.20
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes phase-first task shaping more explicit when `/phase` already exists and relevant governed phase context is available.

Why this matters:
- current RULES doctrine already says task behavior should mirror the active phase and consult broader `/phase` context
- but that wording can still be treated like a soft preference rather than a shaping requirement
- the user wants task-list behavior to stop under-prioritizing `/phase` and to treat available governed phase context as the first shaping authority when relevant
- detached generic task shaping in the presence of relevant governed phase context should be treated as drift, not as an acceptable fallback

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../todo-standards.md`
- `../phase-implementation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`

Review concern:
- strengthen task-shaping priority for `/phase` without weakening the future-phase boundary or forcing speculative next-wave task creation
- preserve the ability to use implied current staged context when the exact next phase file does not yet exist

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards`
- **Change type:** additive

**Before**
```text
Task behavior should mirror the current phase and consult broader `/phase` context, but the wording still allowed that behavior to read like guidance rather than a required shaping step.
```

**After**
```text
When `/phase` exists and relevant governed phase context is available, task creation must inspect that phase context before shaping the live task list, and detached generic task shaping in the presence of that context is treated as task-shaping drift.
```

### Change Item 2
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase-linked task behavior described current-phase-first and phase-context-aware discovery, but it did not yet say strongly enough that relevant governed phase context must be inspected before task shaping.
```

**After**
```text
Phase-linked task behavior now explicitly requires inspection of relevant governed `/phase` context before shaping the live task list and treats generic fallback shaping in the presence of that context as execution drift.
```

### Change Item 3
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master/history surfaces did not yet record this bounded phase-first task-shaping refinement wave.
```

**After**
```text
Master/history surfaces now record the phase-first task-shaping refinement coherently and make it visible that `/phase` is a required task-shaping authority when relevant governed phase context is already available.
```

---

## 4) Verification

- [x] `todo-standards` now explicitly requires inspection of relevant governed `/phase` context before live task shaping when that context exists
- [x] `phase-implementation` now explicitly requires inspection of relevant governed `/phase` context before live task shaping when that context exists
- [x] detached generic task shaping in the presence of relevant governed phase context is now treated as drift rather than as an acceptable fallback
- [x] future-phase boundaries remain intact
- [x] touched master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve current-phase-first and phase-context-aware behavior as the baseline
- narrow the new required-inspection wording before removing it entirely
- do not roll back into a state where available governed `/phase` context can be ignored casually during task shaping
