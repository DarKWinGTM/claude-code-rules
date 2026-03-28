# Phase 004-02 - Realign Startup Governance

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 004-02
> **Status:** Completed
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) + [../design/phase-implementation.design.md](../design/phase-implementation.design.md) + [../design/todo-standards.design.md](../design/todo-standards.design.md) + [../design/strict-file-hygiene.design.md](../design/strict-file-hygiene.design.md)
> **Patch References:** n/a

---

## Objective

Patch the existing governance-owner chains so they defer startup timing to `artifact-initiation-control`.

## Why this phase exists

Without dependent updates, the new owner would exist but the repository would still behave as if startup artifact establishment were optional or blocked by hygiene.

## Design Extraction

- Source requirement: repository-wide startup behavior must be routed through one semantic owner rather than staying fragmented across passive role models and hygiene restrictions
- Derived execution work: update project-documentation-standards, phase-implementation, todo-standards, and strict-file-hygiene to point to the new startup contract
- Target outcome: startup artifact-first behavior is integrated into the existing governance ecosystem

## Flow Diagram

New startup owner exists
  → patch repository role model
  → patch phase startup bridge
  → patch TODO startup behavior
  → patch hygiene deference boundary
  → dependent owners stop contradicting startup governance

## Reviewer Checklist

- [x] `project-documentation-standards` routes startup posture to the new owner
- [x] `phase-implementation` opens `/phase` before drift when warranted
- [x] `todo-standards` distinguishes early establishment from later TODO updates
- [x] `strict-file-hygiene` no longer blocks required governed startup artifacts

## Verification

- touched owner chains reference `artifact-initiation-control`
- TODO chain is fully normalized if touched
- startup gate wording is consistent across the touched chains

## Exit Criteria

- no touched owner chain silently weakens the new startup contract
- startup governance is integrated rather than isolated
