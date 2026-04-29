# Document Changelog & Versions History Control

> **Current Version:** 4.8
> **Design:** [design/document-changelog-control.design.md](design/document-changelog-control.design.md) v4.8
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)

---

## Rule Statement

**Core Principle: Changelogs are the authoritative version/history layer for governed chains; active changelogs keep current version authority and navigation, while `changelog/done/` may hold inactive completed history when active scan surfaces would otherwise become too large.**

---

## Core Contract

### Active changelog authority
Each governed chain keeps one active authoritative changelog.

Required guidance:
- the active changelog owns current version, current index, and forward navigation
- runtime, design, phase, patch, and TODO sync must align to the active changelog version state when applicable
- moving older detail elsewhere must not break the active changelog's ability to explain current authority

### Completed history surface
`changelog/done/` may hold older or completed detailed history when keeping every historical slice in the active scan surface creates unnecessary context bloat.

Required guidance:
- treat `changelog/done/` as inactive-by-default history
- consult `changelog/done/` only for history, audit, rollback, provenance, or trace reconstruction
- keep active changelog pointers/index entries sufficient for navigation when history is moved
- do not use `changelog/done/` as deletion authority or junk classification
- design-specific history belongs under changelog governance, not `design/done/`

### Design pair boundary
Design documents remain active target-state truth. Detailed historical explanation belongs in changelog surfaces, including `changelog/done/` when inactive history separation is needed.

---

## Verification Checklist

- [ ] Active changelog remains the current version authority
- [ ] `changelog/done/` is inactive by default for current-state scans
- [ ] History moved to `changelog/done/` remains reachable when audit/rollback/trace needs it
- [ ] `changelog/done/` is not treated as junk or deletion authorization
- [ ] Design history is not parked under a default `design/done/` pattern

---

## Integration

Related rules:
- [document-design-control.md](document-design-control.md) - active design body and no-default-`design/done/` boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository-wide completed documentation surface model
- [document-patch-control.md](document-patch-control.md) - patch and `patch/done/` history boundary
- [phase-implementation.md](phase-implementation.md) - phase and `phase/done/` history boundary
