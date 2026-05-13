# P096-01 — Changelog Chain Version Detail Shards

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P096-01
> **Status:** Active / In Progress
> **Target Release:** v10.04
> **Design References:**
> - [../design/design.md](../design/design.md) v10.04
> - [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md) v4.12
> - [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) v2.41
> - [../design/document-consistency.design.md](../design/document-consistency.design.md) v1.15
> - [../design/safe-file-reading.design.md](../design/safe-file-reading.design.md) v1.8
> - [../design/context-load-and-document-density-control.design.md](../design/context-load-and-document-density-control.design.md) v1.6
> **Patch References:** [../patch/changelog-chain-version-detail-shards.patch.md](../patch/changelog-chain-version-detail-shards.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make Main RULES support compact active changelog parents with chain-scoped version detail shards.

The target behavior is:
- `changelog/<chain>.changelog.md` remains the current version authority and navigation index
- `changelog/<chain>/vX.YY-short-topic.changelog.md` stores detailed version entries for that chain
- `changelog/done/` remains allowed only as legacy, archive, or explicit fallback history, not the default large-chain split path

---

## Why This Phase Exists

Large changelog chains can become God files when current version authority, detailed historical entries, verification notes, and release movement all accumulate in one active file.

P096-01 changes the doctrine so large chains split by chain-owned version detail shards instead of pushing ordinary version detail into a generic `changelog/done/` bucket.

This keeps current changelog reads cheap while preserving exact version history and reviewable parent-to-shard navigation.

---

## Expected Output

- `document-changelog-control` defines the preferred parent-index plus chain-scoped version-shard model.
- Adjacent documentation, consistency, safe-reading, and density owners know how to read, validate, and repair that model.
- Master README, design, changelog, TODO, phase, and patch records align to `v10.04 / P096-01`.
- Runtime install copied only the 47 README-listed active runtime rules.
- No existing project changelog migration is included in this first doctrine wave.

---

## Action Checklist

- [x] Preflight current `v10.03 / P095` baseline, 47 active runtime count, `master`/`origin` alignment, GitHub auth, and absent `v10.04` release.
- [x] Open P096-01 phase and patch records.
- [x] Update changelog parent/shard doctrine in owner runtime, design, and changelog surfaces.
- [x] Sync adjacent document standards, consistency, safe-reading, and density owner chains where their runtime behavior changes.
- [x] Sync master README, design, changelog, TODO, phase, and patch records.
- [x] Validate 47-file README install arrays, source body sufficiency, parent/shard semantics, links, and density boundaries.
- [x] Install only README-listed active runtime rules to the runtime rules directory.
- [x] Verify 47/47 source/runtime parity and source/destination body sufficiency.
- [ ] Commit, push `master`, create GitHub release `v10.04`, and verify tag/release state.
- [ ] Close P096-01 records only after release verification passes.

---

## Out of Scope

- Migrating existing project or master changelog history into shards in this phase.
- Deleting `changelog/done/` or any completed history.
- Changing active runtime rule count.
- Installing design, changelog, TODO, phase, patch, support, helper, or plugin artifacts as runtime rules.
- Claiming full master governance density rollover completion.

---

## Completion Gate

- Source docs are synchronized for `v10.04 / P096-01`.
- Parent changelog files remain current version authority and index surfaces.
- Chain-scoped version shards are documented as detail surfaces, not independent authorities.
- `changelog/done/` is documented as legacy/archive/fallback rather than the default large-chain split path.
- README Bash and PowerShell install arrays still define exactly 47 matching active runtime files.
- Source/runtime parity and active runtime body sufficiency pass for 47/47 files.
- Touched active docs pass density and God-artifact review.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- `master` push and GitHub release `v10.04` verification pass.

---

## Rollback / Containment

If P096-01 is reversed:
- revert the `v10.04` changelog-sharding doctrine as one governed rollback
- restore prior parent/done changelog wording from `v10.03`
- reinstall the prior 47-file runtime set only under an explicit rollback gate
- do not delete version history, `changelog/done/`, future shard directories, phase records, patch records, or runtime destination extras as cleanup

---

## Current Status

P096-01 is active.

Completed:
- preflight confirmed the `v10.03 / P095` baseline and absent `v10.04` release
- phase and patch startup artifacts are opened
- changelog parent/detail-shard doctrine is implemented in the owner chain
- project documentation, consistency, safe-reading, and density owner chains are synchronized
- README, master design, master changelog, TODO, phase, and patch records are synchronized to active/pre-release `v10.04 / P096-01` state

Pending:
- density/God-artifact review closeout
- commit, push, release, and release-verified closeout
