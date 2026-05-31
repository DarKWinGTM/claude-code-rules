# Phase 037 - analysis surface implementation planning

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

037

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Define the implementation plan for changing the user-facing slash surface and first-response behavior to the selected analysis-only model before runtime mutation.

## Why this phase exists

Phase 036 selected the target invocation design, but it did not authorize runtime mutation. A dedicated planning phase was needed so the later implementation wave could change naming, default first-response behavior, fallback behavior, verification, and migration wording without mixing design sync and runtime execution.

## Expected output

Phase 037 should produce an implementation plan that defines:
- how `/memory-context-intelligence:analysis` becomes the primary public command
- what happens to `/memory-context-intelligence:memory-context-intelligence` during migration
- whether `review` and `packet` stay hidden/deferred or become future phases
- how proposal-first first-response behavior is enforced
- how the no-strong-candidate fallback is implemented
- what verification proves the new surface is working in checked scope

## Entry conditions

- phase 036 is completed docs-only invocation-design sync
- no runtime rename or slash-surface mutation has been performed yet
- current slash proof for `/memory-context-intelligence:memory-context-intelligence` remains the checked pre-implementation baseline

## Gate

Phase 037 closes only when a checked implementation plan exists and clearly separates:
- naming/runtime mutation work
- response-behavior work
- fallback/no-candidate behavior
- verification/proof work
- any later review about whether `review` or `packet` deserve independent surfaces

## Verification / closeout

Phase 037 is completed in checked local scope.

This phase produced the implementation plan that phase 038 later executed, including:
- runtime skill-surface rename to `analysis`
- proposal-first first-response contract wording
- deferred `review` and `packet` boundaries
- contract-test verification strategy
- governed doc sync targets for the implementation wave

## Boundaries preserved after closeout

Phase 037 did not itself:
- rename the installed runtime surface
- claim `/memory-context-intelligence:analysis` was already live
- open `review` or `packet` as public commands by assumption
- change `/additional/` behavior
- claim plugin-managed auto-flow proof, publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge

## Rollback notes

Phase 037 is a non-destructive planning wave. Rolling it back means reverting the implementation-planning record, not mutating the installed runtime surface, reinstalling plugins, or deleting source/package artifacts without separate explicit approval.
