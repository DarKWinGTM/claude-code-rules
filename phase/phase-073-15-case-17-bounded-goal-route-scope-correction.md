# Phase 073-15 - Case 17 Bounded-Goal Route-Scope Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-15
> **Status:** Completed — released and fresh-public-tag verified
> **Target Release:** v10.63
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md), [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md)
> **Patch References:** none

---

## Objective

Correct the remaining Case 17 bounded-goal route-scope contradiction, verify the complete scenario as one semantic unit, and publish the documentation-only correction as v10.63 without changing Runtime Rules, designs/per-rule changelogs, installers, fixtures, or prior immutable releases.

พูดง่าย ๆ: `/goal` นี้เลือกเฉพาะ queue ordering และ worker lease ดังนั้น plan และ proof ต้องอยู่ใน slice เดียวกัน; retry/backoff กับ status visibility ยังเก็บไว้ได้ แต่ต้องเป็น deferred sibling ที่อยู่นอก execution และ proof ของ goal นี้.

## Lineage Decision

- P073-14 and v10.62 are published and immutable.
- The delayed whole-file semantic gate found one residual contradiction inside the same Case 17 owner-boundary family: retry/status sibling candidates still act as current-goal plan and proof obligations.
- The correction introduces no Runtime Rule, capability, installer behavior, architecture family, or new scenario family.
- Therefore `073-15` is the smallest truthful existing-family child; P073-14 must not be reopened or amended.

## Selected Boundary

```text
queue/worker-lease advisory /goal
→ Plan draft contains queue/lease work only
→ Verification route proves queue/lease behavior only
→ retry/backoff remains a deferred sibling candidate
→ status visibility remains a deferred sibling candidate
```

Candidate-goal posture remains separate from advisory eligibility. Goal-authoring constructs the bounded `/goal` and subordinate support after execution selects posture; presentation renders the completed artifact. Compact-in-goal support and `/plan` remain alternative branches. Case 17 creates no durable route file and emits no actual `Plan reference:`.

## Exact Allowlist

The immutable v10.63 release commit changed exactly nine paths:

1. `../playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md`
2. `phase-073-15-case-17-bounded-goal-route-scope-correction.md`
3. `SUMMARY.md`
4. `../TODO.md`
5. `../changelog/changelog.md`
6. `../changelog/changelog/v10.63-case-17-bounded-goal-route-scope-correction.changelog.md`
7. `../README.md`
8. `history/2026-08-09.md`
9. `../todo/history/2026-08-09.md`

`TODO.md`, `phase/SUMMARY.md`, and `changelog/changelog.md` preserve Git mode `100755`; the other paths use or preserve `100644`. No rename, deletion, symlink, submodule, binary, matrix, coverage, design, diagram, patch, installer, fixture, or manifest change is allowed.

Canonical `TODO.md` contains a pre-existing unrelated active plugin item not present in public master. Canonical synchronization must preserve that exact block through a bounded anchor merge; release-owned TODO state must match semantically while the unrelated block remains byte-identical. The other eight candidate paths use exact whole-file synchronization.

## Work Lanes

### Lane 1 - Scenario correction

- keep the advisory `/goal` scoped to queue ordering and worker lease
- keep `Plan draft` limited to queue ordering, lease ownership, and lease state transitions
- keep the verification route limited to queue trace, lease evidence, and caused/not-caused classification
- retain retry/backoff and status visibility as deferred sibling notes outside this goal's execution and proof
- preserve candidate/advisory separation, goal-first visible order, alternative route branches, helper subordination, and the no-`Plan reference:` boundary

### Lane 2 - Governance synchronization

- update only compact phase/TODO/changelog/README current-state anchors
- append daily movement without rewriting prior history
- create one v10.63 release shard
- keep patch posture `none` because the one-scenario diff is directly reviewable

### Lane 3 - Verification and canonical convergence

- run section-bounded positive and forbidden-negative semantic assertions plus independent whole-file doctrine review
- verify exact allowlist, modes, links, README anchors, and `git diff --check`
- prove Runtime Rule/design/per-rule changelog/installer/fixture and prior-release bytes unchanged
- run unchanged Bash/PowerShell fixture matrices and disposable installation
- synchronize eight paths exactly and merge only the release-owned TODO anchors after overlap recheck

### Lane 4 - Root installation

- run the canonical installer twice because the user explicitly selected root installation
- verify 19/19 canonical/root byte and mode parity, ordered manifest convergence, unrelated-file preservation, no new quarantine, and second-run idempotence
- treat installation as an operator-requested deployment/parity witness, not a Runtime Rule Git change

### Lane 5 - Publication and closeout

- publish clean public `master`
- create immutable annotated `v10.63` and GitHub Release
- verify fresh public master/tag clones and v10.60-v10.62 immutability
- publish an eight-path documentation-only closeout without modifying tagged Case 17 or moving v10.63

## Development Verification / TestKit Coverage

Selected route: section-bounded Case 17 assertions plus independent whole-file review, exact diff/mode/link checks, protected-byte comparison, unchanged fixture matrices, disposable installation, canonical synchronization, two-pass root installation, public-master/tag/Release identity, and fresh-tag reproduction.

Required positive assertions:

