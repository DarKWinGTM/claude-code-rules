# P128 — RULES Unified Diagram Doctrine Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P128
> **Status:** Completed / Released
> **Target Release:** v10.36
> **Design References:**
> - [../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md](../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md)
> - [../design/document-governance.design.md](../design/document-governance.design.md)
> - [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md)
> **Patch References:** [../patch/rules-unified-diagram-doctrine-correction.patch.md](../patch/rules-unified-diagram-doctrine-correction.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Normalize RULES around the revised diagram doctrine so the repo treats `diagram/` as a dedicated visual lane, keeps `design/` as textual authority, withdraws fragmented plugin-first assumptions, and opens a governed bootstrap visual anchor at `diagram/STRUCTURE.md`.

---

## Why This Phase Exists

The earlier governed-docs wave assumed diagrams should stay inside `design/**` as companion shards. The user rejected that model and explicitly required a more coherent visual lane closer to the checked NodeClaw pattern.

P128 exists to repair doctrine before implementation continues. The immediate target is not plugin behavior; it is active-owner sync, phase/release-surface alignment, and a bootstrap visual structure surface that matches the revised design basis.

---

## Expected Output

- the revised diagram doctrine is present in checked design/support surfaces inside this worktree
- active document-governance surfaces recognize `diagram/` as a governed visual lane
- inline answer/phase-local diagram formatting stays clearly separate from repository diagram-lane authority
- `diagram/STRUCTURE.md` exists as the top-level whole-repo visual anchor
- active TODO/phase/changelog/patch surfaces close `v10.36 / P128` consistently
- no active current-state surface still presents the fragmented companion assumption as selected truth
- branch/push/release surfaces are updated in the selected outward-facing scope

---

## Action Checklist

- [x] Rewrite the active diagram doctrine around a dedicated `diagram/` visual lane.
- [x] Roll back plugin-side P003 assumptions so plugin is no longer acting as premature doctrine owner.
- [x] Sync active owner surfaces (`document-governance`, related design companions, README, explanation/diagram-boundary docs, TODO, phase, patch, changelog).
- [x] Open `diagram/STRUCTURE.md` as the bootstrap whole-repo visual anchor.
- [x] Run focused diff hygiene and relevant verification for the touched worktree surfaces.
- [x] Re-run runtime install/parity/body-sufficiency proof if touched active runtime files remain inside the install set.
- [x] Reach the push/release action point with explicit approval and update the outward-facing surfaces in the selected scope.

---

## Out of Scope

- reintroducing plugin-governed diagram behavior before doctrine settles
- treating preview/manifest/report output as source truth
- requiring every RULES subject to open a diagram chain immediately
- auto-splitting diagrams because design text already has shards
- executing push/release without explicit approval

---

## Completion Gate

- touched active-owner surfaces consistently distinguish `design/` semantic authority from `diagram/` visual authority
- `diagram/STRUCTURE.md` exists and is bodyful
- no touched active surface still claims the fragmented companion model as selected doctrine
- touched TODO/phase/changelog/patch surfaces align to `v10.36 / P128`
- `git diff --check` passes for the touched worktree changes
- if touched runtime owners remain in the active install set, local install/parity/body-sufficiency proof is rerun and reported
- no push/release is attempted without explicit approval

---

## Current Status

P128 is completed.

Current checked result:
- the revised doctrine spec is written and selected as the active basis for this correction wave
- plugin P003 assumptions were rolled back in the worktree so governed-docs is no longer carrying the premature implementation path
- active owner surfaces now recognize `diagram/` as the dedicated governed visual lane and keep `design/` as semantic authority
- `diagram/STRUCTURE.md` exists as the whole-repo visual anchor
- `git diff --check` passed
- temporary project-local install proof passed with 18 active runtime rule markdown files and parity matched for the touched runtime-owner files `document-governance.md` and `explanation-and-presentation.md`
- the branch was pushed and GitHub release `v10.36` was created in the selected outward-facing scope
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.36
