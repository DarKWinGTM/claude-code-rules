# Project-Local Claude Code Install Architecture and Explanation Clarity Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.18
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.18 / P110`.

It packages a documentation-and-helper correction so project-local Claude Code install becomes script-first instead of README-inline and user-level-first.

---

## Analysis

The released `v10.17 / P109` wave corrected phase lineage behavior, but install guidance still has a shape gap.

The first issue is executable ownership: the README still carries long installer bodies instead of dedicated helper files.

The second issue is target bias: the old guidance centers `~/.claude/rules/` rather than `<project-root>/.claude/rules/` as the primary install surface.

The third issue is support overreach: touched README install wording should not imply Codex CLI or Gemini CLI support when this wave only targets the native Claude Code install surface.

The fourth issue is explanation rigidity: communication answers can still mention raw variables, fields, and config keys without translating what they are doing in the system.

---

## Change Items

### 1) Bash helper extraction

- **Target artifact:** `script/setup-claude-code-rules.sh`
- **Change type:** additive
- **Current state:** no Bash helper script exists in source scope.
- **Target state:** a Bash helper installs the active 18-rule runtime set into a project-local `.claude/rules/` target while preserving owner-aware manifest cleanup.
- **Review point:** remote bootstrap and local-repo execution should both resolve into the same project-local target model.

### 2) PowerShell helper extraction

- **Target artifact:** `script/setup-claude-code-rules.ps1`
- **Change type:** additive
- **Current state:** no PowerShell helper script exists in source scope.
- **Target state:** a PowerShell helper installs the active 18-rule runtime set into a project-local `.claude/rules/` target while preserving owner-aware manifest cleanup.
- **Review point:** keep install semantics aligned with the Bash helper.

### 3) Installer design normalization

- **Target artifact:** `design/design/installer-architecture.design.md`
- **Change type:** additive
- **Current state:** installer behavior is implied by README, phase, and patch surfaces but has no dedicated target-state design surface.
- **Target state:** a dedicated design shard defines primary target, optional global fallback, execution modes, source resolution, cleanup boundary, support boundary, and verification contract.
- **Review point:** keep the install architecture durable enough for future refinement without overclaiming unsupported harness surfaces.

### 4) README install-surface correction

- **Target artifact:** `README.md`
- **Change type:** replacement
- **Current state:** Quick Start still embeds long installer logic and over-broad cross-harness adaptation wording.
- **Target state:** README points to clone → launcher as the primary install path, keeps helper scripts as the execution layer underneath, and states that the current install surface is Claude Code only.
- **Review point:** keep the active runtime install set at 18 and avoid user-level-first wording.

### 5) Explanation clarity doctrine refinement

- **Target artifact:** `accurate-communication.md`, `explanation-and-presentation.md`, `communication-register.md`
- **Change type:** corrective refinement
- **Current state:** easier explanations can still rely too heavily on raw identifiers without translating their system role first.
- **Target state:** selected owners require meaning-first explanation, parent → child nested-key walkthroughs, UI-versus-storage separation when relevant, and proportional anti-over-explanation limits.
- **Review point:** improve readability without drifting into character voice or mini-tutorial over-expansion.

---

## Verification

Required checks before closeout:
- helper scripts exist at the two required paths
- installer design surface exists and governs the selected install model
- helper scripts target `<project-root>/.claude/rules/`
- owner-aware manifest cleanup is preserved
- active runtime install scope remains 18 root files
- touched README sections no longer claim Codex/Gemini support for this install surface
- touched communication/explanation owners require meaning-first identifier explanation, nested-key parent → child walkthroughs when useful, UI-versus-storage separation when relevant, and anti-over-explanation limits
- project-local install proof passes with 18/18 source/destination parity and body sufficiency
- `git diff --check` passes

---

## Implementation Status

P110 is active and not yet released.

Wave startup is complete from the released `v10.17 / P109` baseline. Helper extraction, README install-surface correction, touched master-surface sync, project-local install proof, and `git diff --check` are complete in checked source scope. Release selection is not part of the current goal.

---

## Rollback Approach

If P110 is reversed after release, restore the prior `v10.17 / P109` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat `plugin/`, runtime destination extras, or history/done/archive surfaces as cleanup targets during rollback.
