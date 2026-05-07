# Goal-First Working Frame and Next-Goal Recommendations Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.90
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P075-03 extends the P075 closeout/reporting family after P075-02 added roadmap-aware completion. The new concern is goal awareness: AI should not merely execute task lists; for non-trivial work it should know the current goal, expected output, and completion gate, then use that frame to recommend a supported next goal at true closeout.

This patch is non-code/governance-only. It changes runtime rule doctrine and governed records; no product code or TestKit scenario is in scope.

---

## 2) Analysis

The current RULES system already has roadmap-aware completion, but the natural owner for goal framing is still limited to full-goal-set visibility and anti-fixation. The missing layer is a proportional strategy:

```text
Goal is navigation, not ceremony.
```

The target behavior should:
- establish goal/output/gate for non-trivial work when it prevents drift or improves verification
- keep visible goal framing triggered, not mandatory for every simple response
- preserve selected safe continuation
- recommend meaningful next goals only from checked design/TODO/phase/implementation evidence
- avoid inventing future work or turning next-goal proposals into selected execution

---

## 3) Change Items

### GFW-001 — `goal-set-review-and-priority-balance.md` goal-first owner expansion

- **Target artifact:** `../goal-set-review-and-priority-balance.md`
- **Change type:** additive + metadata alignment

**Before**
```text
The rule keeps the full active goal set visible and prevents single-subtask fixation.
```

**After**
```text
The rule also owns non-trivial goal-first working frames: outcome-first goal, expected output, completion gate, goal hierarchy, triggered visibility, anti-ritual boundaries, and evidence-grounded next-goal recommendations.
```

### GFW-002 — Execution continuity goal-state bridge

- **Target artifact:** `../execution-continuity-and-mode-selection.md`
- **Change type:** additive + metadata alignment

**Before**
```text
Completion-to-roadmap classifies selected successor work, meaningful unselected successor work, ambiguous successor work, and no visible successor work.
```

**After**
```text
Completion-to-roadmap also classifies goal state: selected current/next goal continues; meaningful unselected next goal becomes advisory; ambiguous or approval-sensitive next goal asks narrowly; unsupported next goal is not invented.
```

### GFW-003 — Closing and presentation next-goal shape

- **Target artifacts:** `../response-closing-and-action-framing.md`, `../explanation-quality.md`, `../answer-presentation.md`, `../high-signal-communication.md`
- **Change type:** additive + metadata alignment

**Before**
```text
Closeout can recommend the next phase or wave with goal, output, and gate.
```

**After**
```text
Closeout can recommend a supported next goal with why, expected output, and gate while keeping easy-first explanations compact and preserving useful goal framing from over-pruning.
```

### GFW-004 — Phase and TODO goal/output/gate alignment

- **Target artifacts:** `../phase-implementation.md`, `../todo-standards.md`
- **Change type:** additive + metadata alignment

**Before**
```text
Phase roadmaps and live tasks expose phase context and execution slices.
```

**After**
```text
Phase roadmaps, phase matrices, and non-trivial live tasks can carry goal/output/gate meaning so execution remains outcome-shaped rather than command-only.
```

### GFW-005 — Master governance release sync

- **Target artifacts:** `../README.md`, `../design/design.md`, `../changelog/changelog.md`, `../TODO.md`, `../phase/SUMMARY.md`, this patch file, and `../phase/phase-075-03-goal-first-working-frame-and-next-goal-recommendations.md`
- **Change type:** companion sync only

**Before**
```text
Master records are synchronized through v9.89 / P075-02 roadmap-aware completion behavior.
```

**After**
```text
Master records record v9.90 / P075-03 as a goal-first continuation of the P075 closeout/reporting family, active runtime count remains 44, and runtime install/parity/body-sufficiency verification runs before release completion claims.
```

---

## 4) Verification

- [x] Runtime rule changes are limited to the listed active runtime owners.
- [x] Goal-first guidance is triggered and proportional, not a rigid visible-template requirement.
- [x] Selected safe continuation remains first-class and is not blocked by goal framing.
- [x] Next-goal recommendations require checked roadmap/goal evidence and remain advisory unless selected.
- [x] README active runtime install list remains 44 files.
- [x] Runtime install copies only the 44 active runtime rule files.
- [x] Source/runtime parity and body sufficiency pass for the active runtime install set.
- [x] No plugin/project-owned runtime destination files are touched.
- [x] Git push and GitHub release `v9.90` are verified.

---

## 5) Rollback Approach

If P075-03 proves too broad:
- narrow or revert only the goal-first / next-goal wording and companion record entries
- preserve P075-02 roadmap-aware completion behavior unless separately challenged
- preserve P075-01 phase-backed delivery/feature/impact closeout reporting
- preserve P076 design-to-phase synthesis and P081 worker routing
- preserve P073-10 active runtime body-sufficiency boundaries
- do not delete or manage destination/runtime files outside the current source-owned active runtime install set as part of rollback
