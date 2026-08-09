# Phase 073-14 - Case 17 Goal-First Route-Branch Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-14
> **Status:** Active — release candidate preparation
> **Target Release:** v10.62
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md), [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md)
> **Patch References:** none

---

## Objective

Correct the remaining Case 17 output-order and route-branch contradictions, verify the complete scenario as one semantic unit, and publish the bounded documentation correction as v10.62 without changing Runtime Rules, designs/per-rule changelogs, installers, fixtures, or root installation.

พูดง่าย ๆ: advisory `/goal` ต้องเป็น visible owner ก่อน route support และ compact-in-goal กับ `/plan` ต้องเป็นคนละ branch ที่ goal-authoring เลือกก่อน presentation render.

## Lineage Decision

- P073-13 and v10.61 are completed and immutable.
- The residual defects remain inside the same Case 17 owner-boundary and full-file scenario-verification family.
- They do not introduce a new Runtime Rule, capability, or architecture family.
- Therefore `073-14` is the smallest truthful existing-family child; P073-13 must not be reopened or amended.

## Selected Lifecycle

```text
execution selects advisory eligibility
→ goal-authoring constructs advisory /goal
→ goal-authoring selects one subordinate route branch
  → compact support remains inside /goal
  OR
  → overflow/standalone route opens /plan
→ presentation renders the completed artifact or surface
```

Candidate-goal posture remains separate from advisory eligibility. Queue ordering and worker lease remain the selected goal scope; retry/backoff and status visibility remain subordinate route notes. Case 17 creates no durable route file and emits no actual `Plan reference:`.

## Exact Allowlist

The release candidate changes exactly nine paths:

1. `../playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md`
2. `phase-073-14-case-17-goal-first-route-branch-correction.md`
3. `SUMMARY.md`
4. `../TODO.md`
5. `../changelog/changelog.md`
6. `../changelog/changelog/v10.62-case-17-goal-first-route-branch-correction.changelog.md`
7. `../README.md`
8. `history/2026-08-09.md`
9. `../todo/history/2026-08-09.md`

`TODO.md`, `phase/SUMMARY.md`, and `changelog/changelog.md` preserve mode `100755`; the other paths use or preserve `100644`. No rename, deletion, symlink, submodule, binary, matrix, coverage, or patch change is allowed.

## Work Lanes

### Lane 1 - Scenario correction

- render advisory `/goal` before visible `Plan draft`, `Plan basis`, and verification route
- retain bounded internal planning as construction support rather than visible authority
- model compact-in-goal support and `/plan` as alternative goal-authoring branches
- render only after the selected artifact or surface is complete
- preserve candidate/advisory separation, bounded goal scope, and the no-`Plan reference:` boundary

### Lane 2 - Governance synchronization

- update only compact phase/TODO/changelog/README current-state anchors
- append daily movement without rewriting prior history
- create one v10.62 release shard
- keep patch posture `none` because the one-scenario diff is directly reviewable

### Lane 3 - Verification and canonical convergence

- run full-file positive and forbidden-negative semantic assertions plus independent doctrine review
- verify exact allowlist, modes, links, and `git diff --check`
- prove Runtime Rule/design/per-rule changelog/installer/fixture and prior-release bytes unchanged
- run unchanged Bash/PowerShell fixture matrices and disposable installation
- synchronize only the verified nine paths to canonical source after overlap recheck
- verify 19/19 canonical/root Runtime Rule parity without reinstalling

### Lane 4 - Publication and closeout

- publish clean public `master`
- create immutable annotated `v10.62` and GitHub Release
- verify a fresh public tag clone and v10.60/v10.61 immutability
- publish an eight-path documentation-only closeout without modifying tagged Case 17 or moving v10.62

## Development Verification / TestKit Coverage

Selected route: focused Case 17 ordering/branch assertions plus independent whole-file review, exact diff/mode/link checks, protected-byte comparison, unchanged fixture matrices, disposable installation, canonical parity, fresh-public-master/tag verification, and GitHub Release identity.

Required positive assertions:

- candidate and advisory postures remain separate execution decisions
- advisory `/goal` visibly precedes all subordinate route-support blocks
- goal-authoring chooses compact-in-goal support or `/plan` as alternative branches
- presentation renders only after the selected artifact or surface is complete
- queue/worker lease remains the only objective/proof/scope
- retry/status remain subordinate route notes
- helper output is not goal-completion proof
- no actual `Plan reference:` is emitted

Forbidden assertions:

- visible support before advisory `/goal`
- presentation before construction/support selection completes
- compact support sequenced obligatorily into `/plan`
- `/plan` followed by the stay-inside-`/goal` helper branch
- execution or presentation owning route support or `/plan`
- goal-authoring promoting candidate posture without selected advisory eligibility
- retry/status becoming goal conditions
- an unwritten or unverified `Plan reference:`

Protected unchanged surfaces:

- all 19 Runtime Rules
- all 19 Runtime Rule designs and per-rule changelogs
- Bash/PowerShell installers, launchers, fixture scripts, and manifests
- P073-13/v10.61 and P073-12/v10.60 records and immutable releases
- canonical and installed root Runtime Rules

## Out of Scope

- Runtime Rule, design, or per-rule changelog changes
- runtime version bumps or root installation
- installer/fixture implementation changes
- playground matrix/coverage changes
- README restructuring
- editing completed P073-13/v10.61 or P073-12/v10.60 artifacts
- backup-branch mutation or unrelated canonical cleanup
- deletion, quarantine cleanup, fallback, or restoration

## Risks and Containment

Risks:
- line-level assertions may pass while lifecycle ordering remains contradictory
- canonical is heavily dirty and can receive concurrent overlapping edits
- governance may claim release evidence before publication exists
- public master may advance between verification and push

Containment:
- combine focused assertions with an independent whole-file review
- freeze and recheck canonical allowlist hashes immediately before exact sync
- use candidate wording until public evidence exists
- fetch and require unchanged public master immediately before fast-forward push
- stop on any tenth path, protected-byte drift, or unexplained overlap

## Rollback

- Before publication, discard or revert only the scoped clean v10.62 candidate.
- Stop canonical synchronization on any unexplained overlapping change; never overwrite unrelated work.
- Root Rules remain observation-only and are not reinstalled.
- After publication, use a later release for defects; never amend or force-move v10.60, v10.61, or v10.62.

## Current Verification

Prepared candidate scope only. Semantic, protected-byte, fixture, canonical, public-master, annotated-tag, GitHub Release, and fresh-public-tag verification remain pending.

## Exit Criteria

- Case 17 is goal-first and branch-correct across example and flow.
- Full positive and forbidden-negative semantic checks plus independent review pass.
- Exact nine-path candidate matches canonical with expected modes.
- Protected runtime/governance/install surfaces remain byte-identical.
- Public master, immutable annotated v10.62, GitHub Release, and fresh-public-tag proof pass.
- Eight-path closeout advances master/canonical without modifying tagged Case 17 or any immutable release tag.
