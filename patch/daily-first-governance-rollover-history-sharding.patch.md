# Daily-First Governance Rollover and History Sharding Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/governed-document-rollover-control.design.md](../design/governed-document-rollover-control.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P087-01 addresses active governance entrypoint bloat in long-lived RULES work. The immediate checked examples are `TODO.md` and `phase/SUMMARY.md`, which exceeded practical active-read thresholds and caused `phase/SUMMARY.md` full-read failure. The user selected a daily-first split model and required the main files to reference `done/` and `history/` so shards do not become orphaned.

This patch is governance/rules/docs only. No product code is in scope.

---

## 2) Analysis

Current RULES already recognizes `phase/done/`, `patch/done/`, and `changelog/done/` as inactive history surfaces, but it lacks a first-class owner for daily-first rollover of active control files that grow during long development.

The target behavior should:
- keep `TODO.md` and `phase/SUMMARY.md` as compact current entrypoints
- preserve old content in reachable history/done shards
- use daily history as the default split model
- manage already oversized files, not only future files
- treat autocompact thrash and oversized read failures as maintenance triggers
- avoid deletion-by-size or cleanup-by-rollover

---

## 3) Change Items

### ROL-001 — New active runtime owner

- **Target artifacts:** `../governed-document-rollover-control.md`, `../design/governed-document-rollover-control.design.md`, `../changelog/governed-document-rollover-control.changelog.md`
- **Change type:** additive

**Before**
```text
No first-class runtime owner defines daily-first rollover, size/thrash triggers, existing oversized-file migration, or main-to-history reference integrity for TODO/SUMMARY-style governance entrypoints.
```

**After**
```text
`governed-document-rollover-control` owns daily-first rollover, active entrypoint preservation, history/done shard reference integrity, existing oversized file migration, and no-deletion-by-rollover boundaries.
```

### ROL-002 — Adjacent owner sync

- **Target artifacts:** `../project-documentation-standards.md`, `../todo-standards.md`, `../phase-implementation.md`, `../document-changelog-control.md`, `../safe-file-reading.md`, `../execution-continuity-and-mode-selection.md`, plus paired design/changelog files
- **Change type:** additive + metadata alignment

**Before**
```text
Existing owners define active/done boundaries and bounded reads, but they do not require daily-first active-index/history rollover for growing TODO and phase summary files.
```

**After**
```text
Existing owners recognize `todo/history`, `todo/done`, `phase/history`, and `phase/done` as referenced inactive history/detail surfaces while preserving `TODO.md` and `phase/SUMMARY.md` as active current-state entrypoints.
```

### ROL-003 — Existing oversized file migration

- **Target artifacts:** `../TODO.md`, `../phase/SUMMARY.md`, `../todo/history/2026-05-08-pre-rollover-TODO.md`, `../phase/history/2026-05-08-pre-rollover-SUMMARY.md`, and applicable `done/` references
- **Change type:** restructuring

**Before**
```text
`TODO.md` and `phase/SUMMARY.md` carry accumulated historical detail directly in active scan surfaces, making active reads oversized and context-expensive.
```

**After**
```text
Main entrypoints become compact current indexes with references to `history/` and `done/`; pre-rollover content remains reachable through daily history snapshots.
```

### ROL-004 — Master release sync

- **Target artifacts:** `../README.md`, `../design/design.md`, `../changelog/changelog.md`, this patch file, and `../phase/phase-087-01-daily-first-governance-rollover-history-sharding.md`
- **Change type:** companion sync

**Before**
```text
Master records are synchronized through v9.91 / P085-01 with 45 active runtime rules.
```

**After**
```text
Master records record v9.92 / P087-01, active runtime count increases to 46 after the new rollover owner is installed, and current-state README sections describe active-index/history rollover without dumping changelog detail.
```

---

## 4) Verification

- [x] New rollover owner has substantive runtime body and companion design/changelog files.
- [x] Adjacent owner chains reference rollover without replacing their own semantic roles.
- [x] Pre-rollover `TODO.md` snapshot is preserved.
- [x] Pre-rollover `phase/SUMMARY.md` snapshot is preserved.
- [x] Main `TODO.md` references `todo/history/` and `todo/done/`.
- [x] Main `phase/SUMMARY.md` references `phase/history/` and `phase/done/`.
- [x] Runtime install arrays contain exactly 46 source-owned active runtime rule files.
- [x] Runtime install copies only README-listed active runtime rule files.
- [x] Source/runtime parity and body sufficiency pass for all active runtime files.
- [x] Git push and GitHub release `v9.92` are verified.

---

## 5) Rollback Approach

If P087-01 is too broad:
- revert the v9.92 commit
- preserve pre-rollover snapshots until a safer migration is approved
- narrow size thresholds or surface ownership without deleting history shards
- if the new rollover owner is removed, update active runtime count, README install arrays, master design inventory, runtime install, and release records coherently
- do not delete unrelated runtime destination files or history/done shards by cleanup instinct
