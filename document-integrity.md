# Document Integrity
> **Current Version:** 1.15
> **Design:** [design/document-integrity.design.md](design/document-integrity.design.md) v1.15
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/document-integrity.changelog.md](changelog/document-integrity.changelog.md)

## Rule Statement

**Core Principle: Preserve names, roles, references, history and project state across the checked change. Distinguish Runtime payload parity from Active Project Root convergence; prevent split/duplicate authority, roll oversized entrypoints without losing meaning, and never derive deletion or root replacement from size, cleanliness, isolation or missing recognition.**

This owner verifies cross-reference/chain/rollover integrity and file hygiene. [document-governance.md](document-governance.md) owns roles/chain selection/body eligibility; [authority-and-scope.md](authority-and-scope.md) selects the Active Project Root; [action-safety.md](action-safety.md) approves destructive operations.

## Propagate and Verify Changed Contracts

Resolve concrete paths/symbols/keys/commands or mark unknown; propagate changes through relevant imports, config/build/deploy/install examples, tests/discovery, links and source-comment document references. Rename/move requires recomputed relative paths, not basename guesses. Symbol/key/command changes update checked consumers/examples. Bounded excerpts/nonfindings prove only their scope.

For selected design/changelog chains verify one active generic/semantic parent, declared shape/complete map, child/version ownership/backlinks, no orphan/stale/duplicate/mixed authority, and inactive reference separation. Keep observed example, extracted doctrine, selected target and equivalence basis distinct. Chain changes update map/backlinks and active/inactive roles together.

Bodyful TODO/phase summary remains navigation; shards/history cannot replace it. Separate portable/shared references, checked local values, source/install and destination/runtime paths, source-owned payload and other-owner files. No runtime parity/no-drift/release-ready claim from hashes without substantive bodies.

For migration/authority replacement, verify applicable manifests/imports/dependencies/config/build/deploy/tests/discovery/generated inputs/acceptance select current authority only. History/done/quarantine is provenance, never active/fallback/generated/normal-discovery input. [evidence-discipline.md](evidence-discipline.md) owns two-sided proof; one moved file or grep is insufficient.

## Payload Versus Project Convergence

| Proof layer | Required checked scope |
|---|---|
| Runtime payload parity | selected ordered install payload, bytes/modes/bodies/manifests and destination state |
| Full-project convergence | relevant Active Project Root source/config/Rules/governance/scripts/tests/plugin/support/tooling/generated declarations/modes and classified modified/untracked state |

Payload/candidate/tag/release/clone parity cannot stand for whole-project convergence or authorize root replacement. Preserve local-only/unclassified paths until owner/disposition is resolved: modified/untracked is neither semantic truth nor junk replaceable from public state. Block applicable sync/no-drift/closeout while authoritative/newer state is split, canonical-only components unexplained, or alternate locations own source/task/phase/Patch/commit/release inputs. Disposable verification changes are not implementation.

Report mixed results explicitly rather than hide the failed layer:
```text
Runtime payload parity: passed
Active Project Root convergence: failed or blocked
Completion: blocked
```

Name exactly which layer/scope passed. A bounded payload task may report payload-only success; it cannot close unresolved required project convergence.

## Evidence-bound Patch Timeline Migration

Before mutation build a deterministic manifest: each selected row has admissible original-creation evidence, old/new exact paths, source SHA-256/mode, dependent governed-reference hashes/modes and proposed metadata. Indirect chronology such as mtime/ctime cannot fill a gap; ambiguous rows stay blocked.

Resolve each exact reference to its real old target and recompute relative links after rename across Phase/design/changelog/TODO/history/done/Patch companion history. No global basename replacement, wildcard-example rewrite (`patch/*.patch.md`) or serialized request/transcript mutation by default. Explicitly suspended archive is a sentinel: preserve names/bytes/modes/inactive-disconnected role and exclude it from mutation rows.

Apply only with unchanged manifest/source/reference hashes and explicit action/scope approval. Create generated manifest/journal exclusively with owner-only permissions where supported. Persist rollback journal **before first mutation**, replace references atomically, and classify unchanged/staged/applied states. Rollback is deliberate, not automatic fallback; stop on any hashes/modes outside original/applied journal states.

