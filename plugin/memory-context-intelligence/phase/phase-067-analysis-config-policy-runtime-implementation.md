# Phase 067 - analysis config-policy runtime implementation

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

067

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-config-policy-runtime-implementation.patch.md](../patch/analysis-config-policy-runtime-implementation.patch.md)

## Objective

Implement the bounded config-policy layer for `memory-context-intelligence` so `/memory-context-intelligence:analysis` can load late-bound source policy from an explicit config path or an upward-discovered project config file, apply source-selection/source-limit precedence before `intake → signals → present`, preserve `trace_evidence` as the live promotion anchor, and expose guided config-helper output when no config file is loaded.

## Why this phase exists

Phase 066 clarified the target policy in governed docs, but the runtime still lacked the actual config-loading path. The user then corrected the UX direction: the public skill should help the operator configure policy through guided questions instead of making raw args the normal path. Without phase 067, the docs would describe a policy boundary that the runtime did not yet implement, and the slash surface would still leave config discovery/selection harder than requested.

## Gate

Phase 067 closes only when all of the following are true in checked scope:
- `lib/config_policy.py` provides explicit-path and upward-discovered config loading plus advisory guided config-question output
- `lib/intake.py` applies source-class filtering, historical-shard caps, and non-overriding same-day widening defaults before later stages
- `lib/signals.py` and `lib/presentation.py` keep policy-limited provenance visible without weakening trace-anchored promotion
- `lib/analysis_surface.py` forwards explicit config, emits `source_policy`, and surfaces `config_questions` with `suggested_config_path` when no config file is loaded
- focused `test_intake.py`, `test_signals.py`, `test_analysis_surface.py`, `test_presentation.py`, and `test_analysis_skill_contract.py` pass
- the full runtime package suite passes
- one direct packaged `intake → signals → present` proof confirms config-policy loading exists and repeated topic-card output plus `Next action options` still hold
- one approved local slash proof without config shows the guided helper, and one approved local slash proof with an auto-discovered project config file proves no-args policy loading from `/memory-context-intelligence:analysis`
- governed docs stay aligned on the same bounded behavior, and no touched surface overclaims config as semantic authority, a fifth evidence class, selected-topic persistence, or automatic config mutation

## Verification / closeout

Phase 067 is completed in checked scope.

This closeout now holds:
- the runtime can load source policy from explicit `--config` or upward-discovered `memory-context-intelligence.config.json`
- source policy can limit source classes, cap historical shards, and request same-day widening only for non-explicit runs
- explicit narrow runs stay narrow even when config requests same-day widening
- policy-limited runs surface that limitation through later signals/presentation layers instead of overreading the evidence scope
- the public analysis surface emits advisory `config_questions` and `suggested_config_path` when no config file is loaded, giving the operator a guided helper instead of making raw args the normal UX path
- focused tests passed, the full runtime package suite passed with `98` tests, the direct packaged config-policy proof passed, an added packaged recall-only proof confirmed that `recall_evidence` alone stays low-confidence and emits no live topic candidates without trace, and both approved local slash proofs passed

## Boundaries preserved after closeout

Phase 067 still does not claim:
- automatic config writing or auto-save from the guided helper
- selected-topic persistence inside config
- a fifth evidence class or semantic authority for config
- promotion from `durable_memory_context`, `governance_context`, or `recall_evidence` alone without `trace_evidence`
- `/additional/` behavior changes
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Rolling back phase 067 would remove the runtime config-policy layer and its governed-sync wording while leaving the earlier historical-default, topic-card, and trace-anchored evidence model intact unless a broader rollback is explicitly selected. Any rollback must preserve `/additional/`, retained cache/data, shared marketplace state, and unrelated plugin/runtime surfaces unless the user explicitly authorizes narrower destructive scope.
