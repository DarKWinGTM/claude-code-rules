# Clean plugin-only release recut patch

> **Current Version:** 0.1.75
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)
> **Status:** Phase 071 completed corrective clean plugin-only release recut in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.75
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The phase-070 payload already fixed the plugin README and aligned the adaptive deep-analysis code/docs/tests, but its push path still shared a dirty working tree with unrelated objectives. The safe corrective move is therefore a clean plugin-only release recut from an isolated checkout rather than reworking the runtime contract again.

## 2) Analysis

This wave keeps the same plugin behavior and README boundaries, bumps package/governed versions again, records the corrective release process in governed surfaces, and re-publishes from an isolated clean checkout so the release workspace itself proves that unrelated RULES-root and `plugin/governed-docs` drift were excluded.

## 3) Change items

### 3.1 Bump the package and governed versions for the corrective release
- **Target artifact:** `../.claude-plugin/plugin.json`, `../skills/analysis/SKILL.md`, `../tests/test_plugin_manifest.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../design/04-native-agent-orchestration.design.md`, `../design/08-memory-evidence-source-model.design.md`, `../phase/SUMMARY.md`, and `../changelog/changelog.md`
- **Change type:** replacement
- **Before:** package version was `0.9.26` and the active governed version state was `0.1.74`
- **After:** package version is `0.9.27` and the active governed version state is `0.1.75`

### 3.2 Add governed records for the clean plugin-only release recut
- **Target artifact:** `../phase/phase-071-clean-plugin-only-release-recut.md`, `../changelog/v0.1.75-completed-clean-plugin-only-release-recut.changelog.md`, and `clean-plugin-only-release-recut.patch.md`
- **Change type:** additive
- **Before:** there was no dedicated governed record that proved the corrective clean checkout release path
- **After:** the plugin-local phase/changelog/patch chain records the clean plugin-only release recut explicitly

## 4) Verification

- confirm the isolated release checkout stays clean with `git status --short` before merge/push
- confirm the commit scope with `git diff --name-only` and `git diff --stat` so only `plugin/memory-context-intelligence/**` is included
- run the full plugin suite with `python3 -m unittest discover -s tests -v`
- validate the plugin package with `claude plugin validate <plugin-path>`
- verify README/version/governed closeout alignment and then complete merge, push, tag, and GitHub release for the corrective version

## 5) Rollback approach

If this corrective wave is rolled back, revert only the clean plugin-only recut commit(s), tag, and release path. Do not use rollback as authority to remove unrelated RULES history, revert the checked adaptive deep-analysis contract, or reintroduce the removed Claude Code installation tutorial into the plugin README.
