# Phase 065 - rich topic-card explanation restoration

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

065

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-rich-topic-card-explanation-restoration.patch.md](../patch/analysis-rich-topic-card-explanation-restoration.patch.md)

## Objective

Restore the richer easy-to-understand topic-card explanation quality in `/memory-context-intelligence:analysis` without losing the compact first-pass before/after previews, repeated topic-card rhythm, evidence-calibrated wording, or advisory stale-session boundary.

## Why this phase exists

Phase 064 successfully added compact `Before behavior` / `After behavior` previews to every first-pass topic card, but the user then reported that the older easy-to-understand explanation style had regressed. In checked runtime output, the surface was still rendering through `present --output-mode auto` with no reliable user-language hint, and the known doctrine-level topic bodies were still falling back to English explanation text even when the operator-facing labels should have stayed Thai-native. This phase restores that richer first-pass explanation quality while keeping the first-pass cards compact and evidence-calibrated.

## Gate

Phase 065 closes only when all of the following are true in checked scope:
- focused RED/GREEN tests prove the analysis-surface wrapper now calls `present` in native-first mode and carries a Thai language hint when recent user-facing context is Thai or no stronger language signal is available
- focused RED/GREEN tests prove known doctrine-level topic cards render Thai-native explanation bodies instead of English labels-only hybrids
- focused RED/GREEN tests still prove compact first-pass before/after previews remain present and evidence examples remain conditional on real bounded preview evidence
- the full `memory-context-intelligence` suite passes
- a real local analysis-surface output check shows Thai-native topic-card labels plus richer Thai explanation bodies while preserving repeated topic cards, `next_action_options`, and the advisory stale-session warning
- governed/runtime-facing docs are synchronized to the restored contract

## Verification / closeout

Phase 065 is completed in checked scope.

This closeout now holds:
- `lib/analysis_surface.py` no longer renders the live operator surface through `present --output-mode auto`; it now calls `present` in `native-first` mode and carries an inferred presentation language, with Thai as the local operator-facing fallback when no stronger recent-language signal is available
- `lib/presentation.py` now localizes the known doctrine-level topic-card explanation bodies in Thai instead of localizing only the labels and some titles
- `tests/test_analysis_surface.py` now proves the wrapper uses native-first presentation and passes a Thai language hint when recent user-facing context is Thai
- `tests/test_presentation.py` now proves known doctrine-level topic cards restore richer Thai explanation bodies instead of English labels-only hybrids
- the source package version was bumped from `0.9.23` to `0.9.24`
- focused `tests/test_presentation.py`, `tests/test_analysis_surface.py`, and `tests/test_signals.py` passed with `46` checks
- the full runtime/source suite passed with `90` tests
- a real local source-side `analysis-surface` check via `bin/memory-context-intelligence` returned `status = available`, preserved repeated `topic_cards`, `next_action_options`, and `operator_warnings`, and now shows Thai-native topic-card labels plus richer Thai explanation bodies for the restored doctrine-level topics

## Boundaries preserved after closeout

Phase 065 still does not claim:
- that localized rich explanation bodies are proof of broader multi-session doctrine by themselves
- that `Evidence examples` may be fabricated when preview evidence is absent
- that the compact first-pass contract should be replaced with wrapper-style essay output
- a change to `/additional/`
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 065 is a wrapper/presentation refinement on top of phases 061-064. Rolling it back would remove the restored native-first Thai explanation shaping only, while leaving repeated topic cards, compact first-pass before/after previews, conditional real `Evidence examples`, the advisory `Next action options` bridge, and the stale-session warning path intact unless a broader rollback is explicitly selected.
