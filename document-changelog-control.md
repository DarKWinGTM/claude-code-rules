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

Each governed chain keeps one active authoritative changelog. It owns current version, current index, and forward navigation; runtime, design, phase, patch, and TODO sync align to its version state when applicable. Changelog records shipped/synchronized history and version authority; it should not become phase-definition storage or duplicate active design target-state truth.

`changelog/done/` may hold older/completed detailed history when active scans would otherwise bloat. It is inactive by default, used only for history/audit/rollback/provenance/trace reconstruction, and never deletion authority or junk classification. The active changelog must keep enough pointers/index entries for moved history to remain reachable and must still explain current authority after detail is moved out of the active scan surface.

Design documents remain active target-state truth. Detailed historical explanation, including design-specific history, belongs under changelog governance and may use `changelog/done/`; do not park it under a default `design/done/` pattern.

---

## Verification Checklist

- [ ] Active changelog remains current version/index/navigation authority.
- [ ] `changelog/done/` is inactive history, reachable when audit/rollback/trace needs it, and never junk/deletion authority.
- [ ] Design history is kept under changelog governance, not default `design/done`.

---

## Integration

Related rules:
- [document-design-control.md](document-design-control.md) - active design body and no-default-`design/done/` boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository-wide completed documentation surface model
- [document-patch-control.md](document-patch-control.md) - patch and `patch/done/` history boundary
- [phase-implementation.md](phase-implementation.md) - phase and `phase/done/` history boundary
