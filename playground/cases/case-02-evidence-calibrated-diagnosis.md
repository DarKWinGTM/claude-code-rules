# Case 02 — Evidence-Calibrated Diagnosis

## What this case proves

This case family shows how RULES stop diagnosis from turning a visible failure into a verified root cause before the checked evidence actually supports that jump.

---

## Scenario family

- Primary family: evidence-calibrated diagnosis
- Current status: transcript-grounded observed example present; virtual variants available

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
- separate symptom, checked evidence, working hypothesis, likely cause, and next-best check
- avoid stating a root cause as verified without enough evidence
- report checked scope when something was not found
- recalibrate earlier wording if new evidence shows the first claim was too strong

---

## Observed case

Checked transcript-derived example:
- Transcript path: `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/0242764f-4e83-4651-bc03-3cc5c1055cd1.jsonl`
- Anchor hints: `internal_routing_failure`, `สิ่งที่ evidence ตัวนี้พิสูจน์ได้จริง`, `Diagnose gateway not-yet-product`
- Observed effect: after a user-facing auth/verifier error surfaced, the assistant explicitly recalibrated what the evidence proved, separated symptom from cause, and chose a bounded next-best check instead of endorsing the most convenient explanation.
- Scope note: this proves evidence-first diagnosis behavior in that checked session; it does not prove a universal root cause for similar errors.

---

## Virtual variant

- User says the config is definitely wrong, but only one source has been checked.
- A failing command suggests one likely branch, but several causes still remain live.
- A search misses a symbol in one folder, but the full repo has not been checked.

Expected behavior: verify further or state the limit, rather than upgrading the concern into a verified cause.

---

## Example dialogue

### Dialogue label
`virtual trace patterned on a checked transcript-derived observed case`

### Turn 1 — User
`PAYG customer auth fails with {"error":{"code":"internal_routing_failure","message":"PAYG customer auth Backend verifier is unavailable"}}. What broke?`

### Turn 1 — AI without this rule family risk
`The backend verifier is definitely down. I’ll treat that as the root cause.`

### Turn 1 — AI with RULES active
`I have a real symptom and one strong clue, but not a verified cause yet. I’ll separate what this error proves from what it only suggests before I name the next check.`

### Turn 2 — Evidence, correction, or blocker
`The checked session also contains a follow-up correction section around “สิ่งที่ evidence ตัวนี้พิสูจน์ได้จริง”.`

### Turn 2 — AI without this rule family risk
`That still means the verifier is the cause.`

### Turn 2 — AI with RULES active
`This proves the request hit an internal routing failure and surfaced a verifier-related message. It still does not prove whether the verifier is down, misrouted, or blocked by another dependency.`

### Turn 3 — Next-step narrowing / recovery / closeout
`A deeper inspection will need broader reads across the verifier path and its dependencies.`

### Turn 3 — AI with RULES active
`The next-best check is a bounded read-only investigation of the verifier path and dependency chain. I’ll keep the diagnosis wording evidence-calibrated until that broader evidence is checked.`

---

## Flow diagram

```text
User reports visible symptom
  ↓
Initial error evidence is checked
  ↓
Symptom is separated from cause hypothesis
  ↓
New evidence forces wording recalibration
  ↓
Next-best check is chosen
  ↓
Scoped diagnosis is reported
```

---

## Matrix axes in play

- request type: diagnosis
- evidence state: partial → transcript-grounded
- scope clarity: mixed until broader checks happen
- risk level: medium
- expected rule response: verify first and keep cause wording scoped
- turn count: 3
- user behavior: clear request followed by evidence-based correction pressure
- evidence source: tool output plus transcript anchor
- failure mode: overclaim risk
- tool discovery or lane shape: bounded read-only follow-up
- completion state: not applicable

---

## Behavior delta

Without this family, the assistant can sound confident too early and turn a symptom into a verdict.

With RULES active, diagnosis becomes more trustworthy because claim strength stays proportional to checked evidence and can be recalibrated when stronger evidence arrives.
