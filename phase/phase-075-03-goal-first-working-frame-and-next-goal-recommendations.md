# Phase 075-03 - Goal-First Working Frame and Next-Goal Recommendations

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 075-03
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/goal-set-review-and-priority-balance.design.md](../design/goal-set-review-and-priority-balance.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/response-closing-and-action-framing.design.md](../design/response-closing-and-action-framing.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/high-signal-communication.design.md](../design/high-signal-communication.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md)
> **Patch References:** [../patch/goal-first-working-frame-and-next-goal-recommendations.patch.md](../patch/goal-first-working-frame-and-next-goal-recommendations.patch.md)

---

## Objective

Improve RULES execution behavior so non-trivial work establishes a goal-aware working frame with goal, output, and gate when that prevents drift, supports verification, or improves next-goal recommendations, without turning goal wording into a rigid template or blocking selected safe continuation.

พูดง่าย ๆ: Goal เป็นเข็มทิศ ไม่ใช่พิธีกรรม ต้องช่วยให้ AI รู้ว่ากำลังพางานไปถึงอะไร และเมื่อจบจริงควรเสนอ next goal ที่มีหลักฐานรองรับ.

---

## Runtime Active Rule Changes

- [x] Update `goal-set-review-and-priority-balance.md` as the primary owner for goal-first working frames, goal hierarchy, goal/output/gate, triggered visibility, and anti-ritual boundaries.
- [x] Update `execution-continuity-and-mode-selection.md` so execution continuity tracks current goal, selected next goal, and completion gate without interrupting safe continuation.
- [x] Update `response-closing-and-action-framing.md` so closeout can recommend a supported next goal, not only a next phase/wave.
- [x] Update `explanation-quality.md` so goal-first framing stays easy to understand and proportional.
- [x] Update `answer-presentation.md` with compact goal-aware presentation patterns for non-trivial work.
- [x] Update `high-signal-communication.md` so pruning preserves useful goal/output/gate and next-goal recommendations while removing boilerplate.
- [x] Update `phase-implementation.md` so phase roadmaps and phase matrices can carry goal/output/gate semantics.
- [x] Update `todo-standards.md` so non-trivial live task entries stay outcome/goal-shaped rather than command-only.

---

## Development Docs / Governed Record Sync Only

- [x] Sync paired design files for the touched runtime owners.
- [x] Sync paired changelog files for the touched runtime owners.
- [x] Sync `design/design.md` and `changelog/changelog.md` for v9.90.
- [x] Sync `README.md`, `TODO.md`, and `phase/SUMMARY.md`.
- [x] Mark this phase and patch completed after git push and release verification.
- [x] Install only the 44 README-listed active runtime rule files.
- [x] Verify source/runtime parity, body sufficiency, and destination extras as observed-only.
- [x] Push `master` and publish GitHub release `v9.90`.

---

## Out of Scope

- Adding a new active runtime rule file.
- Forcing visible Goal blocks in every simple answer or trivial task.
- Turning goal-setting into a stop ritual between selected safe phases.
- Inventing next goals when checked design/TODO/phase/implementation surfaces do not support them.
- Managing, deleting, or classifying runtime destination files outside the 44-file source-owned active runtime set.

---

## Development Verification / TestKit Coverage

This is RULES governance/runtime-doctrine work, not product code. The verification route is source consistency, runtime install parity, body-sufficiency validation, and release-surface audit rather than TestKit scenario creation.

Verification route:
- `not_applicable_with_reason` for code TestKit: no executable product behavior is changed
- `source_consistency`: rule/design/changelog version alignment and master surface sync
- `runtime_parity`: README-listed 44 active runtime files copied to `~/.claude/rules/` with hash parity
- `body_sufficiency`: no README-listed active runtime file is metadata-only
- `release_audit`: git push and GitHub release verification

---

## Verification

- [x] Runtime owners contain goal-first, triggered-visibility, anti-ritual, continuation-first, and evidence-grounded next-goal guidance as applicable.
- [x] Companion design and changelog chains are updated for the touched owners.
- [x] Master README/design/changelog/TODO/phase records reflect v9.90 and P075-03.
- [x] README active runtime rule count remains 44.
- [x] Runtime install copies only active runtime rules.
- [x] Source/runtime parity and body-sufficiency checks pass for all 44 active runtime files.
- [x] Other-owner runtime files in the destination remain observed-only and untouched.
- [x] Git push and GitHub release `v9.90` are verified.

---

## Exit Criteria

- P075-03 runtime owner updates are complete.
- Companion design/changelog records are synchronized.
- Master README/design/changelog/TODO/phase records are synchronized.
- Phase and patch records are marked completed with verification basis.
- Runtime install/parity/body-sufficiency checks pass for 44 active runtime rules only.
- No other-owner runtime destination file is managed or deleted.
- `master` is pushed and GitHub release `v9.90` exists.

---

## Risks and Rollback Notes

Risk: goal-first wording could become rigid boilerplate that appears in every simple answer.

Risk: next-goal recommendations could overclaim future work as selected execution.

Risk: goal-setting could interrupt selected safe continuation.

Rollback posture: narrow or revert only the P075-03 goal-first / next-goal wording while preserving P075-02 roadmap-aware completion, P075-01 feature/impact closeout reporting, P076 design-to-phase synthesis, P081 worker routing, and the 44-file runtime install/body-sufficiency boundary.

---

## Closeout Summary

P075-03 delivered goal-first working-frame behavior for the RULES runtime: non-trivial work can use goal/output/gate navigation when it prevents drift or improves verification, selected safe continuation remains unblocked, and next-goal recommendations require checked evidence instead of ritualized guessing. The 44-file active runtime set stayed unchanged, source/runtime parity and body sufficiency passed 44/44 with destination extras observed-only, `master` was pushed, and GitHub release `v9.90` was published.

---

## Next Possible Phases

No next phase is selected by this phase. If goal-first behavior later becomes too visible or too quiet in runtime use, a later P075-04 threshold tuning phase may refine trigger visibility without removing the goal-aware working frame.
