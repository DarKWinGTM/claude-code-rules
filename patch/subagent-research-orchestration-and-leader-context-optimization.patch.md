# Subagent Research Orchestration and Leader Context Optimization Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.87, [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md) v1.2
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P081-02 refines the existing native worker routing family so broad external research and design-improvement analysis use subagent research lanes more effectively. The user wants the AI to pull more value from subagents: leader should decide what to research and how to split it, while subagents perform scoped web/source research, analyze source quality, and return useful findings instead of raw dumps.

พูดง่าย ๆ: เป้าหมายไม่ใช่ “ใช้ agent เยอะ ๆ” แต่คือให้ leader วาง research map แล้วใช้ subagent เป็นเลนค้นคว้า/วิเคราะห์ที่ลด context load และเพิ่มคุณภาพการตัดสินใจ.

This patch keeps active runtime count at 44 because it refines existing rule owners rather than adding a new active runtime rule.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `native-worker-agent-routing-and-context-control.md` owns worker routing, subagent-first scale gate, handoff quality, and leader verification.
- `external-verification-and-source-trust.md` owns external factual verification, source trust, corroboration, and conflict handling.
- `execution-continuity-and-mode-selection.md` owns broad-continuation routing before leader raw absorption.
- `todo-standards.md` owns live task-list expectations and recovery boundaries when tracking is material.
- `project-documentation-standards.md`, `phase-implementation.md`, and `document-consistency.md` own master records and governed sync.

Review concerns:
- Do not over-delegate trivial one-source lookups.
- Do not turn standalone subagent research into mandatory Agent Team workflow.
- Do not let subagents return raw websearch dumps as if that protects leader context.
- Do not let live task/task-hook friction block worker routing when tracking is non-material or can be repaired.
- Do not import plugin/shared-board exact title grammar into Main RULES doctrine.
- Do not claim subagent findings are proof without leader verification.

---

## 3) Change Items

### P08102-001 — Native worker research orchestration refinement

- **Target artifacts:** `../native-worker-agent-routing-and-context-control.md`, `../design/native-worker-agent-routing-and-context-control.design.md`, `../changelog/native-worker-agent-routing-and-context-control.changelog.md`
- **Change type:** replacement / additive refinement

**Before**
```text
Native worker routing says broad external research and high-output evidence are worker-fit, prefers standalone subagent lanes, and requires analyzed handoff quality, but it does not explicitly define research-lane decomposition, subagent search strategy ownership, or leader context protection for design-improvement web research.
```

**After**
```text
Native-worker routing v1.2 adds a research orchestration gate: leader maps research objectives into focused lanes, subagents may refine topic/query strategy inside scope, research handoffs include source quality/conflicts/implications, and the leader synthesizes and verifies only selected high-value evidence instead of absorbing every raw result.
```

### P08102-002 — External verification and source trust integration

- **Target artifacts:** `../external-verification-and-source-trust.md`, `../design/external-verification-and-source-trust.design.md`, `../changelog/external-verification-and-source-trust.changelog.md`
- **Change type:** companion sync

**Before**
```text
External verification requires proactive checking, source trust ranking, corroboration, and conflict reporting, but it does not explicitly say broad source discovery/comparison may be delegated into research lanes while preserving source-trust duties.
```

**After**
```text
External-verification v1.2 allows broad or comparison-heavy external verification to be gathered through native worker research lanes, while keeping authoritative-source ranking, corroboration, conflict reporting, and leader evidence calibration intact.
```

### P08102-003 — Execution continuity integration

- **Target artifacts:** `../execution-continuity-and-mode-selection.md`, `../design/execution-continuity-and-mode-selection.design.md`, `../changelog/execution-continuity-and-mode-selection.changelog.md`
- **Change type:** companion sync

**Before**
```text
Execution continuity routes broad/noisy/context-heavy next slices through worker routing generally, but broad design-improvement research can still be read as a direct websearch continuation path.
```

**After**
```text
Execution-continuity v1.13 explicitly treats broad research/design-improvement continuation as a worker-routing trigger: decompose into research lanes or state a narrow direct-handling reason before leader raw search absorption.
```

### P08102-004 — Live task tracking friction boundary

- **Target artifacts:** `../todo-standards.md`, `../design/todo-standards.design.md`, `../changelog/todo-standards.changelog.md` if touched
- **Change type:** optional companion sync

**Before**
```text
Live task-list usage is expected for non-trivial active work, but the rules do not explicitly separate material tracking requirements from non-material task creation friction during bounded worker dispatch.
```

**After**
```text
If touched, TODO standards v2.24 clarifies that when live tracking is material, repair the task/tracking issue and keep phase linkage visible; when tracking friction is non-material to a bounded research lane, continue worker routing and report the tracking limit rather than collapsing delegation.
```

### P08102-005 — Master records and runtime install

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.86 with 44 active runtime rules and no P081-02 research orchestration refinement.
```

**After**
```text
Master records describe v9.87 with unchanged 44 active runtime rules, record P081-02 as a native-worker routing refinement, preserve README install arrays at 44 active runtime files, and record source/runtime parity after install.
```

---

## 4) Verification

- [x] Native-worker research orchestration chain is version-aligned.
- [x] Adjacent owner integrations are version-aligned where touched.
- [x] Master records describe v9.87 and active runtime count 44 consistently.
- [x] README Bash and PowerShell install arrays include exactly 44 active runtime files.
- [x] Runtime install parity is verified 44/44 for the active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.87` is created.

---

## 5) Rollback Approach

If the research orchestration wording proves too heavy:
- narrow the research orchestration gate to only broad/comparison-heavy external research
- preserve P081-01 standalone-subagent-first and intent-first routing baseline
- remove or narrow any TODO tracking-friction companion wording if it overreaches
- preserve source-trust and evidence-calibration boundaries even if research-lane wording is reduced
- reinstall the prior 44-rule runtime set only under a separate explicit rollback gate
