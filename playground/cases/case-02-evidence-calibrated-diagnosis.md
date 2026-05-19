# Case 02 — Evidence-Calibrated Diagnosis

## What this case proves

This case family shows how RULES prevent diagnosis from jumping too quickly from symptom or concern into verified root-cause language.

---

## Scenario family

- Primary family: evidence-calibrated diagnosis
- Current status: governed baseline; virtual variants available; no checked observed repo incident linked yet

---

## Governing rules

- `evidence-discipline.md` — symptom vs hypothesis vs likely cause vs verified cause
- `accurate-communication.md` — scoped non-finding and claim-strength wording
- `communication-register.md` — avoid verdict-style contradiction without evidence
- `explanation-and-presentation.md` — root-cause walkthrough shape
- `safe-io.md` — bounded reads and scoped file/output checks

---

## Rule-enforced fact

Current RULES require the assistant to:
- separate symptom, checked evidence, working hypothesis, and next-best check
- avoid stating a root cause as verified without enough evidence
- report checked scope when something was not found
- use diagnosis wording that shows what is known, suggested, and still unproven

---

## Observed case

No checked observed example recorded in repo scope yet.

The family remains grounded because the runtime owners explicitly define diagnosis shape, claim states, and scoped non-finding behavior.

---

## Virtual variant

- User says “the config is definitely wrong,” but only one file has been checked.
- A failing command suggests one likely branch, but several causes still remain live.
- A search misses a symbol in one folder, but the full repo has not been checked.

Expected behavior: verify further or state the limit, rather than upgrade the concern into a verified cause.

---

## Example dialogue (virtual)

### User
`The database connection is wrong. Fix it.`

### AI without this rule family risk
`The root cause is definitely the env variable. Change DATABASE_URL to ...`

### AI with RULES active
`I understand the concern, but I have not verified that conclusion yet. I will check the current config source first, then separate symptom, checked evidence, and likely cause.`

---

## Flow diagram

```text
User reports symptom
  ↓
Evidence scope is checked
  ↓
Symptom is separated from cause hypothesis
  ↓
Next-best check is chosen
  ↓
Scoped diagnosis is reported
```

---

## Matrix axes in play

- request type: diagnosis
- evidence state: partial / conflicting / concern-only
- scope clarity: usually mixed until more checking is done
- risk level: medium
- expected rule response: verify first or state uncertainty at the correct strength

---

## Behavior delta

Without this family, the assistant can sound confident too early.

With RULES active, diagnosis should become more trustworthy because claim strength stays proportional to checked evidence.
