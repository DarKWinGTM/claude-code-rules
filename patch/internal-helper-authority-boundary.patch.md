# Internal Helper Authority Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active — candidate verification and installation complete; publication identity pending
> **Target Design:** [../design/design.md](../design/design.md) v10.59
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

`authority-and-scope.md` said assistant-created Team expansion is advisory, while `worker-routing-and-context.md` requires Claude to choose and invoke the smallest helper topology inside selected work. The terms could be read as either blocking useful internal support or permitting unselected durable expansion.

## 2) Analysis

Risk: Medium. Transferring internal routing choices to the user preserves friction and research burden; treating all helper use as implicit authority can widen scope or create duplicate Teams.

Selected distinction:
- new objective, materially wider scope, durable standing-role/Team expansion, or different coordination architecture → advisory until selected;
- bounded support inside an already selected objective → internally invokable under the canonical routing owner when evidence/workload justifies it.

## 3) Change Items

### IHA-001 - Authority classification
- **Target:** `../authority-and-scope.md` and triad.
- **Before:** one team-expansion clause collapses durable expansion and bounded support.
- **After:** durable expansion remains user-selected; bounded helper topology may be invoked internally without widening objective or authority.

### IHA-002 - Routing-owner preservation
- **Target:** authority integration wording and unchanged `../worker-routing-and-context.md`.
- **Before:** the authority clause can appear to own spawn/invocation criteria.
- **After:** authority classifies advisory versus internally invokable scope; worker routing continues to own topology, reuse, permissions, handoffs, and leader verification.

### IHA-003 - Scenario projection
- **Target:** Cases 01 and 14 plus matrix.
- **After:** one bounded lane, real Team dependency, user restriction, and durable-expansion branches are explicit.

## 4) Verification

Candidate checks:
- authority triad aligns at `2.6`;
- `worker-routing-and-context.md` remains byte-identical at `1.16`;
- Cases 01/14 preserve user authority, reuse-before-spawn, dependency-based Team escalation, mutation permissions, subordinate output, and leader verification;
- no routing-choice prompt is required when one bounded helper path is already implied.

Candidate helper-authority scenarios, unchanged-owner proof, canonical/root installation, and fresh-public-master checks pass. Release proof remains pending until the annotated tag, GitHub Release identity, and fresh-tag-clone gates pass.

## 5) Rollback Approach

Before publication, revert only the authority triad and scenario projections; keep worker routing unchanged. After publication, use a later corrective release and never force-move the public tag.
