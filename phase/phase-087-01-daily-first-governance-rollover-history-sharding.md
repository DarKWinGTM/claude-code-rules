# Phase 087-01: Daily-First Governance Rollover and History Sharding

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 087-01
> **Status:** Completed
> **Design References:** [../design/governed-document-rollover-control.design.md](../design/governed-document-rollover-control.design.md) v1.0; [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) v2.37; [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.26; [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.31
> **Patch References:** [../patch/daily-first-governance-rollover-history-sharding.patch.md](../patch/daily-first-governance-rollover-history-sharding.patch.md)
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Add a first-class RULES mechanism for daily-first rollover of oversized governed control files, then apply it to the already oversized `TODO.md` and `phase/SUMMARY.md` surfaces.

## Why This Phase Exists

Long-lived `TODO.md` and `phase/SUMMARY.md` files can become too large for active session scanning. The checked P087 starting state already showed `TODO.md` and `phase/SUMMARY.md` above hard-trigger sizes, and `phase/SUMMARY.md` failed a full read because of token limits. The phase prevents future autocompact thrash by keeping main files as compact active entrypoints and moving accumulated detail into referenced daily/history/done shards.

## Expected Output

- new `governed-document-rollover-control` rule/design/changelog chain
- updated adjacent runtime owner chains for TODO, phase, documentation, changelog, safe reading, and execution continuity
- compacted active `TODO.md` and `phase/SUMMARY.md` with links to `history/` and `done/`
- pre-rollover snapshots preserved under daily history shards
- README/master design/master changelog/patch/TODO/phase records synchronized for v9.92
- runtime install and source/runtime parity/body-sufficiency verification for the 46-file active runtime set

## Completion Gate

P087-01 closes only after source docs are synchronized, active entrypoints reference reachable history/done shards, runtime install copies only README-listed active runtime rules, 46/46 source-runtime parity and body sufficiency pass, `master` is pushed, and GitHub release `v9.92` is verified.

## Action Checklist

- [x] Preserve pre-rollover snapshots of oversized `TODO.md` and `phase/SUMMARY.md`.
- [x] Create the governed-document-rollover-control rule/design/changelog triad.
- [x] Update adjacent owner chains and companions.
- [x] Compact `TODO.md` and `phase/SUMMARY.md` into active entrypoints with history/done references.
- [x] Sync README, master design, master changelog, TODO, phase, and patch records.
- [x] Install active runtime rules only.
- [x] Verify source/runtime parity and active runtime body sufficiency.
- [x] Commit, push, and publish release `v9.92`.

## Out of Scope

- deleting completed history because it is large
- moving design into `design/done/`
- installing TODO/phase/history/done files as runtime rules
- starting P086 constructive-dissent work
- claiming stability beyond checked source/runtime/release gates

## Verification Plan

- active runtime inventory count equals README install arrays
- Bash and PowerShell install arrays match
- every listed active runtime root has canonical metadata, `Full history`, and a substantive body
- `TODO.md` and `phase/SUMMARY.md` are smaller active entrypoints after rollover
- `TODO.md` references `todo/history/` and `todo/done/`
- `phase/SUMMARY.md` references `phase/history/` and `phase/done/`
- rollover shards link back to their parent entrypoints
- pre-rollover snapshots exist and preserve old content
- destination runtime copies match source for the active install set

## Closeout Summary

P087-01 delivered a first-class daily-first rollover rule chain and applied it to the already oversized active `TODO.md` and `phase/SUMMARY.md` surfaces. The practical improvement is that fresh RULES sessions can start from compact current-state entrypoints while still reaching pre-rollover snapshots, daily movement history, and completed/detail shards when audit or rollback needs them.

Verification basis: README install arrays contain exactly 46 source-owned runtime files, runtime install copied only those active roots, and source/runtime parity plus body sufficiency passed 46/46 with destination extras observed-only. `master` was pushed and GitHub release `v9.92` was published.

Next phase state: P086 constructive-dissent refinement remains deferred and not started until explicitly selected.

## Rollback Notes

If the rollover model is wrong, revert the P087 release commit. If only wording is too broad, narrow the new rollover owner and companion surfaces while preserving the pre-rollover snapshots and active entrypoint links until a safer migration plan exists. Do not delete history/done shards as cleanup without explicit destructive authorization and stronger semantic authority.
