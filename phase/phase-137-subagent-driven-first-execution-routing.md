# P137 — Subagent-Driven-First Execution Routing

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P137
> **Status:** Completed / Released
> **Target Release:** v10.45
> **Design References:**
> - [../design/worker-routing-and-context.design.md](../design/worker-routing-and-context.design.md) v1.13
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.21
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.25
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.18
> **Patch References:** [../patch/subagent-driven-first-execution-routing.patch.md](../patch/subagent-driven-first-execution-routing.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make selected, execution-ready, non-trivial plan-backed or goal-backed work prefer Subagent-Driven execution first, while preserving Inline Execution as a checked suitability exception when more effective.

---

## Why This Phase Exists

Current doctrine already has most building blocks:
- `/goal` remains objective owner
- plan files remain route-only support
- worker-routing already owns subagent topology and leader verification
- phase/todo already owns live task shaping for non-trivial work

But one workflow gap still remains:
- selected execution can still surface `Subagent-Driven` vs `Inline Execution` like a default choice instead of deciding the more suitable mode directly
- Subagent-Driven is not yet the explicit preferred default for selected non-trivial plan/goal execution
- Inline Execution exceptions are not yet normalized as checked suitability-based fallbacks

P137 exists to harden that exact execution-default behavior:
- system decides execution posture when selected work is execution-ready
- Subagent-Driven is preferred first for worker-suitable non-trivial work
- Inline stays valid only as a checked direct-handling exception
- goal/plan authority split stays intact

---

## Expected Output

- `execution-and-goal-frame.md` makes selected plan/goal execution posture automatic rather than a default option menu
- `worker-routing-and-context.md` defines the Subagent-Driven-first topology preference and Inline exceptions
- `phase-todo-artifact.md` materializes selected non-trivial plan/goal execution into bounded tasks before deep continuation
- `communication-register.md` removes the ordinary need to surface execution-mode choice prompts and preserves visible reasons for Inline exceptions
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.45 / P137`
- touched runtime rules are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check`, push/update to `master`, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Add the execution-default trigger in `execution-and-goal-frame.md`.
- [x] Add the Subagent-Driven-first topology preference and Inline exception handling in `worker-routing-and-context.md`.
- [x] Add selected execution task materialization guidance in `phase-todo-artifact.md`.
- [x] Add communication wording so execution-mode choice prompts are not surfaced by default when the system can decide suitability directly.
- [x] Sync touched design and per-chain changelog surfaces.
- [x] Sync touched README/TODO/phase/patch/master-changelog surfaces.
- [x] Install/update the touched runtime rules and verify source/runtime parity + body sufficiency.
- [x] Publish the selected scope safely without bundling unrelated dirty repo state.
- [x] Verify the pushed commit, `master` update, and GitHub release `v10.45`.

---

## Out of Scope

- reopening P136 goal-first Plan reference ordering
- changing `/goal` objective ownership
- turning plan files into authority or completion proof
- changing `/plan` overflow-only semantics beyond exact cross-references needed for this wave
- unrelated plugin, companion-doc, memory, phase-grammar, task-board, document-governance, or coding/debug/TDD doctrine work
- broad cleanup of unrelated dirty repo state

---

## Completion Gate

- selected non-trivial plan-backed or goal-backed execution now prefers Subagent-Driven first by doctrine
- Inline Execution remains available only through checked suitability exceptions
- the system no longer needs to surface a default execution-choice menu when suitability can already be decided from checked context
- `/goal` remains objective authority and plan files remain route-only support
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.45 / P137`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is committed, pushed to `master`, tagged, and release-verified

---

## Current Status

P137 is completed.

Current checked progress:
- the route-only plan file exists at `docs/superpowers/plans/2026-06-03-p137-subagent-driven-first-execution-routing.md`
- selected non-trivial plan-backed or goal-backed execution now prefers Subagent-Driven first after a checked suitability gate while Inline remains a checked direct-handling exception
- touched design/changelog/README/TODO/phase/patch surfaces are aligned to `v10.45 / P137`
- touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope
- `git diff --check`, push/update to `master`, GitHub release verification, and final closeout alignment all passed
