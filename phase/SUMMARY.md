# RULES Phase Summary

> **Current Version:** 1.66
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.31
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Status:** P087-01 / v9.92 daily-first governance rollover completed; active summary remains compact for current-state scans
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
| completed | P087-01 | [phase-087-01-daily-first-governance-rollover-history-sharding.md](phase-087-01-daily-first-governance-rollover-history-sharding.md) | Add daily-first rollover governance for oversized active control files | Runtime owner, adjacent owner sync, compact TODO/SUMMARY entrypoints, v9.92 master sync | 46/46 source-runtime parity and body sufficiency pass, master push succeeds, release `v9.92` is verified |
| deferred | P086 | none opened | Constructive-dissent / anti-over-agreement refinement | Not selected in this wave | User explicitly selects P086 after P087 |

---

## Current Phase Detail

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
- Earlier phase-map and extraction tables through P085 remain preserved in the pre-rollover snapshot instead of this active summary.

---

## Verification Focus

- [x] Pre-rollover `phase/SUMMARY.md` snapshot exists.
- [x] Active `phase/SUMMARY.md` now references `phase/history/` and `phase/done/` surfaces.
- [x] Active `TODO.md` references `todo/history/` and `todo/done/` surfaces.
- [x] README, master design, master changelog, TODO, phase, and patch records are synchronized for v9.92 source state.
- [x] Runtime install arrays contain exactly 46 source-owned active runtime rule files.
- [x] Source/runtime parity and active runtime body sufficiency pass for 46/46 files.
- [x] Git push and GitHub release `v9.92` are verified.

---

## Rollback / Containment

If P087-01 is reversed, keep the pre-rollover snapshots until a safer migration is selected. Do not delete `history/` or `done/` shards as cleanup; rollover is reference-preserving history movement, not deletion authority.
