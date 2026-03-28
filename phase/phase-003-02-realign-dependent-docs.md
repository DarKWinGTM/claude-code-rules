# Phase 003-02 - Realign Dependent Docs

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 003-02
> **Status:** Completed
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/document-patch-control.design.md](../design/document-patch-control.design.md) + [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) + [../design/phase-implementation.design.md](../design/phase-implementation.design.md)
> **Patch References:** n/a

---

## Objective

Realign the dependent governance docs so they all reference the corrected patch model consistently.

## Why this phase exists

Even after the patch rule is fixed, the repository still becomes confusing if README, master design, phase helper, and related cross-cutting rules continue to teach old `patches/` or generic `patch.md` wording.

## Design Extraction

- Source requirement: repository-wide governed docs must teach one deterministic patch model without conflicting location or meaning rules
- Derived execution work: update README, master design, phase helper, phase rule, and adjacent governance docs that still referenced the older patch model
- Target outcome: no active documentation layer contradicts the new patch concept

## Flow Diagram

Patch rule is corrected
  → scan dependent governance docs
  → replace stale active patch wording
  → preserve historical references only in history layers
  → repository-level patch teaching becomes consistent

## Reviewer Checklist

- [x] README reflects the active patch model
- [x] master design reflects the active patch model
- [x] phase rule and helper consume the corrected patch-artifact model
- [x] cross-cutting support docs no longer teach old active patch placement

## Verification

- active docs reference `patch/<context>.patch.md` or root `<context>.patch.md`
- active docs no longer teach generic `patch.md`
- old `patches/` references are limited to historical records and migration notes

## Exit Criteria

- active repo docs are internally consistent on patch meaning and placement
- remaining legacy wording is historical only
