# Design - Evidence Discipline

> **Parent Rule:** [../evidence-discipline.md](../evidence-discipline.md)
> **Current Version:** 1.2
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/evidence-discipline.changelog.md](../changelog/evidence-discipline.changelog.md)

---

## Target State

`evidence-discipline.md` is the active runtime owner for verify-first factual discipline, burden-of-proof boundaries, scoped non-findings, and real-vs-mock behavior.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for zero hallucination, no variable guessing, anti-mockup, and evidence-grounded burden of proof.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for verify-first factual discipline, root-cause evidence thresholds, claim-state separation, and real-vs-mock boundaries.

P101 refinement: this owner should now treat user concern as prioritization input rather than factual proof and require explicit assumption handling when a design or recommendation depends on an unverified premise.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
