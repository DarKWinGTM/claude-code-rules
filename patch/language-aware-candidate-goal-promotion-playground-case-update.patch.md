# Language-Aware Candidate-Goal Promotion Playground Case Update Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.23
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.23 / P115`.

It packages one new governed non-runtime playground case family so the recently released language-aware candidate-goal and `/goal` promotion doctrine can be inspected operationally inside `playground/`.

---

## Analysis

The runtime doctrine released in `v10.22 / P114` now makes candidate goals dominant-session-language-aware and promotes only one governed candidate into advisory `/goal` form when the bridge holds.

The remaining gap is operational inspectability: the playground family does not yet show that behavior as a standalone scenario family.

This update stays narrow. It does not change runtime doctrine again. It adds one new case family plus the directly affected governing/master surfaces needed for a release-quality source sync.

---

## Change Items

### 1) New playground case family

- **Target artifact:** `playground/cases/case-15-language-aware-candidate-goal-promotion.md`
- **Change type:** additive
- **Current state:** the playground family has no dedicated case for dominant-session-language ownership, candidate-goal-first successor recommendations, and selective `/goal` promotion.
- **Target state:** the playground family includes one dedicated case showing those behaviors operationally.
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about `rule-enforced fact`, `observed case`, and `virtual variant` separation.

### 2) Playground index update

- **Target artifact:** `playground/README.md`
- **Change type:** additive
- **Current state:** the scenario-family index stops at case 14.
- **Target state:** the index includes case 15 and keeps the playground as a pointer-level governed family entrypoint.
- **Review point:** do not turn the playground README into a broad scenario dump.

### 3) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.22 / P114` as the current released baseline.
- **Target state:** master surfaces open and later close `v10.23 / P115` consistently while preserving the playground non-runtime boundary.
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload.

---

## Verification

Required checks before release closeout:
- `playground/cases/case-15-language-aware-candidate-goal-promotion.md` exists
- `playground/README.md` indexes the new case family
- touched release/master surfaces align to `v10.23 / P115`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- GitHub release `v10.23` is created and verified before closeout wording claims release completion

---

## Implementation Status

P115 is in progress.

The new playground case family exists in source scope and the index update is present; master-surface sync, runtime install-boundary proof, parity/body-sufficiency verification, commit/push, GitHub release verification, and final closeout alignment remain pending.
