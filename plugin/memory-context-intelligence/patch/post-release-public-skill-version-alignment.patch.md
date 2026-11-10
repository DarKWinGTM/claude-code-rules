# Post-release public-skill version alignment patch

> **Current Version:** 0.1.79
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)
> **Status:** Completed / corrective package 0.9.31 released and fresh-tag verified
> **Target Design:** [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

Package `0.9.30` was released and fresh-tag tested, but a later audit found one metadata alignment defect: the public init skill remained at `0.9.29`. Because the published tag is immutable, the correction must use a new package version rather than moving or replacing `0.9.30`.

## Analysis

### Before

- manifest and analysis skill report `0.9.30`
- init skill reports `0.9.29`
- the manifest test checks only the manifest value
- one analysis-skill sentence calls the user-scope config path a project default
- active design/changelog wording still contains pre-verification planning language

### After

- manifest, analysis skill, and init skill report `0.9.31`
- the manifest regression test checks both public skill versions
- config-path wording consistently says user-scope default
- evidence/design/release wording reflects the actual checked proof level
- package `0.9.30` remains untouched; separately approved package `0.9.31` carries the correction and is fresh-tag verified

## Change items

1. **Package and public-skill alignment — replacement**
   - bump manifest and both public skills to `0.9.31`
   - require both skill versions to equal the manifest in tests

2. **Config ownership wording — replacement**
   - replace `project default config file` with `user-scope default config file`

3. **Governed evidence wording — replacement**
   - update selected design, changelog, phase, and patch surfaces from stale planning/current language to evidence-bounded delivered/corrective language

4. **Design metadata restoration — replacement**
   - restore native-agent orchestration shard metadata from the accidental local `0.1.74` regression to tag-backed `0.1.75`

5. **Immutable corrective release — additive**
   - prepare package `0.9.31` from `memory-context-intelligence--v0.9.30`
   - require a new confirmation gate before push, annotated tag, or GitHub Release

## Verification

Selected route: `new_focused_test` plus full source and clean-candidate regression suites.

Observed evidence:
- manifest/public-skill alignment and user-scope wording checks: `21 passed`
- source, clean-candidate, and fresh-tag full suites: `132 passed` each
- source, clean-candidate, and fresh-tag `claude plugin validate`: PASS
- clean candidate: exact 17 allowlisted plugin paths, zero deletions
- approved commit/remote branch/peeled annotated tag: `5e58f018a2b057ffdd009aeca3d88146e0cfab20`
- GitHub Release: non-draft/non-prerelease `memory-context-intelligence v0.9.31`
- fresh tag: manifest and both public skills report `0.9.31`
- published `0.9.30` branch/tag/release remains unchanged at `02b15e29fe5eaf7c05e0a81d0b92ef4773cfd677`

## Rollback approach

After publication, preserve both `0.9.30` and `0.9.31` tags/releases as immutable evidence. Any later defect requires a new corrective package version and confirmation; do not move/delete either release or alter Main RULES, unrelated plugins, or existing additional-stage artifacts.
