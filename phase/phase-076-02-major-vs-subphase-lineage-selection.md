# Phase 076-02 - Major-vs-Subphase Lineage Selection

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 076-02
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/artifact-initiation-control.design.md](../design/artifact-initiation-control.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md)
> **Patch References:** [../patch/phase-lineage-and-subphase-selection-refinement.patch.md](../patch/phase-lineage-and-subphase-selection-refinement.patch.md)

---

## Objective

Refine phase identity selection so phase-shaped follow-up work checks real lineage before opening a new major phase. The assistant should update the current phase, create an existing-family subphase, open a new major phase, or ask/record the lineage basis according to checked phase relationships instead of defaulting to the next major number.

พูดง่าย ๆ: งานต่อจาก phase เดิมไม่ควรถูกเปิดเป็น phase ใหญ่ใหม่โดยอัตโนมัติ; ต้องดูความสัมพันธ์ก่อนว่าเป็นงานในครอบครัวเดิม เป็น subphase หรือเป็น rollout ใหม่จริง ๆ.

---

## Why This Phase Exists

P076 added design-to-phase execution synthesis so clear governed design can drive phase posture, phase order, child files, and current-phase live tasks. The user then identified a practical continuation gap: when later work needs a phase file, the assistant often chooses a fresh major phase without sufficiently checking whether the work belongs under an existing phase family.

This is a subphase of `076` because it refines the phase workspace and phase identity behavior introduced by the design-to-phase synthesis wave. It is not a new first-class rule domain and should not become `084` merely because it is a new concern.

---

## Entry Conditions

- P076-01 design-to-phase execution synthesis is complete.
- P083/v9.82 is complete, installed, pushed, and released.
- Active runtime count is 43.
- User explicitly requested RULES improvement, runtime install, governed docs sync, git push, and detailed GitHub release notes.
- User explicitly wants principle-based criteria rather than a hard rule that always forces subphase usage.

---

## Implementation Plan

### 1) Refine phase identity owner

- Update `phase-implementation.md`, its design, and changelog to v2.26.
- Add the major-vs-subphase lineage gate.
- Define subphase-fit signals and major-phase-fit signals.
- Preserve the no-forced-subphase boundary.
- State that completed status does not automatically break lineage and new concern wording does not automatically justify a new major phase.

### 2) Sync adjacent owners

- Update `artifact-initiation-control` to v1.7 so phase `create now` delegates identity selection instead of implying a new major phase.
- Update `todo-standards` to v2.21 so live task shaping cannot silently allocate a new major phase.
- Update `project-documentation-standards` to v2.32 so governed records preserve phase-family lineage without taking over phase identity semantics.
- Update `execution-continuity-and-mode-selection` to v1.10 so execution momentum cannot allocate a new major phase without lineage handling.

### 3) Sync master records, runtime, and release

- Update `design/design.md` to v9.83 while preserving the active runtime count at 43.
- Update `changelog/changelog.md` with detailed v9.83 release notes.
- Update `README.md` as current-state guidance without destroying existing install/onboarding details.
- Update `TODO.md` and `phase/SUMMARY.md` for P076-02.
- Install only README-listed 43 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime parity.
- Commit, push `master`, and publish GitHub release `v9.83` with detailed improvement notes.

---

## Out of Scope

- No new active runtime rule file.
- No active runtime count increase.
- No hard rule that always uses subphases.
- No removal of valid new-major phase behavior when lineage is genuinely separate.
- No plugin/shared-board/team workflow doctrine changes.
- No memory update for this RULES development wave.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.

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
- `patch/phase-lineage-and-subphase-selection-refinement.patch.md`
- `phase/phase-076-02-major-vs-subphase-lineage-selection.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P076-02 as active during source sync and completed only after source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.83 as the master version authority.
- The touched chain changelogs record `phase-implementation` v2.26, `artifact-initiation-control` v1.7, `project-documentation-standards` v2.32, `todo-standards` v2.21, and `execution-continuity-and-mode-selection` v1.10.
- README presents current-state guidance and detailed improvement context without replacing changelog history.

---

## Verification

- [x] Phase identity owner chains have lineage-first major-vs-subphase selection wording.
- [x] Adjacent owners defer phase identity selection to `phase-implementation.md` instead of allocating a new major phase by startup posture, task shaping, documentation sync, or execution momentum.
- [x] Master records describe v9.83 and active runtime count 43 consistently.
- [x] README Bash and PowerShell install arrays still include exactly 43 active runtime rule files.
- [x] Runtime install parity passes for 43 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and released as `v9.83`.

---

## Closeout Summary

P076-02 delivered lineage-first phase identity selection for phase-shaped follow-up work. The active behavior now checks whether work should update the current phase, become an existing-family subphase, open a genuinely separate major phase, or ask/record the lineage basis instead of defaulting to a fresh major number.

Verification basis: source sync audit passed, README Bash and PowerShell install arrays remained aligned at 43 active runtime rules, runtime install parity passed with no active hash mismatches, master push completed, and GitHub release `v9.83` was published.

---

## Exit Criteria

- Phase lineage owner chains are synchronized.
- P076-02 phase and patch records exist and link correctly.
- Master records describe v9.83 consistently.
- Active runtime count remains 43.
- Final source audit passes.
- Runtime install parity passes for the 43 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.83`.

---

## Risks and Rollback Notes

Risk:
- Lineage wording could be overread as forcing subphases for unrelated work.

Mitigation:
- Preserve explicit major-phase-fit signals and the no-forced-subphase boundary.

Risk:
- Startup or task-list rules could accidentally become phase identity owners.

Mitigation:
- Keep `phase-implementation.md` as the identity owner and make adjacent owners defer to it.

Risk:
- Existing completed phase status could be misread as a lineage break.

Mitigation:
- State that completed parent or sibling phases may still define the same rollout family.

Rollback:
- Narrow the v9.83 lineage wording through a governed rollback if it over-constrains phase identity selection.
- Preserve P076-01 design-to-phase synthesis unless a separate rollback changes that parent behavior.
- Keep active runtime count at 43 unless a separate governed wave changes the active install set.
- Do not delete destination/runtime files outside the source-owned install set without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
