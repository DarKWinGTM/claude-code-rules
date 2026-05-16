# Design - Execution and Goal Frame

> **Parent Rule:** [../execution-and-goal-frame.md](../execution-and-goal-frame.md)
> **Current Version:** 1.2
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/execution-and-goal-frame.changelog.md](../changelog/execution-and-goal-frame.changelog.md)

---

## Target State

`execution-and-goal-frame.md` is the active runtime owner for discussion/execution mode selection, continuous execution, goal framing, and next-work boundaries.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for execution continuity, goal-set review, priority balance, and completion-to-next-goal framing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for discussion/execution mode selection, visible intent read, selective clarification, repair re-anchor, and next-work boundaries.

P099 refinement: this owner must now also preserve broad-objective decomposition before deep execution, worker-fit next-lane continuation, and lane-aware continuation boundaries while keeping delegation and read/output control with `worker-routing-and-context.md` and `safe-io.md`.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Preserve lane decomposition and next-lane continuation semantics without taking delegation or bounded-I/O ownership away from `worker-routing-and-context.md` and `safe-io.md`.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
