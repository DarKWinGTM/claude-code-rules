# Opportunistic God-Line Repair Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/design.md](../design/design.md) v9.98
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P090 created the context-load and document-density owner. P090-01 refines that owner so God-line handling becomes an operational repair posture when an active document is already being touched.

The goal is bounded auto-repair, not broad auto-formatting:
- repair clear, low-risk touched God-line candidates in the same edit
- flag or plan broad, history-heavy, or meaning-risky density debt
- avoid silently appending more content to a known God-line candidate
- keep active runtime count at 47

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `context-load-and-document-density-control.md` owns density lifecycle and God-line doctrine.
- `safe-file-reading.md` owns bounded file reading and sharded design read order.
- `native-worker-agent-routing-and-context-control.md` owns worker scale before broad raw evidence absorption.
- `governed-document-rollover-control.md` owns TODO/phase active-entrypoint rollover.
- `document-consistency.md` owns no-drift, source/runtime parity, and body-sufficiency checks.
- Master records must describe v9.98 / P090-01 consistently.

Review concerns:
- Do not turn opportunistic repair into a blanket repo-wide rewrite policy.
- Do not modify history-heavy or ambiguous lines when the semantic split is risky.
- Do not increase active runtime count or change README install arrays.
- Do not delete runtime destination extras.
- Do not reopen the completed P090 patch as an active artifact.

---

## 3) Change Items

### OGAR-001 — Runtime owner chain refinement

- **Target artifacts:** `../context-load-and-document-density-control.md`, `../design/context-load-and-document-density-control.design.md`, `../changelog/context-load-and-document-density-control.changelog.md`
- **Change type:** replacement / additive refinement

**Before**
```text
The P090 owner defines God-line prevention and append-vs-restructure gates, but it does not explicitly require immediate low-risk repair when the assistant is already touching a God-line candidate.
```

**After**
```text
`context-load-and-document-density-control` v1.1 requires opportunistic repair for touched active-doc God-line candidates when the semantic split is clear and low-risk.

It also defines the boundary:
- broad repairs are planned or routed instead of performed silently
- history-heavy or meaning-risky lines are flagged rather than rewritten immediately
- known God-line candidates must not receive more append-only content
```

### OGAR-002 — Master design and changelog release sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`
- **Change type:** governed release sync

**Before**
```text
Master design and changelog identify v9.97 / P090 as the current release, and the context-load owner chain is at v1.0.
```

**After**
```text
Master design and changelog identify v9.98 / P090-01 as the current release, keep active runtime count at 47, and describe opportunistic God-line repair as a refinement of the P090 owner.
```

### OGAR-003 — README, TODO, and phase tracking sync

- **Target artifacts:** `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-090-01-opportunistic-god-line-repair.md`
- **Change type:** governed tracking and front-page sync

**Before**
```text
README, TODO, and phase summary show P090 / v9.97 as completed, with no active release target selected afterward.
```

**After**
```text
README, TODO, and phase summary track P090-01 / v9.98 during execution and close only after source sync, runtime install, 47/47 parity/body sufficiency, density review, push, and release gates pass.
```

### OGAR-004 — Runtime install and verification

- **Target artifacts:** `/home/node/.claude/rules/`, source README-listed active runtime files
- **Change type:** runtime install and verification

**Before**
```text
Runtime destination contains installed v9.97 active rules with 47/47 source/runtime parity and body sufficiency verified. Destination extras remain observed-only.
```

**After**
```text
Runtime destination contains installed v9.98 active rules with 47/47 source/runtime parity and body sufficiency verified. Destination extras remain observed-only and outside cleanup scope.
```

---

## 4) Verification

Planned verification:
- [ ] Runtime/design/changelog chain aligns at v1.1.
- [ ] README Bash and PowerShell install arrays still contain the same 47 files.
- [ ] README-listed active runtime files all exist at source root.
- [ ] README-listed active runtime files are not metadata-only.
- [ ] Runtime install copies only README-listed active runtime rules.
- [ ] Source/runtime parity passes for 47/47 active files.
- [ ] Active runtime body sufficiency passes for 47/47 active files.
- [ ] Touched active docs are checked for obvious God-line or density regression.
- [ ] `master` push and GitHub release `v9.98` are verified.

---

## 5) Closeout Summary

Pending until source sync, runtime install, verification, push, and release gates pass.

## 6) Rollback Approach

If P090-01 overreaches or causes confusing behavior:
- narrow opportunistic repair wording while preserving God-line prevention and append-vs-restructure principles
- keep worker routing mechanics with the worker-routing owner
- keep read caps with safe reading and safe terminal output owners
- restore prior v9.97 release records only through governed rollback
- reinstall the prior 47-file runtime set only under an explicit rollback gate
- do not delete completed P090 records, P090-01 records, history surfaces, or destination extras as cleanup
