# Single-source authority cleanup patch

> **Current Version:** 0.1.59
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-28)
> **Status:** Phase 055 completed single-source authority cleanup in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.59
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The user required one main path only for `memory-context-intelligence`: keep the plugin identity as `memory-context-intelligence@darkwingtm`, keep the source home under `RULES/plugin/memory-context-intelligence/`, remove the duplicate `TEMPLATE/PLUGIN/memory-context-intelligence/` tree, and do not create a new duplicate.

The duplicate tree had already been removed and the marketplace root had already been migrated to `TEMPLATE`, but several active authority docs still described the removed projection family as if it were current truth.

## 2) Analysis

The cleanup wave needed one coherent before/after review boundary:
- keep one active source home only
- keep the root `TEMPLATE` marketplace as the active shared `darkwingtm` binding
- keep `memory-context-intelligence@darkwingtm` unchanged
- remove active-authority wording that still treated `TEMPLATE/PLUGIN/memory-context-intelligence/` as current runtime truth
- preserve earlier projection-family references only as historical/provenance evidence where they still explain old installability phases

## 3) Change items

### 3.1 Active authority wording cleanup
- **Target artifact:** `../README.md`, `../design/design.md`, `../design/06-plugin-installability.design.md`, `../phase/SUMMARY.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement
- **Before:** active docs still described `TEMPLATE/PLUGIN/memory-context-intelligence/` as a current runtime-facing projection/package truth
- **After:** active docs now describe one RULES-owned source home plus the root `TEMPLATE` marketplace binding as the only current authority model

### 3.2 Historical downgrade of projection-family proof
- **Target artifact:** `../README.md`, `../design/design.md`, `../design/06-plugin-installability.design.md`, `../phase/SUMMARY.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`
- **Change type:** replacement/additive
- **Before:** several phase-031/032/033 statements still read like current truth
- **After:** those references are now explicitly historical/provenance-only where retained

### 3.3 Governed closeout surfaces
- **Target artifact:** `../changelog/changelog.md`, `../changelog/v0.1.59-completed-single-source-authority-cleanup.changelog.md`, `../phase/phase-055-single-source-authority-cleanup.md`, and this patch
- **Change type:** additive/replacement
- **Before:** no dedicated closeout artifact existed for the single-source authority cleanup wave
- **After:** changelog/phase/patch now record this wave explicitly

## 4) Verification

- active docs should describe `RULES/plugin/memory-context-intelligence/` as the single source home
- active marketplace truth should point to the root `TEMPLATE` marketplace entry using supported in-base source `./RULES/plugin/memory-context-intelligence`
- `memory-context-intelligence@darkwingtm` should remain the install identity
- no active config/binding should point to `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence`

## 5) Rollback approach

If this cleanup wave is rolled back, restore the older active-authority wording only if the user explicitly wants that semantic model back. Do not recreate the removed duplicate tree or mutate install/runtime state as part of this patch rollback unless the user explicitly authorizes broader rollback scope.
