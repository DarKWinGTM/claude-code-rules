# Phase 056-01 - Reduce RULES plugin active scope

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 056-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/rules-plugin-coordination-scope-reduction.patch.md](../patch/rules-plugin-coordination-scope-reduction.patch.md)

---

## Objective

Reduce the active RULES plugin package so it no longer claims full active ownership of the coordination runtime while the new coordination package is being prepared.

## Why this phase exists

The checked package still contains compact behavior plus coordination runtime in one package source. This phase records the start of scope reduction so later cutover can remove active overlap cleanly.

## Action points / execution checklist

- [x] identify which current package surfaces should move to `claude-session-coordination@darkwingtm`
- [x] identify which current package surfaces should stay in RULES
- [x] reduce active coordination ownership claims further in package manifests/docs/hooks
- [x] leave only the reduced migration/reference package role on the RULES side while active runtime ownership moves out

## Out of scope

- deleting moved files from RULES immediately
- full archive relocation
- final dual-owner shutdown verification

## Affected artifacts

- `plugin/README.md`
- `plugin/hooks/hooks.json`
- `plugin/.claude-plugin/plugin.json`
- `plugin/.claude-plugin/marketplace.json`

## Verification

- [x] RULES package claims only its reduced active role
- [x] moved coordination runtime is no longer presented as actively owned here

## Exit criteria

- [x] active RULES plugin scope is reduced clearly enough for later cutover
