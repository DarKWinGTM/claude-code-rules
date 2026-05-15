# Source Merge Cleanup Compact Runtime Set Patch

> **Current Version:** 1.0
> **Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3
> **Status:** Active / Release Preparation
> **Target Design:** [design/design.md](../design/design.md) v10.05
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.05 / P097`.

It packages the source-local merge cleanup that reduces the active RULES runtime install set to 18 merged, body-sufficient root runtime rules.

---

## Analysis

The prior released `v10.04 / P096-01` state used a 47-rule active runtime set.

The current source cleanup has merged overlapping rule families into broader owners such as `coding-discipline.md`, `document-governance.md`, `execution-and-goal-frame.md`, `safe-io.md`, and `worker-routing-and-context.md`.

The release risk is not only file count reduction; the risk is broken governance metadata or treating local backup output as active authority.

---

## Change Items

### 1) Runtime install scope

- **Target artifact:** `README.md` install arrays
- **Change type:** replacement
- **Current state:** prior release records describe a 47-rule active runtime set.
- **Target state:** README installs the compact 18-rule merged runtime set.
- **Review point:** install scope must remain root runtime rules only, excluding design, changelog, TODO, phase, patch, support, and backup artifacts.

### 2) Merged runtime owner metadata

- **Target artifact:** merged active root runtime rules plus `design/` and `changelog/` companions
- **Change type:** additive and repair
- **Current state:** some merged runtime files have missing design metadata or changelog/design companion files.
- **Target state:** all 18 active runtime rules have substantive bodies plus resolvable `Design` and `Full history` links.
- **Review point:** design/changelog companions are governance support, not extra runtime install targets.

### 3) Governance surfaces

- **Target artifact:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P097 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces still contain `v10.04 / P096-01` and 47-rule release wording.
- **Target state:** master surfaces identify `v10.05 / P097` as the compact 18-rule merged runtime release preparation wave until release verification passes.
- **Review point:** no doc may claim push/release verification before those gates actually pass.

### 4) Backup/provenance output

- **Target artifact:** `.gitignore`
- **Change type:** additive hygiene boundary
- **Current state:** `.claude-code-rules-legacy-backup/` exists as untracked local backup output.
- **Target state:** backup output is ignored and not committed as active runtime authority.
- **Review point:** ignoring the backup is not deletion and does not make its contents active runtime truth.

---

## Verification

Required checks before release:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- All 18 active runtime files have resolvable design and changelog metadata links.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- Git diff has no whitespace errors.
- GitHub release `v10.05` is created and verified before closeout wording claims release completion.

---

## Rollback Approach

If P097 is rejected before release, restore the prior 47-rule source state from git and do not delete local backup/provenance output as cleanup.

If release already happened, perform a governed rollback release that restores the prior runtime install scope and records the rollback in README, changelog, TODO, phase, and patch surfaces.
