# Phase 064-01 - Retire memsearch custom-skill and bridge doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 064-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/design.md](../design/design.md), [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/retire-memsearch-custom-skill-and-bridge-doctrine.patch.md](../patch/retire-memsearch-custom-skill-and-bridge-doctrine.patch.md)

---

## Objective

Retire discontinued memsearch custom-skill doctrine and the former `session-coordination-bridge` path from Main RULES active teaching while preserving bounded historical records.

## Why this phase exists

The local RULES plugin shell no longer exists, the former bridge skill is not actually usable from this repo now, and the user is discontinuing their custom memsearch skill development. Main RULES should not keep teaching those paths as current capability.

## Action points / execution checklist

- [x] remove memsearch-specific custom-skill naming from active Main RULES doctrine
- [x] replace stale coordination defers with direct out-of-scope wording
- [x] reframe historical index surfaces so bridge/memsearch waves read as retired history only
- [x] preserve detailed historical artifacts without promoting them as current capability
- [x] synchronize touched design/changelog/master surfaces

## Verification

- [x] no active Main RULES doctrine still teaches a memsearch-specific custom-skill path
- [x] no active Main RULES doctrine still teaches `session-coordination-bridge` as a usable path
- [x] retired plugin/skill references in index surfaces are framed as history only

## Exit criteria

- [x] Main RULES active doctrine no longer implies support for retired custom skills or a nonexistent local plugin shell
- [x] the bounded historical record remains readable without reading like current capability
