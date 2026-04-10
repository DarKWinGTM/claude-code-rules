# Changelog - Evidence-Grounded Burden of Proof

> **Parent Document:** [../evidence-grounded-burden-of-proof.md](../evidence-grounded-burden-of-proof.md)
> **Current Version:** 1.3
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-04-09 | **[Added remembered path-matched context handling to the burden-of-proof model](#version-13)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.2 | 2026-04-06 | **[Added post-compact needs-recheck handling to the burden-of-proof model](#version-12)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.1 | 2026-04-05 | **[Added unresolved governing-basis handling to burden-of-proof model](#version-11)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.0 | 2026-03-12 | **[Created first-class evidence-grounded-burden-of-proof rule chain](#version-10)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Created a new design/runtime/changelog triad that governs evidence taxonomy, claim-state taxonomy, burden-of-proof thresholds, contradiction protocol, scoped negative-evidence semantics, and evidence-grounded communication across planning, debugging, coding, and review | |

---

<a id="version-13"></a>
## Version 1.3: Added remembered path-matched context handling to the burden-of-proof model

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `evidence-grounded-burden-of-proof.md` from v1.2 to v1.3.
- Updated `design/evidence-grounded-burden-of-proof.design.md` from v1.2 to v1.3.
- Added `RECALLED_PATH_MATCHED_CONTEXT` so applicable path-scoped memory is explicitly distinguished from current observed local fact.
- Added threshold, protocol, and wording support so remembered path-matched context may aid continuity without being overstated as current verified repo truth.
- Added integration links to the new `memory-governance-and-session-boundary` owner chain.

### Summary
Evidence-grounded-burden-of-proof now treats applicable path-scoped remembered context as a distinct evidence/claim state that still needs recheck before exact current-state repo facts are presented as verified truth.

---

<a id="version-12"></a>
## Version 1.2: Added post-compact needs-recheck handling to the burden-of-proof model

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `evidence-grounded-burden-of-proof.md` from v1.1 to v1.2.
- Updated `design/evidence-grounded-burden-of-proof.design.md` from v1.1 to v1.2.
- Added `POST_COMPACT_NEEDS_RECHECK` as an explicit claim-state for compacted carry-forward details that are no longer exact enough to remain verified without recheck.
- Added threshold, protocol, and work-mode guidance so compacted summary state no longer silently upgrades compressed-away detail into active truth.

### Summary
Evidence-grounded-burden-of-proof now treats compacted carry-forward exact detail as a recheck-needed state unless enough surviving evidence still preserves its exactness.

---

## Version 1.1: Added unresolved governing-basis handling to burden-of-proof model

**Date:** 2026-04-05
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `evidence-grounded-burden-of-proof.md` from v1.0 to v1.1.
- Updated `design/evidence-grounded-burden-of-proof.design.md` from v1.0 to v1.1.
- Added `UNRESOLVED_GOVERNING_BASIS` as an explicit claim-state for materially outcome-changing basis ambiguity.
- Added threshold, protocol, and planning guidance so unresolved policy/frame selection is treated as uncertainty that should trigger clarification rather than silent branch selection.

### Summary
Evidence-grounded-burden-of-proof now treats unresolved governing-basis selection as a first-class uncertainty state instead of allowing one plausible frame to become the active answer without enough proof.

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
