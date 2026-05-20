# Case 17 — Proactive Goal Surfacing and Decision-Ready Explanation

## What this case proves

This case family shows how RULES should surface several materially different next-step options as candidate goals earlier at a real decision boundary, and how the answer should stay easy-first, compact-but-complete, structured, evidence-clear, and decision-ready instead of collapsing too early into one path or sprawling into dense prose.

---

## Scenario family

- Primary family: proactive goal surfacing and decision-ready explanation
- Current status: governed baseline present; virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — allow candidate-goal surfacing at real decision boundaries when several materially different next slices remain live and no one continuation path clearly dominates
- `phase-todo-artifact.md` — let checked phase/roadmap/TODO surfaces shape compact candidate goals from visible unselected next slices
- `explanation-and-presentation.md` — keep the answer easy-first, use a small table when several axes matter, group the explanation by concept, and close with a concise decision-ready next action
- `communication-register.md` — prevent the answer from becoming either abrupt or diffuse while keeping tone professional and human-readable
- `accurate-communication.md` — make verified facts, inference, and hypotheses visible enough that the reader does not have to infer confidence from tone alone
- `evidence-discipline.md` — keep the proof thresholds and claim-state semantics strict while leaving readable grouping to the communication owners

---

## Rule-enforced fact

Current RULES require the assistant to:
- continue directly when one safe path is already clearly selected and dominant
- surface candidate goals when several materially different next slices remain live and no one continuation path clearly dominates
- keep `/goal` stricter than ordinary candidate goals and preserve its advisory-only status
- open non-trivial answers with plain-language orientation, use a small table when several axes matter, explain identifiers by role, and end with a concise decision-ready close when that structure improves understanding
- separate verified fact, evidence-backed inference, and open hypothesis visibly enough for a user to judge confidence correctly

---

## Observed case

No checked observed example recorded in repo scope yet.

---

## Virtual variant

- A user asks why a queue-backed system sometimes stalls and what should be done next.
- The checked evidence shows three meaningful next slices:
  1. inspect queue ordering and worker lease semantics
  2. inspect retry / backoff behavior
  3. inspect status-reporting and visibility gaps
- No one path is clearly dominant yet.
- The answer needs to explain flow/order/concurrency clearly enough that the user can decide which slice to open first.

Expected behavior: the assistant should not collapse prematurely into one unlabeled recommendation and should not answer with a long diffuse paragraph. It should surface the next slices as candidate goals, use a small table for the comparison, separate verified facts from inference/hypothesis, then close with one clear recommendation.

---

## User objective

Understand the system quickly, compare the live next directions clearly, and decide which bounded slice should be selected next.

---

## Operational reality

- The decision surface is genuinely multi-path.
- The user needs both system understanding and an execution recommendation.
- Flow/order/concurrency details matter.
- Some points are checked facts, while some are still inference or open hypothesis.

---

## RULES effect on execution

- Do not continue directly if no one path clearly dominates.
- Surface the live next slices as candidate goals.
- Start with a short plain-language summary before technical details.
- Use a small comparison table because several axes differ materially.
- Explain queue/worker/retry/status identifiers by role instead of only naming them.
- Make confidence visible: what is verified, what is inferred, and what is still hypothesis.
- End with one concise recommendation and why it is first.

---

## Decision

Present the three next slices as candidate goals, compare them in a small table, then recommend the best first slice while keeping the other two visible as real alternatives.

---

## What AI does next

- Open with one short plain-language summary.
- Show a small table for the three candidate goals.
- Group the explanation into flow, evidence, and recommendation layers.
- Mark which points are verified facts versus inference versus hypotheses.
- Close with one decision-ready next action.

---

## Recovery path

- If one path becomes clearly dominant after a new checked fact appears, reduce the candidate-goal set and continue more directly.
- If the comparison is trivial after clarification, skip the table and keep the answer compact.
- If evidence is too weak to compare paths honestly, say so and ask one narrow clarification rather than manufacturing a ranked goal set.

---

## User-visible reply example

`สรุปสั้น ๆ ก่อน: ตอนนี้ปัญหายังไม่ชี้ชัดว่าอยู่ที่ queue order, retry behavior, หรือ status visibility อย่างใดอย่างหนึ่งแบบเด็ดขาด ดังนั้นแทนที่จะฟันธงทางเดียว ควรแยกเป็น 3 goal ให้เทียบก่อน แล้วค่อยเลือก goal แรกที่คุ้มสุดครับ.

| Goal | สิ่งที่จะได้คำตอบ | หลักฐานตอนนี้ | เหมาะเป็นลำดับแรกแค่ไหน |
|---|---|---|---|
| ตรวจ queue/worker lease | รู้ว่าคิวค้างเพราะลำดับหรือการยึดงานไหม | verified fact: มีอาการ stalled queue; inference: lease/order อาจเกี่ยว | สูง |
| ตรวจ retry/backoff | รู้ว่าปัญหาเกิดจากงานล้มแล้ววน retry หรือไม่ | verified fact: ยังไม่มี proof ตรงว่ามี retry storm | กลาง |
| ตรวจ status visibility | รู้ว่าจริง ๆ งานเดินแต่เราเห็นไม่ครบหรือไม่ | hypothesis: อาจเป็น visibility gap มากกว่าคอขวดจริง | กลาง |

Verified:
- มีอาการ stalled queue ใน checked scope
- ตอนนี้ยังไม่มีหลักฐานชัดว่ามี path เดียวที่ควรฟันธงทันที

Inference:
- queue order / worker lease เป็น candidate แรกที่น่าตรวจ เพราะอธิบาย stalled behavior ได้ตรงที่สุดในตอนนี้

Hypothesis:
- ส่วนหนึ่งของปัญหาอาจเป็น status visibility ไม่ใช่ execution bottleneck จริง

แนะนำลำดับแรก: เปิด goal ตรวจ queue/worker lease ก่อน เพราะตอนนี้มันมีทั้ง impact สูงและ evidence support มากสุด เมื่อเทียบกับอีก 2 ทาง.`

---

## Flow diagram

```text
Several meaningful next slices are live
  ↓
No one path clearly dominates
  ↓
Surface candidate goals
  ↓
Open with plain-language summary
  ↓
Use small table for comparison
  ↓
Separate verified / inference / hypothesis
  ↓
Close with one decision-ready recommendation
```

---

## Matrix axes in play

- request type: diagnosis + next-step recommendation
- evidence state: mixed verified facts, inference, and open hypothesis
- scope clarity: several bounded next slices are visible
- risk level: medium
- expected rule response: candidate goals + structured explanation + evidence-layer clarity
- turn count: 2-4+
- user behavior: wants understanding and a decision, not just a raw best-path command
- evidence source: checked current doctrine and execution-state context
- failure mode: premature one-path collapse / abrupt answer / diffuse prose / confidence blur
- tool discovery or lane shape: decision boundary → candidate goals → comparison table → recommendation
- completion state: next slice not selected yet; one recommendation should still emerge

---

## Behavior delta

Without this family, the assistant can answer with one early best-path recommendation or a long prose explanation that still leaves the user to reconstruct the decision surface manually.

With RULES active, the assistant surfaces real candidate goals earlier when the decision boundary is genuinely multi-path, explains the system in an easy-first structured way, separates checked facts from inference/hypothesis, and closes with a recommendation the user can act on immediately.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
