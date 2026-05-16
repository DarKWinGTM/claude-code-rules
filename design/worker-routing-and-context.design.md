# Design - Worker Routing and Context Control

> **Parent Rule:** [../worker-routing-and-context.md](../worker-routing-and-context.md)
> **Current Version:** 1.1
> **Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835
> **Full history:** [../changelog/worker-routing-and-context.changelog.md](../changelog/worker-routing-and-context.changelog.md)

---

## Target State

`worker-routing-and-context.md` is the active runtime owner for leader-context protection, worker routing, custom-agent selection, and document-density control.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for native worker routing, custom agent priority, context-load control, and God-line/God-document routing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for intent taxonomy, routing implications, diagnosis-first mixed-intent handling, and context-safe worker selection.

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
