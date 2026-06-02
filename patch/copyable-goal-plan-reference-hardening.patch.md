# Copyable Goal Plan-Reference Hardening Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.18
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P134 wave.

It packages one bounded doctrine hardening so a durable plan-backed governed `/goal` can no longer lose its route-plan pointer when the user copies only the advisory goal artifact.

---

## Analysis

Before this wave:
- RULES already supported plan-backed governed `/goal` output
- the plan file was already meant to stay route-only support
- but owner/presentation wording still allowed a durable plan pointer to live in surrounding explanation or adjacent support instead of inside the copied artifact itself

That posture was too weak for real execution continuity because the next session could receive a clean objective contract without the route-plan pointer that was supposed to guide execution.

The better posture is:
- `/goal` continues to own outcome, proof/checks, scope, and guardrails
- the plan file continues to stay route-only support
- any durable `Plan reference` must travel inside the same copied goal artifact
- adjacent route notes remain allowed only for non-durable support

This wave is intentionally doctrine/release-sync-only. It does not reopen the broader P130 model or change `/plan` ownership.

---

## Change Items

### 1) Runtime owner hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `phase-todo-artifact.md`, `explanation-and-presentation.md`
- **Change type:** refinement
- **Current state:** durable plan references could still be emitted in surrounding explanation or adjacent support
- **Target state:** durable plan-backed governed `/goal` output now requires an in-artifact `Plan reference` inside the same copied goal artifact
- **Review point:** `/goal` stays objective owner; plan files stay route-only and non-authoritative

### 2) Design and owner-chain version sync

- **Target artifacts:** corresponding design files and per-chain changelogs for the three runtime owners
- **Change type:** release synchronization
- **Current state:** owner-chain versions still ended at the earlier integrated goal-with-planning refinements
- **Target state:** execution/phase-presentation owner chains record the P134 copy-boundary hardening explicitly
- **Review point:** scope stays narrow and avoids unrelated owner chains

### 3) Master release-surface sync

- **Target artifacts:** `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-134-copyable-goal-plan-reference-hardening.md`, `patch/copyable-goal-plan-reference-hardening.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.42-released-copyable-goal-plan-reference-hardening.changelog.md`
- **Change type:** release synchronization
- **Current state:** latest released baseline was `v10.41 / P133`
- **Target state:** touched release surfaces consistently open and close `v10.42 / P134`
- **Review point:** release wording stays evidence-calibrated and does not overclaim untouched stale surfaces

---

## Verification

Required checks before release closeout:
- the three primary `/goal` owner files now keep durable `Plan reference` inside the same copied goal artifact
- `/goal` still owns objective/proof/scope/guardrails
- plan files still read as route-only support rather than authority or completion proof
- touched design/changelog/README/TODO/phase/patch surfaces align to `v10.42 / P134`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and GitHub release verification passes

---

## Implementation Status

P134 is completed.

The copy-boundary loophole for durable plan-backed governed `/goal` output is now closed, the touched owner-chain and release surfaces were synchronized, the plan file remained route-only support, and the selected scope was published through a clean release path with push/tag/release verification.
