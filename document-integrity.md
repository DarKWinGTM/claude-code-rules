# Document Integrity
> **Current Version:** 1.16
> **Design:** [design/document-integrity.design.md](design/document-integrity.design.md) v1.16
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/document-integrity.changelog.md](changelog/document-integrity.changelog.md)

## Rule Statement

**Core Principle: Preserve names, roles, references, history and project state across the checked change. Distinguish Runtime payload parity from Active Project Root convergence; prevent split/duplicate authority, roll oversized entrypoints without losing meaning, and never derive deletion or root replacement from size, cleanliness, isolation or missing recognition.**

This owner verifies cross-reference/chain/rollover integrity and file hygiene. [document-governance.md](document-governance.md) owns roles/chain selection/body eligibility; [authority-and-scope.md](authority-and-scope.md) selects the Active Project Root; [action-safety.md](action-safety.md) approves destructive operations.

## Propagate and Verify Changed Contracts

Resolve paths/symbols/keys/commands or mark unknown; update relevant imports/config/build/deploy/install/examples/tests/discovery/links/source-comment refs. Recompute relative paths after moves, never guess basenames. Update checked consumers; excerpts/nonfindings prove bounded scope only.

Verify selected chains: one generic/semantic parent, declared shape/complete map, child/version ownership/backlinks, no orphan/stale/duplicate/mixed authority, inactive-reference separation. Distinguish observation/doctrine/target/equivalence; update maps/backlinks/roles together.

TODO/phase summary stays bodyful navigation, not replaced by shards/history. Distinguish portable/local, source/install/destination/runtime and payload/other-owner files. Hashes without substantive bodies prove no parity/no-drift/release readiness.

For authority replacement check applicable manifests/imports/dependencies/config/build/deploy/tests/discovery/generated inputs/acceptance select current authority only. History/done/quarantine is provenance, never active/fallback/generated/discovery input. [Evidence](evidence-discipline.md) owns two-sided proof, not one move/grep.

## Payload Versus Project Convergence

| Proof layer | Required checked scope |
|---|---|
| Runtime payload parity | selected ordered install payload, bytes/modes/bodies/manifests and destination state |
| Full-project convergence | relevant Active Project Root source/config/Rules/governance/scripts/tests/plugin/support/tooling/generated declarations/modes and classified modified/untracked state |

Payload/candidate/tag/release/clone parity proves neither whole-project convergence nor root-replacement permission. Preserve unclassified/local-only paths pending ownership: dirty/untracked is neither truth nor public-replaceable junk. Block applicable sync/no-drift/closeout for split authoritative/newer state, unexplained canonical-only parts or alternate source/task/phase/Patch/commit/release authority. Disposable verification edits are not implementation.

Report mixed results explicitly rather than hide the failed layer:
```text
Runtime payload parity: passed
Active Project Root convergence: failed or blocked
Completion: blocked
```

Name exactly which layer/scope passed. A bounded payload task may report payload-only success; it cannot close unresolved required project convergence.

## Evidence-bound Patch Timeline Migration

Before mutation manifest each selected row deterministically: admissible original-creation evidence, exact old/new paths, source SHA-256/mode, dependent governed-reference hashes/modes and proposed metadata. mtime/ctime cannot fill gaps; ambiguous rows stay blocked.

Resolve real old targets; recompute renamed relative links across Phase/design/changelog/TODO/history/done/Patch companion history. No global basename replacement, wildcard-example (`patch/*.patch.md`) rewrite or serialized request/transcript mutation by default. Suspended archives are sentinels: exclude mutation, preserve names/bytes/modes/inactive-disconnected roles.

Require unchanged manifest/source/reference hashes and exact approval. Create manifest/journal exclusively, owner-only where supported. Persist rollback journal **before first mutation**, replace refs atomically, classify unchanged/staged/applied. Rollback is deliberate, never fallback; stop for hashes/modes outside original/applied journal states.

