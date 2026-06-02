# Goal-First Plan Reference Ordering Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.20
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P136 wave.

It packages one bounded doctrine hardening so copied durable-plan-backed governed `/goal` artifacts no longer place `Plan reference:` above the command they belong to.

---

## Analysis

Before this wave:
- P135 already required the route-only plan file to be written before final governed `/goal` emission
- P135 already required the exact `Plan reference` to stay inside the same copied artifact
- but active template wording could still present the copied artifact as `Plan reference:` first and `/goal` second
- owner wording still did not explicitly lock the copied artifact to `/goal` first and `Plan reference:` after

The better posture is:
- when durable route support is present, the copied artifact starts with `/goal`
- `Plan reference:` follows after the `/goal` line inside the same copied artifact
- the reference stays subordinate route support rather than a detachable preface
- P135 plan-file-first authoring remains intact
- `/goal` remains objective owner

This wave is intentionally doctrine/release-sync-only. It does not reopen the broader P130/P134/P135 model and does not change `/plan` overflow-only semantics.

---

## Change Items

### 1) Copied artifact ordering hardening

- **Target artifacts:** `explanation-and-presentation.md`, `execution-and-goal-frame.md`, `phase-todo-artifact.md`
- **Change type:** refinement
- **Current state at phase open:** active doctrine kept `Plan reference` inside the same copied artifact but still allowed ordering drift where the reference appeared before `/goal`
- **Target state:** durable-plan-backed copied governed `/goal` artifacts always present `/goal` first and `Plan reference:` after it inside the same copied artifact
- **Review point:** ordering is explicit without weakening the P135 plan-file-first contract

### 2) Wording alignment

- **Target artifacts:** `accurate-communication.md`, `communication-register.md`
- **Change type:** refinement
- **Current state at phase open:** wording could still describe the reference like a detachable preface or adjacent route note without ordering discipline
- **Target state:** wording makes it clear that `Plan reference:` follows the command inside the copied artifact and remains route-only support
- **Review point:** plan files remain route-only support and do not become authority or completion proof

### 3) Design / release-surface sync

- **Target artifacts:** touched design docs, per-chain changelogs, `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-136-goal-first-plan-reference-ordering.md`, `patch/goal-first-plan-reference-ordering.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.44-released-goal-first-plan-reference-ordering.changelog.md`
- **Change type:** release synchronization
- **Current state:** latest released baseline is `v10.43 / P135`
- **Target state:** touched release surfaces consistently open and close `v10.44 / P136`
- **Review point:** release wording stays evidence-calibrated and limited to the touched ordering scope

---

## Verification

Required checks before release closeout:
- the primary `/goal` owners now require `/goal` first and `Plan reference:` second inside the same copied artifact when durable route support is present
- no touched active owner/template/example still places `Plan reference:` before `/goal`
- wording/presentation owners no longer describe the reference like a detached preface above the command
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.44 / P136`
- `git diff --check` passes
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- the selected scope is committed, pushed to `master`, tagged, and GitHub release verification passes

---

## Implementation Status

P136 is completed.

The route-only plan file exists, the touched root owner/template wording now requires `/goal` first and `Plan reference:` after it inside the same copied artifact, the touched owner-chain and release surfaces were synchronized, touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope, and the selected scope was published through a bounded release path with push/tag/release verification.
