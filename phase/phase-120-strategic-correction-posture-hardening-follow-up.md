# P120 — Strategic Correction Posture Hardening Follow-up

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P120
> **Status:** Active / Owner sync in progress
> **Target Release:** v10.28
> **Design References:**
> - [../design/design.md](../design/design.md) v10.28
> **Patch References:** [../patch/strategic-correction-posture-hardening-follow-up.patch.md](../patch/strategic-correction-posture-hardening-follow-up.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so AI approaches correction reasoning strategically: start from the system logic or shared mechanism before the local symptom, treat supplier/model/path-specific scope as an evidence-backed conclusion rather than an early assumption, prefer shared mechanisms before local exceptions, and use local exceptions only when the evidence supports a real local doctrine difference.

---

## Why This Phase Exists

The released `v10.27 / P119` baseline already hardened active-exchange language alignment, but the checked follow-up discussion still shows one narrower strategic reasoning miss.

The problem is not that AI lacks evidence discipline entirely. The repeated failure is narrower: when a concrete failing case appears, AI can still narrow too early around supplier/model/path-specific fixes because they look convenient or low-blast-radius, instead of first testing which shared logic or mechanism best explains the observed pattern.

This miss also creates a scope-selection problem. A local anomaly is real evidence, but it should not automatically decide the owner level of the fix. Strategic correction posture should treat scope as something to prove, not something to assume.

P120 exists to harden that strategic reasoning posture without turning RULES into a command-style prohibition list and without weakening evidence discipline, accurate wording, or direct-continuation behavior.

---

## Expected Output

- `evidence-discipline.md` encodes that correction scope must be evidence-proven and that local anomalies are evidence inputs rather than immediate owner decisions
- `external-verification-and-source-trust.md` encodes stronger corroboration before provider/supplier/model/path-specific narrowing becomes the recommended fix scope
- `communication-register.md` and `accurate-communication.md` encode recommendation posture that prefers strategy-before-patch and keeps local exceptions as evidence-earned recommendations rather than default convenience fixes
- one related playground case is updated so the behavior delta stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.28 / P120`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- remote default branch reflects the follow-up playground/master-surface updates
- GitHub release `v10.28` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.27 / P119` with no active wave open before P120 startup.
- [ ] Open P120 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Tighten evidence-grounded scope selection in `evidence-discipline.md` so local scope is proven rather than assumed.
- [ ] Tighten corroboration and provider-dependent narrowing guidance in `external-verification-and-source-trust.md`.
- [ ] Tighten recommendation posture in `communication-register.md` and `accurate-communication.md` so AI prefers shared logic before local exception and keeps exception usage evidence-earned.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Update one related playground case and any directly required reference surface.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.28`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- creating a new standalone rule chain when the existing owners can be refined
- turning strategic doctrine into a rigid command-style prohibition list
- hardcoding that supplier-specific fixes are always wrong
- weakening evidence discipline, accurate wording, anti-hallucination boundaries, or direct-continuation priority
- using local exceptions as the default recommendation without evidence
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners align to the P120 strategic posture refinement with no unresolved duplicate-doctrine overlap
- the updated playground case shows the strategy-before-patch behavior delta clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.28 / P120`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.28` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P120 is active.

Current checked progress:
- released baseline before P120 startup is `v10.27 / P119`
- the checked follow-up discussion identifies a strategic correction-posture gap where AI can still narrow too early into local scope from one failing case
- the selected improvement direction is to harden logic-first correction, evidence-proven scope selection, and exception-earned recommendation posture across the touched owners without turning the doctrine into command-style prohibitions
