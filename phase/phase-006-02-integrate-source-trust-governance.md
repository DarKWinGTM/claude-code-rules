# Phase 006-02 - Integrate source-trust governance

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 006-02
> **Status:** In Progress
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md), [../design/zero-hallucination.design.md](../design/zero-hallucination.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md)
> **Patch References:** [../patch/external-verification-and-source-trust.patch.md](../patch/external-verification-and-source-trust.patch.md)

---

## Objective

Integrate the new chain into the adjacent RULES governance surfaces without blurring existing ownership boundaries.

## Why this phase exists

A new first-class rule is not sufficient by itself. The surrounding repository model, README, TODO, phase summary, and adjacent owners must acknowledge where the new chain begins and where adjacent chains still retain authority.

## Design Extraction

- Source requirement: one chain should own external verification and source trust while adjacent chains remain intact
- Derived execution work: patch integration references, inventory, README, changelog, TODO, and phase summary
- Target outcome: the repository now teaches the new chain coherently

## Reviewer Checklist

- [ ] master design inventory includes the new chain
- [ ] README inventory and explanation include the new chain
- [ ] master changelog records the rollout
- [ ] TODO tracks the rollout cleanly
- [ ] phase summary records the new 006 family
- [ ] adjacent chains are only integrated narrowly rather than rewritten broadly

## Verification

- repo-level docs reflect the new chain clearly
- no adjacent chain loses its primary authority unnecessarily
- the new phase family is visible in the RULES phase workspace

## Exit Criteria

- master design synced
- README synced
- TODO synced
- master changelog synced
- phase/SUMMARY synced
- rollout family `006` visible and coherent
