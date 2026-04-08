# Phase 021-02 - Tighten additionalContext to reference-first form

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 021-02
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-reference-first-review-trigger-refinement.patch.md](../patch/compact-reference-first-review-trigger-refinement.patch.md)

---

## Objective

Reduce compact SessionStart `additionalContext` to instruction + locator + bounded status only.

## Why this phase exists

The user wants compact resume to remain reference-first and not drift into a hidden context-restore channel that silently re-expands old summary content back into Claude.

## Action points / execution checklist

- [x] remove direct injection of carried-forward objective/basis/item text blocks from `additionalContext`
- [x] keep one short review-required instruction
- [x] keep review directory and review file pointers
- [x] keep one short objective-status line
- [x] keep one short discipline reminder against replay-based continuation
- [x] keep fallback `additionalContext` equally bounded

## Verification

- success-path `additionalContext` contains no long carried-forward summary block
- success-path `additionalContext` still points to the exact review files
- fallback `additionalContext` points to `index.json`
- the compact review model remains reference-first rather than replay-first

## Exit criteria

- additionalContext is bounded, review-oriented, and no longer acts like a summary replay channel
