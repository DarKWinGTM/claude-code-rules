# Changelog - Evidence-Grounded Burden of Proof

> **Parent Document:** [../evidence-grounded-burden-of-proof.md](../evidence-grounded-burden-of-proof.md)
> **Current Version:** 1.0
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-03-12 | **[Created first-class evidence-grounded-burden-of-proof rule chain](#version-10)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Created a new design/runtime/changelog triad that governs evidence taxonomy, claim-state taxonomy, burden-of-proof thresholds, contradiction protocol, scoped negative-evidence semantics, and evidence-grounded communication across planning, debugging, coding, and review | |

---

<a id="version-10"></a>
## Version 1.0: Created first-class evidence-grounded-burden-of-proof rule chain

**Date:** 2026-03-12
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Created `design/evidence-grounded-burden-of-proof.design.md` as the active target-state design for evidence-grounded judgment and burden-of-proof communication.
- Created runtime `evidence-grounded-burden-of-proof.md` as a first-class rule defining:
  - evidence taxonomy
  - claim-state taxonomy
  - burden-of-proof threshold matrix
  - contradiction protocol
  - negative-evidence / absence semantics
  - burden-of-proof communication contract
  - operational application across planning, debugging, coding, and review
- Positioned the chain as the semantic owner of evidence-threshold judgment while keeping adjacent authority boundaries intact for:
  - `accurate-communication.md`
  - `zero-hallucination.md`
  - `anti-sycophancy.md`
  - `no-variable-guessing.md`
  - `explanation-quality.md`
- Explicitly prohibited unsupported person-directed verdicts such as calling the user wrong, mistaken, or confused without contrary evidence.
- Standardized the distinction between `NOT_FOUND_IN_CHECKED_SCOPE` and stronger absence claims.

### Summary
Created a first-class `evidence-grounded-burden-of-proof` rule chain so evidence thresholds, contradiction discipline, scoped non-findings, and fact-vs-inference-vs-hypothesis communication now have one durable semantic authority instead of remaining scattered across adjacent rules.
