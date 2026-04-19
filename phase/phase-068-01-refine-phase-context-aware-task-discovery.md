# Phase 068-01 - Refine phase-context-aware task discovery

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 068-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/phase-context-aware-task-discovery.patch.md](../patch/phase-context-aware-task-discovery.patch.md)

---

## Objective

Refine the existing owner set so Task List behavior stays current-phase-first but also consults relevant `/phase` planning context more actively whenever that context already exists and is useful.

## Why this phase exists

The current RULES doctrine already aligns tasks to the current phase and clearly implied staged context, but it can still underuse planning context that already exists inside `/phase`.
This wave closes that gap without promoting future-phase work too early:
- current active phase still stays first
- current phase family and staged lane should still matter
- already-authored next planned phase information in `/phase` should help continuity and draft next-work visibility when relevant
- unopened future phases still remain draft/proposal only until made active

## Action points / execution checklist

- [x] refine `todo-standards` so task behavior explicitly consults relevant `/phase` planning context when available
- [x] refine `phase-implementation` so the phase-context hierarchy includes bounded next-phase context from `/phase`
- [x] refine `project-documentation-standards` so the repository model names `/phase` as both current execution structure and bounded next planned structure
- [x] refine `phase-implementation-template` so future authoring exposes active phase family, planned next phase(s), and next-phase activation boundary
- [x] synchronize master/history surfaces for the bounded wave

## Verification

- [x] current-phase-first behavior remains intact
- [x] task discovery now consults relevant `/phase` planning context more actively when that context already exists
- [x] unopened future phases still remain draft/proposal only until made active by governing context
- [x] touched master/history surfaces record the wave coherently

## Exit criteria

- [x] the owner set now expresses current-phase-first but phase-context-aware task discovery without inventing a new doctrine chain
- [x] already-authored next-phase context can guide continuity and draft next-work visibility without becoming silent execution authorization
