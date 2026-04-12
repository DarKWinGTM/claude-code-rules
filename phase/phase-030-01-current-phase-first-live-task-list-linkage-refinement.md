# Phase 030-01 - Current-phase-first live task-list linkage refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 030-01
> **Status:** Completed
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md)
> **Patch References:** none

---

## Objective

Link built-in task-list behavior explicitly to the current active phase so live execution visibility stays tied to the phase that is actually in progress.

## Why this phase exists

The earlier task-list-first wave made live task tracking more proactive, but the user then identified a remaining failure mode where task lists could still drift into future-wave planning instead of mirroring the current active phase. This bounded follow-up closed that gap without opening a new first-class doctrine chain.

## Entry conditions / prerequisites

- the core task-list-first owner set already exists
- the refinement remains bounded to phase-backed live task-list behavior
- no new standalone rule chain is needed if the touched owners can absorb the behavior cleanly

## Action points / execution checklist

- [x] update `todo-standards` with current-phase-first task-list guidance
- [x] update `phase-implementation` with explicit live task-list linkage to the active phase
- [x] update `artifact-initiation-control` so phase-backed task-list initialization is treated as expected startup behavior
- [x] update touched design/changelog/master surfaces for the bounded follow-up wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- reopening unrelated tracking or documentation chains
- changing the durable-vs-live tracking split itself
- creating push/release artifacts before sync and verification complete

## Affected artifacts

- `todo-standards.md`
- `phase-implementation.md`
- `artifact-initiation-control.md`
- touched design/changelog/master surfaces for the bounded follow-up wave

## TODO coordination

- record the bounded follow-up wave in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure touched per-chain changelogs reflect the version bump already recorded for this follow-up
- ensure the master changelog records the bounded follow-up wave

## Verification

- [x] active non-trivial phases now expect a built-in task list that mirrors the current phase execution surface
- [x] one phase may contain several live tasks without forcing future-phase drift
- [x] future-phase tasks remain draft/proposal work until that later phase is actually opened

## Risks / rollback notes

- wording could become too strict if it blocks legitimate draft planning entirely
- rollback should narrow the current-phase-first wording rather than restoring future-phase drift
- preserve the bounded follow-up history instead of silently erasing it

## Next possible phases

- none required for this bounded follow-up wave
- later tracking refinements should open a new rollout family if needed

## Exit criteria

- [x] current-phase-first task-list linkage is explicit and reviewable
- [x] the bounded follow-up remains separate from the earlier broader task-list-first wave
- [x] the touched owner set expresses one coherent phase-backed live task-tracking behavior