- candidate and advisory postures remain separate execution decisions
- advisory `/goal` visibly precedes all route-support blocks
- queue/worker lease is the only objective, execution, proof, and scope of the selected goal
- `Plan draft` contains only queue/lease investigation
- retry/status remain explicit deferred sibling candidates outside execution and proof
- deferred notes are not current-goal execution or verification obligations
- verification contains only queue trace, lease ownership/state transitions, and caused/not-caused classification
- compact-in-goal support and `/plan` remain alternative goal-authoring branches
- presentation renders only after selected construction completes
- helper output is not goal-completion proof
- no actual `Plan reference:` is emitted

Forbidden assertions:

- retry/backoff/status/visibility work inside `Plan draft`
- retry re-entry or status/reporting checks inside the selected verification route
- retry/status as objective, proof, acceptance, completion, or required implementation conditions
- deferred siblings ordered as current-goal steps or required checks
- visible support before advisory `/goal`
- candidate posture automatically promoted into advisory `/goal`
- compact support obligatorily sequenced into `/plan`
- execution or presentation owning route construction
- route/helper completion counting as goal proof
- an unwritten or unverified actual `Plan reference:`

Protected unchanged surfaces:

- all 19 Runtime Rules and their ordered inventory
- all Runtime Rule designs and per-rule changelogs
- Bash/PowerShell installers, launchers, fixture scripts, and manifests
- P073-12 through P073-14 and v10.60-v10.62 artifacts and immutable releases
- unrelated canonical dirty paths and unrelated root Rules

## Out of Scope

- Runtime Rule, design, per-rule changelog, or runtime-version changes
- installer/fixture implementation changes
- playground matrix/coverage changes
- README restructuring
- editing prior completed/blocked phase or release artifacts
- backup-branch topology mutation or unrelated canonical cleanup
- deletion, quarantine cleanup, automatic fallback, or restoration

## Risks and Containment

Risks:
- positive anchors may pass while retry/status remain hidden current-goal obligations
- canonical `TODO.md` has unrelated active work on the same path
- governance may claim publication or installation evidence before it exists
- public master may advance between verification and push

Containment:
- use section-bounded forbidden-negative checks and independent whole-file review
- preserve the unrelated canonical TODO block through a bounded anchor merge and verify it remains byte-identical
- use active/candidate wording until evidence exists
- fetch and require unchanged public master immediately before fast-forward publication
- stop on an unexpected path, protected-byte drift, unexplained overlap, or any failed semantic/install gate

## Root Installation Boundary

The v10.63 source diff contains no Runtime Rule or installer change. After canonical candidate synchronization, run:

```bash
/home/node/workplace/AWCLOUD/TEMPLATE/RULES/script/setup-claude-code-rules.sh \
  --project-root /home/node \
  --source-repo /home/node/workplace/AWCLOUD/TEMPLATE/RULES
```

Run it twice. The gate requires exact 19-file manifest order, canonical/root byte and mode parity, unchanged unrelated root entries, no new quarantine, and identical converged state after the second run.

## Rollback

- Before publication, discard or revert only the scoped clean v10.63 candidate.
- Stop canonical synchronization on unexplained overlap; never overwrite unrelated work.
- If canonical rollback becomes necessary, restore only release-owned anchors/files after a fresh overlap check.
- After publication, use a later release for defects; never amend or force-move v10.60, v10.61, v10.62, or v10.63.
- No deletion, cleanup, quarantine removal, fallback, or restoration action is authorized.

## Verification and Closeout

P073-15 passed its complete release gate:

- release commit `c7f42ecf73c965249611f6c08692310fd8bb7644` changed exactly the governed nine-path set
- annotated `v10.63` tag object `24a13f14960babe01a64967dd91d7695661741ec` peels to the same release commit
- GitHub Release `v10.63` is published, non-draft, and non-prerelease: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.63
- fresh public master and immutable-tag clones passed exact scope/modes, links, section-bounded semantic checks, protected 19-Rule identity, Bash/PowerShell fixtures, and disposable installation
- an independent fresh-tag whole-file doctrine audit returned `PASS` for bounded queue/lease execution and proof, deferred retry/status siblings, owner ordering, alternative route branches, helper non-proof, and the no-actual-`Plan reference:` boundary
- canonical synchronization passed for eight exact files plus the release-owned TODO projection while unrelated plugin work remained preserved
- the canonical installer ran twice against root; 19/19 byte and mode parity, manifest convergence, unrelated `additional/` and `shared-task-list-path-coordination.md` preservation, absent quarantine, and identical second-run state passed
- prior immutable releases remained unchanged: v10.60 tag object `b1bc48e3221001675c9a59293cc469e9540cfd9c`, v10.61 tag object `114d0fb9856fac59c6283f8868c3727c37e0a5cf`, and v10.62 tag object `4246218bbdb9b5a082f0a14a9111ec2d8b9cee13`

The documentation-only closeout updates the eight governed release surfaces and excludes Case 17. It does not move `v10.63`, change any Runtime Rule or installer source, or rewrite the unrelated canonical TODO plugin item.

## Exit Criteria

- [x] Case 17 is bounded-goal consistent across example, decision, and flow.
- [x] Full section-bounded semantic checks and independent pre-publication/fresh-tag reviews passed.
- [x] Exact nine-path release scope and expected modes passed.
- [x] Protected runtime/governance/install surfaces remained unchanged.
- [x] Canonical release-owned synchronization preserved unrelated TODO/plugin work.
- [x] Two-pass root installation proved 19/19 parity, idempotence, unrelated preservation, and no quarantine creation.
- [x] Public master, immutable annotated v10.63, GitHub Release, and fresh-public-tag proof passed.
- [x] Eight-path closeout excludes tagged Case 17 and leaves every immutable tag unchanged.
