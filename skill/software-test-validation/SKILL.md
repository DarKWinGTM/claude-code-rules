---
name: software-test-validation
description: Use when choosing verification for a software change, running tests or builds, investigating failed checks, or deciding what their results establish.
---

# Software Test Validation

Select proof that can change the decision, then run it through the existing test owner. The task's contract and risk determine useful depth, not a tool preference, file count or coverage quota.

## Procedure

1. **Name the claim and gate.** Identify changed behavior, material risk, success/failure signal and selected proof layer. A behavior-preserving refactor usually needs affected regression proof; an integration needs its real boundary exercised. Preserve explicitly selected terminal proof even when it is unavailable. Do not infer a required live, paid, browser or deployed check from generic completion wording.
2. **Identify the evidence gap.** Before adding a case, fixture or runner, state which failure current proof cannot distinguish. Reuse or extend an existing focused case when sufficient. Multiple layers are useful when they catch distinct faults; a new helper, percentage or test-to-code ratio alone does not justify more tests or their removal.
3. **Inspect the actual harness.** Check current commands, selectors, defaults, fixtures, lifecycle and assertions. A registered name or wrapper result does not prove the intended case ran. Use the project's existing runner and output owner; do not create another framework, report schema or Product path merely for test convenience.
4. **Use contract-valid inputs.** Exercise representative valid forms and the nearest meaningful negative/unchanged boundary. Keep fakes at external/test-owned boundaries and label substitutions. Drive the actual producer-to-consumer path when claiming integration; self-consistent handcrafted input does not prove the producer emits it. Observe durable effects independently if a child or observer may fail after commit.
5. **Run and capture.** Bind the exact command/selector, relevant source and fixture version, environment, terminal exit, material stderr and assertions reached. Bound noisy output without hiding failure. For asynchronous fixtures, release resources even when assertions fail; inspect child results, not only the wrapper's exit.
6. **Discriminate failures.** Inspect the earliest decisive failure and the owning contract before editing. Separate invalid fixture/expectation, test-infrastructure limits, pre-existing unrelated failures and a reproduced defect in the changed behavior. Correct only the selected owner or test boundary. Rerun affected checks after a material change, not an unchanged failure for reassurance; preserve passed results whose bindings remain valid.
7. **Close at the selected layer.** Cover material failure, persistence, retry, cleanup and recovery behavior only where the selected outcome depends on it. A missing optional observation is an explicit limit, not an invented blocker. An unavailable explicitly required check remains blocked with its target, prerequisite and observable resume condition.

For overlapping reports, use coverage-receipt-reconciliation to reconcile existing proof. For uncertain cause, use evidence-based-diagnosis-and-remediation. Neither referral selects a larger suite, new task family or live operation.

## Output

Report the command and scoped result, actual exercised behavior, reached/untested cases, substitutions and material remaining proof. Distinguish syntax review, build, focused test, local integration, rendered observation and live acceptance. A passing fake/local check does not establish deployment, external-service success, causal benefit or stability.

Example: a source-only adapter fix with a passing local persistence/retry test is verified at that local gate. A separate unapproved live observation is not a reason to reopen it; a user-selected live terminal gate would instead remain pending.
