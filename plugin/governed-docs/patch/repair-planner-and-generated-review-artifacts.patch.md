# governed-docs repair planner and generated review artifacts patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-03, the Layer C bridge from doctrine findings into reviewable repair-plan output.

## Analysis

Before this slice:
- the evaluator could classify findings, but it could not turn them into operator-usable repair recommendations
- there was no generated artifact model for repair planning
- later executor and release-gate layers would have had to reconstruct repair intent from raw findings

After this slice:
- doctrine findings can now be converted into structured repair-plan items
- generated artifacts preserve checked scope, recommended action, approval boundary, and preservation notes
- the planning layer remains read-only and does not silently mutate governed files

## Change Items

### 1) Add generated repair artifact models
- **Target artifact:** `src/governed_docs/generated_artifacts.py`
- **Change type:** additive
- **Before state:** no structured repair-plan artifact model existed
- **After state:** repair-plan output can preserve checked scope, evidence, recommended action, approval boundary, and preservation notes

### 2) Add repair planner runtime
- **Target artifact:** `src/governed_docs/repair_planner.py`
- **Change type:** additive
- **Before state:** no Layer C planning runtime existed
- **After state:** doctrine findings can be transformed into bounded repair-plan items without mutating governed files

### 3) Add repair-plan command wrapper and focused tests
- **Target artifact:** `src/governed_docs/commands/repair_plan.py`, `tests/test_generated_artifacts.py`, `tests/test_repair_planner.py`
- **Change type:** additive
- **Before state:** there was no operator entry path or focused proof route for repair-plan behavior
- **After state:** repair-plan generation is exercised through focused tests and a read-only operator path

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 40 tests passed
- `./bin/governed-docs repair-plan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → emitted a read-only repair-plan artifact with `Mutated: False`

Covers:
- repair recommendation mapping
- approval-boundary handling
- generated artifact rendering
- read-only planner boundary

Does not cover:
- destructive governed-file mutation
- deployment/runtime proof outside the plugin workspace

## Rollback approach

If this slice needs containment or partial rollback:
- keep scanner/evaluator boundaries intact
- retain repair artifacts only as review output, never as hidden authority
- do not widen rollback into executor or release-gate behavior unless those layers are also explicitly being changed