Verify filename/metadata, exact refs, former inactivity and sentinel together. Ambiguous selected rows, active old refs or archive discovery mean incomplete migration. [Governance](document-governance.md) owns timestamp/metadata/evidence, not the operational journal.

## Bodyful Entry and Preservation-first Rollover

```text
TODO.md → todo/history/YYYY-MM-DD*.md → todo/done/<task-or-wave>.md
phase/SUMMARY.md → phase/history/YYYY-MM-DD*.md → phase/done/phase-NNN-*.md
```

Daily history stores movement/snapshots; done stores larger completed detail. Moved content stays inactive-by-default, parent-linked/backlinked/reachable. Current/pending/deferred remains visible in compact active entrypoints.

Consider rollover at 250–300 lines, 25–30 KB, history exceeding current content or 200+ lines to reach current state. Require it before further broad absorption at roughly 500 lines/50 KB, failed oversized reads, repeated compact refill or autocompact thrash. These are scanability signals, not deletion permission.

Preserve a reachable snapshot → classify current/pending-deferred/completed/daily/historical → move only suitable bulk → update both directions → verify no active item/retained history lost. File size, completed/inactive status, context bloat or convenience cannot justify deletion.

## Density, Owner Repair and Leader Verification

Keep truth/history/proof/risks/exclusions/next work cohesive and correctly owned; version/link parity cannot excuse role overload. Repair clear low-risk touched density locally, otherwise visibly assign planned/deferred/blocked repair. TODO/phase overflow uses history/done, active design coherent shards. Keep touched God Phase/Patch decisions explicit.

Disposition modes: `REPAIR_NOW`, `DELEGATE_REPAIR`, `PLAN_IN_CURRENT_PHASE`, `OPEN_REPAIR_PATCH`, `OPEN_NEW_PHASE_OR_SUBPHASE`, `BLOCK_CLOSEOUT`, `ASK_ONLY_IF_AMBIGUOUS`. Their names are not permission for artifacts, a new major or mutation; startup/lineage still apply.

Before sync/no-drift/closeout/release-ready verify:
- meaning and authority-role boundaries, parent/maps/backlinks/history-done reachability and current references
- runtime/design/changelog versions, selected phase/Patch links, source-owned install array safety and substantive Runtime bodies
- touched God pressure repaired or visibly owned/planned/deferred; ambiguity surfaced as blocker
- required helper-fit burst was narrowed/routed under capture/routing owners or a valid narrow direct exception recorded
- every worker-authored governed edit and selected decision-changing anchor leader-verified

Worker handoffs are evidence, not proof. [Routing](worker-routing-and-context.md) owns net benefit/brief/write limits; [I/O](safe-io.md) burst narrowing. Known anchors, tight interactive flow, high overlap, unavailable tools or user direction may justify direct work. Missing required verification blocks its claim.

Splits/shards/rollovers check future read cost and reference/preservation integrity. Delegated edits need exact disjoint anchors, stable meaning/history/roles and non-destructive permission. Ambiguous authority/history/destruction or analysis-only scope blocks routine repair.

## Creation and Hygiene Boundaries

Reuse the fitting owner. Create only required functional code/config, requested documents, startup-selected governed artifacts (including triggered diagrams), or necessary run evidence placed/retained under [coding-discipline.md](coding-discipline.md). No unrequested summaries/checkpoints/plans, duplicate authority or version-suffixed `-v2`, `_final`, `_backup`, `_draft`, `_old` copies. Ask only for real need/ownership ambiguity; startup grants no arbitrary creation/deletion.

Resolve shared-destination owners before classification. Keep reusable artifacts portable, exact local facts scoped. Cleanup/hygiene/isolation/worktree/sandbox/co-location/untracked state/missing recognition never establishes disposability or root replacement; semantic authority and explicit destructive confirmation remain required. [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) owns notation/binding, [accurate-communication.md](accurate-communication.md) claim wording, and [phase-todo-artifact.md](phase-todo-artifact.md)/[execution-and-goal-frame.md](execution-and-goal-frame.md) startup/continuation.
