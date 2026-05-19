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

## Example dialogue

Use this section for a realistic trace, not a one-line slogan.

Preferred shape:
- 3-6 turns when the case is non-trivial
- at least one realism cue such as user correction, arriving evidence, blocker, retry, or narrowed next step
- explicit label when the dialogue is virtual, transcript-grounded, or mixed
- keep the dialogue compatible with the checked rule behavior and observed evidence boundary

### Dialogue label
`virtual` / `transcript-grounded` / `mixed`

### Turn 1 — User
`<prompt>`

### Turn 1 — AI without this rule family risk
`<ungoverned or weaker response>`

### Turn 1 — AI with RULES active
`<governed response>`

### Turn 2 — Evidence, correction, or blocker
`<new evidence or follow-up turn>`

### Turn 2 — AI without this rule family risk
`<ungoverned or weaker follow-up>`

### Turn 2 — AI with RULES active
`<governed follow-up>`

### Turn 3 — Next-step narrowing / recovery / closeout
`<next step or bounded closeout>`

### Turn 3 — AI with RULES active
`<governed next step>`

---

## Flow diagram

```text
User request
  ↓
Initial read
  ↓
Evidence / correction / blocker arrives
  ↓
Relevant RULES intervene
  ↓
Adjusted reasoning / action path
  ↓
Governed response or next step
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
2. update this case file's observed section and realism trace
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
