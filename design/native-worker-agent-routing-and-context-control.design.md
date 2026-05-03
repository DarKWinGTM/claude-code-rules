# Native Worker Agent Routing and Context Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-03)

---

## 1) Goal

Define a first-class rule chain for native worker routing so broad, high-context, high-output, or naturally parallel work can be split into subagent or Agent Team lanes before the leader session absorbs every raw evidence surface.

The intended outcome is practical: preserve the leader session as controller, verifier, and synthesizer while using workers to filter, research, audit, review, or implement bounded non-overlapping slices.

---

## 2) Problem Statement

Observed failure modes:
- the leader session reads/searches/log-reviews too much raw context directly and fills the context window faster than needed
- agent use happens only after the user explicitly asks, even when the work shape clearly fits a worker lane
- delegation is framed as rigid tool-name mapping rather than workload routing
- worker handoffs are over-constrained by arbitrary word limits or under-constrained as raw dumps
- custom-agent selection can be confused with the earlier question of whether the work should be delegated at all
- execution continuity can push into the next broad slice without re-running a worker-scale gate

The repository needs one source-owned Main RULES chain that says when the assistant should consider workers, how to choose the smallest effective worker structure, and how leader verification remains mandatory.

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- Worker-scale classification before broad main-session absorption
- Direct leader versus focused subagent versus multiple subagents versus Agent Team decisions
- Workload-shape routing criteria
- Native proactive delegation behavior during real execution
- Worker handoff quality and proportionality
- Parallel edit containment
- Leader verification after worker output or edits
- Integration boundary with custom-agent selection and execution-continuity owners

### 3.2 Out of Scope
- Exact custom agent discovery/loading mechanics
- Exact shared-board task title grammar
- Plugin-owned shared-task-list coordination semantics
- Package-owned custom tmux bridge behavior
- Manual registration of external sessions into an official Agent Team
- Replacing task, phase, TODO, evidence, or safety owners

### 3.3 Boundary Principle
This chain decides whether a worker structure is appropriate and which scale fits. It does not decide which visible custom specialist is best once delegation is already appropriate; that belongs to `custom-agent-selection-priority.md`.

---

## 4) Target Behavior

### 4.1 Worker-Scale Gate
Before broad search/read/log/test/docs/governance absorption, the assistant should select one of:
- leader direct handling
- one focused subagent
- multiple independent subagents
- official Agent Team / teammates

If broad worker-fit work stays in the leader session, the assistant should have a narrow reason such as triviality, tight sequencing, low output, exact interactive-control need, high edit overlap, unavailable worker tooling, or user-directed direct handling.

### 4.2 Workload-Shape Routing
Routing should be driven by:
- context cost
- output noise
- independence
- parallel value
- coordination need
- risk and verification burden
- edit overlap
- worker/tool availability
- whether the leader needs raw evidence or analyzed findings

This prevents brittle rules such as “always use agent for WebSearch” or “always use agent for grep.”

### 4.3 Native Execution Behavior
The assistant should proactively look for worker-fit lanes during real work. Agent usage should not be treated as a separate mode requiring the user to request agents every time.

### 4.4 Handoff Contract
Worker output should be analyzed and proportionate. It should include only the material result, checked scope, evidence strength, conflicts or uncertainty, and next verification when useful.

Arbitrary generic handoff limits are not part of the target state. The output size should fit the actual task and evidence complexity.

### 4.5 Leader Verification
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
Is broad/noisy/context-heavy/multi-surface/parallelizable?
  → No: leader direct
  → Yes: worker-scale gate
  ↓
One bounded independent lane enough?
  → Yes: focused subagent
  → No: continue
  ↓
Several independent read-only lanes with low coordination need?
  → Yes: multiple subagents
  → No: continue
  ↓
Needs ownership, dependencies, messaging, or implementation/review/test/docs sync?
  → Yes: Agent Team / teammates
  → No: leader direct with narrow reason
```

---

## 6) Integration Boundary

| Rule | Relationship |
|---|---|
| [../custom-agent-selection-priority.md](../custom-agent-selection-priority.md) | Selects the best available custom/specialist agent after worker routing decides delegation is appropriate |
| [../execution-continuity-and-mode-selection.md](../execution-continuity-and-mode-selection.md) | Ensures continuation into broad next work does not bypass the worker-scale gate |
| [../todo-standards.md](../todo-standards.md) | Live task list supports non-trivial active work and coordinated slices |
| [../phase-implementation.md](../phase-implementation.md) | Phase context shapes worker assignments when phased work is active |
| [../evidence-grounded-burden-of-proof.md](../evidence-grounded-burden-of-proof.md) | Evidence strength governs worker and leader claims |
| [../accurate-communication.md](../accurate-communication.md) | Handoff and completion wording must remain evidence-honest |
| [../zero-hallucination.md](../zero-hallucination.md) | Worker output must not be upgraded into unsupported certainty |

---

## 7) Success Criteria

This chain succeeds when:
- broad work is delegated or explicitly justified before raw leader absorption
- direct leader handling remains the default for trivial or tightly sequential work
- subagents are used for bounded independent filtering/research/review lanes
- Agent Teams are used only when coordination semantics are worth the overhead
- worker handoffs are analyzed and sized to the real evidence, not raw dumps or arbitrary caps
- custom-agent selection happens after routing, not before it
- leader verification remains mandatory before completion claims

---

> Full history: [../changelog/native-worker-agent-routing-and-context-control.changelog.md](../changelog/native-worker-agent-routing-and-context-control.changelog.md)
