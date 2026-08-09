# Changelog - External Verification and Source Trust

> **Parent Document:** [../external-verification-and-source-trust.md](../external-verification-and-source-trust.md)
> **Current Version:** 1.7
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.7 | 2026-08-10 | **[Added capability-bound authorized source selection and bounded substitutes](#version-17)** | 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e |
| 1.6 | 2026-08-09 | **[Compacted source-trust integration handoffs](#version-16)** | 92c4d51e-eb02-4299-823a-1a6b8270f045 |
| 1.5 | 2026-08-08 | **[Separated public evidence lookup from consequential external action](#version-15)** | 92c4d51e-eb02-4299-823a-1a6b8270f045 |
| 1.4 | 2026-08-08 | **[Applied owner-canonical active runtime compression](#version-14)** | 92c4d51e-eb02-4299-823a-1a6b8270f045 |
| 1.3 | 2026-05-22 | **[Added evidence-earned provider/supplier scope narrowing refinement](#version-13)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.2 | 2026-05-06 | **[Integrated source trust with delegated research lanes](#version-12)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 1.1 | 2026-04-30 | **[Added proof-aware external grounding for recommendations and design](#version-11)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Extended external verification so current external facts can ground analysis, design, recommendation, and disagreement while only authoritative requirements, compatibility limits, safety/compliance boundaries, or verified contradictions become binding | |
| 1.0 | 2026-03-31 | **[Created first-class external-verification-and-source-trust rule chain](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created a new design/runtime/changelog triad that governs proactive external verification, source-reliability ranking, corroboration expectations, and source-conflict handling for WebSearch/WebFetch-backed factual work | |

---

<a id="version-17"></a>
## Version 1.7: Added capability-bound authorized source selection and bounded substitutes

**Date:** 2026-08-10
**Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e

### Changes
- Required authenticated, private, local-only, and mechanism-constrained verification to consume capability and authorization preflight from `action-safety.md` before source selection.
- Defined source eligibility separately from source trust and required selection of the strongest reachable authorized claim-fit source.
- Added bounded-substitute handling for supplied screenshots, rendered artifacts, sanitized exports, and public authorities, with explicit provenance and proof limits.
- Preserved `action-safety.md` ownership of approval, credential/session-material boundaries, and retry/failure behavior.
- Preserved `refusal-and-recovery.md` ownership of workflow-block classification and recovery when no eligible source exists.

### Summary
External verification now starts from the eligible-source boundary produced by action safety, then selects the strongest claim-fit authorized source or a clearly bounded substitute without turning source trust into a second approval, credential, or retry authority.

<a id="version-16"></a>
## Version 1.6: Compacted source-trust integration handoffs

**Date:** 2026-08-09
**Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045

### Changes
- Compacted repeated Integration and consumer wording to canonical owner handoffs while preserving the chain’s active behavior, exact guards, and substantive runtime body.

### Summary
This version advances the external-verification-and-source-trust triad for P073-12 owner-boundary repair and bounded runtime compaction without weakening its governed responsibility.

<a id="version-15"></a>
## Version 1.5: Separated public evidence lookup from consequential external action

**Date:** 2026-08-08
**Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045

### Changes
- Clarified that ordinary public read-only lookup remains proactive evidence gathering when proportional.
- Deferred authenticated/private access, mutation, sending or publishing, purchase or payment, deployment, account/shared-state change, sensitive-data disclosure, meaningful cost, and terms acceptance to `action-safety.md` approval gates.
- Preserved source ranking, corroboration, conflict handling, and evidence-earned provider/supplier scope.

### Summary
This version synchronizes the active runtime and design target state for the v10.57 semantic-resolution and owner-canonical compaction wave without claiming publication before the release gate.

<a id="version-14"></a>
## Version 1.4: Applied owner-canonical active runtime compression

**Date:** 2026-08-08
**Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045

### Changes
- Compressed repeated runtime wording in `external-verification-and-source-trust.md` while preserving the chain owner, operational contracts, and exact guard semantics.
- Kept the design target state unchanged while synchronizing runtime, design, and changelog versions for repository release `v10.54`.
- Revalidated this chain as part of the combined 19-Rule runtime set rather than as a standalone duplicated policy package.

### Summary
This version reduces runtime context cost without changing the chain’s governed responsibility or weakening its active decision boundaries.

<a id="version-13"></a>
## Version 1.3: Added evidence-earned provider/supplier scope narrowing refinement

**Date:** 2026-05-22
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `external-verification-and-source-trust.md` from v1.2 to v1.3.
- Updated `design/external-verification-and-source-trust.design.md` from v1.2 to v1.3.
- Added guidance that provider-, supplier-, model-, or path-specific narrowing should be treated as an evidence-earned scope decision rather than a default convenience recommendation.
- Added stronger corroboration expectations when a narrower local doctrine claim would materially change the chosen fix owner.
- Preserved source trust, conflict handling, and broad research-lane orchestration behavior.

### Summary
`external-verification-and-source-trust.md` now requires stronger corroboration before provider/supplier/model/path-specific scope becomes the strategic recommendation.

---

<a id="version-12"></a>
## Version 1.2: Integrated source trust with delegated research lanes

**Date:** 2026-05-06
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `external-verification-and-source-trust.md` from v1.1 to v1.2.
- Updated `design/external-verification-and-source-trust.design.md` from v1.1 to v1.2.
- Added an orchestrated external research boundary so broad, comparison-heavy, or source-volume-heavy verification can be gathered through native worker research lanes.
- Required research lane assignments and handoffs to preserve source tier, freshness, specificity, conflict state, downgraded weak sources, and leader verification needs.
- Clarified that delegated research lowers leader raw context load but does not lower external source-trust or evidence-calibration requirements.

### Summary
External verification now works cleanly with subagent research orchestration: workers can gather and compare broad source sets, while this chain still controls source trust, corroboration, conflict handling, and evidence-strength boundaries.

---

<a id="version-11"></a>
## Version 1.1: Added proof-aware external grounding for recommendations and design

**Date:** 2026-04-30
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `external-verification-and-source-trust.md` from v1.0 to v1.1.
- Updated `design/external-verification-and-source-trust.design.md` from v1.0 to v1.1.
- Added proof-aware external evidence grounding for analysis, design, recommendation, and disagreement when current external facts materially affect the answer.
- Clarified that external evidence becomes binding only for authoritative requirements, compatibility limits, safety/compliance boundaries, or verified contradictions.
- Added design/recommendation integrity wording so source checks improve judgment without silently becoming a rigid architecture mandate.

### Summary
External-verification-and-source-trust now uses current external facts as stronger reasoning input for recommendations and designs while preserving trade-offs unless the evidence is genuinely binding.

---

<a id="version-10"></a>
## Version 1.0: Created first-class external-verification-and-source-trust rule chain

**Date:** 2026-03-31
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/external-verification-and-source-trust.design.md` as the active target-state design for proactive external verification and source-trust analysis.
- Created runtime `external-verification-and-source-trust.md` as a first-class rule defining:
  - proactive external verification triggers
  - external-source trust ranking
  - corroboration / multi-source comparison expectations
  - source-conflict handling
  - verification-before-recommendation expectations for current external facts
  - honest bounded fallback behavior after incomplete verification
- Positioned the chain as the semantic owner of external verification and source-trust workflow while keeping adjacent authority boundaries intact for:
  - `zero-hallucination.md`
  - `evidence-grounded-burden-of-proof.md`
  - `accurate-communication.md`
  - `anti-sycophancy.md`
  - `operational-failure-handling.md`
- Explicitly prohibited silent equal-trust treatment of weak/contradictory sources and encouraged proactive verification when low-cost checks materially improve accuracy.

### Summary
Created a first-class `external-verification-and-source-trust` rule chain so proactive web verification, source-trust ranking, corroboration, and source-conflict handling now have one durable semantic authority instead of remaining scattered across adjacent rules.
