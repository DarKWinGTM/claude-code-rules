# Phase 027 - darkwingtm uninstall lifecycle closeout

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

027

## Status

Completed / Historical evidence

## Historical Reclassification

Phase 027 remains valid historical checked evidence from the temporary/remapped `darkwingtm` state. After the runtime marketplace mapping was restored to `darkwingtm` -> `<template-plugin-root>`, this phase no longer represents current target-state proof; retained cache/data from the old proof is evidence only, not active install state.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Close the namespace-aligned install lifecycle by proving the approved uninstall-only behavior for `memory-context-intelligence@darkwingtm` after phase 026 created a checked local-scope darkwingtm install state.

## Why this phase exists

Phase 023 proved uninstall-only behavior only for `memory-context-intelligence@rules-local`. Phase 026 later installed `memory-context-intelligence@darkwingtm`, so the lifecycle closeout had to verify the corresponding darkwingtm uninstall path rather than inheriting the transitional rules-local closeout.

## Goal

Remove the local installed/enabled entry for `memory-context-intelligence@darkwingtm` under explicit uninstall-only approval while preserving marketplace registration, source package, governed docs, cache/data retained by `--keep-data`, and `/additional/` material.

## Output

Completed output:

- approval-sensitive uninstall-only command and output for `memory-context-intelligence@darkwingtm`
- post-uninstall checks showing the installed plugin absent from normal and bare plugin lists
- post-uninstall details check showing `memory-context-intelligence@darkwingtm` not found
- darkwingtm marketplace registration intentionally retained
- local enablement removed from `<workspace-root>/.claude/settings.local.json`
- global installed-plugin registry entry removed from `<user-claude-root>/plugins/installed_plugins.json`
- cache path `<user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0` retained after `--keep-data` and marked with `.orphaned_at`
- source package and `/additional/` material preserved
- clear boundary that publication, external marketplace release, slash-command/chat invocation, stable/broad production readiness, main RULES promotion/mutation/merge, and unrelated darkwingtm plugin mismatch repair remain unproven or out of scope

## Gate

Completed after phase 026 produced checked local install visibility and after the user explicitly approved the uninstall-only proof path.

## Owner

Install lifecycle closeout owner.

## Files

Updated closeout docs:

- `phase/SUMMARY.md`
- this phase file
- `design/06-plugin-installability.design.md`
- `design/design.md`
- `README.md`
- `skills/memory-context-intelligence/SKILL.md`
- `changelog/changelog.md`
- `changelog/v0.1.32-completed-darkwingtm-install-lifecycle-closeout.changelog.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md`

## Verification

Verification route: approval-gated `smoke_check`.

Ran from `<workspace-root>`:

```bash
claude plugin uninstall --scope local --keep-data "memory-context-intelligence@darkwingtm"
claude plugin marketplace list --json
claude plugin list --json
claude --bare plugin list --json
claude --bare plugin details "memory-context-intelligence@darkwingtm"
```

Command result:

```text
✔ Successfully uninstalled plugin: memory-context-intelligence (scope: local)
```

Post-uninstall CLI evidence:

- `claude plugin marketplace list --json` still includes `darkwingtm` as a directory marketplace with path and install location `<repo-root>/plugin`.
- `claude plugin list --json` does not include `memory-context-intelligence@darkwingtm`.
- `claude --bare plugin list --json` does not include `memory-context-intelligence@darkwingtm`.
- `claude --bare plugin details "memory-context-intelligence@darkwingtm"` exited `1` with `Plugin "memory-context-intelligence@darkwingtm" not found. Run `claude plugin list` to see installed plugins, or pass --plugin-dir <path> to load one from disk.`

Post-uninstall file/state evidence:

- `<workspace-root>/.claude/settings.local.json` contains no `memory-context-intelligence` reference and has no memory plugin matches in permissions allow/deny/ask.
- `<user-claude-root>/plugins/installed_plugins.json` no longer has the key `memory-context-intelligence@darkwingtm`.
- `<user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0` remains present after `--keep-data`; `.orphaned_at` exists with value `1779155486899`.
- `<repo-root>/plugin/memory-context-intelligence/` remains present, including `.claude-plugin/` and `skills/memory-context-intelligence/SKILL.md`.
- `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md` remains present.

## Risks closed

- The phase no longer assumes rules-local uninstall evidence applies to darkwingtm uninstall.
- The installed/enabled state is absent after uninstall, while retained cache/data is documented separately as retained `--keep-data` cache.
- Source package, governed docs, marketplace registration, and `/additional/` material were not deleted.
- Existing unrelated darkwingtm plugin mismatch errors were observed in plugin-list output but not repaired in this phase.

## Rollback notes

Phase 027 intentionally performed only the approved uninstall-only closeout. Reinstalling `memory-context-intelligence@darkwingtm`, removing the retained darkwingtm marketplace registration, deleting retained cache/data, deleting source package files, deleting governed docs, or changing `/additional/` material would be separate approval-sensitive work.
