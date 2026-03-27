# Phase 004 - Sync Master Docs, Install, and Verify

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P4
> **Status:** Completed
> **Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2
> **Design References:** [../design/natural-professional-communication.design.md](../design/natural-professional-communication.design.md)
> **Patch References:** n/a

---

## Objective

Synchronize the repository-level governance docs, install touched runtime rules, and verify parity.

## Why this phase exists

The doctrine should become visible in the repository model and active in the installed runtime environment, not remain source-only.

## Design Extraction

- Source requirement: the new doctrine and touched refinements must become visible across governance layers and active runtime copies
- Derived execution work: update master docs, install new/touched runtime files, and verify source/install parity
- Target outcome: repository and installed runtime state are synchronized

## Flow Diagram

Touched chains are complete
  → update master inventories and history
  → install new and touched runtime files
  → compare source and installed copies
  → synchronized governance and runtime state

## Reviewer Checklist

- [x] `design/design.md` reflects the new chain and touched refinements
- [x] `README.md` reflects the new chain, corrected active count, and corrected install set
- [x] `TODO.md` records the governance wave
- [x] `changelog/changelog.md` records the repository-level wave
- [x] installed runtime copies exist and parity verification passes

## Verification

- master docs updated
- runtime copies installed to `~/.claude/rules/`
- source/install parity verified

## Exit Criteria

- repository-level governance and installed runtime state both reflect the communication-naturalness wave
