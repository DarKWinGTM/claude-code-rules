---
name: coverage-receipt-reconciliation
description: Use when reconciling overlapping test reports, conflicting coverage claims, partial executions or the validity of previous test results.
---

# Coverage Receipt Reconciliation

Determine what existing results actually prove against the selected acceptance gate. This procedure owns coverage accounting; software-test-validation selects/runs useful proof, and workflow-continuity owns continuation and persistent status.

## Procedure

1. **Derive the selected inventory.** Start from current behavior/contracts and the existing case registry. For each required workflow, identify its actual owner case, accepted selector and input/pipeline boundary. Distinguish registered, selected, executed, assertions reached and terminal outcome. A case name or registration is not a pass.
2. **Bind the evidence.** Check the recorded command, exact selector, relevant source/test artifacts, execution environment and lifecycle. Use existing native report fields; missing bindings are unobserved, not invented. Compare the actual command contract rather than a truncated display or guessed argument count.
3. **Respect the capture boundary.** Inspect the terminal exit, child results and assertions actually reached. A later diagnostic, partial JSON record or peer summary cannot replace a bound gate verdict. If the checker had a wrong expectation, correct it and reuse matching valid evidence rather than calling that a Product failure.
4. **Preserve distinct outcomes.** Mark passed, failed, blocked, untested and unreached separately. Fail-fast leaves later assertions unproved. Preserve earlier genuine passes; a selected compound run cannot claim its unexecuted tail.
5. **Deduplicate by underlying case/gate.** Retain provenance while reporting the verified union, not the sum of overlapping totals. Distinct operations, input forms or pipeline boundaries are not interchangeable merely because their labels look alike. Combined-path coverage needs a case that actually combines the required conditions.
6. **Reconcile drift proportionately.** Identify which changed artifact affects which owner, selector or lifecycle. Preserve results whose relevant bindings remain valid; rerun only affected selected gates unless acceptance or a freshness requirement needs a new run. Describe unrelated metadata drift rather than claiming all artifacts unchanged.

## Output

Give the selected inventory, per-case result and evidence binding, deduplicated verified coverage, missing proof and exact resume condition. Hand this to the existing status/checklist owner; a discrepancy does not itself authorize new tests, tasks, a report schema or a second evidence authority. Local results do not establish external-service or deployed behavior.

Example: reports covering cases 1–5 and 4–7 establish seven unique passed cases when their bindings match. A selected eighth case stopped before its assertion remains unreached; do not call all eight complete or sum the overlapping reports to nine.
