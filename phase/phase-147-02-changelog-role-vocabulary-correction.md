# Phase 147-02 - Changelog Role Vocabulary Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Parent Phase:** [phase-147-evidence-first-counter-analysis-and-owner-integrity.md](phase-147-evidence-first-counter-analysis-and-owner-integrity.md)
> **Phase ID:** 147-02
> **Status:** Active — candidate cross-surface behavior verified; publication identity pending
> **Target Release:** v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/changelog-role-vocabulary-correction.patch.md](../patch/changelog-role-vocabulary-correction.patch.md)

---

## Objective

Remove undefined changelog repair vocabulary and align startup/repair routing with the active parent, indexed same-chain detail, and inactive reference-history roles.

## Selected Semantic Obligations

1. The active changelog parent owns current version, map, and navigation.
2. Active same-chain version detail belongs under the chain's indexed version-shard path, represented in runtime consumer wording as `changelog/<chain>/v*.changelog.md`.
3. `changelog/done/` is inactive completed/reference/provenance history only when that role applies.
4. No fallback owner, automatic resolution path, or restoration mechanism exists for changelog content.
5. Full doctrine remains owned by unchanged `document-governance.md`; the phase/TODO consumer stays compact.

## Implementation Scope

- `phase-todo-artifact.md` / design / changelog → version `1.33`.
- Master changelog current-authority wording, README vocabulary anchor, Playground Case 09, and matrix cell.

## Out of Scope

- changing `document-governance.md`;
- moving or deleting changelog history;
- creating automatic fallback or restoration behavior;
- normalizing unrelated chains.

## Development Verification / TestKit Coverage

Verification route: `existing_test` through Case 09 plus focused literal/link checks.

Required checks:
- active parent, active detail, and inactive history roles are distinct;
- active runtime/design surfaces contain no stale fallback token;
- master row resolves to the v10.59 detail shard;
- no history is deleted or made active by location alone.

## Current Disposition

- Runtime/design/changelog implementation: implemented.
- Version, active-token, master/playground/link, candidate/canonical/root installation parity, and fresh-public-master checks: passed in candidate scope.
- Annotated tag, GitHub Release identity, and fresh-tag-clone gates: pending.

## Risks and Rollback

- Risk: compact consumer wording can accidentally redefine the canonical chain model.
- Containment: keep full owner doctrine in unchanged `document-governance.md` and verify only synchronized role projection.
- Before publication, revert this triad and its bounded projections only; preserve all history.

## Exit Criteria

- Triad aligns at `1.33`.
- Active owner vocabulary is consistent across selected surfaces.
- No fallback owner appears in active runtime/design behavior.
- Child status becomes `verified` only after full release gates pass.
