# Changelog - Authority and Scope

> **Parent Document:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md)
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-02-22 | **[Added deterministic precedence contract and tie-break semantics](#version-11-added-deterministic-precedence-contract-and-tie-break-semantics)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | - Upgraded rule/design alignment from v1.0 to v1.1 around explicit precedence ordering | |
| | | - Added normalized term definitions for hard-boundary conflict handling | |
| | | Summary: Synchronized authority rule and design to deterministic conflict-resolution behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10-standardization)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

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
