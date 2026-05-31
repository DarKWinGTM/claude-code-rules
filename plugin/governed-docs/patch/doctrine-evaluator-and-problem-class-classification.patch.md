# governed-docs doctrine evaluator and problem-class classification patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-02, the second bounded runtime slice for `governed-docs` after the explicit-path scanner foundation.

The selected slice is: Layer B doctrine evaluator plus maintenance problem-class classification on top of the existing `ScanResult` foundation.

## Analysis

Before this slice:
- the plugin could scan governed surfaces read-only, but it could not distinguish observed facts from RULES judgments
- there was no runtime finding model for doctrine-aware classifications
- no implementation existed for the required classification states or maintenance problem-class mapping

After this slice:
- Layer B evaluation now exists as a separate read-only runtime surface
- scanner facts and doctrine judgments are distinct
- the required classification states and main maintenance problem classes are mapped in focused tests without widening into repair planning or mutation behavior

## Change Items

### 1) Add doctrine finding models
- **Target artifact:** `src/governed_docs/finding_models.py`
- **Change type:** additive
- **Before state:** no evaluator/finding runtime model existed
- **After state:** the evaluator can return structured doctrine findings and an evaluation result without mutating governed files

### 2) Add doctrine evaluator runtime
- **Target artifact:** `src/governed_docs/doctrine_evaluator.py`
- **Change type:** additive
- **Before state:** no Layer B runtime existed
- **After state:** `ScanResult` can be classified into doctrine findings with explicit classification states and maintenance problem classes

### 3) Add focused evaluator tests
- **Target artifact:** `tests/test_doctrine_evaluator.py`
- **Change type:** additive
- **Before state:** no tests existed for evaluator classifications or problem-class mapping
- **After state:** focused tests prove compliant, legacy-but-allowed, drift, ambiguous-needs-basis, safe-auto-repair, and blocked states plus the main maintenance problem classes

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 17 tests passed
- scanner→evaluator runtime check against the governed-docs workspace emitted read-only findings in checked scope
- existing scanner command still preserved explicit target-path behavior and no-mutation wording

Covers:
- required evaluator classification states
- main maintenance problem-class mapping
- read-only boundary between scanner facts and doctrine judgments
- preservation of the explicit target-path gate after evaluator implementation

Does not cover:
- repair planner implementation
- generated review artifacts
- bounded executor/normalizer behavior
- hook wiring
- public skill/agent installation wiring
- release-gate flow
- article-style Markdown presentation

## Rollback approach

If this slice needs containment or partial rollback:
- keep the explicit target-path gate and scanner foundation intact
- retain the finding model if useful, but narrow evaluator warning-prefix handling before widening into later layers
- do not promote any rollback into repair planner, executor, or hook work
