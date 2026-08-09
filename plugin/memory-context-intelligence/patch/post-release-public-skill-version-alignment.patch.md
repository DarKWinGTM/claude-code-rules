# Post-release public-skill version alignment patch

> **Current Version:** 0.1.79
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)
> **Status:** corrective source and exact clean candidate verified; external-action confirmation pending
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
- package `0.9.30` remains untouched; a separately approved `0.9.31` release carries the correction

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

Required evidence:
- manifest/public-skill alignment test passes
- analysis user-scope wording test passes
- full plugin suite passes
- `claude plugin validate` passes
- clean candidate has exact allowlisted scope and no deletions
- published `0.9.30` tag/release remains unchanged

## Rollback approach

Before external release, revert only the v0.1.79/plugin `0.9.31` corrective delta. Do not move or delete package `0.9.30`, and do not alter Main RULES, unrelated plugins, or existing additional-stage artifacts.
