# P115 — Language-Aware Candidate-Goal Promotion Playground Case Update

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P115
> **Status:** Active / Source sync in progress
> **Target Release:** v10.23
> **Design References:**
> - [../design/design.md](../design/design.md) v10.23
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.23
> **Patch References:** [../patch/language-aware-candidate-goal-promotion-playground-case-update.patch.md](../patch/language-aware-candidate-goal-promotion-playground-case-update.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Release one new governed non-runtime playground case family that shows dominant-session-language ownership, candidate-goal-first successor recommendations, and selective promotion into advisory `/goal` form while keeping the playground outside the active 18-file runtime install payload.

---

## Why This Phase Exists

The released `v10.22 / P114` wave changed the runtime doctrine for language-aware candidate goals and promoted `/goal` suggestions, but the playground family still lacks a dedicated case that shows that behavior operationally.

Without a dedicated case:
- the new doctrine exists only in owner rules and release notes
- the behavior remains harder to inspect as an operational scenario
- the playground family misses one clear case family for language-aware goal promotion behavior

P115 exists to add one focused scenario family and ship it as a governed non-runtime playground update.

---

## Expected Output

- `playground/cases/case-15-language-aware-candidate-goal-promotion.md` exists as a new scenario family
- `playground/README.md` indexes the new case family
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.23 / P115`
- playground remains non-runtime and outside the 18-file runtime install payload
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- GitHub release `v10.23` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.22 / P114` with no active wave open before P115 startup.
- [ ] Add the new playground case file for language-aware candidate-goal promotion.
- [ ] Update the playground index and any directly affected design/master surfaces.
- [ ] Open P115 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Create and verify GitHub release `v10.23`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- changing the active 18-file runtime rule set
- adding `playground/` to runtime install payloads
- inventing transcript-grounded observed history for the new case
- broad playground family restructuring beyond this one new scenario family
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- `case-15-language-aware-candidate-goal-promotion.md` exists and is indexed in `playground/README.md`
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.23 / P115`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push and GitHub release `v10.23` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P115 is active.

Current checked progress:
- released baseline before P115 startup is `v10.22 / P114`
- the new case file and playground README index update are already present in source scope
- touched master/design/changelog/TODO/phase/patch surfaces are being synced for release
- runtime install-boundary proof, parity/body-sufficiency verification, push, and GitHub release proof are still pending at this stage
