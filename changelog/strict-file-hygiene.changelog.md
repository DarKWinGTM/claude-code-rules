# Changelog - Strict File Hygiene

> **Parent Document:** [../strict-file-hygiene.md](../strict-file-hygiene.md)
> **Current Version:** 1.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.5 | 2026-04-25 | **[Added shared runtime destination non-member boundary](#version-15)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 1.4 | 2026-04-17 | **[Blocked cleanup/hygiene from acting as deletion authority](#version-14)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| | | Summary: Refined strict-file-hygiene so junk-file wording stays creation-side only, newly encountered files are not disposable by cleanup instinct alone, and hygiene/isolation rationale no longer reads like delete permission | |
| 1.3 | 2026-04-02 | **[Added portable-artifact hygiene guidance](#version-13)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended strict-file-hygiene so reusable artifacts should avoid machine-local hardcoded defaults by default and now defer broader portability expectations to `portable-implementation-and-hardcoding-control` | |
| 1.2 | 2026-03-28 | **[Added startup-governance deference for required governed artifacts](#version-12)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Refined strict-file-hygiene so required governed startup artifacts resolved through `artifact-initiation-control` are allowed, while junk summaries and duplicate docs remain prohibited | |
| 1.1 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-11)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical `Design + Session + Full history` runtime header metadata without changing substantive strict-file-hygiene behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-15"></a>
## Version 1.5: Added shared runtime destination non-member boundary

**Date:** 2026-04-25
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `strict-file-hygiene.md` from v1.4 to v1.5.
- Updated `design/strict-file-hygiene.design.md` from v1.4 to v1.5.
- Added explicit shared-destination non-member wording so destination/runtime files outside the current source-owned active runtime install set are not junk by default.
- Updated the classify/remove decision flow to resolve owner/project scope before hygiene classification when files are co-located in a shared runtime destination.
- Preserved the rule that hygiene, cleanup, isolation, worktree, sandbox, and runtime co-location are not deletion authority.

### Summary
Strict-file-hygiene now blocks runtime-destination co-location from becoming a junk-file classification shortcut for other-owner runtime files.

---

<a id="version-14"></a>
## Version 1.4: Blocked cleanup/hygiene from acting as deletion authority

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `strict-file-hygiene.md` from v1.3 to v1.4.
- Updated `design/strict-file-hygiene.design.md` from v1.3 to v1.4.
- Clarified that junk-file hygiene remains a creation/duplication rule rather than deletion authority.
- Added explicit anti-pattern coverage so untracked/newly seen files are not treated as disposable by cleanup instinct alone.
- Added a decision-flow boundary that routes delete/remove behavior to stronger semantic-authority and destructive-confirmation owners.

### Summary
Strict-file-hygiene now blocks cleanup and hygiene wording from being overread as deletion authority, especially for newly encountered or untracked repo files.

---

<a id="version-13"></a>
## Version 1.3: Added portable-artifact hygiene guidance

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `strict-file-hygiene.md` from v1.2 to v1.3.
- Updated `design/strict-file-hygiene.design.md` from v1.2 to v1.3.
- Added a portable-artifact hygiene principle so reusable artifacts should not embed machine-local hardcoded defaults by default.
- Added explicit integration to `portable-implementation-and-hardcoding-control.md`.

### Summary
Extended strict-file-hygiene so reusable shared artifacts now avoid machine-local hardcoded defaults by default while broader portability governance is delegated to the new first-class owner.

---

<a id="version-12"></a>
## Version 1.2: Added startup-governance deference for required governed artifacts

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/strict-file-hygiene.design.md` from v1.1 to v1.2.
- Updated runtime `strict-file-hygiene.md` from v1.1 to v1.2.
- Added a governed-startup exception so required design/changelog/TODO/phase/patch artifacts resolved through `artifact-initiation-control` are not treated as junk files.
- Preserved the prohibition on arbitrary proactive summaries, duplicate docs, and version-suffixed copies.
- Added explicit integration wording so hygiene defers to startup-governance for required artifact creation instead of silently blocking it.

### Summary
Refined strict-file-hygiene so it no longer suppresses required governed startup artifacts while still preventing non-required junk files and duplicates.

---

<a id="version-11"></a>
## Version 1.1: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `strict-file-hygiene.md` from v1.0 to v1.1.
- Updated `design/strict-file-hygiene.design.md` from v1.0 to v1.1.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing strict-file-hygiene behavioral contract.

### Summary
Normalized runtime/design metadata to the cleanup-wave header standard without changing the substantive file-hygiene policy.

---

<a id="version-10"></a>
## Version 1.0: Standardization

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Migrated rule to standard template
- Established version history in changelog file

### Summary
Migrated to standard template
