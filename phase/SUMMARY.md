# RULES Phase Summary

> **Current Version:** 1.67
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.31
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Status:** P088 / v9.93 memory root-index relative scope compaction completed, installed, pushed, and released
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Daily History:** [history/2026-05-08.md](history/2026-05-08.md)
> **Pre-Rollover Snapshot:** [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
> **Completed Detail:** [done/](done/)

---

## Current Purpose

This file is the compact active phase roadmap/index. Historical phase-map detail before P087-01 is intentionally not duplicated here; use the pre-rollover snapshot for audit, rollback, or provenance.

Active scans should start here, then follow `history/` or `done/` links only when the current task needs historical detail.

---

## Active Phase Roadmap

| State | Phase | File | Goal | Output | Gate |
|---|---|---|---|---|---|
| completed | P088 | [phase-088-memory-root-index-relative-scope-compaction.md](phase-088-memory-root-index-relative-scope-compaction.md) | Compact root memory indexing without hiding active memory meaning | Memory-governance v1.7, root `MEMORY.md` `Scope` + `Memory base` format, v9.93 master sync | Source docs sync, runtime install, 46/46 parity/body sufficiency, `master` push, and release `v9.93` verified |
| completed | P087-01 | [phase-087-01-daily-first-governance-rollover-history-sharding.md](phase-087-01-daily-first-governance-rollover-history-sharding.md) | Add daily-first rollover governance for oversized active control files | Runtime owner, adjacent owner sync, compact TODO/SUMMARY entrypoints, v9.92 master sync | 46/46 source-runtime parity and body sufficiency pass, master push succeeds, release `v9.92` is verified |
| deferred | P086 | none opened | Constructive-dissent / anti-over-agreement refinement | Not selected in this wave | User explicitly selects P086 after P088 |

---

## Current Phase Detail

### P088 — Memory Root Index Relative Scope Compaction

- **Status:** Completed
- **Design References:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md) v1.7
- **Patch References:** [../patch/memory-root-index-relative-scope-compaction.patch.md](../patch/memory-root-index-relative-scope-compaction.patch.md)
- **Expected Output:** root `MEMORY.md` remains a useful active index while path-scoped sections declare one canonical `Scope` and one `Memory base`, then list visible relative one-line hooks; README, master design/changelog, TODO, phase, and patch records align to v9.93 / P088.
- **Completion Gate:** source docs synchronized, runtime install copies only README-listed active runtime rules, 46/46 source/runtime parity and body sufficiency pass, `master` is pushed, and GitHub release `v9.93` is verified.

### P087-01 — Daily-First Governance Rollover and History Sharding

- **Status:** Completed
- **Design References:** [../design/governed-document-rollover-control.design.md](../design/governed-document-rollover-control.design.md) v1.0; [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) v2.37; [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.26; [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.31
- **Patch References:** [../patch/daily-first-governance-rollover-history-sharding.patch.md](../patch/daily-first-governance-rollover-history-sharding.patch.md)
- **Expected Output:** compact active `TODO.md` and `phase/SUMMARY.md`; reachable `todo/history`, `todo/done`, `phase/history`, and `phase/done` references; new rollover runtime owner; v9.92 synced master records.
- **Completion Gate:** source docs synchronized, runtime install copies only README-listed active runtime rules, 46/46 source/runtime parity and body sufficiency pass, `master` is pushed, and GitHub release `v9.92` is verified.

---

## History and Done References

- Daily phase movement: [history/2026-05-08.md](history/2026-05-08.md)
- Pre-rollover phase summary snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Completed phase detail surface: [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)

---

## Recent Completed Release Context

- P085-01 / v9.91 was completed, installed, pushed, and released with 45/45 runtime parity/body-sufficiency gates passed.
- P087-01 / v9.92 was completed, installed, pushed, and released with 46/46 runtime parity/body-sufficiency gates passed.
- P088 / v9.93 was completed, installed, pushed, and released with 46/46 runtime parity/body-sufficiency gates passed.
- Earlier phase-map and extraction tables through P085 remain preserved in the pre-rollover snapshot instead of this active summary.

---

## Verification Focus

- [x] Pre-rollover `phase/SUMMARY.md` snapshot exists.
- [x] Active `phase/SUMMARY.md` references `phase/history/` and `phase/done/` surfaces.
- [x] Active `TODO.md` references `todo/history/` and `todo/done/` surfaces.
- [x] Memory governance runtime/design/changelog align at v1.7.
- [x] Active root `MEMORY.md` uses `Scope` + `Memory base` sections with visible relative hooks.
- [x] README, master design, master changelog, TODO, phase, and patch records are synchronized for v9.93 / P088 source state.
- [x] Runtime install arrays contain exactly 46 source-owned active runtime rule files.
- [x] Source/runtime parity and active runtime body sufficiency pass for 46/46 files.
- [x] Git push and GitHub release `v9.93` are verified.

---

## Rollback / Containment

If P088 is reversed, restore the prior root `MEMORY.md` layout and memory-governance v1.6 doctrine from the v9.93 rollback point while keeping memory detail files intact. Do not delete memory detail files, `history/`, or `done/` shards as cleanup; both P087 rollover and P088 memory-index compaction are reference-preserving governance changes, not deletion authority.
