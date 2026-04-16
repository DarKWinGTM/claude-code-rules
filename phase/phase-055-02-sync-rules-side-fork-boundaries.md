# Phase 055-02 - Sync RULES-side fork boundaries

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 055-02
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md), [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md)
> **Patch References:** [../patch/session-coordination-fork-authority-split.patch.md](../patch/session-coordination-fork-authority-split.patch.md)

---

## Objective

Synchronize RULES-side boundary docs so the coordination fork is visible consistently across root/plugin surfaces.

## Why this phase exists

Without surface sync, later readers would still see the old unified plugin story and misread which package owns the active coordination runtime.

## Action points / execution checklist

- [x] update root README to describe the two-package split direction
- [x] update plugin-extension design wording to stop teaching the old unified package as the intended end-state
- [x] keep the split direction visible enough for later migration/archive work

## Out of scope

- active hook cutover
- archive relocation
- release packaging for the new plugin

## Affected artifacts

- `README.md`
- `design/rules-plugin-extension.design.md`
- `phase/SUMMARY.md`
- `TODO.md`
- `changelog/changelog.md`
- `changelog/rules-plugin-extension.changelog.md`

## Verification

- [x] root/plugin/design wording no longer treats the unified package as the stable future target
- [x] split-package install story is visible

## Exit criteria

- [x] RULES-side fork boundary wording is synchronized
