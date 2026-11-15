# Workflow Continuity Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.2
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.2
> **Full history:** [../changelog/workflow-continuity.changelog.md](../changelog/workflow-continuity.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Preserve ongoing discussion as well as resume selected work from checked state. Help the user and assistant remember accumulated details and multiple/branching threads through readable task records. Assess continuity risk and revisit value rather than imposing a schema, cadence or task count. Do not repeat completed work, take over peer-owned execution or cross a stop boundary; accepted meaning and matching proof still determine execution completion.

## Procedure Contract

Input is the latest user direction, current discussion or selected work, relevant records and available tools; execution also supplies its owner, required proof and stop condition. Proactively preserve accumulated discussion where continuity risk makes task records useful, including before a design is settled. Choose the next open question during discussion, or the next unmet gate during selected execution.

Use semantic granularity: update a fitting record, or selectively link an independently revisitable branch when that improves recall. No fixed template, tree, cadence, task count or transcript copy is required. Keep substantive requirements, alternatives, rationale, contract details and open/revised choices in readable content with their selection state. Retain valid prior detail, verify the meaningful recovery path and read relevant content on return. A short self-contained exchange need not create a task. Recording proposals does not authorize implementation or create execution dependencies. If supported tools/readback are unavailable, state the limit without inventing a backend or claiming persistence.

Compare records by outcome, ownership, acceptance and proof layer before treating statuses as conflicting. Preserve accepted outstanding threads when work is added, paused or reprioritized; record each thread's disposition and resume condition in the fitting existing owner. Reprioritization is not cancellation, while explicit user cancellation/replacement retires the affected thread. Assistant proposals remain unselected. Retire superseded plans while preserving genuine passes and independent deliverables. Continue independent selected safe work when one exact branch is blocked; otherwise name the enabling event and stop at that dependency.

The [task recovery reference](../references/task-recovery.md) owns selected record recovery; the [closeout reference](../references/closeout.md) owns a required durable/release handoff. Neither reference creates an obligation to recover a board, publish or create artifacts on every task.

Discussion output makes current threads, useful details, actual decisions and open questions easy to recover, with brief user-facing orientation only when useful. Execution output states what is complete at which proof layer, the current required action and owner, any exact blocker/resume condition and the applicable stop boundary. Optional successors remain unselected.

## Invariants and Failure Boundaries

- Memory, summaries and peer reports are leads, not fresh authority or proof that work ran.
- Missing records do not authorize resetting a board, recreating files or inferring completion. Preserve provenance and verify supported changes.
- Source/local and live gates may legitimately differ. Do not demote selected terminal proof or reopen a satisfied gate for optional observation.
- Queue acceptance, an acknowledgment or an edit is not terminal proof. Administrative uncertainty remains distinct from substantive acceptance.
- Do not duplicate peer-owned work or poll expected notices when other selected work can proceed.

## Ownership and Development

This Skill owns continuation, recovery and handoff procedure, not a particular board backend, session transport or personal checklist convention. Its local design and history follow the parent library's source-first maintenance contract. Installed same-name additions require separate reconciliation before deployment; this baseline does not migrate them.

## Verification

Use existing Skill-library checks for metadata, aligned versions, reference closure, portability and written continuation contracts. Exercise full drafts in bounded paired read-only contexts: sustained versus self-contained discussion, retained detail versus a useful new branch, proposed versus selected action, readable recovery versus metadata-only assumptions, and useful user orientation versus ceremony. Include reprioritization/cancellation and unavailable-tool boundaries. Synthetic interpretation is not native capture, runtime adoption or causal benefit. A changed procedure must also distinguish an independent runnable branch from a genuinely blocked dependency and preserve an explicitly required terminal gate. The initial governance addition preserves the operational body and both references, so it does not require a new board mutation or runtime scenario. A source check is not persisted-task or handoff-acceptance proof.
