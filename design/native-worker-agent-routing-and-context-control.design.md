# Native Worker Agent Routing and Context Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-04)

---

## 1) Goal

Define a first-class rule chain for native worker routing so broad, high-context, high-output, or naturally parallel work is usually handled by the smallest effective standalone worker lane before the leader session absorbs raw evidence.

The intended outcome is practical: preserve the leader session as controller, verifier, and synthesizer while using subagents or comparable worker mechanisms to filter, research, audit, review, or implement bounded non-overlapping slices. Agent Team / teammate workflow remains available only as an exceptional escalation when shared coordination semantics are genuinely needed.

---

## 2) Problem Statement

Observed failure modes:
- the leader session reads/searches/log-reviews too much raw context directly and fills the context window faster than needed
- agent use happens only after the user explicitly asks, even when the work shape clearly fits a worker lane
- pasted paths/logs from another session can be misread as authorization to inspect a project when the user is really asking about AI/RULES behavior
- delegation is framed as rigid tool-name mapping rather than intent and capability-based workload routing
- a ban on teammate / Agent Team workflow can be overread as a ban on standalone subagents or other non-team worker tools
- Agent Team can be over-selected when one standalone subagent would cover the work with less coordination overhead
- worker handoffs are over-constrained by arbitrary word limits or under-constrained as raw dumps
- custom-agent selection can be confused with the earlier question of whether the work should be delegated at all
- execution continuity can push into the next broad slice without re-running an intent and worker-scale gate

The repository needs one source-owned Main RULES chain that says when the assistant should consider workers, how to choose the smallest effective worker structure, how subagent-first routing should work, and how leader verification remains mandatory.

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- Intent-first classification before project exploration or broad evidence absorption
- Worker-scale classification before broad main-session absorption
- Direct leader versus focused standalone subagent versus multiple subagents versus Agent Team escalation decisions
- Capability-based workload routing criteria
- Native proactive delegation behavior during real execution
- Team/teammate restriction boundary when standalone subagents remain allowed
- Worker handoff quality and proportionality
- Parallel edit containment
- Leader verification after worker output or edits
- Integration boundary with custom-agent selection and execution-continuity owners

### 3.2 Out of Scope
- Exact custom agent discovery/loading mechanics
- Exact tool-name taxonomies for every possible worker mechanism
- Exact shared-board task title grammar
- Plugin-owned shared-task-list coordination semantics
- Package-owned custom tmux bridge behavior
- Manual registration of external sessions into an official Agent Team
- Replacing task, phase, TODO, evidence, or safety owners

### 3.3 Boundary Principle
This chain decides whether a worker structure is appropriate, which capability is needed, and which scale fits. It does not decide which visible custom specialist is best once delegation is already appropriate; that belongs to `custom-agent-selection-priority.md`.

---

## 4) Target Behavior

### 4.1 Intent-First Gate
Before broad work begins, the assistant should classify what the user is actually asking for:
- AI behavior / RULES behavior / workflow compliance
- project fact-checking or codebase inspection
- implementation or refactor execution
- review/audit/verification
- explanation only

If the user asks about assistant behavior while pasting another session’s logs, those logs are evidence for behavior analysis. They are not automatic permission to inspect the project named in the logs.

### 4.2 Subagent-First Worker-Scale Gate
Before broad search/read/log/test/docs/governance absorption, the assistant should select one of:
- leader direct handling
- one focused standalone subagent or comparable worker lane
- multiple independent standalone subagents
- official Agent Team / teammates only when shared coordination is genuinely required

If broad worker-fit work stays in the leader session, the assistant should have a narrow reason such as triviality, tight sequencing, low output, exact interactive-control need, high edit overlap, unavailable worker tooling, explicit all-agent restriction, or user-directed direct handling.

### 4.3 Capability-Based Routing
Routing should be driven by:
- user intent and active scope
- needed context isolation
- context cost
- output noise
- broad read/search/filter capability
- independence
- domain or specialist reasoning need
- parallel value
- coordination need
- risk and verification burden
- edit overlap
- worker/tool availability
- whether the leader needs raw evidence or analyzed findings

This prevents brittle rules such as “always use agent for WebSearch” or “always use agent for grep.” The rule identifies the needed worker capability first, then selects the smallest available mechanism.

### 4.4 Team Restriction Boundary
A user restriction on `teammate` or `Agent Team` should block coordinated team workflow, not standalone subagents, `Agent(...)`, `Explore(...)`, read-only reviewer agents, auditor agents, or similar non-team worker mechanisms unless the user explicitly bans those too.

### 4.5 Handoff Contract
Worker output should be analyzed and proportionate. It should include only the material result, checked scope, evidence strength, conflicts or uncertainty, and next verification when useful.

Arbitrary generic handoff limits are not part of the target state. The output size should fit the actual task and evidence complexity.

### 4.6 Leader Verification
The leader session remains responsible for:
- final synthesis
- resolving conflicting worker findings
- inspecting changed artifacts after worker edits
- making evidence-calibrated completion and verification claims

---

## 5) Decision Model

```text
Incoming work or next execution slice
  ↓
What is the user intent?
  → AI/RULES behavior: answer from behavior/governance first
  → project fact/implementation/review: continue
  → unclear and outcome-changing: clarify or state bounded working scope
  ↓
Is broad/noisy/context-heavy/multi-surface/parallelizable work needed?
  → No: leader direct
  → Yes: worker-scale gate
  ↓
One bounded independent lane enough?
  → Yes: focused standalone subagent
  → No: continue
  ↓
Several independent read-only lanes with low coordination need?
  → Yes: multiple standalone subagents
  → No: continue
  ↓
Needs ownership, dependencies, messaging, or implementation/review/test/docs sync?
  → Yes: Agent Team / teammates only if allowed and justified
  → No: leader direct with narrow reason
```

---

## 6) Integration Boundary

| Rule | Relationship |
|---|---|
| [../custom-agent-selection-priority.md](../custom-agent-selection-priority.md) | Selects the best available custom/specialist agent after worker routing decides delegation and required capability |
| [../execution-continuity-and-mode-selection.md](../execution-continuity-and-mode-selection.md) | Ensures continuation rechecks intent and does not bypass the worker-scale gate |
| [../todo-standards.md](../todo-standards.md) | Live task list supports non-trivial active work and coordinated slices |
| [../phase-implementation.md](../phase-implementation.md) | Phase context shapes worker assignments when phased work is active |
| [../evidence-grounded-burden-of-proof.md](../evidence-grounded-burden-of-proof.md) | Evidence strength governs worker and leader claims |
| [../accurate-communication.md](../accurate-communication.md) | Handoff and completion wording must remain evidence-honest |
| [../zero-hallucination.md](../zero-hallucination.md) | Worker output must not be upgraded into unsupported certainty |

---

## 7) Success Criteria

This chain succeeds when:
- intent is classified before project exploration or broad evidence absorption
- broad work is delegated to a standalone worker lane or explicitly justified before raw leader absorption
- direct leader handling remains the default for trivial or tightly sequential work
- subagents are used first for bounded independent filtering/research/review lanes
- Agent Teams are used only when coordination semantics are worth the overhead and allowed by user direction
- teammate/Agent Team restrictions are not misread as standalone-subagent bans
- worker handoffs are analyzed and sized to the real evidence, not raw dumps or arbitrary caps
- custom-agent selection happens after routing, not before it
- leader verification remains mandatory before completion claims

---

> Full history: [../changelog/native-worker-agent-routing-and-context-control.changelog.md](../changelog/native-worker-agent-routing-and-context-control.changelog.md)
