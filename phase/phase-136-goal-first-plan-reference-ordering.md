# P136 — Goal-First Plan Reference Ordering

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P136
> **Status:** Completed / Released
> **Target Release:** v10.44
> **Design References:**
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.17
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.20
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.24
> - [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.38
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.17
> **Patch References:** [../patch/goal-first-plan-reference-ordering.patch.md](../patch/goal-first-plan-reference-ordering.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Close the remaining governed `/goal` artifact-ordering gap after P135 by making copied durable-plan-backed goal artifacts always present `/goal` before `Plan reference:` inside the same copied artifact.

---

## Why This Phase Exists

P135 already fixed the bigger operational gap:
- the route-only plan file is written first
- the final copied governed `/goal` artifact carries the exact in-artifact `Plan reference`
- save-plan / rerun-`/goal` loops are no longer the normal path

At phase open, one visible artifact-ordering gap remained:
- active template wording could still place `Plan reference:` before `/goal`
- owner wording still required the same copied artifact but did not yet hard-lock `/goal` first and `Plan reference:` second

P136 exists to harden that exact output contract:
- copied governed `/goal` artifact starts with `/goal`
- `Plan reference:` follows after it inside the same copied artifact
- plan-file-first authoring from P135 stays intact
- `/goal` stays objective owner
- the plan file stays route-only support

---

## Expected Output

- `explanation-and-presentation.md` shows the copied governed `/goal` artifact in the required order: `/goal` first, `Plan reference:` second
- `execution-and-goal-frame.md` and `phase-todo-artifact.md` explicitly require that same copied-artifact ordering for durable-plan-backed governed goals
- `accurate-communication.md` and `communication-register.md` align wording so the reference does not read like a detachable preface above the command
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.44 / P136`
- `git diff --check`, source/runtime parity + body sufficiency, push/update to `master`, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Reconfirm the exact ordering drift in active owner/template surfaces.
- [x] Harden `explanation-and-presentation.md` so copied governed `/goal` artifact examples show `/goal` first and `Plan reference:` second.
- [x] Harden `execution-and-goal-frame.md` and `phase-todo-artifact.md` so the ordering becomes an explicit owner contract.
- [x] Align `accurate-communication.md` and `communication-register.md` to the same ordering rule.
- [x] Sync touched design and per-chain changelog surfaces.
- [x] Sync touched README/TODO/phase/patch/master-changelog surfaces.
- [x] Install/update the touched runtime rules and verify source/runtime parity + body sufficiency.
- [x] Publish the selected scope safely without bundling unrelated dirty repo state.
- [x] Verify the pushed commit, `master` update, and GitHub release `v10.44`.

---

## Out of Scope

- reopening the broader P130/P134/P135 goal model beyond this exact ordering gap
- changing `/goal` objective ownership
- turning the plan file into authority or completion proof
- making `/plan` the ordinary paired next step for every route-heavy goal
- plugin, diagram, memory, or unrelated installer doctrine work
- broad cleanup of unrelated stale wording outside touched current-state sync

---

## Completion Gate

- copied governed `/goal` artifacts that carry durable route support now surface `/goal` before `Plan reference:` inside the same copied artifact
- no touched active owner/template/example still places `Plan reference:` before `/goal`
- P135 plan-file-first authoring remains intact
- `/goal` still owns outcome/proof/scope/guardrails
- the plan file still reads as route-only support rather than authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.44 / P136`
- `git diff --check` passes
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- the selected scope is committed, pushed to `master`, tagged, and release-verified

---

## Current Status

P136 is completed.

Current checked progress:
- the route-only plan file for P136 exists at `docs/superpowers/plans/2026-06-03-p136-goal-first-plan-reference-ordering.md`
- the touched root owner/template wording now requires `/goal` first and `Plan reference:` after it inside the same copied artifact
- touched design/changelog/README/TODO/phase/patch surfaces are aligned to `v10.44 / P136`
- touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope
- `git diff --check`, push/update to `master`, GitHub release verification, and final closeout alignment all passed
