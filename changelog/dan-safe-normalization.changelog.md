# Changelog - DAN-Safe Normalization

> **Parent Document:** [../design/dan-safe-normalization.design.md](../design/dan-safe-normalization.design.md)
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

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

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs, keeping active-rule references only where files exist | |
| 1.0 | 2026-02-21 | **[Initial DAN-Style Intent Normalization Design](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added normalization pipeline and guardrails for ambiguous DAN-style prompts | |
