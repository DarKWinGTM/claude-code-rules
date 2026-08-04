# Document Integrity

> **Current Version:** 1.7
> **Design:** [design/document-integrity.design.md](design/document-integrity.design.md) v1.7
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/document-integrity.changelog.md](changelog/document-integrity.changelog.md)

---

## Rule Statement

**Core Principle: Keep names, paths, identifiers, parent/shard roles, and cross-references consistent across checked scope; prevent duplicate or ambiguous governed parent authority; roll accumulated TODO and phase-summary history into daily-first referenced shards before size bloat causes context loss; prevent unnecessary junk files and duplicate artifacts while explicitly allowing required governed startup artifacts from `artifact-initiation-control`; and never use rollover, hygiene, cleanup, isolation, worktree, sandbox, runtime co-location, untracked state, or missing recognition as standalone deletion authority.**

This rule owns cross-reference consistency, change propagation, reference verification, daily-first governance rollover, active-entrypoint/history/done shard boundaries, oversize-trigger response, existing-file migration, and creation/duplication hygiene. It does not replace TODO, phase, changelog, destructive-confirmation, or safe-file-reading semantics.

---

## Core Contract

### 1) Cross-reference consistency

- keep names, paths, identifiers, and references consistent across the response or checked artifact set
- verify concrete references or mark them unknown/unverified, and verify impacted files/sections before sync/no-drift claims
- update or describe dependencies when a change impacts multiple files/sections
- treat source comments that cite governed docs as checked references; update or remove the comment when the referenced path or anchor moves out of checked scope
- keep scoped non-findings scoped when a source comment's governed-doc reference is not found; do not silently upgrade a limited search into a global broken-link claim
- separate portable shared references, checked local facts, machine-scoped examples, source-side install paths, destination/runtime paths, governed design parent indexes, governed design child shards, active parent changelogs, changelog version detail shards, changelog legacy/archive/fallback history, source-owned active runtime install scope, shared runtime destinations, other-owner runtime files, and local execution paths
- keep governed design parent indexes and child/sibling shards aligned so selected chain shape, shard maps, parent scope, child target-state authority, and normalized same-stem parent/directory pairs do not drift
- keep active parent changelog shard maps and chain-scoped version detail child/sibling shards aligned so selected chain shape, version-to-shard mapping, shard-to-parent back-links, normalized same-stem parent/directory pairs, and non-authority detail status do not drift
- when a governed design/changelog parent uses active shards, make the selected chain shape explicit enough that no-drift review can distinguish single-file bootstrap, flat sibling shard mode, same-stem normalized mode, and archive fallback mode
- keep namespace scope, parent model choice, selected parent filename, coexistence state, bootstrap exit trigger, and shard-opening basis aligned but distinct when they materially affect structure selection
- keep observed project shape, extracted doctrine, selected target form, and any equivalence claim basis aligned but distinct when a checked example is used to justify governance structure
- keep `changelog/done/` distinct from ordinary chain-scoped version detail shards unless the checked parent authority selects it as legacy, archive, completed-history, or fallback history
- when the compact active-entrypoint model is selected, keep `TODO.md` and `phase/SUMMARY.md` visibly current rather than letting history/done shards silently become the effective owner path
- keep other-owner runtime files outside the current project's parity/install target set unless owner/project scope is explicitly selected or verified
- include active runtime body sufficiency when claiming source/runtime parity, no-drift, release readiness, or active runtime install success
- defer broader portability and anti-hardcoding to `portable-implementation-and-hardcoding-control.md`

#### Reference roles and checks

