# Design - Safe I/O

> **Parent Rule:** [../safe-io.md](../safe-io.md)
> **Current Version:** 1.1
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/safe-io.changelog.md](../changelog/safe-io.changelog.md)

---

## Target State

`safe-io.md` is the active runtime owner for bounded file reading and terminal output with parent-index-first and worker-first behavior.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

P099 refinement extends the target state with delegate-first aggregate read/output burst signals, explicit burst-risk posture, and tighter coordination with worker-routing when leader raw intake would become the expensive path.

---

## Scope

This design owns the target-state shape for safe file reading, safe terminal output, sharded design/changelog reads, and high-output command control.

It also owns read/output-side delegation triggers for aggregate-read bursts and noisy command flows, while leaving routing topology and worker orchestration to `worker-routing-and-context.md`.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Keep the compact merged runtime set at 18 active root rules; P099 must not become a new root rule.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

Read/output burst detection stays here; worker topology selection, lane templates, and handoff orchestration stay in `worker-routing-and-context.md`.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.

P099 validation should also confirm the runtime body contains delegate-first burst signals, burst-risk wording in the I/O risk model, and command/read flow updates without widening the active runtime set.
