# Governed Document God-File Prevention Patch

> **Current Version:** 1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.99
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

P091 adds file-level governance for God-file and God-document prevention across active RULES documentation surfaces.

This patch is non-code and governance-only. It defines conceptual and structural document-role changes; concrete runtime behavior changes are implemented in the affected rule/design/changelog chains.

---

## Analysis

The existing RULES set already covers God-line density, active entrypoint rollover, design sharding, and phase/subphase lineage.

The missing layer is a document-capacity gate for governed files that are trying to own too many roles or independent execution slices.

The repair model should be role-aware:
- design overload routes to target-state sharding or changelog-backed history removal
- changelog overload routes to compact current index plus `changelog/done/`
- TODO and phase summary overload route to daily-first history/done rollover
- phase overload routes to subphase or new major phase through bounded goal/output/gate lineage
- patch overload routes to separate self-identifying patch artifacts
- README overload routes to current-state summaries with detail delegated to governed owners

---

## Change Items

### 1) Document role model

- **Target artifact:** `project-documentation-standards.md` and design/changelog companions
- **Change type:** additive
- **Current state:** document roles are defined, but file-level overload is not named as a governed failure mode.
- **Target state:** add God-file prevention as a repository-wide role boundary and capacity gate for active governed documents.

### 2) Density and context-load owner

- **Target artifact:** `context-load-and-document-density-control.md` and design/changelog companions
- **Change type:** additive
- **Current state:** God-line and touched-line repair are defined.
- **Target state:** add God-document detection, append-vs-redistribute guidance, and touched-doc repair-or-plan behavior for file-level overload.

### 3) Phase owner

- **Target artifact:** `phase-implementation.md` and design/changelog companions
- **Change type:** additive
- **Current state:** phase lineage and main/subphase boundary are defined.
- **Target state:** add God Phase detection: one phase file must not carry independent goals, outputs, gates, rollback boundaries, or capability streams that deserve split phases.

### 4) Specialized document owners

- **Target artifacts:** design, changelog, TODO, patch, rollover, and consistency owner chains
- **Change type:** additive
- **Current state:** each owner defines its role but does not uniformly classify file-level overload.
- **Target state:** each owner names its overload signals and correct repair route without using cleanup or deletion as the default response.

### 5) Master and release surfaces

- **Target artifacts:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, and `phase/SUMMARY.md`
- **Change type:** synchronization
- **Current state:** v9.98 / P090-01 is released and no active phase is selected.
- **Target state:** v9.99 / P091 is recorded as active, then released after install/parity/body-sufficiency/density gates pass.

---

## Verification

Before closeout:
- README Bash install array contains exactly 47 active runtime files.
- README PowerShell install array contains exactly the same 47 active runtime files.
- Runtime install copied only the README-listed source-owned active runtime rules.
- Source/runtime parity and body sufficiency pass for 47/47 files.
- Touched P091 active docs avoid new God-line appends and include God-file-oriented capacity checks.
- README, master design, master changelog, TODO, phase, and patch records align to v9.99 / P091.
- `master` push and GitHub release `v9.99` are verified.

---

## Rollback Approach

If rollback is needed:
- revert the P091/v9.99 governance changes through a governed rollback
- reinstall the prior v9.98 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, unrelated runtime destination files, or other-owner files as cleanup

---

## Current Status

Patch is complete. Source/runtime install, 47/47 parity/body sufficiency, density review, `master` push, and GitHub release `v9.99` verification passed.
