# Worker-First Aggregate-Read Gate Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v10.01
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

P093 turns broad governance/code reading from a soft worker-routing preference into an enforceable aggregate-read gate.

This patch is non-code and governance-only. It changes RULES behavior for worker routing, context-load control, safe file reading, execution continuity, document consistency, and release validation.

Concrete runtime behavior is implemented by the affected root runtime rules and synchronized design/changelog chains.

---

## Analysis

The failure mode is repeated context overflow from leader sessions reading many bounded governance/code files directly.

Each individual read may be bounded, but the aggregate cost of design, changelog, TODO, phase, patch, and source/test files can fill the leader context before implementation or verification is complete.

The target behavior should be:
- classify broad governance/code scans as worker-fit by default
- dispatch a standalone read-only worker before broad leader absorption
- require worker output to return filtered findings, conflicts, exact anchors, and leader verification needs
- preserve direct leader reads for narrow known files and exact edit/verify ranges
- block broad sync/no-drift/release-ready claims when the aggregate-read gate is skipped without a narrow reason

---

## Change Items

### 1) Worker-routing owner

- **Target artifacts:** `native-worker-agent-routing-and-context-control.md` and design/changelog companions
- **Change type:** additive
- **Current state:** worker routing covers broad reads, searches, multi-surface audits, and high-output work.
  Broad governance/code scans are not named as a hard aggregate-read gate.
- **Target state:** define a named worker-first aggregate-read gate for broad governance/code scans, with direct leader handling allowed only through a narrow stated exception.

### 2) Context-load owner

- **Target artifacts:** `context-load-and-document-density-control.md` and design/changelog companions
- **Change type:** additive
- **Current state:** aggregate read-burst control warns that bounded reads can still overload context.
- **Target state:** add deterministic triggers for worker-first filtering.
  Triggers include 3+ governance surfaces, cross-surface release sync, broad code+docs scans, and repo-wide search followed by multi-file reads.

### 3) Safe file-reading owner

- **Target artifacts:** `safe-file-reading.md` and design/changelog companions
- **Change type:** additive
- **Current state:** broad file reads should use worker routing when appropriate.
- **Target state:** broad governance/code file scans use worker-first filtering by default.
  Leader direct reads remain for narrow known files, exact ranges, and final verification anchors.

### 4) Execution-continuity owner

- **Target artifacts:** `execution-continuity-and-mode-selection.md` and design/changelog companions
- **Change type:** additive
- **Current state:** broad continuation should not turn into leader raw absorption.
- **Target state:** execution momentum cannot bypass the aggregate-read gate during broad continuation, release closeout, or no-drift review.

### 5) Consistency and release gate owner

- **Target artifacts:** `document-consistency.md` and design/changelog companions
- **Change type:** additive
- **Current state:** consistency checks verify cross-reference, role boundaries, source/runtime scope, and God-artifact outcomes.
- **Target state:** broad sync/no-drift/closeout/release-ready claims require worker-gate compliance or a documented narrow direct-handling exception.

### 6) Master and release surfaces

- **Target artifacts:** `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, and P093 phase/patch records
- **Change type:** synchronization
- **Current state:** v10.00 / P092 is released and no active phase is selected.
- **Target state:** v10.01 / P093 is recorded as active, then released after gates pass.
  Gates: source sync, runtime install, parity/body sufficiency, density/God-artifact review, push, and GitHub release.

---

## Verification

Before closeout:
- README Bash install array contains exactly 47 active runtime files.
- README PowerShell install array contains exactly the same 47 active runtime files.
- Runtime install copies only the README-listed source-owned active runtime rules.
- Source/runtime parity and body sufficiency pass for 47/47 files.
- Touched P093 active docs avoid new God-line appends.
- Touched owner chains define worker-first aggregate-read gate behavior consistently.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- README, master design, master changelog, TODO, phase, and patch records align to v10.01 / P093.
- `master` push and GitHub release `v10.01` are verified.

---

## Rollback Approach

If rollback is needed:
- revert the P093/v10.01 worker-first gate changes through a governed rollback
- reinstall the prior v10.00 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, unrelated runtime destination files, or other-owner files as cleanup

---

## Current Status

Patch is complete. Source sync, install, parity/body sufficiency, density/God-artifact review, push, and release verification passed.
