# governed-docs phase-backed implementation program expansion patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope synced
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures the phase-program repair after the first implementation slice proved that the later required coverage had not yet been opened in child phase files.

## Analysis

Before this patch:
- P001-01 had been implemented and verified
- later required coverage existed only as short roadmap bullets and design shards
- the phase program did not yet open child files for doctrine evaluator, repair planner, skill/agent surfaces, bounded executor policy, hook posture, or release-gate flow

After this patch:
- the full v1 implementation wave is now represented as explicit child phases
- implementation order is visible
- the latest Markdown/article presentation requirement is preserved as a separate later phase rather than silently mixed into the current wave

## Change Items

### 1) Expand phase summary coverage
- **Target artifact:** `phase/SUMMARY.md`
- **Change type:** refinement
- **Before state:** later layers were only implied
- **After state:** the summary maps design shards to child phases, shows implementation order, and opens the full v1 wave coverage explicitly

### 2) Open child phases for the remaining v1 wave
- **Target artifact:** `phase/phase-001-02-*.md` through `phase/phase-001-06-*.md`
- **Change type:** additive
- **Before state:** later layers had no dedicated phase files
- **After state:** evaluator, repair planner, operator skill/agent surfaces, bounded executor policy/hook guardrails, and release-gate flow all have their own bounded phase files

### 3) Preserve later Markdown/article presentation as a separate proposal phase
- **Target artifact:** `phase/phase-001-07-article-markdown-presentation-separate-later-phase.md`
- **Change type:** additive
- **Before state:** the latest presentation request was only in transcript context
- **After state:** it is tracked as a separate later phase with clear out-of-scope boundaries for the current wave

### 4) Sync durable tracking surfaces
- **Target artifact:** `TODO.md`, `changelog/changelog.md`
- **Change type:** refinement
- **Before state:** durable tracking emphasized only the completed first slice
- **After state:** durable tracking now reflects the full opened implementation wave while keeping unchecked later slices separate from completed scope

## Verification

Checked verification for this patch:
- phase summary now names explicit child phase files through P001-06
- each new child phase file defines objective / expected output / gate / out-of-scope / affected artifacts
- P001-01 remains the only runtime slice claimed implemented in checked scope
- later slices remain planned/selected and are not overclaimed as implemented

## Rollback approach

If the phase program needs further restructuring:
- keep P001-01 as the completed scanner foundation
- preserve design-shard source-of-truth mapping
- narrow or regroup later child phases without collapsing them back into vague roadmap bullets
- keep the presentation proposal separate unless explicitly promoted
