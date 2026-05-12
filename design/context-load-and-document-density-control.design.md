# Context Load and Document Density Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.4
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-12)

---

## P093 Target-State Refinement: Aggregate Read-Burst Gate

The context-load owner now treats aggregate governance/code reads as one context-cost event.

Worker-first filtering is required before leader raw absorption when aggregate triggers apply. Skipping the gate blocks broad sync, no-drift, closeout, or release-ready claims unless a narrow direct-handling exception is stated.

Worker handoffs should return filtered findings, conflicts, exact anchors, and leader verification needs so the leader verifies selected anchors instead of absorbing every raw source.

---

## P092 Target-State Refinement: Automatic God Artifact Planning

The context-load owner now treats God artifact findings as actionable workflow events.

Detection must flow into classification, owner routing, action-mode selection, repair or visible planning, and closeout verification.

Clear touched-scope repairs happen immediately.
Broad, ambiguous, or owner-sensitive repairs become governed repair slices instead of warnings.

---

## P091 Target-State Refinement: God-Document Prevention

The context-load owner now treats file-level responsibility overload as part of the context lifecycle.

God-document candidates should be repaired by role-aware redistribution, design sharding, rollover, phase/patch splitting, or explicit follow-up.

Do not append more content into an overloaded active file when an owner-specific route exists.

## 1) Goal

Define a first-class RULES owner for context-load lifecycle management and document-density strategy.

The target outcome is practical:
- broad raw evidence is filtered before it burdens the leader session
- active docs stay cheap to read, edit, diff, and verify later
- clear low-risk God-line candidates in touched active docs are repaired opportunistically
- compact/thrash is treated as a signal to repair workflow or document structure
- the solution stays strategic instead of becoming a blunt post-compact restriction

พูดง่าย ๆ: ปัญหาไม่ใช่ว่า “อ่านเยอะไม่ได้” แต่คือ leader ไม่ควรอ่าน raw content กว้าง ๆ เองถ้า worker ช่วยกรองได้ และ docs ไม่ควรถูกเขียนเป็นบรรทัดยักษ์ที่ทำให้รอบถัดไปอ่านแพงกว่าเดิม.

---

## 2) Problem Statement

Observed failure modes:
- several individually bounded reads can combine into a large context burst
- line count can hide real size when markdown lines are thousands of characters
- leader sessions sometimes read raw design/changelog/TODO/phase/patch sets directly instead of routing broad review to a worker
- active summaries can become history dumps because new releases are appended to one dense line
- a small logical edit can produce a huge one-line diff when the target line is already too dense
- assistants may notice a touched God-line candidate but only warn instead of repairing a clear low-risk split
- compact/thrash can be misread as a need for rigid post-compact bans instead of a workflow and document-structure repair signal

The system needs an owner that connects these issues across reading, writing, worker routing, and closeout verification.

---

## 3) Target-State Model

### 3.1 Context lifecycle

Context load is managed before, during, and after work:
- before reading: define the question and route broad raw content through workers when appropriate
- while reading: consider aggregate output and line density, not only line count
- while writing: avoid creating future read/diff debt
- after compact/thrash: diagnose source patterns and repair structure

### 3.2 Leader and worker roles

Leader session:
- sets the question and scope
- chooses the authority surface
- dispatches workers for broad raw evidence
- verifies selected anchors
- makes the final decision and closeout claim

Worker lane:
- reads broad raw documents, logs, searches, or audits
- filters evidence into anchors, conflicts, risks, and verification needs
- reports checked scope without dumping raw bodies

### 3.3 Document-density model

Active documents should behave like navigable maps.

Preferred active-doc shape:
- short current-state bullets
- small focused tables
- separate verification and risk sections
- local low-risk repair of touched God-line candidates
- pointers to changelog/history/done detail
- compact parent indexes for sharded active designs

Unhealthy shape:
- one bullet carrying version history, current state, verification, caveats, exclusions, and next work
- append-only release timelines in active summaries
- repeated one-line replacement diffs larger than the logical change

---

## 4) Strategic Mechanisms

### 4.1 Question-first evidence routing

Before broad reading, ask what decision or sync claim needs evidence. This prevents generic “read all governance surfaces” behavior.

### 4.2 Aggregate read-burst awareness

A read plan should account for the sum of planned outputs. A sequence of bounded reads may still be too large if each file is dense.

### 4.3 Worker-first broad raw absorption

When raw evidence is broad, noisy, or multi-surface, workers should absorb and filter it before the leader reads selected anchors.

This extends worker-routing doctrine with a specific context-load reason: protecting the leader window is part of correctness, not only efficiency.

### 4.4 Opportunistic touched-doc repair

When the assistant is already editing an active document and a touched line is a clear, low-risk God-line candidate, the target state is immediate local repair in the same edit.

The repair should split mixed responsibilities without changing meaning.

If the split is broad, history-heavy, ambiguous, or likely to change meaning, the target state is explicit density-debt tracking instead of silent append-only growth.

### 4.5 Append-vs-restructure gate

Before adding to an active line, classify the new content and inspect the target line's responsibility.

If the line is already dense:
- split it when the repair is clear and low-risk
- move or flag it through the correct owner when it is not

### 4.6 Density-aware closeout

Governance sync should include a quick density check when touched docs are active entrypoints or review surfaces. Semantic sync is incomplete if the update leaves the next session with avoidable context debt.

---

## 5) Owner Boundaries

This rule owns:
- context-load lifecycle strategy
- aggregate read-burst control
- leader-context protection as a context-safety requirement
- document-density and God-line prevention
- opportunistic touched-doc God-line repair
- append-vs-restructure decision gates
- compact/thrash as repair signal

This rule does not own:
- exact worker scale mechanics, which stay with `native-worker-agent-routing-and-context-control.md`
- exact read caps, which stay with `safe-file-reading.md` and `safe-terminal-output.md`
- TODO/phase rollover semantics, which stay with `governed-document-rollover-control.md`
- design shard semantics, which stay with `document-design-control.md`
- version authority, which stays with changelog governance
- deletion authority, which stays outside density and hygiene signals

---

## 6) Acceptance Criteria

- The existing active runtime rule advances to v1.1 without adding a new runtime rule.
- README install arrays remain at the same 47 source-owned active runtime rule files.
- The rule tells assistants to repair clear low-risk touched active-doc God-line candidates in the same edit.
- The rule tells assistants to flag or plan broad, history-heavy, or meaning-risky density debt instead of silently appending.
- The rule preserves worker-first broad raw evidence filtering and compact/thrash repair signals.
- Master design, changelog, TODO, phase, and patch records describe v9.98 / P090-01 consistently.
- Source/runtime parity and active runtime body sufficiency pass for 47/47 runtime files.

---

## 7) Verification Notes

P090-01 verification should check both semantic governance sync and future-read cost.

Required verification categories:
- README Bash and PowerShell arrays contain the same 47 files
- runtime/design/changelog chain versions align at v1.1
- active runtime install parity passes for 47/47 files
- active runtime body sufficiency passes for 47/47 files
- touched active docs avoid new God-line style append dumps
- clear low-risk touched-doc God-line candidates are repaired or explicitly flagged
- broad final audit uses worker filtering when the scope is multi-surface
