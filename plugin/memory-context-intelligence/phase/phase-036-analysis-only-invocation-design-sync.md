# Phase 036 - analysis-only invocation design sync

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

036

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Synchronize the governed docs to a clear invocation-design decision before runtime mutation: keep `/memory-context-intelligence:analysis` as the single primary public command for the next implementation wave, and keep `/memory-context-intelligence:review` plus `/memory-context-intelligence:packet` deferred until they have clearly distinct purposes.

## Why this phase exists

Earlier phases proved install/load truth, named slash-surface proof for `/memory-context-intelligence:memory-context-intelligence`, and the broader peer-surface model. But the user-facing invocation design was still ambiguous because the default response shape drifted toward package-map and mechanism-first explanation instead of proposal-first topic suggestions.

## Approval boundary

Phase 036 executed as a docs-only design/governance sync wave.

Executed boundary:
- no runtime surface rename or mutation
- no plugin reinstall or uninstall
- no marketplace mutation
- no source package deletion or narrowing
- no `/additional/` behavior change
- no new proof, publication, stable/broad production readiness, or main RULES promotion/mutation/merge claim

## Expected output

Phase 036 produces:
- one selected public invocation model for the next implementation wave
- a clear first-response contract for the later analysis command
- aligned design/README/changelog/TODO/phase/patch/skill wording without pretending the runtime surface already changed

## Entry conditions

- phase 035 is completed checked-local proof-and-blocker capture evidence
- current runtime proof for `/memory-context-intelligence:memory-context-intelligence` remains valid existing behavior
- plugin-managed auto-flow remains unclaimed
- source authority remains `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`

## Gate

Phase 036 closes only when all of the following are true in checked scope:
- governed docs select analysis-only as the single primary public command for later implementation
- `review` and `packet` are explicitly deferred unless their purposes separate clearly later
- the selected first response is proposal-first topic suggestions rather than package-map or internal pipeline explanation
- docs separate current checked runtime truth from the selected target invocation design
- the next implementation-planning phase is explicitly defined

## Design decision

Selected public model now:
- primary public command after later implementation: `/memory-context-intelligence:analysis`
- deferred public commands: `/memory-context-intelligence:review`, `/memory-context-intelligence:packet`

Selected first-response contract:
- present proposed improvement topics directly
- include short why/impact wording and a recommended first topic when one is materially stronger
- do not default to package-map, governance-map, or internal pipeline narration
- open deeper mechanism, matrix, packet, or rollout detail only after topic selection or explicit internal request
- if no strong candidate exists, say so directly

## Verification / closeout

Phase 036 is completed in checked local scope.

This closes the docs-only invocation-design question because:
- design now explicitly selects analysis-only as the next public command model
- docs now distinguish current proven slash behavior from the selected target invocation design
- the next implementation-planning phase is opened as phase 037 before any runtime mutation

## Boundaries preserved after closeout

Phase 036 still does not claim:
- runtime implementation of `/memory-context-intelligence:analysis`
- runtime removal/renaming of `/memory-context-intelligence:memory-context-intelligence`
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 036 is a docs-only governance wave. Rolling it back means reverting the design decision wording and phase opening, not mutating the installed runtime surface, reinstalling plugins, or deleting source/package artifacts without separate explicit approval.
