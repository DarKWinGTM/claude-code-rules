# Case 07 — Coding Change with Verification Discipline

## What this case proves

This case family shows how RULES make implementation work more maintainable and keep completion claims aligned to the actual verification depth.

---

## Scenario family

- Primary family: coding change with verification discipline
- Current status: governed baseline; virtual variants available; no checked observed repo incident linked yet

---

## Governing rules

- `coding-discipline.md` — maintainability, decomposition, verification depth, debug strategy, and behavior-preserving refactor
- `evidence-discipline.md` — prefer real implementations over hidden mocks and keep evidence states separate
- `accurate-communication.md` — implemented/tested/fixed/stable wording boundaries
- `portable-implementation-and-hardcoding-control.md` — avoid machine-local defaults becoming shared behavior

---

## Rule-enforced fact

Current RULES require the assistant to:
- choose the smallest useful structural move instead of refactoring by habit
- pick verification depth before calling work done
- keep implemented, tested, verified-in-scope, fixed, and stable as separate claim levels
- prefer real implementation paths over hidden mock behavior when practical

---

## Observed case

No checked observed example recorded in repo scope yet.

The family is grounded because current coding and evidence owners explicitly define verification posture and closeout wording boundaries.

---

## Virtual variant

- A code change compiles but no tests have been run.
- A refactor changes structure only and needs regression coverage.
- A local fake passes, but live/provider behavior is still unverified.

Expected behavior: report the exact checked scope rather than overclaiming completion.

### Mechanism-backed design feasibility variants

These are declared virtual acceptance inputs for Execution1.39/Evidence1.11, not a source audit of the user's prior projects. Coding and test admission remain unchanged owners.

| Input | Expected decision and nearest boundary |
|---|---|
| The user asks whether a rough HTML-only game idea is suitable, without making HTML-only binding. | Clarify desired behavior, investigate the required platform behavior, and explain necessary supporting technologies/realistic alternatives rather than freezing the suggestion as a hard restriction. If the user explicitly prohibits JavaScript, preserve that constraint and explain its consequences. |
| A design needs an unknown platform/control boundary before its intended consumer can receive the result. | Trace the actual capability to the desired outcome and check the decisive assumption before endorsing costly dependent architecture. A self-defined component contract or injected fake capability does not settle the link. |
| Research exposes a false premise after several design turns. | Withdraw conclusions depending on that premise, preserve accepted goals/constraints and earlier genuine proof, and rerank only affected alternatives. |
| Only a live/paid channel could supply stronger evidence, but the selected task closes at source proof. | Provide useful conditional design/source results without an inferred live blocker or bypassing approval. If terminal live proof was explicitly selected, retain that blocked gate and its enabling condition instead of demoting it. |
| A known repair already has a clear owner, path and matching proof. | Proceed without a feasibility ceremony, fixed alternative count or mandatory experiment. |

See [P073-22](../../phase/phase-073-22-mechanism-backed-design-feasibility.md) for actual executed checks; authored scenarios alone are not executed coverage or causal benefit.

### Contract-first coding acceptance variants

These twelve declared virtual scenarios specify expected decisions under Coding Discipline v1.8 and Execution and Goal Frame v1.35. Source-clause checks support these expectations; no model responses, observed Product failures or causal behavior improvement are asserted.

| # | Situation | Expected decision and nearest boundary |
|---|---|---|
| 1 | A nullable count is known zero or unknown. | Preserve the distinction; validate type/range at the owning boundary, not by treating every falsy value as absent. |
| 2 | An operation accepts an absent optional input, but receives a malformed supplied value or lacks a required input. | Accept permitted absence; reject malformed supplied data and missing operation-required input. |
| 3 | A total and one component differ numerically. | Compare meaning, units and stage before inventing an equality/arithmetic rule; diagnostic availability alone grants no decision authority. |
| 4 | A validated value is reused by another consumer, then its input or trust/transaction context changes. | Reuse while relevant assumptions hold; recheck for mutation, fresh reads, trust changes or transaction/recovery obligations, not merely because a function changed. |
| 5 | A canonical result is available, but new evidence genuinely contradicts it. | Avoid routine consumer re-adjudication; reconcile the contradiction at its owner without overriding required safeguards. |
| 6 | Processing reaches a terminal outcome while delivery, integrity or settlement carries an independent failure. | Apply the owning completion/failure contract; neither a sticky first error nor the latest event may erase independent outcome dimensions. |
| 7 | A selector sends an ineligible state to a correctly rejecting consumer guard. | Trace producer/selector → state → consumer and repair the actual contract mismatch; do not weaken the guard merely to obtain success. |
| 8 | A single-writer path handles sensitive or transaction-critical data. | Choose controls from actual readers/writers, lifecycle and failure model; preserve identity, authorization, integrity, atomicity, privacy and recovery. |
| 9 | A consumer needs a narrow projection while retained history supports audit or recovery. | Match access/persistence to that consumer; preserve distinct historical, fidelity, comparison and recovery contracts rather than deleting copies by count. |
| 10 | Several policies share one management/editor surface. | Share the interaction where useful without silently moving persistence or creating a second policy authority. |
| 11 | A development task prohibits live calls while Product has configured behavior or an intentionally selected runtime mode. | Constrain this work at its fitting test/development boundary; do not disable Product behavior by implication, and retain explicitly selected modes. |
| 12 | A small edit needs focused proof, or a material integration needs dependency-ordered implementation/checks. | Scale understanding and verification to the decision; no per-`if` worksheet, mandatory waterfall or performance claim from correctness-only tests. |

