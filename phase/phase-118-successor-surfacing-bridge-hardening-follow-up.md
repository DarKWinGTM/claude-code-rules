# P118 — Successor-Surfacing Bridge Hardening Follow-up

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P118
> **Status:** Completed / Released
> **Target Release:** v10.26
> **Design References:**
> - [../design/design.md](../design/design.md) v10.26
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.26
> **Patch References:** [../patch/successor-surfacing-bridge-hardening-follow-up.patch.md](../patch/successor-surfacing-bridge-hardening-follow-up.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so when AI already sees meaningful successor work it does not stop at a generic future note such as “ถ้าจะไปต่อ...” or “implementation wave ใหม่”, but instead selects the correct successor surface: direct continuation, candidate goals, advisory next goal, or advisory `/goal`.

---

## Why This Phase Exists

P117 improved candidate-goal surfacing and decision-ready explanation behavior, but follow-up analysis against real transcript cases still shows one residual miss pattern.

The residual pattern is not that AI cannot see successor work at all. The repeated failure is narrower: AI often recognizes that meaningful next work exists, but still closes with a broad future note or a soft offer instead of converting that successor state into the correct governed next-step shape.

The checked case set shows three common miss forms:
- a bounded governed successor is visible, but the answer still ends in prose instead of advisory `/goal`
- several meaningful next slices remain live, but the answer still collapses into a vague next-step sentence instead of compact candidate goals
- a successor label is broad (`implementation wave ใหม่`) and the assistant echoes that broad label instead of deriving the smallest bounded successor slice from checked execution surfaces

P118 exists to harden that bridge without reopening the broader response-style wave and without weakening direct-continuation priority where one safe path is already clearly selected.

---

## Expected Output

- `execution-and-goal-frame.md` encodes a stronger anti-generic-future-note bridge when meaningful successor work is already visible
- `phase-todo-artifact.md` encodes smaller bounded successor-slice derivation from checked phase/roadmap/TODO/current-state surfaces when upstream labels stay too broad
- `explanation-and-presentation.md` encodes a clearer closing boundary so closeout + generic future note is not treated as sufficient when a governed next-step surface should appear
- design companions and owner changelog parents sync to the touched runtime owners without duplicate-doctrine drift
- one related playground case is updated so the residual miss/fix stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.26 / P118`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- remote default branch reflects the follow-up playground/master-surface updates
- GitHub release `v10.26` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.25 / P117` with no active wave open before P118 startup.
- [ ] Open P118 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Tighten successor-surfacing bridge doctrine in `execution-and-goal-frame.md` without weakening direct continuation when one path clearly dominates.
- [ ] Tighten bounded successor-slice derivation in `phase-todo-artifact.md` so broad future labels are not echoed back unchanged when checked execution surfaces already provide a smaller next slice.
- [ ] Tighten closing/next-step presentation in `explanation-and-presentation.md` so generic future-note closeout is no longer enough when a governed next-step surface should be shown.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Update one related playground case and any directly required index/reference surface.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.26`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- reopening the broad non-trivial response-style wave except where a touched bridge owner truly requires a small closing-boundary refinement
- weakening evidence discipline, accurate wording, or anti-hallucination boundaries
- forcing every closeout to emit candidate goals or `/goal`
- reducing direct continuation priority where one safe next slice is already clearly selected
- adding `playground/` to runtime install payloads
- expanding the active runtime install set beyond 18 files
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched runtime owners align to the P118 follow-up refinement with no unresolved duplicate-doctrine overlap
- the updated playground case shows the residual miss/fix clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.26 / P118`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.26` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P118 is completed.

Current checked progress:
- released baseline before P118 startup was `v10.25 / P117`
- the checked real-case set justified the bounded follow-up and the selected owner set was refined without reopening the broader response-style wave
- the updated playground case is present in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch update, and GitHub release proof all passed
