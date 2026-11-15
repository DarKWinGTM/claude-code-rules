---
name: workflow-continuity
description: Use when preserving discussion threads or resuming work.
---

# Workflow Continuity

> **Current Version:** 1.2
> **Design:** [design/workflow-continuity.design.md](design/workflow-continuity.design.md) v1.2
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Full history:** [changelog/workflow-continuity.changelog.md](changelog/workflow-continuity.changelog.md)

Help the user and assistant remember evolving discussion threads as well as resume selected work from checked state. Tracking is shared working memory, not implementation permission or a second design authority; accepted meaning and matching proof still determine execution completion.

## Discussion continuity

Use task records proactively when accumulated detail, concurrent topics or branching questions create a meaningful continuity risk. Do not wait for settled decisions, docs sync or a compaction warning. For a short self-contained exchange, no task ceremony is needed. Choose timing and depth from context and revisit value, not a fixed template, turn count or mandatory checkpoint schedule.

Reuse the fitting topic record and selectively link an independently revisitable branch when that helps recall; this is not a mandatory tree or one task per message. Preserve substantive requirements, alternatives, reasons, contract details and open questions with their actual selection state. Retain valid prior detail when incorporating revisions. Keep critical context in readable record content; metadata may supplement it, but an unchecked metadata-only path is not sufficient recovery. Verify meaningful readback at continuity boundaries, and read relevant record contents after compaction or on return rather than relying on titles or update acknowledgments.

Make names and descriptions useful to the user. Give a brief orientation when it helps them find an unfinished thread, not a dashboard or report every turn. Recording a proposal does not authorize implementation or promote a topic link into an execution dependency. End discussion records at their selected boundary, not after each answer; open status does not guarantee retention or complete capture. If supported tools or readback are unavailable, disclose the limitation and continue useful conversation, not invent a backend, reset records or claim that capture succeeded. Later selected synthesis belongs at the governed design owner, not permanently in the task list.

## Procedure

1. **Re-anchor.** Read the latest user direction, current discussion or selected work, relevant constraints and stop boundary; identify owner and required proof where execution needs them. Preserve accepted outstanding threads when work is added, paused or reprioritized; reprioritization is not cancellation. Explicit user cancellation or replacement retires the affected thread, while assistant proposals remain unselected. Retire superseded plans and helper assignments; a short request to continue resumes that selected scope, not every visible proposal.
2. **Recover the smallest useful context.** Read relevant task details and applicable design/execution documents, then only the implementation or results needed for the current question. Keep material discussion context current without waiting for an execution plan. Match source scope, freshness and proof layer. Summaries, memory and peer reports are leads, not fresh authority or evidence that work ran.
3. **Reconcile by meaning.** Compare outcome, owner, acceptance and proof layer before treating two statuses as contradictory. Distinct source/local and live gates may legitimately differ. Preserve passed gates, provenance and independent deliverables. Missing records are not permission to reset a board, recreate files or infer completion; follow [task-recovery.md](references/task-recovery.md) when recovery is actually selected.
4. **Choose the useful continuation.** During discussion, continue the relevant open question or branch without manufacturing an implementation blocker. During execution, continue independent selected safe work while an exact dependent branch is blocked. Do not duplicate peer-owned execution, poll expected notices or wait idly when runnable selected work remains. If every remaining execution step depends on one unchanged blocker, name the enabling event and stop there.
5. **Update at useful boundaries.** Incorporate material changes while preserving still-valid discussion detail. For selected execution, give each thread its own changed, retained, blocked, deferred or completed disposition when an adjacent outcome settles; a newer objective or completed slice does not implicitly close another. Keep result, proof pointer, pending obligation and resume condition where needed. Use supported lifecycle fields; keep tentative or paused meaning explicit in the content. Do not create a task per file or command, another status authority or routine checkpoint ceremony.
6. **Respect completion and stop conditions.** An acknowledgment, edit or queue acceptance is not terminal proof. Close a satisfied bounded gate without reopening it for optional work; keep explicitly required terminal proof pending when unavailable. Do not demote a required check or let an unrelated aggregate failure block a scope that does not require it.
7. **Hand off or close.** Synthesize actual results into affected durable owners where required, preserve pending semantics and pass evidence to the existing finalization owner before the family closes. Use [closeout.md](references/closeout.md) for a governed documentation/release handoff, not for every small edit.

## Output

For discussion, make the current threads, useful detail, actual decisions and open questions easy to recover, with brief user-facing orientation when useful. For execution, state what is complete at which proof layer, the current required action and owner, any exact blocker/resume condition and the applicable stop boundary. Keep optional successors visibly unselected. Use the working language and requested depth; no fixed board backend, session transport or personal checklist style is required.

Example: a discussion gains a new constraint and an independent question. Retain the existing reasoning and still-open alternatives, update the fitting record and separate the new question only if it helps navigation. That record does not authorize implementation. In execution, if checks A/B passed, C is blocked and selected D is independent, preserve A/B, perform D and stop only C's dependent work. A required terminal C keeps the overall outcome pending.
