# Plugin-scoped git push and release patch

> **Current Version:** 0.1.72
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)
> **Status:** Phase 068 completed plugin-scoped git push update and release in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.72
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

`memory-context-intelligence` had already become the active RULES-owned plugin source, but the whole capsule still sat in git as an untracked directory. The user explicitly clarified that this plugin is part of RULES and should already live inside the repo. A plugin-scoped release wave was therefore needed to track the capsule directly in repo history, keep unrelated repo edits out of the commit, and cut a plugin-specific push/release path.

## 2) Analysis

The safe move is a plugin-scoped release wave rather than a broad RULES repo release. That means: isolate commit scope to `plugin/memory-context-intelligence/**`, bump package/release metadata only inside the plugin-local governed chain, keep phase-067 runtime semantics unchanged, verify the full plugin suite after the metadata bump, and produce a plugin-specific tag/release path whose notes/artifact naming point to `memory-context-intelligence` directly.

## 3) Change items

### 3.1 Track the capsule directly in RULES git history
- **Target artifact:** `../**`
- **Change type:** additive/reclassification through git tracking
- **Before:** `plugin/memory-context-intelligence/**` existed in the RULES working tree but was not yet recorded as tracked repo history
- **After:** the plugin path is included in a plugin-scoped RULES commit without pulling unrelated repo changes into the same wave

### 3.2 Bump plugin package version and aligned governed version surfaces
- **Target artifact:** `../.claude-plugin/plugin.json`, `../skills/analysis/SKILL.md`, `../tests/test_plugin_manifest.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../design/08-memory-evidence-source-model.design.md`, `../phase/SUMMARY.md`, and `../changelog/changelog.md`
- **Change type:** replacement
- **Before:** package version was `0.9.24` and active governed version state was `0.1.71`
- **After:** package version is `0.9.25` and active governed version state is `0.1.72`

### 3.3 Add plugin-scoped release governance records
- **Target artifact:** `../phase/phase-068-plugin-scoped-git-push-and-release.md`, `../changelog/v0.1.72-completed-plugin-scoped-git-push-and-release.changelog.md`, and `plugin-scoped-git-push-and-release.patch.md`
- **Change type:** additive
- **Before:** there was no dedicated plugin-local record for the repo-tracking/push/release wave
- **After:** the plugin-local phase/changelog/patch chain records the release wave and provides plugin-specific release notes

## 4) Verification

- confirm plugin-scoped staging with `git diff --cached --name-only` and check unrelated RULES repo edits stay out of the commit
- run the full plugin suite with `python3 -m unittest discover -s tests -p 'test_*.py' -v`
- verify the plugin-scoped commit hash exists in transcript
- verify branch push output in transcript
- verify plugin-specific tag/release output in transcript

## 5) Rollback approach

If this wave is rolled back, revert only the plugin-scoped release commit/tag/release path and the aligned plugin-local metadata updates. Do not use rollback as authority to remove unrelated RULES repo history, revert non-plugin work, or weaken the already-checked phase-067 config-policy boundaries.
