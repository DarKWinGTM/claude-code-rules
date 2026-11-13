---
name: workflow-continuity
description: Use when resuming interrupted work, recovering task records, reconciling workflow status, or preparing a continuation handoff.
---

# Workflow Continuity

Resume the selected outcome from checked state without repeating completed work or crossing its stop boundary. Tracking is a navigation aid; implementation, acceptance and matching proof determine what is actually complete.

## Procedure

1. **Re-anchor.** Read the latest user direction, selected outcome, current owner, required proof and explicit stop condition. Retire superseded plans and helper assignments; a short request to continue resumes that selected scope, not every visible proposal.
2. **Recover the smallest useful context.** Inspect existing task records and applicable design/execution documents, then the implementation or results needed to resolve uncertainty. Match source scope, freshness and proof layer. Summaries, memory and peer reports are leads, not fresh authority or evidence that work ran.
3. **Reconcile by meaning.** Compare outcome, owner, acceptance and proof layer before treating two statuses as contradictory. Distinct source/local and live gates may legitimately differ. Preserve passed gates, provenance and independent deliverables. Missing records are not permission to reset a board, recreate files or infer completion; follow [task-recovery.md](references/task-recovery.md) when recovery is actually selected.
4. **Choose the next unmet gate.** Continue independent selected safe work while an exact dependent branch is blocked. Do not duplicate peer-owned execution, poll expected notices or wait idly when runnable selected work remains. If every remaining step depends on one unchanged blocker, name the enabling event and stop there.
5. **Update at useful boundaries.** Keep settled result, proof pointer, pending obligation and resume condition in the fitting existing record when persistence matters. Use its supported status/dependency fields; do not create a task per file or command, another status authority or routine checkpoint ceremony.
6. **Respect completion and stop conditions.** An acknowledgment, edit or queue acceptance is not terminal proof. Close a satisfied bounded gate without reopening it for optional work; keep explicitly required terminal proof pending when unavailable. Do not demote a required check or let an unrelated aggregate failure block a scope that does not require it.
7. **Hand off or close.** Synthesize actual results into affected durable owners where required, preserve pending semantics and pass evidence to the existing finalization owner before the family closes. Use [closeout.md](references/closeout.md) for a governed documentation/release handoff, not for every small edit.

## Output

State what is complete at which proof layer, the current required action and owner, the exact blocker/resume condition if any, and the applicable stop boundary. Keep optional successors visibly unselected. Use the working language and the requested level of detail; no fixed board backend, session transport or personal checklist style is required.

Example: checks A and B passed, C awaits an authorized environment change, and selected D is independent. Preserve A/B, perform D, then stop only the work dependent on C. If C is an explicitly required terminal gate, the overall outcome remains pending even after D passes.
