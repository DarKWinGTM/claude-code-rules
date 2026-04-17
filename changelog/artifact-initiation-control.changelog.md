# Changelog - Artifact Initiation Control

> **Parent Document:** [../artifact-initiation-control.md](../artifact-initiation-control.md)
> **Current Version:** 1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.5 | 2026-04-17 | **[Kept newly encountered file classification separate from disposal conclusions](#version-15)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 1.4 | 2026-04-12 | **[Kept initialized live task lists as the active objective surface](#version-14)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.3 | 2026-04-11 | **[Made phase-backed live task-list startup expected](#version-13)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.2 | 2026-04-10 | **[Added early live task-tracking posture for non-trivial work](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.1 | 2026-04-08 | **[Narrowed startup patch posture for greenfield baseline formation](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Refined startup-governance so patch is no longer treated as the default startup artifact during greenfield / baseline-formation work unless a real existing before/after review surface or explicit user request justifies it | |
| 1.0 | 2026-03-28 | **[Created first-class artifact-initiation-control rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new startup-governance owner chain so design, changelog, TODO, phase, and patch posture must be resolved before meaningful governed work drifts | |

---

<a id="version-15"></a>
## Version 1.5: Kept newly encountered file classification separate from disposal conclusions

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `artifact-initiation-control.md` from v1.4 to v1.5.
- Updated `design/artifact-initiation-control.design.md` from v1.4 to v1.5.
- Extended existing-authority and startup-resolution guidance so newly encountered unclear files must be checked against governed surfaces before they are treated as unnecessary.
- Clarified that `not required` does not by itself mean `safe to remove` for an already-present or newly encountered file.
- Added anti-pattern coverage against collapsing unresolved classification into cleanup/disposal logic.

### Summary
Artifact-initiation-control now keeps startup classification separate from disposal conclusions, reducing the chance that unresolved new files are overread as safe cleanup targets.

---

<a id="version-14"></a>
## Version 1.4: Kept initialized live task lists as the active objective surface

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `artifact-initiation-control.md` from v1.3 to v1.4.
- Updated `design/artifact-initiation-control.design.md` from v1.3 to v1.4.
- Added explicit guidance that once the live task list is initialized for the active objective, it should normally be reused rather than recreated unless a true objective-boundary reset or explicit user reset applies.
- Preserved the startup artifact-resolution order and existing task-list initialization triggers.

### Summary
Artifact-initiation-control now treats the initialized live task list as the continuing surface for the active objective instead of leaving continuity implicit.

---

<a id="version-13"></a>
## Version 1.3: Made phase-backed live task-list startup expected

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/artifact-initiation-control.design.md` from v1.2 to v1.3.
- Updated runtime `artifact-initiation-control.md` from v1.2 to v1.3.
- Strengthened startup posture so when an active phase already exists for non-trivial work, live task-list initialization is treated as expected rather than optional.
- Extended the artifact matrix and startup contract so phase-backed live task tracking is less likely to be silently skipped.
- Added quality/anti-pattern coverage against phase-backed work beginning with no visible task tracking.

### Summary
Artifact-initiation-control now treats phase-backed live task tracking as expected startup behavior for non-trivial work instead of leaving it merely implicit.

---

<a id="version-12"></a>
## Version 1.2: Added early live task-tracking posture for non-trivial work

**Date:** 2026-04-10
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/artifact-initiation-control.design.md` from v1.1 to v1.2.
- Updated runtime `artifact-initiation-control.md` from v1.1 to v1.2.
- Extended startup-governance so non-trivial tracked work now resolves early live task-list posture instead of leaving execution visibility implicit.
- Added a live task-list row to the startup artifact requirement matrix.
- Extended the startup communication contract so live task-list initialization can be made explicit alongside normal artifact posture.
- Added an anti-pattern against non-trivial tracked work beginning with no live task tracking.

### Summary
Artifact-initiation-control now treats early live task-list tracking as part of startup posture when non-trivial work needs visible execution state.

---

<a id="version-11"></a>
## Version 1.1: Narrowed startup patch posture for greenfield baseline formation

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/artifact-initiation-control.design.md` from v1.0 to v1.1.
- Updated runtime `artifact-initiation-control.md` from v1.0 to v1.1.
- Narrowed the startup trigger language so patch is no longer implied by default for greenfield / baseline-formation work.
- Updated the artifact requirement matrix so patch now defaults to `not required` during greenfield startup unless a real existing before/after review surface or explicit user request justifies it.
- Added an explicit anti-pattern against creating patch by default during startup when no stable before-state exists.

### Summary
Refined startup-governance so patch remains available for real reviewable deltas, but is no longer treated as the default startup artifact for new-project baseline formation.

---

<a id="version-10"></a>
## Version 1.0: Created first-class artifact-initiation-control rule chain

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/artifact-initiation-control.design.md` as the target-state startup-governance design.
- Created runtime `artifact-initiation-control.md` as a first-class rule owning startup artifact posture resolution.
- Defined the meaningful-work boundary, artifact-resolution states, artifact requirement matrix, startup-resolution order, and startup communication contract.
- Positioned the chain as a narrow startup owner that integrates with project-documentation, phase, TODO, patch, and hygiene rules without replacing their semantic ownership.

### Summary
Created a first-class `artifact-initiation-control` rule chain so governed artifact posture is resolved before meaningful work drifts rather than being backfilled later.
