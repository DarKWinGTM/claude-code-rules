# Phase 063 - stale-session diagnostic safeguard

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

063

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-stale-session-diagnostic-safeguard.patch.md](../patch/analysis-stale-session-diagnostic-safeguard.patch.md)

## Objective

Add one temporary stale-session diagnostic safeguard to `/memory-context-intelligence:analysis` so long-lived freshness mismatch can be surfaced to the operator without changing the normal analysis status/output and without turning restart into the final fix.

## Why this phase exists

Phase 062 hardened the operator contract around slash invocation and generic no-request fallback, but the checked workflow still lacked a dedicated stale-session warning path. The strongest checked reading remained a freshness mismatch between a long-lived session and a newer installed plugin update, not a verified exact internal loader/cache slot. This phase exists to make that mismatch visible as an advisory diagnostic only.

## Gate

Phase 063 closes only when all of the following are true in checked scope:
- focused RED/GREEN tests prove the analysis surface emits an advisory `stale_long_lived_session` warning when checked freshness evidence shows the current session predates the installed plugin update
- focused RED/GREEN tests prove missing/invalid freshness evidence does not fabricate the warning
- focused RED/GREEN tests prove the warning does not change normal `available` status or replace topic-card / `Next action options` output
- focused skill-contract tests prove restart guidance stays temporary/diagnostic only and does not normalize the bug
- focused suite passes
- full `memory-context-intelligence` suite passes
- governed/runtime-facing docs are synchronized to the diagnostic-only contract

## Verification / closeout

Phase 063 is completed in checked scope.

This closeout now holds:
- `lib/analysis_surface.py` now resolves checked local transcript freshness evidence and installed plugin metadata to emit one advisory `stale_long_lived_session` warning when the session predates the installed plugin update
- the source `.claude-plugin/plugin.json` syntax regression was fixed so the manifest is valid JSON again and fresh plugin registration no longer drops `/memory-context-intelligence:analysis` into `Unknown command`
- the warning remains additive only and does not change `available`, `blocked`, `dormant`, or `no-topics` status semantics
- repeated topic cards and the compact `Next action options` bridge remain intact
- focused RED/GREEN proof passed for the new stale-session analysis-surface tests plus the new manifest-validity test
- focused `tests/test_presentation.py`, `tests/test_analysis_surface.py`, and `tests/test_analysis_skill_contract.py` passed with `35` checks
- the full runtime/source suite passed with `86` tests
- fresh installed-local `claude -p '/memory-context-intelligence:analysis' --permission-mode bypassPermissions --output-format json` returned normal topic-card output again after the manifest repair
- targeted installed-cache `analysis-surface --session-id d42465eb-30a7-4bc8-b9d6-03e52306e9a5` proof emitted `stale_long_lived_session` while preserving `status = available`, repeated `topic_cards`, and `next_action_options`
- the source package version was bumped from `0.9.21` to `0.9.22`

## Boundaries preserved after closeout

Phase 063 still does not claim:
- that the exact internal long-lived-session stale slot is fully reproduced or permanently eliminated across every interactive session shape
- that restart is the final fix
- that session-dependent no-response is now acceptable normal behavior
- a change to `/additional/`
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 063 is an additive diagnostic layer on top of the existing historical-first, repeated topic-card, and phase-062 slash-request hardening contract. Rolling it back would remove the advisory freshness warning only, while leaving the rest of the analysis contract intact unless a broader rollback is explicitly selected.
