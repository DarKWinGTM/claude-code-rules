# Phase 043-01 - Reunify Rules plugin source

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 043-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/unified-rules-plugin-rollout.patch.md](../patch/unified-rules-plugin-rollout.patch.md)

---

## Objective

Re-unify the Rules plugin so compact helper behavior and the session coordination skill live together again under `<rules-root>/plugin`.

## Why this phase exists

The user wants the Rules plugin to be one unified Rules-owned package rather than a split topology with duplicate maintained package paths.

## Action points / execution checklist

- [x] restore compact hook/helper files into `plugin/`
- [x] keep `session-coordination-bridge` inside the same package
- [x] update plugin metadata to unified wording
- [x] stop treating split package copies as the intended maintained model

## Out of scope

- creating a second first-class plugin authority
- changing the root runtime rule count
- redefining the underlying compact/post-compact semantics

## Affected artifacts

- `plugin/.claude-plugin/plugin.json`
- `plugin/.claude-plugin/marketplace.json`
- `plugin/hooks/hooks.json`
- `plugin/scripts/*.sh`
- `plugin/skills/session-coordination-bridge/`
- `plugin/README.md`
- `design/rules-plugin-extension.design.md`

## Verification

- [x] compact helper files are present again in the Rules plugin package
- [x] the skill is still present in the same package
- [x] unified package wording is visible in metadata and docs

## Next possible phases

- `043-02` sync governance/install/release surfaces

## Exit criteria

- [x] the Rules plugin is unified again at the source level
- [x] no second maintained package source is required for the intended model
