# Phase 027-01 - Refine task-list-first execution tracking

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 027-01
> **Status:** In Progress
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/task-list-first-execution-tracking.patch.md](../patch/task-list-first-execution-tracking.patch.md)

---

## Objective

Refine the execution/startup/documentation owner set so Claude Code uses the built-in task list more proactively for non-trivial work while keeping `TODO.md` as the durable repository/project tracking artifact.

## Why this phase exists

The user sees the built-in task list as a useful live surface for showing what will be done, what is in progress, and what has already completed. The current RULES stack already governs durable `TODO.md` tracking and startup artifact posture, but it does not yet explicitly define built-in task tracking as the live execution surface for non-trivial work.

## Entry conditions / prerequisites

- the refinement remains bounded to the execution/startup/documentation owner set
- the governed patch artifact for this wave is already established
- no new first-class rule chain is needed if the current owner set can absorb the behavior cleanly

## Action points / execution checklist

- [ ] update `todo-standards` as the primary live-vs-durable tracking owner
- [ ] update `artifact-initiation-control` as the startup companion for early task-list posture
- [ ] update `project-documentation-standards` as the repository-model companion
- [ ] update touched design/changelog artifacts for the three owner chains
- [ ] create a bounded governed patch artifact for this refinement wave
- [ ] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- creating a new first-class doctrine chain
- rewriting `phase-implementation.md`
- rewriting communication/presentation owners unless a contradiction appears
- turning the built-in task list into a governed document artifact

## Affected artifacts

- `todo-standards.md`
- `artifact-initiation-control.md`
- `project-documentation-standards.md`
- touched design and changelog companions for those three chains
- bounded patch and phase artifacts for wave `027`

## TODO coordination

- record the bounded task-list-first refinement as completed work in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- add per-chain changelog entries for `todo-standards`, `artifact-initiation-control`, and `project-documentation-standards`
- add one repository-level master changelog entry for release-level visibility

## Verification

- [ ] built-in task list is now explicitly treated as the live execution surface for non-trivial work
- [ ] `TODO.md` remains explicitly the durable/project execution-tracking artifact
- [ ] trivial work is not forced into task-list overhead
- [ ] task entries are expected to be created early, outcome-sized, and updated through completion

## Risks / rollback notes

- over-applying task-list-first behavior could create ceremony for trivial work if the triggers are too broad
- rollback should narrow trigger/update language first rather than removing the durable-vs-live tracking distinction entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `027-02` sync master docs and runtime install parity
- no additional rollout family is required unless later audit finds drift beyond the touched owner set

## Exit criteria

- [ ] task-list-first behavior is clearly split across primary tracking, startup posture, and repository-model ownership
- [ ] the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
- [ ] the touched owner set expresses one coherent live-vs-durable tracking behavior
