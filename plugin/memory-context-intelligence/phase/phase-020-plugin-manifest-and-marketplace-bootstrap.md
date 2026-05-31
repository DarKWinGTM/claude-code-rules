# Phase 020 - Plugin manifest and local marketplace bootstrap

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

020

## Status

Completed

## Historical reclassification note

Under the later selected namespace basis, this phase remains Completed and valid as checked source-side/bootstrap evidence, but it is transitional. It does not prove the selected target install ID `memory-context-intelligence@darkwingtm` because the checked local runtime mapping still has `darkwingtm` pointing at `<template-plugin-root>` while `rules-local` points at `<repo-root>/plugin`.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Prepare the package manifest and source-side local marketplace/bootstrap surface needed for later load and install proof.

## Why this phase exists

The package can be usable in checked scope without being installable through Claude Code plugin mechanisms. Before load proof, the manifest and local marketplace root must identify the source package, machine-facing metadata, and bootstrap path clearly without moving active source truth into runtime install state.

## Goal

Make the manifest and source-side local marketplace bootstrap ready for phase 021 session-only load testing while keeping the active implementation home unchanged.

## Output

Completed output:

- updated `.claude-plugin/plugin.json` author identity to lowercase `darkwingtm` and `https://github.com/darkwingtm`
- selected and created the source-side parent marketplace bootstrap surface at `<repo-root>/plugin/.claude-plugin/marketplace.json`
- added one local marketplace plugin entry for `memory-context-intelligence` with source `./memory-context-intelligence`
- kept the marketplace description and plugin entry wording source-side only, with no runtime load, persistent install, publication, marketplace release, or main RULES promotion claim
- made no persistent Claude runtime install mutation, no external install/cache mutation, and no `settings.json` edit

## Gate

Phase 020 is complete in checked source scope because the manifest/bootstrap files now identify the local source package for phase 021 session-only load proof and the active implementation home still remains `<repo-root>/plugin/memory-context-intelligence/`.

Phase 021 remains the first actual session-only load-proof gate. Phase 020 does not claim session-only load proof, persistent install proof, publication, marketplace release, or main RULES promotion/merge.

## Owner

Plugin package/manifest owner.

## Files

Implemented source-side file changes:

- `.claude-plugin/plugin.json`
- `../.claude-plugin/marketplace.json` at `<repo-root>/plugin/.claude-plugin/marketplace.json`
- package README and governed docs for phase closeout

## Verification

Verification route: `smoke_check` limited to file/bootstrap-surface verification.

Checked scope for phase 020 is limited to source-side manifest and marketplace bootstrap files plus governed documentation sync. It verifies that the expected files exist and contain the selected source-side metadata/path references. It does not verify Claude Code session load, persistent install, reload behavior, uninstall behavior, publication, external marketplace release, or runtime availability.

Any later phase that touches Claude runtime install state, external install/cache locations, persistent runtime config, or `settings.json` still requires explicit approval before mutation.

## Risks

- confusing local marketplace bootstrap with session-only or persistent install proof
- moving source truth into an install output path
- changing author identity outside the manifest/bootstrap scope
- accidentally treating the parent local marketplace file as a public marketplace release

## rollback notes

Rollback should restore the previous manifest/bootstrap state and remove only bootstrap outputs created by this phase after explicit action-and-scope confirmation if deletion is required. Do not delete the source package, persistent Claude runtime state, external install/cache locations, `settings.json`, or phase-015 `/additional/` trial artifact as a phase-020 rollback side effect.
