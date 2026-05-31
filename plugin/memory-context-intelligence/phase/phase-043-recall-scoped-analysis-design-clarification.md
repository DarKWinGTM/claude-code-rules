# Phase 043 - recall-scoped analysis design clarification

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

043

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/07-recall-scoping-and-time-window.design.md](../design/07-recall-scoping-and-time-window.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Clarify, from checked memsearch/recall evidence, how `/analysis` should use current-session and same-day memory instead of broad all-history input.

## Why this phase exists

Phase 042 proved the public `/analysis` surface and memsearch-backed output, but it still left the input-shaping question too broad. The user then redirected the work: first understand memsearch/recall properly, then define the correct design for session-scoped and same-day-scoped analysis before any new runtime mutation.

## Gate

Phase 043 closes only when all of the following are true in checked scope:
- checked local memsearch docs/runtime surfaces are used to describe current recall behavior
- the design explicitly distinguishes current recall capability from desired `/analysis` scoping behavior
- the selected model defines current-session scope, same-day scope, configurable same-day lookback, and no broad all-history default
- implementation remains deferred until this design is explicit
- active design/phase/TODO lineage is synchronized to that clarified contract

## Verification / closeout

Phase 043 is completed in checked local scope.

This closeout now holds:
- checked local evidence shows current memsearch recall is search → expand → transcript drill-down
- checked local evidence shows public recall currently proves query/top-k/source-prefix behavior, not first-class `session/day/lookback` flags
- a checked local experiment shows exact `session_id` search within a same-day `source_prefix` still returns mixed-session results, so raw UUID query is not the deterministic selector for `/analysis`
- design now requires an L0 deterministic scope-narrowing stage before deeper recall/analysis
- selected default scope is current project → current day → current session, with optional same-day lookback and same-day-only widening before any broader history
- implementation changes remain intentionally deferred in this wave

## Boundaries preserved after closeout

Phase 043 still does not claim:
- runtime implementation of the new recall-scoped contract
- new public `review` or `packet` surfaces
- `/additional/` behavior change
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 043 is a docs/design clarification wave. Rolling it back means reverting the recall-scoping contract wording unless the user explicitly approves broader runtime/package mutation.
