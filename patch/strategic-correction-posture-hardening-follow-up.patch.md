# Strategic Correction Posture Hardening Follow-up Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.28
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.28 / P120`.

It packages one bounded runtime + playground follow-up refinement so AI correction reasoning starts from the shared logic before local symptoms and narrows into local exceptions only when evidence earns that move.

---

## Analysis

The released `v10.27 / P119` baseline already improved active-exchange language alignment, but the checked follow-up still shows a narrower strategic correction miss.

The residual miss is not that evidence discipline is missing altogether. The failure is narrower: AI can still overfit to a current failing supplier/model/path case because a local patch looks convenient or low-blast-radius, even when the available evidence has not yet proved that the underlying doctrine is truly local.

This is a strategy problem more than a wording problem. The better posture is to start from the mechanism or shared logic that best explains the anomaly, then let evidence determine whether the scope really narrows to supplier-specific or stays shared.

This update stays narrow. It does not create a new standalone rule chain, does not ban local exceptions categorically, does not weaken evidence discipline, and does not expand the runtime install set. It refines the correct strategic owners, updates one existing playground case, and syncs the directly affected governing/master surfaces.

---

## Change Items

### 1) Logic-first correction and scope-as-conclusion refinement

- **Target artifact:** touched evidence owner governing burden of proof, claim-state separation, and scope honesty
- **Change type:** refinement
- **Current state:** evidence thresholds already exist, but strategic fix-scope narrowing from one local anomaly is still under-specified
- **Target state:** local anomalies are evidence inputs, while supplier/model/path-specific scope remains a conclusion to prove rather than the default starting assumption
- **Review point:** preserve evidence semantics as principles rather than turning them into a command-style prohibition list

### 2) Corroborated provider/supplier narrowing refinement

- **Target artifact:** touched external/source-trust owner governing provider- and version-dependent evidence
- **Change type:** refinement
- **Current state:** corroboration and conflict handling exist, but the doctrine does not yet explicitly connect them to supplier/model/path-specific fix-scope recommendations
- **Target state:** narrowing a recommendation into provider/supplier/model/path-specific scope should require corroboration strong enough to earn that narrower owner decision
- **Review point:** preserve proportional research expectations and avoid turning corroboration into a blanket blocker when scope is already proven

### 3) Strategy-before-patch recommendation refinement

- **Target artifact:** touched communication owners governing recommendation posture and evidence-shaped correction wording
- **Change type:** refinement
- **Current state:** evaluation-before-agreement and evidence-grounded recommendation wording already exist, but they do not yet explicitly discourage convenience-first local patch recommendations when shared logic is still the stronger explanatory candidate
- **Target state:** AI should prefer strategy-before-patch reasoning, compare shared mechanisms against local exceptions, and keep local exceptions as evidence-earned recommendations rather than default convenience fixes
- **Review point:** preserve human-readable recommendation wording and avoid replacing principles with rigid do/don't lists

### 4) Playground case update

- **Target artifact:** one existing case under `playground/cases/`
- **Change type:** refinement
- **Current state:** the playground covers evidence, portability, and language-alignment boundaries, but it does not yet inspect the strategic fix-scope failure mode directly enough
- **Target state:** one updated case visibly shows the behavior delta from case-first/local-fix-first to logic-first/scope-proven/strategy-before-patch
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about `rule-enforced fact`, `observed case`, and `virtual variant` separation

### 5) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.27 / P119` as the current released baseline with no active wave open
- **Target state:** master surfaces open and later close `v10.28 / P120` consistently while preserving the 18-file runtime install scope, evidence-discipline strictness, direct-continuation boundaries, and the non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners encode logic-first correction posture rather than case-first/local-fix-first reasoning
- touched owners make supplier/model/path-specific narrowing something the evidence must prove rather than the default convenience recommendation
- touched owners preserve the principle that exceptions can still exist, but only as evidence-earned doctrine differences
- one related playground case is updated with an inspectable behavior delta
- touched release/master surfaces align to `v10.28 / P120`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.28` is created and verified before closeout wording claims release completion

---

## Implementation Status

P120 is completed.

The checked strategic-reasoning gap and the selected bounded improvement direction were already established; owner refinement, companion/changelog sync, playground case update, runtime install-boundary proof, parity/body-sufficiency verification, commit/push/default-branch update, GitHub release verification, and final closeout alignment all completed.
