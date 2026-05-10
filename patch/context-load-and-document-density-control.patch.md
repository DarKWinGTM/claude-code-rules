# Context Load and Document Density Control Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/design.md](../design/design.md) v9.97
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P090 adds a new runtime owner for context-load and document-density control after evidence showed that context pressure came from an aggregate read burst plus dense active documentation lines.

The user clarified two important boundaries:
- reading a lot is not inherently wrong when the task requires it
- the real problem is leader-session raw absorption when a worker could read and filter broad evidence

This patch is governance-only and non-code. It changes RULES runtime doctrine, documentation records, runtime install scope, and release metadata.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `native-worker-agent-routing-and-context-control.md` owns worker scale and dispatch decisions.
- `safe-file-reading.md` owns bounded file reading and sharded design read order.
- `safe-terminal-output.md` owns command-output bounding.
- `governed-document-rollover-control.md` owns TODO/phase entrypoint rollover.
- `document-design-control.md` owns compact design indexes and child shards.
- `document-consistency.md` owns cross-reference, no-drift, and active runtime body checks.
- Master records must describe v9.97 / P090 consistently.

Review concerns:
- Do not turn the solution into a simple “read less” rule.
- Do not create a blanket post-compact restriction when workflow repair is the real fix.
- Do not replace existing worker routing or safe reading owners.
- Do not create God-line style docs while adding a rule against God lines.
- Do not edit NodeClaw files; they are evidence only.
- Do not delete runtime destination extras.

---

## 3) Change Items

### CLDDC-001 — New active runtime owner chain

- **Target artifacts:** `../context-load-and-document-density-control.md`, `../design/context-load-and-document-density-control.design.md`, `../changelog/context-load-and-document-density-control.changelog.md`
- **Change type:** additive runtime/design/changelog chain

**Before**
```text
RULES has safe reading, worker routing, rollover, and document consistency owners, but no single runtime owner connects aggregate read-burst risk, leader-context protection, document density, God-line prevention, append-vs-restructure decisions, and compact/thrash repair signals.
```

**After**
```text
`context-load-and-document-density-control` v1.0 owns context-load lifecycle and document-density strategy.

It defines:
- leader-context protection
- worker-first broad raw evidence filtering
- aggregate read-burst awareness
- God-line prevention
- append-vs-restructure gates
- active entrypoints as maps
- density-aware verification
- compact/thrash as a repair signal
```

### CLDDC-002 — Active runtime install scope increase

- **Target artifact:** `../README.md`
- **Change type:** additive install scope update

**Before**
```text
README Bash and PowerShell install arrays list 46 source-owned active runtime rule files, and current-state cards describe v9.96 / P089 as the latest release.
```

**After**
```text
README Bash and PowerShell install arrays list 47 source-owned active runtime rule files including `context-load-and-document-density-control.md`. Current-state guidance describes v9.97 / P090 as the latest context-load and document-density release while keeping destination extras observed-only.
```

### CLDDC-003 — Master design and changelog release sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`
- **Change type:** governed release sync

**Before**
```text
Master design and changelog identify v9.96 / P089 as the current release and describe active runtime count 46.
```

**After**
```text
Master design and changelog identify v9.97 / P090 as the current release, describe the new context-load/document-density runtime owner, and align active runtime count to 47.
```

### CLDDC-004 — TODO and phase tracking sync

- **Target artifacts:** `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-090-context-load-and-document-density-control.md`
- **Change type:** governed tracking and phase sync

**Before**
```text
TODO and phase summary show no active release target after v9.96 / P089 closeout.
```

**After**
```text
TODO and phase summary track P090 / v9.97 during execution, including source sync, runtime install, 47/47 parity/body-sufficiency checks, density checks, push, and GitHub release verification. P090 phase closes only after those gates pass.
```

### CLDDC-005 — Runtime install and verification

- **Target artifacts:** `/home/node/.claude/rules/`, source README-listed active runtime files
- **Change type:** runtime install and verification

**Before**
```text
Runtime destination contains installed v9.96 active rules with 46/46 source/runtime parity and body sufficiency verified. Destination extras remain observed-only.
```

**After**
```text
Runtime destination contains installed v9.97 active rules with 47/47 source/runtime parity and body sufficiency verified. Destination extras remain observed-only and outside cleanup scope.
```

---

## 4) Verification

Planned verification:
- [x] New runtime/design/changelog chain exists and aligns at v1.0.
- [x] README Bash and PowerShell install arrays contain the same 47 files.
- [x] README-listed active runtime files all exist at source root.
- [x] README-listed active runtime files are not metadata-only.
- [x] Runtime install copies only README-listed active runtime rules.
- [x] Source/runtime parity passes for 47/47 active files.
- [x] Active runtime body sufficiency passes for 47/47 active files.
- [x] Touched active docs are checked for obvious God-line or density regression.
- [ ] `master` push and GitHub release `v9.97` are verified.

---

## 5) Rollback Approach

If P090 overreaches or causes confusing behavior:
- narrow the runtime rule wording while preserving the leader-context and density-lifecycle principles
- keep worker routing mechanics with the worker-routing owner
- keep read caps with safe reading and safe terminal output owners
- revert master v9.97 records only through governed rollback
- reinstall the prior 46-file runtime set only under an explicit rollback gate
- do not delete NodeClaw evidence files, P090 records, or destination extras as cleanup
