# Workflow Continuity Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.1
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.1
> **Full history:** [../changelog/workflow-continuity.changelog.md](../changelog/workflow-continuity.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Resume the selected outcome from checked state without repeating completed work, taking over peer-owned execution or crossing a stop boundary. Tracking helps navigation; accepted meaning and matching proof determine completion.

## Procedure Contract

Input is the latest user direction, selected outcome, owner, required proof and stop condition. Recover only the task, design, implementation and result context needed to identify the next unmet gate.

Compare records by outcome, ownership, acceptance and proof layer before treating statuses as conflicting. Preserve accepted outstanding threads when work is added, paused or reprioritized; record each thread's disposition and resume condition in the fitting existing owner. Reprioritization is not cancellation, while explicit user cancellation/replacement retires the affected thread. Assistant proposals remain unselected. Retire superseded plans while preserving genuine passes and independent deliverables. Continue independent selected safe work when one exact branch is blocked; otherwise name the enabling event and stop at that dependency.

The [task recovery reference](../references/task-recovery.md) owns selected record recovery; the [closeout reference](../references/closeout.md) owns a required durable/release handoff. Neither reference creates an obligation to recover a board, publish or create artifacts on every task.

Output states what is complete at which proof layer, the current required action and owner, any exact blocker/resume condition and the applicable stop boundary. Optional successors remain unselected.

## Invariants and Failure Boundaries

- Memory, summaries and peer reports are leads, not fresh authority or proof that work ran.
- Missing records do not authorize resetting a board, recreating files or inferring completion. Preserve provenance and verify supported changes.
- Source/local and live gates may legitimately differ. Do not demote selected terminal proof or reopen a satisfied gate for optional observation.
- Queue acceptance, an acknowledgment or an edit is not terminal proof. Administrative uncertainty remains distinct from substantive acceptance.
- Do not duplicate peer-owned work or poll expected notices when other selected work can proceed.

## Ownership and Development

This Skill owns continuation, recovery and handoff procedure, not a particular board backend, session transport or personal checklist convention. Its local design and history follow the parent library's source-first maintenance contract. Installed same-name additions require separate reconciliation before deployment; this baseline does not migrate them.

## Verification

Use existing Skill-library checks for metadata, aligned versions, reference closure, portability and written continuation contracts. A changed procedure should distinguish an independent runnable branch from a genuinely blocked dependency and preserve an explicitly required terminal gate. The initial governance addition preserves the operational body and both references, so it does not require a new board mutation or runtime scenario. A source check is not persisted-task or handoff-acceptance proof.
