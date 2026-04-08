# Phase 018-02 - Sync plugin docs and verify compact handoff lifecycle

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 018-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md](../patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md)

---

## Objective

Synchronize root/package docs for Wave 018 and verify the new compact handoff lifecycle with real runtime checks.

## Why this phase exists

The plugin lifecycle change only stays low-confusion if package docs, root governance surfaces, and live verification all teach the same rules-first / plugin-second / ephemeral-handoff-only model.

## Action points / execution checklist

- [x] update `plugin/README.md`
- [x] update `design/rules-plugin-extension.design.md`
- [x] update `changelog/rules-plugin-extension.changelog.md`
- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] update/reload the installed plugin
- [x] verify active-handoff creation, consume/delete behavior, bounded SessionStart proof creation, and prune behavior with real runtime checks

## Verification

- package/root docs agree on the `active-handoff.json` + `last-sessionstart-consumed.json` lifecycle
- docs no longer teach the old latest-witness contract as active behavior
- live plugin runtime checks confirm create → consume/delete → bounded proof → prune behavior in both temporary and real plugin-data paths
- compact `SessionStart` now splits outputs along the officially verified boundary: user-visible `systemMessage` for the compact-resume line plus `hookSpecificOutput.additionalContext` for the re-anchor reminder, without duplicating the signal line inside the reminder context
- the source package metadata/docs are synchronized to v1.1.1 and the install/update docs now use the `rules-compact-extension@darkwingtm` identifier shape

## Exit criteria

- Wave 018 is visible and coherent across package docs, root governance surfaces, and runtime verification notes
- the plugin companion remains clearly support-only and subordinate to root RULES authority
- the active package contract is now ephemeral handoff state plus bounded SessionStart consumed proof rather than latest witness storage
