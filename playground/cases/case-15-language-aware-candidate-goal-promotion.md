# Case 15 — Language-Aware Candidate Goal Promotion

## What this case proves

This case family shows how RULES keep successor recommendations aligned to the user's dominant session language, shape several live next directions as candidate goals instead of a plain choice list, and promote only the best-supported governed repo candidate into advisory `/goal` form.

---

## Scenario family

- Primary family: language-aware candidate-goal promotion
- Current status: governed baseline present; virtual variants available

---

## Governing rules

- `communication-register.md` — keep goal-oriented wording aligned to the dominant session language and preserve a high-signal boundary between candidate goals and promoted commands
- `accurate-communication.md` — keep candidate-goal and promoted-`/goal` wording advisory, evidence-calibrated, and language-aligned to the active session
- `execution-and-goal-frame.md` — shape several live successor directions as candidate goals first, then promote only the best-supported governed candidate into `/goal`
- `phase-todo-artifact.md` — keep design-first sourcing and material-only execution/release inputs when a governed candidate is promoted
- `explanation-and-presentation.md` — present candidate goals clearly before command promotion and keep the promoted `/goal` compact

---

## Rule-enforced fact

Current RULES require the assistant to:
- follow the dominant session language by default when surfacing candidate goals or promoted `/goal` suggestions unless the user explicitly selects another language
- prefer candidate goals over a plain unlabeled choice list when several meaningful successor directions remain live
- keep candidate goals distinct from promoted `/goal` commands instead of turning every option into command form
- promote only the best-supported governed repo candidate into advisory `/goal` form under the existing governed-work-only boundary
- keep governed `/goal` sourcing design-first, then active execution surfaces, with changelog/patch/README included only when they materially shape completion, review, or current-state impact

---

## Observed case

No checked observed example recorded in repo scope yet.

---

## Virtual variant

- A user has been communicating in Thai-first language through the active session.
- The current work slice is complete enough that several next directions are now live.
- One direction is lightweight and non-governed.
- One direction is governed repo work with design and execution consequences.
- A third direction is plausible but still too broad to promote safely into command form.

Expected behavior: the assistant should not answer with a plain English choice list and should not convert every option into `/goal`. It should keep the option set in Thai-first candidate-goal form, then promote only the governed candidate that actually satisfies the `/goal` bridge.

---

## User objective

Choose the next governed work slice clearly without losing language continuity or collapsing every possible next move into command syntax too early.

---

## Operational reality

- The user's active working language is Thai-first.
- Several next directions remain live at the same time.
- Only one next direction is bounded enough, governed enough, and proof-shaped enough for command promotion.
- The assistant still needs to preserve design-first sourcing and compact output if it promotes one candidate into `/goal`.

---

## RULES effect on execution

- Read the active session language first instead of defaulting to English command prose by habit.
- Frame the live next directions as candidate goals so the user can compare outcomes, not just labels.
- Keep trivial or broad options as prose goals when they do not merit command promotion.
- Promote only the best-supported governed candidate into advisory `/goal` form.
- Build that promoted command from design-first target truth, then active execution surfaces, while keeping the final wording compact.

---

## Decision

Use Thai-first candidate goals for the option set, then promote only the single governed repo candidate that satisfies the existing `/goal` bridge.

---

## What AI does next

- Identify the dominant session language from the user's active working language.
- List the live successor directions as compact candidate goals rather than a plain choice list.
- Separate lightweight/non-governed candidates from governed repo candidates.
- Select only the best-supported governed candidate for advisory `/goal` promotion.
- Keep the promoted `/goal` compact and sourced from design first, then active execution surfaces.

---

## Recovery path

- If none of the candidates is bounded enough yet, keep them as prose goals and ask one narrow clarification only if the ambiguity changes the path materially.
- If the governed candidate lacks transcript-visible proof, leave it as a candidate goal and defer command promotion.
- If the user switches language explicitly, let that explicit selection replace the default dominant-session-language behavior.

---

## User-visible reply example

`ตอนนี้มี 3 goal ที่ไปต่อได้ครับ: Goal A คือปิดงาน wording owner ให้ครบก่อน, Goal B คือทำ governed runtime/design/changelog sync สำหรับ wave ถัดไป, และ Goal C คือไปที่ release lane ต่อเลย แต่ในสามตัวนี้มีแค่ Goal B ที่เข้าเงื่อนไข governed "/goal" แบบครบ ดังนั้นถ้าจะ promote เป็น command ผมจะเสนอเฉพาะตัวนั้น ไม่แปลงทุกตัวเลือกเป็น /goal ครับ.`

---

## Flow diagram

```text
Several next directions remain live
  ↓
Read dominant session language
  ↓
Shape options as candidate goals
  ↓
Test each candidate against governed `/goal` bridge
  ↓
Promote only the best-supported governed candidate
```

---

## Matrix axes in play

- request type: next-step recommendation / successor selection
- evidence state: enough for one governed candidate, insufficient or unnecessary for the others
- scope clarity: several live directions, one bounded governed slice
- risk level: medium
- expected rule response: language-align, shape candidate goals, promote one governed candidate only
- turn count: 2-4+
- user behavior: Thai-first communication, several possible next directions
- evidence source: checked current doctrine and execution-state context
- failure mode: English-default drift / plain choice-list drift / over-promotion of every option into `/goal`
- tool discovery or lane shape: next-step reasoning → candidate-goal set → selective governed command promotion
- completion state: one governed candidate may continue, others remain advisory options

---

## Behavior delta

Without this family, the assistant can fall back to an English-shaped next-step list or overcorrect by turning every option into `/goal`, even when only one successor slice is governed and bounded enough for command form.

With RULES active, the assistant keeps the option set in the user's dominant session language, shapes it as candidate goals, and promotes only the best-supported governed repo candidate into advisory `/goal` form while leaving the other options as prose goals.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
