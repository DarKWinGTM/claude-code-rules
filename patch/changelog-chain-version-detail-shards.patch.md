# Changelog Chain Version Detail Shards Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/document-changelog-control.design.md](../design/document-changelog-control.design.md) v4.12
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is a governance-only patch for `v10.04 / P096-01`.

It changes the changelog-history split model for large governed chains. The new preferred model is a compact active parent changelog plus chain-scoped version detail shards:

```text
changelog/
  <chain>.changelog.md
  <chain>/
    vX.YY-short-topic.changelog.md
```

The parent remains current version authority and navigation. Version shards store detailed entries for that same chain. `changelog/done/` remains an allowed legacy/archive/fallback surface, not the default split target for ordinary large-chain version detail.

---

## Analysis

Current RULES doctrine already prevents changelog God files, but it routes older or bulky completed history primarily to `changelog/done/`.

That keeps active scans smaller, but it can blur chain ownership for ordinary version detail because a generic done bucket is not as direct as a chain-local shard directory.

The target model keeps three boundaries clear:
- current authority stays in `changelog/<chain>.changelog.md`
- detailed version history stays near the owning chain in `changelog/<chain>/`
- generic completed or legacy history stays in `changelog/done/` only when explicitly selected

No existing changelog content is migrated by this patch. This patch updates doctrine and verification behavior first.

---

## Change Items

### 1) Changelog owner chain

- **Target artifact:** `document-changelog-control.md`, `design/document-changelog-control.design.md`, `changelog/document-changelog-control.changelog.md`
- **Change type:** replacement and additive doctrine
- **Current state:** large changelog history is allowed to move to `changelog/done/` when active scans bloat.
- **Target state:** large chains should prefer `changelog/<chain>/vX.YY-short-topic.changelog.md` detail shards, while the parent changelog remains current version authority and index.
- **Review point:** ensure version shards are detail surfaces and cannot become separate version authority.

### 2) Project documentation standards

- **Target artifact:** `project-documentation-standards.md` and design/changelog companions if runtime behavior changes
- **Change type:** additive document-role entry and boundary refinement
- **Current state:** required document set names active changelogs and `changelog/done/`, but not chain-scoped version detail shards.
- **Target state:** document set recognizes `changelog/<chain>/v*.changelog.md` as same-chain version detail shards and keeps `changelog/done/` as legacy/archive/fallback.
- **Review point:** runtime install scope must remain the 47 README-listed root rules only.

### 3) Consistency, reading, and density owners

- **Target artifact:** `document-consistency.md`, `safe-file-reading.md`, `context-load-and-document-density-control.md`, plus design/changelog companions where touched
- **Change type:** additive validation and reading guidance
- **Current state:** consistency and reading rules cover changelog/done and broad governance reads, but not a parent-to-version-shard model.
- **Target state:** parent indexes are read first, selected version shards are read only when needed, shard links are verified, and God-directory drift is blocked.
- **Review point:** no no-drift or release-ready claim is valid if parent/shard links, current-version mapping, or shard authority boundaries are unresolved.

### 4) Master release surfaces and runtime install

- **Target artifact:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P096-01 phase record, this patch record, and runtime rules destination
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.03 / P095` as released.
- **Target state:** master surfaces identify `v10.04 / P096-01`, runtime install copies the same 47 active rules, and source/runtime parity plus body sufficiency pass.
- **Review point:** do not claim release completion before push and GitHub release verification pass.

---

## Implementation Status

Source doctrine sync is implemented for the owner chains:
- `document-changelog-control` v4.12
- `project-documentation-standards` v2.41
- `document-consistency` v1.15
- `safe-file-reading` v1.8
- `context-load-and-document-density-control` v1.6

Master source records are synchronized to active/pre-release `v10.04 / P096-01` state.

Validation, runtime install, and 47/47 source/runtime parity plus source/destination body sufficiency passed. Pending gates remain density/God-artifact review closeout, push, and GitHub release `v10.04` verification.

---

## Verification

Required checks before release:
- README Bash and PowerShell install arrays contain exactly the same 47 active runtime rule files.
- All 47 source root runtime files have substantive active bodies.
- Runtime install copies only README-listed active runtime rules.
- Source/runtime parity passes for 47/47 files.
- Parent changelog plus version-shard doctrine is present in touched owner chains.
- `changelog/done/` is still allowed as legacy/archive/fallback and is not treated as deletion or migration authority.
- Touched active docs pass density and God-artifact review.
- GitHub push and release `v10.04` verification pass.

---

## Rollback Approach

Revert the `v10.04 / P096-01` doctrine edits as one governed rollback if the parent/shard model is not accepted.

Rollback must preserve existing history and must not delete `changelog/done/`, future chain shard directories, phase records, patch records, or runtime destination extras.

If runtime install already happened, reinstall the prior 47-rule runtime set only under an explicit rollback gate.
