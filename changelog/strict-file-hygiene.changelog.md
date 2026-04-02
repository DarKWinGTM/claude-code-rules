# Changelog - Strict File Hygiene

> **Parent Document:** [../strict-file-hygiene.md](../strict-file-hygiene.md)
> **Current Version:** 1.3
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-04-02 | **[Added portable-artifact hygiene guidance](#version-13)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended strict-file-hygiene so reusable artifacts should avoid machine-local hardcoded defaults by default and now defer broader portability expectations to `portable-implementation-and-hardcoding-control` | |
| 1.2 | 2026-03-28 | **[Added startup-governance deference for required governed artifacts](#version-12)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Refined strict-file-hygiene so required governed startup artifacts resolved through `artifact-initiation-control` are allowed, while junk summaries and duplicate docs remain prohibited | |
| 1.1 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-11)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical `Design + Session + Full history` runtime header metadata without changing substantive strict-file-hygiene behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

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
