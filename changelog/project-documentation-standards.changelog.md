# Changelog - Project Documentation Standards

> **Parent Document:** [../project-documentation-standards.md](../project-documentation-standards.md)
> **Current Version:** 2.42
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

---

## Version History (Unified)

<a id="version-242"></a>
## Version 2.42: Added dedicated diagram lane role model

**Date:** 2026-06-01
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.41 to v2.42.
- Added `diagram/STRUCTURE.md`, `diagram/<subject>.design.md`, and optional child visual shards to the repository role model.
- Clarified that `diagram/` is a dedicated governed visual lane rather than a mirror of `design/**` shard structure.
- Clarified that integrated subject diagrams should start whole and split only when visual complexity or genuinely different visual questions justify it.

### Summary
Project-documentation-standards now treats `diagram/` as a first-class governed visual lane and separates visual-source structure from text-design shard structure.

---

<a id="version-241"></a>
## Version 2.41: Added changelog version detail shard role model

**Date:** 2026-05-13
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated runtime `project-documentation-standards.md` from v2.40 to v2.41.
- Updated `design/project-documentation-standards.design.md` from v2.40 to v2.41.
- Added `changelog/<chain>/v*.changelog.md` as an indexed same-chain version detail surface.
- Clarified that active parent changelogs remain current version authority, index, shard map, and navigation surfaces.
- Reclassified `changelog/done/` as legacy/archive/completed-history/fallback rather than the default split target for ordinary large-chain version detail.

### Summary
Project-documentation-standards now models active parent changelogs, chain-scoped version detail shards, and `changelog/done/` fallback history as distinct documentation surfaces.

---

<a id="version-240"></a>
## Version 2.40: Added automatic God artifact planning role model

**Date:** 2026-05-11
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Added automatic God artifact planning to the repository document-role model.
- Required detected overload to be repaired, routed, visibly planned, deferred, or blocked before sync claims.
- Kept repair role-aware and explicitly outside deletion authority.

### Summary
Added automatic God artifact planning role model for P092 / v10.00.

---

## Version 2.39: Added governed document God-file prevention role model

- Added P091 governed document God-file prevention and repair semantics for this owner chain.
- Preserved role-specific authority boundaries while adding the correct split, shard, rollover, or redistribution route.


| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.42 | 2026-06-01 | **[Added dedicated diagram lane role model](#version-242)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 2.41 | 2026-05-13 | **[Added changelog version detail shard role model](#version-241)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| | | Summary: Modeled active parent changelogs, chain-scoped version detail shards, and `changelog/done/` fallback history as distinct documentation surfaces. | |
| 2.40 | 2026-05-11 | **[Added automatic God artifact planning role model](#version-240)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.38 | 2026-05-10 | **[Added governed design shard role model](#version-238)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.37 | 2026-05-08 | **[Added daily-first governance rollover documentation surfaces](#version-237)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Added `todo/history/`, `todo/done/`, and `phase/history/` to the repository role model while keeping `TODO.md` and `phase/SUMMARY.md` as compact active entrypoints with reachable history/done links. | |
| 2.36 | 2026-05-07 | **[Added README current-state release sync discipline](#version-236)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Clarified that README release sync updates current overview/status/install/latest-refinement/quality signals instead of dumping changelog timelines into the README body | |
| 2.35 | 2026-05-06 | **[Added active runtime body-sufficiency install boundary](#version-235)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Added repository documentation guidance that source-owned active runtime install targets must carry substantive runtime bodies and cannot be satisfied by metadata-only design pointers | |
| 2.34 | 2026-05-06 | **[Recorded repository-level verification coverage alignment for governed coding phases](#version-234)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Added repository documentation alignment for material Development Verification / TestKit Coverage across phase, TODO, changelog, and closeout surfaces without duplicating the verification strategy owner | |
| 2.33 | 2026-05-04 | **[Kept task lists non-authoritative but visibly phase-linked](#version-233)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Clarified that built-in task lists remain live tracking and never define phases, but non-trivial phase-backed entries should visibly point back to active or implied phase context | |
| 2.32 | 2026-05-04 | **[Added phase lineage preservation at the documentation layer](#version-232)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.31 | 2026-04-29 | **[Added completed documentation surface governance](#version-231)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.30 | 2026-04-25 | **[Clarified source-owned runtime install scope in shared destinations](#version-230)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.29 | 2026-04-20 | **[Added bounded `/phase` planning-context use at the repository model layer](#version-229)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.28 | 2026-04-18 | **[Reinforced phase-shaped task creation alignment at the repository model layer](#version-228)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.27 | 2026-04-18 | **[Reasserted governed companion surfaces alongside live execution surfaces](#version-227)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.26 | 2026-04-17 | **[Added master-surface consultation before junk/disposal classification](#version-226)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.25 | 2026-04-17 | **[Reduced memsearch wording to shared-board defer only](#version-225)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 2.24 | 2026-04-17 | **[Reduced repository task-list documentation to global role-model guidance](#version-224)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 2.23 | 2026-04-13 | **[Raised visible session ownership into a default task-list standard](#version-223)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.22 | 2026-04-13 | **[Resynced coordination-companion integration references after wave 038](#version-222)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.21 | 2026-04-13 | **[Separated shared-board request naming from receiving-side execution phase structure](#version-221)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.20 | 2026-04-13 | **[Deferred shared-board multi-session coordination semantics to the new coordination owner](#version-220)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.19 | 2026-04-12 | **[Recognized active execution-discovery surfaces at the repository model layer](#version-219)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.18 | 2026-04-12 | **[Added same-objective live task-list continuity at the repository model layer](#version-218)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.17 | 2026-04-12 | **[Added execution-surface deferral to the new continuity and goal-review owners](#version-217)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.16 | 2026-04-10 | **[Clarified live built-in task tracking versus durable TODO tracking](#version-216)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.15 | 2026-04-09 | **[Kept reusable package-local support assets portable by default](#version-215)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.14 | 2026-04-08 | **[Narrowed repository startup patch posture for greenfield baseline formation](#version-214)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.13 | 2026-04-06 | **[Added support-layer modeling for the optional RULES plugin extension area](#version-213)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 2.12 | 2026-04-02 | **[Added portable public onboarding/install guidance](#version-212)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended project-documentation-standards so README and install/onboarding docs now avoid workstation-specific absolute paths as public defaults and explicitly separate source-side guidance from destination/runtime notation | |
| 2.11 | 2026-04-02 | **[Integrated portable-default documentation guidance](#version-211)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended project-documentation-standards so shared governed docs/templates stay portable by default and now defer anti-hardcoding discipline to `portable-implementation-and-hardcoding-control` | |
| 2.10 | 2026-03-30 | **[Added explicit phase-to-patch linkage verification for phased work](#version-210)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Refined the repository role model so phased work with governed patch artifacts must show explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files | |
| 2.9 | 2026-03-28 | **[Added startup artifact gate and routed repository startup behavior to artifact-initiation-control](#version-29)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Refined the repository role model so meaningful governed work now resolves startup artifact posture before drift instead of relying on late backfill | |
| 2.8 | 2026-03-28 | **[Changed active patch placement to `patch/` or root and aligned repository role wording](#version-28)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Replaced the lingering `patches/` teaching model with an explicit repository-wide patch placement rule using `patch/<context>.patch.md` or root `<context>.patch.md`, while clarifying that patch means a self-identifying before/after artifact | |
| 2.5 | 2026-03-15 | **[Added directory-as-namespace naming guidance for governed document workspaces](#version-25)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Refined project-documentation-standards so namespaced workspaces may use role-based filenames like `design.md`, `changelog.md`, `patch.md`, and `TODO.md` when the parent path already supplies stable context | |

---

<a id="version-238"></a>
## Version 2.38: Added governed design shard role model

**Date:** 2026-05-10
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.37 to v2.38.
- Updated `design/project-documentation-standards.design.md` from v2.37 to v2.38.
- Added `design/<slug>/*.design.md` as governed active child design shards in the repository role model.
- Clarified that compact parent design indexes remain the first current-state lookup surface for sharded active designs.
- Preserved the no-default-`design/done` boundary and kept design shards distinct from completed-history surfaces.

### Summary
Project-documentation-standards now models large active design surfaces as compact parent indexes plus governed child shards, keeping design detail active while reducing broad-read pressure.

---

<a id="version-236"></a>

---

<a id="version-237"></a>
## Version 2.37: Added daily-first governance rollover documentation surfaces

**Date:** 2026-05-08
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Added `todo/history/`, `todo/done/`, and `phase/history/` to the repository role model while keeping `TODO.md` and `phase/SUMMARY.md` as compact active entrypoints with reachable history/done links.

### Summary
Added `todo/history/`, `todo/done/`, and `phase/history/` to the repository role model while keeping `TODO.md` and `phase/SUMMARY.md` as compact active entrypoints with reachable history/done links.

## Version 2.36: Added README current-state release sync discipline

**Date:** 2026-05-07
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.35 to v2.36.
- Updated `design/project-documentation-standards.design.md` from v2.35 to v2.36.
- Clarified README as the current front page for overview, status cards, install arrays, active runtime count, latest refinement, current quality signals, and current safety/runtime notes.
- Clarified that release sync should not turn README into a changelog timeline dump.

### Summary
Project-documentation-standards now makes README release sync current-state-oriented while leaving detailed release history in changelog surfaces.

---

<a id="version-235"></a>
## Version 2.35: Added active runtime body-sufficiency install boundary

**Date:** 2026-05-06
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.34 to v2.35.
- Updated `design/project-documentation-standards.design.md` from v2.34 to v2.35.
- Added repository documentation guidance that README-listed/source-owned active runtime files must contain substantive runtime behavior bodies, not metadata-only design pointers.
- Clarified that runtime install/parity claims include body sufficiency in addition to source-owned scope and metadata alignment.
- Added integration with `unified-version-control-system.md` v1.3 and `document-consistency.md` v1.9.

### Summary
Project-documentation-standards now treats active runtime body sufficiency as part of the repository install model, so design/changelog surfaces cannot stand in for installed runtime rule behavior.

---

<a id="version-234"></a>
## Version 2.34: Recorded repository-level verification coverage alignment for governed coding phases

**Date:** 2026-05-06
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.33 to v2.34.
- Updated `design/project-documentation-standards.design.md` from v2.33 to v2.34.
- Added repository-level guidance that governed coding phases should keep material Development Verification / TestKit Coverage aligned across phase, TODO, changelog, and closeout surfaces.
- Added integration references to `development-verification-and-debug-strategy.md`, `phase-implementation.md` v2.28, and `todo-standards.md` v2.23.
- Preserved document-role boundaries so project-documentation does not duplicate the verification strategy owner.

### Summary
Project-documentation-standards now keeps material coding verification coverage synchronized across governed repository records while leaving the detailed debug/testing/TestKit strategy with the new development verification owner.

---

<a id="version-233"></a>
## Version 2.33: Kept task lists non-authoritative but visibly phase-linked

**Date:** 2026-05-04
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.32 to v2.33.
- Updated `design/project-documentation-standards.design.md` from v2.32 to v2.33.
- Clarified that Claude Code's built-in task list remains live in-session tracking and does not define phases.
- Added the companion boundary that non-trivial phase-backed live task entries should visibly point to active or clearly implied phase context.
- Updated integration references to the touched P076-03 owner versions.
- Preserved runtime install scope, shared-destination owner boundaries, and governed document-role separation.

### Summary
Project-documentation-standards now preserves the task-list-as-pointer model: live task entries can visibly reference phase context without becoming the semantic authority for phases.

---

<a id="version-232"></a>
## Version 2.32: Added phase lineage preservation at the documentation layer

**Date:** 2026-05-04
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.31 to v2.32.
- Updated `design/project-documentation-standards.design.md` from v2.31 to v2.32.
- Clarified that `phase/SUMMARY.md` should preserve phase-family lineage when that context affects later major-vs-subphase decisions.
- Clarified that phase file creation and selection defer to `phase-implementation.md` rather than defaulting documentation startup into a new major phase.
- Preserved completed-history boundaries for `phase/done/`, `patch/done/`, and `changelog/done/`.

### Summary
Project-documentation-standards now supports the phase lineage gate by keeping phase-family relationships visible in governed records without taking over phase identity semantics.

---

<a id="version-231"></a>
## Version 2.31: Added completed documentation surface governance

**Date:** 2026-04-29
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.30 to v2.31.
- Updated `design/project-documentation-standards.design.md` from v2.30 to v2.31.
- Added the completed documentation surface model for `phase/done/`, `patch/done/`, and `changelog/done/`.
- Clarified that `design/` remains active blueprint/target-state authority and does not use a default `design/done/` pattern.
- Added active-scan guidance so current-state work starts from active surfaces and opens `done/` only for history, audit, rollback, provenance, or trace reconstruction.
- Preserved the rule that completed history is not junk and does not authorize deletion.

### Summary
Project-documentation-standards now separates active documentation surfaces from completed history surfaces so large projects can reduce scan bloat without losing governed traceability or weakening file-hygiene/deletion boundaries.

---

<a id="version-230"></a>
## Version 2.30: Clarified source-owned runtime install scope in shared destinations

**Date:** 2026-04-25
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `project-documentation-standards.md` from v2.28/v2.29 drift to v2.30.
- Updated `design/project-documentation-standards.design.md` from v2.28/v2.29 drift to v2.30.
- Clarified that runtime installs target the current project/source-owned active runtime rule files only, not every file in a shared runtime destination.
- Added wording that shared runtime destinations may contain other project/plugin-owned runtime rules that remain out of scope unless their owner/project is explicitly selected or verified.
- Preserved the boundary that design, changelog, TODO, phase, patch, support, helper, and extension-package surfaces are not runtime-rule install targets.

### Summary
Project-documentation-standards now separates source-owned active runtime install scope from shared runtime destination co-location, reducing the chance that other-owner runtime files are treated as current-project managed files.

---

<a id="version-229"></a>
## Version 2.29: Added bounded `/phase` planning-context use at the repository model layer

**Date:** 2026-04-20
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `project-documentation-standards.md` from v2.28 to v2.29.
- Updated `design/project-documentation-standards.design.md` from v2.28 to v2.29.
- Clarified that when `/phase` already contains relevant planning data, the assistant should not ignore current phase, active phase family, phase ordering/dependencies, and already-authored next planned phases during bounded task discovery.
- Clarified that `/phase` may contribute both current execution structure and already-authored next planned structure at the repository model layer.
- Preserved the boundary that unopened future-phase work does not silently become active execution work just because the planning data already exists.

### Summary
Project-documentation-standards now says more clearly that `/phase` should be used as a bounded planning/discovery surface when relevant, while still keeping unopened future work out of active execution.

---

<a id="version-228"></a>
## Version 2.28: Reinforced phase-shaped task creation alignment at the repository model layer

**Date:** 2026-04-18
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `project-documentation-standards.md` from v2.27 to v2.28.
- Updated `design/project-documentation-standards.design.md` from v2.27 to v2.28.
- Added repository-level wording that where the checked repository/workstream already operates through a phased or staged structure, live task-list creation should remain aligned to that phase-shaped execution model.
- Extended cross-document alignment wording so live task creation is less likely to flatten phase-shaped work into detached standalone tasks.

### Summary
Project-documentation-standards now reinforces at the repository-model layer that phased repositories should produce phase-shaped task creation, not just phase-shaped documents.

---

<a id="version-227"></a>
## Version 2.27: Reasserted governed companion surfaces alongside live execution surfaces

**Date:** 2026-04-18
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `project-documentation-standards.md` from v2.26 to v2.27.
- Updated `design/project-documentation-standards.design.md` from v2.26 to v2.27.
- Clarified that required design/changelog/TODO/phase/patch surfaces remain governed companions and must not be downgraded into optional execution aids just because the assistant also has a live task-list surface.
- Extended repository-role wording so live execution surfaces and governed companion surfaces stay distinct but cooperative.
- Added verification coverage for preserving governed companion visibility during active execution.

### Summary
Project-documentation-standards now makes it clearer that live execution surfaces help run the work, but they do not replace required governed companion artifacts.

---

<a id="version-226"></a>
## Version 2.26: Added master-surface consultation before junk/disposal classification

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `project-documentation-standards.md` from v2.25 to v2.26.
- Updated `design/project-documentation-standards.design.md` from v2.25 to v2.26.
- Added a master-surface consultation boundary so newly encountered files must be checked against README/design/changelog/TODO/relevant phase/relevant patch surfaces before they are treated as junk, disposable, or non-governed.
- Clarified that startup artifact posture and `not required` classification do not by themselves authorize removal of an already-present or newly encountered file.

### Summary
Project-documentation-standards now requires master-surface consultation before cleanup/disposal classification, reducing the chance that git-state noise is mistaken for semantic truth.

---

<a id="version-225"></a>
## Version 2.25: Reduced memsearch wording to shared-board defer only

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added explicit repository-level boundary wording so shared-board-specific memsearch handling no longer remains in Main RULES active doctrine.
- Updated integration references to the current touched chain versions after the memsearch ownership split.
- Kept project-documentation-standards focused on repository role boundaries rather than active shared-board memsearch doctrine.

### Summary
Project-documentation-standards now keeps no active memsearch doctrine of its own beyond a shared-board/out-of-scope boundary, and its integration block now matches the touched-chain versions from this ownership split.

---

<a id="version-224"></a>
## Version 2.24: Reduced repository task-list documentation to global role-model guidance

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Reduced `project-documentation-standards.md` so shared-task-list-path naming, lease, handoff, retention, and visible session grammar now defer to `claude-session-coordination` instead of remaining embedded in the repository role model.
- Preserved the repository-level distinction between built-in task list as the live execution surface and `TODO.md` as the durable tracking surface.

### Summary
Project-documentation-standards now keeps only the global repository role model for task tracking, while shared-task-list-path-specific semantics move to the plugin-owned coordination rule source.

---

<a id="version-223"></a>
## Version 2.23: Raised visible session ownership into a default task-list standard

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.22 to v2.23.
- Updated `design/project-documentation-standards.design.md` from v2.22 to v2.23.
- Added explicit repository-level wording that visible session ownership remains a default task-list standard for session-owned work rather than a convention that only applies when several sessions share one task-list path.
- Added explicit wording that request-layer, held-owner, and blocked-owner title forms stay distinct through the central coordination owner.

### Summary
Project-documentation-standards now treats visible session ownership as a general task-list standard at the repository-model layer instead of a multi-session-only convention.

---

<a id="version-222"></a>
## Version 2.22: Resynced coordination-companion integration references after wave 038

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.21 to v2.22.
- Updated `design/project-documentation-standards.design.md` from v2.21 to v2.22.
- Refreshed integration references so `todo-standards` now points to v2.11 and `shared-execution-coordination` now points to v1.2.
- Preserved the existing repository role model and wave-037 semantics while keeping companion references aligned with the current coordination-owner set.

### Summary
Project-documentation-standards now keeps its coordination-companion references aligned with the current shared-board/runtime owner versions after wave 038.

---

<a id="version-221"></a>
## Version 2.21: Separated shared-board request naming from receiving-side execution phase structure

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.20 to v2.21.
- Updated `design/project-documentation-standards.design.md` from v2.20 to v2.21.
- Added explicit repository-level wording that shared-board request-layer naming should remain distinct from receiving-side execution-layer phase structure.
- Preserved the existing repository role model and coordination-owner deferral boundary.

### Summary
Project-documentation-standards now keeps the repository model clearer by separating cross-session request naming from receiving-side execution phase structure.

---

<a id="version-220"></a>
## Version 2.20: Deferred shared-board multi-session coordination semantics to the new coordination owner

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.19 to v2.20.
- Updated `design/project-documentation-standards.design.md` from v2.19 to v2.20.
- Added explicit repository-level wording that shared-board multi-session coordination semantics stay outside Main RULES scope.
- Preserved the existing repository role model and execution-surface boundaries.

### Summary
Project-documentation-standards now keeps the repository execution-surface model while deferring multi-session shared-board coordination protocol details to the new coordination owner.

---

<a id="version-219"></a>
## Version 2.19: Recognized active execution-discovery surfaces at the repository model layer

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.18 to v2.19.
- Updated `design/project-documentation-standards.design.md` from v2.18 to v2.19.
- Added explicit repository-level wording that design, phase, TODO, task-list, and checked implementation state may all act as execution-discovery surfaces once work is already in execution mode.
- Added a quality metric for execution-discovery surface clarity while preserving the broader repository role model.

### Summary
Project-documentation-standards now recognizes the active execution surfaces that can reveal the next unfinished work once execution mode is already underway.

---

<a id="version-218"></a>
## Version 2.18: Added same-objective live task-list continuity at the repository model layer

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.17 to v2.18.
- Updated `design/project-documentation-standards.design.md` from v2.17 to v2.18.
- Added explicit repository-level wording that within the same active objective, the live task-list surface should normally be reused and extended rather than replaced, while durable history still belongs in TODO/phase/changelog surfaces.
- Preserved the broader document-role model and execution-surface deferral to the continuity/goal-review owners.

### Summary
Project-documentation-standards now recognizes same-objective live task-list continuity without blurring the boundary between live execution state and durable history surfaces.

---

<a id="version-217"></a>
## Version 2.17: Added execution-surface deferral to the new continuity and goal-review owners

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `project-documentation-standards.md` from v2.16 to v2.17.
- Updated `design/project-documentation-standards.design.md` from v2.16 to v2.17.
- Added explicit repository-level wording that execution-continuity and goal-review semantics may shape how active work keeps moving and how the full objective set stays visible, while tasks/phases/docs remain execution surfaces rather than the owner of that behavior.
- Preserved the existing repository role model and startup/document-role boundaries.

### Summary
Project-documentation-standards now recognizes the new continuity and goal-review owners without letting execution surfaces masquerade as the owner of those behaviors.

---

<a id="version-216"></a>
## Version 2.16: Clarified live built-in task tracking versus durable TODO tracking

**Date:** 2026-04-10
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.15 to v2.16.
- Updated runtime `project-documentation-standards.md` from v2.15 to v2.16.
- Clarified that Claude Code's built-in task list is the live in-session execution surface for active non-trivial work.
- Clarified that `TODO.md` remains the durable repository/project execution-tracking document and does not replace live task visibility.
- Updated the decision model, checklist, quality metrics, and integration wording so live task tracking is recognized without turning the task list into a governed document artifact.
- Corrected the changelog header so `Current Version` now matches the latest recorded version.

### Summary
Project-documentation-standards now distinguishes live built-in task tracking from durable `TODO.md` tracking, keeping the repository role model clearer during active non-trivial work.

---

<a id="version-215"></a>
## Version 2.15: Kept reusable package-local support assets portable by default

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.14 to v2.15.
- Updated runtime `project-documentation-standards.md` from v2.14 to v2.15.
- Added explicit repository-level wording that package-local support assets such as plugin-owned docs, scripts, optional skills, and optional agents should stay portable by default when they are maintained as reusable source artifacts.
- Extended checklist wording so support/extension package content is not allowed to bake workstation-specific absolute paths into reusable source content by default.

### Summary
Project-documentation-standards now keeps reusable package-local support assets portable by default instead of treating them like a loophole outside the normal shared-artifact portability contract.

---

<a id="version-214"></a>
## Version 2.14: Narrowed repository startup patch posture for greenfield baseline formation

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.13 to v2.14.
- Updated runtime `project-documentation-standards.md` from v2.13 to v2.14.
- Refined the repository role model so patch is explicitly non-default during greenfield / baseline-formation startup when no stable before-state exists yet.
- Updated the required-document wording so patch is described as a separate before/after review artifact for an existing governed surface.
- Narrowed the startup decision model and verification checklist so startup work does not create patch by default unless a real existing review surface or explicit user request justifies it.

### Summary
Refined the repository-level startup model so new-project baseline formation now defaults to design/changelog/TODO/phase posture first, while patch remains conditional on a real existing before/after review surface.

---

<a id="version-213"></a>
## Version 2.13: Added support-layer modeling for the optional RULES plugin extension area

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.12 to v2.13.
- Updated runtime `project-documentation-standards.md` from v2.12 to v2.13.
- Added `plugin/**` as an optional support / extension-package area in the repository model.
- Added explicit wording that package-local plugin assets may use `README.md`, `.claude-plugin/`, `hooks/`, `scripts/`, and optional `skills/` or `agents/` without creating a second governance stack.
- Extended checklist and authority wording so support/extension-package artifacts remain clearly subordinate to the root governance surfaces.

### Summary
Extended the repository role model so the RULES plugin companion can exist as a clean support / extension package without weakening the rules-first authority system.

---

## Version 2.12: Added portable public onboarding/install guidance

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.11 to v2.12.
- Updated runtime `project-documentation-standards.md` from v2.11 to v2.12.
- Added a first-class public onboarding/install guidance section to the repository role model.
- Added explicit requirements so public README/install docs:
  - default to repo-root-relative or other portable source guidance when possible
  - avoid workstation-specific absolute paths and internal umbrella workspace roots as public defaults
  - distinguish source-side guidance from destination/runtime notation
  - scope exact local absolute paths as local examples or machine-scoped contracts when they appear
- Added verification and quality-metric coverage for portable onboarding/install guidance.
- Added explicit integration to `document-consistency.md` for source-vs-destination notation clarity.

### Summary
Strengthened the repository documentation model so public onboarding/install docs are now governed as portable documentation surfaces rather than being left to ad hoc README wording.

---

<a id="version-211"></a>
## Version 2.11: Integrated portable-default documentation guidance

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `project-documentation-standards.md` from v2.10 to v2.11.
- Updated `design/project-documentation-standards.design.md` from v2.10 to v2.11.
- Added cross-document guidance that shared governed docs/templates should remain portable by default rather than embedding machine-specific environment assumptions.
- Added explicit integration to `portable-implementation-and-hardcoding-control.md`.

### Summary
Extended project-documentation-standards so shared governed docs and templates stay portable by default while broader anti-hardcoding ownership is delegated to the new first-class chain.

---

<a id="version-210"></a>
## Version 2.10: Added explicit phase-to-patch linkage verification for phased work

**Date:** 2026-03-30
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.9 to v2.10.
- Updated runtime `project-documentation-standards.md` from v2.9 to v2.10.
- Added an explicit cross-document alignment rule that phased work with governed patch artifacts must show patch linkage from `phase/SUMMARY.md` and relevant child phase files.
- Added the same requirement to the repository verification checklist.
- Added an explicit quality metric for phase-to-patch linkage coverage when patch is in scope.
- Preserved the existing separation between phase as the live execution workspace and patch as the governed before/after artifact layer.

### Summary
Refined the repository document-role model so phased work with governed patch artifacts must now show explicit patch linkage in the live phase workspace rather than leaving patch participation implicit.

---

<a id="version-29"></a>
## Version 2.9: Added startup artifact gate and routed repository startup behavior to artifact-initiation-control

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.8 to v2.9.
- Updated runtime `project-documentation-standards.md` from v2.8 to v2.9.
- Added `artifact-initiation-control.md` as the first-class startup-governance owner in the repository role model.
- Added a startup artifact gate so meaningful governed work now resolves design/changelog/TODO/phase/patch posture before drift.
- Clarified that startup artifact establishment is separate from the later UDVC-1 synchronization order.
- Updated the decision model, verification checklist, quality metrics, and integration references to the startup-governance model.

### Summary
Refined the repository document-role model so startup artifact posture is now an explicit governed decision rather than an implicit late-stage backfill behavior.

---

<a id="version-28"></a>
## Version 2.8: Changed active patch placement to `patch/` or root and aligned repository role wording

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.7 to v2.8.
- Updated runtime `project-documentation-standards.md` from v2.7 to v2.8.
- Replaced the active shared patch location from `patches/` to `patch/`.
- Added explicit repository-wide allowance for root `<context>.patch.md`.
- Removed lingering directory-as-namespace `patch.md` teaching from the active role model.
- Clarified that a patch is a self-identifying before/after artifact rather than a prose-only recap.
- Updated the required document set, boundary wording, decision model, checklist, and integration references to the corrected patch model.

### Summary
Completed the repository-level patch-role correction so active docs now teach one clear patch model: self-identifying before/after patch artifacts in `patch/` or at repository root.
