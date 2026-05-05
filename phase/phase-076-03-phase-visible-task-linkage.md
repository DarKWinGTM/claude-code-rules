# Phase 076-03 - Phase-Visible Task Linkage

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 076-03
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md)
> **Patch References:** [../patch/phase-visible-task-linkage.patch.md](../patch/phase-visible-task-linkage.patch.md)

---

## Objective

Refine phase-backed live task-list behavior so Claude Code built-in task entries visibly carry active or clearly implied phase context instead of only aligning internally to that context.

พูดง่าย ๆ: ถ้างานกำลังทำตาม phase อยู่ task list ต้องมองเห็นได้ว่า task นั้นผูกกับ phase ไหน ไม่ใช่มีแค่ AI รู้ในใจว่า task นี้มาจาก phase.

---

## Why This Phase Exists

P076-01 made clear governed design able to drive phase posture, phase order, child files, and current-phase live tasks. P076-02 then made phase identity selection lineage-first so related follow-up work can become an existing-family subphase instead of defaulting to a new major phase.

The user identified the next practical gap: after phase planning is done and execution starts, built-in task-list entries may still be generic and not visibly reference the phase. The checked rule set already requires phase-aware task shaping, but it only prefers phase IDs when useful and does not require visible phase linkage in each task entry.

This is a subphase of `076` because it refines the same phase-to-live-execution bridge. It is not a new first-class rule domain and should not open a new major phase.

---

## Entry Conditions

- P076-01 design-to-phase execution synthesis is complete.
- P076-02 major-vs-subphase lineage selection is complete.
- P073-09/v9.84 runtime semantic compression refresh, runtime install, source/runtime parity, push, and release are complete.
- Active runtime count is 43.
- The user explicitly requested RULES improvement, runtime install, governed docs sync, git push, release, and systematic phase planning.

---

## Implementation Plan

### 1) Establish phase-visible task contract

- Update `phase-implementation.md`, its design, and changelog to require visible phase linkage when active or clearly implied phase context exists.
- Make the link acceptable in task subject or description.
- Prefer compact phase tokens such as `P076-03` in the subject when no stronger title grammar blocks it.
- Require `phase_ref` or equivalent description linkage when title grammar/prefix constraints make subject linkage awkward.

### 2) Sync live task-list and startup owners

- Update `todo-standards.md` and its companion design/changelog so phase-backed task entries visibly expose phase context instead of only aligning internally.
- Update `artifact-initiation-control.md` and its companion design/changelog so startup live task-list initialization under phase context creates phase-linked entries from the start.

### 3) Sync documentation and execution-continuity boundaries

- Update `project-documentation-standards.md` and its companion design/changelog so built-in task lists remain live tracking, not phase authority, while still pointing visibly to the governing phase context.
- Update `execution-continuity-and-mode-selection.md` and its companion design/changelog so continuation-created task entries preserve visible phase linkage.

### 4) Sync master records, runtime, and release

- Update `design/design.md` to v9.85 while preserving active runtime count 43.
- Update `changelog/changelog.md` with detailed v9.85 release notes.
- Update `README.md` as current-state guidance without destroying existing install/onboarding details.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and `patch/phase-visible-task-linkage.patch.md`.
- Install only README-listed 43 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime parity.
- Commit, push `master`, and publish GitHub release `v9.85` with detailed improvement notes.

---

## Out of Scope

- No new active runtime rule file.
- No active runtime count increase.
- No shared-board or plugin-owned task-title grammar change.
- No teammate / Agent Team doctrine change.
- No memory update for this RULES development wave.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.
- No hard requirement that every task subject uses one exact title format when a stronger title grammar applies.

---

## Affected Artifacts

### Refined active runtime rule chains

- `phase-implementation.md`
- `artifact-initiation-control.md`
- `todo-standards.md`
- `project-documentation-standards.md`
- `execution-continuity-and-mode-selection.md`

### Companion design and changelog chains

- `design/phase-implementation.design.md`
- `changelog/phase-implementation.changelog.md`
- `design/artifact-initiation-control.design.md`
- `changelog/artifact-initiation-control.changelog.md`
- `design/todo-standards.design.md`
- `changelog/todo-standards.changelog.md`
- `design/project-documentation-standards.design.md`
- `changelog/project-documentation-standards.changelog.md`
- `design/execution-continuity-and-mode-selection.design.md`
- `changelog/execution-continuity-and-mode-selection.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/phase-visible-task-linkage.patch.md`
- `phase/phase-076-03-phase-visible-task-linkage.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P076-03 as active during source sync and completed only after source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.85 as the master version authority when the wave completes.
- The touched chain changelogs record `phase-implementation` v2.27, `artifact-initiation-control` v1.8, `todo-standards` v2.22, `project-documentation-standards` v2.33, and `execution-continuity-and-mode-selection` v1.11.
- README presents current-state guidance and detailed improvement context without replacing changelog history.

---

## Verification

- [x] Phase-visible task linkage wording exists in the phase owner chain.
- [x] Live task-list and startup owners require visible phase linkage for phase-backed task entries.
- [x] Documentation and execution-continuity owners preserve the distinction that task lists do not define phases but must visibly point to active/implied phase context when used for phase-backed work.
- [x] Master records describe v9.85 and active runtime count 43 consistently.
- [x] README Bash and PowerShell install arrays still include exactly 43 active runtime rule files.
- [x] Runtime install parity passes for 43 active runtime rule files.
- [ ] Source/runtime release artifacts are pushed and released as `v9.85`.

---

## Exit Criteria

- Phase-visible task linkage owner chains are synchronized.
- P076-03 phase and patch records exist and link correctly.
- Master records describe v9.85 consistently.
- Active runtime count remains 43.
- Final source audit passes.
- Runtime install parity passes for the 43 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.85`.

---

## Risks and Rollback Notes

Risk:
- Visible phase-link wording could be overread as requiring one rigid subject format in every task system.

Mitigation:
- Allow subject or description linkage, preserve required title grammar, and keep shared-board/plugin grammar outside Main RULES doctrine.

Risk:
- Built-in task-list entries could be mistaken for phase authority.

Mitigation:
- Preserve the boundary that `phase/SUMMARY.md` and active phase files define phase semantics; task entries are live execution pointers, not authority.

Risk:
- Startup/task-list owners could duplicate phase identity ownership.

Mitigation:
- Keep phase identity selection under `phase-implementation.md` while adjacent owners only require visible linkage after active or implied phase context is selected.

Rollback:
- Narrow the v9.85 visible-linkage wording through a governed rollback if it over-constrains task wording.
- Preserve P076-01/P076-02 design-to-phase and lineage behavior unless a separate rollback changes that parent behavior.
- Keep active runtime count at 43 unless a separate governed wave changes the active install set.
- Do not delete destination/runtime files outside the source-owned install set without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
