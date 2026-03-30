# Phase 005-01 - Harden phase-patch linkage

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 005-01
> **Status:** Implemented - Pending Review
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) + [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/phase-linkage-hardening.patch.md](../patch/phase-linkage-hardening.patch.md)

---

## Objective

Harden the central RULES contract so phased work with governed patch artifacts must declare phase-to-patch linkage explicitly in the live phase workspace.

## Why this phase exists

The repository already had:
- startup artifact ordering strong enough to put phase before patch when needed
- a corrected before/after patch model

But it still left one practical gap:
- patch participation in phased work could remain too implicit in `phase/SUMMARY.md` and child phase files

## Design Extraction

- Source requirement: phased work should keep phase and patch separate while making their relationship explicit when both are in scope
- Derived execution work: tighten `phase-implementation`, reinforce `project-documentation-standards`, update the helper template, and capture the change in patch form
- Target outcome: the live phase workspace becomes explicit enough that patch participation is reviewable rather than implied

## Flow Diagram

phase-first startup behavior already exists
  → identify remaining live linkage gap
  → tighten phase rule
  → reinforce repository verification rule
  → update helper teaching
  → central RULES now teach explicit phase-to-patch linkage

## Reviewer Checklist

- [x] the change stays narrow and does not broaden into a patch/phase rewrite
- [x] `phase-implementation.md` now makes explicit linkage visible when patch is in scope
- [x] `project-documentation-standards.md` now checks explicit phase-to-patch linkage in verification
- [x] `phase-implementation-template.md` teaches the same expectation
- [x] no global reverse-link requirement from patch back to phase was introduced

## Verification

- `phase-implementation.md` explicitly requires live phase-to-patch linkage when patch is in scope
- `project-documentation-standards.md` checks for that linkage
- the helper template teaches that same live-workspace behavior
- the refinement preserves the one-way synthesis boundary

## Exit Criteria

- the central RULES contract now matches the workspace-proven pattern used in `general-expert` and `multi-hat-system`
- phase and patch remain separate roles, but their relationship is now explicit when both are active
