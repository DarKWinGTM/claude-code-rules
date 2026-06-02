# P131 — RULES Diagram Infrastructure Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P131
> **Status:** Completed / Released
> **Target Release:** v10.39
> **Design References:**
> - [../design/design.md](../design/design.md) v10.35
> - [../design/document-governance.design.md](../design/document-governance.design.md) v1.13
> **Patch References:** [../patch/rules-diagram-infrastructure-doctrine.patch.md](../patch/rules-diagram-infrastructure-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so diagram documentation becomes required governed-docs infrastructure rather than an optional visual companion lane. `diagram/` should become the only governed diagram authority family, `diagram/STRUCTURE.md` should become the mandatory compact active whole-project diagram-side entrypoint, and diagram docs should remain subordinate to `design/**` semantics while preserving future `history/` / `done/` as preservation infrastructure rather than cleanup.

---

## Why This Phase Exists

The released P128/P129 model already established a governed diagram lane and made governed source mandatory Kroki-compatible, but it still treated the lane as conditional and had not yet turned the good observed document pattern into explicit RULES infrastructure doctrine.

The selected next step is stricter and more structural:
- diagram docs are no longer an optional companion family
- governed diagram authority stays under `diagram/` only
- `diagram/STRUCTURE.md` becomes the required diagram-side project map
- child diagrams remain zoom-in / decomposition views rather than unrelated fragments
- future `diagram/history/` / `diagram/done/` remain preservation infrastructure rather than cleanup paths

P131 exists to make that infrastructure model explicit in active RULES doctrine and then close the wave through source sync, runtime install parity, branch/default-branch alignment, and GitHub release verification.

---

## Expected Output

- `document-governance.md` teaches that `diagram/` is required governed-docs infrastructure for RULES
- `document-governance.md` teaches that governed diagram authority is `diagram/`-scoped only
- `document-governance.md` teaches that `diagram/STRUCTURE.md` is mandatory as the compact active diagram-side entrypoint
- `document-governance.md` teaches that `diagram/STRUCTURE.md` owns whole-project concept mapping, source/folder topology mapping, authority-boundary explanation, and diagram-to-diagram navigation
- `design/document-governance.design.md` carries the P131 target-state refinement
- `changelog/document-governance.changelog.md` records Version 1.13 / P131
- `docs/superpowers/specs/2026-06-02-rules-diagram-infrastructure-doctrine.md` exists as the route-driving doctrine spec
- `diagram/STRUCTURE.md` exists as the active whole-project diagram-side authority surface and states the current doctrine posture directly
- touched README/changelog/TODO/phase/patch surfaces align to `v10.39 / P131`
- runtime install/update verification, parity/body-sufficiency verification, `git diff --check`, push/default-branch verification, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Open P131 as the infrastructure refinement wave on top of the released `v10.38 / P130` baseline.
- [x] Tighten `document-governance.md` so `diagram/` becomes required RULES infrastructure, diagram authority stays `diagram/`-scoped, and `diagram/STRUCTURE.md` becomes mandatory/bodyful.
- [x] Tighten `design/document-governance.design.md` with the P131 target-state refinement.
- [x] Tighten `changelog/document-governance.changelog.md` to record Version 1.13 / P131.
- [x] Add the P131 infrastructure spec at `docs/superpowers/specs/2026-06-02-rules-diagram-infrastructure-doctrine.md`.
- [x] Add and sync `diagram/STRUCTURE.md` as the active diagram-side whole-project entrypoint.
- [x] Sync touched README/changelog/TODO/phase/patch surfaces to `v10.39 / P131`.
- [x] Re-install/update the active runtime rules into `~/.claude/rules` and verify parity/body sufficiency for the touched active runtime owners.
- [x] Run `git diff --check` clean for the selected P131 scope.
- [x] Commit the selected P131 scope, verify remote `master`, publish GitHub release `v10.39`, and finalize closeout records.

---

## Out of Scope

- making diagram docs semantic authority over `design/**`
- reopening unrelated plugin or governed-docs implementation work
- forcing every possible subsystem to immediately open its own child diagram file
- treating future `diagram/history/` / `diagram/done/` as cleanup/disposal surfaces
- widening the active runtime install set beyond the current owned active runtime rules
- bundling unrelated dirty/untracked repo state into the P131 release wave

---

## Completion Gate

- `diagram/` is explicitly required governed-docs infrastructure for RULES
- governed diagram authority is explicitly `diagram/`-scoped only
- `diagram/STRUCTURE.md` is mandatory and bodyful rather than a shallow router
- `diagram/STRUCTURE.md` owns concept/folder/topology/boundary/navigation mapping
- `design/**` remains semantic authority if text and diagram differ
- future `diagram/history/` / `diagram/done/` are preservation infrastructure rather than cleanup authority
- touched README/changelog/TODO/phase/patch surfaces align to `v10.39 / P131`
- runtime install/update verification and body-sufficiency/parity checks pass in checked scope
- `git diff --check`, branch/default-branch verification, and GitHub release verification pass

---

## Current Status

P131 is completed.

Current checked progress:
- the target source path now carries the P131 doctrine in the runtime owner, design companion, owner changelog, doctrine spec, and `diagram/STRUCTURE.md`
- `diagram/STRUCTURE.md` now states the current doctrine posture directly and acts as the active whole-project diagram-side entrypoint
- touched README/changelog/TODO/phase/patch surfaces are aligned to `v10.39 / P131`
- runtime install/update verification passed for the current active runtime rule set with checked parity/body sufficiency in scope
- `git diff --check`, push/update to remote `master`, GitHub release verification, and final closeout alignment passed
