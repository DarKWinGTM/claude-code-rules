# Context Load and Document Density Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-10)

---

## 1) Goal

Define a first-class RULES owner for context-load lifecycle management and document-density strategy.

The target outcome is practical:
- broad raw evidence is filtered before it burdens the leader session
- active docs stay cheap to read, edit, diff, and verify later
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

### 4.4 Append-vs-restructure gate

Before adding to an active line, classify the new content and inspect the target line's responsibility. If the line is already dense, split it or move historical detail to the correct owner.

### 4.5 Density-aware closeout

Governance sync should include a quick density check when touched docs are active entrypoints or review surfaces. Semantic sync is incomplete if the update leaves the next session with avoidable context debt.

---

## 5) Owner Boundaries

This rule owns:
- context-load lifecycle strategy
- aggregate read-burst control
- leader-context protection as a context-safety requirement
- document-density and God-line prevention
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

- A new active runtime rule exists and is included in the runtime install set.
- README install arrays move from 46 to 47 source-owned active runtime rules.
- The rule tells assistants to use workers as broad raw evidence filters before leader absorption.
- The rule defines God-line and append-vs-restructure doctrine for active governance docs.
- The rule frames compact/thrash as a repair signal rather than a simple post-compact restriction.
- Master design, changelog, TODO, phase, and patch records describe v9.97 / P090 consistently.
- Source/runtime parity and active runtime body sufficiency pass for 47/47 runtime files.

---

## 7) Verification Notes

P090 verification should check both semantic governance sync and future-read cost.

Required verification categories:
- README Bash and PowerShell arrays contain the same 47 files
- new runtime/design/changelog chain versions align at v1.0
- active runtime install parity passes for 47/47 files
- active runtime body sufficiency passes for 47/47 files
- touched active docs avoid new God-line style append dumps
- broad final audit uses worker filtering when the scope is multi-surface
