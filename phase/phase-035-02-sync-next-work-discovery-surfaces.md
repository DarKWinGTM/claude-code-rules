# Phase 035-02 - Sync next-work discovery surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 035-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/next-work-discovery-from-execution-surfaces.patch.md](../patch/next-work-discovery-from-execution-surfaces.patch.md)

---

## Objective

Synchronize the master RULES governance surfaces and installed runtime copies after the next-work discovery refinement.

## Why this phase exists

The owner updates only become operationally real when the master inventory, README, TODO, changelog, phase summary, and installed runtime copies all reflect the same bounded next-work discovery model.

## Entry conditions / prerequisites

- `035-01` is complete and the touched owner chains are already updated
- the bounded patch artifact for this wave already exists
- the active runtime rule count should remain unchanged at 39

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check source/install alignment
- [x] complete postflight review before closing the wave

## Out of scope

- creating additional first-class owner chains
- changing the active runtime rule count
- broad cleanup of unrelated historical review-state drift

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] master surfaces record wave `035` coherently
- [x] touched rule descriptions show the new next-work discovery behavior accurately
- [x] installed runtime files match source for the touched rules
- [x] postflight review confirms the refinement remains bounded to active execution discovery

## Risks / rollback notes

- sync drift can survive even when owner semantics are correct, so master/install parity checks remain required
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted
- preserve wave history instead of silently erasing the refinement wave

## Next possible phases

- none required once sync/parity/review are complete

## Exit criteria

- [x] repository-level governance reflects the next-work discovery model coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `035` phase family is visible and reviewable from `phase/SUMMARY.md`
