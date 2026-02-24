# Changelog - Document Changelog Control

> **Parent Document:** [../document-changelog-control.md](../document-changelog-control.md)
> **Current Version:** 4.6
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.6 | 2026-02-23 | **[Adopted UDVC-1 deterministic contract baseline](#version-46)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Synchronized design/runtime/changelog to v4.6 with triad alignment, mandatory metadata, canonical anchors, and fixed execution order | |
| 4.5 | 2026-02-22 | **[Synchronized runtime session metadata to real active session value](#version-45)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Replaced runtime placeholder session text with active-session UUID | |
| 4.4 | 2026-02-21 | **[Introduced OR compliance and explicit pair behavior](#version-44)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added OR compliance and strict design/changelog pair separation | |
| 4.3 | 2026-01-20 | **[Required detailed sections plus unified table in changelog](#version-43)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Established two-part changelog format | |
| 4.2 | 2026-01-20 | **[Clarified changelog header and section naming](#version-42)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Clarified header naming versus table format in changelog files | |
| 4.1 | 2026-01-20 | **[Clarified design navigator behavior](#version-41)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Design docs provide navigation link rather than duplicated full history | |
| 4.0 | 2026-01-20 | **[Established baseline version-governance architecture](#version-40)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Introduced foundational documentation version-governance model | |

---

<a id="version-46"></a>
## Version 4.6: Adopted UDVC-1 deterministic contract baseline

**Date:** 2026-02-23
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated runtime `document-changelog-control.md` from v4.5 to v4.6.
- Aligned runtime contract to `design/document-changelog-control.design.md` v4.6.
- Formalized mandatory rule-chain triad alignment requirements in runtime policy text.
- Formalized mandatory metadata contract for rule/design/patch/changelog layers.
- Standardized canonical version-anchor policy to `#version-xy`.
- Enforced fixed synchronization order: `design → runtime rule → changelog → TODO`.

### Summary
Established UDVC-1 as the active deterministic governance contract and synchronized rule/design/changelog references to v4.6.

---

<a id="version-45"></a>
## Version 4.5: Synchronized runtime session metadata to real active session value

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Replaced placeholder session text in runtime `document-changelog-control.md` with active-session UUID.
- Preserved v4.4 semantics (OR compliance and pair behavior).

### Summary
Closed runtime session-metadata contradiction by replacing placeholder session text with real session value.

---

<a id="version-44"></a>
## Version 4.4: Introduced OR compliance and explicit pair behavior

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Clarified traceable version path as OR compliance (`local table` OR `full-history link`).
- Made pair behavior explicit when design/changelog documents coexist.
- Normalized malformed legacy changelog structure while preserving historical intent.

### Summary
Added OR compliance and explicit design/changelog pair behavior.

---

<a id="version-43"></a>
## Version 4.3: Required detailed sections plus unified table in changelog

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified changelog as two mandatory parts: detailed sections and `Version History (Unified)` table.

### Summary
Established two-part changelog format as mandatory.

---

<a id="version-42"></a>
## Version 4.2: Clarified changelog header and section naming

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified usage of `Version History` section header and distinction from data format.

### Summary
Reduced ambiguity between header naming and table format.

---

<a id="version-41"></a>
## Version 4.1: Clarified design navigator behavior

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified design documents as navigator/link-only for version history in pair model.

### Summary
Prevented duplicated full-history blocks across design/changelog pair.

---

<a id="version-40"></a>
## Version 4.0: Established baseline version-governance architecture

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Introduced structured documentation version-governance model.
- Established changelog-centered authority concept.

### Summary
Baseline architecture for documentation version governance.
