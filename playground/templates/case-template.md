# Case XX — <scenario-family-name>

## What this case proves

One or two sentences describing the behavior impact this case family is meant to demonstrate.

---

## Scenario family

- Primary family: `<name>`
- Current status: governed baseline / observed examples present-or-absent / virtual variants available

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
- keep it factual and scoped
- do not turn one observed case into a global claim beyond the evidence held

---

## Virtual variant

This section is explicitly illustrative.

List a few plausible branches such as:
- branch A
- branch B
- branch C

Each virtual branch should remain compatible with the same checked rule behavior.

---

## Example dialogue (virtual unless explicitly observed)

### User
`<prompt>`

### AI without this rule family risk
`<ungoverned or weaker response>`

### AI with RULES active
`<governed response>`

---

## Flow diagram

```text
User request
  ↓
Initial decision point
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
2. update this case file's observed section
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
