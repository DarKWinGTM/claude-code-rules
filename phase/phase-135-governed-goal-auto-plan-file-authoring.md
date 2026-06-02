# P135 — Governed Goal Auto-Plan-File Authoring

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P135
> **Status:** Completed / Released
> **Target Release:** v10.43
> **Design References:**
> - [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.19
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.23
> - [../design/document-integrity.design.md](../design/document-integrity.design.md) v1.7
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.16
> - [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.37
> - [../design/communication-register.design.md](../design/communication-register.design.md) v1.16
> **Patch References:** [../patch/governed-goal-auto-plan-file-authoring.patch.md](../patch/governed-goal-auto-plan-file-authoring.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Close the remaining governed `/goal` authoring gap after P134 by making the route-only plan file write part of the same assistant-owned authoring flow.

---

## Why This Phase Exists

P134 already fixed one important problem: if a durable route plan exists, the copied governed `/goal` artifact must carry `Plan reference` inside the same artifact.

But one operational gap still remained:
- the assistant could still draft a route
- then ask whether to save the plan
- or ask the user to invoke `/goal` again
- even though no real stop gate existed

P135 exists to harden that exact sequence:
- write the route-only plan file first when the governed trigger holds
- only then emit the final copied `/goal` artifact with exact `Plan reference`
- keep `/goal` as objective owner
- keep the plan file route-only support
- keep `/plan` as overflow / explicit standalone planning / later route revision only

---

## Expected Output

- `execution-and-goal-frame.md` requires actual governed `/goal` authoring with durable route support to write the route-only plan file before final goal emission
- `phase-todo-artifact.md` requires that same write step inside the governed authoring flow and bans save-plan/rerun-`/goal` loops when no real stop gate exists
- `document-integrity.md` explicitly allows the required route-only plan file for governed `/goal` authoring while still blocking speculative or duplicate plan artifacts
- `explanation-and-presentation.md` emits the final copied `/goal` artifact only after the route-only plan file has been written successfully
- `accurate-communication.md` and `communication-register.md` align wording so the assistant does not phrase plan persistence as a user-owned save step or a second `/goal` invocation loop
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.43 / P135`
- `git diff --check`, branch/default-branch verification, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Harden `execution-and-goal-frame.md` so actual governed `/goal` authoring writes the route-only plan file before final goal emission.
- [x] Harden `phase-todo-artifact.md` so governed `/goal` sourcing/authoring keeps plan-file write inside the same flow and does not bounce save/rerun prompts to the user.
- [x] Add the file-hygiene carve-out in `document-integrity.md` for required governed route-only goal plans.
- [x] Align `explanation-and-presentation.md`, `accurate-communication.md`, and `communication-register.md` to the new no-save-loop behavior.
- [x] Sync touched design and per-chain changelog surfaces.
- [x] Sync touched README/TODO/phase/patch/master-changelog surfaces.
- [x] Publish the selected scope safely without bundling unrelated dirty repo state.
- [x] Verify the pushed commit and GitHub release `v10.43`.

---

## Out of Scope

- reopening the broader P130/P134 `/goal` model beyond this exact authoring-sequence gap
- changing `/goal` objective ownership
- turning the plan file into objective authority or completion proof
- making `/plan` the ordinary paired next step for every route-heavy goal
- broad cleanup of unrelated stale wording outside touched current-state sync
- plugin, diagram, installer, memory-context, or runtime-destination doctrine work

---

## Completion Gate

- actual governed `/goal` authoring with durable route support now writes the route-only plan file before final goal emission
- save-plan / rerun-`/goal` loops are explicitly rejected when no real stop gate exists
- `Plan reference` cannot point to an unwritten file
- `/goal` still owns outcome/proof/scope/guardrails
- the plan file still reads as route-only support rather than authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.43 / P135`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and release-verified

---

## Current Status

P135 is completed.

Current checked progress:
- the governed `/goal` authoring sequence now owns plan-file persistence when the durable-route trigger holds
- the assistant no longer leaves save-plan or rerun-`/goal` prompts as the normal continuation path for this flow
- the route-only plan file remains subordinate support and does not become objective authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces are aligned to `v10.43 / P135`
- the selected doctrine/release-sync scope was published through a clean isolated release path rather than the dirty local working tree
- `git diff --check`, push/update to `master`, GitHub release verification, and final closeout alignment all passed
