# Phase 076-04 - Main/Subphase Boundary Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 076-04
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md)
> **Patch References:** [../patch/phase-main-subphase-boundary-refinement.patch.md](../patch/phase-main-subphase-boundary-refinement.patch.md)

---

## Objective

Refine phase identity selection so a major phase cannot become an open-ended umbrella just because later work shares a broad product area, owner chain, or historical lineage. Subphases should continue the same bounded execution gate; new main phases should open when the work has its own capability, output, verification gate, release boundary, or rollback boundary.

พูดง่าย ๆ: lineage ช่วยบอกความเกี่ยวข้อง แต่ไม่ควรขังงานใหม่ทั้งหมดไว้ใต้ phase ใหญ่เดิมตลอดไป.

---

## Why This Phase Exists

P076-02 added major-vs-subphase lineage selection so related follow-up work does not automatically become a new major phase. The user then identified the opposite failure mode from live NodeClaw phase/task behavior: work can remain under one old major phase through endless subphases even when the new slice has a distinct capability, gate, or rollout meaning.

This is a subphase of `076` because it refines the same phase identity selection owner introduced by P076-02. It is not a new first-class rule domain, but it tightens the boundary so existing-family lineage remains evidence rather than a permanent container.

---

## Entry Conditions

- P076-01 design-to-phase execution synthesis is complete.
- P076-02 major-vs-subphase lineage selection is complete.
- P076-03 phase-visible task linkage is complete.
- P086/v9.94 constructive dissent and anti-over-agreement refinement is complete, installed, pushed, and released.
- Active runtime count is 46.
- The user explicitly requested RULES improvement, runtime install, governed design/changelog/TODO/phase/patch sync, git push, release, and systematic phase planning.

---

## Implementation Plan

### 1) Tighten phase identity owner

- Update `phase-implementation.md`, its design, and changelog to v2.32.
- Add bounded-phase doctrine: a subphase must continue the same bounded execution gate, not only the same broad domain.
- Add phase saturation / umbrella escape signals for when a new main phase is clearer.
- State that lineage is evidence, not a prison.
- Clarify that same product area, same owner chain, or same historical phase family is insufficient by itself when the new work has a distinct output/gate/release/rollback meaning.

### 2) Sync master governed records

- Update `design/design.md` to v9.95 while preserving active runtime count 46.
- Update `changelog/changelog.md` with v9.95 release notes.
- Update `README.md` current-state guidance without turning it into a changelog dump.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and `patch/phase-main-subphase-boundary-refinement.patch.md`.

### 3) Install, verify, push, and release

- Install only README-listed active runtime rule files into `/home/node/.claude/rules/`.
- Verify README Bash and PowerShell arrays remain aligned at 46 active runtime files.
- Verify source/runtime parity and active runtime body sufficiency for all 46 active runtime files.
- Commit the v9.95 governed changes.
- Push `master`.
- Publish GitHub release `v9.95`.
- Run final post-release audit before closeout.

---

## Out of Scope

- No new active runtime rule file.
- No active runtime count increase.
- No direct management of NodeClaw phase files; NodeClaw was evidence for RULES behavior only.
- No hard rule that always prefers a new major phase.
- No hard rule that always prefers a subphase.
- No plugin/shared-board/team workflow doctrine change.
- No memory update for this RULES development wave.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.

---

## Affected Artifacts

### Refined active runtime rule chain

- `phase-implementation.md`

### Companion design and changelog chain

- `design/phase-implementation.design.md`
- `changelog/phase-implementation.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/phase-main-subphase-boundary-refinement.patch.md`
- `phase/phase-076-04-main-subphase-boundary-refinement.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P076-04 as active during source sync and completed only after source audit, runtime install parity/body sufficiency, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.95 as the master version authority when the wave completes.
- `changelog/phase-implementation.changelog.md` records `phase-implementation` v2.32.
- README presents current-state guidance and detailed improvement context without replacing changelog history.

---

## Verification

- [x] Phase identity owner chain contains bounded-phase, phase-saturation, and umbrella-escape doctrine.
- [x] Master records describe v9.95 and active runtime count 46 consistently.
- [x] README Bash and PowerShell install arrays still include exactly 46 active runtime rule files.
- [x] Runtime install parity passes for 46 active runtime rule files.
- [x] Active runtime body sufficiency passes for 46 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and released as `v9.95`.

---

## Exit Criteria

- Phase identity owner chain is synchronized at v2.32.
- P076-04 phase and patch records exist and link correctly.
- Master records describe v9.95 consistently.
- Active runtime count remains 46.
- Final source audit passes.
- Runtime install parity and body sufficiency pass for the 46 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.95`.

---

## Closeout Summary

P076-04 delivered bounded main/subphase boundary doctrine for the existing `phase-implementation` owner. The practical improvement is that future phase selection keeps real lineage visible without trapping distinct work inside an old umbrella phase when output, verification gate, release boundary, or rollback meaning diverges.

Verification:
- Source sync audit passed for README, master design/changelog, TODO, phase, patch, and the `phase-implementation` v2.32 chain.
- Runtime install copied only the 46 README-listed active runtime rules.
- Source/runtime parity and active runtime body sufficiency passed 46/46 with destination extras observed-only.
- `master` push and GitHub release `v9.95` were verified.

Next phase state: none selected.

---

## Risks and Rollback Notes

Risk:
- Umbrella-escape wording could be overread as forcing new main phases too often.

Mitigation:
- Keep lineage as meaningful evidence and require distinct output/gate/release/rollback signals before escaping an existing family.

Risk:
- Bounded-phase wording could weaken valid subphase continuity for real follow-up work.

Mitigation:
- Preserve subphase use when the work continues the same bounded execution gate, target output, verification gate, dependency chain, or rollback boundary.

Risk:
- Evidence from NodeClaw could be mistaken as authorization to edit NodeClaw phase files.

Mitigation:
- Treat NodeClaw as behavioral evidence only; this wave changes RULES source and runtime install only.

Rollback:
- Narrow the v9.95 bounded-phase wording through a governed rollback if it over-corrects toward new-major proliferation.
- Preserve P076-02 lineage-first behavior unless a separate rollback changes that parent behavior.
- Keep active runtime count at 46 unless a separate governed wave changes the active install set.
- Do not delete destination/runtime files outside the source-owned install set without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
