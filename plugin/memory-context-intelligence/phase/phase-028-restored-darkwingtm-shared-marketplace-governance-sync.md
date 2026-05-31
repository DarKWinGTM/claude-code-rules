# Phase 028 - restored darkwingtm shared-marketplace governance sync

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

028

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Align the active governed docs to the restored shared `darkwingtm` marketplace runtime state without mutating runtime/plugin state.

## Why this phase exists

Phases 025-027 recorded valid checked evidence while the effective local `darkwingtm` marketplace mapping was temporarily/remapped to `<repo-root>/plugin`. The runtime mapping was later restored to the shared marketplace at `<template-plugin-root>` to recover other plugins. That restoration changes current runtime truth, so the active docs must stop treating phases 025-027 as current target-state proof.

## Current runtime truth

- active source package remains `<repo-root>/plugin/memory-context-intelligence/`
- active runtime marketplace mapping is restored to `darkwingtm` -> `<template-plugin-root>`
- `<template-plugin-root>/.claude-plugin/marketplace.json` does not include `memory-context-intelligence`
- `memory-context-intelligence@darkwingtm` is not currently installed/enabled under the restored shared marketplace
- retained cache/data from the old proof is historical evidence only, not active install state

## Goal

Complete a docs-only governance correction that preserves phases 025-027 as historical checked evidence while reopening the current `memory-context-intelligence@darkwingtm` target-state path under the restored shared marketplace.

## Output

Completed docs-only output:

- active installability design states the restored shared-marketplace runtime truth
- phase summary maps phase 028 as completed and phases 029-030 as planned
- phase 025-027 files carry historical reclassification notes near the top
- changelog, README, patch, and root TODO wording stop presenting phases 025-027 as current closed runtime truth
- phases 017-018 remain deferred
- `/additional/` trial-stage behavior remains unchanged

## Gate

Completed when the governed docs consistently distinguish:

- current runtime truth under `darkwingtm` -> `<template-plugin-root>`
- historical evidence from phases 025-027 under the temporary/remapped state
- future design work in phase 029
- future approval-sensitive reproof in phase 030

## Owner

Docs-only marketplace-governance correction owner.

## Verification

Verification route: `not_applicable_with_reason` for runtime/plugin behavior; this phase is docs-only governance sync.

Checked-scope docs verification focus:

- phase 028 is marked completed only as a documentation/governance correction
- phase 029 remains planned design resolution without runtime mutation
- phase 030 remains planned and approval-sensitive
- active docs state that the restored shared marketplace does not currently include `memory-context-intelligence`
- active docs state that `memory-context-intelligence@darkwingtm` is not currently installed/enabled

This phase does not verify current plugin availability, persistent install, uninstall lifecycle behavior, publication, external marketplace release, slash-command/chat invocation, stable/broad production readiness, main RULES promotion, main RULES mutation, or main RULES merge.

## Runtime mutation boundary

Phase 028 intentionally does not mutate:

- plugin install state
- settings
- marketplace registry
- cache
- source package runtime contents
- `/additional/` runtime material

## Risks / limits

- The restored shared `darkwingtm` marketplace may contain or support other plugins, so adding `memory-context-intelligence` there needs a design decision before mutation.
- Prior proof cache/data can be useful evidence, but it must not be mistaken for active installed/enabled state.
- The selected target install ID remains `memory-context-intelligence@darkwingtm`, but current availability under the restored marketplace is unproven and currently not present.

## Rollback notes

Rollback is limited to reverting the v0.1.33 governed documentation correction if selected. Do not mutate plugin install state, settings, marketplace registry, cache, source package runtime contents, or `/additional/` material as phase-028 rollback.

## Next phases

- Phase 029: resolve the shared `darkwingtm` marketplace design without runtime mutation.
- Phase 030: reprove `memory-context-intelligence@darkwingtm` only after phase 029 selects a design and the user explicitly approves any required mutation.
