# P138 — Semantic Code Naming and Code-Doc Comment Linkage

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P138
> **Status:** Completed / Released
> **Target Release:** v10.46
> **Design References:**
> - [../design/coding-discipline.design.md](../design/coding-discipline.design.md) v1.2
> - [../design/document-governance.design.md](../design/document-governance.design.md) v1.14
> - [../design/document-integrity.design.md](../design/document-integrity.design.md) v1.8
> **Patch References:** [../patch/semantic-code-naming-and-code-doc-comment-linkage.patch.md](../patch/semantic-code-naming-and-code-doc-comment-linkage.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make semantic/domain/behavior-first code naming and bounded code-to-governed-doc comment linkage the released P138 baseline.

---

## Why This Phase Exists

P138 closes one bounded coding-doctrine gap:
- `coding-discipline.md` now requires semantic/domain/behavior-first identifiers so implementation names expose role and behavior before comments have to compensate.
- `document-governance.md` now reinforces that design, phase, patch, changelog, and source comments each keep distinct authority roles.
- `document-integrity.md` now treats governed-doc citations in source comments as checked references that must be updated or removed when paths, sections, authority roles, or nearby behavior change.

This release keeps code meaning in code names and moves document provenance into bounded comments only where it materially helps maintenance.

---

## Expected Output

- `coding-discipline.md` now rejects phase/doc/ticket/patch/changelog history in ordinary identifiers unless the token is itself a real external/domain contract term.
- `document-governance.md` now keeps design, phase, patch, changelog, and source-comment responsibilities clearly separated.
- `document-integrity.md` now treats governed-doc citations in source comments as checked references that must stay maintained.
- Touched design/changelog/README/TODO/phase/patch surfaces align to one released `v10.46 / P138` baseline.
- Touched runtime rules are installed/updated and verified for source/runtime parity + body sufficiency.
- `git diff --check`, push/update to `master`, tag, and GitHub release verification all pass before closeout claims release completion.

---

## Action Checklist

- [x] Record the runtime-doctrine source-edit baseline from completed Tasks #453, #456, and #457.
- [x] Sync `design/coding-discipline.design.md` and `changelog/coding-discipline.changelog.md` to v1.2.
- [x] Sync `design/document-governance.design.md` and `changelog/document-governance.changelog.md` to v1.14.
- [x] Sync `design/document-integrity.design.md` and `changelog/document-integrity.changelog.md` to v1.8.
- [x] Open then finalize `TODO.md`, `phase/SUMMARY.md`, this phase file, and the P138 patch file for the selected release wave.
- [x] Complete final verification, install, publish, tag, and release evidence in Task #455.

---

## Out of Scope

- Product-code implementation or broad rename sweeps.
- Turning source comments into a new authority layer.
- Reopening unrelated P132-P137 release surfaces or unrelated plugin waves.

---

## Completion Gate

- semantic/domain/behavior-first code naming doctrine is synchronized across the runtime owner, design companion, and changelog surfaces.
- bounded governed-doc source-comment linkage is synchronized across coding, document-governance, and document-integrity owners.
- TODO, phase, patch, README, master changelog, and version-detail release surfaces are aligned to the released `v10.46 / P138` state.
- final verification checks ran and passed in checked scope.
- runtime install/update, source/runtime parity, body sufficiency, commit, push, tag, and release verification are completed.

---

## Development Verification / TestKit Coverage

- **Route:** `not_applicable_with_reason` for product behavior; this wave is governed-document synchronization and doctrine release work only.
- **Checks run:** `git diff --check`, touched runtime install/update verification, source/runtime parity, body sufficiency, branch/default-branch update verification, tag verification, and GitHub release verification.
- **Confidence:** released and verified in the checked doctrine scope.

---

## Current Status

P138 is completed.

Current checked progress:
- semantic/domain/behavior-first code naming and bounded governed-doc source-comment linkage are now the released coding-doctrine baseline.
- touched design/changelog/README/TODO/phase/patch surfaces are aligned to `v10.46 / P138`.
- touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope.
- `git diff --check`, push/update to `master`, tag `v10.46`, and GitHub release verification all passed.
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.46
