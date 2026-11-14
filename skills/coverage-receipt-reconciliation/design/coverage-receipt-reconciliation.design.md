# Coverage Receipt Reconciliation Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.0
> **Full history:** [../changelog/coverage-receipt-reconciliation.changelog.md](../changelog/coverage-receipt-reconciliation.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Determine what existing test results prove against a selected acceptance gate. This is coverage accounting, not authority to admit new tests, run a larger suite, create a report schema or change persistent task status.

## Procedure Contract

Input is the selected behavior/contract inventory, existing case registry and available reports. Identify the actual owner case, selector, input form and pipeline boundary for each required workflow.

Bind evidence to its command, source/test artifacts, environment, lifecycle, reached assertions and terminal outcome. Inspect actual child outcomes and capture limits; a wrapper, partial record or peer summary does not replace the bound verdict.

Preserve passed, failed, blocked, untested and unreached states. Deduplicate by the underlying case/gate and relevant bindings, retaining provenance. Assess drift only against the owner, selector or lifecycle it can affect; rerun affected selected gates rather than invalidating all evidence by association.

Output gives the selected inventory, per-case disposition and evidence binding, deduplicated verified union, missing proof and exact resume condition for the existing workflow/status owner.

## Invariants and Failure Boundaries

- Registered, selected, executed, assertions reached and terminal outcome are distinct; none can silently stand in for the next.
- Missing bindings are unobserved, not invented. Fail-fast leaves later assertions unproved.
- Overlapping totals are not additive. Similar labels do not make different operations, input forms or boundaries interchangeable.
- Combined-path coverage requires a case that combines the conditions; separate passing fragments are insufficient.
- A checker expectation can be wrong without the underlying operation failing. Preserve valid evidence and distinguish unrelated drift.

## Ownership and Development

Software test validation owns useful proof selection/execution; workflow continuity owns resumption and persistent status. This Skill hands off accounting without creating another truth authority. Its local design/history follow the library's source-first contract; installed additions are not migrated by this baseline.

## Verification

Use existing Skill-library metadata, aligned version/link, portability and written-reconciliation checks. A changed accounting procedure should distinguish overlapping valid evidence from an unreached required case or an incompatible binding. The initial governance addition preserves the operational body and does not require new software tests or reports beyond source-contract checks. Local accounting does not establish external-service success, deployed behavior or measured benefit.
