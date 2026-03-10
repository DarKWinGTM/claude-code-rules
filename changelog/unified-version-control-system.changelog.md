# Changelog - Unified Version-Control System

> **Parent Document:** [../unified-version-control-system.md](../unified-version-control-system.md)
> **Current Version:** 1.2
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-03-08 | **[Extended UDVC-1 controller to enforce runtime-header and support-boundary cleanup](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Updated the controller chain so one active model now covers runtime header normalization, active-state design bodies, and governed/support boundary enforcement | |
| 1.1 | 2026-02-24 | **[Activated runtime unified controller and completed governance-reference alignment](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Materialized runtime `unified-version-control-system.md`, aligned master design/TODO activation state, and completed triad synchronization closure | |
| 1.0 | 2026-02-24 | **[Initial unified controller design created](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added design specification for a single controller rule that centralizes UDVC-1 governance across design/changelog/TODO/patch workflows | |

---

<a id="version-12"></a>
## Version 1.2: Extended UDVC-1 controller to enforce runtime-header and support-boundary cleanup

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `design/unified-version-control-system.design.md` from v1.1 to v1.2.
- Updated runtime `unified-version-control-system.md` from v1.1 to v1.2.
- Added explicit controller-level enforcement for the canonical root runtime header contract:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Retired `Based on:` as an allowed active root runtime header label at the controller level.
- Added explicit repository role-boundary language for README, TODO, and support artifacts.
- Clarified that active design docs hold current guidance while historical detail lives in changelog files.

### Summary
Expanded the controller so the repository now teaches one active governance model across headers, active-state design bodies, and governed/support boundaries.

---

<a id="version-11"></a>
## Version 1.1: Activated runtime unified controller and completed governance-reference alignment

**Date:** 2026-02-24
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created runtime `unified-version-control-system.md` (v1.1) aligned to `design/unified-version-control-system.design.md` v1.1.
- Updated master design (`design/design.md`) activation state:
  - Converted Sub-Rule Index entry from pending activation to active.
  - Updated rule purpose entry to v1.1 reference.
  - Removed activation-queue wording tied to pending runtime materialization.
- Updated `TODO.md`:
  - Marked runtime materialization/alignment task as completed.
  - Added history row recording runtime activation closure.
- Completed rule/design/changelog/TODO synchronization cycle for this rollout.

### Summary
Runtime unified-controller activation is now complete and governance references are aligned to active state under one deterministic UDVC-1 mechanism.

---

<a id="version-10"></a>
## Version 1.0: Initial unified controller design created

**Date:** 2026-02-24
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/unified-version-control-system.design.md`.
- Defined single-mechanism governance statement (UDVC-1 only).
- Defined chain authority, metadata, anchor, and synchronization-order contracts.
- Defined rollout split between design-first creation and pending runtime materialization.

### Summary
Established the design/changelog baseline for a unified version-control controller rule without introducing a competing governance mechanism.
