# Phase 075-02 - Roadmap-Aware Completion and Next-Phase Proposal Behavior

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 075-02
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/response-closing-and-action-framing.design.md](../design/response-closing-and-action-framing.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/high-signal-communication.design.md](../design/high-signal-communication.design.md), [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md)
> **Patch References:** [../patch/roadmap-aware-completion-and-next-phase-proposal-behavior.patch.md](../patch/roadmap-aware-completion-and-next-phase-proposal-behavior.patch.md)

---

## Objective

Improve RULES closeout and phase-planning behavior so, after a governed objective is truly complete, the assistant can recommend the best-supported next phase or wave from checked roadmap surfaces without blocking selected safe continuation.

พูดง่าย ๆ: ถ้างานจบจริงแล้วและมีงานถัดไปที่เห็นจาก design/phase/TODO ควรเสนอว่าควรไปทางไหนต่อ แต่ถ้า phase ถัดไปถูกเลือกและปลอดภัยแล้วก็ให้เดินต่อ ไม่ต้องหยุดถามเกินจำเป็น.

---

## Why This Phase Exists

P075-01 made closeouts explain delivery, improvement, impact, verification, and next phase state. The remaining gap is that completion can still end without a useful next-phase recommendation even when `design`, `phase/SUMMARY.md`, `TODO.md`, or checked implementation state already show meaningful successor work.

The improvement must remain principle-based:
- continue selected, safe, unblocked work first
- recommend only at true completion boundaries
- keep unselected future work advisory
- ask narrowly when the successor is ambiguous, approval-sensitive, destructive, or materially divergent
- use roadmap or phase-matrix analysis when design evidence is broad enough to justify more than one current phase

---

## Entry Conditions

- User explicitly requested RULES improvement, install, governed docs sync, git push, and release.
- P075-01 already established phase-backed closeout feature/impact reporting.
- P076/P076-02/P076-03 already established design-to-phase synthesis, lineage-first phase identity, and visible phase-linked task behavior.
- P081-02 already established subagent research orchestration; P075-02 extends worker-fit scope to broad roadmap/phase-matrix analysis.
- Active runtime count stays 44; no new runtime rule is added.

---

## Runtime Active Rule Changes

- [x] Update `phase-implementation.md` so phase summaries can carry bounded roadmaps or phase matrices and phase closeout can recommend supported successor phases.
- [x] Update `execution-continuity-and-mode-selection.md` with a completion-to-roadmap bridge that separates selected continuation from advisory next work.
- [x] Update `response-closing-and-action-framing.md` with roadmap-aware completion and optional deep-dive offer behavior.
- [x] Update `explanation-quality.md` so easy-first explanations can be complete enough, recommend next roadmap work at true completion, and offer one specific deeper explanation path.
- [x] Update `answer-presentation.md` with compact roadmap-aware completion and optional deep-dive presentation patterns.
- [x] Update `high-signal-communication.md` so pruning does not remove required roadmap recommendations or useful deep-dive offers.
- [x] Update `native-worker-agent-routing-and-context-control.md` so broad roadmap/phase-matrix analysis can use focused worker lanes before leader raw absorption.

---

## Development Docs / Governed Record Sync Only

- [x] Sync paired design files for the seven touched runtime owners.
- [x] Sync paired changelog files for the seven touched runtime owners.
- [x] Sync `design/design.md` and `changelog/changelog.md` for v9.89.
- [x] Sync `README.md`, `TODO.md`, and `phase/SUMMARY.md`.
- [ ] Mark this phase and patch completed after source/runtime verification.
- [x] Install only the 44 README-listed active runtime rule files.
- [x] Verify source/runtime parity, body sufficiency, and destination extras as observed-only.
- [ ] Push `master` and publish GitHub release `v9.89`.

---

## Out of Scope

- Adding a new active runtime rule file.
- Weakening continuation-first execution when selected safe work can proceed.
- Turning every completion into a forced proposal block.
- Auto-promoting draft/proposal roadmap entries into active phases.
- Making README/TODO/phase/patch/design/changelog files runtime install targets.
- Managing, deleting, or classifying destination/runtime files outside the 44-file source-owned active runtime set.

---

## Affected Artifacts

Runtime active rule changes:
- `phase-implementation.md`
- `execution-continuity-and-mode-selection.md`
- `response-closing-and-action-framing.md`
- `explanation-quality.md`
- `answer-presentation.md`
- `high-signal-communication.md`
- `native-worker-agent-routing-and-context-control.md`

Development docs / governed record sync only:
- `design/phase-implementation.design.md`
- `design/execution-continuity-and-mode-selection.design.md`
- `design/response-closing-and-action-framing.design.md`
- `design/explanation-quality.design.md`
- `design/answer-presentation.design.md`
- `design/high-signal-communication.design.md`
- `design/native-worker-agent-routing-and-context-control.design.md`
- `changelog/phase-implementation.changelog.md`
- `changelog/execution-continuity-and-mode-selection.changelog.md`
- `changelog/response-closing-and-action-framing.changelog.md`
- `changelog/explanation-quality.changelog.md`
- `changelog/answer-presentation.changelog.md`
- `changelog/high-signal-communication.changelog.md`
- `changelog/native-worker-agent-routing-and-context-control.changelog.md`
- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/roadmap-aware-completion-and-next-phase-proposal-behavior.patch.md`

Runtime destination:
- active runtime copies only for the README-listed 44-file set

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

- [x] Seven runtime owners contain roadmap-aware completion, next-phase recommendation, optional deep-dive, or roadmap-worker routing guidance as applicable.
- [x] Companion design and changelog chains are updated for the seven touched owners.
- [x] Master README/design/changelog/TODO/phase records reflect v9.89 and P075-02.
- [x] README active runtime rule count remains 44.
- [x] Runtime install copies only active runtime rules.
- [x] Source/runtime parity and body-sufficiency checks pass for all 44 active runtime files.
- [x] Other-owner runtime files in the destination remain observed-only and untouched.
- [ ] Git push and GitHub release `v9.89` are verified.

---

## Exit Criteria

- P075-02 runtime owner updates are complete.
- Companion design/changelog records are synchronized.
- Master README/design/changelog/TODO/phase records are synchronized.
- Phase and patch records are marked completed with verification basis.
- Runtime install/parity/body-sufficiency checks pass for 44 active runtime rules only.
- No other-owner runtime destination file is managed or deleted.
- `master` is pushed and GitHub release `v9.89` exists.

---

## Risks and Rollback Notes

Risk: roadmap-aware completion could become a new stop ritual that interrupts safe selected continuation.

Risk: recommendations could overclaim future work as active execution.

Risk: optional deep-dive offers could become low-signal boilerplate if overused.

Rollback posture: narrow or revert only the P075-02 roadmap-aware completion, optional deep-dive, and roadmap-worker-routing wording while preserving P075-01 feature/impact closeout reporting, P076 design-to-phase synthesis, P081 worker routing, and the 44-file runtime install/body-sufficiency boundary.

---

## Next Possible Phases

No next phase is selected by this phase. If the roadmap-aware completion behavior proves too broad after runtime use, a later P075-03 narrowing phase may refine trigger thresholds without removing the completion-to-roadmap bridge.
