# Phase 031 - supported active runtime package exposure design

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

031

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Select a supported docs-only runtime exposure design for `memory-context-intelligence@darkwingtm` after the phase-030 shared-marketplace bridge failed, without remapping the shared marketplace away from `<template-plugin-root>` and without relying on unsupported path traversal outside the marketplace base.

## Why this phase exists

Phase 029 selected a shared-marketplace bridge entry. Phase 030 proved that selected bridge is blocked in implementation: adding `memory-context-intelligence` inside `<template-plugin-root>/.claude-plugin/marketplace.json` with source `../RULES/plugin/memory-context-intelligence` made the plugin appear in available plugin output, but install failed because Claude Code rejected the outside-base source as unsupported / path traversal.

Because of that blocker, the next supported design is not another bridge-entry install attempt. Phase 031 selects a governed export/projection model that keeps source authority in the RULES plugin capsule while exposing a runtime-facing package inside the supported `darkwingtm` marketplace base later.

## Selected supported runtime exposure design

The selected docs-only design is:

- active runtime marketplace remains `darkwingtm` -> `<template-plugin-root>`
- checked local active runtime marketplace base remains `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/`
- future runtime-facing package path should be `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/`
- that runtime-facing path is not a second source of truth
- the runtime-facing path is a governed export/projection/runtime-facing artifact generated from or synced from `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`
- active source authority remains `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`
- drift prevention must come from governed sync/export rules, version alignment, and later reproof, not manual independent maintenance under `TEMPLATE/PLUGIN`

พูดง่าย ๆ: ตัวจริงที่แก้คือ `RULES/plugin/memory-context-intelligence/`; ส่วน `TEMPLATE/PLUGIN/memory-context-intelligence/` เป็น package หน้า runtime ที่ค่อยสร้างหรือ sync ทีหลัง เพื่อให้ marketplace โหลดได้แบบ supported.

## Rejected alternatives

Phase 031 explicitly rejects these alternatives:

- remapping `darkwingtm` to `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/` because it breaks other plugins that belong to the shared `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/` marketplace
- using a bridge entry with source `../RULES/plugin/memory-context-intelligence` because phase 030 proved Claude Code rejects that outside-base source as unsupported / path traversal during install
- treating `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/` as an independent manually maintained package because that creates source drift and duplicate truth

## Expected output

Phase 031 produces docs-only governed design selection. It does not create or update the runtime-facing package, marketplace registry, install state, settings, cache, source runtime contents, or `/additional/` material.

## Entry conditions

- phase 030 is recorded as blocked, not completed
- the failed shared-marketplace bridge entry has been removed from `<template-plugin-root>/.claude-plugin/marketplace.json`
- active runtime marketplace `darkwingtm` remains mapped to `<template-plugin-root>`
- existing shared `@darkwingtm` plugins remain preserved
- phases 020-023 remain transitional `@inline` / `rules-local` evidence
- phases 025-027 remain historical checked evidence from the temporary/remapped `darkwingtm` state
- phase 028 remains completed docs-only restored shared-marketplace governance sync
- phase 029 remains completed docs-only bridge design evidence, now rejected by phase 030 implementation evidence as unsupported
- phase 030 remains blocked implementation evidence

## Gate

Phase 031 closes with docs-only supported exposure design. It does not claim runtime proof by itself.

Phase 032 is the approval-sensitive successor phase. It may proceed only after explicit approval to create or update the runtime-facing package under `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/` and then re-prove availability, install, and uninstall behavior under `darkwingtm`.

## Owner

Supported runtime exposure design owner.

## Out of scope

- editing the shared runtime marketplace registry as part of phase 031
- creating or updating `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/` as part of phase 031
- installing or enabling `memory-context-intelligence@darkwingtm`
- uninstalling plugins
- remapping `darkwingtm` away from `<template-plugin-root>`
- relying on unsupported `../RULES/plugin/memory-context-intelligence` path traversal
- manually maintaining a second independent source package under `TEMPLATE/PLUGIN`
- mutating source package runtime contents
- mutating `/additional/` trial-stage behavior
- publication or external marketplace release
- slash-command/chat invocation proof
- stable/broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Verification / closeout

Phase 031 verification is documentation/design verification only:

- the selected exposure model is documented in the installability design shard
- source-of-truth and drift-prevention boundaries are explicit
- rejected alternatives are explicit
- later phase 032 mutation and verification gates are explicit and approval-sensitive
- phase 029 remains historical docs-only bridge design evidence but is no longer the selected supported implementation path
- phase 030 remains blocked rather than reclassified as completed
- existing shared `@darkwingtm` plugin preservation remains a boundary
- no new runtime install, uninstall, cache, marketplace, settings, source package, runtime-facing package, or `/additional/` mutation is claimed by phase 031

## Rollback notes

Phase 031 rollback is limited to reverting its governed documentation/design changes unless the user separately approves runtime mutation rollback scope. Because phase 031 is docs-only design work, rollback must not delete historical proof files, retained cache/data, source package files, existing shared marketplace plugins, a future runtime-facing projection package, or `/additional/` material.
