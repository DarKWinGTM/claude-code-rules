# Changelog - Document Patch Control

> **Parent Document:** [../document-patch-control.md](../document-patch-control.md)
> **Current Version:** 1.2
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-02-23 | **[Synchronized patch-control runtime contract to UDVC-1 metadata baseline](#version-12)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Aligned runtime/design/changelog to v1.2 with mandatory patch metadata and deterministic synchronization contract | |
| 1.1 | 2026-02-22 | **[Synchronized patch-control references to active runtime standards](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Closed patch-reference/version drift across runtime/design/changelog artifacts | |
| 1.0 | 2026-02-01 | **[Initial design](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Initial release of patch-control standards | |

---

<a id="version-12"></a>
## Version 1.2: Synchronized patch-control runtime contract to UDVC-1 metadata baseline

**Date:** 2026-02-23
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated runtime `document-patch-control.md` from v1.1 to v1.2.
- Aligned runtime `Based on` reference to `design/document-patch-control.design.md` v1.2.
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
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

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
