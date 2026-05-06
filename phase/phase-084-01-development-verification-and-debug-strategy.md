# Phase 084-01 - Development Verification and Debug Strategy

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 084-01
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/development-verification-and-debug-strategy.design.md](../design/development-verification-and-debug-strategy.design.md)
> **Patch References:** [../patch/development-verification-and-debug-strategy.patch.md](../patch/development-verification-and-debug-strategy.patch.md)

---

## Objective

Create a first-class RULES owner that makes debug/testing/TestKit verification strategy a normal part of non-trivial coding work without turning every small edit into a rigid testing ceremony.

พูดง่าย ๆ: งาน coding ที่มี behavior จริงต้องมีแผนพิสูจน์ผล ไม่ใช่แก้ไฟล์แล้วบอกว่าเสร็จ แต่ TestingKit เป็นตัวเลือกเชิงกลยุทธ์ ไม่ใช่ของที่ต้องสร้างทุกครั้ง.

---

## Why This Phase Exists

The user identified a coding-workflow gap: AI can improve accuracy and reduce bugs by planning debug/testing/TestKit verification as part of development. Existing rules cover maintainable code structure, evidence wording, phase closeout, and continuation, but no first-class owner defines the coding-time verification strategy itself.

P084-01 is a new major phase because it creates a new first-class runtime rule domain: development verification/debug/testing strategy.

---

## Entry Conditions

- P082/P083 maintainable-code structure and helper/comment discipline are complete.
- P076-03 phase-visible task linkage is complete.
- Current master state is v9.85 with 43 active runtime rules.
- User explicitly requested RULES improvement, runtime install, governed docs sync, git push, release, and systematic phase planning.

---

## Implementation Plan

### 1) Create the verification strategy owner

- Create `development-verification-and-debug-strategy.md`.
- Create companion design and changelog files.
- Define proportionate verification depth, debug strategy, TestKit/scenario decision, and coding closeout evidence boundaries.

### 2) Integrate adjacent owners

- Update `maintainable-code-structure-and-decomposition` to defer verification strategy to the new owner.
- Update `accurate-communication` to align coding closeout wording with verification evidence.
- Update `phase-implementation` to include Development Verification / TestKit Coverage for phase-backed coding work.
- Update `todo-standards` to keep verification slices visible for non-trivial coding tasks.
- Update `project-documentation-standards` to record repository-level verification coverage expectations for governed coding phases.
- Update `execution-continuity-and-mode-selection` so implementation does not stop before verification when verification is the implied safe next slice.

### 3) Sync governed master records

- Update `design/design.md` to v9.86 and active runtime count 44.
- Update `changelog/changelog.md` with v9.86 release notes.
- Update `README.md` current-state guidance and install arrays.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and the patch record.

### 4) Install, verify, push, release

- Install only README-listed 44 active runtime rules into `/home/node/.claude/rules/`.
- Verify source/runtime parity.
- Commit, push `master`, and publish GitHub release `v9.86`.

---

## Out of Scope

- No mandatory TestKit scenario for every task.
- No live/provider/runtime checks without approval and environment readiness.
- No replacement of project-specific test architecture.
- No broad runtime topology mutation.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.

---

## Affected Artifacts

### New active runtime rule chain

- `development-verification-and-debug-strategy.md`
- `design/development-verification-and-debug-strategy.design.md`
- `changelog/development-verification-and-debug-strategy.changelog.md`

### Refined adjacent active runtime rule chains

- `maintainable-code-structure-and-decomposition.md`
- `accurate-communication.md`
- `phase-implementation.md`
- `todo-standards.md`
- `project-documentation-standards.md`
- `execution-continuity-and-mode-selection.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/development-verification-and-debug-strategy.patch.md`
- `phase/phase-084-01-development-verification-and-debug-strategy.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P084-01 as active during source sync and completed only after source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.86 as the master version authority when the wave completes.
- The touched chain changelogs record the new v1.0 owner and adjacent owner version bumps.
- README presents current-state guidance and install arrays for 44 active runtime rules.

---

## Verification

- [x] New rule/design/changelog triad exists and aligns at v1.0.
- [x] Adjacent owner integrations are synchronized and version-aligned.
- [x] Master records describe v9.86 and active runtime count 44 consistently.
- [x] README Bash and PowerShell install arrays include exactly 44 active runtime rule files.
- [x] Runtime install parity passes for 44 active runtime rule files.
- [ ] Source/runtime release artifacts are pushed and released as `v9.86`.

---

## Exit Criteria

- Development verification strategy owner chain exists.
- Adjacent owner integrations are synchronized.
- Master records describe v9.86 consistently.
- Active runtime count becomes 44.
- Runtime install parity passes for 44 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.86`.

---

## Risks and Rollback Notes

Risk:
- Verification strategy could be overread as mandatory full TestKit work for every edit.

Mitigation:
- Keep the rule strategy-based, proportional, and explicit that TestKit is an option for scenario-like work, not a universal artifact.

Risk:
- Fake/local checks could be overclaimed as live proof.

Mitigation:
- Preserve evidence-boundary tables and accurate-communication integration.

Rollback:
- Narrow trigger wording before removing the new owner.
- Preserve edit-only/fake-local overclaim prevention if any rollback happens.
- Remove the rule from install arrays and master inventory only through governed rollback.
- Do not delete destination/runtime files outside the source-owned install set without separate explicit authorization.

---

## Next Possible Phases

- None selected.
