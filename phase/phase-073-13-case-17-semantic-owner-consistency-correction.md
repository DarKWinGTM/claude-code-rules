# Phase 073-13 - Case 17 Semantic-Owner Consistency Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-13
> **Status:** Active — release candidate preparation
> **Target Release:** v10.61
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md), [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md), [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md)
> **Patch References:** none

---

## Objective

Correct the stale semantic-owner assignments that remain inside Case 17 after v10.60, verify the complete scenario as one semantic unit, and publish the bounded documentation correction as v10.61 without changing Runtime Rules, their design/per-rule changelog companions, installers, fixtures, or the root runtime installation.

พูดง่าย ๆ: Runtime Rules ถูกแล้ว แต่ Case 17 ยังมีข้อความเก่าที่ทำให้ execution หรือ phase/TODO ดูเหมือนเป็น owner ของการสร้าง `/goal` และ route support; phase นี้แก้เฉพาะ scenario และพิสูจน์ทั้งไฟล์ก่อน release.

## Lineage Decision

- P073-12 is completed and immutable with v10.60.
- The defect is inside the P073-12 goal-owner scenario-verification gate, not a new capability or Runtime Rule family.
- The correction preserves the same 19-Rule owner-boundary and release-proof family.
- Therefore `073-13` is the smallest truthful existing-family child; reopening P073-12 or creating a new major would misstate lineage.

## Selected Owner Model

```text
execution-and-goal-frame
→ selects direct continuation / candidate goals / advisory eligibility / clarification / none

goal-authoring-and-route-support
→ receives the selected posture
→ owns bounded goal construction, subordinate route support, durable plan lifecycle, and /plan overflow

phase-todo-artifact
→ supplies checked execution evidence and selected-goal phase/task linkage only

explanation-and-presentation
→ renders the selected posture only
```

A durable `Plan reference:` remains invalid until a route-only file exists and was verified. When present, `/goal` precedes `Plan reference:` inside the same copied artifact. Case 17 creates no durable route file and therefore emits no actual `Plan reference:`.

## Exact Allowlist

The candidate changes exactly nine paths:

1. `../playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md`
2. `phase-073-13-case-17-semantic-owner-consistency-correction.md`
3. `SUMMARY.md`
4. `../TODO.md`
5. `../changelog/changelog.md`
6. `../changelog/changelog/v10.61-case-17-semantic-owner-consistency-correction.changelog.md`
7. `../README.md`
8. `history/2026-08-09.md`
9. `../todo/history/2026-08-09.md`

`TODO.md`, `phase/SUMMARY.md`, and `changelog/changelog.md` preserve mode `100755`; the other paths use or preserve `100644`. No rename, deletion, symlink, submodule, binary, matrix, or coverage change is allowed.

## Work Lanes

### Lane 1 - Scenario correction

- correct the Case 17 governing-rule owner map
- attribute pre-goal route synthesis to goal-authoring after execution selects posture
- keep phase/TODO as checked-evidence and selected-goal-linkage provider only
- keep presentation rendering-only
- remove owner-overloaded `/plan` wording and prevent an invalid `Plan reference:` example

### Lane 2 - Governance synchronization

- update compact phase/TODO/changelog/README current-state anchors
- append daily movement without rewriting prior history
- create one v10.61 release shard
- keep patch posture `none` because the one-scenario semantic diff is directly reviewable

### Lane 3 - Verification and canonical convergence

- verify full-file positive and forbidden-negative assertions
- verify exact allowlist, modes, links, and `git diff --check`
- prove all Runtime Rule/design/per-rule changelog/installer/fixture bytes unchanged
- run unchanged Bash/PowerShell fixture matrices and disposable installation
- synchronize only the verified nine paths to canonical source
- hash-check canonical/root Runtime Rule parity without reinstalling

### Lane 4 - Publication and closeout

- publish clean public `master`
- create immutable annotated `v10.61` and GitHub Release
- verify a fresh public tag clone and v10.60 immutability
- publish a documentation-only closeout commit without moving v10.61

## Development Verification / TestKit Coverage

Selected route: full Case 17 semantic assertion plus independent whole-file review, exact diff/mode/link checks, protected-byte comparison, unchanged fixture matrices, disposable installation, canonical parity, fresh-public-master/tag verification, and GitHub Release identity.

Required positive assertions:

- execution selects posture and hands it off
- goal-authoring constructs the selected goal and owns subordinate route support
- goal-authoring owns durable plan verification, artifact order, and `/plan` overflow
- phase/TODO supplies checked evidence and selected-goal linkage only
- presentation renders without selecting or promoting
- helper output remains subordinate and is not completion proof

Forbidden assertions:

- execution owns goal construction, route synthesis, durable plan lifecycle, or `/plan` overflow
- phase/TODO shapes/promotes candidates, plans advisory `/goal`, owns route support, or emits `Plan reference:`
- presentation selects or promotes posture
- goal-authoring independently promotes an unselected candidate
- an unwritten/unverified `Plan reference:` is emitted

Protected unchanged surfaces:

- all 19 Runtime Rules
- all 19 Runtime Rule designs and per-rule changelogs
- Bash/PowerShell installers and fixture scripts
- P073-12 phase, v10.60 patch, and v10.60 release shard
- canonical and installed root Runtime Rules

## Out of Scope

- Runtime Rule, design, or per-rule changelog changes
- runtime version bumps or installation
- installer/fixture implementation changes
- playground matrix/coverage changes
- README restructuring
- editing completed P073-12/v10.60 artifacts
- backup-branch mutation
- deletion, quarantine cleanup, automatic fallback, or restoration

## Risks and Containment

Risks:
- positive-anchor checks can pass while contradictory scenario text remains
- command-surface “owner” wording can be confused with Runtime Rule semantic ownership
- candidate documentation can claim publication evidence before it exists
- broad sync can overwrite unrelated dirty canonical work

Containment:
- inspect every relevant Case 17 occurrence, not only changed lines
- combine positive and forbidden-negative checks with an independent whole-file review
- use prepared/candidate wording until public evidence exists
- freeze and enforce the exact nine-path allowlist
- stop on unexplained canonical overlap and copy only verified paths

## Rollback

- Before publication, discard only the scoped clean v10.61 candidate if a gate fails.
- Stop canonical synchronization on unexplained overlapping changes; do not overwrite unrelated work.
- Root Rules remain observation-only and are not reinstalled.
- After publication, use a later corrective release; never amend or force-move v10.60 or v10.61.

## Exit Criteria

- Case 17 is internally consistent across governing rules, facts, example, decision, and flow.
- Full positive and forbidden-negative semantic checks pass.
- The exact nine-path candidate matches canonical with expected modes.
- Protected runtime/governance/install surfaces remain byte-identical.
- Public master, immutable annotated v10.61, GitHub Release, and fresh-public-tag proof pass.
- Documentation-only closeout advances master and canonical without changing tagged Case 17 or either immutable release tag.
