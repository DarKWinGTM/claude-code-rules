# Changelog - Zero Hallucination

> **Parent Document:** [../zero-hallucination.md](../zero-hallucination.md)
> **Current Version:** 1.4
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.4 | 2026-04-17 | **[Added git-state negative-claim limits for file disposability](#version-14)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| | | Summary: Extended zero-hallucination so git-state signals remain local observations only and do not justify claims that a file is irrelevant, non-governed, or disposable | |
| 1.3 | 2026-03-12 | **[Materialized zero-hallucination runtime body and added evidence-state / negative-claim discipline](#version-13)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Replaced the header-only runtime stub with a full rule body that now distinguishes fact, inference, hypothesis, and scoped non-findings, adds source-priority behavior, and forbids turning limited non-findings into stronger contradiction or absence claims | |
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the zero-hallucination chain to the cleanup-wave version state | |
| 1.1 | 2026-02-22 | **[Added Shared Verification Trigger Model (WS-5)](#version-11-added-shared-verification-trigger-model-ws-5)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added deterministic verification triggers and status labels across runtime/design contract text | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-14"></a>
## Version 1.4: Added git-state negative-claim limits for file disposability

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `zero-hallucination.md` from v1.3 to v1.4.
- Updated `design/zero-hallucination.design.md` from v1.3 to v1.4.
- Added negative-claim guidance and examples clarifying that git untracked/new/dirty status is only a local observation.
- Added anti-pattern coverage so git-state signals no longer read like proof that a file is irrelevant, non-governed, or disposable.

### Summary
Zero-hallucination now blocks git-state observations from being overread as disposal truth, keeping file-meaning claims aligned to stronger checked evidence.

---

<a id="version-13"></a>
## Version 1.3: Materialized zero-hallucination runtime body and added evidence-state / negative-claim discipline

**Date:** 2026-03-12
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `zero-hallucination.md` from v1.2 to v1.3.
- Updated `design/zero-hallucination.design.md` from v1.2 to v1.3.
- Replaced the header-only runtime stub with a full rule body defining:
  - source-priority behavior
  - fact vs inference vs hypothesis separation
  - uncertainty-honesty behavior
  - negative-claim / absence discipline
- Standardized the distinction between scoped non-findings and stronger absence claims.
- Clarified that limited non-findings do not justify direct contradiction against the user by themselves.
- Integrated the new first-class `evidence-grounded-burden-of-proof` chain as the owner of burden thresholds while keeping zero-hallucination as the factual-claim verification owner.

### Summary
Materialized zero-hallucination into a real runtime rule body and strengthened it so technical claims, absence claims, and evidence-limited findings now stay aligned to actual proof strength.

---

<a id="version-12"></a>
## Version 1.2: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `zero-hallucination.md` from v1.1 to v1.2.
- Updated `design/zero-hallucination.design.md` from v1.1 to v1.2.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing zero-hallucination behavioral contract.

### Summary
Normalized the zero-hallucination chain to the canonical cleanup-wave runtime header format while preserving substantive verification behavior.

---

## Version 1.1: Added Shared Verification Trigger Model (WS-5)

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `zero-hallucination.md` from v1.0 to v1.1.
- Updated `design/zero-hallucination.design.md` from v1.0 to v1.1.
- Added shared verification trigger model to standardize when claims require explicit verification.
- Added deterministic reporting labels for verification state:
  - `✅ Verified`
  - `⚠️ Unverified`
  - `❌ Not Found`

### Summary
Aligned runtime and design behavior to a shared WS-5 verification-trigger contract for deterministic evidence-first responses.

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
