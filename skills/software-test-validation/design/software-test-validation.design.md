# Software Test Validation Design

> **Parent Document:** [Portable Skill library](../../../design/design/skill-library.design.md)
> **Current Version:** 1.0
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Runtime Source:** [../SKILL.md](../SKILL.md) v1.0
> **Full history:** [../changelog/software-test-validation.changelog.md](../changelog/software-test-validation.changelog.md)
> **Chain Shape:** single-file-bootstrap

## Purpose and Scope

Select and execute proof that can change the decision for a software change. The selected contract, risk and evidence gap determine depth; a runner preference, file count or coverage quota does not.

## Procedure Contract

Input is the changed behavior, selected acceptance/proof layer, material risk and existing harness. Identify the fault current proof cannot distinguish before adding a case, fixture or runner.

Inspect actual commands, selectors, admission defaults, lifecycle and assertions. Use contract-valid representative inputs and the nearest meaningful negative or unchanged boundary. Exercise the real producer-to-consumer chain when claiming integration; isolate and disclose external substitutions.

Bind execution to the exact command, source/fixtures, environment, reached assertions and terminal outcome. Release asynchronous resources even when a check fails. Classify invalid expectations, infrastructure limits, unrelated failures and reproduced defects before correction; rerun affected checks after a material change.

Output names the command, scoped result, actual exercised behavior, reached/untested cases, substitutions and remaining selected proof.

## Invariants and Failure Boundaries

- A registered or selected case is not executed coverage, and wrapper success does not replace child outcomes.
- A new helper or test ratio alone does not justify more tests or removing existing proof. Reuse the fitting owner and runner.
- Keep source, build, focused tests, local integration, rendered observation and live acceptance distinct.
- Generic completion wording does not select a live, paid, browser or deployed gate. An explicitly required terminal check remains pending when unavailable.
- Preserve passed evidence whose bindings remain valid; an unrelated aggregate failure does not automatically expand a bounded task.

## Ownership and Development

This Skill owns proof selection/execution. Coverage receipt reconciliation accounts for existing overlapping results; evidence-based diagnosis handles unresolved causes. Referrals do not select another suite or operation. The parent library design owns source-first maintenance and separately selected deployment; local governance is not an extra test layer on every invocation.

## Verification

Use existing Skill-library metadata, link, portability and written-contract checks. For a changed decision, pair a case needing the selected check with a near-miss that must not acquire an invented gate or test campaign. The initial governance addition preserves the existing operational body and does not rerun application workflows. Static and synthetic results do not establish external-service success, deployment or user benefit.
