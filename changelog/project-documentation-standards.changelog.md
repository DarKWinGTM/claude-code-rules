# Changelog - Project Documentation Standards

> **Parent Document:** [../project-documentation-standards.md](../project-documentation-standards.md)
> **Current Version:** 2.11
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
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
