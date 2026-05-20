# P114 — Language-Aware Candidate Goal and Goal-Command Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P114
> **Status:** Active / Source sync in progress
> **Target Release:** v10.22
> **Design References:**
> - [../design/design.md](../design/design.md) v10.22
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/language-aware-candidate-goal-and-goal-command-doctrine.patch.md](../patch/language-aware-candidate-goal-and-goal-command-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so `/goal` suggestions follow the dominant session language by default, successor recommendations are expressed as candidate goals before raw choice lists, and only the best-supported governed repo candidate is selectively promoted into advisory `/goal` command form under the existing governed-work-only boundary.

---

## Why This Phase Exists

The released `v10.21 / P113` wave hardened governed-work-only `/goal` sourcing, but it still leaves two behavior gaps.

The first gap is language ownership: `/goal` can still drift toward English-shaped command wording even when the user's active working language is Thai-first.

The second gap is successor-shape ambiguity: when several next directions remain live, RULES can still fall back to plain next-step choice wording instead of using candidate goals as the more execution-aware recommendation shape.

P114 exists to make `/goal` language-aware and to insert a candidate-goal layer between generic next-step choice lists and promoted governed `/goal` commands.

---

## Expected Output

- exact trigger conditions state how dominant session language owns candidate-goal and promoted `/goal` wording by default
- exact trigger conditions state when successor recommendations should be shaped as candidate goals instead of plain unlabeled choices
- exact trigger conditions state when one candidate goal may be promoted into advisory governed `/goal` form
- touched runtime/design/changelog owners align to the new language-aware candidate-goal doctrine
- at least two concrete Thai-first governed examples exist: one non-release and one release-closeout
- master README/design/changelog/TODO/phase/patch surfaces open and later close P114 consistently
- active runtime install scope remains 18
- runtime install, source/runtime parity, source/destination body sufficiency, and `git diff --check` pass before release closeout
- GitHub release `v10.22` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.21 / P113` with no active wave open before P114 startup.
- [ ] Update the wording and presentation owners for dominant-session-language candidate-goal and promoted-`/goal` behavior.
- [ ] Update the execution/sourcing owners for candidate-goal-first successor recommendation and selective promotion into governed `/goal`.
- [ ] Sync touched owner design companions and owner changelog parents.
- [ ] Open P114 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Preserve at least two Thai-first governed examples: one non-release and one release-closeout.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Create and verify GitHub release `v10.22`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- forcing English default wording when the session is clearly Thai-first
- promoting every candidate goal into `/goal` command form
- turning candidate goals into a long template dump or mini-spec
- changing advisory `/goal` behavior into selected execution
- expanding the active runtime install set beyond 18 root runtime rules
- drifting into unrelated plugin/runtime work outside this repo

---

## Completion Gate

- active doctrine explicitly defines dominant-session-language ownership for candidate goals and promoted `/goal`
- active doctrine explicitly defines candidate-goal shaping for several live successor directions
- active doctrine explicitly defines selective promotion from candidate goal to governed `/goal`
- at least two Thai-first governed examples exist for audit and review
- touched runtime/design/changelog files align to `v10.22 / P114`
- active runtime install scope remains 18 and install/parity/body-sufficiency checks pass
- `git diff --check` passes
- branch push and GitHub release `v10.22` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P114 is active.

Current checked progress:
- the released baseline is `v10.21 / P113`
- the isolated worktree remains the active execution surface
- touched runtime owners are in progress for language-aware candidate-goal and promoted-`/goal` doctrine
- release verification, runtime install/parity, push, and GitHub release proof are still pending at this stage
