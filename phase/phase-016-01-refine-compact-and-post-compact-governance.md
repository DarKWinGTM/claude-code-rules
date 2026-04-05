# Phase 016-01 - Refine compact and post-compact governance

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 016-01
> **Status:** Completed
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/compact-post-compact-governance-refinement.patch.md](../patch/compact-post-compact-governance-refinement.patch.md)

---

## Objective

Refine the existing communication-owner set so compacted-session continuation re-anchors to the active objective before continuing and does not silently treat compressed-away detail as exact verified truth.

## Why this phase exists

The RULES system already handled continuation-first behavior, evidence thresholds, and compact presentation patterns, but it did not yet express one coherent post-compact contract. This phase closes that gap without creating a new doctrine chain.

## Action points / execution checklist

- [x] update `accurate-communication` as the primary post-compact re-anchor wording owner
- [x] update `authority-and-scope` as the active-objective / active-frame re-anchor owner
- [x] update `evidence-grounded-burden-of-proof` with a post-compact needs-recheck evidence state
- [x] update `explanation-quality` so one short re-anchor is preferred over replaying stale history
- [x] update `answer-presentation` with a compact post-compact re-anchor layout pattern
- [x] keep the refinement bounded and avoid creating a new standalone compact doctrine chain

## Verification

- compacted-session continuation now re-anchors to the active objective before resuming
- compressed-away exact detail is no longer treated as automatically still-verified truth
- stale assistant branches are not revived after compact by default
- explanations and layouts now prefer one short re-anchor over long replay

## Exit criteria

- compact/post-compact behavior is clearly split across wording, authority, burden-of-proof, explanation flow, and presentation ownership
- the refinement remains a bounded owner-set wave rather than a new doctrine chain
- the touched owner set expresses one coherent re-anchor-before-continuation behavior
