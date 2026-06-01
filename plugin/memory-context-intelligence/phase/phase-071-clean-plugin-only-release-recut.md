# Phase 071 - clean plugin-only release recut

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

071

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/04-native-agent-orchestration.design.md](../design/04-native-agent-orchestration.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/clean-plugin-only-release-recut.patch.md](../patch/clean-plugin-only-release-recut.patch.md)

## Objective

Re-cut the already-checked `memory-context-intelligence` plugin release from an isolated clean checkout so the branch-first merge, push, tag, and GitHub release path are proven without unrelated RULES-root or `plugin/governed-docs` working-tree drift, while keeping the same plugin-only runtime contract and README cleanup.

## Why this phase exists

Phase 070 already aligned the plugin payload itself, but its outward release path still shared a dirty working tree with unrelated objectives. The corrective wave is therefore not a feature redesign; it is a clean plugin-only recut that preserves the same README/runtime/docs/tests truth while proving the release process from an isolated clean checkout.

## Gate

Phase 071 closes only when all of the following are true in checked scope:
- the plugin README still has no `Install Claude Code` tutorial, no generic shell-prerequisite install section, and no `/login` bootstrap guidance that does not belong in the plugin README
- the plugin payload remains limited to `plugin/memory-context-intelligence/**` plus only strictly required plugin-specific git/release metadata
- the package version is bumped from `0.9.26` to `0.9.27` and the governed version chain is bumped from `0.1.74` to `0.1.75`
- the isolated release checkout stays clean before merge/push so unrelated RULES-root and `plugin/governed-docs` drift is not part of the release workspace
- the full plugin test suite passes in the final version state and plugin manifest validation passes
- the corrective branch merges back to `master`, `origin/master` is pushed, and the GitHub release for the new plugin tag succeeds

## Verification / closeout

Phase 071 is completed in checked scope.

This closeout now holds:
- the plugin README remains plugin-specific and still omits the unnecessary Claude Code installation tutorial
- the runtime/code/tests/governed-docs truth from phase 070 is preserved unchanged except for the corrective version bump
- the plugin package version is now `0.9.27` and the active governed version chain is now `0.1.75`
- the release branch/tag/release path is re-proved from an isolated clean checkout without unrelated working-tree drift in the release workspace
- future development remains open after this corrective release wave

## Boundaries preserved after closeout

Phase 071 still does not claim:
- bare `/analysis` as a proved current runtime surface
- reopening `review` or `packet`
- plugin-managed auto-flow proof
- publication breadth beyond this plugin-specific release path
- stable/broad production readiness beyond checked evidence
- main RULES promotion or broader RULES mutation
- any weakening of `trace_evidence` as the live promotion anchor
