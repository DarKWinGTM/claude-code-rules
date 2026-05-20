# P116 — End-to-End Language-Aligned Goal Surface Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P116
> **Status:** Active / Source sync in progress
> **Target Release:** v10.24
> **Design References:**
> - [../design/design.md](../design/design.md) v10.24
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.24
> **Patch References:** [../patch/end-to-end-language-aligned-goal-surface-refinement.patch.md](../patch/end-to-end-language-aligned-goal-surface-refinement.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so candidate goals, advisory `/goal`, recommendation labels, and recap/closing lines follow the dominant session language end-to-end while preserving advisory `/goal`, exact-literal boundaries, the active 18-file runtime install scope, and the non-runtime playground boundary.

---

## Why This Phase Exists

The released `v10.22 / P114` wave taught RULES to make candidate goals and promoted `/goal` language-aware, and `v10.23 / P115` added one playground case for that doctrine.

The remaining gap is surface completeness: current doctrine says the promoted command should follow the dominant session language, but some output templates and examples still hardcode English wrapper labels such as `Suggested /goal:` and slot labels such as `Done when` / `Prove with` even when the user's session language is Thai-first.

Without this refinement:
- the runtime doctrine and the visible output examples disagree
- the assistant can still emit English-shell + Thai-content goal output
- the playground family still lacks one dedicated scenario that shows wrapper-label language alignment as operational behavior

P116 exists to make the language surface end-to-end consistent and release that refinement as one governed runtime + playground update.

---

## Expected Output

- touched runtime owners teach dominant-session-language behavior across wrapper labels, candidate-goal headings, promoted `/goal`, and recap/closing lines
- exact literals such as `/goal`, file paths, version tags, and code identifiers stay explicitly preservable when they should remain exact
- one new governed non-runtime playground case family exists and is indexed
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.24 / P116`
- playground remains non-runtime and outside the 18-file runtime install payload
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- GitHub release `v10.24` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.23 / P115` with no active wave open before P116 startup.
- [ ] Update the language-surface doctrine in the touched runtime owners.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Add the new playground case file and update the playground index.
- [ ] Open P116 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Create and verify GitHub release `v10.24`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- changing the active 18-file runtime rule set
- adding `playground/` to runtime install payloads
- changing advisory `/goal` into selected execution
- translating exact literals that should remain exact
- broad playground family restructuring beyond this one new scenario family
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched runtime owners, design companions, and owner changelog parents align to the P116 language-surface refinement
- the new playground case exists and is indexed in `playground/README.md`
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.24 / P116`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push and GitHub release `v10.24` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P116 is active.

Current checked progress:
- released baseline before P116 startup is `v10.23 / P115`
- runtime doctrine gaps are already identified in the checked owner files and output templates
- P116 startup surfaces are being opened for the runtime + playground refinement
- runtime install-boundary proof, parity/body-sufficiency verification, push, and GitHub release proof are still pending at this stage
