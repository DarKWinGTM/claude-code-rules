# Phase 006-01 - Create external verification rule

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 006-01
> **Status:** Implemented - Pending Review
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md)
> **Patch References:** [../patch/external-verification-and-source-trust.patch.md](../patch/external-verification-and-source-trust.patch.md)

---

## Objective

Create the first-class rule chain that owns proactive external verification and source-trust workflow.

## Why this phase exists

The current stack already has strong anti-hallucination and burden-of-proof behavior, but it does not yet have one semantic owner for external source ranking, corroboration expectations, proactive web verification triggers, and source-conflict handling.

## Design Extraction

- Source requirement: external factual verification should become more proactive, more source-aware, and more accurate
- Derived execution work: create the new design/runtime/changelog triad and patch artifact
- Target outcome: one durable owner exists for external verification and source trust

## Reviewer Checklist

- [x] new design file exists
- [x] runtime rule exists
- [x] changelog authority exists
- [x] patch artifact exists
- [x] chain scope is distinct from zero-hallucination, burden-of-proof, communication, and failure-handling owners

## Verification

- new chain exists as a governed triad
- patch artifact shows before/after governance need clearly
- source-trust workflow is now defined in one place

## Exit Criteria

- `design/external-verification-and-source-trust.design.md` exists
- `external-verification-and-source-trust.md` exists
- `changelog/external-verification-and-source-trust.changelog.md` exists
- `patch/external-verification-and-source-trust.patch.md` exists
