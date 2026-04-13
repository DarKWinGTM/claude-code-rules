# Shared Execution Coordination

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)

---

## 1) Goal

Create one first-class rule chain for shared execution coordination so multi-session work can use a shared task list, optional memory/search aids, and future optional peer messaging without losing semantic authority boundaries or task-history continuity.

---

## 2) Problem Statement

The active RULES stack already contains useful pieces of the behavior:
- `todo-standards` defines the built-in task list as the live execution surface
- `phase-implementation` links active phases to the current task list
- `execution-continuity-and-mode-selection` continues work and discovers next unfinished slices from execution surfaces
- `project-documentation-standards` recognizes execution surfaces at the repository role-model layer
- `memory-governance-and-session-boundary` keeps memory as context rather than authority

But the repository still lacks one semantic owner for **multi-session shared execution coordination itself**.

Observed failure modes this design intends to close:
- task-list semantics are scattered across several owner chains, so multi-session coordination behavior lacks one explicit contract
- shared task lists coordinate work in practice, but lease / provenance / handoff state remains under-specified
- task lists are sometimes cleared too aggressively, making execution history and handoff follow-through harder to track
- optional tools such as memsearch may improve continuity, but the system still needs to work when those tools are absent
- future optional peer-messaging layers such as `claude-peers-mcp` may strengthen live coordination, but should not be treated as active required infrastructure before the rule layer explicitly adopts them

---

## 3) Scope and Boundary

### 3.1 In Scope
- shared task list as execution-coordination layer
- shared-board versus semantic-truth boundary
- session lease / provenance semantics
- handoff semantics
- context-bridge behavior across baseline and optional layers
- retention / aging / anti-overclear policy for shared execution boards
- duplicate-drift prevention for shared coordination boards
- optional memsearch layer as supplemental context bridge
- future optional `claude-peers-mcp` integration boundary

### 3.2 Out of Scope
- replacing phase semantics
- replacing memory applicability semantics
- replacing execution continuity / stop-gate semantics
- defining undocumented task-system internals that do not exist in the current environment
- activating `claude-peers-mcp` as a current required runtime dependency

### 3.3 Owner split
This chain should own the **coordination protocol**.
It should not take over the existing owners of:
- durable-vs-live tracking role
- phase semantics
- repository document-role semantics
- memory applicability
- continue/stop behavior

---

## 4) Core Model

### 4.1 Shared Execution Board Principle
A shared task list is the execution board, not the semantic truth.

### 4.2 Session-Lease Principle
Active session ownership should behave like a lease rather than permanent ownership.

### 4.2.1 Visible Session Identity Principle
Session-held, handed-off, or blocked-on-session work should be visibly distinguishable from shared/open board work.

Required meaning:
- visible session ownership should be the default board-facing standard for session-owned work, not a convention that only appears when a shared task-list path is active
- the same visible ownership discipline should apply whether the current task list is being used by one session or several sessions
- scan-time session identity should be strong enough that another session can tell which work is actively held versus generally available
- visible session identity belongs in the compact board-facing representation, not only in long description text
- comparable session-held work should use a stable visible session-id pattern rather than several ad hoc title styles

### 4.2.2 Session-State Grammar Principle
Visible session identity should use a small stable grammar that preserves state meaning rather than one universal ambiguous prefix.

Required meaning:
- request/handoff tasks may use `For <session-short-id> owner: <work request>`
- actively held execution tasks may use `<session-short-id> owner: <execution task>`
- blocked ownership-dependent tasks may use `Blocked on <session-short-id>: <task>` or an equivalently clear blocked-on-session pattern
- open/unclaimed tasks may remain sessionless or use an explicit open marker when helpful
- one exact phrase should not be forced across request, held, and blocked states if it collapses those meanings together

### 4.3 Handoff Principle
Cross-session work transfer should be explicit enough that the receiving session can continue without guessing.

### 4.3.1 Request-Layer vs Execution-Layer Principle
The shared board request layer and the receiving-side execution layer should remain distinct rather than collapsing into one title format.

