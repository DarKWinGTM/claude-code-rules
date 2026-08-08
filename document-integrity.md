# Document Integrity

> **Current Version:** 1.10
> **Design:** [design/document-integrity.design.md](design/document-integrity.design.md) v1.10
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/document-integrity.changelog.md](changelog/document-integrity.changelog.md)

---

## Rule Statement

**Core Principle: Keep names, paths, identifiers, parent/shard roles, and cross-references consistent across checked scope; prevent duplicate or ambiguous governed parent authority; roll accumulated TODO and phase-summary history into daily-first referenced shards before size bloat causes context loss; prevent unnecessary junk files and duplicate artifacts while explicitly allowing required governed startup artifacts selected by `phase-todo-artifact.md`; and never use rollover, hygiene, cleanup, isolation, worktree, sandbox, runtime co-location, untracked state, or missing recognition as standalone deletion authority.**

This rule owns cross-reference consistency, change propagation, reference verification, daily-first governance rollover, active-entrypoint/history/done shard boundaries, oversize-trigger response, existing-file migration, and creation/duplication hygiene. It does not replace TODO, phase, changelog, destructive-confirmation, or safe-file-reading semantics.

---

## Core Contract

### 1) Cross-reference and governed-chain consistency
Keep names, paths, identifiers, and references consistent across checked scope; verify concrete targets or mark them unknown, propagate rename/move/key/command changes, and keep non-findings scoped. Governed-document references in source comments are checked dependencies and must be updated or removed when their target moves.

For a design/changelog chain selected under `document-governance.md`, verify:
- exactly one active parent model and no ambiguous generic/semantic coexistence
- declared chain shape and complete parent map
- child/version ownership, parent back-links, and no orphan, stale, duplicate, or mixed-mode authority
- history/fallback remains distinct from ordinary active detail
- observed example, extracted doctrine, selected target, and equivalence basis remain distinct when applicable

Keep active entrypoints current and history/done reachable; do not let shards replace `TODO.md` or `phase/SUMMARY.md` navigation. Separate portable/shared references, checked local facts, source/install paths, destination/runtime paths, source-owned runtime scope, and other-owner runtime files. Source/runtime parity and release-ready claims also require active runtime body sufficiency.

| Reference family | Integrity check |
|---|---|
| path, symbol, command, config | resolve from the relevant file/search/command scope and propagate dependents |
| governed parent/shard/history | parent role, declared map, back-link, active/inactive role, no competing authority |
| source comment → governed doc | cited path/anchor resolves after changes |
| source-owned runtime set | checked inventory and substantive bodies |
| shared destination / other owner | resolve owner/project scope before classification |
| local or machine-specific value | label checked local scope; defer portable defaults to `portable-implementation-and-hardcoding-control.md` |

### 2) God-file, worker-gate, and delegated-repair consistency

A sync must not move content into the wrong owner or overload one active file: verify current state, target-state design, version history, execution tracking, phase execution, patch review, and rollback detail remain in their owning surfaces; when a touched document is split, sharded, or rolled over, verify parent/index links, shard maps, back-links, and child/history/done references; include God Phase and God Patch split decisions in no-drift review when phase or patch files are touched; do not claim sync/no-drift if active docs became role-overloaded even though versions and links match.

A no-drift/sync/closeout/release-ready claim is invalid when: (a) touched governed documents still have unresolved God pressure neither repaired nor represented as a visible governed repair slice (repaired splits reflected in links/indexes; planned repair has a visible owner in task/TODO/phase/patch/changelog; broad deferred repair labeled as deferred; unresolved ambiguity surfaced as a blocker); (b) the leader skipped worker-first filtering for a worker-fit aggregate read with no narrow direct-handling exception recorded (worker handoff must return filtered findings, conflicts, exact anchors, and leader verification needs; leader must verify selected anchors; direct leader handling is limited to narrow known files, exact edit/verify ranges, or a stated narrow exception); or (c) worker-edited governed documents have not been leader-verified. Worker handoff is input, not proof.

Leader verification must check: meaning preservation and authority-role boundaries; history/done reachability and cross-reference resolution; version alignment across runtime/design/changelog surfaces; phase and patch links when touched; README install-array safety when install/onboarding surfaces are touched; source-owned runtime install scope and active runtime body sufficiency. Skipped or incomplete verification is a blocker.

### 3) Active entrypoints and daily-first rollover
`TODO.md` and `phase/SUMMARY.md` remain bodyful current-state entrypoints; history/done never replaces root navigation.

```text
TODO.md → todo/history/YYYY-MM-DD*.md → todo/done/<task-or-wave>.md
phase/SUMMARY.md → phase/history/YYYY-MM-DD*.md → phase/done/phase-NNN-*.md
```

Daily history stores movement/snapshots; `done/` stores larger completed detail. All moved content remains inactive-by-default, parent-linked, back-linked, and reachable.

