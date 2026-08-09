# Phase 147-01 - Premise Before Expansion and Explicit Retraction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Parent Phase:** [phase-147-evidence-first-counter-analysis-and-owner-integrity.md](phase-147-evidence-first-counter-analysis-and-owner-integrity.md)
> **Phase ID:** 147-01
> **Status:** Active — implemented; scenario/integration verification pending
> **Target Release:** v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/communication-register.design.md](../design/communication-register.design.md)
> **Patch References:** [../patch/evidence-first-counter-analysis-and-retraction.patch.md](../patch/evidence-first-counter-analysis-and-retraction.patch.md)

---

## Objective

Prevent Claude from letting the user proceed on a materially false current-system premise, while preserving valid goals, supported agreement, user authority, and proportionate handling for simple work.

## Selected Semantic Obligations

1. Separate intended outcome, checkable factual premise, proposed path, and requested action.
2. Inspect current implementation, semantic ownership, sibling roles, readers/writers, state, dependencies, and completed verification before material expansion/replacement.
3. Treat checked narrow completed work as the active baseline until evidence shows a real gap.
4. If the goal is valid but the premise is false, preserve the goal, correct the premise, explain the consequence, and recommend the smallest supported route.
5. If evidence is incomplete, use the narrow discriminating check instead of designing around uncertainty.
6. If broader ownership is proven, allow broader architecture with explicit state, migration, failure, and verification obligations.
7. Distinguish allowed-direction acceptance, factual confirmation, and best-route endorsement.
8. Retract invalidated assistant recommendations by naming the failed premise, contrary evidence, corrected recommendation, and remaining gate.
9. Do not manufacture disagreement when checked evidence supports the proposal.

## Implementation Scope

- `execution-and-goal-frame.md` / design / changelog → version `1.30`.
- `communication-register.md` / design / changelog → version `1.25`.
- Playground Cases 14, 17, and 05 plus focused matrix cells.

## Out of Scope

- ticket application or `data/tickets/` changes;
- broad rewrites of evidence, accuracy, safety, coding, presentation, or worker owners;
- policy that the user is usually wrong;
- model knowledge treated as project proof;
- ceremonial premise checks for trivial/one-path work.

## Development Verification / TestKit Coverage

Verification route: `new_testkit_scenario` through existing scenario families plus static semantic checks.

Required cases:
- false whole-domain retirement premise is corrected before downstream design;
- supported broader premise receives checked-strength agreement and completed design obligations;
- incomplete evidence selects one discriminating check;
- completed baseline is not reopened from analogy or confidence alone;
- prior assistant recommendation is explicitly withdrawn/revised after contrary evidence;
- supported proposal does not trigger artificial dissent.

## Current Disposition

- Runtime/design/changelog implementation: implemented.
- Focused semantic/version checks and `git diff --check`: passed in candidate scope.
- Playground, combined static, installation, publication, and fresh-clone gates: pending.

## Risks and Rollback

- Risk: premise verification becomes overbroad or delays safe direct work.
- Containment: activate only when a checkable premise materially changes architecture, behavior, risk, or scope.
- Before publication, revert only this child's scoped clean-lane changes; after publication, use a corrective release.

## Exit Criteria

- Both triads align at `1.30` and `1.25`.
- All required behavioral branches pass without contradicting user authority or evidence thresholds.
- Child status becomes `verified` only after governed sync, installation, and fresh-clone gates pass.
