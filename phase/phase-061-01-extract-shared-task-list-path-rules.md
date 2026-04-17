# Phase 061-01 - Extract shared-task-list-path rules

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 061-01
> **Status:** Completed
> **Design References:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../../PLUGIN/claude-session-coordination/design/shared-task-list-path-coordination.design.md](../../PLUGIN/claude-session-coordination/design/shared-task-list-path-coordination.design.md)
> **Patch References:** none

---

## Objective

Finish the Main RULES sync so current RULES surfaces keep only the global task-list doctrine while shared-task-list-path semantics defer cleanly to the plugin-owned rule source.

## Why this phase exists

After the plugin-owned rule chain was created, Main RULES still had current-surface wording that implied an active reduced plugin shell or pointed readers toward `RULES/plugin` artifacts that had already been removed.
This phase closes that last current-surface drift without deleting the older historical rollout records.

## Action points / execution checklist

- [x] remove current-surface references that still point at `plugin/README.md` or `RULES/plugin`
- [x] rewrite current boundary docs so `claude-session-coordination` is the active coordination package/runtime owner
- [x] reframe the former RULES plugin-extension design chain as historical context only
- [x] keep older plugin-topology phase/patch history readable without teaching it as the current topology

## Out of scope

- deleting historical phase/patch/changelog records
- implementing the future export/sync mechanism for plugin-owned rule source
- package-runtime verification inside `claude-session-coordination`

## Affected artifacts

- `README.md`
- `design/design.md`
- `design/rules-plugin-extension.design.md`
- `checkpoint.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `changelog/rules-plugin-extension.changelog.md`

## Verification

- [x] current root/design/checkpoint surfaces no longer point readers to an active `RULES/plugin` shell
- [x] current active surfaces describe `claude-session-coordination` as the active coordination runtime/package owner
- [x] Main RULES current surfaces now keep only the global doctrine while shared-path-specific semantics defer to the plugin-owned rule source
- [x] older plugin-topology history remains preserved as history only

## Exit criteria

- [x] current RULES surfaces no longer imply an active local plugin shell
- [x] Main RULES shared-task extraction cleanup is complete enough for final consistency audit work
