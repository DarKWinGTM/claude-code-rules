# Changelog - DAN-Safe Normalization

> **Parent Document:** [../dan-safe-normalization.md](../dan-safe-normalization.md)
> **Current Version:** 1.2
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the DAN-safe normalization chain to the cleanup-wave version state | |
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs, keeping active-rule references only where files exist | |
| 1.0 | 2026-02-21 | **[Initial DAN-Style Intent Normalization Design](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added normalization pipeline and guardrails for ambiguous DAN-style prompts | |

---

<a id="version-12"></a>
## Version 1.2: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `dan-safe-normalization.md` from v1.1 to v1.2.
- Updated `design/dan-safe-normalization.design.md` from v1.1 to v1.2.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing normalization-first behavioral contract.
- Normalized the changelog parent document to the active runtime authority path.

### Summary
Normalized the DAN-safe normalization chain to the canonical cleanup-wave runtime header format while preserving substantive behavior.

---

<a id="version-11"></a>
## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/dan-safe-normalization.design.md` to v1.1
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links
- Preserved existing link to active rule `zero-hallucination.md`
- Clarified Integration heading to `Related design docs / active rules`

### Summary
Removed broken design integration links and aligned references with current design-phase intent

---

<a id="version-10"></a>
## Version 1.0: Initial DAN-Style Intent Normalization Design

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/dan-safe-normalization.design.md` v1.0
- Defined normalize-first principle for DAN/jailbreak-style ambiguous framing
- Added normalization pipeline: extract intent, strip wrapper, bind scope, classify, decide
- Added guardrails to prevent normalization-as-bypass
- Added outcomes and integration points to refusal/decision rules

### Summary
Established normalization-first design that evaluates true bounded intent without weakening hard safety boundaries
