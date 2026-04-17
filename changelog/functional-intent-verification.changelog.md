# Changelog - Functional Intent Verification

> **Parent Document:** [../functional-intent-verification.md](../functional-intent-verification.md)
> **Current Version:** 1.2
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-04-17 | **[Materialized destructive-confirmation runtime behavior and blocked cleanup/isolation delete authorization](#version-12)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| | | Summary: Replaced the header-only runtime stub with a real destructive-intent rule body and made cleanup/isolation rationale insufficient to authorize repository-file deletion | |
| 1.1 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-11)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical `Design + Session + Full history` runtime header metadata without changing substantive functional-intent behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-12"></a>
## Version 1.2: Materialized destructive-confirmation runtime behavior and blocked cleanup/isolation delete authorization

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `functional-intent-verification.md` from v1.1 to v1.2.
- Updated `design/functional-intent-verification.design.md` from v1.1 to v1.2.
- Materialized the runtime file from a header-only stub into a full destructive-intent rule body.
- Replaced the header-only runtime stub with a real rule body covering destructive confirmation, cleanup/isolation limits, and safe defaults.
- Added explicit wording that cleanup, hygiene, isolation, worktree, and sandbox rationale do not by themselves authorize deletion.
- Added repo-file deletion guidance that requires stronger semantic authority and explicit confirmation before removal.

### Summary
Functional-intent-verification now actively governs destructive delete intent at runtime and blocks cleanup/isolation rationale from substituting for deletion authorization.

---

<a id="version-11"></a>
## Version 1.1: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `functional-intent-verification.md` from v1.0 to v1.1.
- Updated `design/functional-intent-verification.design.md` from v1.0 to v1.1.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing functional-intent verification contract.

### Summary
Normalized runtime/design metadata to the cleanup-wave header standard without changing the substantive functional-intent policy.

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
