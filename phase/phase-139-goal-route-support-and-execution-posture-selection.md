# P139 — Goal Route Support and Execution Posture Selection

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P139
> **Status:** Completed / Released
> **Target Release:** v10.47
> **Design References:**
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.22
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.26
> - [../design/worker-routing-and-context.design.md](../design/worker-routing-and-context.design.md) v1.14
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.19
> - [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.39
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.18
> **Patch References:** [../patch/goal-route-support-and-execution-posture-selection.patch.md](../patch/goal-route-support-and-execution-posture-selection.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make plain goal requests resolve the smallest sufficient route support automatically when needed, and make selected goal/plan execution choose posture internally from checked context instead of exposing a default user-facing mode choice.

---

## Why This Phase Exists

P139 closes one bounded goal/plan workflow gap:
- users should not need to learn `goal plan file` to receive proper governed route support
- `/goal` should stay the objective owner while any plan file remains route-only support
- selected `/goal` or selected plan execution should choose Subagent-Driven vs Inline internally from checked context
- user-facing wording should normally report the chosen action, route support, and remaining gate rather than internal routing labels

This release keeps route depth and execution posture adaptive, but it keeps the decision mechanism inside RULES instead of turning it into a user-facing choice ritual.

---

## Expected Output

- plain goal requests now trigger planning-depth resolution when route pressure or governed complexity requires support
- durable `Plan reference:` appears only after the route-only plan file already exists in checked scope or was successfully written in the same flow
- selected goal/plan execution no longer emits `Subagent-Driven` vs `Inline Execution` as a default user-facing menu
- touched design/changelog/README/TODO/phase/patch/master-changelog/release-detail surfaces align to one released `v10.47 / P139` baseline
- touched runtime rules are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check`, push/update to `master`, tag, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Harden `execution-and-goal-frame.md` for planning-depth resolution and internal posture selection.
- [x] Harden `phase-todo-artifact.md` for plain-goal route support and selected execution task shaping.
- [x] Harden `worker-routing-and-context.md`, `communication-register.md`, `accurate-communication.md`, and `explanation-and-presentation.md` for routing-label suppression and exact `Plan reference:` semantics.
- [x] Sync touched design and per-chain changelog surfaces.
- [x] Sync README/TODO/phase/patch/master-changelog/release-detail surfaces.
- [x] Complete final verification, install, publish, tag, and release evidence.

---

## Out of Scope

- making `/plan` mandatory for every `/goal`
- forcing durable plan files for trivial or already direct goals
- broad generic team/agent doctrine beyond the selected goal/plan boundary
- product-code implementation work
- unrelated plugin, memory, or governed-docs waves

---

## Completion Gate

- plain goal requests now resolve planning depth automatically for governed/non-trivial/route-heavy work
- users no longer need `goal plan file` phrasing to receive proper governed route support
- selected `/goal` or selected plan execution no longer surfaces `Subagent-Driven` vs `Inline Execution` as a default user-facing choice menu
- touched runtime owners, design companions, per-chain changelogs, TODO/phase/patch/README/master-changelog/detail surfaces align to released `v10.47 / P139`
- touched runtime install/update, source/runtime parity, body sufficiency, `git diff --check`, push/update to `master`, tag `v10.47`, and GitHub release verification all pass

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is governed doctrine/release work only.
- **Checks run:** `git diff --check`, touched runtime install/update verification, source/runtime parity, body sufficiency, branch/default-branch update verification, tag verification, and GitHub release verification.
- **Confidence:** released and verified in the checked doctrine scope.

---

## Current Status

P139 is completed.

Current checked progress:
- plain goal requests now auto-resolve the smallest sufficient route support when governed/non-trivial/route-heavy work needs it.
- selected goal/plan execution now chooses posture internally from checked context and does not emit a default user-facing routing choice menu.
- touched design/changelog/README/TODO/phase/patch/master-changelog/release-detail surfaces are aligned to `v10.47 / P139`.
- touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope.
- `git diff --check`, push/update to `master`, tag `v10.47`, and GitHub release verification all passed.
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.47
