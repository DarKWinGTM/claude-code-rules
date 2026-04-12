# Shared Execution Coordination

> **Current Version:** 1.0
> **Design:** [design/shared-execution-coordination.design.md](design/shared-execution-coordination.design.md) v1.0
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
| Session-lease clarity | High |
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
