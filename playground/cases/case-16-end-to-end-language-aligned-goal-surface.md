# Case 16 — End-to-End Language-Aligned Goal Surface

## What this case proves

This case family shows how RULES keep the full visible goal surface aligned to the user's active-exchange language: candidate-goal labels, promoted `/goal`, surrounding recommendation labels, recap/closing lines, and the natural-language scaffold around preserved exact literals all follow the same language unless a checked exact literal should remain exact.

---

## Scenario family

- Primary family: end-to-end language-aligned goal surface
- Current status: governed baseline present; observed + virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — make candidate-goal labels, promoted `/goal`, recommendation labels, and recap/closing lines follow the dominant language of the active exchange end-to-end
- `explanation-and-presentation.md` — keep output examples and wrapper labels language-surface-neutral or active-exchange-language-driven instead of English-first by habit
- `accurate-communication.md` — keep candidate goals, promoted `/goal`, recap wording, and scaffold text around preserved exact literals language-aligned while preserving exact literals when they should remain exact
- `communication-register.md` — keep the visible goal surface aligned to the user's working language without turning exact tokens into cosmetic translations
- `phase-todo-artifact.md` — keep `/goal` sourcing slots semantic rather than mandatory English surface labels and keep exact-literal preservation token-scoped rather than block-scoped

---

## Rule-enforced fact

Current RULES require the assistant to:
- follow the dominant language of the active exchange across candidate-goal labels, promoted `/goal`, recommendation labels, recap/closing lines, and the natural-language scaffold around preserved exact literals even when the user has not given a direct language instruction
- treat an explicit user language request as a stronger override, not as a prerequisite for alignment
- preserve exact literals such as `/goal`, file paths, version tags, code-level identifiers, and query parameters when they should remain exact
- treat `Done when` / `Prove with` / `Scope` / `Keep` / `Stop after` as concept-slot examples rather than mandatory English output labels
- keep several live next directions as candidate goals first and promote only the best-supported governed candidate into advisory `/goal` form
- reject wrapper-only translation where the wrapper changes language but the goal-shaped body still remains in another language beyond preserved exact literals

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/1f1873d2-0feb-485f-a5ff-d383254590dd.jsonl`
- Anchor hints: `แนะนำใช้คำสั่งนี้:`, `/goal Done when ephonechat_structured`, `ขอเป็นภาษาไทย`
- Observed effect: after a Thai-first active exchange, the assistant translated the wrapper but left the promoted `/goal` body in English-first template wording. The body only shifted after the user pointed out the language mismatch, which proves wrapper-only translation was still surviving when the active exchange language was already clear enough.

---

## Virtual variant

- A user has been communicating in one main language through the active exchange without issuing a direct language instruction.
- The current work slice is complete enough that two next directions are live.
- One direction is a bounded governed repo slice that qualifies for advisory `/goal` promotion.
- The assistant also wants to add a short recap line after the recommendation.

Expected behavior: the assistant should not localize only the wrapper while leaving the goal-shaped body in another language. It may keep `/goal` exact, but the surrounding natural-language scaffold and recap should stay in the same active-exchange language.

---

## User objective

Get a next-step recommendation that feels like one coherent response in the same working language as the current exchange rather than a translated wrapper around a body that still follows another language template.

---

## Operational reality

- The user's active working language across the current exchange is usually obvious even without a direct language command.
- One governed next direction is bounded enough for advisory `/goal` promotion.
- The assistant may still need to keep exact literals such as `/goal`, file paths, and query parameters unchanged.
- The visible wrapper labels and recap line are part of the user-facing surface, not decorative extras outside the language policy.

---

## RULES effect on execution

- Read the dominant language of the active exchange before emitting candidate-goal labels, wrapper labels, or goal-shaped body text.
- Treat a direct language instruction as a stronger override if the user gives one.
- Keep exact literals exact only where exactness matters.
- Avoid wrapper-only translation around a still-foreign goal body.
- Keep the recap/closing line in the same dominant language as the rest of the visible goal surface.
- Promote only the best-supported governed candidate into advisory `/goal` form.

---

## Decision

Use one coherent active-exchange language across the full visible goal surface, keep `/goal` exact as a literal command token, and keep other exact path/version/code/query tokens unchanged only where exactness matters.

---

## What AI does next

- Identify the dominant language from the user's active working language across the current exchange.
- Shape the live next directions as candidate goals in that language.
- Preserve `/goal` and any other checked exact literals where exactness matters.
- Promote only the governed candidate that satisfies the `/goal` bridge.
- Keep the wrapper label, body text, and recap line in the same dominant language.

---

## Recovery path

- If the user explicitly asks for another language, switch the full natural-language wrapper surface to that language while still preserving exact literals.
- If the candidate is not bounded enough yet, leave it as a prose goal instead of forcing command promotion.
- If a token looks English but is actually an exact identifier, keep it exact and do not translate it for cosmetic consistency.

---

## User-visible reply example

`ก่อน (ผิด):
แนะนำใช้คำสั่งนี้:
/goal Done when witness lookup works again. Prove with: reproduce the timeout and add focused coverage. Scope: touched owners only.

หลัง (ถูก):
แนะนำใช้คำสั่งนี้:
/goal เสร็จเมื่อ witness lookup ใช้งานได้อีกครั้ง. พิสูจน์โดย: reproduce timeout เดิม, เพิ่ม focused coverage, และยืนยันใน transcript. ขอบเขต: touched owners only โดยคง exact literals เช่น `/goal` และ `page_size=10` ตามเดิม.

สรุปสั้น ๆ: สิ่งที่ต้องคงเป็นอังกฤษมีเฉพาะ exact literals; scaffold รอบ ๆ ต้องเป็นภาษาเดียวกับ active exchange ทั้งก้อนครับ.`

---

## Flow diagram

```text
Several next directions remain live
  ↓
Read dominant language of the active exchange
  ↓
Shape candidate-goal labels and body text in that language
  ↓
Keep exact literals exact where needed
  ↓
Promote one governed candidate into `/goal`
  ↓
Keep wrapper + body + recap in the same language
```

---

## Matrix axes in play

- request type: next-step recommendation / successor selection / promoted command
- evidence state: enough for one governed candidate
- scope clarity: bounded governed slice + visible wrapper/body language boundary
- risk level: medium
- expected rule response: language-align the whole visible surface, not only the wrapper
- turn count: 2-4+
- user behavior: one main working language across the exchange with exact-literal tokens mixed into the request
- evidence source: checked current doctrine and transcript-derived observed case
- failure mode: wrapper-only translation / body-language drift / over-translation of exact literals
- tool discovery or lane shape: next-step reasoning → candidate-goal set → selective command promotion → same-language recap
- completion state: one governed candidate may continue; the others remain advisory options

---

## Behavior delta

Without this family, the assistant can still emit a wrapper in the user's language while the goal-shaped body remains in another language template, which makes the response look half-localized rather than language-aligned.

With RULES active, the assistant keeps the whole visible goal surface in the active-exchange language, preserves `/goal` and other exact literals where exactness matters, and avoids wrapper-only translation drift.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
