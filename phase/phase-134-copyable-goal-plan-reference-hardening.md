# P134 — Copyable Goal Plan-Reference Hardening

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P134
> **Status:** Completed / Released
> **Target Release:** v10.42
> **Design References:**
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.18
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.22
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.15
> **Patch References:** [../patch/copyable-goal-plan-reference-hardening.patch.md](../patch/copyable-goal-plan-reference-hardening.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Close the copy-boundary gap for plan-backed governed `/goal` output.

---

## Why This Phase Exists

Before this wave, RULES already supported plan-backed governed `/goal` authoring, but the doctrine still allowed a durable route-plan pointer to live in surrounding explanation or adjacent route support.

That left one practical failure mode:
- the user could copy only the advisory `/goal` artifact
- the copied goal would still carry outcome/proof/scope/guardrails
- but the plan-file pointer could be lost, which made route discipline drift-prone in the next session

P134 exists to harden that exact gap without reopening the broader P130 model:
- `/goal` still owns the objective contract
- the plan file still stays route-only support
- adjacent route notes are still allowed for non-durable support
- but any durable `Plan reference` must now travel inside the same copied goal artifact

---

## Expected Output

- `execution-and-goal-frame.md` requires a durable plan-backed governed `/goal` to carry `Plan reference` inside the same copyable goal artifact
- `phase-todo-artifact.md` translates governed `/goal` sourcing into an in-artifact `Plan reference` slot when a durable route plan materially guides execution
- `explanation-and-presentation.md` updates the promoted advisory `/goal` shape and template so the copied artifact itself carries the plan pointer
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.42 / P134`
- no owner wording makes the plan file objective authority, completion proof, or a replacement `/plan` surface
- `git diff --check`, branch/default-branch verification, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Harden `execution-and-goal-frame.md` so durable plan pointers cannot live only in surrounding explanation.
- [x] Harden `phase-todo-artifact.md` so governed `/goal` sourcing requires an in-artifact `Plan reference` slot for durable route plans.
- [x] Harden `explanation-and-presentation.md` so the advisory `/goal` block/template keeps the plan pointer inside the same copied artifact.
- [x] Sync the touched design and per-chain changelog surfaces.
- [x] Sync the touched README/TODO/phase/patch/master-changelog release surfaces.
- [x] Publish the selected scope safely without bundling unrelated dirty repo state.
- [x] Verify the pushed commit and GitHub release `v10.42`.

---

## Out of Scope

- reopening the broader P130 always-on plan-file-backed governed `/goal` model
- changing `/goal` objective ownership
- making plan files objective authority or completion proof
- making `/plan` the default paired next step for every route-heavy goal
- broad cleanup of unrelated stale wording outside touched current-state sync
- plugin, diagram, installer, memory-context, or runtime-destination doctrine work

---

## Completion Gate

- the three primary `/goal` owner files agree that any durable plan-backed governed `/goal` must keep `Plan reference` inside the same copied goal artifact
- adjacent support remains allowed only for non-durable route notes
- `/goal` still owns outcome/proof/scope/guardrails
- the plan file still reads as route-only support, not authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.42 / P134`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and release-verified

---

## Current Status

P134 is completed.

Current checked progress:
- the copy-boundary loophole is closed in the three governed `/goal` owner files
- the visible advisory `/goal` presentation now keeps durable `Plan reference` inside the same copied artifact
- plan files remain subordinate route support and do not become objective authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces are aligned to `v10.42 / P134`
- the selected doctrine/release-sync scope was published through a clean isolated release path rather than the dirty local working tree
- `git diff --check`, push/update to `master`, GitHub release verification, and final closeout alignment all passed
