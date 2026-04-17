# Startup Governance vs Execution Continuity Tightening Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md) v1.6
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded tightening wave that closes the remaining interpretation gap between startup-governance and execution-continuity behavior.

Why this matters:
- startup artifact posture should still be resolved first when governed work crosses the meaningful-work boundary
- once that gate is resolved and the path is clear, execution should keep moving without re-pausing over the same governance decision
- live execution surfaces should help run the work, but they should not silently downgrade required design/changelog/TODO/phase/patch companions into optional extras

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../execution-continuity-and-mode-selection.md`
- `../project-documentation-standards.md`
- `../todo-standards.md`
- `../phase-implementation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- touched chain changelogs for the affected owners

Review concern:
- the wave should tighten existing owners rather than invent a new first-class doctrine chain
- startup governance must stay early and decisive without becoming a repeated stop ritual on every later slice
- documentation companions must stay visibly governed while live execution surfaces remain useful and active

---

## 3) Change Items

### Change Item 1
- **Target location:** `execution-continuity-and-mode-selection`
- **Change type:** additive

**Before**
```text
Execution continuity strongly encouraged continuing active work, but the chain did not yet say explicitly that unresolved startup artifact posture still blocks execution continuity when meaningful governed work has already crossed the startup boundary.
```

**After**
```text
Execution continuity now includes a startup-gate-first boundary: unresolved startup artifact posture remains a real precondition, and continuous execution applies after that gate is resolved enough for the active governed slice.
```

### Change Item 2
- **Target location:** `project-documentation-standards`
- **Change type:** additive

**Before**
```text
The repository model distinguished live execution surfaces from durable/governed surfaces, but it still risked reading as if the live task list could make required design/changelog/TODO/phase/patch companions feel optional.
```

**After**
```text
The repository model now states directly that required governed surfaces remain governed companions even when live execution surfaces are also active.
```

### Change Item 3
- **Target location:** `todo-standards`
- **Change type:** additive

**Before**
```text
TODO synchronization order was clear, but required TODO sync could still be underread as lower-priority bookkeeping instead of companion work that still needs to be completed for a fully synchronized governed wave.
```

**After**
```text
TODO standards now states that when `TODO.md` is required for the governed work, TODO synchronization is required companion work rather than optional bookkeeping.
```

### Change Item 4
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase establishment was already tied to startup governance, but clearly staged/governed work could still be read as if `/phase` might be deferred until later backfill.
```

**After**
```text
Phase implementation now states more directly that when staged/governed work is already clearly implied, phase posture should be resolved early rather than left implicit until later backfill.
```

### Change Item 5
- **Target location:** master surfaces and history surfaces
- **Change type:** additive

**Before**
```text
README, master design, master changelog, TODO, and phase summary did not yet record this specific tightening wave.
```

**After**
```text
Master/history surfaces now record the startup-governance versus execution-continuity tightening wave so repo-level guidance and history stay aligned.
```

---

## 4) Verification

- [x] `execution-continuity-and-mode-selection` now treats unresolved startup artifact posture as a real stop gate
- [x] `project-documentation-standards` now keeps required governed companions visible alongside live execution surfaces
- [x] `todo-standards` now treats required TODO sync as companion work rather than optional bookkeeping
- [x] `phase-implementation` now treats clearly staged/governed work as requiring early phase posture instead of late backfill
- [x] master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the tightening proves too strong:
- preserve the startup-gate-first boundary in execution continuity
- preserve the governed-companion visibility rule in repository documentation standards
- preserve required TODO sync and early phase-posture wording
- narrow phrasing before removing the refinement entirely
- do not roll back into a state where execution continuity again reads like permission to outrun unresolved startup governance
