# P117 — Proactive Goal Surfacing and Decision-Ready Response Style Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P117
> **Status:** Active / Owner sync in progress
> **Target Release:** v10.25
> **Design References:**
> - [../design/design.md](../design/design.md) v10.25
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.25
> **Patch References:** [../patch/proactive-goal-surfacing-and-decision-ready-response-style-refinement.patch.md](../patch/proactive-goal-surfacing-and-decision-ready-response-style-refinement.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so AI surfaces next-step options as candidate goals more appropriately at real decision boundaries and so default non-trivial responses become easy-first, compact-but-complete, scanable, identifier-meaning-first, evidence-layer-clear, and decision-ready without creating duplicate doctrine, drift, or ritualized trivial-answer overhead.

---

## Why This Phase Exists

Two gaps are now visible in the released baseline.

First, goal-oriented next-step surfacing is still too selective. Current doctrine strongly prefers direct continuation and closeout-only successor framing, which means several materially different next directions are often collapsed into one best path before the user sees candidate goals.

Second, the current communication owners already support easy-first explanation, scanable structure, human-readable wording, identifier glosses, and evidence-calibrated wording, but they do not yet encode the requested default non-trivial answer shape clearly enough as one normalized owner-aligned behavior. The result is that answers can still be correct yet feel either too abrupt or too diffuse, and multi-axis explanations do not always escalate into the small-table + grouped structure soon enough.

P117 exists to tighten those owners without creating new rule chains and to make the combined behavior inspectable as one governed runtime + playground release.

---

## Expected Output

- touched runtime owners encode more proactive candidate-goal surfacing at real decision boundaries without weakening direct-continuation behavior when one path clearly dominates
- touched communication/presentation owners encode the default non-trivial answer shape as easy-first, compact-but-complete, scanable, small-table-when-useful, identifier-meaning-first, evidence-layer-clear, and concise-decision-ready
- evidence discipline remains strict and owner boundaries remain normalized rather than duplicated
- one new governed non-runtime playground case family exists and is indexed
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.25 / P117`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- remote default branch reflects the new playground case and touched master surfaces
- GitHub release `v10.25` is created and verified before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.24 / P116` with no active wave open before P117 startup.
- [ ] Tighten goal-surfacing doctrine in the correct owners without duplicating `/goal` or candidate-goal policy across unrelated surfaces.
- [ ] Tighten default non-trivial response-style doctrine in the correct communication/presentation owners without weakening evidence discipline.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Add one new playground case file and update the playground index.
- [ ] Open P117 master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.25`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- creating a new standalone rule chain when an existing owner can be refined
- weakening evidence discipline, accurate wording, or anti-hallucination boundaries
- forcing every answer to be long or table-shaped
- turning trivial tasks into a ritualized structure-first response flow
- adding `playground/` to runtime install payloads
- expanding the active runtime install set beyond 18 files
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched runtime owners, communication/presentation owners, and any necessary boundary owners align to the P117 refinement with no unresolved duplicate-doctrine overlap
- the new playground case exists and is indexed in `playground/README.md`
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.25 / P117`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.25` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P117 is active.

Current checked progress:
- released baseline before P117 startup is `v10.24 / P116`
- owner evidence for both behavior gaps is already checked in runtime communication/presentation/evidence surfaces
- P117 startup surfaces are being opened for the combined runtime + playground refinement
- runtime install-boundary proof, parity/body-sufficiency verification, push/default-branch update, and GitHub release proof are still pending at this stage
