# Init configuration surface patch

> **Current Version:** 0.1.77
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-02)
> **Status:** active review artifact
> **Target Design:** [../design/09-init-configuration-surface.design.md](../design/09-init-configuration-surface.design.md)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

The plugin already had a shared config-policy reader, but setup was indirect and project-local by default. This patch introduces a dedicated public setup surface and moves the default config target to the user-scope Claude runtime directory.

## Analysis

Before:
- no `/memory-context-intelligence:init`
- guided config helper lived only inside `/analysis`
- default config discovery/suggested path was project-local/upward-discovered

After:
- `/memory-context-intelligence:init` exists as the setup/config surface
- the shared config contract now carries `analysis.scope_policy`
- the default config target is `~/.claude/memory-context-intelligence.config.json`
- stored default scope affects analysis only when the operator did not explicitly narrow the run

## Change items

- add init skill surface
- extend config-policy helpers and write/update behavior
- switch default config location to user scope
- expose `scope_policy` in runtime payloads
- sync README/design/phase/changelog surfaces

## Verification

Use the focused init-wave tests plus the full package suite and one checked local init-flow proof with one checked analysis config-consumption proof.

## Rollback approach

Rollback by reverting the init skill, the scope-policy contract additions, and the user-scope config default selection together; do not leave analysis consuming a config shape that the setup surface no longer writes.
