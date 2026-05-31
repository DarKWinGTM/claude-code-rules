# Multi-source config-policy docs sync patch

> **Current Version:** 0.1.70
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-31)
> **Status:** Phase 066 completed docs-only multi-source config-policy sync in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.70
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The recent design discussion selected a stronger target direction for `memory-context-intelligence`: multi-source by design, with any future config file treated as a late-bound source-selection/source-limit policy instead of a required new authority layer. Current runtime truth already has the four-class evidence model, so this wave only needs a governed docs sync that makes the target wording explicit without overclaiming runtime implementation.

## 2) Analysis

The safe move is a docs-only wave. The governed surfaces should explain what a config file would control — source mode, bounded defaults, allowlists, explicit disables, and missing-source reporting posture — while preserving the current rule that `trace_evidence` remains the live promotion anchor. That keeps current runtime truth and target docs policy separate instead of letting the new direction read like already-shipped code.

## 3) Change items

### 3.1 Align source-model owner wording
- **Target artifact:** `../design/08-memory-evidence-source-model.design.md`
- **Change type:** additive/refinement
- **Before:** the four-class model was explicit, but no config-file boundary explained how future source-policy settings fit that model
- **After:** the source-model owner now says config file is a late-bound source-selection/source-limit policy for the same four classes, not a fifth evidence class, not semantic authority, and not promotion proof by itself

### 3.2 Align operator/presentation wording
- **Target artifact:** `../design/02-topic-list-and-choice-flow.design.md`
- **Change type:** additive/refinement
- **Before:** configuration language focused on presentation modes only
- **After:** the topic-list owner now says a future config file may also hold bounded source-policy defaults, but cannot override evidence/provenance boundaries or replace structured fileless selected-topic state

### 3.3 Sync parent design, README, phase, changelog, and TODO
- **Target artifact:** `../design/design.md`, `../README.md`, `../phase/SUMMARY.md`, `../phase/phase-066-multi-source-config-policy-doc-sync.md`, `../changelog/changelog.md`, `../changelog/v0.1.70-completed-multi-source-config-policy-doc-sync.changelog.md`, and `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement/additive
- **Before:** the parent/current-state surfaces stopped at phase 065 / v0.1.69 and did not yet align on the docs-only config-policy target
- **After:** those surfaces now record phase 066 / v0.1.70 as a docs-only clarification wave, keep `/memory-context-intelligence:analysis` active, keep `review` / `packet` deferred, preserve trace anchoring, and keep runtime/code/package version unchanged

## 4) Verification

- read back the touched governed surfaces and confirm they all describe config file with the same bounded meaning
- confirm the touched surfaces all preserve `trace_evidence` as the live promotion anchor
- confirm the touched surfaces all keep the wave docs-only and do not imply runtime config-file loading, code changes, package-version changes, or test reruns
- confirm portability wording still avoids machine-local defaults in shared docs

## 5) Rollback approach

If this wave is rolled back, revert the docs-only config-policy wording changes only. Do not mutate runtime/code surfaces, package version, install state, retained cache/data, or `/additional/` material unless a broader rollback is explicitly selected.
