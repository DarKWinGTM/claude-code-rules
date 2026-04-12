# Changelog - Project Documentation Standards

> **Parent Document:** [../project-documentation-standards.md](../project-documentation-standards.md)
> **Current Version:** 2.17
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
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
