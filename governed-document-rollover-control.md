# Governed Document Rollover Control

> **Current Version:** 1.1
> **Design:** [design/governed-document-rollover-control.design.md](design/governed-document-rollover-control.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/governed-document-rollover-control.changelog.md](changelog/governed-document-rollover-control.changelog.md)

---

## Rule Statement

**Core Principle: Keep active governance entrypoints small, current, and navigable by rolling accumulated TODO and phase-summary history into daily-first referenced shards before size bloat causes context loss, while preserving all governed meaning and never using rollover as deletion authority.**

This rule owns daily-first governance rollover, active-index/history/done shard boundaries, oversize-trigger response, existing-file migration, and reference-integrity checks for long-lived governed control files. It does not replace TODO semantics, phase semantics, changelog authority, file hygiene, destructive confirmation, or safe file-reading behavior.

---

## Core Contract

### 1) Active entrypoints stay current

`TODO.md` and `phase/SUMMARY.md` remain mandatory active entrypoints.

Required guidance:
- keep active entrypoints focused on current state, active/pending work, current roadmap/index, and links to retained history
- do not let daily/history/done shards replace the root navigation role
- move accumulated movement, completed detail, and old phase-map bulk into referenced shards when size triggers fire
- keep enough context in the active entrypoint for a fresh session to find the current work without reading every historical detail

### 2) Daily-first rollover model

Use daily history shards first for ordinary accumulation.

Preferred structure:

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

### 3) Size and thrash triggers

Rollover should be considered when any soft trigger is met:
- an active governance entrypoint exceeds roughly 250-300 lines
- an active governance entrypoint exceeds roughly 25-30 KB
- completed/history content is larger than current active content
- a reader must scan 200+ lines to find current state

Rollover is required before further broad absorption when any hard trigger is met:
- an active governance entrypoint exceeds roughly 500 lines
- an active governance entrypoint exceeds roughly 50 KB
- tool reads fail or become oversized because of the file
- autocompact thrashing points to repeated large file or output absorption
- active-file reads repeatedly refill context after compact

Thresholds are practical guardrails, not deletion authority. A file may roll over earlier when scanability is already degraded.

### 4) Existing oversized file migration

Existing large `TODO.md`, `phase/SUMMARY.md`, or comparable governed entrypoints must be managed, not exempted.

Migration steps:
1. preserve a pre-rollover snapshot or equivalent reachable history shard
2. classify content as active current state, pending/deferred state, completed detail, daily movement, or historical index/detail
3. keep active current/pending state in the entrypoint
4. move historical/completed bulk into `history/` or `done/` shards
5. add bidirectional references: entrypoint to shard, shard back to parent entrypoint
6. verify active items were not lost and moved history remains reachable

### 5) Reference integrity and no orphan shards

Main files must point to history and done surfaces when those surfaces exist or are part of the governed model.

Required guidance:
- active entrypoints link to the relevant daily/history/done shards
- shards identify their parent entrypoint and scope
- moved history remains reachable from the active file
- no shard should become an orphan authority that must be guessed by filename alone
- archive/detail files are inactive by default unless the active entrypoint selects them for current review

### 6) Rollover is not cleanup deletion

Rollover preserves meaning. It does not authorize deletion.

Not allowed:
- deleting historical content because a file is large
- treating completed status as disposable status
- removing shards because they are inactive by default
- using context bloat, autocompact thrash, cleanup, hygiene, or convenience as removal authority
- claiming no active item was lost without checking active/pending references after migration

---

### 7) God-document repair routing

God-file pressure is a rollover and redistribution signal when active entrypoints accumulate roles beyond their purpose.

Required guidance:
- route accumulated TODO movement to `todo/history/` or `todo/done/`
- route accumulated phase movement to `phase/history/` or `phase/done/`
- keep active entrypoints as maps after rollover, not link-only placeholders
- do not roll active target-state design truth into history/done; use design sharding or changelog history separation instead
- preserve bidirectional references so moved detail remains reachable

Rollover may be part of God-document repair, but the repair must preserve meaning and owner boundaries.

## Decision Flow

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

---

## Verification Checklist
- [ ] God-document pressure is repaired through role-aware rollover/sharding/splitting without deleting governed meaning.

- [ ] `TODO.md` and `phase/SUMMARY.md` remain active current-state/navigation entrypoints.
- [ ] Daily-first `history/` shards exist when movement/history bulk is moved out.
- [ ] `done/` references exist for completed detail surfaces when applicable.
- [ ] Main files reference moved shards, and shards link back to parent entrypoints.
- [ ] Existing oversized files are migrated or explicitly queued when hard triggers block safe broad reading.
- [ ] Active/pending items are preserved after rollover.
- [ ] Rollover did not delete governed meaning or classify files as disposable by size alone.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Active entrypoint scanability | High |
| Orphaned history/done shards | 0 |
| Active item loss during rollover | 0 critical cases |
| Rollover-as-deletion incidents | 0 critical cases |
| Oversized active entrypoint thrash | Low |

---

## Integration

Related rules:
- [project-documentation-standards.md](project-documentation-standards.md) - repository document-role model and governed history surfaces
- [todo-standards.md](todo-standards.md) - TODO active index, durable tracking, and pending-only discipline
- [phase-implementation.md](phase-implementation.md) - phase summary/index and completed phase history
- [document-changelog-control.md](document-changelog-control.md) - changelog active history/version authority and `changelog/done/` precedent
- [safe-file-reading.md](safe-file-reading.md) - bounded reads and oversized file handling
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - rollover maintenance as a continuation gate when large files block safe execution
- [strict-file-hygiene.md](strict-file-hygiene.md) - rollover is preservation, not cleanup deletion

---

> **Full history:** [changelog/governed-document-rollover-control.changelog.md](changelog/governed-document-rollover-control.changelog.md)
