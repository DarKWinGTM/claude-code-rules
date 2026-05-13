# Document Changelog & Versions History Control

> **Current Version:** 4.12
> **Design:** [design/document-changelog-control.design.md](design/document-changelog-control.design.md) v4.12
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)

---

## Rule Statement

**Core Principle: Changelogs are the authoritative version/history layer for governed chains; active parent changelogs keep current version authority and navigation, chain-scoped version detail shards hold large same-chain version entries when needed, `changelog/done/` remains legacy/archive/fallback history, and daily TODO/phase rollover stays with its dedicated owner.**

---

## Core Contract

Each governed chain keeps one active authoritative parent changelog. It owns current version, current index, shard map when present, and forward navigation. Runtime, design, phase, patch, and TODO sync align to the parent changelog version state when applicable. Changelog records shipped/synchronized history and version authority; it should not become phase-definition storage, duplicate active design target-state truth, or serve as README current-state content.

Large governed chains may split detailed version sections into chain-scoped version detail shards under `changelog/<chain>/vX.YY-short-topic.changelog.md`. The parent changelog must keep current version authority, a readable version index, and links to any shards that hold detailed entries. A shard must identify or clearly fit the parent chain, link back to the parent, and remain a detail surface for that parent. A shard is not a second version authority, a phase file, a TODO tracker, or a standalone release record.

`changelog/done/` remains allowed for legacy, archive, completed-history, or explicit fallback cases where chain-scoped version shards are not the right shape. It is inactive by default, used only for history/audit/rollback/provenance/trace reconstruction, and never deletion authority or junk classification. The active parent changelog must keep enough pointers/index entries for moved or sharded history to remain reachable and must still explain current authority after detail leaves the active scan surface.

Daily-first rollover for `TODO.md` and `phase/SUMMARY.md` is owned by `governed-document-rollover-control.md`; changelog history remains version authority and should not absorb TODO/phase daily movement by default. Design documents remain active target-state truth. README remains the current-state front page for overview, install, active count, latest refinement, and quality signals; detailed version timelines belong in changelog governance, not README release-sync dumps.

---

### Chain-Scoped Version Detail Shards

Use chain-scoped version detail shards when a changelog needs to preserve detailed version entries but the active parent is becoming expensive to read, edit, or verify.

Required guidance:
- keep `changelog/<chain>.changelog.md` as the current version authority, index, and navigation surface
- place same-chain detailed entries in `changelog/<chain>/vX.YY-short-topic.changelog.md` when sharding is needed
- use self-identifying shard filenames that include the version and a short topic
- keep parent-to-shard and shard-to-parent links resolvable
- keep one version detail entry in one active shard or in the parent, not duplicated as competing authority
- preserve exact historical content during migration unless an explicit governed rewrite is selected
- do not create a God directory where the parent no longer tells readers which shard owns which version detail

---

### Changelog God-file prevention

A changelog becomes a God file when current version authority turns into phase planning, design target-state storage, TODO tracking, release dashboarding, or detailed history that makes the active changelog hard to scan.

Required guidance:
- keep the active parent changelog as current version, index, shard map, and navigation authority
- move bulky same-chain version detail into chain-scoped version shards when active scans bloat
- use `changelog/done/` only for legacy, archive, completed-history, or explicit fallback cases
- keep design target state in design, phase execution in phase, TODO tracking in TODO, and current front-page status in README
- avoid appending release prose that duplicates active README, TODO, phase, or patch content

## Verification Checklist

- [ ] Active parent changelogs avoid God-file overload by moving bulky same-chain version detail into reachable chain-scoped shards when needed.
- [ ] Parent changelogs remain current version/index/shard-map/navigation authority.
- [ ] Version detail shards link back to their parent and do not become separate version authorities.
- [ ] `changelog/done/` is legacy/archive/fallback history, reachable when audit/rollback/trace needs it, and never junk/deletion authority.
- [ ] Changelog history remains separate from daily TODO/phase rollover history and does not replace `TODO.md` or `phase/SUMMARY.md` active entrypoints.
- [ ] Design history is kept under changelog governance, not default `design/done`.

---

## Integration

Related rules:
- [document-design-control.md](document-design-control.md) - active design body and no-default-`design/done` boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository-wide document-role model and changelog shard surface classification
- [document-patch-control.md](document-patch-control.md) - patch and `patch/done/` history boundary
- [phase-implementation.md](phase-implementation.md) - phase, `phase/history/`, and `phase/done/` history boundary
- [document-consistency.md](document-consistency.md) - parent/shard link, version, and no-drift checks
- [safe-file-reading.md](safe-file-reading.md) - parent-first changelog reads and selective shard reads
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - daily-first TODO/phase active-entrypoint rollover boundary
