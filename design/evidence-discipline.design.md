# Design - Evidence Discipline

> **Parent Rule:** [../evidence-discipline.md](../evidence-discipline.md)
> **Current Version:** 1.6
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/evidence-discipline.changelog.md](../changelog/evidence-discipline.changelog.md)

---

## Target State

`evidence-discipline.md` is the active runtime owner for verify-first factual discipline, burden-of-proof boundaries, scoped non-findings, and real-vs-mock behavior.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for zero hallucination, no variable guessing, anti-mockup, and evidence-grounded burden of proof.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on former root files.

P098 refinement: this owner must now also preserve target-state doctrine for verify-first factual discipline, root-cause evidence thresholds, claim-state separation, and real-vs-mock boundaries.

P101 refinement: this owner should now treat user concern as prioritization input rather than factual proof and require explicit assumption handling when a design or recommendation depends on an unverified premise.

P117 refinement: this owner should now make the presentation boundary explicit: evidence semantics, proof thresholds, and claim-state distinctions stay here, while human-facing grouping/labels for verified fact, inference, and hypothesis defer to the communication/presentation owners.

P120 refinement: this owner should now keep correction scope as an evidence-earned conclusion rather than an early convenience assumption, preserve logic-first reasoning before local scope narrowing, and allow local exceptions only when checked evidence supports a real local doctrine difference.

P146 refinement: this owner should require two-sided migration proof—positive target behavior/selection evidence plus proportionate negative former-path inactivity and discovery evidence—while preserving `NOT_FOUND_IN_CHECKED_SCOPE` versus `STRONG_ABSENCE_CLAIM` and rejecting target tests, file movement, or one grep as migration-complete proof.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact 19-Rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
