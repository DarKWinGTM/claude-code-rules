# Active-Exchange Language Alignment Hardening Follow-up Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** In progress
> **Target Design:** [design/design.md](../design/design.md) v10.27
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.27 / P119`.

It packages one bounded runtime + playground follow-up refinement so active-exchange language alignment in goal-shaped output becomes explicit without reopening the broader response-style wave.

---

## Analysis

The released `v10.26 / P118` baseline already improved successor-surfacing behavior, but the checked follow-up still shows a narrower language-alignment miss.

The residual miss is not that language alignment is absent everywhere. In the checked case, AI can localize the wrapper or parts of the visible goal surface, but still leaves the promoted `/goal` body or recommendation body in another language even when the user's active working language across the current exchange is already clear.

The boundary problem is that exact literals do need preservation, but preservation is currently too coarse when the model treats the whole block as if it were exact. The correct split is narrower: preserve exact literals such as `/goal`, file paths, identifiers, version tags, and query parameters, while localizing the natural-language scaffold around them.

This update stays narrow. It does not create a new standalone rule chain, does not hardcode Thai, does not weaken evidence discipline, does not reduce direct-continuation priority, and does not expand the runtime install set. It refines the correct existing owners, updates one existing playground case, and syncs the directly affected governing/master surfaces.

---

## Change Items

### 1) Active-exchange language selection refinement

- **Target artifact:** touched runtime owner governing candidate goals, promoted `/goal`, recommendation labels, and recap/closing lines
- **Change type:** refinement
- **Current state:** dominant-session-language guidance exists, but it still leaves room for wrapper-only translation or for over-preserving the whole block as if it were exact
- **Target state:** the default language for goal-shaped output is inferred from the user's active working language across the current exchange; explicit language request remains a stronger override
- **Review point:** preserve direct continuation and keep exact literals exact only where exactness materially matters

### 2) Concept-slot versus exact-literal boundary refinement

- **Target artifact:** touched runtime owner governing `/goal` slot translation from execution surfaces
- **Change type:** refinement
- **Current state:** concept-slot wording can follow the dominant session language, but the exact-literal boundary is not explicit enough to stop whole-block preservation drift
- **Target state:** scaffold wording localizes, exact literals stay token-scoped, and the whole emitted command body is no longer treated as one exact literal
- **Review point:** preserve material-only sourcing and avoid inventing details absent from checked execution surfaces

### 3) Wrapper-only-translation anti-pattern refinement

- **Target artifact:** touched communication/presentation owners governing visible answer shape
- **Change type:** refinement
- **Current state:** wrapper labels and goal-shaped body can still drift into mixed-language output
- **Target state:** translating only the wrapper while leaving the goal/recommendation body in another language is explicitly disallowed except for preserved exact literals
- **Review point:** keep the fix narrow to language alignment in goal-shaped output and avoid reopening the broader response-style wave unnecessarily

### 4) Playground case update

- **Target artifact:** one existing case under `playground/cases/`
- **Change type:** refinement
- **Current state:** the playground covers end-to-end language alignment conceptually, but it does not yet inspect wrapper-only translation as a distinct observed miss/fix
- **Target state:** one updated case visibly shows the miss/fix so the refinement remains inspectable without opening a broad new family
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about `rule-enforced fact`, `observed case`, and `virtual variant` separation

### 5) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.26 / P118` as the current released baseline with no active wave open
- **Target state:** master surfaces open and later close `v10.27 / P119` consistently while preserving the 18-file runtime install scope, evidence-discipline strictness, direct-continuation boundaries, and the non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners encode active-exchange language as the default for goal-shaped output without requiring direct language instructions every time
- touched owners preserve exact literals at token level rather than treating the whole block as exact
- touched owners reject wrapper-only translation as sufficient language alignment
- one related playground case is updated with an inspectable miss/fix
- touched release/master surfaces align to `v10.27 / P119`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.27` is created and verified before closeout wording claims release completion

---

## Implementation Status

P119 is in progress.

The checked follow-up language-alignment gap and the selected bounded improvement direction already exist; owner refinement, companion/changelog sync, playground case update, runtime install-boundary proof, parity/body-sufficiency verification, commit/push/default-branch update, GitHub release verification, and final closeout alignment remain pending.
