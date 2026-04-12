# Shared Execution Coordination

> **Current Version:** 1.2
> **Design:** [design/shared-execution-coordination.design.md](design/shared-execution-coordination.design.md) v1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/shared-execution-coordination.changelog.md](changelog/shared-execution-coordination.changelog.md)

---

## Rule Statement

**Core Principle: Treat a shared task list as an execution-coordination layer rather than semantic truth, make multi-session lease and handoff state explicit enough for real collaboration, preserve task continuity by default, and support optional context/communication extensions without requiring them.**

This rule owns multi-session shared execution coordination. It does not replace design, phase, TODO, execution-continuity, or memory-governance owners.

---

## Core Contract

### 1) Shared Execution Board Principle
A shared task list is the live execution board.
It is not the semantic truth for what the work means.

Required guidance:
- use the shared task list to coordinate who is doing what, what is blocked, what is handed off, and what is complete
- keep semantic truth in design, phase, `TODO.md`, and checked implementation state
- do not let the task list become the only owner of deep contract meaning

### 2) Coordination Record Principle
When multi-session work is materially active, each coordination task should make the execution state explicit enough for another session to continue safely.

Visible session identity should be strong enough that another session can tell at a glance which work is shared/open versus actively held by a specific session.

A coordination task should define, or clearly map to:
- logical owner or lane
- active session lease when relevant
- session provenance when relevant
- handoff state when relevant
- dependency / blocker state
- done criteria
- context references for continuation when relevant

Required guidance:
- use native task fields when they exist
- if the task surface lacks a native field for one of these semantics, encode it through stable task naming and/or structured description text instead of silently dropping the meaning
- keep one task focused on one real execution slice rather than packing several deliverables into one vague record

### 2.1) Recommended Coordination Types
When task classification helps scanability, prefer one of these coordination types:
- `Deliverable`
- `Blocker`
- `Verification`
- `Coordination`

This is a recommended classification aid, not a requirement that every task title use a rigid prefix.

### 2.2) Visible Session Identity Principle
Session-specific work should be visibly distinguishable from shared/open board work.

Required guidance:
- if a task is actively held by one session, handed off to one session, or blocked on one session, the visible task title should identify that session clearly enough for fast scanability
- shared/open tasks that are not yet session-held do not need a session id in the title by default
- do not hide session-held meaning only inside long description text when the compact board view is where coordination actually happens
- use a stable visible session-id pattern rather than mixing several ad hoc title styles for the same kind of session-held work

### 3) Session-Lease Principle
A task may be actively held by one session at a time without becoming that session's permanent property.

Required guidance:
- treat active session ownership as a lease, not as irreversible permanent ownership
- session provenance may remain visible after the lease moves
- the same task may be handed off, reclaimed, or resumed by a different session when the workflow requires it
- session disappearance or staleness should expire the lease, reopen the task, or move the task forward — not silently delete the task

### 4) Handoff Principle
Session-to-session work transfer should be explicit enough that the receiving session can continue without guessing.

Required guidance:
- prefer explicit handoff state over implicit "someone else will probably pick this up"
- a handoff should identify the target continuation task or context reference when that is materially useful
- receiving a handoff is not the same thing as proving the task is done
- acceptance, completion, return, or blocked follow-up should be visible in the shared execution board rather than left only in transient chat

### 4.1) Request-Layer vs Execution-Layer Principle
A shared execution board may contain request-layer items and execution-layer items, but those two layers should not be conflated.

Required guidance:
- use the shared board request layer for cross-session requests, handoffs, and coordination prompts
- use the receiving session's own execution layer for phase/objective/task-family organization after the work is accepted
- do not let a request-layer title masquerade as if it were already the receiving session's execution phase structure

### 4.2) Receiving-Side Phase Ownership Principle
Phase ownership belongs to the execution owner / receiving session.

Required guidance:
- phase labels should not be carried across sessions as the default visible handoff title label
- the sender may reference upstream phase context when useful, but that upstream phase should stay in handoff notes or description context by default rather than becoming the visible owner label
- if phase tracking is needed after acceptance, the receiving session should remap the work into its own phase, objective, or task family

