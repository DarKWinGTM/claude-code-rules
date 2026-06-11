# P143 — Hybrid Progress Reporting Surface Alignment

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P143
> **Status:** Active / In Progress
> **Target Release:** v10.51
> **Design References:**
> - [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.41
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.20
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.21
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.25
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.29
> **Patch References:** [../patch/hybrid-progress-reporting-surface-alignment.patch.md](../patch/hybrid-progress-reporting-surface-alignment.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Standardize a bounded hybrid progress-reporting model for non-trivial Claude work so updates can clearly show `Current`, `Done so far`, `In progress`, `Remaining`, `Blockers / Notes`, and `Next`, while keeping evidence-strength wording honest, keeping safe continuation as the default when no real stop gate exists, and preserving the route-only `/goal` authoring boundary.

---

## Why This Phase Exists

The current RULES set already contains several important pieces:
- evidence-calibrated status wording
- compact diagnostic snapshots
- continuation-first execution guidance
- phase-backed closeout wording
- the P141 boundary that stops governed goal authoring from leaking into a default execution-mode menu

What it still lacks is one compact, repeatable in-flight progress shape that brings those pieces together.

That gap creates a practical problem:
- readers can understand the doctrine if they inspect several owners together
- but during active work they still have to reconstruct what has been done, what is still moving, what remains open, and what comes next

P143 closes that gap with one bounded hybrid progress-reporting surface instead of reopening the broader goal/plan architecture.

---

## Expected Output

- non-trivial in-flight updates can use a compact hybrid progress snapshot built around `Current`, `Done so far`, `In progress`, `Remaining`, `Blockers / Notes`, and `Next`
- `Done so far` remains bounded to checked scope and does not read like total completion
- progress narration remains compatible with continuation-first execution and does not become a stop reason or milestone-only pause
- route-only governed `/goal` authoring still ends at the goal artifact plus subordinate route support, with no default `Subagent-Driven` / `Inline Execution` menu leakage
- touched runtime/design/changelog/TODO/phase/patch surfaces align to one `v10.51 / P143` baseline once release verification completes

---

## Action Checklist

- [x] Implement the selected runtime-owner doctrine updates.
- [x] Sync the touched design companions and per-chain changelogs.
- [ ] Sync `TODO.md`, `phase/SUMMARY.md`, this phase file, and `patch/hybrid-progress-reporting-surface-alignment.patch.md`.
- [ ] Decide and complete release-scope sync (`changelog/changelog.md` and a `v10.51` release-detail shard) only if the wave is promoted through release closeout.
- [ ] Complete final verification, runtime install/update verification if selected, and any release/publish evidence required by the chosen closeout scope.

---

## Out of Scope

- reopening the broader P139 / P140 / P141 / P142 architecture beyond this progress-reporting gap
- adding a new command surface
- reintroducing a default `Subagent-Driven` / `Inline Execution` menu after route-only goal authoring
- forcing a heavy status block onto trivial replies or one-step answers
- unrelated plugin or non-RULES waves

---

## Completion Gate

- the shared hybrid progress markers now exist across the selected runtime owners in a consistent way
- the wording keeps `implemented`, `tested`, `verified-in-scope`, `working`, `fixed`, and `stable` distinct
- `Done so far` is bounded to checked scope and no longer reads like full completion
- progress narration does not become a stop gate or milestone-only pause when safe continuation exists
- route-only `/goal` authoring still stops at the goal artifact plus subordinate route support without leaking an execution-mode menu
- touched design/changelog/TODO/phase/patch surfaces align to one `v10.51 / P143` state when the wave is locally synchronized
- if runtime install/update or release scope is selected, source/runtime parity + body sufficiency, `git diff --check`, and any required publish evidence all pass before closeout is claimed at that strength

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is governed wording, presentation, and execution-surface work only.
- **Checks planned:** touched-owner anchor verification, per-chain changelog sync, TODO/phase/patch sync, `git diff --check`, and runtime install/update parity plus body sufficiency if runtime install verification is included in closeout.
- **Confidence:** runtime and design/changelog owner updates are in progress; release-scope sync is not yet claimed.

---

## Current Status

P143 is active.

Current checked progress:
- the selected runtime-owner doctrine updates are in place across `accurate-communication.md`, `explanation-and-presentation.md`, `communication-register.md`, `execution-and-goal-frame.md`, and `phase-todo-artifact.md`
- the touched design companions and per-chain changelogs are aligned to the same hybrid progress-reporting refinement
- this clean worktree was opened from `origin/master` because the main local RULES checkout is ahead/behind and full of unrelated modified/untracked state outside the selected wave
- TODO/phase/patch current-state sync plus any release-scope closeout are still pending
