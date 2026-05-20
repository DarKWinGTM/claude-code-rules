# Case XX — <scenario-family-name>

## What this case proves

One or two sentences describing the behavior impact this case family is meant to demonstrate.

---

## Scenario family

- Primary family: `<name>`
- Current status: governed baseline / transcript-grounded observed examples present-or-absent / virtual variants available

---

## Governing rules

- `<rule-file>.md` — short role
- `<rule-file>.md` — short role

---

## Rule-enforced fact

State only the behavior currently required by checked RULES.

Use this section for:
- what the assistant should do
- what the assistant should avoid
- what the assistant should ask or verify first

Do not place observed history or virtual exploration here.

---

## Observed case

Use one of these shapes:
- checked observed example with source anchors
- `No checked observed example recorded in repo scope yet.`

If you record an observed example:
- name the checked source surface
- if transcript-derived, record the exact checked transcript path
- add short anchor hints that another reviewer can search quickly
- say what the observed case proves in scope
- keep it factual and scoped
- do not turn one observed case into a global claim beyond the evidence held

Helpful transcript-derived subshape:
- Transcript path: `...jsonl`
- Anchor hints: `...`, `...`, `...`
- Observed effect: ...
- Scope note: ...

---

## Virtual variant

This section is explicitly illustrative.

List a few plausible branches such as:
- branch A
- branch B
- branch C

Each virtual branch should remain compatible with the same checked rule behavior.

---

## User objective

State the concrete thing the user is trying to get done in this scenario.

Keep it outcome-first and practical.

---

## Operational reality

State the actual working conditions that shape execution here.

Use this section for things such as:
- what evidence exists already
- what is missing
- what is blocked
- what capability or environment boundary matters
- what makes the request easy, risky, broad, or constrained

---

## RULES effect on execution

Explain how RULES change the assistant's operational behavior in this case.

Use this section for:
- what RULES force the assistant to check first
- what RULES prevent the assistant from doing by momentum
- what classification, guardrail, or routing behavior becomes active

This is the main behavior layer. Do not make dialogue the primary explanation.

---

## Decision

State the resulting operational decision clearly.

Examples:
- latest user instruction becomes the active path
- `verify first`
- `NEED_CONTEXT`
- `ALLOW_CONSTRAINED`
- ask before mutate
- downgrade the completion claim
- worker-route the broad lane before deeper raw intake

---

## What AI does next

List the next concrete AI actions that should happen under current RULES.

Keep it execution-shaped rather than rhetorical.

---

## Recovery path

State how safe progress can continue from the current state.

Use this section for:
- what the user can provide
- what evidence or approval would unblock the work
- what narrower safe path remains available now

---

## User-visible reply example

Give one compact example of what the assistant could say to the user after applying the operational decision.

If the case is virtual, keep the example compatible with that virtual boundary.

Dialogue, if included at all, should be supporting illustration only, not the main explanatory layer.

---

## Flow diagram

Optional. Use only when it helps clarify the operational decision flow.

```text
User objective arrives
  ↓
Operational reality is checked
  ↓
Relevant RULES intervene
  ↓
Decision is selected
  ↓
Next action / recovery path becomes visible
```

---

## Matrix axes in play

- request type: ...
- evidence state: ...
- scope clarity: ...
- risk level: ...
- expected rule response: ...
- turn count: ...
- user behavior: ...
- evidence source: ...
- failure mode: ...
- tool discovery or lane shape: ...
- completion state: ...

---

## Behavior delta

Describe what changes when RULES are active versus when the assistant is unguided.

Keep this section claim-calibrated:
- use grounded behavior language
- avoid invented capabilities
- do not rewrite the whole scenario as marketing prose

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
