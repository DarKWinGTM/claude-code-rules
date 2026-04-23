# Changelog - Document Design Control

> **Parent Document:** [../document-design-control.md](../document-design-control.md)
> **Current Version:** 1.9
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.9 | 2026-04-23 | **[Added doc-derived knowledge capture to the governed design layer](#version-19)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 1.8 | 2026-03-08 | **[Enforced active-state-only design bodies and support-artifact boundary](#version-18)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Updated the chain to prohibit historical audit content in active design docs and to clarify that support-only artifacts should not remain in ambiguous `.design.md` form | |
| 1.7 | 2026-02-23 | **[Synchronized design-control runtime contract to UDVC-1 baseline](#version-17)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Aligned runtime rule/design/changelog to v1.7 with triad checks, canonical anchor policy, and fixed execution order | |
| 1.6 | 2026-02-22 | **[Removed runtime version-table contradiction and synchronized references](#version-16)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Closed v1.6 rule/design/changelog drift and removed runtime self-contradiction | |
| 1.5 | 2026-02-22 | **[Clarified pair-model language governance references](#version-15)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Closed version/reference/language drift for the v1.5 cycle | |
| 1.4 | 2026-02-21 | **[Synchronized metadata to latest consistency patch set](#version-14)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Parent path, version marker, session metadata, and heading normalization | |
| 1.3 | 2026-01-26 | **[Added simple/complex pattern decision model](#version-13)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Added Pattern 1 for single-design projects and Pattern 2 for multi-design projects | |
| 1.2 | 2026-01-21 | **[Changed terminology to neutral relationship](#version-12)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Replaced hierarchical wording with related-reference wording | |
| 1.1 | 2026-01-21 | **[Aligned design docs to navigator behavior](#version-11)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Removed local version-table expectation from design docs | |
| 1.0 | 2026-01-20 | **[Initial design-control standard](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Established baseline naming/location/structure standards for design docs | |

---

<a id="version-19"></a>
## Version 1.9: Added doc-derived knowledge capture to the governed design layer

**Date:** 2026-04-23
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated runtime `document-design-control.md` from v1.8 to v1.9.
- Updated `design/document-design-control.design.md` from v1.8 to v1.9.
- Added an explicit rule that implementation-critical knowledge learned from external docs/specs/provider references must be normalized into the governed design layer before or alongside continued multi-step work that relies on it.
- Added extraction-specificity guidance so design captures preserve implementation-relevant truth rather than copied source prose.
- Added verification/quality checks for external-doc-derived implementation truth capture.

### Summary
Document-design-control now makes governed design the required durable home for implementation-relevant knowledge extracted from external docs/specs when later work still depends on it.

---

<a id="version-18"></a>
## Version 1.8: Enforced active-state-only design bodies and support-artifact boundary

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `design/document-design-control.design.md` from v1.7 to v1.8.
- Updated runtime `document-design-control.md` from v1.7 to v1.8.
- Clarified that active design bodies must not embed audit logs, remediation history, rollout journals, or obsolete pending instructions.
- Added an explicit support-artifact boundary so reference-only materials do not remain in ambiguous governed `.design.md` form.
- Preserved canonical-anchor and synchronization-order requirements while tightening active-state design-body behavior.

### Summary
Updated the chain so design docs now explicitly represent current active state only, while support-only artifacts are kept out of ambiguous governed design semantics.

---

<a id="version-17"></a>
## Version 1.7: Synchronized design-control runtime contract to UDVC-1 baseline

**Date:** 2026-02-23
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated runtime `document-design-control.md` from v1.6 to v1.7.
- Synchronized runtime `Based on` reference to `design/document-design-control.design.md` v1.7.
- Added explicit rule-chain triad alignment requirements.
- Added canonical anchor policy (`#version-xy`) in runtime contract.
- Added non-negotiable synchronization order (`design → runtime rule → changelog → TODO`).
- Preserved navigator-only behavior for design documents in pair model.

### Summary
Aligned the design-control runtime rule with UDVC-1 deterministic governance while keeping design/changelog pair behavior explicit.

---

<a id="version-16"></a>
## Version 1.6: Removed runtime version-table contradiction and synchronized references

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Removed embedded runtime `## Version` table from `document-design-control.md`.
- Updated design and runtime references to v1.6.
- Corrected design-layer full-history link path.

### Summary
Closed v1.6 synchronization drift and eliminated runtime self-contradiction.

---

<a id="version-15"></a>
## Version 1.5: Clarified pair-model language governance references

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Aligned changelog with rule/design v1.5.
- Clarified pair-model requirements and language-governance references.

### Summary
Closed remaining v1.5 reference and language drift.

---

<a id="version-14"></a>
## Version 1.4: Synchronized metadata to latest consistency patch set

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated parent reference path, current version marker, and active session metadata.
- Standardized heading style to `Version History (Unified)`.

### Summary
Metadata synchronization for consistency patch cycle.

---

<a id="version-13"></a>
## Version 1.3: Added simple/complex pattern decision model

**Date:** 2026-01-26
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added Pattern 1 (single-design root layout) and Pattern 2 (multi-design directory layout).

### Summary
Added location/suffix decision model for design docs.

---

<a id="version-12"></a>
## Version 1.2: Changed terminology to neutral relationship

**Date:** 2026-01-21
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Replaced hierarchical "primary" terminology with neutral related-reference terminology.

### Summary
Normalized wording to non-hierarchical relationship language.

---

<a id="version-11"></a>
## Version 1.1: Aligned design docs to navigator behavior

**Date:** 2026-01-21
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Removed version-table expectation from design docs.
- Synchronized with changelog-control navigator behavior.

### Summary
Design docs are navigator/link-only in pair model.

---

<a id="version-10"></a>
## Version 1.0: Initial design-control standard

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Established baseline standards for design naming, location, structure, and changelog integration.

### Summary
Initial release of document-design-control standards.