### 4.3) Canonical Handoff Naming Principle
Cross-session request titles should prioritize the receiving session and the requested work, not the sender's phase label.

Required guidance:
- prefer visible handoff/request naming such as `For <session-short-id> owner: <work request>`
- use the same visible session-id style for comparable handoff/request tasks instead of mixing unrelated title patterns
- do not attach the sender's phase as the default visible request prefix when the work is being handed off to another session
- if source trace matters, store it in the description / handoff note instead of treating it like the receiving session's visible execution label

### 4.4) Handoff Note Principle
When cross-session context needs to travel with the task, keep that context in handoff notes rather than in overloaded visible title labels.

Useful handoff-note fields include:
- source session
- upstream context
- dependency note
- optional source phase reference
- receiving-session remap note

### 4.5) Accept-and-Remap Principle
Accepting a request-layer task and mapping it into the receiving session's execution structure are related but not identical actions.

Required guidance:
- a request-layer task may remain as coordination history even after acceptance
- the receiving session may create or update its own execution-layer task/phase/objective mapping after acceptance
- do not assume that the sender's phase naming should survive as the receiving session's execution identity

### 4.6) Handoff Lifecycle Principle
A shared-board handoff should move through explicit coordination states rather than jumping directly from request to forgotten history.

A useful lifecycle is:
- requested
- accepted
- remapped
- in_progress
- completed
- blocked
- returned

Required guidance:
- the exact storage shape may vary with tool limits, but the semantic state should still be legible
- acceptance should be visible before the work is treated as fully received
- remap should be visible when the work moves from shared request layer into the receiving session's execution structure
- blocked or returned states should remain visible enough that another session can understand why the handoff did not simply disappear

### 5) Context-Bridge Principle
Cross-session continuation should use the strongest available context bridge without making optional tooling mandatory.

Baseline continuation surfaces:
- shared task list
- active phase and `phase/SUMMARY.md`
- `TODO.md`
- design / checked implementation state
- native Claude memory when applicable

Optional stronger context bridge:
- memsearch or equivalent extension/plugin recall layer when available

Future optional stronger live coordination layer:
- `claude-peers-mcp` or equivalent peer-messaging layer

Required guidance:
- if memsearch is available, it may be used to improve cross-session recall and handoff accuracy
- when memsearch is available, prefer it as a recall accelerator after the shared board and active execution surfaces have identified the relevant continuation target
- do not let memsearch override checked task/phase/design/implementation evidence when those stronger surfaces already settle the active execution meaning
- if memsearch is unavailable, the coordination model must still function through the baseline surfaces
- treat memsearch as a supplemental context bridge, not as semantic truth or required infrastructure
- treat `claude-peers-mcp` as optional future live coordination infrastructure unless and until the active rule layer explicitly adopts it
- do not design the core coordination model so it fails when optional extensions are absent

### 6) Continuity-First Retention Principle
Do not clear the shared task list by default while the same active objective remains live.

Required guidance:
- prefer retain / reuse / extend over clear / recreate / wipe
- keep completed tasks visible long enough for handoff, audit, and execution continuity to remain followable
- do not clear the shared task list merely because another session resumed work in the same workspace
- do not clear the shared task list merely because a new slice inside the same active objective was discovered

### 6.1) Partial Cleanup Principle
If cleanup is needed, prefer partial retirement over full-board clearing.

Required guidance:
- prefer archive / retire / age-out behavior over blanket deletion
- cleanup should remove or retire only the eligible stale subset rather than wiping active and recent history together
- cleanup should preserve enough visible execution history that another session can still understand how the current state was reached

### 6.2) Aging Principle
Time-based cleanup may be used only as a bounded eligibility rule, not as blanket deletion policy.

Examples of potentially eligible stale classes:
- completed tasks with no unresolved dependency or handoff state
- stale coordination notes that no longer affect active execution
- expired session-lease records whose work has already been reopened, reassigned, or completed

Tasks that should not be aged out casually while the objective remains active:
- in-progress tasks
- blocked tasks
- pending or accepted handoff tasks
- verification tasks that still act as evidence gates
- objective-anchor tasks that still explain the active execution family

