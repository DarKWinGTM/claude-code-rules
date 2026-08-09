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
- distinguish accepting an allowed direction from confirming a factual premise or endorsing it as the best route
- explicitly retract an earlier assistant recommendation when later evidence disproves its premise instead of silently switching position or saying only that the user was right
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
- User proposes a direction whose factual premise needs verification before agreement.
- Claude initially recommends the proposed replacement, but later checked source disproves the ownership premise.
- A status update could be phrased as either noisy recap or concise snapshot.
- Execution selects candidate/advisory-goal posture; communication and presentation must keep it high-signal and render it without becoming promotion authority.

Expected behavior: explain clearly, keep tone practical, and match wording strength to evidence. Accept an allowed direction without claiming its premise is proven; if the earlier recommendation fails, say that it is withdrawn/revised, name the failed premise and contrary evidence, then state the corrected recommendation and remaining gate. Do not replace that correction with praise or a bare `you were right`.

---

## User objective

Get an explanation or reply that is easier to follow without losing technical accuracy or evidence discipline.

---

## Operational reality

- The answer problem is presentation quality, not necessarily missing facts.
- Raw identifiers, stiff wording, or over-produced tone can obscure the real meaning.
- The assistant still has to preserve exact claim strength while simplifying the language.

---

## RULES effect on execution

- Lead with the point when it matters.
- Separate direction acceptance, factual confirmation, and route-quality endorsement.
- When checked evidence invalidates earlier advice, retract it explicitly and re-anchor from the contrary evidence.
- Explain important identifiers by role instead of leaving them as floating names.
- Keep the tone natural, non-character, and evidence-calibrated.
- Render execution-selected candidate/advisory output without independently selecting or promoting a candidate.

---

## Decision

Simplify and clarify the answer without upgrading certainty or dropping the checked technical meaning.

---

## What AI does next

- State the main point first.
- Verify decision-changing premises before agreement-shaped wording.
- If prior advice is disproved, state the withdrawal/revision, failed premise, contrary evidence, corrected route, and remaining gate.
- Translate important names into human-role explanations.
- Keep the wording simple, direct, and matched to the evidence held.

---

## Recovery path

- If the user wants a simpler version, keep reducing jargon one layer at a time.
- If the user wants deeper detail, expand the exact mechanism after the plain-language frame is clear.

---

## User-visible reply example

`proofWorkflow` คือขั้นตอนที่ระบบใช้ตัดสินว่าต้องพิสูจน์อะไรบ้างก่อนจะถือว่าผลลัพธ์เชื่อถือได้ — พูดง่าย ๆ มันคือกฎการเช็กก่อนสรุปผล.`

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

Without this family, the assistant can sound either too stiff or too casually certain, agree with a proposal above the checked evidence, or silently reverse an invalid recommendation.

With RULES active, the answer becomes easier to understand, calmer, and precise about direction versus fact versus recommendation quality; disproved assistant advice is explicitly retracted and re-anchored.
