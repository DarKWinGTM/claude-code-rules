# Semantic Code Naming and Code-Doc Comment Linkage Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/coding-discipline.design.md](../design/coding-discipline.design.md) v1.2
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P138 wave.

It packages one bounded doctrine refinement: code should use semantic/domain/behavior-first identifiers, and source comments that point to governed docs should stay bounded, useful, and maintainable rather than becoming duplicate documentation or stale authority links.

---

## Analysis

Before this wave:
- code-comment discipline already preferred useful explanation over syntax narration
- governed documents already owned design, phase, patch, changelog, and integrity surfaces
- source comments could still drift into either over-documenting implementation or carrying stale governed-doc references
- source identifiers could still depend too much on comments or nearby docs to reveal domain meaning and behavior

The better posture is:
- code names should first carry implementation role, domain meaning, and behavior
- comments should explain what code cannot express cleanly, including bounded references to governed docs only when that lowers maintenance risk
- governed docs remain durable authority surfaces; source comments remain local implementation context or signposts
- governed-doc citations in source comments are treated as checked references that need update or removal when the cited path, section, role, or nearby behavior changes

This patch is intentionally bounded to the P138 doctrine/release slice only.

---

## Change Items

### 1) Coding discipline sync

- **Target artifacts:** `coding-discipline.md`, `design/coding-discipline.design.md`, `changelog/coding-discipline.changelog.md`
- **Change type:** released doctrine refinement
- **Current state:** coding doctrine implied semantic naming and useful comments, but did not explicitly reject governance artifact IDs in ordinary identifiers or define bounded governed-doc comment linkage.
- **Target state:** coding doctrine now requires semantic/domain/behavior-first identifiers and bounded source-comment linkage to governed docs.
- **Review point:** coding comments remain clarity aids and do not replace clearer names or governed documentation.

### 2) Document governance sync

- **Target artifacts:** `document-governance.md`, `design/document-governance.design.md`, `changelog/document-governance.changelog.md`
- **Change type:** released doctrine refinement
- **Current state:** document-role doctrine already separated major owner surfaces, but source-comment linkage was not yet explicit as a bounded local explanation/signpost layer.
- **Target state:** document governance now records that design, phase, patch, changelog, and source comments keep separate roles while source comments do not become naming authority or parallel doc bodies.
- **Review point:** design, phase, patch, changelog, and source comments keep separate owner roles.

### 3) Document integrity sync

- **Target artifacts:** `document-integrity.md`, `design/document-integrity.design.md`, `changelog/document-integrity.changelog.md`
- **Change type:** released doctrine refinement
- **Current state:** governed-doc citations inside source comments could still be treated as incidental local text instead of maintained references.
- **Target state:** document integrity now requires governed-doc citations in source comments to be updated or removed when referenced paths, headings, owner roles, or nearby behavior change.
- **Review point:** stale source-comment citations are treated as reference drift, not harmless local text.

### 4) Release-surface sync

- **Target artifacts:** `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-138-semantic-code-naming-and-code-doc-comment-linkage.md`, `patch/semantic-code-naming-and-code-doc-comment-linkage.patch.md`, `changelog/changelog.md`, `changelog/changelog/v10.46-released-semantic-code-naming-and-code-doc-comment-linkage.changelog.md`
- **Change type:** release synchronization
- **Current state:** released baseline was `v10.45 / P137`, while P138 existed only as an open wave in the authoring workspace.
- **Target state:** release/current-state surfaces now align to one promoted `v10.46 / P138` baseline.
- **Review point:** release wording must match real install, parity, branch/default-branch, tag, and GitHub release evidence.

---

## Verification

Required checks before release closeout:
- semantic/domain/behavior-first naming doctrine is visible in the touched coding owner and companion surfaces
- bounded governed-doc source-comment linkage is visible across the touched coding/document-governance/document-integrity owners
- README/TODO/phase/patch/master-changelog/version-detail surfaces align to `v10.46 / P138`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is committed, pushed to `master`, tagged, and GitHub release verification passes

---

## Implementation Status

P138 is completed.

The touched doctrine owners now require semantic/domain/behavior-first code naming and bounded governed-doc source-comment linkage, the touched owner-chain and release surfaces are synchronized to `v10.46 / P138`, touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope, and the selected scope was published through a bounded release path with push/tag/release verification.
