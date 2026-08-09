# Changelog Role Vocabulary Correction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active — candidate verification and installation complete; publication identity pending
> **Target Design:** [../design/design.md](../design/design.md) v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

`phase-todo-artifact.md` used an undefined changelog fallback token even though governed changelog doctrine already distinguishes the active parent, indexed same-chain detail, and inactive `done/` history.

## 2) Analysis

Risk: Medium. Undefined owner vocabulary can route content into an imagined path or make inactive history sound like an active fallback/restoration source.

Selected owner model:
- active parent → current version, map, navigation;
- active same-chain detail → indexed chain version shard (`changelog/<chain>/v*.changelog.md` as portable consumer notation);
- inactive completed/reference history → `changelog/done/` when applicable;
- no fallback owner or automatic resolution path.

## 3) Change Items

### CRV-001 - Runtime consumer correction
- **Target:** `../phase-todo-artifact.md` and triad.
- **Before:** bulky version history routes to an undefined fallback concept.
- **After:** active same-chain detail and inactive reference history route to their real owners; full doctrine remains with unchanged `document-governance.md`.

### CRV-002 - Master current-authority wording
- **Target:** `../changelog/changelog.md` current-version authority section.
- **Before:** active detail is described as superseded and archive history as fallback.
- **After:** current parent, indexed active detail, and inactive legacy/reference history are distinct without fallback semantics.

### CRV-003 - Scenario and front-page projection
- **Target:** Case 09, matrix, and surgical README vocabulary anchor.
- **After:** user-facing/current-state wording matches the governed owner split.

## 4) Verification

Candidate checks:
- phase/TODO triad aligns at `1.33`;
- active runtime/design surfaces contain no stale fallback token;
- master v10.59 row resolves to its detail shard;
- Case 09 proves parent/detail/done separation;
- no history is moved, deleted, or activated by location alone.

Candidate owner-vocabulary, link, canonical/root installation, and fresh-public-master checks pass. Release proof remains pending until the annotated tag, GitHub Release identity, and fresh-tag-clone gates pass.

## 5) Rollback Approach

Before publication, revert only this triad and bounded wording projections. Never delete or disconnect reachable changelog history as rollback. After publication, use a later corrective release.