### 4) Trigger and migration contract
Consider rollover around 250–300 lines, 25–30 KB, history larger than current content, or 200+ lines to reach current state. Require it before further broad absorption around 500 lines, 50 KB, failed/oversized reads, repeated compact refill, or autocompact thrash. These are scanability triggers, never deletion authority.

For an oversized entrypoint: preserve a reachable snapshot; classify current, pending/deferred, completed, daily, and historical content; keep current/pending state in the entrypoint; move only the appropriate bulk; update references both ways; and verify no active item or retained history was lost.

Rollover preserves meaning. File size, completed/inactive status, context bloat, cleanup, hygiene, or convenience never authorizes deletion.

### 5) Density and God-document repair
Keep active lines concept-focused and separate current state, history, verification, risks, exclusions, and next work when they mix. Repair clear low-risk touched density now; otherwise create a visible owner-specific repair slice. TODO/phase accumulation routes to their history/done surfaces, while active design truth uses design sharding rather than rollover history.

Delegated repair requires bounded exact artifacts/anchors, meaning preservation, history reachability, stable authority roles, and non-destructive behavior. Ambiguous authority, history/destructive risk, or analysis-only scope blocks routine delegated edits. Verify future read cost after non-trivial governance changes.

Action modes remain: `REPAIR_NOW`, `DELEGATE_REPAIR`, `PLAN_IN_CURRENT_PHASE`, `OPEN_REPAIR_PATCH`, `OPEN_NEW_PHASE_OR_SUBPHASE`, `BLOCK_CLOSEOUT`, `ASK_ONLY_IF_AMBIGUOUS`.

### 6) File hygiene
- edit the existing fitting authority before creating a parallel one
- create only required functional code/config, user-requested documents, governed startup artifacts selected by `phase-todo-artifact.md`, or short-lived `/tmp` files
- do not create unrequested summaries/checkpoints/work plans, duplicate authorities, or version-suffixed copies such as `-v2`, `_final`, `_backup`, `_draft`, or `_old`
- ask when artifact need or ownership is ambiguous; required-startup status does not authorize arbitrary creation or deletion
- resolve owner/project scope before classifying files in shared destinations
- keep reusable artifacts portable unless explicitly machine-scoped
- hygiene, cleanup, isolation, worktree, sandbox, runtime co-location, untracked state, or missing recognition never authorizes deletion; removal requires stronger semantic authority and destructive confirmation

---

## Output and Change-Impact Standards
Use precise portable placeholders, exact local values only as checked local facts, and stable path/line/symbol references when useful. Wording labels defer to `accurate-communication.md`; avoid vague references or one local path acting as both source and runtime destination.

Renames/moves update imports, links, install examples, governed-doc comments, and dependent paths; symbol/key/command changes update checked usages and examples. Chain changes update maps, back-links, and active/fallback roles together. Runtime parity checks source-owned scope and substantive bodies, not hashes alone. Keep new-file classification unresolved until relevant authority/history and owner scope are checked.

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| new/renamed/moved file, symbol, config key, command | update related references and verify consistency across checked scope |
| sync/no-drift/closeout/release-ready claim | verify impacted files/sections, worker handoffs, and body sufficiency |
| sharded design or changelog structure | verify parent index/shard map, shard-to-parent back-links, selected-shard scope |
| touched governed document shows God pressure | route to split/shard/rollover repair with preserved links |
| active entrypoint hits soft/hard size/thrash trigger | roll over into daily history/done shards with bidirectional references |
| oversized existing `TODO.md`/`phase/SUMMARY.md` | migrate with snapshot, classification, and reference integrity |
| new/unclear file appears | check master surfaces, resolve owner/project scope, keep classification unresolved when incomplete |
| cleanup/hygiene/isolation/co-location rationale for deletion | stop; require stronger semantic authority plus destructive-confirmation owner |

---

## Anti-Patterns
Avoid duplicate authority/junk artifacts; classifying new, untracked, co-located, or shared-destination files without owner scope; any deletion justified only by size/status/cleanup/hygiene/isolation/worktree/sandbox/context pressure; orphan or root-replacing shards; unverified no-loss/no-drift claims; worker handoffs treated as proof; or vague/machine-local references presented as portable authority.

---

## Integration
Related owners:
- [document-governance.md](document-governance.md) — roles, chain shapes, runtime body sufficiency
- [phase-todo-artifact.md](phase-todo-artifact.md) / [execution-and-goal-frame.md](execution-and-goal-frame.md) — startup, active entrypoints, continuation
- [safe-io.md](safe-io.md) / [evidence-discipline.md](evidence-discipline.md) — bounded checks and claim scope
- [action-safety.md](action-safety.md) / [authority-and-scope.md](authority-and-scope.md) — destructive confirmation and ownership
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) — portable reference forms