| Type | Preferred form | Check |
|---|---|---|
| File/source path | `<workspace-root>/src/config.js`, `<repo-root>`, or repo-root `./`; exact path only as scoped local fact | Glob / Read / command context |
| Governed design generic parent | `design/design.md` when the checked folder already fully scopes one design chain | Read role statement and verify no competing semantic active parent exists |
| Governed design semantic parent index | `design/<slug>.design.md` when the checked folder contains several chains or needs a self-identifying parent filename | Read parent index and verify shard map plus declared chain shape |
| Governed design child shard | `design/<slug>/<slice>.design.md` as active target-state detail in same-stem nested mode | Parent shard map + targeted Read |
| Governed design flat sibling shard | `<current-design-folder>/<slice>.design.md` beside the compact parent when the current folder already scopes the chain | Parent shard map + declared flat sibling mode + targeted Read |
| Active generic parent changelog | `changelog/changelog.md` when the checked folder already fully scopes one changelog chain | Read role statement and verify no competing semantic active parent exists |
| Active semantic parent changelog | `changelog/<chain>.changelog.md` when the checked folder contains several chains or needs a self-identifying parent filename | Read parent and verify current version plus shard map and declared chain shape |
| Changelog version detail shard | `changelog/<chain>/vX.YY-short-topic.changelog.md` as indexed same-chain version detail in same-stem nested mode | Parent shard map + shard-to-parent back-link |
| Changelog flat sibling version detail shard | `<current-changelog-folder>/vX.YY-short-topic.changelog.md` beside the compact parent when the current folder already scopes the chain | Parent shard map + declared flat sibling mode + shard-to-parent back-link |
| Changelog legacy/archive/fallback history | `changelog/done/*.changelog.md` as inactive-by-default history | Active parent reference or audit/rollback/provenance need |
| Source comment governed-doc reference | `design/<slug>.design.md#section`, `phase/phase-NNN-*.md#section`, or `patch/<context>.patch.md#section` when a source comment materially points outside code | Verify cited path/anchor; update or remove the comment if the referenced target moves or no longer resolves in checked scope |
| Destination/runtime path | `<install-root>/skills`, `<user-runtime-rules>` | config/source contract check |
| Source-owned active runtime files | checked current-project install set with substantive root bodies, not every shared-destination file or metadata-only stub | checked source inventory + body-sufficiency check |
| Shared destination / other-owner runtime file | destination may contain several owners; non-members need owner/project scope | source/destination contract + owner resolution |
| Local execution path | exact current-machine/harness path only | execution context |
| Symbol / command / config | `getUserById`, `npm run build`, `DATABASE_URL` | search, run when needed, or read config source |

Verify before asserting: concrete references, cross-file sync/no-drift, rename/move/update impact, ambiguous references; parent-index-to-child/sibling-shard and active-parent-changelog-to-version-detail child/sibling-shard alignment, selected chain-shape declaration, shard map completeness, orphan/stale shard status, mixed-mode drift, `changelog/done/` fallback drift; namespace-scope / parent-model-choice / selected-parent-filename / coexistence-state / bootstrap-exit-trigger / shard-opening-basis alignment when naming and timing affect structure selection; observed-project-shape / extracted-doctrine / selected-target-form separation plus equivalence-claim basis when an example is used as doctrine evidence; parity scope vs shared-destination ownership, active runtime body sufficiency; worker-edited governed docs before sync/no-drift/closeout/release-ready claims; tool-path leakage. If checked scope is limited, report the non-finding as scoped rather than global absence.

### 2) God-file, worker-gate, and delegated-repair consistency

A sync must not move content into the wrong owner or overload one active file: verify current state, target-state design, version history, execution tracking, phase execution, patch review, and rollback detail remain in their owning surfaces; when a touched document is split, sharded, or rolled over, verify parent/index links, shard maps, back-links, and child/history/done references; include God Phase and God Patch split decisions in no-drift review when phase or patch files are touched; do not claim sync/no-drift if active docs became role-overloaded even though versions and links match.

A no-drift/sync/closeout/release-ready claim is invalid when: (a) touched governed documents still have unresolved God pressure neither repaired nor represented as a visible governed repair slice (repaired splits reflected in links/indexes; planned repair has a visible owner in task/TODO/phase/patch/changelog; broad deferred repair labeled as deferred; unresolved ambiguity surfaced as a blocker); (b) the leader skipped worker-first filtering for a worker-fit aggregate read with no narrow direct-handling exception recorded (worker handoff must return filtered findings, conflicts, exact anchors, and leader verification needs; leader must verify selected anchors; direct leader handling is limited to narrow known files, exact edit/verify ranges, or a stated narrow exception); or (c) worker-edited governed documents have not been leader-verified. Worker handoff is input, not proof.

Leader verification must check: meaning preservation and authority-role boundaries; history/done reachability and cross-reference resolution; version alignment across runtime/design/changelog surfaces; phase and patch links when touched; README install-array safety when install/onboarding surfaces are touched; source-owned runtime install scope and active runtime body sufficiency. Skipped or incomplete verification is a blocker.

### 3) Active entrypoints stay current

