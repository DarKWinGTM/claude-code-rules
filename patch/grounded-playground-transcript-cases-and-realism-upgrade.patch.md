# Grounded Playground Transcript Cases and Realism Upgrade Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.20
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.20 / P112`.

It packages a realism and evidence upgrade for the non-runtime `playground/` family so behavior scenarios are grounded in actual Claude Code transcript evidence from this machine instead of relying mostly on clean illustrative examples.

---

## Analysis

The released `v10.19 / P111` wave created the baseline playground family, but the first version still has three material gaps.

The first issue is observed-evidence density: several case files still say no checked observed example exists even though real transcript candidates are available.

The second issue is dialogue realism: many examples still show short single-step contrast rather than the more realistic user → tool/evidence → correction/blocker → re-anchor → closeout rhythm of actual Claude Code sessions.

The third issue is scenario diversity: real transcript evidence exposes patterns such as claim-audit disproval and workflow-blocked visual QA that deserve either new family owners or stronger explicit coverage.

---

## Change Items

### 1) Playground architecture refinement

- **Target artifact:** `design/design/playground-architecture.design.md`
- **Change type:** refinement
- **Current state:** the playground architecture defines the baseline fact/observed/virtual split, but it does not yet strongly require transcript-grounded observed anchors or richer realism structure.
- **Target state:** the design shard explicitly requires exact transcript path plus anchor hints for transcript-derived observed cases and supports broader realism features such as multi-turn traces and stronger flow narration.
- **Review point:** keep observed evidence factual and scoped.

### 2) Template and matrix realism upgrade

- **Target artifact:** `playground/templates/case-template.md`, `playground/matrix.md`
- **Change type:** refinement
- **Current state:** the template and matrix support baseline scenarios, but realism is still too abstract.
- **Target state:** the template supports realistic multi-turn traces and transcript-anchor recording, while the matrix includes stronger realism axes and workflow complexity cues.
- **Review point:** do not collapse observed fact into virtual exploration.

### 3) Transcript-grounded observed cases

- **Target artifact:** `playground/observed/2026-05.md` plus selected `playground/cases/*.md`
- **Change type:** corrective enrichment
- **Current state:** observed logs and case files rely too much on release/governance examples and not enough on real session transcripts.
- **Target state:** observed entries include exact checked transcript paths and anchor hints for real cases such as evidence-first diagnosis, completion-claim disproval, rollover preservation, workflow blocks, and authoritative external-doc verification.
- **Review point:** transcript-derived cases must stay factual and scoped.

### 4) Scenario diversity upgrade

- **Target artifact:** selected `playground/cases/*.md` and any new case files justified by evidence
- **Change type:** additive / refinement
- **Current state:** the family is rule-complete but still too narrow in the kinds of real failure and recovery patterns it demonstrates.
- **Target state:** the family either expands existing cases or adds new ones for transcript-grounded patterns such as claim-audit status ladders and visual-QA workflow blocks.
- **Review point:** new family creation must follow checked evidence, not convenience.

### 5) Master-surface synchronization

- **Target artifact:** touched `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P112 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** `v10.19 / P111` is the current released baseline and no active wave is open.
- **Target state:** master surfaces identify `v10.20 / P112` as the active grounded-playground-upgrade wave until release closeout.
- **Review point:** keep runtime install count at 18 and preserve `plugin/` as observed-only and out of staged wave scope.

---

## Verification

Required checks before release closeout:
- transcript-derived observed cases include exact checked transcript paths and anchor hints
- each updated scenario still separates `rule-enforced fact`, `observed case`, and `virtual variant`
- updated scenarios include richer multi-turn traces and stronger flow diagrams where relevant
- any new scenario families are justified by checked transcript evidence
- `playground/` remains outside the runtime install payload
- runtime install still copies only the 18 README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency still pass for 18/18 files
- `git diff --check` passes
- GitHub release `v10.20` must be created and verified before closeout wording claims release completion

---

## Implementation Status

P112 is active and not yet released.

Wave startup is complete from the released `v10.19 / P111` baseline. Transcript-anchor verification, template/matrix realism upgrade, updated observed/case surfaces, touched playground/design sync, and runtime-boundary verification are now complete in checked source scope. Commit / push / GitHub release verification and final closeout are still pending.

---

## Rollback Approach

If P112 is reversed after release, restore the prior `v10.19 / P111` source state through a governed rollback release while keeping the active runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat `plugin/`, runtime destination extras, or history/done/archive surfaces as cleanup targets during rollback.
