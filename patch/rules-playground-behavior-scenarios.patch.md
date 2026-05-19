# RULES Playground Behavior Scenarios Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.19
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.19 / P111`.

It packages a documentation-family expansion so RULES can show how current rules change AI behavior in practice without turning README into a scenario dump and without expanding the runtime install payload.

---

## Analysis

The released `v10.18 / P110` wave fixed install architecture and explanation clarity, but the repository still lacks a governed demonstration family for behavior impact.

The first issue is surface ownership: README can point to examples, but it is not the right place to grow scenario families, coverage matrices, and ongoing observed logs.

The second issue is evidence separation: checked rule behavior, observed incidents, and virtual scenario exploration need a dedicated structure so they do not drift into one another.

The third issue is coverage: there is currently no family-level matrix proving that all 18 active runtime rules are represented by at least one grounded scenario family.

The fourth issue is update continuity: future observed cases need a governed home that can expand over time without inflating changelog, TODO, or README bodies.

---

## Change Items

### 1) Playground architecture design

- **Target artifact:** `design/design/playground-architecture.design.md`
- **Change type:** additive
- **Current state:** no dedicated design shard governs a playground family for RULES behavior scenarios.
- **Target state:** a dedicated design shard defines playground role, fact/observed/virtual separation, coverage contract, update flow, README boundary, runtime boundary, and verification contract.
- **Review point:** keep playground as a non-runtime governed family.

### 2) Playground family baseline files

- **Target artifact:** `playground/README.md`, `playground/coverage.md`, `playground/matrix.md`, `playground/templates/case-template.md`, `playground/observed/2026-05.md`
- **Change type:** additive
- **Current state:** no governed `playground/` family exists.
- **Target state:** the baseline family entrypoint, matrices, template, and observed log exist and align to the selected behavior-evidence model.
- **Review point:** keep observed records factual and virtual exploration visibly labeled.

### 3) Scenario-family case set

- **Target artifact:** `playground/cases/*.md`
- **Change type:** additive
- **Current state:** there are no governed case-family documents showing how current RULES shape AI behavior.
- **Target state:** 10 grounded scenario-family files exist, each separating `rule-enforced fact`, `observed case`, and `virtual variant`.
- **Review point:** ground every scenario in current checked rule behavior rather than invented capability.

### 4) README pointer-level integration

- **Target artifact:** `README.md`
- **Change type:** additive / replacement
- **Current state:** README has no compact governed pointer to a separate playground family.
- **Target state:** README adds only compact navigation/pointer-level integration and keeps the playground out of the runtime install payload.
- **Review point:** avoid broad README rewrite or scenario dumping.

### 5) Master-surface governance sync

- **Target artifact:** touched `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P111 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** `v10.18 / P110` is the current released baseline and no active wave is open.
- **Target state:** master surfaces identify `v10.19 / P111` as the active playground-family wave until release closeout.
- **Review point:** keep runtime install count at 18 and preserve `plugin/` as observed-only and out of staged wave scope.

---

## Verification

Required checks before release closeout:
- all baseline playground files exist at the selected paths
- 10 scenario-family case files exist under `playground/cases/`
- every scenario visibly separates `rule-enforced fact`, `observed case`, and `virtual variant`
- `playground/coverage.md` maps all 18 active runtime rules to at least one scenario family
- `playground/matrix.md` explicitly covers several virtual-case axes such as request type, evidence state, scope clarity, risk, and expected rule response
- README keeps only a compact playground pointer
- `playground/` remains outside the runtime install payload
- runtime install still copies only the 18 README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency still pass for 18/18 files
- `git diff --check` passes
- GitHub release `v10.19` must be created and verified before closeout wording claims release completion

---

## Implementation Status

P111 is active and not yet released.

Wave startup is complete from the released `v10.18 / P110` baseline. Playground-family design and file creation, prompt/response example dialogues, flow diagrams, README pointer integration, touched master-surface sync, runtime-boundary verification, project-local install proof, and `git diff --check` are complete in checked source scope. Release closeout is still pending.

---

## Rollback Approach

If P111 is reversed after release, restore the prior `v10.18 / P110` source state through a governed rollback release while keeping the active runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat `plugin/`, runtime destination extras, or history/done/archive surfaces as cleanup targets during rollback.
