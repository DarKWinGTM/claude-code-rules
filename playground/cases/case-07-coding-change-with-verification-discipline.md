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

---

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
