# Design - Coding Discipline

> **Parent Rule:** [../coding-discipline.md](../coding-discipline.md)
> **Current Version:** 1.2
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/coding-discipline.changelog.md](../changelog/coding-discipline.changelog.md)

---

## Target State

`coding-discipline.md` is the active runtime owner for maintainable code structure, proportionate verification, and tactical-to-strategic convergence.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for responsibility boundaries, helper/comment discipline, behavior-preserving refactor, debug/test depth, and tactical convergence.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for maintainable code structure, proportionate verification, coding/debug root-cause narrowing, and tactical-to-strategic convergence.

P138 refinement: this owner should now require semantic/domain/behavior-first identifiers and bounded governed-doc source-comment linkage, so source names and comments explain implementation meaning without turning comments into duplicate documentation or stale governance pointers.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Preserve semantic/domain/behavior-first naming as coding-time clarity doctrine rather than documentation ceremony.
- Keep governed-doc citations in source comments bounded to useful purpose, process, constraint, side-effect, or external-contract pointers.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
