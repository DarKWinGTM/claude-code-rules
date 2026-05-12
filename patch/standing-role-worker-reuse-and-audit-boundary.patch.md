# Standing-Role Worker Reuse and Audit Boundary Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Completed / Released
> **Target Design:** [../design/design.md](../design/design.md) v10.03
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

P095 is a released governance-only update that promotes universal standing-role worker and teammate reuse doctrine into Main RULES.

The target behavior is not to copy plugin-owned coordination mechanics. It is to make role reuse, phase-ID-as-context, and evidence-based lifecycle audit apply whether or not `claude-session-coordination` is active.

---

## Analysis

`claude-session-coordination` clause 6 contains both universal doctrine and package-local mechanics.

The universal doctrine belongs in Main RULES:
- stable standing-role workers or teammates should be reused across phases
- phase/task IDs should be assignment context, not worker identity
- active or recent aligned roles should be steered before duplicate-looking spawns
- lifecycle decisions need a scoped audit before reuse, spawn, respawn, shutdown, or duplicate/overlap reporting
- simultaneous same-role lanes should be distinguished by responsibility, surface, or output
- worker-scale decisions should preserve the difference between one focused standalone lane and coordinated Agent Team workflow

Plugin-only mechanics stay local to `claude-session-coordination`.

Excluded examples:
- shared-board title grammar
- session-short-id prefixes
- creator-owner hook validation
- hidden registries
- package tmux bridge behavior
- exact `--teammate-mode tmux` behavior

---

## Change Items

### 1) Native worker routing owner

- **Target artifacts:** `native-worker-agent-routing-and-context-control.md` and design/changelog companions
- **Change type:** additive refinement
- **Current state:** worker routing already says to reuse active/recent standing-role workers before duplicate-looking spawns, but it does not yet define a full mechanism-neutral audit contract for lifecycle decisions.
- **Target state:** define global standing-role worker/teammate reuse and audit doctrine.
  Require phase/task IDs to live in assignment context, audit scoped coordination evidence before lifecycle decisions, and name simultaneous same-role lanes by real responsibility or surface rather than phase ID alone.

### 2) Master and release surfaces

- **Target artifacts:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, and P095 phase/patch records
- **Change type:** synchronization
- **Current state:** v10.02 / P094 is released; P095 is not yet recorded as active or released.
- **Target state:** v10.03 / P095 is recorded as released after implementation, install, push, and release gates pass.
  Runtime install count remains 47.

---

## Verification

Before closeout:
- README Bash install array contains exactly 47 active runtime files.
- README PowerShell install array contains exactly the same 47 active runtime files.
- Runtime install copies only the README-listed source-owned active runtime rules for the current 47-file set.
- Source/runtime parity and source/destination active runtime body sufficiency pass for 47/47 files.
- Native-worker runtime/design/changelog align to v1.7.
- Standing-role reuse, phase-ID-as-context, lifecycle audit, scoped state evidence, responsibility-based lane naming, and worker-scale rules are present.
- Plugin-only mechanics remain exclusions or plugin-local references only.
  - Shared-board grammar and session-short-id prefixes stay local.
  - Creator-owner hooks and hidden registries stay local.
  - Package tmux bridge behavior and exact `--teammate-mode tmux` behavior stay local.
  - None of these become Main RULES required behavior.
- Touched active docs avoid new God-line or God-document overload.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- README, master design, master changelog, TODO, phase, and patch records align to v10.03 / P095.
- `master` push and GitHub release `v10.03` verification pass.

---

## Rollback Approach

If rollback is needed:
- revert the P095/v10.03 standing-role reuse and audit changes through a governed rollback
- reinstall the prior v10.02 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, unrelated runtime destination files, or other-owner files as cleanup

---

## Current Status

Patch is completed for the v10.03 release.

Verified in source/runtime/release:
- owner-chain edits are complete
- master source sync is complete
- runtime install copied the 47 README-listed root rules
- source/runtime parity and source/destination body sufficiency passed for 47/47 files
- semantic promotion, plugin exclusion, and P095-specific density review passed
- `master` push and GitHub release `v10.03` verification passed
- release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.03
- release target and tag point to commit `d5d7f1dbd3f16a1159f308e67b577878784f0356`
- published at `2026-05-12T22:23:41Z`
- broader master governance density rollover remains deferred in `TODO.md`

Pending gates:
- none for P095
