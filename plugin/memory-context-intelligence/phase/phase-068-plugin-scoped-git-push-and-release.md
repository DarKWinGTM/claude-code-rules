# Phase 068 - plugin-scoped git push and release

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

068

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/plugin-scoped-git-push-and-release.patch.md](../patch/plugin-scoped-git-push-and-release.patch.md)

## Objective

Close a plugin-scoped git push update and release wave for `memory-context-intelligence` from the RULES repo without pulling unrelated RULES changes into the commit, push, or release path.

## Why this phase exists

The capsule had already become the active RULES-owned source authority, but it still sat in git as an untracked directory. The user then clarified that `plugin/memory-context-intelligence` is part of RULES and should already live in the repo. This phase closes that gap by moving the capsule into plugin-scoped repo history, aligning release metadata, and executing a plugin-specific push/release path.

## Gate

Phase 068 closes only when all of the following are true in checked scope:
- `plugin/memory-context-intelligence/**` is tracked in RULES git history through a plugin-scoped commit
- `.claude-plugin/plugin.json` and the active governed release surfaces are synced to the release wave version state
- unrelated RULES repo changes remain outside the plugin-scoped commit
- the full plugin test suite still passes after the version/release metadata sync
- the selected branch push succeeds
- a plugin-specific tag/release path references `memory-context-intelligence` directly and is visible in transcript evidence

## Verification / closeout

Phase 068 is completed in checked scope.

This closeout now holds:
- the capsule is tracked directly under `RULES/plugin/memory-context-intelligence/` in repo history instead of remaining untracked-only source state
- the plugin package version is bumped to `0.9.25` and the active governed version chain is bumped to `0.1.72`
- the release wave stays plugin-scoped and avoids unrelated RULES repo modifications in the release commit
- the selected branch push plus plugin-specific release path are executed as transcript-visible proof rather than being left as implied future work
- phase-067 config-policy behavior and its trace-anchored boundaries remain unchanged

## Boundaries preserved after closeout

Phase 068 still does not claim:
- new runtime semantics beyond phase 067
- automatic config writing or selected-topic persistence
- a fifth evidence class or semantic-authority promotion for config
- reopening `review` / `packet`
- `/additional/` behavior changes
- broad main-RULES release readiness beyond this plugin-scoped wave
- inclusion of unrelated RULES repo modifications in the plugin-scoped release commit
