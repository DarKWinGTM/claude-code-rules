# Proactive Analysis and Design Completeness Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active
> **Target Design:** [../design/design.md](../design/design.md) v10.58
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Current RULES can preserve selected design obligations during execution but do not generally require non-trivial analysis/design to proactively complete material omissions before the user specifies every detail.

## 2) Analysis

Risk: Medium. Too little guidance keeps the assistant passive; too much creates speculative overdesign, fabricated requirements, and option ceremony.

The target is proportional completeness: inspect only material decision inputs, recommend one best-supported route, and preserve evidence status and user authority.

## 3) Change Items

### PDC-001 - Canonical completeness gate
- **Target:** `../execution-and-goal-frame.md` and triad
- **Before:** completeness activation is largely bounded to selected governed design slices during execution.
- **After:** non-trivial analysis/design checks outcome, success conditions, constraints, dependencies, state/integration assumptions, failure behavior, verification, real alternatives, and a simpler sufficient path; it recommends the best-supported route without scope takeover.

### PDC-002 - Implementation consequence
- **Target:** `../coding-discipline.md` and triad
- **Before:** verification strategy exists, but a general happy-path completeness check is not explicit.
- **After:** material behavior/state/integration/failure/observability/verification gaps must be covered or explicitly disposed without speculative abstraction.

### PDC-003 - Communication and rendering
- **Target:** `../communication-register.md`, `../explanation-and-presentation.md`, and triads
- **Before:** high-signal pruning and decision-ready explanation exist but may prune material completeness findings or lack a compact recommended-route shape.
- **After:** retain findings that change decision/action/risk/dependency/verification and optionally render `Recommended`, `Why`, material constraints/dependencies, main trade-off/failure mode, and verification.

### PDC-004 - Scenario coverage
- **Target:** `../playground/cases/case-17-proactive-goal-surfacing-and-decision-ready-explanation.md`, `../playground/coverage.md`, `../playground/matrix.md`
- **After:** underspecified durable-design, real-alternative, simpler-path, evidence-boundary, advisory-divergence, and anti-overdesign variants are explicit.

## 4) Verification

Passed in candidate scope:
- four planned triads align to versions `1.29`, `1.24`, `1.23`, and `1.4`;
- Active Runtime Rule inventory remains 19;
- focused semantic/version checks cover the completeness and anti-overdesign obligations.

Passed in combined checked scope:
- simple/direct and non-trivial scenario variants pass as one checked set;
- no manufactured option list or fabricated project fact;
- force words and owner boundaries remain preserved;
- body sufficiency and canonical/root parity pass 19/19.

Pending:
- publication identity and fresh-public-clone parity/reproduction.

## 5) Rollback Approach

Before publication, revert only this patch's scoped clean-lane changes. After publication, use a corrective release; never force-move the public tag.
