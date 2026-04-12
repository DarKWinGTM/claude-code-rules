# Phase 033-03 - Integrate execution continuity and goal review

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 033-03
> **Status:** Completed
> **Design References:** [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/goal-set-review-and-priority-balance.design.md](../design/goal-set-review-and-priority-balance.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/continuous-execution-and-goal-set-review.patch.md](../patch/continuous-execution-and-goal-set-review.patch.md)

---

## Objective

Integrate the new execution-continuity and goal-review owners into adjacent rules, master governance surfaces, and installed runtime copies.

## Why this phase exists

The new owners only become operationally real when adjacent runtime rules defer cleanly to them, the master inventories and install set include them, and the installed runtime copies match source.

## Entry conditions / prerequisites

- `033-01` and `033-02` are complete
- the governed patch artifact for this wave already exists
- the touched runtime integrations remain bounded and avoid unnecessary expansion into `accurate-communication.md`

## Action points / execution checklist

- [x] update adjacent runtime/design/changelog companions
- [x] update master design/README/changelog/TODO/phase surfaces
- [x] install touched runtime copies into `~/.claude/rules/`
- [x] parity-check source/install alignment

## Out of scope

- unrelated rule-chain rewrites
- aggressive expansion of `accurate-communication.md`
- release/git work before sync and verification complete

## Affected artifacts

- touched runtime/design/changelog companions for adjacent owner chains
- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] adjacent owners defer cleanly to the new chains
- [x] active runtime inventory/install set includes both new rules
- [x] master surfaces record wave `033` coherently
- [x] installed runtime copies match source for all touched rules

## Risks / rollback notes

- sync drift can survive even when the new chains are sound, so master/install parity checks remain required
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted
- preserve wave history instead of silently erasing the integration slice

## Next possible phases

- none required once sync and parity complete
- any later refinement should open a new bounded wave

## Exit criteria

- [x] repository-level governance reflects the new chains coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `033` phase family is visible and reviewable from `phase/SUMMARY.md`
