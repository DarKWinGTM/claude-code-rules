# Phase 047 - analysis review correction

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

047

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/07-recall-scoping-and-time-window.design.md](../design/07-recall-scoping-and-time-window.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Correct `/memory-context-intelligence:analysis` so the first response behaves as a design-grounded, current-session-first RULES/workflow review surface rather than as a generic same-day trace-pattern miner.

## Why this phase exists

After phase 046 settled the owner model for any future true bare `/analysis`, the remaining mismatch was behavior. Manual output still showed two design breaks: it could drift into non-current-session same-day evidence by default, and its first-response topic framing still read like generic recurring-pattern mining instead of a RULES/workflow review surface.

## Gate

Phase 047 closes only when all of the following are true in checked scope:
- current-session-first remains the default first-pass scope inside the current day shard
- same-day widening happens only through an explicit fallback selection after current-session insufficiency
- first-response topics are framed as design-grounded RULES/workflow review topics rather than generic recurring-pattern summaries
- provenance stays visible enough for the user to distinguish current-session-only evidence from explicitly widened same-day fallback evidence
- focused intake/signals/presentation/analysis-contract tests pass, and the full runtime package suite stays green
- active source/runtime docs preserve the checked plugin-owned surface `/memory-context-intelligence:analysis`, keep `review` and `packet` deferred, keep `/additional/` unchanged, and avoid new auto-flow/publication/stable-broad/main-RULES claims

## Verification / closeout

Phase 047 is completed in checked local scope.

This closeout now holds:
- the analysis skill contract is current-session-first by default and allows same-day widening only when explicitly selected as fallback
- the topic-generation contract now frames recurring output as design-grounded workflow/evidence/surface review topics instead of generic recurring-pattern titles
- presentation preserves provenance fields so first-response output can disclose evidence scope cleanly
- focused intake/signals/presentation/analysis-contract tests passed and the full runtime package suite stayed green
- active source-authority and runtime-facing docs now describe the same corrected first-response behavior

## Boundaries preserved after closeout

Phase 047 still does not claim:
- a current proved bare `/analysis` runtime surface
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge
- `/additional/` behavior change
- new public `review` or `packet` command surfaces

## Rollback notes

Phase 047 is an implementation-and-governance correction wave for the already-selected plugin analysis surface. Rolling it back would knowingly reintroduce the user-visible drift between current-session purity, review framing, and provenance disclosure. Do not mutate `/additional/` material or reopen bare-surface ownership work as part of a phase-047 rollback unless the user explicitly authorizes a broader scope.
