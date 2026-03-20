# Changelog - Authority and Scope

> **Parent Document:** [../authority-and-scope.md](../authority-and-scope.md)
> **Current Version:** 1.3
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-03-17 | **[Added fresh-user-directive override over previously offered assistant options](#version-13)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Refined authority-and-scope so assistant-generated options remain advisory only and a fresh user directive overrides prior option framing unless the user explicitly selected one | |
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the authority-and-scope chain to the cleanup-wave version state | |
| 1.1 | 2026-02-22 | **[Added deterministic precedence contract and tie-break semantics](#version-11-added-deterministic-precedence-contract-and-tie-break-semantics)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | - Upgraded rule/design alignment from v1.0 to v1.1 around explicit precedence ordering | |
| | | - Added normalized term definitions for hard-boundary conflict handling | |
| | | Summary: Synchronized authority rule and design to deterministic conflict-resolution behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10-standardization)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-13"></a>
## Version 1.3: Added fresh-user-directive override over previously offered assistant options

**Date:** 2026-03-17
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `authority-and-scope.md` from v1.2 to v1.3.
- Updated `design/authority-and-scope.design.md` from v1.2 to v1.3.
- Added an explicit rule that assistant-generated options are advisory only unless the user explicitly selects one.
- Added an explicit precedence rule that a fresh user directive overrides previously offered assistant options when it changes scope, task, or action.
- Extended the conflict-resolution contract and quality metrics to cover fresh-directive override behavior.

### Summary
Refined authority-and-scope so a new user instruction cannot get trapped behind previously offered assistant options unless the user explicitly chooses one of them.

---

<a id="version-12"></a>
## Version 1.2: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `authority-and-scope.md` from v1.1 to v1.2.
- Updated `design/authority-and-scope.design.md` from v1.1 to v1.2.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing deterministic authority-order and tie-break semantics.

### Summary
Normalized the authority-and-scope chain to the canonical cleanup-wave runtime header format while preserving substantive authority behavior.

---

## Version 1.1: Added deterministic precedence contract and tie-break semantics

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `authority-and-scope.md` to v1.1 with explicit precedence matrix:
  - `HARD_BOUNDARY`
  - `USER_INSTRUCTION`
  - `RULE_CONTRACTS`
  - `DEFAULT_BEHAVIOR`
- Added deterministic term definitions for:
  - `higher-level safety policies`
  - `hard boundary`
  - `unresolved block`
- Added tie-break rules for hard-boundary conflicts and unresolved non-hard ambiguity.
- Updated `design/authority-and-scope.design.md` to v1.1 with matching conflict-resolution contract.

### Summary
Synchronized authority rule and design to deterministic precedence and tie-break semantics.

---

## Version 1.0: Standardization

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Migrated rule to standard template
- Established version history in changelog file

### Summary
Migrated to standard template