`TODO.md` and `phase/SUMMARY.md` remain mandatory active entrypoints. Keep them focused on current state, active/pending work, current roadmap/index, and links to retained history. Do not let daily/history/done shards replace the root navigation role. Move accumulated movement, completed detail, and old phase-map bulk into referenced shards when size triggers fire. Keep enough context for a fresh session to find the current work without reading every historical detail.

### 4) Daily-first rollover model

Use daily history shards first for ordinary accumulation:

```text
TODO.md
  → current active task index
  → todo/history/YYYY-MM-DD*.md
  → todo/done/<task-or-wave>.md when detail is too large for the active file

phase/SUMMARY.md
  → current phase roadmap/index
  → phase/history/YYYY-MM-DD*.md
  → phase/done/phase-NNN-*.md when completed phase detail is retained outside active scans
```

Daily history stores what moved today, compact closeout notes, rollover snapshots, and audit trail. `done/` stores larger completed task, wave, or phase detail that should remain reachable but inactive by default.

### 5) Size and thrash triggers

Soft triggers (rollover considered): active entrypoint exceeds ~250-300 lines or ~25-30 KB; completed/history content larger than current active content; reader must scan 200+ lines to find current state.

Hard triggers (rollover required before further broad absorption): active entrypoint exceeds ~500 lines or ~50 KB; tool reads fail or become oversized; autocompact thrashing points to repeated large-file or output absorption; active-file reads repeatedly refill context after compact.

Thresholds are practical guardrails, not deletion authority. A file may roll over earlier when scanability is already degraded.

### 6) Existing oversized file migration

Existing large `TODO.md`, `phase/SUMMARY.md`, or comparable governed entrypoints must be managed, not exempted: (1) preserve a pre-rollover snapshot or equivalent reachable history shard; (2) classify content as active current state, pending/deferred state, completed detail, daily movement, or historical index/detail; (3) keep active current/pending state in the entrypoint; (4) move historical/completed bulk into `history/` or `done/` shards; (5) add bidirectional references (entrypoint↔shard); (6) verify active items were not lost and moved history remains reachable.

### 7) Reference integrity and no orphan shards

Main files must point to history and done surfaces when those surfaces exist or are part of the governed model: active entrypoints link to the relevant daily/history/done shards; shards identify their parent entrypoint and scope; moved history remains reachable from the active file; no shard should become an orphan authority guessed by filename alone; archive/detail files are inactive by default unless the active entrypoint selects them for current review.

When normalized parent/shard mode is selected for a broad design or changelog chain, verify the compact parent still names the selected chain shape and active shard map and that child/version shards remain reachable through the parent rather than through archive fallback paths.

When flat sibling shard mode is selected, verify the compact parent explicitly declares that mode, names the active sibling shard map, and prevents the same chain from silently competing with a same-stem nested shard directory at the same time.

### 8) Rollover is not cleanup deletion

Rollover preserves meaning. It does not authorize deletion. Not allowed: deleting historical content because a file is large; treating completed status as disposable; removing shards because they are inactive by default; using context bloat, autocompact thrash, cleanup, hygiene, or convenience as removal authority; claiming no active item was lost without checking active/pending references after migration.

### 9) God-document repair routing and automatic planning

God-file pressure is a rollover and redistribution signal: route accumulated TODO movement to `todo/history/` or `todo/done/`; route accumulated phase movement to `phase/history/` or `phase/done/`; keep active entrypoints as maps after rollover, not link-only placeholders; do not roll active target-state design truth into history/done (use design sharding or changelog history separation); preserve bidirectional references.

When God-document pressure points to TODO or phase accumulation, rollover becomes an owned repair action: repair immediately when current/history/done split is clear and low-risk; create or extend a visible repair slice when rollover needs broader classification; preserve active entrypoints as compact maps after any split; keep moved history reachable through parent and shard references; block closeout when touched active entrypoints remain overloaded without a repaired or planned route. Rollover repair remains preservation work; never cleanup deletion.

### 9.1) Document-density, compact-thrash, and delegated governed-document repair
Active governed documents should stay cheap to read and edit.

