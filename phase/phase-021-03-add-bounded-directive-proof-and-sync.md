# Phase 021-03 - Add bounded directive proof and sync docs

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 021-03
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-reference-first-review-trigger-refinement.patch.md](../patch/compact-reference-first-review-trigger-refinement.patch.md)

---

## Objective

Add bounded proof for the emitted review directive and synchronize docs/version surfaces to the reference-first compact review model.

## Why this phase exists

The user wants proof of what directive was emitted, but without storing another full context replay payload. This phase adds a bounded directive-proof file and keeps docs/governance aligned with the tightened implementation.

## Action points / execution checklist

- [x] add `sessionstart-directive.json` as bounded directive proof
- [x] include review targets, short directive text, and status counts only
- [x] expose `hasDirective` in the compact index
- [x] sync docs/changelog/TODO/phase/patch surfaces to the new reference-first model
- [x] verify source and bridge runtime parity

## Verification

- `sessionstart-directive.json` is created on SessionStart handling
- directive proof remains bounded and does not store long old-context replay text
- docs and version surfaces match the new reference-first review-trigger model

## Exit criteria

- compact review trigger has visible review-required wording, bounded reference-first additionalContext, and bounded directive proof
