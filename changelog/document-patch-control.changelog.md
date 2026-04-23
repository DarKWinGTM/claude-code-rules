# Changelog - Document Patch Control

> **Parent Document:** [../document-patch-control.md](../document-patch-control.md)
> **Current Version:** 2.6
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.6 | 2026-04-23 | **[Added external-requirement basis visibility for patch review](#version-26)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.5 | 2026-04-08 | **[Narrowed patch semantics so startup baseline formation no longer implies patch by default](#version-25)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Clarified that patch normally assumes an existing before-state and is not the default governing artifact for greenfield / baseline-formation startup unless a real review surface or explicit user request exists | |
| 2.2 | 2026-03-15 | **[Added path-aware patch naming guidance for filename-authoritative versus path-authoritative workspaces](#version-22)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Refined patch-control so `<context>.patch.md` remains valid when filenames must carry context, while `patch.md` is also valid when the parent workspace path already provides the stable namespace | |
| 2.1 | 2026-03-13 | **[Clarified one-way patch-to-phase synthesis without creating reverse-link requirements](#version-21)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Preserved patch governance and `/patches` separation while explicitly allowing `phase-implementation` to consume relevant patch inputs one-way without requiring patch documents to point back to phase | |
| 2.0 | 2026-03-12 | **[Required comparison-friendly change representation for governed patch documents](#version-20)** | 451fb64e-f2a5-43a5-bf98-47f01244f15c |
| | | Summary: Strengthened patch-control so `.patch.md` documents must show target locations and current-vs-proposed change representation clearly enough for review, while preserving the `/phase` boundary | |
| 1.9 | 2026-03-11 | **[Removed `/patches` from the live phase-plan model and clarified patch governance as separate from `/phase`](#version-19)** | 92fed037-8ba9-48a6-95c4-e1085f28bb32 |
| | | Summary: Redefined `/patches` as a separate patch/review artifact layer, moved live phased execution fully into `/phase`, and made patch-versus-phase namespace separation explicit | |
| 1.8 | 2026-03-11 | **[Changed patch governance to parent patch/index plus mandatory child phase files for multi-phase work](#version-18)** | 92fed037-8ba9-48a6-95c4-e1085f28bb32 |
| | | Summary: Kept one parent patch/index as the governed entry point, required child phase files under `.phases/` for multi-phase work, and prohibited collapsing all live phase detail back into the parent patch body | |
| 1.7 | 2026-03-10 | **[Added role-specific patch-governance checklist and clarified checklist boundary versus phase-implementation](#version-17)** | 468e053d-9953-496e-8e83-910e2ae67402 |
| | | Summary: Added a dedicated patch-governance checklist for governed review/change artifacts, clarified that patch-control validates patch quality rather than phase-planning quality, and made the checklist boundary versus `phase-implementation` explicit | |
| 1.6 | 2026-03-10 | **[Refocused patch control on governance while moving phase semantics to the new rule chain](#version-16)** | 468e053d-9953-496e-8e83-910e2ae67402 |
| | | Summary: Kept patch docs as the live governed execution-plan artifacts, redirected semantic phase behavior to `phase-implementation.md`, and clarified the helper-only role of the root template | |
| 1.5 | 2026-03-10 | **[Moved flexible phase template to RULES root and corrected placement contract](#version-15)** | b1fc974f-b7df-4f24-9080-c941153612ca |
| | | Summary: Corrected the reusable phase template placement to the RULES root, updated patch-governance references, and kept the template non-governed | |
| 1.4 | 2026-03-10 | **[Extended patch governance to support flexible phased execution planning](#version-14)** | b1fc974f-b7df-4f24-9080-c941153612ca |
| | | Summary: Kept patch docs as the governed transition-plan layer, added flexible project-defined phase planning rules, and introduced a then-historical non-governed support-template boundary later corrected to the root helper model | |
| 1.3 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-13)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Replaced legacy `Based on` runtime metadata with canonical `Design + Session + Full history` header structure and aligned the chain version state | |
| 1.2 | 2026-02-23 | **[Synchronized patch-control runtime contract to UDVC-1 metadata baseline](#version-12)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Aligned runtime/design/changelog to v1.2 with mandatory patch metadata and deterministic synchronization contract | |
| 1.1 | 2026-02-22 | **[Synchronized patch-control references to active runtime standards](#version-11)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Closed patch-reference/version drift across runtime/design/changelog artifacts | |
| 1.0 | 2026-02-01 | **[Initial design](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Initial release of patch-control standards | |

---

<a id="version-26"></a>
## Version 2.6: Added external-requirement basis visibility for patch review

**Date:** 2026-04-23
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated runtime `document-patch-control.md` from v2.5 to v2.6.
- Updated `design/document-patch-control.design.md` from v2.5 to v2.6.
- Added an explicit external-requirement basis rule so patch context/analysis can show the implementation-relevant basis when a change is materially constrained by docs/specs/provider references.
- Clarified that patch should point to normalized design truth when design already owns the extracted external requirement.
- Preserved the boundary that patch does not replace design as the target-state truth layer.

### Summary
Document-patch-control now makes it easier for later review to understand which external requirement materially drove a change, without turning patch into a duplicate design layer.

---

<a id="version-25"></a>
## Version 2.5: Narrowed patch semantics so startup baseline formation no longer implies patch by default

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/document-patch-control.design.md` from v2.4 to v2.5.
- Updated runtime `document-patch-control.md` from v2.4 to v2.5.
- Added an explicit semantic boundary that patch is not the default startup artifact for greenfield / baseline-formation work when no stable before-state exists yet.
- Clarified that patch normally assumes an identifiable current/before surface.
- Preserved the existing before/after patch definition, change-representation requirements, and `/phase` separation while making startup posture more precise.

### Summary
Refined patch semantics so greenfield startup is no longer quietly treated like a patchable delta, while real before/after review artifacts remain fully supported.

---

<a id="version-22"></a>
## Version 2.2: Added path-aware patch naming guidance for filename-authoritative versus path-authoritative workspaces

**Date:** 2026-03-15
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `design/document-patch-control.design.md` from v2.1 to v2.2.
- Updated runtime `document-patch-control.md` from v2.1 to v2.2.
- Refined patch naming so the chain now distinguishes between filename-authoritative naming and path-authoritative naming.
- Preserved `<context>.patch.md` when the filename must carry the stable identifying context.
- Added explicit allowance for `patch.md` when the parent workspace path already acts as the stable namespace and only one same-role patch artifact exists in the directory.
- Added an anti-redundancy rule against repeating the same context in both path and filename without a real portability, review, or search benefit.
- Expanded checklist and quality-metric coverage for naming-mode clarity.

### Summary
Refined `document-patch-control` so patch naming now supports both context-bearing filenames and path-authoritative `patch.md` naming, while discouraging redundant path-plus-filename repetition.

---

<a id="version-21"></a>
## Version 2.1: Clarified one-way patch-to-phase synthesis without creating reverse-link requirements

**Date:** 2026-03-13
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `design/document-patch-control.design.md` from v2.0 to v2.1.
- Updated runtime `document-patch-control.md` from v2.0 to v2.1.
- Preserved patch metadata, change-representation, and patch-versus-phase namespace requirements.
- Added an explicit one-way synthesis clarification so `phase-implementation.md` may consume relevant governed patch inputs inside live phased execution planning.
- Clarified that this does not create a reverse-link requirement from patch documents back to phase.
- Preserved the rule that `/patches` remains outside the live `/phase` workspace even when patch inputs are synthesized into the live phase plan.

### Summary
Clarified that patch artifacts may feed phased execution planning one-way without weakening patch governance or turning patch documents into the live phase workspace.

---

<a id="version-20"></a>
## Version 2.0: Required comparison-friendly change representation for governed patch documents

**Date:** 2026-03-12
**Session:** 451fb64e-f2a5-43a5-bf98-47f01244f15c

### Changes
- Updated `design/document-patch-control.design.md` from v1.9 to v2.0.
- Updated runtime `document-patch-control.md` from v1.9 to v2.0.
- Added an explicit change-representation requirement so governed `.patch.md` files must show the intended change concretely enough for review instead of relying on prose-only plan descriptions.
- Required patches that concern code, configuration, commands, queries, schemas, or structured text to show:
  - target artifact or stable target location
  - current state
  - proposed state
  - enough comparison detail for reviewer evaluation
- Added preferred comparison forms including before/after snippets, current/target tables, unified diff style blocks, patch hunk sections, and clearly scoped replacement blocks.
- Added a target-location requirement for each concrete patch item.
- Added a non-code patch allowance so governance-only or conceptual patches may omit code snippets only if they explicitly declare themselves non-code/conceptual and still provide structured current-state vs target-state comparison.
- Expanded the patch checklist and quality metrics to validate change-representation clarity and target-location clarity.

### Summary
Strengthened `document-patch-control` so governed `.patch.md` files must now present the actual intended change surface in a comparison-friendly way rather than remaining vague prose-only review artifacts.

---

<a id="version-19"></a>
## Version 1.9: Removed `/patches` from the live phase-plan model and clarified patch governance as separate from `/phase`

**Date:** 2026-03-11
**Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32

### Changes
- Updated `design/document-patch-control.design.md` from v1.8 to v1.9.
- Updated runtime `document-patch-control.md` from v1.8 to v1.9.
- Reframed `/patches` as a governed patch/review artifact layer rather than the live phase-plan namespace.
- Explicitly moved live phased execution planning into `/phase`.
- Clarified that the live phase workspace now uses:
  - `phase/SUMMARY.md`
  - `phase/phase-010-<phase-name>.md` and peer files
- Prohibited using patch files as the active phase summary/index or per-phase execution files.
- Updated the checklist, integration contract, and quality metrics to validate patch-versus-phase namespace separation.

### Summary
Updated `document-patch-control` so `/patches` is now clearly separate from live phased execution, which must live under `/phase` with `SUMMARY.md` and child phase files.

---

<a id="version-18"></a>
## Version 1.8: Changed patch governance to parent patch/index plus mandatory child phase files for multi-phase work

**Date:** 2026-03-11
**Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32

### Changes
- Updated `design/document-patch-control.design.md` from v1.7 to v1.8.
- Updated runtime `document-patch-control.md` from v1.7 to v1.8.
- Reframed patch governance around:
  - one parent patch/index file as the governed execution entry point
  - one child phase file per live phase for multi-phase work
- Added the canonical child phase-file path model under `patches/<context>.phases/`.
- Defined the parent-versus-child ownership split so:
  - the parent patch/index owns global control, phase index, cross-phase coordination, end-to-end verification, and overall rollback
  - child phase files own phase-local checklist detail, design traceability, verification, exit criteria, and rollback notes
- Added child phase-file metadata expectations (`Parent Patch`, `Phase ID`, `Status`, `Session`).
- Explicitly prohibited collapsing all live multi-phase detail back into one parent patch execution body.
- Updated the governance checklist and quality metrics to validate parent/child topology for multi-phase work.

### Summary
Updated `document-patch-control` so multi-phase work now uses a parent patch/index plus child phase files, preserving one governing entry point while preventing oversized one-file execution plans.

---

<a id="version-17"></a>
## Version 1.7: Added role-specific patch-governance checklist and clarified checklist boundary versus phase-implementation

**Date:** 2026-03-10
**Session:** 468e053d-9953-496e-8e83-910e2ae67402

### Changes
- Updated `design/document-patch-control.design.md` from v1.6 to v1.7.
- Updated runtime `document-patch-control.md` from v1.6 to v1.7.
- Added an explicit checklist-boundary contract so `document-patch-control` validates governed patch quality rather than phased execution-plan quality.
- Added a role-specific patch governance checklist covering:
  - identity and metadata
  - patch authority integrity
  - structure and reviewability
  - synchronization behavior
- Clarified that phase-sequencing quality, per-phase planning quality, and per-phase execution detail remain inside `phase-implementation` when phases are used.
- Added boundary wording to reduce overlap between patch checklist concerns and phase checklist concerns.

### Summary
Strengthened `document-patch-control` with its own role-specific checklist while making its governance boundary versus `phase-implementation` explicit.

---

<a id="version-16"></a>
## Version 1.6: Refocused patch control on governance while moving phase semantics to the new rule chain

**Date:** 2026-03-10
**Session:** 468e053d-9953-496e-8e83-910e2ae67402

### Changes
- Updated `design/document-patch-control.design.md` from v1.5 to v1.6.
- Updated runtime `document-patch-control.md` from v1.5 to v1.6.
- Clarified that patch documents remain the live governed execution-plan artifacts.
- Clarified that `phase-implementation.md` now owns semantic phase behavior, including:
  - when phased planning should be used
  - flexible phase ordering
  - stable per-phase fields
  - design traceability
  - TODO and changelog coordination inside the phase plan
  - cross-phase handoffs
  - verification and rollback expectations
- Reduced semantic duplication in patch-control so this chain stays focused on metadata, lifecycle, and synchronization behavior.
- Preserved the root-level `phase-implementation-template.md` as a non-governed helper only.

### Summary
Refocused patch control on governed patch lifecycle and metadata while delegating phase semantics to the new `phase-implementation` rule chain.

---

<a id="version-15"></a>
## Version 1.5: Moved flexible phase template to RULES root and corrected placement contract

**Date:** 2026-03-10
**Session:** b1fc974f-b7df-4f24-9080-c941153612ca

### Changes
- Updated `design/document-patch-control.design.md` from v1.4 to v1.5.
- Updated runtime `document-patch-control.md` from v1.4 to v1.5.
- Corrected the canonical template location from `support/phase-implementation-template.md` to root-level `phase-implementation-template.md`.
- Clarified that the template stays non-governed while being colocated with the active RULES files for discoverability.
- Updated related integration links and wording to the root-level template path.

### Summary
Corrected the reusable phase-template placement so it now sits at the RULES root while preserving the existing patch-governance model and non-governed status.

---

<a id="version-14"></a>
## Version 1.4: Extended patch governance to support flexible phased execution planning

**Date:** 2026-03-10
**Session:** b1fc974f-b7df-4f24-9080-c941153612ca

### Changes
- Updated `design/document-patch-control.design.md` from v1.3 to v1.4.
- Updated runtime `document-patch-control.md` from v1.3 to v1.4.
- Clarified that patch docs remain the governed transition-plan layer under UDVC-1.
- Added a flexible phase-planning contract so phased execution can be:
  - merged
  - split
  - skipped
  - repeated
  - reordered
- Clarified that common phase patterns are examples only, not a fixed repository-wide sequence.
- Added stable phase-block field expectations for objective, prerequisites, in-scope actions, affected artifacts, verification, exit criteria, and rollback-risk notes.
- Added cross-phase dependency and handoff guidance.
- Added integration language for a non-governed support template at the then-active historical path `support/phase-implementation-template.md`, which was later corrected to the root helper location.

### Summary
Expanded patch governance so projects can plan implementation in clear phases without inventing a second planning system or forcing a rigid global phase order.

---

<a id="version-13"></a>
## Version 1.3: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `document-patch-control.md` from v1.2 to v1.3.
- Updated `design/document-patch-control.design.md` from v1.2 to v1.3.
- Replaced runtime `Based on:` metadata with canonical `Design:` metadata.
- Preserved required canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing document-patch-control behavioral contract.

### Summary
Normalized the document-patch-control chain to the canonical cleanup-wave runtime header format while preserving substantive rule behavior.

---

<a id="version-12"></a>
## Version 1.2: Synchronized patch-control runtime contract to UDVC-1 metadata baseline

**Date:** 2026-02-23
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated runtime `document-patch-control.md` from v1.1 to v1.2.
- Aligned runtime `Design` reference to `design/document-patch-control.design.md` v1.2.
- Added explicit mandatory patch metadata contract in runtime rule text.
- Added explicit patch-changelog metadata requirements in runtime rule text.
- Added session-integrity and version-alignment constraints for patch documents.
- Added deterministic synchronization order including patch metadata final sync when affected.

### Summary
Aligned patch governance runtime/design/changelog artifacts to UDVC-1 metadata and synchronization contract.

---

<a id="version-11"></a>
## Version 1.1: Synchronized patch-control references to active runtime standards

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated runtime/design pair to v1.1.
- Updated related reference baseline to `document-design-control.md` v1.6.

### Summary
Closed patch-reference/version drift for runtime/design/changelog artifacts.

---

<a id="version-10"></a>
## Version 1.0: Initial design

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Defined patch document standards and `.patch.md` naming.
- Established required structure and lifecycle model.
- Defined integration behavior with design/changelog/TODO.

### Summary
Initial release of patch-control standards.
