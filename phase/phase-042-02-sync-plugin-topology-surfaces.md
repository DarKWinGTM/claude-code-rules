# Phase 042-02 - Sync plugin topology surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 042-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/plugin-topology-correction.patch.md](../patch/plugin-topology-correction.patch.md)

---

## Objective

Synchronize governance, install, and release surfaces after correcting the plugin topology.

## Why this phase exists

The topology correction only becomes trustworthy when the README, TODO, changelog, phase summary, package metadata, and installed plugin state all describe the same split: `rules-compact-extension` for compact helper behavior and `claude-code-rules` for the coordination skill.

## Entry conditions / prerequisites

- `042-01` is complete
- the bounded patch artifact for this correction already exists
- the shared `darkwingtm` marketplace has been restored

## Action points / execution checklist

- [x] update `README.md`
- [x] update `TODO.md`
- [x] update `changelog/changelog.md`
- [x] update `changelog/rules-plugin-extension.changelog.md`
- [x] update `phase/SUMMARY.md`
- [x] restore `darkwingtm` plugin resolution
- [x] reinstall affected plugins from `@darkwingtm`
- [x] keep `claude-code-rules@claude-code-rules` limited to local development/testing

## Out of scope

- deleting `rules-compact-extension`
- merging the two plugin packages into one in this wave
- changing the root runtime rule count

## Affected artifacts

- `README.md`
- `TODO.md`
- `changelog/changelog.md`
- `changelog/rules-plugin-extension.changelog.md`
- `phase/SUMMARY.md`
- plugin install state in the local machine environment

## Verification

- [x] governance surfaces describe the same two-plugin topology
- [x] the shared `darkwingtm` marketplace is active again
- [x] the darkwingtm plugin family resolves correctly again
- [x] `claude-code-rules@darkwingtm` is the intended public install target

## Risks / rollback notes

- installed state can drift again if the shared marketplace is removed or overridden carelessly
- rollback should preserve the restored plugin family resolution and only narrow wording if needed

## Next possible phases

- none required once commit/push/release are complete

## Exit criteria

- [x] governance surfaces reflect the corrected topology coherently
- [x] plugin family resolution is restored
- [x] the `042` phase family is visible and reviewable from `phase/SUMMARY.md`