Required guidance:
- keep one line or bullet focused on one concept or one tight fact group
- split current state, history, verification, risks, exclusions, and next work when they start to mix
- treat very long active lines as repair triggers, not disposal proof
- when a touched area is a clear low-risk God-line candidate, repair it in the same change instead of only warning about it
- when the split is history-heavy, authority-shifting, broad, or meaning-risky, record a visible repair slice instead of forcing an unsafe edit
- treat compact/thrash or repeated oversized rereads as repair signals; diagnose whether the cause is dense files, oversized entrypoints, missed worker routing, or raw output flooding
- after non-trivial governance edits, verify future read cost as well as semantic sync by checking long lines, mixed current/history summary lines, and whether touched density debt was repaired or explicitly flagged
- delegated governed-document repair is allowed only when the repair is bounded, meaning-preserving, assigned to exact artifacts/anchors, and preserves history reachability, authority roles, and non-destructive behavior
- if repair ambiguity, authority ambiguity, history risk, destructive risk, or analysis-only scope remains, do not delegate the edit as routine worker work

Named action modes for touched-scope repair remain:
- `REPAIR_NOW`
- `DELEGATE_REPAIR`
- `PLAN_IN_CURRENT_PHASE`
- `OPEN_REPAIR_PATCH`
- `OPEN_NEW_PHASE_OR_SUBPHASE`
- `BLOCK_CLOSEOUT`
- `ASK_ONLY_IF_AMBIGUOUS`

### 10) File hygiene

- **Existing file first:** if the right authority file exists and still fits the role, edit it instead of creating a duplicate or parallel authority.
- **No junk docs:** do not create unnecessary summaries, duplicate plans, checkpoint/work-summary files, or version-suffixed copies such as `-v2`, `_final`, `_backup`, `_draft`, or `_old` unless the user explicitly requests them.
- **Ask when unclear:** unclear artifact necessity is a question, not permission to create speculative files or silently skip a required governed startup artifact.
- **Governed-startup exception:** required design/changelog/TODO/phase/patch startup artifacts from `artifact-initiation-control` may be created proactively and are not junk. Ambiguous startup need still requires asking; this exception applies only to required governed startup artifacts, not arbitrary summaries or duplicate docs; it does not authorize deletion of newly encountered files merely because they do not match the expected artifact set.
- **Shared-destination boundary:** destination/runtime files outside the current source-owned active runtime install set are not junk merely because they share a runtime directory; resolve owner/project scope before classification.
- **Portable-artifact hygiene:** reusable helpers/support artifacts avoid machine-local defaults unless explicitly machine-scoped; broader portability defers to `portable-implementation-and-hardcoding-control.md`.
- **No deletion by hygiene:** hygiene, cleanup, isolation, worktree, sandbox, runtime co-location, untracked state, or missing recognition is never standalone deletion authority; removal needs stronger semantic authority plus the destructive-confirmation owner.

---

## Allowed vs Not Allowed

Allowed creation: functional code/config required for operation; documents explicitly requested by the user; required governed startup artifacts from `artifact-initiation-control`; intentionally short-lived temporary files in `/tmp`.

Not allowed: version-suffixed copies (`-v2`, `_final`, `_draft`, `_backup`, `_old`); checkpoint/summary/plan/work-summary files not requested and not required by startup governance; duplicate authority artifacts when an existing file already serves the role; treating untracked/newly seen or shared-destination files as junk by cleanup instinct alone; using hygiene/cleanup/isolation/worktree/sandbox/runtime co-location rationale as deletion authority.

---

## Output and Cross-Section Standards

Use precise portable placeholders (`<workspace-root>/src/config.js`, `<repo-root>`, `<install-root>`, `<user-runtime-rules>`), exact values only as checked local facts, stable line/symbol references when useful (`config.js:42`, `getUserById()`), and explicit labels:

```markdown
✅ Verified: `<workspace-root>/src/config.js`
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found In Checked Scope: `/missing/file.js`
```

Avoid vague references ("the config file", "that function") or one workstation path acting as both source and destination/runtime path. In reusable source artifacts prefer placeholders or env/config resolution. Source-owned install scope points to checked source inventory, not every file in a shared runtime destination. Source/runtime parity names both install scope and body sufficiency; a hash match to a metadata-only root is not no-drift.

Change-impact expectations: renaming/moving files updates imports, links, install examples, source comments that cite governed docs, and dependent paths; renaming symbols updates usages within checked scope; changing config keys or commands updates related docs, examples, and verification instructions; normalizing install docs keeps source-side, destination/runtime, shared destination, and other-owner runtime wording separate; sharding changelog version detail updates parent shard maps, shard-to-parent back-links, and `changelog/done/` fallback wording together; runtime parity/no-drift checks body sufficiency as well as metadata/links/hashes. Classify new files against master surfaces and dependent history; keep classification unresolved when checked scope is incomplete.

