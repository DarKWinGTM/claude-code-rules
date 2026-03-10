# Changelog - Project Documentation Standards

> **Parent Document:** [../project-documentation-standards.md](../project-documentation-standards.md)
> **Current Version:** 2.1
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.1 | 2026-03-10 | **[Added first-class phase-rule role and clarified helper-versus-patch authority model](#version-21)** | 468e053d-9953-496e-8e83-910e2ae67402 |
| | | Summary: Added `phase-implementation.md` as the semantic phase-planning rule, kept patches as the governed plan instances, and clarified how TODO and changelog remain companion layers rather than phase authorities | |
| 2.0 | 2026-03-10 | **[Corrected root-level helper placement for phase implementation template](#version-20)** | b1fc974f-b7df-4f24-9080-c941153612ca |
| | | Summary: Moved the reusable phase template to the RULES root, updated repository role wording, and preserved the non-governed helper boundary | |
| 1.9 | 2026-03-10 | **[Clarified patch-vs-support boundary for flexible phased execution planning](#version-19)** | b1fc974f-b7df-4f24-9080-c941153612ca |
| | | Summary: Defined patch docs as the live governed phase-plan artifact, used a then-historical support-template authoring model, and preserved UDVC-1 authority boundaries before later correction to the root helper path | |
| 1.8 | 2026-03-08 | **[Clarified overview/runtime/history/support boundaries for anti-poisoning cleanup](#version-18)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Updated the chain to define explicit role boundaries for README, runtime rules, design docs, changelogs, TODO, and support artifacts | |
| 1.7 | 2026-02-23 | **[Synchronized project-documentation runtime contract to UDVC-1 baseline](#version-17)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Aligned runtime/design/changelog references to v1.7 and updated governance contract language to deterministic UDVC-1 model | |
| 1.6 | 2026-02-22 | **[Synchronized references to active runtime baselines](#version-16)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Closed WS-4 reference drift for project-documentation standards artifacts | |
| 1.5 | 2026-02-22 | **[Synchronized rule/design and normalized policy references](#version-15)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Closed version/reference/language drift for this chain | |
| 1.4 | 2026-02-21 | **[Synced design reference and TODO authority](#version-14)** | f19e8a67-d3c2-4f24-9080-c941153612ca |
| | | Summary: Synchronized design/TODO governance references | |
| 1.3 | 2026-02-01 | **[Added version-authority rules](#version-13)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Added strict changelog-authority synchronization policy | |
| 1.2 | 2026-02-01 | **[Added patches-directory support](#version-12)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Added `patches/` support for complex projects | |
| 1.1 | 2026-02-01 | **[Added patch-control integration](#version-11)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Integrated patch governance into document standards | |
| 1.0 | 2026-01-21 | **[Initial version](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Initial release of project documentation standards | |

---

<a id="version-21"></a>
## Version 2.1: Added first-class phase-rule role and clarified helper-versus-patch authority model

**Date:** 2026-03-10
**Session:** 468e053d-9953-496e-8e83-910e2ae67402

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.0 to v2.1.
- Updated runtime `project-documentation-standards.md` from v2.0 to v2.1.
- Added `phase-implementation.md` to the required-document model as the semantic rule for phased execution planning.
- Clarified the repository role split so:
  - `phase-implementation.md` is the semantic rule
  - `patches/*.patch.md` is the live governed plan instance
  - `phase-implementation-template.md` is the readable root-level helper
  - `TODO.md` and changelog remain companion layers rather than plan authorities
- Clarified that phase plans should explicitly show how TODO execution work and changelog impact relate to the active phases when that coordination matters.
- Updated decision-model, checklist, and integration references to match the new rule chain.

### Summary
Updated the repository role model so phased planning now has a first-class rule authority, while patches remain the governed execution artifacts and the root template stays a readable non-governed helper.

---

<a id="version-20"></a>
## Version 2.0: Corrected root-level helper placement for phase implementation template

**Date:** 2026-03-10
**Session:** b1fc974f-b7df-4f24-9080-c941153612ca

### Changes
- Updated `design/project-documentation-standards.design.md` from v1.9 to v2.0.
- Updated runtime `project-documentation-standards.md` from v1.9 to v2.0.
- Corrected the canonical reusable phase-template location from `support/phase-implementation-template.md` to root-level `phase-implementation-template.md`.
- Added explicit repository-role wording for root-level helper artifacts colocated with the active RULES files.
- Preserved the non-governed helper boundary for the phase template.
- Updated references, checklists, and decision-flow wording to the root-level path.

### Summary
Corrected the repository model so the reusable phase template now lives at the RULES root, matching operator expectation while preserving the existing governed-vs-non-governed authority split.

---

<a id="version-19"></a>
## Version 1.9: Clarified patch-vs-support boundary for flexible phased execution planning

**Date:** 2026-03-10
**Session:** b1fc974f-b7df-4f24-9080-c941153612ca

### Changes
- Updated `design/project-documentation-standards.design.md` from v1.8 to v1.9.
- Updated runtime `project-documentation-standards.md` from v1.8 to v1.9.
- Added an explicit patch role so `patches/*.patch.md` is the governed transition-plan layer for live phased execution planning.
- Clarified that reusable authoring templates, at that historical point, belonged in `support/` and remained non-governed artifacts.
- Added a flexible phase-planning boundary so support templates do not become a competing governance system.
- Clarified that TODO and changelog keep their original roles and do not become the primary place for defining project phases.
- Added support-template examples referencing the then-active historical path `support/phase-implementation-template.md`, later corrected to the root helper path.

### Summary
Updated the repository role model so phased implementation planning can be reusable and flexible while still staying inside the existing patch and UDVC-1 governance system.

---

<a id="version-18"></a>
## Version 1.8: Clarified overview/runtime/history/support boundaries for anti-poisoning cleanup

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `design/project-documentation-standards.design.md` from v1.7 to v1.8.
- Updated runtime `project-documentation-standards.md` from v1.7 to v1.8.
- Defined explicit role boundaries for:
  - `README.md` as overview-only
  - root runtime rules as the active runtime layer
  - `design/*.design.md` as active target-state guidance
  - `changelog/*.changelog.md` as chain authority
  - `TODO.md` as execution-only
  - support/reference artifacts as non-governed support materials
- Added support-artifact boundary guidance so prompt/reference files do not remain in ambiguous governed design space.
- Preserved UDVC-1 synchronization-order requirements under the clarified repository role model.

### Summary
Updated the chain to make repository roles explicit, reducing governance ambiguity and accidental poisoning from mixed artifact semantics.

---

<a id="version-17"></a>
## Version 1.7: Synchronized project-documentation runtime contract to UDVC-1 baseline

**Date:** 2026-02-23
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated runtime `project-documentation-standards.md` from v1.6 to v1.7.
- Aligned runtime `Design` reference to `design/project-documentation-standards.design.md` v1.7.
- Updated runtime required-document table to deterministic UDVC-1 terminology.
- Updated runtime governance section to explicit synchronization order (`design → runtime rule → changelog → TODO`).
- Updated runtime integration references to active versions:
  - `document-changelog-control.md` v4.6
  - `document-design-control.md` v1.7
  - `todo-standards.md` v2.1
  - `document-patch-control.md` v1.2

### Summary
Aligned project-documentation runtime/design/changelog artifacts to UDVC-1 baseline and active governance version references.

---

<a id="version-16"></a>
## Version 1.6: Synchronized references to active runtime baselines

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated references to `document-changelog-control.md` v4.5 and `document-patch-control.md` v1.1.

### Summary
Closed WS-4 reference drift.

---

<a id="version-15"></a>
## Version 1.5: Synchronized rule/design and normalized policy references

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated rule/design pair to v1.5 and normalized cross-reference wording.

### Summary
Closed v1.5 reference and language drift.

---

<a id="version-14"></a>
## Version 1.4: Synced design reference and TODO authority

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4f24-9080-c941153612ca

### Changes
- Updated design reference to v1.4 and confirmed TODO authority mapping.

### Summary
Maintained design/TODO synchronization record.

---

<a id="version-13"></a>
## Version 1.3: Added version-authority rules

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added strict changelog-authority and synchronization rule language.

### Summary
Defined version authority behavior.

---

<a id="version-12"></a>
## Version 1.2: Added patches-directory support

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added `patches/` support in templates and checklist.

### Summary
Enabled patch-document directory support for complex projects.

---

<a id="version-11"></a>
## Version 1.1: Added patch-control integration

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added patch governance integration into required documents and rule mapping.

### Summary
Integrated patch-control standard into project-documentation policy.

---

<a id="version-10"></a>
## Version 1.0: Initial version

**Date:** 2026-01-21
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Created initial project-documentation standards chain.

### Summary
Initial release of project documentation standards.
