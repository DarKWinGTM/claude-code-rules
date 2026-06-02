# Governed Goal Auto-Plan-File Authoring Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.19
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P135 wave.

It packages one bounded doctrine hardening so actual governed `/goal` authoring no longer stops after route drafting or bounces the save/emit steps back to the user when no real stop gate exists.

---

## Analysis

Before this wave:
- P134 already required durable `Plan reference` to stay inside the same copied goal artifact
- but the actual authoring flow could still behave like the plan-file write was optional
- file hygiene did not yet clearly allow the required route-only plan file for this governed flow
- wording owners did not explicitly reject `save the plan?` or `run /goal again` loops

The better posture is:
- when the governed trigger holds and route basis is sufficient, write the route-only plan file first
- only then emit the final copied `/goal` artifact with exact `Plan reference`
- if the write fails, report the blocker instead of fabricating route durability
- keep `/goal` as objective owner
- keep the plan file as route-only support

This wave is intentionally doctrine/release-sync-only. It does not reopen the broader P130/P134 model and does not change `/plan` overflow-only semantics.

---

## Change Items

### 1) Governed `/goal` authoring sequence hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `phase-todo-artifact.md`
- **Change type:** refinement
- **Current state:** route-only plan persistence could still be treated like an optional follow-up step even after route basis was sufficient
- **Target state:** actual governed `/goal` authoring writes the route-only plan file first, then emits the final copied goal artifact with exact in-artifact `Plan reference`
- **Review point:** `/goal` stays objective owner; save-plan and rerun-`/goal` loops are rejected when no real stop gate exists

### 2) File-hygiene carve-out

- **Target artifact:** `document-integrity.md`
- **Change type:** refinement
- **Current state:** required governed route-only goal plans were not explicitly classified as allowed artifacts
- **Target state:** the selected governed `/goal` contract may create the exact route-only plan file it requires, while speculative or duplicate plan artifacts remain disallowed
- **Review point:** the exception stays narrow and does not weaken anti-junk doctrine broadly

### 3) Wording / presentation alignment

- **Target artifacts:** `explanation-and-presentation.md`, `accurate-communication.md`, `communication-register.md`
- **Change type:** refinement
- **Current state:** wording could still externalize plan persistence as a user-owned save step or second `/goal` invocation
- **Target state:** wording and artifact templates now assume the route-only plan file was already written before the final goal is shown, unless a blocker is reported
- **Review point:** plan files remain route-only support and do not become authority or completion proof

### 4) Design / release-surface sync

- **Target artifacts:** touched design docs, per-chain changelogs, `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-135-governed-goal-auto-plan-file-authoring.md`, `patch/governed-goal-auto-plan-file-authoring.patch.md`, `changelog/changelog.md`, `changelog/changelog/v10.43-released-governed-goal-auto-plan-file-authoring.changelog.md`
- **Change type:** release synchronization
- **Current state:** latest released baseline was `v10.42 / P134`
- **Target state:** touched release surfaces consistently open and close `v10.43 / P135`
- **Review point:** release wording stays evidence-calibrated and limited to the touched scope

---

## Verification

Required checks before release closeout:
- the primary `/goal` owners now require plan-file write before final governed goal emission when the durable-route trigger holds
- `document-integrity.md` allows the exact governed route-only plan file without allowing speculative or duplicate plan artifacts
- wording/presentation owners no longer treat plan saving or rerun-`/goal` as the normal user-facing continuation path
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.43 / P135`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and GitHub release verification passes

---

## Implementation Status

P135 is completed.

The governed `/goal` authoring sequence now writes the route-only plan file before final goal emission, the file-hygiene carve-out now allows the exact required route-only plan artifact, the touched owner-chain and release surfaces were synchronized, and the selected scope was published through a clean release path with push/tag/release verification.
