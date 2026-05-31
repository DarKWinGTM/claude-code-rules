# Phase 034 - harness-surface governance sync

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

034

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Complete docs-only harness-surface governance sync so `memory-context-intelligence` is documented as one plugin capability with three peer harness-facing surfaces — harness-native skill, named slash command, and plugin-managed auto flow — while `bin/memory-context-intelligence` is reclassified as an internal implementation mechanism only.

## Why this phase exists

Phase 033 closed the broader transcript-governed darkwingtm correction in checked local scope, but the governed docs still allowed a user-reading drift where runtime-facing package docs and skill docs could be read as steering post-install usage toward `bash ./bin/memory-context-intelligence`. Phase 034 exists to remove that confusion without deleting source artifacts, without touching `/additional/`, and without overclaiming slash-command/chat invocation proof.

## Approval boundary

Phase 034 executed as a docs-only governance sync wave.

Executed boundary:
- no reinstall command executed in this phase
- no uninstall command executed in this phase
- no marketplace remap or registry mutation executed in this phase
- no source package deletion or narrowing occurred
- no `/additional/` behavior change occurred
- no slash-command/chat invocation proof claim
- no publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge claim
- no runtime cleanup of `bin/memory-context-intelligence`

## Expected output

Phase 034 produces:
- RULES-side and runtime-facing package docs that agree on one capability with three peer harness-facing surfaces
- explicit separation between harness-facing surfaces and internal `bin/**` implementation mechanism
- explicit separation between install/load proof, skill proof, slash proof, and auto-flow proof
- removal of any doc wording that treats `bash ./bin/memory-context-intelligence` as the primary post-install workflow for the user

## Entry conditions

- phase 033 is completed checked-local correction closeout evidence
- active source authority remains `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`
- active runtime marketplace remains `darkwingtm` -> `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`
- supported runtime-facing projection remains `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/`
- no further runtime mutation is required to classify the surface model correctly

## Gate

Phase 034 closes only when all of the following are true in checked scope:
- README, design parent, installability shard, phase summary, changelog parent/detail, patch, root TODO, runtime-facing package README, and `skills/memory-context-intelligence/SKILL.md` agree that `memory-context-intelligence` is one plugin capability with three peer harness-facing surfaces
- `bin/memory-context-intelligence` is documented as an internal implementation mechanism only
- no checked doc tells the user to use `bash ./bin/memory-context-intelligence` as the primary post-install workflow
- install/load proof is described separately from skill proof, slash proof, and auto-flow proof

## Checked evidence

- RULES-side README now contains a dedicated harness-facing surface model section and explicitly says `bin/memory-context-intelligence` is not the primary post-install workflow for the user.
- `design/design.md` now states that the capsule exposes one plugin capability through peer harness-facing surfaces rather than through a primary external CLI workflow.
- `design/06-plugin-installability.design.md` now defines the harness-facing surface model and the proof-separation boundary explicitly.
- `phase/SUMMARY.md` now records phase 034 and preserves the harness-facing surface model in current runtime truth and program boundaries.
- `changelog/changelog.md` now maps v0.1.39 as the harness-surface governance sync detail shard.
- The active patch now records phase 034 as docs-only harness-surface governance sync with the affected artifact set.
- Root `TODO.md` now records phase 034 as a completed checked-local governance sync item.
- `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/README.md` now reclassifies command usage under an internal implementation adapter heading and says it is not the primary post-install workflow.
- `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md` now states that this skill is one harness-facing entry surface for the capability and reclassifies the command adapter as internal only.

## Verification / closeout

Phase 034 is completed in checked local scope.

This closes the harness-surface governance sync objective because:
- the user-facing surface model is now documented as one plugin capability with three peer harness-facing entry surfaces
- the internal command adapter is now separated from user-facing plugin usage
- docs no longer instruct the user to adopt external CLI-first post-install usage
- proof categories are now separated so install/load evidence cannot be silently upgraded into slash or auto-flow proof

## Boundaries preserved after closeout

Phase 034 still does not claim:
- slash-command/chat invocation proof
- publication or external marketplace release
- stable or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge
- runtime cleanup/removal of `bin/memory-context-intelligence`

## Rollback notes

Because phase 034 is a docs-only governance sync wave, rollback is limited to reverting the governed documentation sync if selected. It does not authorize deleting source authority, removing `bin/memory-context-intelligence`, uninstalling the current local plugin entry, removing marketplace registrations, or mutating `/additional/` material without separate explicit approval.
