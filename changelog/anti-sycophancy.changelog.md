# Changelog - Anti Sycophancy

> **Parent Document:** [../anti-sycophancy.md](../anti-sycophancy.md)
> **Current Version:** 1.6
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.6 | 2026-04-30 | **[Added evidence-seeking proof-aware recommendation posture](#version-16)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Extended anti-sycophancy so substantial recommendation, design, agreement, and disagreement seek practical evidence when factual grounding would improve judgment without turning ordinary evidence into a forced path | |
| 1.5 | 2026-04-30 | **[Added evidence-calibrated agreement principle](#version-15)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Extended anti-sycophancy from disagreement-only posture into evidence-calibrated agreement/disagreement so user preference can be accepted without factual endorsement and factual agreement requires evidence | |
| 1.4 | 2026-03-27 | **[Added calm constructive correction tone guidance to anti-sycophancy](#version-14)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| | | Summary: Extended anti-sycophancy so disagreement now avoids both praise-heavy softening and rhetorical sharpness, keeping correction calm, useful, and claim-focused | |
| 1.3 | 2026-03-12 | **[Materialized anti-sycophancy runtime body and added evidence-grounded contradiction ladder](#version-13)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Replaced the header-only runtime stub with a full disagreement rule that now requires contrary evidence before direct contradiction, separates verified contradiction from partial-evidence tension, and prefers claim-focused correction over person-directed verdicts | |
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the design/session version state for the anti-sycophancy chain | |
| 1.1 | 2026-02-22 | **[Added Shared Verification Trigger Model (WS-5)](#version-11-added-shared-verification-trigger-model-ws-5)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added deterministic pre-agreement verification triggers and status labels for evidence-first disagreement behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-16"></a>
## Version 1.6: Added evidence-seeking proof-aware recommendation posture

**Date:** 2026-04-30
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `anti-sycophancy.md` from v1.5 to v1.6.
- Updated `design/anti-sycophancy.design.md` from v1.5 to v1.6.
- Added practical evidence-seeking before substantial factual alignment, disagreement, recommendation, and design judgment.
- Added an evidence-grounded recommendation/design ladder path that uses proof as support while preserving alternatives unless evidence creates a hard constraint.
- Added forbidden-behavior coverage for floating recommendations and proof overreach.

### Summary
Anti-sycophancy now prevents both over-agreement and over-correction by grounding factual alignment or challenge in practical evidence while keeping ordinary evidence from becoming a rigid final lock.

---

<a id="version-15"></a>
## Version 1.5: Added evidence-calibrated agreement principle

**Date:** 2026-04-30
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `anti-sycophancy.md` from v1.4 to v1.5.
- Updated `design/anti-sycophancy.design.md` from v1.4 to v1.5.
- Added an evidence-calibrated agreement principle so the assistant can acknowledge concerns and accept user-owned preferences/directions without endorsing unverified factual claims.
- Replaced a disagreement-only ladder with a calibration ladder covering user preference/direction, verified support, partial evidence, insufficient evidence, and verified contradiction.
- Added trigger and forbidden-behavior coverage for root-cause/security claims, unsupported factual endorsement, and preference/fact conflation.

### Summary
Anti-sycophancy now prevents over-agreement without becoming a rigid "never agree" rule: agreement is allowed when evidence supports it, user direction remains accepted as direction, and contradictions stay claim-focused and evidence-grounded.

---

<a id="version-14"></a>
## Version 1.4: Added calm constructive correction tone guidance to anti-sycophancy

**Date:** 2026-03-27
**Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2

### Changes
- Updated `anti-sycophancy.md` from v1.3 to v1.4.
- Updated `design/anti-sycophancy.design.md` from v1.3 to v1.4.
- Added constructive-disagreement guidance against flattery-heavy softening that weakens the actual correction.
- Added guidance against rhetorical sharpness when calmer claim-focused correction is sufficient.
- Added forbidden-behavior and anti-pattern coverage for praise-heavy correction framing and unnecessary rhetorical edge.

### Summary
Extended anti-sycophancy so disagreement now avoids both praise-heavy softening and rhetorical sharpness, keeping correction calm, useful, and claim-focused.

---

<a id="version-13"></a>
## Version 1.3: Materialized anti-sycophancy runtime body and added evidence-grounded contradiction ladder

**Date:** 2026-03-12
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `anti-sycophancy.md` from v1.2 to v1.3.
- Updated `design/anti-sycophancy.design.md` from v1.2 to v1.3.
- Replaced the header-only runtime stub with a full rule body defining:
  - evidence-before-correction discipline
  - a contradiction ladder for verified contradiction vs partial-evidence tension vs insufficient evidence
  - claim-focused vs person-focused correction boundaries
  - constructive disagreement expectations
- Added an explicit rule that the assistant must not say the user is wrong, mistaken, or confused without contrary evidence.
- Clarified that limited non-findings and partial evidence are not enough for unqualified contradiction.
- Integrated the new `evidence-grounded-burden-of-proof` chain as the burden-threshold authority while preserving anti-sycophancy as the disagreement-posture owner.

### Summary
Materialized anti-sycophancy into a real runtime rule body and refined it so disagreement now stays evidence-grounded, proportionate, and claim-focused instead of swinging between false agreement and overreaching contradiction.

---

<a id="version-12"></a>
## Version 1.2: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `anti-sycophancy.md` from v1.1 to v1.2.
- Updated `design/anti-sycophancy.design.md` from v1.1 to v1.2.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing evidence-first anti-sycophancy behavioral contract.

### Summary
Normalized the anti-sycophancy chain to the canonical cleanup-wave runtime header format while preserving substantive rule behavior.

---

## Version 1.1: Added Shared Verification Trigger Model (WS-5)

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `anti-sycophancy.md` from v1.0 to v1.1.
- Updated `design/anti-sycophancy.design.md` from v1.0 to v1.1.
- Added shared verification trigger model for pre-agreement evidence checks.
- Added deterministic reporting labels for verification state:
  - `✅ Verified`
  - `⚠️ Unverified`
  - `❌ Not Found`

### Summary
Aligned anti-sycophancy runtime and design behavior to WS-5 deterministic verification-trigger checks before technical agreement.

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
