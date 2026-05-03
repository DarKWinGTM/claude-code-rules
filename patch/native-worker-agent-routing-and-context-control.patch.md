# Native Worker Agent Routing and Context Control Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.79
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P080 responds to a native execution workflow gap: broad reads, searches, logs, docs, audits, and parallelizable work can overload the leader session when a bounded worker lane could filter or analyze the evidence first.

พูดง่าย ๆ: main Claude ควรเป็นคนคุมงานและ verify ไม่ใช่ต้องอ่าน raw ทุกอย่างเองเสมอ ถ้างานกว้างหรือ noisy ก็ควรพยายามใช้ subagent หรือ Agent Team อย่างเป็นระบบ.

This is a source/governance/runtime-install patch. It adds a first-class runtime rule owner and connects it to the existing custom-agent selection and execution-continuity chains.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `custom-agent-selection-priority.md` already owns best-fit specialist/custom-agent selection.
- `execution-continuity-and-mode-selection.md` already owns whether clear execution continues or stops.
- Existing evidence and communication rules already govern claim strength, handoff wording, and completion claims.
- Runtime install must remain limited to README-listed active runtime rule files.

Review concerns:
- Do not force agents into trivial tasks.
- Do not route by rigid tool-name mapping.
- Do not impose arbitrary handoff caps such as 300 words.
- Do not allow worker summaries to become proof without leader verification.
- Do not import plugin/shared-board/custom tmux bridge grammar into Main RULES doctrine.
- Do not claim runtime parity until the 42-rule install/audit gate actually passes.

---

## 3) Change Items

### PAA-001 — New native worker-routing owner

- **Target artifact:** `../native-worker-agent-routing-and-context-control.md`
- **Target design:** `../design/native-worker-agent-routing-and-context-control.design.md`
- **Change type:** additive

**Before**
```text
RULES did not have a source-owned Main RULES owner for proactive worker routing and leader-context protection. Related behavior existed in runtime/package-adjacent coordination material, but not as a first-class active runtime rule in this source set.
```

**After**
```text
A new active runtime rule owns worker-scale gating, workload-shape routing, native proactive worker use, subagent versus Agent Team scale decisions, analyzed handoffs, parallel edit containment, and main-controller verification.
```

### PAA-002 — Custom-agent selection integration

- **Target artifacts:** `../custom-agent-selection-priority.md`, `../design/custom-agent-selection-priority.design.md`, `../changelog/custom-agent-selection-priority.changelog.md`
- **Change type:** additive / boundary clarification

**Before**
```text
Custom-agent-selection-priority selected clear best-fit custom specialists, but the relation to a separate workload-routing owner was not explicit.
```

**After**
```text
Custom-agent-selection-priority remains the specialist selection owner after worker routing determines delegation is appropriate. It does not become the owner of broad-work routing or leader-context control.
```

### PAA-003 — Execution-continuity integration

- **Target artifacts:** `../execution-continuity-and-mode-selection.md`, `../design/execution-continuity-and-mode-selection.design.md`, `../changelog/execution-continuity-and-mode-selection.changelog.md`
- **Change type:** additive / metadata repair

**Before**
```text
Execution-continuity source metadata lagged its changelog state and did not explicitly say broad continuation should pass through the worker-scale gate.
```

**After**
```text
Execution-continuity aligns version metadata and adds the boundary that continuing into broad, high-output, or multi-surface next work should respect the native worker-routing gate.
```

### PAA-004 — Master record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** companion sync

**Before**
```text
Master records describe v9.78 with 41 active runtime rules and no P080 owner in the active runtime inventory.
```

**After**
```text
Master records describe v9.79 with 42 active runtime rules and P080 as the current native worker-routing and context-control refinement.
```

### PAA-005 — P080 phase record

- **Target artifact:** `../phase/phase-080-01-native-worker-agent-routing-and-context-control.md`
- **Change type:** additive

**Before**
```text
No active P080 phase record exists.
```

**After**
```text
A P080 phase record tracks source update, governed sync, runtime install, parity verification, push, and release gates.
```

### PAA-006 — Runtime install and release boundary

- **Target artifacts:** README-listed active runtime rule files and `/home/node/.claude/rules/` deployed copies
- **Change type:** install / verification

**Before**
```text
The active runtime install set contains 41 source-owned runtime rule files.
```

**After**
```text
The active runtime install set contains 42 source-owned runtime rule files after copying only README-listed active runtime rules and verifying source/runtime hash parity.
```

---

## 4) Verification

- [x] New rule/design/changelog triad exists and links resolve.
- [x] `custom-agent-selection-priority` remains selection owner, not routing owner.
- [x] `execution-continuity-and-mode-selection` version metadata and integration text are synchronized.
- [x] Master records, README, TODO, phase, and patch describe P080/v9.79 consistently.
- [x] README Bash and PowerShell install arrays include 42 active runtime files.
- [x] Golden scenarios pass: broad work delegates or justifies direct handling; trivial work stays direct; handoff is analyzed and proportionate; leader verification remains mandatory.
- [x] Runtime install parity is verified for the 42 active runtime rule files.
- [x] Source/runtime release artifacts are ready for git push and release v9.79.

---

## 5) Rollback Approach

If P080 proves too broad:
- narrow the worker-scale gate triggers
- keep the custom-agent selection boundary clarification
- preserve the direct-handling exception for trivial/tightly sequential work
- preserve leader verification and parallel edit containment
- remove the P080 file from README install arrays and master inventory only through a separate governed rollback
- do not delete destination/runtime files outside the source-owned install set as part of rollback without explicit destructive authorization