### 4.3.2 Receiving-Side Phase Ownership Principle
Phase identity belongs to the execution owner / receiving session rather than the sender's visible request title.

### 4.3.3 Canonical Handoff Naming Principle
Cross-session requests should prioritize target-session visibility and requested work rather than carrying the sender's phase label as the default visible title prefix.

### 4.3.4 Handoff Note Principle
Source session, upstream context, dependency notes, and optional source phase should live in handoff notes/description rather than overloaded visible title labels.

### 4.3.5 Accept-and-Remap Principle
Receiving-side remap into phase/objective/task-family should happen after acceptance and belong to the receiver's execution structure.

### 4.3.6 Handoff Lifecycle Principle
Shared-board handoff should move through explicit coordination states rather than jumping directly from request to forgotten history.

Required meaning:
- a useful lifecycle includes requested, accepted, remapped, in_progress, completed, blocked, and returned states
- acceptance and remap should be distinguishable so request-layer history does not masquerade as receiving-side execution structure
- blocked or returned outcomes should remain visible enough that another session can understand why the handoff did not simply disappear

### 4.4 Context-Bridge Principle
Continuation should use the strongest available context bridge while keeping optional tools optional.

### 4.5 Continuity-First Retention Principle
Shared execution boards should be preserved by default within the same active objective.

### 4.6 Partial Cleanup Principle
Cleanup should retire eligible stale subsets rather than wiping the board.

### 4.6.1 Retention Matrix Principle
Retention should depend on task class and coordination state rather than one global cleanup reflex.

Required meaning:
- in-progress, blocked, pending-handoff, accepted-handoff, verification, and objective-anchor work should remain visible while it still matters
- fully completed and dependency-clear coordination history may become retirement candidates sooner than active execution records
- session-lease expiry should trigger reopen or reassign evaluation before retirement is considered

### 4.7 Optional-Extension Principle
memsearch and future peer-messaging layers may strengthen coordination, but the baseline coordination model must still function without them.

---

## 5) Extension-Layer Boundary

### 5.1 Baseline continuation surfaces
The baseline coordination model should work with:
- shared task list
- active phase and `phase/SUMMARY.md`
- `TODO.md`
- design / checked implementation state
- native Claude memory when applicable

### 5.2 Optional memsearch layer
memsearch should be modeled as an optional extension/plugin layer.

Required meaning:
- if available, it may improve cross-session recall and handoff accuracy
- it should be used as a recall accelerator after stronger execution surfaces identify the relevant continuation target
- if unavailable, the coordination model must still function through the baseline surfaces
- it is a supplemental context bridge, not semantic truth or required infrastructure

### 5.3 Future optional live coordination layer
`claude-peers-mcp` should be modeled as future optional live coordination infrastructure only.

Required meaning:
- it may later strengthen peer discovery, direct handoff, and live blocker resolution
- it should not be described as active RULES behavior until the rule layer explicitly adopts it

---

## 6) Retention and Aging Model

### 6.1 Retain-by-default rule
Within the same active objective, reuse and extension should be the default.

### 6.2 Full reset boundary
Full reset should be limited to:
- explicit user reset
- true objective closure
- truly new objective opening
- other explicit authority-driven reset conditions

### 6.3 Partial retirement rule
Cleanup should prefer archive / retire / age-out behavior over blanket clear.

### 6.4 Aging eligibility rule
Time age may make a task eligible for retirement, but should not override:
- active in-progress state
- blocker state
- handoff state
- verification relevance
- objective-anchor relevance

A bounded stale threshold such as several hours may be used as an eligibility signal, not as a blanket wipe rule.

---

## 7) Success Criteria

This chain succeeds when:
- the shared task list is explicitly recognized as execution coordination rather than semantic truth
- multi-session lease and handoff behavior are explicit enough for real continuation
- shared-board history is not cleared too aggressively by default
- partial cleanup is supported without destroying coordination history
- memsearch improves coordination when available but is not required
- future optional `claude-peers-mcp` planning stays clearly outside active RULES behavior until explicitly adopted
- adjacent owner chains can defer coordination-specific semantics here without losing their own correct narrower roles
