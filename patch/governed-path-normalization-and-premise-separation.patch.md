# Governed Path Normalization and Premise-Separation Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.09
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.09 / P101`.

It packages a documentation-normalization wave across broad governed design/changelog/TODO/phase structures together with a premise-separation interaction refinement so the assistant can acknowledge concern without prematurely endorsing an unverified conclusion or drifting into the wrong next action.

---

## Analysis

The released `v10.08 / P100` wave reduced repeated runtime wording safely, but it left two higher-order issues open.

The first issue is structural: RULES doctrine allows sharding and rollover, yet broad chains can still stay root-heavy too long because the normalized path form is not explicit enough.

The second issue is epistemic: RULES discourages over-agreement, but the mechanism is still too wording-heavy. Concern, factual claim, goal request, proposal, and assistant next action need clearer separation before recommendation, agreement, or continuation.

---

## Change Items

### 1) Normalization doctrine hardening

- **Target artifact:** `document-governance.md`, `document-integrity.md`, `phase-todo-artifact.md`, `safe-io.md`
- **Change type:** additive refinement plus normalization hardening
- **Current state:** path-based sharding and rollover are supported, but broad-chain normalization and compact-entrypoint schema remain too flexible.
- **Target state:** broad governed chains have a strong-preferred parent-index + path-shard doctrine; `TODO.md` / `phase/SUMMARY.md` have stricter compact-entrypoint expectations; parent-first + smallest-shard reading is clearer.
- **Review point:** keep owner boundaries explicit and preserve `changelog/done/` as legacy/archive/fallback rather than the ordinary active detail namespace.

### 2) Master design normalization

- **Target artifact:** `design/design.md` plus `design/design/`
- **Change type:** restructuring
- **Current state:** the master design still carries too much active architecture plus release-history weight in one parent file.
- **Target state:** `design/design.md` becomes a compact active parent index and active design truth is redistributed into child shards under `design/design/`.
- **Review point:** keep design as active target-state authority, not history storage.

### 3) Master changelog normalization

- **Target artifact:** `changelog/changelog.md` plus `changelog/changelog/` and any required legacy archive under `changelog/done/`
- **Change type:** restructuring
- **Current state:** the master changelog remains a large root-heavy active history surface.
- **Target state:** `changelog/changelog.md` becomes a compact active parent authority and detailed master-version entries move into chain-scoped version shards under `changelog/changelog/`.
- **Review point:** use `changelog/done/` only for older legacy archive detail that should not remain in the active normalized chain.

### 4) Premise-separation interaction refinement

- **Target artifact:** `communication-register.md`, `evidence-discipline.md`, `execution-and-goal-frame.md`, `accurate-communication.md`
- **Change type:** additive refinement
- **Current state:** anti-over-agreement and anti-drift behavior exists, but it is still too indirect when a user concern also contains a proposed conclusion or path.
- **Target state:** the assistant explicitly separates concern, factual claim, goal, proposal, selected direction, and next action before endorsement or continuation.
- **Review point:** improve epistemic discipline without turning the assistant into blunt contradiction-by-default behavior.

### 5) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P101 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.08 / P100` as the current released wave.
- **Target state:** master surfaces identify `v10.09 / P101` as the current released normalization + premise-separation wave after release verification passes.
- **Review point:** keep runtime install count at 18 unless a separate install-scope change is explicitly validated.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Parent/shard normalization is explicit and validated for new `design/design/` and `changelog/changelog/` chains.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Concern/fact/proposal/goal/next-action separation remains explicit in the touched interaction owners.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- Git diff has no whitespace errors.
- GitHub release `v10.09` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P101 is released as `v10.09`.

Closeout summary: doctrine updates, master normalization, touched companion/master-surface sync, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification all passed in checked scope.

Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.09

Release target and tag point to commit `c883b8617ebfda89ff8dc288533dffe835d6785b`.

Published at `2026-05-17T00:52:06Z`.

---

## Rollback Approach

If P101 is reversed after release, restore the prior `v10.08 / P100` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/memory-context-intelligence/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
