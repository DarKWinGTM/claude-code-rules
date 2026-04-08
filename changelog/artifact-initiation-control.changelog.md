# Changelog - Artifact Initiation Control

> **Parent Document:** [../artifact-initiation-control.md](../artifact-initiation-control.md)
> **Current Version:** 1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-04-08 | **[Narrowed startup patch posture for greenfield baseline formation](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Refined startup-governance so patch is no longer treated as the default startup artifact during greenfield / baseline-formation work unless a real existing before/after review surface or explicit user request justifies it | |
| 1.0 | 2026-03-28 | **[Created first-class artifact-initiation-control rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new startup-governance owner chain so design, changelog, TODO, phase, and patch posture must be resolved before meaningful governed work drifts | |

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
