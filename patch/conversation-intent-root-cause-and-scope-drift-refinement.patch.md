# Conversation Intent, Root-Cause, and Scope-Drift Refinement Patch

> **Current Version:** 1.0
> **Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835
> **Status:** Released / Completed
> **Target Design:** [design/design.md](../design/design.md) v10.06
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.06 / P098`.

It packages a doctrine refinement across existing merged owner rules so the assistant can expose a concise working interpretation of user intent when helpful, clarify selectively, reason toward root cause more cleanly, and repair scope drift after correction.

---

## Analysis

The released `v10.05 / P097` wave compacted the active runtime install set to 18 merged rules, but did not yet teach a complete conversation doctrine for visible intent read and diagnosis-first root-cause framing.

The main risk in P098 is not file count. The main risks are:
- making the assistant ceremonial by forcing intent mirroring on trivial asks
- over-clarifying instead of continuing with a bounded working read
- overclaiming root cause from partial evidence
- spreading the doctrine into the wrong owners and damaging the merged owner boundaries established in P097

---

## Change Items

### 1) Primary execution doctrine

- **Target artifact:** `execution-and-goal-frame.md`
- **Change type:** additive refinement
- **Current state:** intent classification, discussion/execution mode, and stop/continue behavior already exist, but visible working interpretation is not a first-class doctrine.
- **Target state:** the rule teaches visible intent read, goal lock, selective clarification, and repair re-anchor when these reduce drift.
- **Review point:** do not turn this into mandatory ceremonial wording for trivial asks.

### 2) Intent taxonomy and routing implications

- **Target artifact:** `worker-routing-and-context.md`
- **Change type:** additive refinement
- **Current state:** intent-first routing exists, but the taxonomy and implications for mixed asks can be made more explicit.
- **Target state:** the rule contains a clearer intent taxonomy, routing implications, and diagnosis-first handling for mixed symptom-heavy asks.
- **Review point:** routing ownership must stay here; it must not duplicate execution-mode or evidence-threshold logic.

### 3) Root-cause evidence and wording

- **Target artifact:** `evidence-discipline.md`, `accurate-communication.md`, `communication-register.md`, `explanation-and-presentation.md`, `coding-discipline.md`
- **Change type:** additive refinement
- **Current state:** evidence, wording, and debug strategy already exist, but they do not yet provide one clean doctrine for root-cause-focused conversation.
- **Target state:** touched owners separate symptom, hypothesis, likely cause, verified cause, next-best check, and coding/debug-specific root-cause narrowing.
- **Review point:** evidence ownership, wording ownership, presentation ownership, and coding/debug ownership must stay separated.

### 4) Governance and release surfaces

- **Target artifact:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P098 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.05 / P097` as the current released wave.
- **Target state:** master surfaces identify `v10.06 / P098` as the active refinement wave until release verification passes.
- **Review point:** keep runtime install count at 18 unless a new install gate explicitly changes it.

---

## Verification

Verified checks for release:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Visible intent read, selective clarification, root-cause framing, repair re-anchor, intent taxonomy, trigger additions, anti-patterns, examples, and success metrics are present in the correct owners.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- Git diff has no whitespace errors.
- GitHub release `v10.06` was created and verified before closeout wording claimed release completion.
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.06
- Release target and tag point to commit `e3b9801560a5be177fcc7bf8fbe8498e5eb5cdb5`.
- Published at `2026-05-16T03:36:14Z`.

---

## Implementation Status

P098 is released and closed for `v10.06`.

Validation, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, consistency sweep, push, and GitHub release verification passed.

Release evidence:
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.06
- Release target and tag point to commit `e3b9801560a5be177fcc7bf8fbe8498e5eb5cdb5`.
- Published at `2026-05-16T03:36:14Z`.

---

## Rollback Approach

If P098 is reversed after release, restore the prior `v10.05 / P097` source state through a governed rollback release and keep the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat runtime destination extras as deletion targets during rollback.
