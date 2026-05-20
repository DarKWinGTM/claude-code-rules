# Case 16 — End-to-End Language-Aligned Goal Surface

## What this case proves

This case family shows how RULES keep the full visible goal surface aligned to the user's dominant session language: candidate-goal labels, promoted `/goal`, surrounding recommendation labels, and recap/closing lines all follow the same language unless a checked exact literal should remain exact.

---

## Scenario family

- Primary family: end-to-end language-aligned goal surface
- Current status: governed baseline present; virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — make candidate-goal labels, promoted `/goal`, recommendation labels, and recap/closing lines follow the dominant session language end-to-end
- `explanation-and-presentation.md` — keep output examples and wrapper labels language-surface-neutral or dominant-session-language-driven instead of English-first by habit
- `accurate-communication.md` — keep candidate goals, promoted `/goal`, and recap wording language-aligned while preserving exact literals when they should remain exact
- `communication-register.md` — keep the visible goal surface aligned to the user's working language without turning exact tokens into cosmetic translations
- `phase-todo-artifact.md` — keep `/goal` sourcing slots semantic rather than mandatory English surface labels

---

## Rule-enforced fact

Current RULES require the assistant to:
- follow the dominant session language across candidate-goal labels, promoted `/goal`, recommendation labels, and recap/closing lines unless the user explicitly selects another language style
- preserve exact literals such as `/goal`, file paths, version tags, and code-level identifiers when they should remain exact
- treat `Done when` / `Prove with` / `Scope` / `Keep` / `Stop after` as concept-slot examples rather than mandatory English output labels
- keep several live next directions as candidate goals first and promote only the best-supported governed candidate into advisory `/goal` form

---

## Observed case

No checked observed example recorded in repo scope yet.

---

## Virtual variant

- A user has been communicating in Thai-first language through the active session.
- The current work slice is complete enough that two next directions are live.
- One direction is a bounded governed repo slice that qualifies for advisory `/goal` promotion.
- The assistant also wants to add a short recap line after the recommendation.

Expected behavior: the assistant should not answer with English-first wrapper labels around Thai-first goal output. It may keep `/goal` exact, but the surrounding natural-language labels and recap should stay Thai-first.

---

## User objective

Get a next-step recommendation that feels like one coherent Thai-first response rather than an English shell with Thai content inserted into it.

---

## Operational reality

- The user's active working language is Thai-first.
- One governed next direction is bounded enough for advisory `/goal` promotion.
- The assistant may still need to keep exact literals such as `/goal` and file paths unchanged.
- The visible wrapper labels and recap line are part of the user-facing surface, not decorative extras outside the language policy.

---

## RULES effect on execution

- Read the dominant session language before emitting candidate-goal labels or wrapper labels.
- Keep exact literals exact only where exactness matters.
- Avoid English-first wrappers around non-English goal output.
- Keep the recap/closing line in the same dominant session language as the goal surface.
- Promote only the best-supported governed candidate into advisory `/goal` form.

---

## Decision

Use Thai-first wording across the full visible goal surface, keep `/goal` exact as a literal command token, and keep any exact path/version/code identifiers unchanged only where exactness matters.

---

## What AI does next

- Identify the dominant session language from the user's active working language.
- Shape the live next directions as candidate goals in that language.
- Preserve `/goal` and any other checked exact literals where exactness matters.
- Promote only the governed candidate that satisfies the `/goal` bridge.
- Keep the wrapper label and recap line in the same dominant session language.

---

## Recovery path

- If the user explicitly asks for English output, switch the full natural-language wrapper surface to English while still preserving exact literals.
- If the candidate is not bounded enough yet, leave it as a prose goal instead of forcing command promotion.
- If a token looks English but is actually an exact identifier, keep it exact and do not translate it for cosmetic consistency.

---

## User-visible reply example

`เป้าหมายถัดไปที่ไปต่อได้ตอนนี้มี 2 แบบครับ:
- เป้าหมาย 1: ปิด wording owner ให้ครบก่อน
- เป้าหมาย 2: เปิด wave docs sync สำหรับ P116

คำสั่ง /goal ที่แนะนำ:
/goal เสร็จเมื่อ P116 sync runtime/design/changelog/TODO/phase/patch surfaces ครบและตรวจ language surface แล้วว่า candidate goals, wrapper labels และ recap lines เป็นไทยสอดคล้องกันทั้งหมด. พิสูจน์โดย: อ้างไฟล์/section ที่แก้จริงและยืนยันว่า playground ยังเป็น non-runtime. ขอบเขต: touched RULES owners + playground case ใหม่. คงไว้: /goal ยังเป็น advisory และ exact literals ที่ต้องคงรูปเดิมยังคงเดิม. หยุดเมื่อ docs sync และ consistency check เสร็จ

สรุปสั้น ๆ: ตอนนี้ถ้าจะไปต่อแบบ governed ผมแนะนำเป้าหมาย 2 เพราะ bounded และ proof ชัดที่สุดครับ.`

---

## Flow diagram

```text
Several next directions remain live
  ↓
Read dominant session language
  ↓
Shape candidate-goal labels in that language
  ↓
Keep exact literals exact where needed
  ↓
Promote one governed candidate into `/goal`
  ↓
Keep recap/closing line in the same language
```

---

## Matrix axes in play

- request type: next-step recommendation / successor selection / promoted command
- evidence state: enough for one governed candidate
- scope clarity: bounded governed slice + visible wrapper language requirement
- risk level: medium
- expected rule response: language-align the whole visible surface, not only the command body
- turn count: 2-4+
- user behavior: Thai-first communication with exact-literal tokens mixed into the request
- evidence source: checked current doctrine and execution-state context
- failure mode: English-wrapper drift / recap-language drift / over-translation of exact literals
- tool discovery or lane shape: next-step reasoning → candidate-goal set → selective command promotion → same-language recap
- completion state: one governed candidate may continue; the others remain advisory options

---

## Behavior delta

Without this family, the assistant can still emit English-first wrapper labels around Thai-first goal output, which makes the response look half-translated rather than language-aligned.

With RULES active, the assistant keeps the whole visible goal surface in the user's dominant session language, preserves `/goal` and other exact literals where exactness matters, and avoids English-shell + Thai-content output.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
