# Phase 003-01 - Define Patch Model

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 003-01
> **Status:** Completed
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Design References:** [../design/document-patch-control.design.md](../design/document-patch-control.design.md) + [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/consistency-rule-enhancement.patch.md](../patch/consistency-rule-enhancement.patch.md) + [../patch/legacy-rules-migration.patch.md](../patch/legacy-rules-migration.patch.md)

---

## Objective

Define the corrected patch concept as a governed before/after change artifact and lock the active placement model.

## Why this phase exists

The repository had drifted into an ambiguous patch concept where prose-heavy patch summaries could be mistaken for valid patch artifacts. The active patch model needed one explicit semantic definition and one deterministic placement rule.

## Design Extraction

- Source requirement: patch must mean a self-identifying before/after change artifact with explicit target locations and comparison-friendly change representation
- Derived execution work: update `document-patch-control` and `project-documentation-standards` so the patch concept and placement model become explicit
- Target outcome: the active rule layer teaches one deterministic patch contract

## Patch-to-Phase Extraction

- Source patch input: `patch/consistency-rule-enhancement.patch.md` and `patch/legacy-rules-migration.patch.md`
- Derived execution work: normalize the patch examples so the examples now embody the same before/after contract they are supposed to teach
- Target outcome: active patch examples reinforce the corrected patch model instead of contradicting it

## Flow Diagram

Ambiguous patch concept exists
  → define patch as before/after artifact
  → lock active placement to `patch/<context>.patch.md` or root `<context>.patch.md`
  → normalize in-repo patch examples
  → active patch model becomes deterministic

## Reviewer Checklist

- [x] `document-patch-control` defines patch as a before/after artifact
- [x] patch location model is explicit and deterministic
- [x] generic `patch.md` is no longer part of the active model
- [x] the patch examples reflect the corrected artifact contract

## Verification

- active patch rule and project-documentation rule use the corrected patch definition
- active placement model uses `patch/<context>.patch.md` or root `<context>.patch.md`
- historical patch examples are rewritten as explicit before/after artifacts

## Exit Criteria

- no active patch-governance doc leaves patch meaning implicit
- the active repository model and example patches teach the same contract
