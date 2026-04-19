# Phase-Context-Aware Task Discovery Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.18
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes Task List behavior consult `/phase` more actively whenever governed phase context already exists and is relevant.

Why this matters:
- current RULES doctrine already says live task creation should be current-phase-first and should align to clearly implied staged/phase context
- but `/phase` often already contains more planning information than just the currently open phase file
- when phase order, dependencies, and already-authored next planned phases are visible, task behavior should not ignore that context
- at the same time, the refinement must preserve the boundary that unopened future-phase work does not silently become active execution work

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../todo-standards.md`
- `../phase-implementation.md`
- `../project-documentation-standards.md`
- `../phase-implementation-template.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`

Review concern:
- the refinement should make `/phase` context more actively usable without weakening the current future-phase draft boundary
- next-phase information should be usable as bounded planning input, not silent activation permission
- the wave should remain inside existing owners rather than creating a new first-class doctrine chain

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards`
- **Change type:** additive

**Before**
```text
Task-list doctrine already favored the current active phase and clearly implied staged context, but it did not yet explicitly say that existing `/phase` planning data such as ordering, dependencies, and authored next phases should also be consulted when relevant.
```

**After**
```text
Task-list doctrine now stays current-phase-first while also consulting relevant `/phase` planning data such as active phase family, phase ordering/dependencies, and already-authored next planned phases when that information exists and helps continuity or draft next-work visibility.
```

### Change Item 2
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase-linked task behavior already allowed implied current staged context and bounded next-work discovery, but it did not yet define an explicit phase-context hierarchy that includes already-authored next-phase context from `/phase`.
```

**After**
```text
Phase implementation now defines a bounded phase-context hierarchy for task behavior: current active phase, current phase family, and already-authored next-phase context from `/phase`, while preserving that unopened future phases remain draft-only until made active by governing context.
```

### Change Item 3
- **Target location:** `project-documentation-standards`
- **Change type:** additive

**Before**
```text
The repository model already treated design, phase, TODO, task-list, and checked implementation state as execution-discovery surfaces, but it did not yet say clearly that `/phase` may contribute both current execution structure and already-authored next planned structure.
```

**After**
```text
The repository model now says that `/phase` may contribute both the governed current execution structure and already-authored next planned structure for bounded task discovery, without silently activating unopened future work.
```

### Change Item 4
- **Target location:** `phase-implementation-template`
- **Change type:** additive

**Before**
```text
The root helper exposed current active phase and next checkpoint fields, but it did not yet explicitly surface active phase family, planned next phases, or the activation boundary for next-phase context.
```

**After**
```text
The root helper now exposes active phase family, planned next phase(s), and explicit activation-boundary wording so future `/phase` authoring can support the refined doctrine consistently.
```

### Change Item 5
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master README/design/TODO/changelog/phase surfaces did not yet record this bounded phase-context-aware discovery wave.
```

**After**
```text
Master/history surfaces now record the phase-context-aware task discovery refinement as a bounded wave and keep the doctrine coherent across repo-level guidance.
```

---

## 4) Verification

- [x] `todo-standards` stays current-phase-first while explicitly consulting relevant `/phase` planning data when available
- [x] `phase-implementation` now defines a bounded phase-context hierarchy without weakening future-phase draft boundaries
- [x] `project-documentation-standards` now treats `/phase` as both current execution structure and bounded next planned structure for discovery
- [x] `phase-implementation-template` now exposes fields needed to author the refined doctrine clearly
- [x] master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve current-phase-first task behavior
- preserve the future-phase draft-only boundary
- narrow the newly added next-phase-context wording before removing it entirely
- do not roll back into a state where already-authored `/phase` planning context is ignored when it is relevant and already visible
