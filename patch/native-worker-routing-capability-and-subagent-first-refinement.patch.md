# Native Worker Routing Capability and Subagent-First Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.80
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P081 refines the just-added P080 native worker-routing model after user testing showed two behavior gaps:
- the assistant could still treat pasted paths/logs from another session as a project-exploration request when the user was asking about AI/RULES behavior
- the worker model could still read as Agent Team-adjacent when the intended normal path is standalone subagent / worker-lane assistance

พูดง่าย ๆ: P081 ไม่ได้เพิ่ม rule ใหม่ แต่ทำให้ rule เดิมฉลาดขึ้น — classify intent ก่อน, ใช้ subagent-first สำหรับงาน broad, และอย่า over-task เป็น Agent Team ถ้าไม่ต้องใช้ shared coordination จริง ๆ.

This is a source/governance/runtime-install patch. It refines existing owner chains, keeps active runtime count at 42, and prepares v9.80.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `native-worker-agent-routing-and-context-control.md` owns worker routing and leader-context protection.
- `custom-agent-selection-priority.md` owns downstream best-fit specialist selection.
- `execution-continuity-and-mode-selection.md` owns discussion/execution mode and continuation boundaries.
- Runtime install must remain limited to README-listed active runtime rule files.

Review concerns:
- Do not add a new active runtime rule when an existing owner can be refined.
- Do not hardcode exact tool names as doctrine.
- Do not misread teammate / Agent Team restrictions as all-subagent bans.
- Do not make Agent Team the normal path for broad read/search/audit work.
- Do not let custom-agent selection become routing owner.
- Do not claim runtime parity until the 42-rule install/audit gate actually passes.
- Do not update memory for this correction; it belongs in RULES.

---

## 3) Change Items

### PAB-001 — Native worker routing subagent-first refinement

- **Target artifact:** `../native-worker-agent-routing-and-context-control.md`
- **Target design:** `../design/native-worker-agent-routing-and-context-control.design.md`
- **Change type:** additive / boundary clarification

**Before**
```text
The P080 rule defined native worker routing and a direct/subagent/multi-subagent/Agent Team scale model, but it did not yet emphasize intent-first behavior before project exploration or subagent-first handling strongly enough for the tested behavior case.
```

**After**
```text
The rule explicitly classifies user intent before broad work, treats pasted logs/paths as evidence for the active question rather than project authorization, routes by required capability and workload shape, prefers standalone subagent lanes for broad independent work, and keeps Agent Team as an exceptional coordination escalation.
```

### PAB-002 — Custom-agent capability-fit selection boundary

- **Target artifacts:** `../custom-agent-selection-priority.md`, `../design/custom-agent-selection-priority.design.md`, `../changelog/custom-agent-selection-priority.changelog.md`
- **Change type:** additive / boundary clarification

**Before**
```text
Custom-agent-selection-priority was already downstream of worker routing, but the capability-selection relation and non-escalation boundary were not explicit enough.
```

**After**
```text
Custom-agent-selection-priority chooses the best visible specialist for the required capability after native worker routing decides intent, worker need, and worker scale. It must not turn agent availability into a routing decision or escalate subagent-fit work into Agent Team workflow.
```

### PAB-003 — Execution-continuity intent recheck

- **Target artifacts:** `../execution-continuity-and-mode-selection.md`, `../design/execution-continuity-and-mode-selection.design.md`, `../changelog/execution-continuity-and-mode-selection.changelog.md`
- **Change type:** additive / boundary clarification

**Before**
```text
Execution-continuity routed broad next slices through worker routing, but it did not explicitly require rechecking intent when pasted project evidence might actually support a behavior/RULES question.
```

**After**
```text
Execution-continuity rechecks intent before project exploration, keeps behavior/RULES analysis in discussion/governance mode when appropriate, and then applies subagent-first worker routing before broad continuation.
```

### PAB-004 — Master record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** companion sync

**Before**
```text
Master records describe v9.79 with 42 active runtime rules and P080 as the current native worker-routing owner addition.
```

**After**
```text
Master records describe v9.80 with 42 active runtime rules and P081 as the subagent-first, capability-based, intent-first refinement to the P080 worker-routing model.
```

### PAB-005 — P081 phase record

- **Target artifact:** `../phase/phase-081-01-native-worker-routing-capability-and-subagent-first-refinement.md`
- **Change type:** additive

**Before**
```text
No P081 phase record exists.
```

**After**
```text
A P081 phase record tracks owner-chain refinement, governed sync, runtime install, parity verification, push, and release gates.
```

### PAB-006 — Runtime install and release boundary

- **Target artifacts:** README-listed active runtime rule files and `/home/node/.claude/rules/` deployed copies
- **Change type:** install / verification

**Before**
```text
The active runtime install set contains 42 source-owned runtime rule files from v9.79.
```

**After**
```text
The active runtime install set still contains 42 source-owned runtime rule files after copying only README-listed active runtime rules and verifying source/runtime hash parity for v9.80.
```

---

## 4) Verification

- [x] Native worker routing source/design/changelog updated to v1.1.
- [x] Custom-agent selection source/design/changelog updated to v1.3.
- [x] Execution-continuity source/design/changelog updated to v1.9.
- [x] Master records, README, TODO, phase, and patch describe P081/v9.80 consistently.
- [x] README Bash and PowerShell install arrays include exactly 42 active runtime files.
- [x] Golden scenarios pass: intent-first behavior, subagent-first broad work, capability-based routing, teammate/Agent Team restriction boundary, analyzed handoff, and leader verification.
- [x] Runtime install parity is verified for the 42 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.80` is created.

---

## 5) Rollback Approach

If P081 proves too broad:
- narrow the intent-recheck trigger wording
- keep subagent-first as a preference for broad independent worker-fit work, not a mandatory path for trivial work
- preserve the custom-agent downstream selection boundary
- preserve execution-continuity’s broad-work worker routing gate
- revert the master v9.80 docs only through a separate governed rollback
- do not delete destination/runtime files outside the source-owned install set as part of rollback without explicit destructive authorization
