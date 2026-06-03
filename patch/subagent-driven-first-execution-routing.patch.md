# Subagent-Driven-First Execution Routing Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.21
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P137 wave.

It packages one bounded doctrine hardening so selected non-trivial plan-backed or goal-backed work no longer needs to surface `Subagent-Driven` vs `Inline Execution` as an ordinary user-facing choice when the system can decide the more suitable execution mode directly.

---

## Analysis

Before this wave:
- `/goal` already remained objective owner and plan files already remained route-only support
- worker-routing already supported standalone subagents, helper lanes, and leader verification
- phase/todo already supported built-in task shaping for non-trivial work
- but selected execution still did not explicitly prefer Subagent-Driven first by doctrine
- Inline Execution exceptions were not yet normalized as checked suitability-based fallbacks

The better posture is:
- selected non-trivial plan/goal execution should prefer Subagent-Driven first
- Inline Execution should remain valid only when a checked direct-handling exception makes it more effective for the current slice
- worker-routing should keep topology ownership
- phase/todo should keep task shaping ownership
- the system should not default to surfacing the execution-mode choice menu when it can decide suitability directly

This wave is intentionally doctrine/release-sync-only. It does not reopen P136 goal-first Plan reference ordering and does not change `/goal` objective ownership or `/plan` overflow semantics.

---

## Change Items

### 1) Selected execution posture hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `worker-routing-and-context.md`, `phase-todo-artifact.md`
- **Change type:** refinement
- **Current state:** selected execution can still surface execution mode as a default choice rather than deciding the more suitable posture directly
- **Target state:** selected non-trivial plan/goal execution prefers Subagent-Driven first, with Inline allowed only through checked suitability exceptions
- **Review point:** goal/plan authority split and owner boundaries remain intact

### 2) Communication alignment

- **Target artifact:** `communication-register.md`
- **Change type:** refinement
- **Current state:** execution-mode choice can still read like a normal option menu even when the system can decide suitability directly
- **Target state:** communication suppresses default execution-choice prompts while preserving visible checked reasons for Inline exceptions
- **Review point:** communication remains transparent without reintroducing unnecessary user-choice theater

### 3) Design / release-surface sync

- **Target artifacts:** touched design docs, per-chain changelogs, `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-137-subagent-driven-first-execution-routing.md`, `patch/subagent-driven-first-execution-routing.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.45-released-subagent-driven-first-execution-routing.changelog.md`
- **Change type:** release synchronization
- **Current state:** latest released baseline is `v10.44 / P136`
- **Target state:** touched release surfaces consistently open and close `v10.45 / P137`
- **Review point:** release wording stays evidence-calibrated and limited to the touched execution-default scope

---

## Verification

Required checks before release closeout:
- selected non-trivial plan-backed or goal-backed execution now prefers Subagent-Driven first by doctrine
- Inline Execution remains available only through checked suitability exceptions
- the system no longer needs to surface a default execution-style choice prompt when suitability can be decided from checked context
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.45 / P137`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is committed, pushed to `master`, tagged, and GitHub release verification passes

---

## Implementation Status

P137 is completed.

The route-only plan file exists, the touched doctrine owners now prefer Subagent-Driven first for selected non-trivial plan-backed or goal-backed execution while preserving Inline as a checked exception, the touched owner-chain and release surfaces were synchronized, touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope, and the selected scope was published through a bounded release path with push/tag/release verification.
