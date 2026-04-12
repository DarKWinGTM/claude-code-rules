# Phase 034-01 - Refine task-list continuity

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 034-01
> **Status:** Completed
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/task-list-continuity-and-objective-boundary-retention.patch.md](../patch/task-list-continuity-and-objective-boundary-retention.patch.md)

---

## Objective

Refine task-list semantics so the built-in task list is reused within the same active objective instead of being repeatedly replaced by fresh task sets.

## Why this phase exists

The current rules already make the task list the live execution surface, but the user identified a remaining continuity gap: repeated replacement makes earlier completed and in-progress work hard to see. This phase closes that gap while preserving the boundary that a genuinely new objective may still start a fresh task list.

## Entry conditions / prerequisites

- the task-list-first tracking model already exists
- the refinement remains bounded to same-objective task-list continuity rather than creating a new first-class rule chain
- the governed patch artifact for this wave is already established

## Action points / execution checklist

- [x] update `todo-standards` as the primary continuity owner
- [x] update `phase-implementation` as the phase-companion continuity owner
- [x] update `artifact-initiation-control` as the startup continuity companion
- [x] update `project-documentation-standards` as the repository-model companion
- [x] update touched design/changelog/master surfaces for the bounded follow-up wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- turning the built-in task list into a permanent cross-objective history store
- replacing `TODO.md` / `phase` / `changelog` as durable history surfaces
- forcing one forever-growing task list across unrelated objectives

## Affected artifacts

- `todo-standards.md`
- `artifact-initiation-control.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- touched design and changelog companions for those chains
- bounded patch and phase artifacts for wave `034`

## Verification

- [x] same-objective work now reuses the existing task list by default
- [x] completed tasks remain visible until objective closure
- [x] new tasks append into the active objective surface instead of replacing it
- [x] true reset/new-objective boundaries remain explicit

## Risks / rollback notes

- wording could become too broad and accidentally imply one permanent list across unrelated objectives
- rollback should narrow same-objective continuity wording before removing it entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `034-02` sync master docs and runtime install parity
- no new owner chain is needed if the bounded companion updates stay coherent

## Exit criteria

- [x] task-list continuity is clearly owned without blurring objective-boundary resets
- [x] the refinement remains a bounded follow-up wave rather than a new doctrine chain
- [x] the touched owner set expresses one coherent same-objective task-list retention model
