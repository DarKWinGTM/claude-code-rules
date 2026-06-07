# P142 — Phase Authoring Template Relocation and Runtime Boundary

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P142
> **Status:** Completed / Released
> **Target Release:** v10.50
> **Design References:**
> - [../design/document-governance.design.md](../design/document-governance.design.md) v1.15
> - [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md) v2.44
> - [../design/document-patch-control.design.md](../design/document-patch-control.design.md) v2.10
> **Patch References:** [../patch/phase-authoring-template-relocation-and-runtime-boundary.patch.md](../patch/phase-authoring-template-relocation-and-runtime-boundary.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Relocate the old phase authoring helper out of the RULES root into `template/phase-authoring-template.md`, make its support-only/non-runtime/non-authority role explicit, and remove the root-level ambiguity that made it look like an active phase Rule.

---

## Why This Phase Exists

The repo currently has one file whose placement sends the wrong signal:
- `phase-implementation-template.md` lives beside active runtime Rule files in the root active product surface
- but it is not a runtime Rule
- and the real active phase doctrine already lives elsewhere

That mismatch creates two problems:
- readers cannot tell whether the file is a real Rule or only a drafting scaffold
- phase doctrine ownership looks split or ambiguous even though runtime behavior already belongs to `phase-todo-artifact.md` plus governed `phase/` surfaces

P142 fixes the placement, naming, and boundary story together without promoting the whole template into runtime.

---

## Expected Output

- `phase-implementation-template.md` is removed from the RULES root
- `template/phase-authoring-template.md` exists as the canonical support-only template path
- current-state docs no longer make the template read like an active Rule
- active phase doctrine location is explicit: `phase-todo-artifact.md` plus governed `phase/` surfaces
- touched runtime/design/changelog/TODO/phase/patch surfaces align to one `v10.50 / P142` baseline once release verification completes

---

## Action Checklist

- [x] Relocate and rename the template into the dedicated `template/` directory.
- [x] Update current-state runtime/design/diagram references so the template no longer reads like a root Rule.
- [x] Sync `TODO.md`, `phase/SUMMARY.md`, this phase file, and `patch/phase-authoring-template-relocation-and-runtime-boundary.patch.md`.
- [x] Sync `changelog/changelog.md` and `changelog/changelog/v10.50-released-phase-authoring-template-relocation-and-runtime-boundary.changelog.md`.
- [x] Complete final verification, install, publish, tag, and release evidence.

---

## Out of Scope

- promoting the full template into the active runtime payload
- broad phase-doctrine rewrites unrelated to this placement/boundary issue
- rewriting historical provenance references only because the path changed
- unrelated plugin or non-RULES waves

---

## Completion Gate

- the relocated template no longer reads like an active Rule
- current-state references now point to `template/phase-authoring-template.md` where active authority requires the new path
- runtime install scope remains correct and does not accidentally absorb the template into the active payload
- touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces align to `v10.50 / P142`
- touched runtime-owner install/update verification, source/runtime parity, body sufficiency, `git diff --check`, push/update to `master`, tag, and GitHub release verification all pass

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is governed doctrine/current-state/runtime-boundary work only.
- **Checks run:** active-reference verification, runtime/install-scope verification, source/runtime parity for touched runtime owners, `git diff --check`, push to `master`, tag verification, and GitHub release verification.
- **Confidence:** released and verified in the checked doctrine scope.

---

## Current Status

P142 is completed.

Current checked progress:
- the template has been moved out of the root active product surface into `template/phase-authoring-template.md`
- current-state runtime/design/diagram references no longer point to the old root path in checked active surfaces
- `document-governance.md` now classifies template-directory support artifacts as non-governed unless promoted
- TODO/phase/patch/master-changelog/detail surfaces align to `v10.50 / P142`, touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency, `git diff --check` passed, and push to `master`, tag `v10.50`, and GitHub release verification passed
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.50
