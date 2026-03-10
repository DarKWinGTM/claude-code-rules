# Changelog - Anti Sycophancy

> **Parent Document:** [../anti-sycophancy.md](../anti-sycophancy.md)
> **Current Version:** 1.2
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the design/session version state for the anti-sycophancy chain | |
| 1.1 | 2026-02-22 | **[Added Shared Verification Trigger Model (WS-5)](#version-11-added-shared-verification-trigger-model-ws-5)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added deterministic pre-agreement verification triggers and status labels for evidence-first disagreement behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

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
