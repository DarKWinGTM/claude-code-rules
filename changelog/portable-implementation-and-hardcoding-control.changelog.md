# Changelog - Portable Implementation and Hardcoding Control

> **Parent Document:** [../portable-implementation-and-hardcoding-control.md](../portable-implementation-and-hardcoding-control.md)
> **Current Version:** 1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-04-09 | **[Extended portability rules to reusable support/package source artifacts](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.1 | 2026-04-02 | **[Added public onboarding/install portability and source-vs-destination guidance](#version-11)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended the chain so public install/onboarding docs now treat workstation-specific absolute paths and internal umbrella workspace roots as portability failures by default, while adding explicit source-side versus destination/runtime notation guidance | |
| 1.0 | 2026-04-02 | **[Created first-class portable-implementation-and-hardcoding-control rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new design/runtime/changelog triad that governs portable implementation defaults, late-bound environment resolution, scoped local observations, and anti-hardcoding discipline for shared artifacts | |

---

<a id="version-12"></a>
## Version 1.2: Extended portability rules to reusable support/package source artifacts

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `portable-implementation-and-hardcoding-control.md` from v1.1 to v1.2.
- Updated `design/portable-implementation-and-hardcoding-control.design.md` from v1.1 to v1.2.
- Extended the chain so reusable support/package source artifacts such as plugin-owned docs, scripts, skills, and agents are explicitly portable-by-default when they are maintained as reusable source content.
- Added a distinct failure class for workstation-specific absolute paths embedded into such reusable support/package source artifacts.

### Summary
Portable-implementation-and-hardcoding-control now treats reusable support/package source artifacts as portable-by-default and no longer lets workstation paths hide inside them as if they were shared contracts.

---

<a id="version-11"></a>
## Version 1.1: Added public onboarding/install portability and source-vs-destination guidance

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/portable-implementation-and-hardcoding-control.design.md` from v1.0 to v1.1.
- Updated runtime `portable-implementation-and-hardcoding-control.md` from v1.0 to v1.1.
- Expanded the chain to explicitly cover public onboarding/install guidance in addition to general shared-artifact portability.
- Added an explicit source-side versus destination/runtime notation contract for public install docs.
- Added trigger-model coverage for README quickstart, clone-and-install, and marketplace add/install examples.
- Added new anti-pattern coverage for:
  - internal umbrella workspace roots being taught as public defaults
  - source and destination/runtime notation being blurred together
- Added validation and quality-metric coverage for public onboarding/install portability.
- Added explicit integration to `document-consistency.md` so notation separation stays consistent across checked references.

### Summary
Strengthened the portability owner so public onboarding/install docs are now governed as a first-class portability concern rather than being treated as a narrow README wording issue.

---

<a id="version-10"></a>
## Version 1.0: Created first-class portable-implementation-and-hardcoding-control rule chain

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/portable-implementation-and-hardcoding-control.design.md` as the active target-state design for portable implementation defaults and anti-hardcoding discipline.
- Created runtime `portable-implementation-and-hardcoding-control.md` as a first-class rule defining:
  - portable-core and late-binding principles
  - separation between portable contracts and observed local facts
  - canonical placeholder/env notation expectations
  - allowed machine-scoped exceptions
  - forbidden anti-patterns around hardcoded environment assumptions
  - validation checklist expectations for shared artifacts
- Positioned the chain as the semantic owner of portable implementation and environment-binding discipline while keeping adjacent owner boundaries intact for:
  - `no-variable-guessing.md`
  - `accurate-communication.md`
  - `project-documentation-standards.md`
  - `strict-file-hygiene.md`
  - `tactical-strategic-programming.md`

### Summary
Created a first-class `portable-implementation-and-hardcoding-control` rule chain so hardcoded environment assumptions in shared artifacts now have one durable semantic owner instead of remaining scattered across adjacent rules.
