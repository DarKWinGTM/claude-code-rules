# Proactive Goal Surfacing and Decision-Ready Response Style Refinement Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.25
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.25 / P117`.

It packages one combined runtime + playground refinement so goal-oriented next-step surfacing becomes more proactive where several meaningful successor slices remain live, and so default non-trivial answer structure becomes easier to read and more decision-ready without duplicating existing owner doctrine.

---

## Analysis

The released baseline already contains strong language-aware goal behavior and strong easy-first communication behavior, but the owner set still leaves two gaps.

The first gap is behavioral priority. Current execution doctrine heavily prefers direct continuation and closeout-only successor surfacing, so candidate goals do not appear often enough when the assistant is at a real decision boundary and several materially different next slices are live.

The second gap is owner completeness. Current communication/presentation owners already teach plain-language explanation, scanable grouping, light-table usage, identifier glosses, and evidence-calibrated wording, but they do not yet encode the requested default non-trivial answer shape clearly enough as one normalized owner-aligned behavior. That leaves room for answers that are still correct but feel too abrupt, too diffuse, or insufficiently structured when several axes need to be compared.

This update stays narrow. It does not create a new standalone rule chain, does not weaken evidence discipline, does not force tables or long structure into trivial work, and does not expand the runtime install set. It refines the correct existing owners, adds one new playground case family, and syncs the directly affected governing/master surfaces.

---

## Change Items

### 1) Goal-surfacing owner refinement

- **Target artifact:** touched runtime owners governing continuation, next-goal discovery, and candidate-goal shaping
- **Change type:** refinement
- **Current state:** candidate-goal surfacing is mostly tied to closeout and can be bypassed by direct-continuation priority too early.
- **Target state:** candidate goals become easier to surface at real decision boundaries when several materially different next slices remain live and no one continuation path clearly dominates.
- **Review point:** keep `/goal` advisory, preserve direct continuation when one path clearly dominates, and avoid turning trivial micro-choices into artificial goal menus.

### 2) Default response-style owner refinement

- **Target artifact:** touched communication/presentation/evidence-surface wording owners
- **Change type:** refinement
- **Current state:** easy-first explanation, scanable grouping, light tables, identifier glosses, and evidence wording exist, but the default non-trivial answer shape is still not explicit enough as one normalized owner-aligned behavior.
- **Target state:** default non-trivial answers become easy-first, compact-but-complete, scanable, identifier-meaning-first, evidence-layer-clear, and concise-decision-ready.
- **Review point:** preserve factual precision, avoid ritualizing trivial answers, and keep boundary ownership clear between shape/tone/writing versus factual proof thresholds.

### 3) New playground case family

- **Target artifact:** `playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md`
- **Change type:** additive
- **Current state:** the playground family has no dedicated case that combines more proactive candidate-goal surfacing with the requested decision-ready explanation shape.
- **Target state:** the playground family includes one dedicated case showing both behaviors operationally.
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about `rule-enforced fact`, `observed case`, and `virtual variant` separation.

### 4) Playground index update

- **Target artifact:** `playground/README.md`
- **Change type:** additive
- **Current state:** the scenario-family index stops at case 16.
- **Target state:** the index includes case 17 and keeps the playground as a pointer-level governed family entrypoint.
- **Review point:** do not turn the playground README into a broad scenario dump.

### 5) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.24 / P116` as the current released baseline.
- **Target state:** master surfaces open and later close `v10.25 / P117` consistently while preserving the 18-file runtime install scope, evidence-discipline strictness, trivial-answer anti-ritual boundaries, and the non-runtime playground boundary.
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload.

---

## Verification

Required checks before release closeout:
- touched goal-surfacing owners encode more proactive candidate-goal surfacing without breaking direct-continuation boundaries
- touched response-style owners encode the requested default non-trivial answer shape without duplicating evidence-discipline semantics
- `playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md` exists
- `playground/README.md` indexes the new case family
- touched release/master surfaces align to `v10.25 / P117`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the new case and touched master surfaces after update
- GitHub release `v10.25` is created and verified before closeout wording claims release completion

---

## Implementation Status

P117 is completed.

The owner evidence for both behavior gaps was checked; owner refinement, companion/changelog sync, playground case creation, runtime install-boundary proof, parity/body-sufficiency verification, commit/push/default-branch update, GitHub release verification, and final closeout alignment all completed.
