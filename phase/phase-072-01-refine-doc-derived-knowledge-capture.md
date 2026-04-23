# Phase 072-01 - Refine doc-derived knowledge capture

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 072-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/document-design-control.design.md](../design/document-design-control.design.md), [../design/document-patch-control.design.md](../design/document-patch-control.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/doc-derived-knowledge-capture-refinement.patch.md](../patch/doc-derived-knowledge-capture-refinement.patch.md)

---

## Objective

Refine the existing owner set so implementation-critical knowledge learned from docs/specs/provider references is captured in governed artifacts before or alongside later multi-step work that still depends on it.

## Why this phase exists

The current document system already separates design, phase, patch, TODO, and changelog roles, but it still leaves one dangerous gap in practice:
- assistant reads docs/specs correctly
- uses the knowledge in the current turn
- but does not always normalize the implementation-relevant truth into governed artifacts before later execution continues
- once compact or handoff happens, that knowledge may drop out of the active working context and force unnecessary re-reading

This wave closes that gap without collapsing document roles together:
- design should own extracted implementation truth
- phase should carry the execution consequence of that truth
- patch should surface the external-requirement basis when review depends on it
- execution continuity should stop for capture before later work keeps relying on transient doc-reading memory

## Action points / execution checklist

- [x] refine `document-design-control` so doc-derived implementation truth must be captured in design when later work still depends on it
- [x] refine `phase-implementation` so later execution reuses normalized design truth rather than transient doc-reading memory
- [x] refine `document-patch-control` so externally driven change basis stays visible enough for review
- [x] refine `execution-continuity-and-mode-selection` so capture-before-continue becomes explicit when implementation-critical external knowledge has not yet been externalized
- [x] synchronize master/history surfaces for the bounded wave

## Verification

- [x] doc-derived implementation truth now has an explicit governed home in design
- [x] later phased execution now points back to normalized design truth when external docs/specs materially constrain the work
- [x] externally driven patch rationale now stays visible enough for review
- [x] execution continuity now includes a capture-before-continue boundary for implementation-critical external knowledge
- [x] touched master/history surfaces record the wave coherently

## Exit criteria

- [x] the owner set now expresses doc-derived knowledge capture without inventing a new first-class documentation stack
- [x] the document system now preserves implementation-relevant extracted truth more reliably across compact/handoff boundaries
