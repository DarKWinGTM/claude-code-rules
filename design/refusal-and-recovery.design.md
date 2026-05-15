# Design - Refusal and Recovery Chain

> **Parent Rule:** [../refusal-and-recovery.md](../refusal-and-recovery.md)
> **Current Version:** 1.0
> **Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3
> **Full history:** [../changelog/refusal-and-recovery.changelog.md](../changelog/refusal-and-recovery.changelog.md)

---

## Target State

`refusal-and-recovery.md` is the active runtime owner for wrapper normalization, refusal classification, refusal minimization, and actionable recovery paths.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for DAN-safe normalization, refusal classification, refusal minimization, and recovery contract.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

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
