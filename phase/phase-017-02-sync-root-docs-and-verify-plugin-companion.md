# Phase 017-02 - Sync root docs and verify plugin companion

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 017-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/rules-plugin-extension-companion.patch.md](../patch/rules-plugin-extension-companion.patch.md)

---

## Objective

Synchronize root governance surfaces for the plugin companion wave and verify that the new package remains support/extension-only.

## Why this phase exists

The plugin companion only stays low-confusion if the root role model, README install guidance, master changelog, TODO, and phase summary all teach the same rules-first / plugin-second boundary.

## Action points / execution checklist

- [x] update `project-documentation-standards` design/runtime/changelog
- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] verify `plugin/` package metadata and hook files are coherent
- [x] expand plugin installation and hook-behavior documentation in root/package docs

## Verification

- plugin install and update flow is documented in enough detail for package-root use
- plugin docs explain SessionStart / PreCompact / PostCompact behavior and duplicate-hook-path troubleshooting
- root docs do not imply plugin authority replaces root RULES

## Exit criteria

- root governance surfaces and plugin package structure are aligned
- the plugin companion is visible, documented, and clearly subordinate to root RULES authority
- the `017` phase family is visible and reviewable from `phase/SUMMARY.md`
