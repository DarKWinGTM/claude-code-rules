# Phase 147-03 - Internal Helper Authority Boundary

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Parent Phase:** [phase-147-evidence-first-counter-analysis-and-owner-integrity.md](phase-147-evidence-first-counter-analysis-and-owner-integrity.md)
> **Phase ID:** 147-03
> **Status:** Verified — released in v10.59
> **Target Release:** v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/worker-routing-and-context.design.md](../design/worker-routing-and-context.design.md)
> **Patch References:** [../patch/internal-helper-authority-boundary.patch.md](../patch/internal-helper-authority-boundary.patch.md)

---

## Objective

Distinguish user-owned objective/durable coordination expansion from the smallest bounded support topology Claude may invoke inside an already selected objective to gather evidence, analyze, review, or verify work.

## Selected Semantic Obligations

1. New user-visible objective, materially wider scope, durable standing-role/Team expansion, and materially different coordination architecture remain advisory until selected.
2. Inside a selected objective, bounded helper topology is internally invokable under `worker-routing-and-context.md` when workload evidence justifies it.
3. One independent axis prefers one standalone lane; independent cells may use parallel standalone lanes; Team scale requires real shared dependencies, messaging, staged workflow, or durable role coordination.
4. Reuse aligned roles before spawning and respect user bans, write permissions, edit overlap, and shared-state isolation.
5. Helper output remains subordinate evidence input; Leader/Main retains source implementation, integration, verification, and completion claims.
6. Internal routing cannot widen objective, source authority, or mutation permission.

## Implementation Scope

- `authority-and-scope.md` / design / changelog → version `2.6`.
- Playground Cases 01 and 14 plus focused matrix cells.
- `worker-routing-and-context.md` remains byte-identical at `1.16`.

## Out of Scope

- new worker topology doctrine;
- changes to Agent/Teammate permissions or invocation mechanics;
- durable Team creation without dependency evidence;
- transferring Active Rule/source integration to helpers.

## Development Verification / TestKit Coverage

Verification route: `existing_test` through Cases 01/14 plus unchanged-owner byte checks.

Required branches:
- one bounded independent helper lane is internally selected without a routing-choice prompt;
- real Team dependency permits coordinated escalation inside the selected objective;
- user agent restriction blocks the prohibited mechanism while allowed direct/standalone handling remains bounded;
- new objective or durable Team expansion remains advisory;
- worker routing stays the canonical topology owner and byte-identical.

## Current Disposition

- Runtime/design/changelog implementation: implemented.
- Semantic/version, scenario, unchanged-owner, candidate/canonical/root installation parity, and fresh-public-master checks: passed in candidate scope.
- Annotated `v10.59` tag, GitHub Release identity, and fresh-public-tag verification: passed.

## Risks and Rollback

- Risk: internal invocation wording can be misread as authority to expand scope or mutate source.
- Containment: bind invocation to a selected objective, canonical routing checks, explicit permissions, and leader verification.
- Before publication, revert only this triad and bounded projections; after publication, use a corrective release.

## Exit Criteria

- Authority triad aligns at `2.6`.
- Worker routing remains unchanged at `1.16`.
- All helper/durable-expansion branches pass without authority transfer.
- Child status becomes `verified` only after full release gates pass.
