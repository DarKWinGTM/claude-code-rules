# Analysis config-policy runtime implementation patch

> **Current Version:** 0.1.71
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-31)
> **Status:** Phase 067 completed runtime config-policy loading and guided config-helper sync in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.71
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Phase 066 selected the bounded config-policy direction in docs, but the runtime still lacked actual config loading and the public analysis surface still made raw args the awkward fallback path. The user then clarified the operator UX requirement: when the skill is invoked, it should help the operator configure policy through guided questions instead of depending on raw args as the normal path.

## 2) Analysis

The safe move is a bounded runtime implementation wave rather than a broader redesign. Config policy should stay late-bound and subordinate to the four-class evidence model already in place. That means loading config before later stages, applying source-class and historical-limit routing there, keeping explicit narrow runs narrow, and surfacing any resulting policy limitation honestly all the way to the operator-facing payload. The guided helper should remain advisory only and must not auto-write config or turn config into semantic authority.

## 3) Change items

### 3.1 Add config-policy loader and guided helper owner
- **Target artifact:** `../lib/config_policy.py`
- **Change type:** additive
- **Before:** no dedicated helper loaded analysis config policy or generated guided config questions
- **After:** one helper now owns explicit-path/upward-discovered config loading, source-policy normalization, and advisory `config_questions` plus `suggested_config_path`

### 3.2 Apply source-policy routing in intake
- **Target artifact:** `../lib/intake.py`
- **Change type:** replacement/additive
- **Before:** intake used bounded runtime defaults only and did not load config policy before source gathering
- **After:** intake now loads source policy, applies source-class filtering and historical-shard caps before later stages, and keeps explicit narrow runs narrow even when config requests same-day widening

### 3.3 Preserve trace-anchored promotion and policy-limited provenance
- **Target artifact:** `../lib/signals.py` and `../lib/presentation.py`
- **Change type:** refinement
- **Before:** later stages did not carry config-policy limitation notes through the full review/presentation path
- **After:** policy-limited runs now keep visible limitation notes and still require `trace_evidence` for promotable live candidates

### 3.4 Surface guided config UX on the public analysis wrapper
- **Target artifact:** `../lib/analysis_surface.py`, `../bin/memory-context-intelligence`, and `../skills/analysis/SKILL.md`
- **Change type:** replacement/additive
- **Before:** the public surface did not expose config loading state or guided helper output
- **After:** the analysis wrapper forwards explicit config paths, exposes `source_policy`, shows guided helper output when config is not loaded, and documents that config help is advisory instead of raw-args-first UX

### 3.5 Sync governed owner surfaces
- **Target artifact:** `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../design/08-memory-evidence-source-model.design.md`, `../phase/SUMMARY.md`, `../phase/phase-067-analysis-config-policy-runtime-implementation.md`, `../changelog/changelog.md`, `../changelog/v0.1.71-completed-analysis-config-policy-runtime-implementation.changelog.md`, and `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement/additive
- **Before:** active governed docs still stopped at the docs-only phase-066 interpretation
- **After:** active governed docs now describe the implemented bounded config-policy behavior, the guided helper UX, the preserved trace anchor, and the same proof boundary across all touched owner surfaces

## 4) Verification

- run focused `test_intake.py`, `test_signals.py`, `test_analysis_surface.py`, `test_presentation.py`, and `test_analysis_skill_contract.py`
- run the full runtime package suite and confirm it passes with `98` tests
- run one direct packaged `intake → signals → present` proof with config policy loaded and confirm repeated topic cards plus `Next action options` still render
- run one added packaged recall-only `intake → signals → present` proof and confirm the run stays low-confidence with no live topic candidates when `trace_evidence` is absent
- run one approved local slash proof without config and confirm the guided helper appears
- run one approved local slash proof with an auto-discovered project config file and confirm the guided helper stays absent while no-args config loading works
- read back the touched governed docs and confirm they all preserve the same bounded meaning for config policy, guided helper behavior, and trace-anchored promotion

## 5) Rollback approach

If this wave is rolled back, revert the bounded config-policy implementation and its governed-sync wording together. Do not use rollback as authority to delete `/additional/` artifacts, retained cache/data, shared marketplace state, or unrelated plugin/runtime surfaces unless a broader destructive scope is explicitly selected.
