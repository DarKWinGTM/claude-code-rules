# Case 05 — Communication and Presentation Calibration

## What this case proves

This case family shows how RULES make answers clearer, more evidence-calibrated, and easier to understand without drifting into character voice or empty filler.

---

## Scenario family

- Primary family: communication and presentation calibration
- Current status: governed baseline; checked observed example present; virtual variants available

---

## Governing rules

- `communication-register.md` — natural professional tone, proposal evaluation, high-signal pruning
- `accurate-communication.md` — claim-strength wording and identifier-by-role explanation
- `explanation-and-presentation.md` — plain-language-first flow and concise action framing
- `audience-surface-disclosure-control.md` — keep direct-user explanation and audience-safe wording separate when needed

---

## Rule-enforced fact

Current RULES require the assistant to:
- lead with the point when the point matters most
- keep agreement and contradiction calibrated to checked evidence
- explain identifiers by role when raw names alone would be hard to follow
- keep simplified answers natural and non-character while avoiding stiff spec tone
- use concise structure that improves reading rather than ceremonial formatting

---

## Observed case

Checked observed example in repo scope:
- the released `v10.18 / P110` wave explicitly updated `accurate-communication.md`, `communication-register.md`, and `explanation-and-presentation.md` so identifiers are explained by system role and simpler wording stays non-character and proportional
- this observed effect is also recorded in `playground/observed/2026-05.md` as `O-2026-05-02`

---

## Virtual variant

- User asks for a simpler explanation of an internal field name.
- User proposes a direction that needs evaluation before agreement.
- A status update could be phrased as either noisy recap or concise snapshot.

Expected behavior: explain clearly, keep tone practical, and match wording strength to evidence.

---

## Example dialogue (virtual)

### User
`Explain proofWorkflow in plain language.`

### AI without this rule family risk
`proofWorkflow is the supplier-local proofWorkflow object with override semantics.`

### AI with RULES active
`พูดง่าย ๆ มันคือชุดกติกาที่บอกว่าระบบจะใช้วิธี proof แบบไหนในแต่ละกรณี และถ้ามี override มันจะเปลี่ยนจากค่า default ตรงไหนบ้าง.`

---

## Flow diagram

```text
User asks for easier explanation
  ↓
Important identifiers are identified
  ↓
Roles are translated into human meaning
  ↓
Tone is kept practical and non-character
  ↓
Compact, clearer explanation is returned
```

---

## Matrix axes in play

- request type: explanation / recommendation / status update
- evidence state: verified / partial / user-direction-only
- scope clarity: usually clear
- risk level: low to medium
- expected rule response: answer directly with evidence-calibrated wording and role-aware explanation

---

## Behavior delta

Without this family, the assistant can sound either too stiff or too casually certain.

With RULES active, the answer should become easier to understand, calmer, and more precise about what is fact versus recommendation.
