# Phase 035-01 - Refine next-work discovery from execution surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 035-01
> **Status:** Completed
> **Design References:** [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/next-work-discovery-from-execution-surfaces.patch.md](../patch/next-work-discovery-from-execution-surfaces.patch.md)

---

## Objective

Refine RULES so the assistant can discover the next unfinished work from the current execution surfaces instead of waiting for the user to restate it.

## Why this phase exists

The current RULES already support continuous execution when the next step is obvious. The remaining gap is that real project work often exposes the next unfinished slice through task / phase / TODO / design / checked implementation state together, not through one already-restated prompt. This phase closes that gap without turning discovery into uncontrolled objective drift.

## Entry conditions / prerequisites

- the execution-continuity and goal-review owners already exist
- same-objective task-list continuity already exists
- the refinement remains bounded to existing owners rather than creating another first-class chain
- the governed patch artifact for this wave is already established

## Action points / execution checklist

- [x] update `execution-continuity-and-mode-selection` as the primary owner
- [x] update `todo-standards` as the live task-list discovery companion
- [x] update `phase-implementation` as the phase-work discovery companion
- [x] update `project-documentation-standards` as the repository-model companion
- [x] keep the refinement bounded to the same active objective / execution mode rather than creating cross-objective drift
- [x] avoid expanding `accurate-communication.md` for this wave

## Out of scope

- opening a brand new unrelated objective automatically
- bypassing legitimate stop gates or approval-sensitive boundaries
- treating speculative future-phase work as active by default
- replacing the existing goal-review owner or task-list continuity owner

## Affected artifacts

- `execution-continuity-and-mode-selection.md`
- `todo-standards.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- touched design and changelog companions for those chains
- bounded patch and phase artifacts for wave `035`

## Verification

- [x] execution continuity now includes active next-work discovery semantics
- [x] the task list is explicitly the first next-work discovery surface within the same objective
- [x] the phase workspace is explicitly available as a bounded discovery surface when the task list alone is insufficient
- [x] the repository model explicitly recognizes execution-discovery surfaces once execution mode is active
- [x] the refinement stayed inside the existing owner set

## Risks / rollback notes

- wording could become too broad and accidentally imply new-objective auto-selection
- wording could weaken future-phase boundaries if it is read as permission to promote draft work too early
- rollback should narrow discovery wording before removing the refinement entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `035-02` sync master docs and runtime install parity
- no new first-class owner chain is needed if the bounded companion updates stay coherent

## Exit criteria

- [x] active next-work discovery is clearly owned without weakening stop-gate boundaries
- [x] the task-list / phase / repository companions express one coherent bounded discovery model
- [x] the refinement remains a bounded follow-up wave instead of a new doctrine chain
