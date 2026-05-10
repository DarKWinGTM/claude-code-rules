# Governed Design Sharding Compact Index Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.96
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P089 adds doctrine for active governed design documents that become too large for safe repeated reads. The concrete evidence came from NodeClaw's `api-payg-ai-proxy-gateway.design.md` recovery pattern: the main design file became a compact active index, while detailed target-state sections moved into governed child design shards under `design/api-payg-ai-proxy-gateway/`.

พูดง่าย ๆ: นี่ไม่ใช่การย้าย design เก่าไป archive แต่เป็นการทำ design active ให้แบ่งอ่านได้โดยยังคง authority ชัดเจน.

This patch does not add a new active runtime rule. The active runtime install count remains 46.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `document-design-control.md` owns governed design document structure and active design authority.
- `project-documentation-standards.md` owns repository-wide document role modeling.
- `safe-file-reading.md` owns bounded file-reading behavior and context-flood prevention.
- `document-consistency.md` owns cross-reference, shard map, and no-drift verification.
- Master records (`design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, `phase/SUMMARY.md`) must describe v9.96 / P089 consistently.

Review concerns:
- Do not create a default `design/done` model.
- Do not classify child design shards as inactive history by default.
- Do not make compact indexes link-only routers with no active target-state summary.
- Do not let broad shard sweeps become default leader-session raw absorption.
- Do not increase the active runtime rule count.
- Do not edit NodeClaw files; NodeClaw is evidence for RULES behavior only.

---

## 3) Change Items

### GDSCI-001 — Compact design index and governed child shard doctrine

- **Target artifacts:** `../document-design-control.md`, `../design/document-design-control.design.md`, `../changelog/document-design-control.changelog.md`
- **Change type:** additive runtime/design refinement

**Before**
```text
`document-design-control` requires governed design files to be active target-state truth, avoids default `design/done`, and keeps history in changelog governance, but it does not define a compact active index plus governed child shard model for large active designs.
```

**After**
```text
`document-design-control` v1.11 defines governed design sharding: `design/<slug>.design.md` remains the compact active index/authority gateway, while `design/<slug>/*.design.md` child shards remain active target-state design detail. The index must preserve purpose, authority, shard map, current target-state summary, and read path; child shards must identify parent/index scope and not become hidden or conflicting authority.
```

### GDSCI-002 — Repository role model for design shards

- **Target artifacts:** `../project-documentation-standards.md`, `../design/project-documentation-standards.design.md`, `../changelog/project-documentation-standards.changelog.md`
- **Change type:** additive repository model refinement

**Before**
```text
The required document set lists `design/*.design.md` as active target behavior/contract and states that design has no default `design/done` surface.
```

**After**
```text
`project-documentation-standards` v2.38 adds `design/<slug>/*.design.md` as governed active child design shards for large designs whose compact parent index stays at `design/<slug>.design.md`. The model keeps shards active by default, distinguishes them from history/done rollover, and requires current-state scans to begin at the parent index.
```

### GDSCI-003 — Index-first, shard-selective reading

- **Target artifacts:** `../safe-file-reading.md`, `../design/safe-file-reading.design.md`, `../changelog/safe-file-reading.changelog.md`
- **Change type:** additive read-path refinement

**Before**
```text
Safe-file-reading covers bounded file reads and oversized TODO/phase entrypoint rollover triggers, but does not define how to read sharded active design surfaces.
```

**After**
```text
`safe-file-reading` v1.6 says sharded governed designs should be read index-first, then by selected child shards only. Broad shard audits should use worker filtering when context-heavy. Design sharding is not the same as TODO/phase history rollover because child shards remain active design target-state.
```

### GDSCI-004 — Index-to-shard consistency and drift checks

- **Target artifacts:** `../document-consistency.md`, `../design/document-consistency.design.md`, `../changelog/document-consistency.changelog.md`
- **Change type:** additive consistency refinement

**Before**
```text
Document-consistency verifies references, source/destination roles, runtime install scope, body sufficiency, and junk/disposal classification, but not compact design index to child-shard consistency.
```

**After**
```text
`document-consistency` v1.10 includes governed design shard references as a reference role and requires parent-index-to-child-shard consistency checks before no-drift or sync claims. Checks include stale shard maps, missing or orphan shards, conflicting shard authority, and scoped non-findings when only selected shards were read.
```

### GDSCI-005 — Master governed record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.95/P076-04 as the current release and do not yet record governed design sharding compact-index doctrine.
```

**After**
```text
Master records describe v9.96/P089 with the active runtime count still 46. README current-state guidance names governed design sharding as the latest refinement without replacing changelog history, and TODO/phase surfaces track release gates accurately.
```

### GDSCI-006 — P089 phase record and release boundary

- **Target artifact:** `../phase/phase-089-governed-design-sharding-compact-index.md`
- **Change type:** additive phase record

**Before**
```text
No P089 child phase record exists for governed design sharding compact-index doctrine.
```

**After**
```text
A P089 phase record tracks owner-chain updates, master governed sync, runtime install/parity/body-sufficiency checks, git push, and GitHub release `v9.96` gates.
```

---

## 4) Verification

Runtime install, source/runtime parity, and active runtime body sufficiency passed for 46/46 active files with destination extras observed-only. `master` push and GitHub release `v9.96` are verified.

- [x] `document-design-control` runtime/design/changelog updated and audited at v1.11.
- [x] `project-documentation-standards` runtime/design/changelog updated and audited at v2.38.
- [x] `safe-file-reading` runtime/design/changelog updated and audited at v1.6.
- [x] `document-consistency` runtime/design/changelog updated and audited at v1.10.
- [x] Master records, README, TODO, phase, and patch describe P089/v9.96 consistently.
- [x] README Bash and PowerShell install arrays remain exactly 46 active runtime files.
- [x] Runtime install parity is verified for the 46 active runtime rule files.
- [x] Active runtime body sufficiency is verified for the 46 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.96` is created.

---

## 5) Rollback Approach

If P089 over-prescribes design sharding or causes confusion:
- narrow compact-index/shard wording while preserving the core active-design-versus-history boundary
- keep `design/done` as not-default unless a separate governed wave changes that model
- keep child shards active target-state by default unless explicitly retired through governed authority
- revert master v9.96 records only through governed rollback
- keep active runtime count at 46 unless a separate governed wave changes the active install set
