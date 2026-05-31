# governed-docs release-gate flow and closeout consistency patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-06, the release-gate and final closeout-consistency slice.

## Analysis

Before this slice:
- earlier layers could scan, classify, plan, and define execution policy, but they still could not answer the closeout question directly
- the plugin-local chain had no README front page, so the active surface inventory was incomplete for final gate evaluation
- completion wording still depended on manual reasoning rather than a dedicated gate

After this slice:
- release-gate verdict logic exists as a tested runtime module and operator command
- the plugin-local chain now includes `README.md`, satisfying the active governed-surface inventory in checked local scope
- final closeout wording can be anchored to a concrete gate outcome instead of ad hoc completion narration

## Change Items

### 1) Add release-gate runtime and command
- **Target artifact:** `src/governed_docs/release_gate.py`, `src/governed_docs/commands/release_gate.py`
- **Change type:** additive
- **Before state:** no closeout gate runtime existed
- **After state:** the plugin can emit `pass`, `pass-with-notes`, `rework`, and `blocked` verdicts from checked governed-surface findings

### 2) Add focused release-gate tests and CLI routing coverage
- **Target artifact:** `tests/test_release_gate.py`, `src/governed_docs/cli.py`
- **Change type:** additive / refinement
- **Before state:** no focused proof route existed for gate verdict branching
- **After state:** verdict behavior is testable and routable from the operator command layer

### 3) Add plugin-local README front page for gate completeness
- **Target artifact:** `README.md`
- **Change type:** additive
- **Before state:** the active governed-surface set was incomplete because `README.md` was missing
- **After state:** the plugin-local chain now has its required front page and the gate can evaluate the workspace without front-page drift

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 40 tests passed
- `./bin/governed-docs release-gate /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → returned `Verdict: pass`

Covers:
- verdict branching logic
- operator release-gate route
- active governed-surface completeness for the plugin workspace in checked local scope

Does not cover:
- external deployment/runtime truth outside the plugin workspace
- broader product release readiness beyond the selected governed-doc scope

## Rollback approach

If this slice needs containment or partial rollback:
- preserve the README front page even if gate wording changes
- narrow verdict mapping before widening completion claims
- keep gate outcomes scoped to governed-doc closeout rather than external runtime truth
