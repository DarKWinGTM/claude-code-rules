# Shared Execution Coordination

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.10
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd (2026-04-15)

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

### 4.4 Group-Local Communication Principle
Live session-to-session communication should be scoped to sessions that already share the same task list / execution board group.

Required meaning:
- `CLAUDE_CODE_TASK_LIST_ID` should act as the standard upstream identity for the shared task-list boundary
- local board paths may still be derived internally from that id for runtime access, but should not replace the task-list id as the main public contract
- sessions outside that shared board group should not be treated as default live peers
- group membership should be derived from already-working shared execution surfaces rather than a new standalone broker

### 4.5 Peer-Request-Not-Takeover Principle
The live bridge should default to delivering additional work requests between peer sessions, not taking control of another session.

Required meaning:
- one session may request additional work or information from another session already working in that area
- the default interaction should not hard-interrupt or replace the target session's current execution context
- direct peer-to-peer requests inside the same group are allowed and do not need to route through one permanent leader session
- a session may temporarily act as an orchestrator without becoming the only central controller for the whole group

### 4.6 Board-Anchored Visibility Principle
Live bridge requests should remain visibly anchored to the shared task board rather than becoming hidden side-channel communication.

Required meaning:
- live requests should reference a shared task / request / objective anchor whenever practical
- sessions may communicate directly, but the existence and outcome of meaningful requests should still be visible in shared coordination history
- the board remains the shared visible execution record even when tmux transport is used to carry richer context

### 4.7 Low-Aggression Delivery Principle
The default live request style should be low-aggression and safe for parallel work.

Required meaning:
- the target session should be asked to finish its current safe slice first before switching to the additional request
- the live bridge should be optimized for richer request delivery, not for forceful interruption
- prompt wording and transport policy should avoid derailing the target session's current work unless a later explicitly selected urgent mode is introduced

### 4.7.1 Anchored-Task Board Reflection Principle
When bridge-side request/report state is reflected back into shared coordination surfaces, the first reflection step should prefer the existing anchored task.

Required meaning:
- if `board_ref` resolves safely to an existing shared-board task, that anchored task should be updated first
- reflection may use coarse native task fields plus clearly visible note text when task storage cannot represent the full lifecycle nuance directly
- reflection should fail closed when the anchor is ambiguous, missing, or unsupported
- bridge-side machine-readable request/report files must not become a second hidden authority or hidden history stack
- the first reflection wave should not auto-create a second hidden request/held/blocked task family by default

### 4.8 Context-Bridge Principle
Continuation should use the strongest available context bridge while keeping optional tools optional.

### 4.9 Continuity-First Retention Principle
Shared execution boards should be preserved by default within the same active objective.

### 4.10 Partial Cleanup Principle
Cleanup should retire eligible stale subsets rather than wiping the board.

### 4.10.1 Retention Matrix Principle
Retention should depend on task class and coordination state rather than one global cleanup reflex.

Required meaning:
- in-progress, blocked, pending-handoff, accepted-handoff, verification, and objective-anchor work should remain visible while it still matters
- fully completed and dependency-clear coordination history may become retirement candidates sooner than active execution records
- session-lease expiry should trigger reopen or reassign evaluation before retirement is considered

### 4.11 Optional-Extension Principle
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
- receive-side continuation should explicitly check whether memsearch is available before assuming the extension exists
- it should be used as a recall accelerator after stronger execution surfaces identify the relevant continuation target
- if unavailable or the availability/probe step fails, the coordination model should fall back immediately to native memory plus the checked baseline surfaces
- it is a supplemental context bridge, not semantic truth or required infrastructure

### 5.3 Future optional live coordination layer
`claude-peers-mcp` should be modeled as future optional live coordination infrastructure only.

Required meaning:
- it may later strengthen peer discovery, direct handoff, and live blocker resolution
- it should not be described as active RULES behavior until the rule layer explicitly adopts it
- if current-environment testing shows the required delivery path is blocked or non-operational, the mechanism should remain concept-only rather than being described as a viable current option
- if a candidate replacement such as `FileChanged` hook probing is documented but repeated runtime tests do not produce actual usable trigger behavior, that path should also remain `not yet usable` rather than being described as a viable current option
- a bounded `TaskCreated` validator may be added inside `claude-session-coordination@darkwingtm` for shared-task-list creation control when `CLAUDE_CODE_TASK_LIST_ID` is set
- such a validator should reject malformed session-state creation attempts with retryable feedback, still allow clearly open/shared task titles, and stay limited to creation until later waves explicitly widen the lifecycle coverage

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
