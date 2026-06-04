# Changelog - Document Integrity

> **Parent Document:** [../document-integrity.md](../document-integrity.md)
> **Current Version:** 1.8
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.8 | 2026-06-04 | **[Added P138 governed-doc source-comment reference integrity](#version-18)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.7 | 2026-06-03 | **[Added P135 governed goal route-plan file-hygiene carve-out](#version-17)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.6 | 2026-05-18 | **[Added P108 document-density and repair-owner uptake](#version-16)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.5 | 2026-05-17 | **[Added P105 folder-scoped generic-parent integrity refinement](#version-15)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.4 | 2026-05-17 | **[Added P104 naming and dual-parent integrity refinement](#version-14)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.3 | 2026-05-17 | **[Added P103 observed-shape, doctrine, and target-form integrity checks](#version-13)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.2 | 2026-05-17 | **[Added P102 chain-shape integrity and flat-sibling verification](#version-12)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.1 | 2026-05-17 | **[Added P101 normalized parent-shard integrity refinement](#version-11)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.0 | 2026-05-16 | **[Created merged runtime owner chain](#version-10)** | 6ecc64cf-8eed-497a-9b84-02f5d5228ee3 |
| | | Summary: Created `document-integrity.md` as a body-sufficient merged runtime owner for cross-reference consistency, rollover integrity, hygiene boundaries, and no-delete-by-cleanup discipline in the compact 18-rule runtime set. | |

---

<a id="version-18"></a>
## Version 1.8: Added P138 governed-doc source-comment reference integrity

**Date:** 2026-06-04
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.7 to v1.8.
- Updated `design/document-integrity.design.md` from v1.7 to v1.8.
- Added integrity expectations for source comments that cite governed documents, including checked path/section/reference treatment.
- Required cited governed-doc links in source comments to be updated or removed when paths, headings, owner roles, or nearby behavior change.
- Preserved file-hygiene and no-delete-by-cleanup boundaries; this entry does not claim release, publish, install, tag, or runtime parity completion.

### Summary
`document-integrity.md` now treats governed-doc citations inside source comments as maintainable checked references rather than harmless local text that can silently go stale.

---

<a id="version-17"></a>
## Version 1.7: Added P135 governed goal route-plan file-hygiene carve-out

**Date:** 2026-06-03
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.6 to v1.7.
- Updated `design/document-integrity.design.md` from v1.6 to v1.7.
- Added a narrow file-hygiene exception for route-only plan files required by the selected governed `/goal` authoring contract.
- Preserved the ban on speculative summaries/checkpoints, duplicate authority artifacts, and version-suffixed plan copies.

### Summary
`document-integrity.md` now allows the exact route-only plan artifact that governed `/goal` authoring needs without reopening junk-plan creation behavior.

---

<a id="version-16"></a>
## Version 1.6: Added P108 document-density and repair-owner uptake

**Date:** 2026-05-18
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.5 to v1.6.
- Updated `design/document-integrity.design.md` from v1.5 to v1.6.
- Absorbed document-density, compact-thrash, God-line/God-file, and delegated governed-document repair doctrine that had been duplicated in worker-routing.
- Preserved preservation-first, no-delete, and no-drift semantics while compacting the routing owner.

### Summary
`document-integrity.md` now owns the moved document-density and governed-document repair doctrine needed to keep worker-routing compact.

---

<a id="version-15"></a>
## Version 1.5: Added P105 folder-scoped generic-parent integrity refinement

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.4 to v1.5.
- Updated `design/document-integrity.design.md` from v1.4 to v1.5.
- Replaced master-only generic-parent assumptions with namespace-scope integrity checks.
- Added explicit verification that folder-scoped generic parents are valid only when no competing semantic active parent remains.
- Preserved bootstrap timing checks, parent/shard integrity, and no-delete-by-cleanup boundaries.

### Summary
`document-integrity.md` now carries the P105 corrective refinement needed to verify generic-parent use by namespace scope without allowing dual-parent authority drift.

---

<a id="version-14"></a>
## Version 1.4: Added P104 naming and dual-parent integrity refinement

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.3 to v1.4.
- Updated `design/document-integrity.design.md` from v1.3 to v1.4.
- Added integrity coverage for actual chain subject, selected parent filename, compatibility-parent role, bootstrap exit trigger, and shard-opening basis.
- Added explicit verification that generic compatibility parents and semantic active parents do not remain ambiguous competing owners.
- Preserved existing parent/shard integrity, reference consistency, rollover discipline, and no-delete-by-cleanup boundaries.

### Summary
`document-integrity.md` now carries the P104 integrity refinement needed to verify semantic parent naming and bootstrap-vs-shard timing without leaving dual-parent ambiguity behind.

---

<a id="version-13"></a>
## Version 1.3: Added P103 observed-shape, doctrine, and target-form integrity checks

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.2 to v1.3.
- Updated `design/document-integrity.design.md` from v1.2 to v1.3.
- Added no-drift review coverage so `observed project shape`, `extracted doctrine`, `selected target form`, and `equivalence claim basis` stay aligned but distinct when checked examples ground governance structure.
- Extended integrity verification so checked example structure is not collapsed into the selected RULES target form without checked equivalence evidence.
- Preserved parent/shard integrity, reference consistency, rollover discipline, and no-delete-by-cleanup boundaries.

### Summary
`document-integrity.md` now carries the P103 integrity refinement needed to keep example-backed governance wording precise during sync, verification, and closeout.

---

<a id="version-12"></a>
## Version 1.2: Added P102 chain-shape integrity and flat-sibling verification

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.1 to v1.2.
- Updated `design/document-integrity.design.md` from v1.1 to v1.2.
- Expanded integrity checks so parent design/changelog authorities now verify declared chain shape, sibling-shard maps, and no-orphan/no-mixed-mode drift.
- Added reference-role entries for flat sibling design shards and flat sibling changelog version-detail shards.
- Strengthened no-drift review so parent/sibling and parent/nested shard modes are distinguished explicitly instead of being inferred from filename shape alone.

### Summary
`document-integrity.md` now carries the P102 chain-shape integrity refinement needed to keep flat sibling shard mode reviewable without weakening existing normalized parent/shard checks.

---

<a id="version-11"></a>
## Version 1.1: Added P101 normalized parent-shard integrity refinement

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `document-integrity.md` from v1.0 to v1.1.
- Updated `design/document-integrity.design.md` from v1.0 to v1.1.
- Added normalized same-stem parent/shard integrity and compact-entrypoint visibility checks.
- Strengthened no-orphan and archive-fallback verification for broad design/changelog chains and compact TODO/phase entrypoints.

### Summary
`document-integrity.md` now carries the P101 normalized parent-shard integrity refinement while preserving reference, rollover, and no-delete-by-cleanup discipline.

---
<a id="version-10"></a>
## Version 1.0: Created merged runtime owner chain

**Date:** 2026-05-16
**Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3

### Changes
- Created `document-integrity.md` as an active runtime rule in the compact merged runtime set.
- Created `design/document-integrity.design.md` as the target-state companion for the merged owner chain.
- Preserved absorbed-rule behavior for document consistency, governed rollover, file hygiene, shard links, and active entrypoint integrity.
- Kept historical legacy root files outside the active runtime authority after merge cleanup.

### Summary
`document-integrity.md` now provides one governed runtime owner for cross-reference consistency, rollover integrity, hygiene boundaries, and no-delete-by-cleanup discipline, reducing root-rule fragmentation while preserving execution-relevant doctrine.
