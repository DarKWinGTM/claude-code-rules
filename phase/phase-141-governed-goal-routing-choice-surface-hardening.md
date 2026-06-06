# P141 — Governed Goal Routing-Choice Surface Hardening

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P141
> **Status:** Active / In Progress
> **Target Release:** v10.49
> **Design References:**
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.24
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.28
> - [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.40
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.20
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.19
> **Patch References:** [../patch/governed-goal-routing-choice-surface-hardening.patch.md](../patch/governed-goal-routing-choice-surface-hardening.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Harden RULES so governed `/goal` authoring stays objective-facing, ends cleanly at the emitted goal artifact plus subordinate route support when execution was not yet selected, and no longer leaks a default `Subagent-Driven` / `Inline Execution` choice menu after authoring-only turns.

---

## Why This Phase Exists

P139 already established two important ideas:
- plain goal requests should receive the smallest sufficient route support automatically
- selected goal/plan execution posture should be chosen internally instead of surfaced as a default user-facing menu

The remaining leak is the authoring boundary.

A governed goal/plan-file turn can still do the right authoring work and then drift into a follow-up `Which approach?` menu even though:
- the user asked only for goal/plan-file authoring
- no materially different execution path was being chosen at that moment
- the internal routing decision belongs to the later execution transition, not to the authoring closeout

P141 closes that leak by making the authoring stop boundary explicit across the goal, phase/task, wording, register, and presentation owners.

---

## Expected Output

- governed goal/plan-file authoring turns now stop at the emitted goal artifact plus subordinate route support when execution was not yet selected
- execution-posture selection remains internal for actual execution-ready work
- default user-facing `Subagent-Driven` / `Inline Execution` menus no longer appear as authoring closeout leakage
- touched runtime/design/changelog/TODO/phase/patch surfaces align to one `v10.49 / P141` baseline once release verification completes
- touched runtime-owner install/update, source/runtime parity, and body sufficiency verification pass before release closeout

---

## Action Checklist

- [x] Implement the selected primary runtime-owner doctrine updates.
- [x] Sync the touched design companions and per-chain changelogs.
- [x] Sync `TODO.md`, `phase/SUMMARY.md`, this phase file, and `patch/governed-goal-routing-choice-surface-hardening.patch.md`.
- [ ] Sync `changelog/changelog.md` and `changelog/changelog/v10.49-released-governed-goal-routing-choice-surface-hardening.changelog.md`.
- [ ] Complete final verification, install, publish, tag, and release evidence.

---

## Out of Scope

- reopening the broader P130 / P134 / P135 / P139 goal-plan architecture beyond this leak boundary
- adding a new command surface
- making `/plan` the default paired next step for every route-heavy goal
- forcing durable plan files for trivial or obvious one-step goals
- product-code implementation work
- unrelated RULES waves, plugin waves, or cleanup work

---

## Completion Gate

- governed goal/plan-file authoring turns now stop cleanly at the authoring surface when execution was not yet selected
- execution-posture selection remains internal and no default execution-mode menu leaks into authoring closeout
- touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces align to `v10.49 / P141`
- touched runtime-owner install/update verification, source/runtime parity, body sufficiency, `git diff --check`, push/update to `master`, tag, and GitHub release verification all pass

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is governed doctrine/release work only.
- **Checks planned:** touched-owner anchor verification, doc-surface alignment, runtime install/update verification, source/runtime parity, body sufficiency, `git diff --check`, branch/default-branch update verification, tag verification, and GitHub release verification.
- **Confidence:** implementation and owner sync are in progress; release-level verification has not been claimed yet.

---

## Current Status

P141 is active.

Current checked progress:
- the selected runtime-owner doctrine edits are in place across `execution-and-goal-frame.md`, `phase-todo-artifact.md`, `accurate-communication.md`, `communication-register.md`, and `explanation-and-presentation.md`
- the touched design companions and per-chain changelogs are aligned to the same authoring stop-boundary refinement
- `TODO.md`, `phase/SUMMARY.md`, this phase file, and `patch/governed-goal-routing-choice-surface-hardening.patch.md` now reflect the active wave
- touched runtime install/update parity is aligned and `git diff --check` passed, but release-history sync plus push/update to `master`, tag `v10.49`, and GitHub release verification remain blocked because `master` is `ahead 3, behind 19` relative to `origin/master` and the working tree still contains extensive unrelated modified/untracked files outside P141 scope
