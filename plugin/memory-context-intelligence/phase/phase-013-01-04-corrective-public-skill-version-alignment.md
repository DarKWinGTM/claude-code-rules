# Phase 013-01-04 — Corrective Public-Skill Version Alignment

> **Parent Phase:** [phase-013-01-deterministic-standalone-additional-stage-emission.md](phase-013-01-deterministic-standalone-additional-stage-emission.md)
> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Current Version:** 0.1.79
> **Status:** Completed / package 0.9.31 released and fresh-tag verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.79
> **Patch Reference:** [../patch/post-release-public-skill-version-alignment.patch.md](../patch/post-release-public-skill-version-alignment.patch.md)
> **Changelog Reference:** [../changelog/v0.1.79-corrective-public-skill-version-alignment.changelog.md](../changelog/v0.1.79-corrective-public-skill-version-alignment.changelog.md)
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)

---

## Objective

Correct the public init-skill version mismatch and active governed wording drift through a new immutable corrective package release, without moving or deleting `memory-context-intelligence--v0.9.30`.

## Output

- manifest, analysis skill, and init skill aligned at `0.9.31`
- regression coverage for both public skill version anchors
- user-scope config wording aligned
- selected design/changelog/phase/patch wording aligned with checked evidence
- native-agent design shard metadata restored to tag-backed `0.1.75`
- exact plugin-only corrective release candidate based on v0.9.30

## Gate

1. focused RED confirms manifest/public-skill and config-wording defects
2. focused GREEN passes after correction
3. full source suite and package validation pass
4. clean v0.9.30-based candidate has exact allowlist and no deletions
5. clean-candidate full suite and package validation pass
6. explicit external-action confirmation names the new branch, SHA, tag, release title, path count, and tests
7. approved push, annotated tag, GitHub Release, and fresh-tag proof pass

## Verification record

- RED: `2 failed, 18 passed` for manifest/public-skill alignment and user-scope wording
- focused GREEN: `21 passed`
- full source suite: `132 passed`
- source plugin validation: PASS
- clean candidate base: immutable `memory-context-intelligence--v0.9.30` at `02b15e29fe5eaf7c05e0a81d0b92ef4773cfd677`
- clean candidate scope: exact 17 allowlisted plugin paths, zero deletions
- clean candidate full suite: `132 passed`
- clean candidate plugin validation: PASS
- approved corrective commit: `5e58f018a2b057ffdd009aeca3d88146e0cfab20`
- remote branch: `mci-release-v0.9.31` resolves to the approved commit
- annotated tag: `memory-context-intelligence--v0.9.31`; tag object `e9217f0014eef2c9553fa2104d071128d941e571`; peeled commit matches the approved commit
- GitHub Release: `memory-context-intelligence v0.9.31`, non-draft and non-prerelease — https://github.com/DarKWinGTM/claude-code-rules/releases/tag/memory-context-intelligence--v0.9.31
- fresh tagged clone: manifest, analysis skill, and init skill all report `0.9.31`; full suite `132 passed`; plugin validation PASS; HEAD matches the approved commit
- immutable v0.9.30 recheck: branch and peeled annotated tag still resolve to `02b15e29fe5eaf7c05e0a81d0b92ef4773cfd677`; release remains non-draft and non-prerelease

## Boundaries

- package `0.9.30`, its branch/tag, and GitHub Release remain immutable
- no force push, tag movement, release replacement, or deletion
- no Main RULES mutation/promotion/merge
- no marketplace installation or stability claim
- unrelated dirty source-tree changes remain excluded

## Rollback / containment

The published `0.9.31` tag and GitHub Release are immutable release evidence. Any later defect requires a new corrective package version; do not force-move or replace `0.9.31` or `0.9.30`. Existing additional-stage artifacts and unrelated source state remain untouched.