Required guidance:
- a bounded aging window may be used for cleanup eligibility when helpful, for example several hours such as a 6-hour stale threshold
- aging should move tasks toward retirement eligibility, not justify immediate blanket clearing
- time age alone should not override active dependency, blocker, handoff, or objective-anchor significance

### 6.3) Retention Matrix Principle
Retention should depend on task class and coordination state rather than one global cleanup reflex.

Required guidance:
- keep in-progress, blocked, pending-handoff, accepted-handoff, verification, and objective-anchor tasks visible while they still matter to the active objective
- allow fully completed, dependency-clear, and no-longer-relevant coordination tasks to become retirement candidates sooner than active execution records
- session-lease expiry should trigger reopen/reassign evaluation before retirement is considered
- if cleanup is performed, preserve enough visible history that another session can still reconstruct the recent execution path and handoff trail

### 7) Reset-Boundary Principle
Full reset is a special case, not the default maintenance action.

Full reset is appropriate only when one or more are true:
- the user explicitly asks for reset / clear
- the active objective is genuinely closed
- a clearly different new objective has opened
- durable archive/retirement behavior already preserved the necessary execution history elsewhere

Full reset is not justified merely because:
- a new session started in the same workspace
- a new slice of the same objective was discovered
- some tasks are old
- another session needs to see the board more clearly

### 8) Duplicate-Drift Prevention Principle
Shared execution boards should reduce duplicate work, not multiply it.

Required guidance:
- prefer updating, claiming, or handing off an existing relevant task before creating a near-duplicate task for the same execution slice
- if duplicate tasks already exist for the same slice, reconcile them instead of leaving both active as competing truths
- stable naming and/or structured task descriptions should help multiple sessions recognize that they are touching the same slice

---

## Verification Checklist

- [ ] Shared task list is treated as execution coordination rather than semantic truth
- [ ] Multi-session lease and provenance behavior is explicit enough for continuation
- [ ] Handoff behavior is explicit enough for cross-session continuation
- [ ] Session-held work is visibly distinguishable from shared/open board work
- [ ] Request-layer naming is distinct from receiving-side execution-layer naming
- [ ] Source phase is not used as the default visible handoff title label
- [ ] Receiving session remap behavior is explicit when accepted work needs phase/objective tracking
- [ ] Handoff lifecycle states are explicit enough to follow request -> accept -> remap -> execute / return / block outcomes
- [ ] Baseline coordination works without memsearch
- [ ] memsearch is treated as optional supplemental context bridge when available
- [ ] `claude-peers-mcp` is kept future-optional unless explicitly activated by later rule work
- [ ] Task continuity is preserved by default within the same active objective
- [ ] Cleanup behavior is partial / class-aware rather than blanket clearing
- [ ] Aging rules do not erase active blockers, handoffs, verification tasks, or objective anchors casually
- [ ] Session disappearance expires or reopens leases instead of silently deleting tasks

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Shared-board vs semantic-truth clarity | 100% |
| Multi-session handoff clarity | High |
| Visible session-held task clarity | High |
| Request-vs-execution layer clarity | High |
| Receiving-side phase ownership clarity | High |
| Session-lease clarity | High |
| Handoff lifecycle clarity | High |
| Framework usefulness without memsearch | High |
| memsearch optionality clarity | 100% |
| `claude-peers-mcp` future-optional boundary clarity | 100% |
| Unnecessary full-board clears | Low |
| Partial-retention / age-out correctness | High |
| Duplicate-task drift within one objective | Low |

---

## Integration

Related rules:
- [todo-standards.md](todo-standards.md) - keeps live-vs-durable tracking role and task-update discipline
- [phase-implementation.md](phase-implementation.md) - keeps current-phase task linkage and phase execution semantics
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - keeps continue/stop/next-work discovery semantics
- [project-documentation-standards.md](project-documentation-standards.md) - keeps repository execution-surface role model
- [memory-governance-and-session-boundary.md](memory-governance-and-session-boundary.md) - keeps memory applicability and optional-extension authority boundaries
- [authority-and-scope.md](authority-and-scope.md) - keeps overall precedence and user authority boundaries
