# Phase 053 - historical-default analysis implementation

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

053

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
- [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/07-recall-scoping-and-time-window.design.md](../design/07-recall-scoping-and-time-window.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-historical-default-scope-redesign.patch.md](../patch/analysis-historical-default-scope-redesign.patch.md)

## Objective

Implement the approved historical-default redesign for `/memory-context-intelligence:analysis` so the default scope analyzes broader historical work patterns across the user's memory corpus instead of current-session-first narrowing.

## Why this phase exists

The earlier analysis surface had already gained scoped recall, multi-source evidence classes, and proposal-first output, but it still defaulted to a current-session-first slice. That reduced the tool's usefulness for its actual purpose: reviewing repeated historical work patterns across sessions. This phase exists to move the default scope to broader historical memory, keep live promotion trace-anchored, and preserve current-session evidence as supporting provenance rather than as the main gate.

## Gate

Phase 053 closes only when all of the following are true in checked scope:
- default intake scope uses bounded broader historical memory across the user's work corpus instead of current-session-first narrowing
- repeated historical trace can surface topic candidates without requiring current-session trace as the primary gate
- current-session evidence is supporting provenance/freshness context only, not the default scope owner
- scoring and promotion rank historical repetition, cross-session breadth, and recency ahead of current-session confirmation
- presentation and skill-contract output distinguish `historical-only` from `confirmed-in-current-session` and use historical-first no-topics wording
- focused tests pass in both the runtime-facing and source-authority trees
- one real local `intake -> signals -> present` run proves historical-default behavior
- governed and runtime-facing docs, TODO, phase, changelog, and patch are synced consistently for this redesign wave

## Verification / closeout

Phase 053 is completed in checked scope.

This closeout now holds:
- `lib/intake.py` defaults to a bounded recent historical shard set instead of forcing current-session-first narrowing
- explicit `day`, `session`, and `lookback` narrowing still work when requested
- `lib/signals.py` promotes repeated historical patterns without requiring current-session confirmation as the primary gate
- historical repetition, cross-session breadth, and recency now rank ahead of current-session confirmation
- `current_session_confirmation` remains visible as provenance and score boost only
- `lib/presentation.py` and `skills/analysis/SKILL.md` now use historical-first insufficiency wording and provenance labels such as `historical-only` versus `confirmed-in-current-session`
- focused runtime and source-authority tests passed for intake, signals, presentation, and analysis-contract behavior
- a real local `intake -> signals -> present` chain proved the historical-default path in checked scope
- governed source-authority docs and runtime-facing docs are synced to the redesigned contract

## Boundaries preserved after closeout

Phase 053 still does not claim:
- a change to `/additional/` behavior
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 053 is an implementation wave for analysis scope, ranking, provenance, and doc sync. Rolling it back would restore the older current-session-first default model. Do not mutate `/additional/`, install state, or main RULES as part of a phase-053 rollback unless the user explicitly authorizes broader rollback scope.
