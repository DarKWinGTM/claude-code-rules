# Governed Document Rollover Control Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-08)
> **Full history:** [../changelog/governed-document-rollover-control.changelog.md](../changelog/governed-document-rollover-control.changelog.md)

---

## Current Target State

The RULES repository needs active governance entrypoints that stay readable during long development runs. `TODO.md` and `phase/SUMMARY.md` remain the navigation roots, but accumulated completed detail, daily movement, and historical phase index bulk should move into daily-first referenced shards once size or autocompact pressure makes active scanning unsafe.

This design creates one first-class owner for that behavior: daily-first rollover is an active governance maintenance mechanism, not a cleanup instinct and not a replacement for TODO or phase authority.

---

## P091 Target State: God-Document Repair Routing

Rollover is one repair route for God-document pressure in active TODO and phase entrypoints.

It preserves current maps while moving accumulated daily movement or completed detail to reachable history/done shards.

It does not replace design sharding, changelog history governance, or phase/patch splitting when those owners fit better.

## 1) Goal

Define a deterministic rollover model for long-lived governed control files so future work can keep current state small while preserving historical detail.

The target behavior is:
- `TODO.md` stays the current durable execution index
- `phase/SUMMARY.md` stays the active phase roadmap/index
- daily movement/history lives under `todo/history/` and `phase/history/`
- large completed detail lives under `todo/done/` or `phase/done/` when the owning rule allows it
- main files reference the shards they rely on
- shards link back to their parent entrypoint
- existing oversized files are migrated instead of ignored
- no content is deleted merely because it is old, completed, or large

---

## 2) Scope

Applies to governed active entrypoint files whose accumulated content can damage context efficiency or cause repeated oversized reads.

Primary targets:
- `TODO.md`
- `phase/SUMMARY.md`

Aligned precedent:
- active changelog plus `changelog/done/` history separation

Out of scope:
- making design docs use `design/done/`
- changing changelog version authority
- deleting old files or history
- installing history/done shards as runtime rules
- compressing active runtime rule bodies

---

## 3) Rollover Model

### 3.1 Active entrypoints

The active file carries only what a fresh session needs first: current state, active/pending items, current phase roadmap/index, and reachable pointers to historical detail.

### 3.2 Daily history

Daily history is the default rollover target for ordinary movement and large pre-rollover snapshots.

Examples:
- `todo/history/2026-05-08.md`
- `phase/history/2026-05-08.md`
- `phase/history/2026-05-08-pre-rollover-SUMMARY.md`

### 3.3 Done detail

`done/` stores larger completed detail that is still governed history but inactive by default. For phase detail, filenames keep the existing phase grammar where possible. For TODO detail, filenames should identify the task, wave, or rollover reason.

### 3.4 Reference integrity

A valid split is not just file movement. The parent entrypoint must reference the child shard, and the child shard must identify the parent. This keeps history discoverable after compaction, handoff, or fresh-session re-entry.

---

## 4) Trigger Strategy

Soft triggers should start rollover planning:
- roughly 250-300 lines
- roughly 25-30 KB
- completed/history sections exceed active/current sections
- active state requires scanning 200+ lines

Hard triggers require rollover or a narrow bounded-read workaround before broad continuation:
- roughly 500 lines
- roughly 50 KB
- read/tool output fails from size
- autocompact thrashing identifies file/output bloat
- repeated active-file reads refill context shortly after compact

The thresholds are intentionally practical and reviewable. They should not become deletion criteria.

---

## 5) Existing Oversized File Migration

Existing oversized files follow the same model as future ones. The migration should preserve a snapshot, classify current versus historical content, rewrite the active entrypoint as a compact index, and verify that current/pending work and moved history remain reachable.

The migration may be staged, but if a hard trigger is already blocking safe execution, the active entrypoint should be compacted before more broad reads depend on it.

---

## 6) Integration Notes

- `todo-standards` owns TODO semantics and pending-only discipline.
- `phase-implementation` owns phase summary, phase history, and phase done semantics.
- `project-documentation-standards` owns repository-level recognition of the surfaces.
- `safe-file-reading` owns bounded reads and read-thrash handling.
- `execution-continuity-and-mode-selection` owns when rollover maintenance becomes a continuation gate.
- `strict-file-hygiene` and destructive-confirmation owners continue to block deletion-by-cleanup behavior.

---

## 7) Verification

A rollover is acceptable only when:
- active entrypoints remain the first lookup surface
- `history/` and `done/` surfaces are referenced from the entrypoint when used
- shards link back to parent entrypoints
- active/pending work remains visible in the active entrypoint
- pre-rollover content is preserved or intentionally summarized with a reachable source
- runtime install lists exclude history/done shards unless a future explicit gate changes scope

---

> **Full history:** [../changelog/governed-document-rollover-control.changelog.md](../changelog/governed-document-rollover-control.changelog.md)
