# P119 — Active-Exchange Language Alignment Hardening Follow-up

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P119
> **Status:** Completed / Released
> **Target Release:** v10.27
> **Design References:**
> - [../design/design.md](../design/design.md) v10.27
> **Patch References:** [../patch/active-exchange-language-alignment-hardening-follow-up.patch.md](../patch/active-exchange-language-alignment-hardening-follow-up.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so goal-shaped and recommendation-shaped natural-language scaffold follows the user's active exchange language by default, explicit language requests act as a stronger override, and exact literals such as `/goal`, file paths, identifiers, version tags, and query parameters remain preserved without turning the whole block into an exact literal.

---

## Why This Phase Exists

The released `v10.26 / P118` baseline already hardened successor-surfacing behavior, but the checked follow-up discussion still shows one narrower language-alignment miss.

The problem is not that RULES lack language-alignment doctrine entirely. The repeated failure is narrower: AI can localize wrapper wording or part of the visible goal surface, but still leave the promoted `/goal` body or recommendation body in another language even when the user's active working language across the current exchange is already clear.

This miss also exposes a boundary problem. Exact literals such as `/goal`, file paths, identifiers, version tags, and query parameters do need preservation, but the assistant can over-preserve by treating the whole command body as if it were one exact literal.

P119 exists to harden that language-selection boundary without reopening the broader response-style wave, without forcing Thai specifically, and without weakening direct-continuation, evidence-discipline, or anti-hallucination behavior.

---

## Expected Output

- `execution-and-goal-frame.md` encodes active-exchange language as the default for goal-shaped next-step surfaces while keeping explicit language requests as a stronger override
- `phase-todo-artifact.md` encodes concept-slot translation so `/goal` scaffold text localizes while exact literals remain preserved at token level rather than block level
- `communication-register.md`, `accurate-communication.md`, and `explanation-and-presentation.md` encode that wrapper labels and goal/recommendation body must stay language-aligned end-to-end rather than only at the wrapper layer
- one related playground case is updated so the wrapper-only-translation miss/fix stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.27 / P119`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- remote default branch reflects the follow-up playground/master-surface updates
- GitHub release `v10.27` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.26 / P118` with no active wave open before P119 startup.
- [ ] Open P119 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Tighten active-exchange language selection in `execution-and-goal-frame.md` without weakening direct continuation or exact-literal preservation.
- [ ] Tighten concept-slot translation in `phase-todo-artifact.md` so scaffold text localizes while exact literals remain preserved at token level.
- [ ] Tighten end-to-end language-alignment wording in `communication-register.md`, `accurate-communication.md`, and `explanation-and-presentation.md` so wrapper-only translation is no longer sufficient.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Update one related playground case and any directly required reference surface.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.27`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- creating a new standalone rule chain when the existing owners can be refined
- hardcoding that output must be Thai
- treating the whole `/goal` block as an exact literal
- weakening evidence discipline, accurate wording, anti-hallucination boundaries, or direct-continuation priority
- forcing every closeout to emit candidate goals or `/goal`
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched runtime owners and communication/presentation owners align to the P119 refinement with no unresolved duplicate-doctrine overlap
- the updated playground case shows the wrapper-only-translation miss/fix clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.27 / P119`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.27` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P119 is completed.

Current checked progress:
- released baseline before P119 startup was `v10.26 / P118`
- the checked follow-up discussion identified an active-exchange language-alignment miss in goal-shaped output without proving a larger doctrine absence
- the selected improvement direction hardened the active-exchange-language default, explicit-request override, and exact-literal token boundary across the touched owners without reopening the broader response-style wave
- the updated playground case is present in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch update, and GitHub release proof all passed
