# Phase 018 - Main RULES merge closeout

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 018
> **Status:** Planned / Deferred
> **Design References:** [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

If the user selects promotion, perform the governed main RULES merge and close out the capsule promotion path.

## Why this phase exists

Main RULES merge is a separate governed action. It must update the correct owner surfaces, preserve version/changelog/design alignment, and avoid treating the capsule or `/additional/` layer as permanent competing authority.

## Goal

Move a proven additional-stage rule into the selected main RULES owner chain, or close with a documented no-merge outcome.

## Output

- governed main RULES design/runtime/changelog/TODO/phase or patch updates as required by the selected owner chain
- removal, retirement, or continued-trial decision for the `/additional/` rule
- closeout note for the capsule phase program
- verification record for source/runtime parity if a runtime RULES install is part of the selected merge path

## Gate

The phase is complete when the selected merge or no-merge outcome is documented, required governed surfaces are synchronized, and `/additional/` no longer silently competes with the main owner chain.

## Owner

Main RULES governance owner, with explicit user selection and normal RULES release/verification gates.

## Files

Future implementation may touch main RULES governed documents and runtime rule files only after user-selected promotion. This documentation pass does not touch those implementation/runtime files.

## Verification

- verify selected main RULES owner chain before editing
- verify governed design/changelog/runtime/TODO/phase/patch sync as applicable
- verify `/additional/` trial rule status after merge or no-merge closeout
- verify runtime install/source parity only if the selected merge includes runtime install work

## Risks / rollback notes

The risk is creating two active authorities for the same doctrine. Rollback must follow the main RULES destructive/rollback gates and preserve enough history to explain whether the trial was merged, retained, revised, or retired.