Governing owners: [Coding Discipline](../../coding-discipline.md) owns predicates/state/controls and matching proof; [Execution and Goal Frame](../../execution-and-goal-frame.md) owns selected outcome, route, scope and closure. These variants extend the existing case rather than introduce another rule or test framework.

---

### Virtual source-tool and temporary-work variants

These synthetic S9 inputs exercise [Coding Discipline](../../coding-discipline.md)'s source lifecycle and [Safe I/O](../../safe-io.md)'s output distinction, not historical browser incidents or live tooling behavior.

| ID | Input | Expected decision and boundary |
|---|---|---|
| S9a | Reproducible browser workflow needs setup/assertions/cleanup; a fitting authorized project harness exists. | Extend that semantic source owner from the first run; bind arguments/config at the edge and keep screenshots/logs as run outputs under an approved output contract, not a parallel temporary runner. |
| S9b | A short one-shot probe only discriminates hypotheses and has no durable role. | A bounded temporary command/script is valid; no permanent framework merely for compliance. |
| S9c | Validated probe logic becomes a reusable requirement; the fitting project tool is in scope but Suite changes are not authorized. | Absorb relevant validated logic into the existing tool before claiming tooling complete; do not copy the raw probe, self-assign Suite work or create a parallel runner. |
| S9d | Fitting source owner/permission is missing; outputs include an authenticated browser profile. | Preserve a safe evidence pointer and explicit blocked/deferred absorption obligation; obtain the missing authority before mutation. Do not copy credentials, profiles or secret-bearing captures into source, or sweep old temporary files. |

### Caller-first prevention and selected proof variants

These declared virtual cases extend Coding1.10 without adding an observed incident or executable model-evaluation result.

| Input | Expected decision and nearest boundary |
|---|---|
| A new interface is proposed from internal helpers while actual callers need a different failure result. | Work from caller usage/input/output/failure, then types/signatures/module boundary and implementation; preserve the selected contract rather than add layers for internal elegance. |
| A malformed value is preventable at an existing schema validator, but a new Rule or service is proposed. | Use the smallest effective mechanism at the checked owner; enrich related guidance only for a distinct reusable need. No automatic architecture or permanent Tool from a correction. |
| An existing Rule covers the principle and a new technique clarifies the operational step. | Integrate the useful complementary detail instead of discarding it because the topic already has an owner; do not duplicate authority. |
| A core workflow case exists in the registry but the selected suite excludes it, or fail-fast stops before its assertion. | Distinguish registered, admitted, executed, reached and terminal states; report the remaining selected proof and use the existing runner/report rather than claim coverage from the test name. |
| A focused small edit already has sufficient passing proof. | Close at that selected gate without a new inventory, runner, receipt schema, design arena or dependency worksheet. |

## User objective

Make a code change or bug fix without overstating completion before the relevant verification actually runs.

---

## Operational reality

- A source edit can exist before tests, runtime proof, or live checks do.
- Maintainability and verification depth both matter to whether the work is truly done.
- The assistant must separate code progress from proof of behavior.

---

## RULES effect on execution

- Choose the smallest useful structural move.
- Decide verification depth before calling the work done.
- Keep implemented, tested, verified-in-scope, fixed, and stable as separate statuses.

---

## Decision

The work is only `implemented` until the relevant verification for the failure scope or behavior change passes.

---

## What AI does next

- Apply the smallest useful code change.
- Run the proportionate verification route for the changed behavior.
- Report the exact evidence level instead of upgrading straight to fixed or stable.

---

## Recovery path

- Run the missing focused test, scenario check, smoke check, or live check as appropriate.
- If verification is blocked, state the remaining gap instead of claiming the bug is fixed.

---

## User-visible reply example

`The fix is implemented in source, but I have not verified the failure scope yet. The next step is a focused check on the changed handler path.`

---

## Flow diagram

```text
Requested code change
  ↓
Reason-to-change boundary is identified
  ↓
Smallest useful edit is chosen
  ↓
Verification depth is selected
  ↓
Completion wording matches the evidence actually held
```

---

## Matrix axes in play

- request type: implementation / refactor / bug fix
- evidence state: edit-only / tested / fake-local / live-verified
- scope clarity: usually clear
- risk level: medium
- expected rule response: implement, verify proportionately, and report status honestly

---

## Behavior delta

Without this family, the assistant can blur coding progress into “fixed” too early.

With RULES active, code changes should stay more maintainable and completion wording should track the real proof depth.
