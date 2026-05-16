# Design - Explanation and Presentation

> **Parent Rule:** [../explanation-and-presentation.md](../explanation-and-presentation.md)
> **Current Version:** 1.1
> **Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835
> **Full history:** [../changelog/explanation-and-presentation.changelog.md](../changelog/explanation-and-presentation.changelog.md)

---

## Target State

`explanation-and-presentation.md` is the active runtime owner for plain-language explanation, scan-friendly presentation, diagram discipline, and concise action framing.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for answer presentation, explanation quality, no-frame diagrams, and response closing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for plain-language explanation, visible intent-read response shapes, root-cause walkthroughs, and concise action framing.

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
