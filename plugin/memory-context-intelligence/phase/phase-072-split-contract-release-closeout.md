# Phase 072 - split-contract release closeout

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

072

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md)

## Patch References

- none

## Objective

Close the plugin-scoped release wave for the per-topic additional-artifact split contract by bumping the package/governed versions again, preserving plugin-only release scope, and keeping the packet/additional/public-surface boundaries explicit in the released state.

## Why this phase exists

Phase 071 completed the implementation and verification of the split contract, but a separate closeout wave is still useful so the released version state clearly records the plugin-only release boundary, the final package/governed version bump, and the fact that this wave did not reopen public surfaces or weaken the trace anchor.

## Gate

Phase 072 closes only when all of the following are true in checked scope:
- the package version is bumped from `0.9.27` to `0.9.28`
- the governed version chain is bumped from `0.1.75` to `0.1.76`
- plugin-only README/design/phase/changelog/version surfaces stay aligned to the released split-contract truth
- focused checks and the full plugin suite still pass after the release-version bump
- no new public surface, main RULES mutation, or combined multi-topic additional output is introduced by the release closeout

## Verification / closeout

Phase 072 is completed in checked scope.

This closeout now holds:
- the split-contract hardening remains intact in the released state
- package/governed version surfaces are aligned to `0.9.28` / `0.1.76`
- the plugin-only release boundary remains explicit
- the released state still keeps one selected topic per artifact and forbids combined multi-topic additional output

## Boundaries preserved after closeout

Phase 072 still does not claim:
- a changed public surface for `/memory-context-intelligence:analysis`
- reopening `review` or `packet` as public commands
- any weakening of `trace_evidence` as the live promotion anchor
- main RULES mutation, promotion, or merge
- stable/broad production readiness beyond checked scope
