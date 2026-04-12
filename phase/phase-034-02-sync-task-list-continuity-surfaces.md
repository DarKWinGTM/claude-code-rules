# Phase 034-02 - Sync task-list continuity surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 034-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/task-list-continuity-and-objective-boundary-retention.patch.md](../patch/task-list-continuity-and-objective-boundary-retention.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the task-list continuity refinement.

## Why this phase exists

The owner updates only become operationally real when the inventories, README, TODO, changelog, phase summary, and installed runtime copies all reflect the same same-objective task-list continuity model.

## Entry conditions / prerequisites

- `034-01` is complete and the touched owner chains are already updated
- the bounded patch artifact for this wave already exists
- the runtime install target remains limited to the touched rule subset plus the already-dirty accurate-communication maintenance copy

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check source/install alignment
- [x] include the already-open accurate-communication size maintenance in the same sync/release pass if still dirty

## Out of scope

- rewriting unrelated rule chains
- turning the task list into a permanent durable history system
- release/git work before sync and verification complete

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] master surfaces record wave `034` coherently
- [x] task-list continuity wording is visible at both owner and repository levels
- [x] installed runtime files match source for the touched rules
- [x] any carried dirty state from accurate-communication size maintenance is also synchronized in this pass

## Risks / rollback notes

- sync drift can survive even when owner semantics are correct, so master/install parity checks remain required
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted
- preserve wave history instead of silently erasing the refinement wave

## Next possible phases

- none required once sync/parity/release are complete

## Exit criteria

- [x] repository-level governance reflects the same-objective task-list continuity model coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `034` phase family is visible and reviewable from `phase/SUMMARY.md`
