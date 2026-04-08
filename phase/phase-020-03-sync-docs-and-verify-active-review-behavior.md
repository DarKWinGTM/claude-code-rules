# Phase 020-03 - Sync docs and verify active review behavior

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 020-03
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md](../patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md)

---

## Objective

Synchronize package/root governance docs and verify that the active review-trigger behavior is reflected consistently after the hook change.

## Why this phase exists

The RULES source package, shared bridge package, and master governance artifacts need to describe the new review-trigger semantics clearly enough that the runtime behavior is reviewable and not mistaken for another passive status refinement.

## Action points / execution checklist

- [x] update plugin/package docs to describe the active review-trigger behavior
- [x] update design/changelog/master docs to record the Wave 020 refinement
- [x] update TODO and phase summary to reflect the completed wave
- [x] bump source and bridge package metadata so the installed runtime can pick up the new behavior
- [x] verify syntax of both SessionStart hook scripts
- [x] verify synthetic success-path output shows explicit review-before-continuation wording plus exact file pointers

## Verification

- source and bridge SessionStart scripts pass shell syntax check
- synthetic success-path output shows the active review trigger wording
- docs and version surfaces describe the review-trigger refinement consistently
- master changelog/TODO/phase summary all record the Wave 020 completion

## Exit criteria

- code, package docs, and governance docs describe the same active review-trigger behavior
- source and bridge package metadata are aligned to the new version
- Wave 020 is visible in patch/phase/changelog/TODO/master summary surfaces
