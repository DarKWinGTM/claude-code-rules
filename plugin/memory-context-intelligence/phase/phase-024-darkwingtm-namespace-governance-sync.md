# Phase 024 - darkwingtm namespace governance sync

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

024

## Status

Completed by this documentation wave.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Clarify the selected target namespace for `memory-context-intelligence` before any further installability implementation.

## Why this phase exists

The checked local phase-020 through phase-023 evidence used `@inline` and `rules-local` proof paths. The user later selected `darkwingtm` as the target marketplace namespace, and the current checked local mapping still has `darkwingtm` pointing at `<template-plugin-root>` while `rules-local` points at `<repo-root>/plugin`. The active source home remains `<repo-root>/plugin/memory-context-intelligence/`.

That means the previous proof remains valid historical evidence, but it is transitional and cannot be treated as final proof for `memory-context-intelligence@darkwingtm`.

## Goal

Make the governed docs state the selected target install ID and the transitional status of phases 020-023 clearly enough that phases 025-027 can reprove the lifecycle under the correct namespace.

## Output

Completed output:

- active docs name `memory-context-intelligence@darkwingtm` as the selected target install ID
- active docs preserve `<repo-root>/plugin/memory-context-intelligence/` as the active source home
- active docs preserve the checked local mapping distinction: `darkwingtm` points at `<template-plugin-root>`; `rules-local` points at `<repo-root>/plugin`
- phases 020-023 remain completed but are reclassified as transitional rules-local / `@inline` proof
- phases 025-027 are opened as planned darkwingtm proof phases
- no runtime install state, settings, marketplaces, or cache are mutated by phase 024

## Gate

Phase 024 is complete when README, design, phase summary, phase 020-023 notes, changelog, patch, and root TODO all reflect the darkwingtm target namespace, preserve prior evidence without falsifying it, and identify darkwingtm proof as not yet performed.

## Owner

Governance/design sync owner.

## Files

- `README.md`
- `design/design.md`
- `design/06-plugin-installability.design.md`
- `phase/SUMMARY.md`
- `phase/phase-020-plugin-manifest-and-marketplace-bootstrap.md`
- `phase/phase-021-session-only-load-proof.md`
- `phase/phase-022-persistent-install-proof.md`
- `phase/phase-023-reload-uninstall-and-install-doc-closeout.md`
- `phase/phase-024-darkwingtm-namespace-governance-sync.md`
- `phase/phase-025-darkwingtm-session-only-proof.md`
- `phase/phase-026-darkwingtm-persistent-install-proof.md`
- `phase/phase-027-darkwingtm-uninstall-lifecycle-closeout.md`
- `changelog/changelog.md`
- `changelog/v0.1.28-opened-darkwingtm-namespace-correction-wave.changelog.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md`

## Verification

Verification route: documentation/governance review.

Covers:

- target namespace wording
- transitional reclassification of phases 020-023
- planned phase 025-027 path
- no runtime mutation by this phase

Does not cover:

- session-only `memory-context-intelligence@darkwingtm` load proof
- persistent `memory-context-intelligence@darkwingtm` install proof
- darkwingtm uninstall lifecycle proof
- slash-command/chat invocation proof
- publication or external marketplace release

## Risks

- overstating transitional `rules-local` proof as final darkwingtm proof
- losing or weakening valid phase-020 through phase-023 checked-local evidence
- accidentally mutating runtime install state during a docs-only correction wave
- treating author metadata `darkwingtm` as install namespace proof

## rollback notes

Rollback is documentation-only. Revert the 0.1.28 doc wave if needed. Do not delete or mutate runtime install state, settings, marketplaces, cache, the source package, retained `rules-local` state, or `/additional/` trial material as part of phase 024 rollback.
