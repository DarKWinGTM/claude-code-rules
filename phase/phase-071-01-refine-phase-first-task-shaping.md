# Phase 071-01 - Refine phase-first task shaping

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 071-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/phase-first-task-shaping-refinement.patch.md](../patch/phase-first-task-shaping-refinement.patch.md)

---

## Objective

Refine the existing owner set so phase-first task shaping becomes an explicit requirement whenever `/phase` exists and relevant governed phase context is already available.

## Why this phase exists

The current RULES doctrine already supports current-phase-first and phase-context-aware task behavior, but that wording can still read too softly in practice.
This wave closes that gap:
- relevant governed `/phase` context should be inspected before task shaping when it exists
- current active phase remains the default shaping authority
- detached generic task shaping in the presence of relevant governed phase context should be treated as drift
- future-phase boundaries still remain intact and draft-only rules still apply to unopened future work

## Action points / execution checklist

- [x] refine `todo-standards` so relevant governed `/phase` context becomes a required inspection step before task shaping when available
- [x] refine `phase-implementation` so phase-linked task shaping uses the same required-inspection posture
- [x] preserve current-phase-first behavior and future-phase draft boundaries
- [x] synchronize master/history surfaces for the bounded wave

## Verification

- [x] relevant governed `/phase` context is now an explicit required inspection step before live task shaping when available
- [x] detached generic task shaping in the presence of relevant governed phase context now reads as drift rather than as an acceptable fallback
- [x] current-phase-first behavior remains intact
- [x] future-phase boundaries remain intact
- [x] touched master/history surfaces record the wave coherently

## Exit criteria

- [x] the owner set now expresses phase-first task shaping more explicitly without inventing a new doctrine chain
- [x] `/phase` is now stronger as a task-shaping authority when relevant governed context already exists
