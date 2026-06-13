# Design - Goal Authoring and Route Support

> **Parent Rule:** [../goal-authoring-and-route-support.md](../goal-authoring-and-route-support.md)
> **Current Version:** 1.0
> **Session:** 8b04beb0-b5ef-4500-a3f5-558bcedd088a
> **Full history:** [../changelog/goal-authoring-and-route-support.changelog.md](../changelog/goal-authoring-and-route-support.changelog.md)

---

## Target State

`goal-authoring-and-route-support.md` is the active runtime owner for governed `/goal` authoring, route-support extraction, `Plan reference` discipline, and selected-goal overflow handling into `/plan`.

It separates detailed goal-authoring doctrine from execution continuity and phase/task shaping so the runtime layer can stay compact without duplicating the same `/goal` contract across several root rules.

---

## Scope

This design owns the target-state shape for:
- plain governed goal request handling
- governed-surface sourcing order for `/goal`
- bounded goal artifact construction
- smallest-sufficient route support
- durable `Plan reference` validity
- subordinate internal helper / route-support behavior
- goal-authoring stop boundaries
- advisory `/goal` promotion conditions
- selected-goal overflow into `/plan`
- `/goal` versus `/plan` authority separation

---

## Runtime Requirements

- Keep `/goal` as the objective owner for outcome, proof/checks, scope, and hard guardrails.
- Keep `/plan` as route-only support when overflow route detail or explicit standalone planning is materially needed.
- Preserve direct continuation when one safe execution path is already implied; do not force `/goal` or `/plan` as ritual surfaces.
- Keep route-only plan files from reading like completion proof.
- Keep phase/task materialization and execution posture outside this owner.
- Keep metadata linked to this design and the chain changelog.

---

## Boundaries

This design does not own discussion-versus-execution mode selection, continuous execution, or next-goal bridge logic; those remain with `execution-and-goal-frame.md`.

It does not own startup artifact posture, phase/TODO linkage, or live task materialization; those remain with `phase-todo-artifact.md`.

Historical detail remains in changelog, not as a parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, links to this design and its changelog, ships in the active runtime install set when install is in scope, and leaves `execution-and-goal-frame.md` plus `phase-todo-artifact.md` with only their execution/task-surface bridges instead of the full duplicated `/goal` authoring contract.