Verify target filename/metadata, exact updated references, former-path inactivity and preserved sentinel together. Selected ambiguous rows, active old references or archive normal discovery keep migration incomplete. [document-governance.md](document-governance.md) owns exact timestamp/metadata/admissible evidence, not this operational journal.

## Bodyful Entry and Preservation-first Rollover

```text
TODO.md → todo/history/YYYY-MM-DD*.md → todo/done/<task-or-wave>.md
phase/SUMMARY.md → phase/history/YYYY-MM-DD*.md → phase/done/phase-NNN-*.md
```

Daily history stores movement/snapshots; done stores larger completed detail. Moved content stays inactive-by-default, parent-linked/backlinked/reachable. Current/pending/deferred remains visible in compact active entrypoints.

Consider rollover at 250–300 lines, 25–30 KB, history exceeding current content or 200+ lines to reach current state. Require it before further broad absorption at roughly 500 lines/50 KB, failed oversized reads, repeated compact refill or autocompact thrash. These are scanability signals, not deletion permission.

Preserve a reachable snapshot → classify current/pending-deferred/completed/daily/historical → move only suitable bulk → update both directions → verify no active item/retained history lost. File size, completed/inactive status, context bloat or convenience cannot justify deletion.

## Density, Owner Repair and Leader Verification

Keep current truth/history/proof/risks/exclusions/next work concept-focused and correctly owned; version/link parity does not excuse role overload. Clear low-risk touched density is repaired locally; otherwise record visible owner-specific planned/deferred/blocked repair. TODO/phase overflow uses history/done; active design truth uses coherent sharding. God Phase/Patch decisions remain explicit when those owners are touched.

Disposition modes: `REPAIR_NOW`, `DELEGATE_REPAIR`, `PLAN_IN_CURRENT_PHASE`, `OPEN_REPAIR_PATCH`, `OPEN_NEW_PHASE_OR_SUBPHASE`, `BLOCK_CLOSEOUT`, `ASK_ONLY_IF_AMBIGUOUS`. Their names are not permission for artifacts, a new major or mutation; startup/lineage still apply.

Before sync/no-drift/closeout/release-ready verify:
- meaning and authority-role boundaries, parent/maps/backlinks/history-done reachability and current references
- runtime/design/changelog versions, selected phase/Patch links, source-owned install array safety and substantive Runtime bodies
- touched God pressure repaired or visibly owned/planned/deferred; ambiguity surfaced as blocker
- required helper-fit burst was narrowed/routed under capture/routing owners or a valid narrow direct exception recorded
- every worker-authored governed edit and selected decision-changing anchor leader-verified

Worker handoffs are filtered evidence, not proof. [worker-routing-and-context.md](worker-routing-and-context.md) owns net benefit/brief/write limits; [safe-io.md](safe-io.md) owns burst narrowing. Known files/exact edit/proof ranges, tight interactive sequence, high overlap, unavailable tools or explicit direction may justify direct handling. Incomplete required verification blocks the corresponding claim.

Non-trivial split/shard/rollover repairs verify future read cost as well as references/preservation. Delegated edits require exact non-overlapping artifacts/anchors, stable meaning/history/roles and non-destructive permission; ambiguous authority/history/destructive risk or analysis-only scope prevents routine repair.

## Creation and Hygiene Boundaries

Use the existing fitting owner first. Create only required functional code/config, requested documents, startup-selected governed artifacts (including conditional diagrams), or short-lived `/tmp` evidence. No unrequested summaries/checkpoints/plans/duplicate authority/version-suffixed `-v2`, `_final`, `_backup`, `_draft`, `_old` copies. Ask only for real need/ownership ambiguity; startup never authorizes arbitrary creation/deletion.

Resolve shared-destination owners before classification. Keep reusable artifacts portable, exact local facts scoped. Cleanup/hygiene/isolation/worktree/sandbox/co-location/untracked state/missing recognition never establishes disposability or root replacement; semantic authority and explicit destructive confirmation remain required. [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) owns notation/binding, [accurate-communication.md](accurate-communication.md) claim wording, and [phase-todo-artifact.md](phase-todo-artifact.md)/[execution-and-goal-frame.md](execution-and-goal-frame.md) startup/continuation.
