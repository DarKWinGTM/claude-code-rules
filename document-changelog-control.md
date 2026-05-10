# Document Changelog & Versions History Control

> **Current Version:** 4.11
> **Design:** [design/document-changelog-control.design.md](design/document-changelog-control.design.md) v4.11
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)

---

## Rule Statement

**Core Principle: Changelogs are the authoritative version/history layer for governed chains; active changelogs keep current version authority and navigation, while `changelog/done/` may hold inactive completed history when active scan surfaces would otherwise become too large and daily TODO/phase rollover stays with its dedicated owner.**

---

## Core Contract

Each governed chain keeps one active authoritative changelog. It owns current version, current index, and forward navigation; runtime, design, phase, patch, and TODO sync align to its version state when applicable. Changelog records shipped/synchronized history and version authority; it should not become phase-definition storage, duplicate active design target-state truth, or serve as README current-state content.

`changelog/done/` may hold older/completed detailed history when active scans would otherwise bloat. It is inactive by default, used only for history/audit/rollback/provenance/trace reconstruction, and never deletion authority or junk classification. The active changelog must keep enough pointers/index entries for moved history to remain reachable and must still explain current authority after detail is moved out of the active scan surface. Daily-first rollover for `TODO.md` and `phase/SUMMARY.md` is owned by `governed-document-rollover-control.md`; changelog history remains version authority and should not absorb TODO/phase daily movement by default.

Design documents remain active target-state truth. README remains the current-state front page for overview, install, active count, latest refinement, and quality signals; detailed version timelines belong in changelog instead of README release-sync dumps. Detailed historical explanation, including design-specific history, belongs under changelog governance and may use `changelog/done/`; do not park it under a default `design/done/` pattern.

---

### Changelog God-file prevention

A changelog becomes a God file when current version authority turns into phase planning, design target-state storage, TODO tracking, release dashboarding, or detailed history that makes the active changelog hard to scan.

Required guidance:
- keep the active changelog as current version, index, and navigation authority
- move older or bulky completed history into `changelog/done/` when active scans bloat
- keep design target state in design, phase execution in phase, TODO tracking in TODO, and current front-page status in README
- avoid appending release prose that duplicates active README, TODO, phase, or patch content

## Verification Checklist
- [ ] Active changelog avoids God-file overload by keeping detailed completed history in reachable inactive history when needed.

- [ ] Active changelog remains current version/index/navigation authority.
- [ ] README current-state sync is not replaced by changelog timeline dumping.
- [ ] `changelog/done/` is inactive history, reachable when audit/rollback/trace needs it, and never junk/deletion authority.
- [ ] Changelog history remains separate from daily TODO/phase rollover history and does not replace `TODO.md` or `phase/SUMMARY.md` active entrypoints.
- [ ] Design history is kept under changelog governance, not default `design/done`.

---

## Integration

Related rules:
- [document-design-control.md](document-design-control.md) - active design body and no-default-`design/done/` boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository-wide completed documentation surface model
- [document-patch-control.md](document-patch-control.md) - patch and `patch/done/` history boundary
- [phase-implementation.md](phase-implementation.md) - phase, `phase/history/`, and `phase/done/` history boundary
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - daily-first TODO/phase active-entrypoint rollover boundary
