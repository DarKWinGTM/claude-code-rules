# Phase 029 - shared darkwingtm marketplace design resolution

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

029

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Resolve how `memory-context-intelligence` should be exposed through the restored shared `darkwingtm` marketplace without mutating runtime state.

## Entry conditions

- phase 028 completed the restored shared-marketplace governance sync
- active runtime mapping is `darkwingtm` -> `<template-plugin-root>`
- the restored shared marketplace does not currently include `memory-context-intelligence`
- `memory-context-intelligence@darkwingtm` is not currently installed/enabled
- phases 025-027 remain historical evidence only, not current runtime truth

## Selected design

Phase 029 selects the smallest viable non-breaking shared-marketplace bridge design:

- keep active runtime marketplace `darkwingtm` mapped to `<template-plugin-root>`
- do not use `<repo-root>/plugin` as the active runtime marketplace root
- later, with explicit approval, add `memory-context-intelligence` as an extra entry inside `<template-plugin-root>/.claude-plugin/marketplace.json`
- the later entry should use source `../RULES/plugin/memory-context-intelligence`
- keep `<template-plugin-root>/memory-context-intelligence/` as deprecated historical docs only, not the active plugin package

## Why this design is selected

This bridge preserves the restored shared `darkwingtm` marketplace while keeping one active source authority for this capsule.

Rejected alternatives:

- remapping `darkwingtm` to `<repo-root>/plugin` is rejected because it would break existing plugins that belong to the restored shared marketplace under `<template-plugin-root>`
- creating a second active `memory-context-intelligence` package under `<template-plugin-root>` is rejected because it would create source drift and duplicate truth; the active source authority remains `<repo-root>/plugin/memory-context-intelligence/`

## Output

Completed output:

- selected shared-marketplace bridge design for `memory-context-intelligence@darkwingtm`
- explicit source-home versus runtime-marketplace boundaries
- preservation rule for other `darkwingtm` plugins by keeping the active marketplace root at `<template-plugin-root>`
- preservation rule for `<template-plugin-root>/memory-context-intelligence/` as deprecated historical docs only
- approval-sensitive phase-030 reproof plan

## Gate

Phase 029 closes because the design is selected and documented. It did not mutate plugin install state, settings, marketplace registry, cache, installed plugins, source package runtime contents, or `/additional/` runtime material.

## Owner

Shared marketplace design-resolution owner.

## Out of scope

- installing or enabling `memory-context-intelligence@darkwingtm`
- editing the shared runtime marketplace registry
- changing plugin cache or installed-plugin registry state
- mutating source package runtime contents
- changing `/additional/` trial-stage behavior
- promoting or merging main RULES

## Verification / closeout

Phase 029 is docs-only verification-in-scope for design selection. It selects the bridge-entry design that phase 030 may later implement after approval.

Still unproven after phase 029:

- current `memory-context-intelligence@darkwingtm` marketplace availability under restored `darkwingtm`
- current `memory-context-intelligence@darkwingtm` install or enablement
- uninstall lifecycle behavior against the restored shared-marketplace bridge design
- publication or external marketplace release
- slash-command/chat invocation proof
- stable/broad production readiness
- main RULES promotion, mutation, or merge

## Rollback notes

Phase 029 is docs-only design work. Rollback should be limited to reverting its governed documentation/design changes unless the user separately approves runtime mutation rollback scope. It must not delete historical evidence, remove retained cache/data, edit the shared marketplace, reinstall/uninstall plugins, or change `/additional/` material.