---

## Decision Flows

### Reference consistency

```text
Create reference
  ↓
Does it exist or resolve?
  → YES: use precise reference
  → NO: mark unknown/unverified
  ↓
What role? (portable shared / source-side / design parent index / design child shard / active parent changelog / changelog version detail shard / changelog fallback history / source-owned active runtime / shared runtime destination / other-owner runtime / checked local fact / machine-scoped example)
  ↓
Consistent with related references?
  → YES: continue
  → NO: fix inconsistency
```

Change impact flow: identify affected references → list dependencies → update related references → verify consistency.

### Governance rollover

```text
Governed entrypoint read or update planned
  ↓
Size/thrash trigger present?
  → NO: update normally, keep current/history balance
  → YES: continue
  ↓
Is this an active entrypoint?
  → YES: preserve snapshot, split history/done detail, keep compact current index
  → NO: check owning rule before moving content
  ↓
References updated both ways?
  → NO: repair entrypoint and shard links
  → YES: verify active items and moved history are reachable
```

### File hygiene

```text
AI wants to create a file
  ↓
Correct authority file exists?
  → YES: edit existing file
  → NO: create only if functional code/config, required governed startup artifact, user-requested document, or allowed short-lived /tmp file
  → Otherwise: do not create

AI wants to classify/remove a newly encountered file
  ↓
Shared runtime destination and outside current source-owned install set?
  → YES: resolve owner/project scope first
  ↓
Master surfaces / governed history checked?
  → NO: check first and keep classification unresolved
  ↓
Stronger semantic authority plus destructive confirmation exists?
  → YES: follow the destructive-confirmation owner
  → NO: do not delete
```

Cleanup, hygiene, isolation, sandbox, worktree, runtime co-location, and git state can explain why a file looks suspicious, but they do not decide whether it is disposable. If a file's semantic role is unclear, preserve it and resolve authority first.

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

- duplicate authority artifacts when an existing file serves the role; unrequested summary/checkpoint/plan/work-summary or version-suffixed copies
- treating untracked/newly seen or shared-destination files as junk without owner/project scope resolution
- using hygiene/cleanup/isolation/worktree/sandbox/runtime co-location rationale as deletion authority
- deleting historical content because a file is large; treating completed or inactive-by-default status as disposable
- using context bloat, autocompact thrash, cleanup, or convenience as removal authority
- claiming no active item was lost without checking active/pending references after migration
- letting daily/history/done shards replace the root navigation role; leaving orphan shards guessed by filename alone
- claiming sync/no-drift when active docs became role-overloaded even though versions and links match
- skipping worker-first filtering for a worker-fit aggregate read without a narrow direct-handling exception; treating worker handoff as proof instead of leader-verified input
- vague references ("the config file", "that function"); one workstation path acting as both source and destination/runtime path
- treating missing recognition or co-location as disposal proof

---

## Integration

- [phase-todo-artifact.md](phase-todo-artifact.md) - startup artifact posture owner
- [authority-and-scope.md](authority-and-scope.md) - user authority and runtime co-location ownership boundary
- [document-governance.md](document-governance.md) - compact design index and governed child shard role boundaries
- [document-governance.md](document-governance.md) - active parent changelog, version detail shard, and fallback history boundaries
- [execution-and-goal-frame.md](execution-and-goal-frame.md) - rollover maintenance as continuation gate when large files block safe execution
- [action-safety.md](action-safety.md) - verify execution intent when references affect actions; destructive-confirmation owner for removal
- [evidence-discipline.md](evidence-discipline.md) - verify values, not only existence; do not guess required file identities
- [phase-todo-artifact.md](phase-todo-artifact.md) - phase summary/index and completed phase history
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable/local and source/destination notation and anti-hardcoding
- [document-governance.md](document-governance.md) - repository-wide document-role model and governed history surfaces
- [safe-io.md](safe-io.md) - bounded reads and oversized file handling
- [phase-todo-artifact.md](phase-todo-artifact.md) - TODO active index, durable tracking, and pending-only discipline
- [document-governance.md](document-governance.md) - active runtime body-sufficiency and version-governance validation
- [evidence-discipline.md](evidence-discipline.md) - do not fabricate references
