# Case 17 — Proactive Goal Surfacing and Decision-Ready Explanation

## What this case proves

This case family shows how RULES should surface several materially different next-step options as candidate goals earlier at a real decision boundary, how the answer should stay easy-first, compact-but-complete, structured, evidence-clear, and decision-ready instead of collapsing too early into one path, stopping at a generic future note, or sprawling into dense prose, and how a selected governed goal may then bridge into `/plan` without turning route detail into new goal conditions or treating route completion as goal completion.

---

## Scenario family

- Primary family: proactive goal surfacing and decision-ready explanation
- Current status: governed baseline present; virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — allow candidate-goal surfacing at real decision boundaries when several materially different next slices remain live and no one continuation path clearly dominates, then keep `/goal` as the objective owner and `/plan` as the route owner once one governed goal is selected
- `phase-todo-artifact.md` — let checked phase/roadmap/TODO surfaces shape compact candidate goals from visible unselected next slices, then bridge selected governed route-heavy work into `/plan` only when the route is materially non-trivial
- `explanation-and-presentation.md` — keep the answer easy-first, use a small table when several axes matter, group the explanation by concept, and keep selected-goal output distinct from plan-route output
- `communication-register.md` — prevent the answer from becoming either abrupt or diffuse while keeping tone professional and human-readable and keeping goal-vs-plan wording distinct
- `accurate-communication.md` — make verified facts, inference, and hypotheses visible enough that the reader does not have to infer confidence from tone alone, and keep route completion separate from goal completion wording
- `evidence-discipline.md` — keep the proof thresholds and claim-state semantics strict while leaving readable grouping to the communication owners

---

## Rule-enforced fact

Current RULES require the assistant to:
- continue directly when one safe path is already clearly selected and dominant
- surface candidate goals when several materially different next slices remain live and no one continuation path clearly dominates
- keep `/goal` stricter than ordinary candidate goals and preserve its advisory-only status
- keep `/goal` responsible for objective, proof, and scope after one governed goal is selected
- use `/plan` only for route/sequence/task breakdown when the selected goal's route is still materially non-trivial
- return closeout to the goal gate instead of treating finished plan steps as sufficient proof by themselves
- open non-trivial answers with plain-language orientation, use a small table when several axes matter, explain identifiers by role, and end with a concise decision-ready close when that structure improves understanding
- separate verified fact, evidence-backed inference, and open hypothesis visibly enough for a user to judge confidence correctly

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/519ee145-4708-49b8-9b9e-e57227b2ade7.jsonl`
- Anchor hints: `P696 ปิดได้แล้ว`, `implementation wave ใหม่`, `ขอคำสั่ง goal ในการดำเนินการ`
- Observed effect: after a docs-lock closeout already made the successor state visible, the answer still ended in a generic future note instead of surfacing a governed next-step shape directly enough; the user had to ask again for a goal command.
- Scope note: this proves a residual successor-surfacing bridge miss in that checked session; it does not prove that every closeout should emit `/goal`.

---

## Virtual variant

- A user asks why a queue-backed system sometimes stalls and what should be done next.
- The checked evidence shows three meaningful next slices:
  1. inspect queue ordering and worker lease semantics
  2. inspect retry / backoff behavior
  3. inspect status-reporting and visibility gaps
- No one path is clearly dominant yet.
- The answer needs to explain flow/order/concurrency clearly enough that the user can decide which slice to open first.
- After the first slice is selected, the remaining route is still multi-file and verification-sensitive enough that `/plan` may become useful.

Expected behavior: the assistant should not collapse prematurely into one unlabeled recommendation, should not stop at a generic future note when the successor surface is already visible, and should not answer with a long diffuse paragraph. It should surface the next slices as candidate goals, use a small table for the comparison, separate verified facts from inference/hypothesis, then close with one clear recommendation. If the user selects that governed goal and the route remains materially non-trivial, the assistant should bridge into `/plan` for route detail while keeping `/goal` as the objective contract.

---

## User objective

Understand the system quickly, compare the live next directions clearly, decide which bounded slice should be selected next, and understand when a selected goal should stay as `/goal` versus when the route should bridge into `/plan`.

---

## Operational reality

- The decision surface is genuinely multi-path.
- The user needs both system understanding and an execution recommendation.
- Flow/order/concurrency details matter.
- Some points are checked facts, while some are still inference or open hypothesis.
- After one goal is selected, the remaining route can still be non-trivial enough that objective and route must stay visibly separate.

---

## RULES effect on execution

- Do not continue directly if no one path clearly dominates.
- Surface the live next slices as candidate goals.
- Start with a short plain-language summary before technical details.
- Use a small comparison table because several axes differ materially.
- Explain queue/worker/retry/status identifiers by role instead of only naming them.
- Make confidence visible: what is verified, what is inferred, and what is still hypothesis.
- If one governed goal is selected and the route is still materially non-trivial, keep that selected goal in `/goal` and move route detail into `/plan`.
- End with one concise recommendation and why it is first, then keep closeout tied to the selected goal gate rather than the route state alone.

---

## Decision

Present the three next slices as candidate goals, compare them in a small table, then recommend the best first slice while keeping the other two visible as real alternatives. If the user selects that governed goal and the route is still materially non-trivial, bridge into `/plan` for route detail while keeping the selected goal as the objective owner.

---

## What AI does next

- Open with one short plain-language summary.
- Show a small table for the three candidate goals.
- Group the explanation into flow, evidence, and recommendation layers.
- Mark which points are verified facts versus inference versus hypotheses.
- Close with one decision-ready next action.
- If the user selects the governed first goal and route complexity remains material, keep `/goal` focused on outcome/proof/scope and move route breakdown into `/plan`.

---

## Recovery path

- If one path becomes clearly dominant after a new checked fact appears, reduce the candidate-goal set and continue more directly.
- If the comparison is trivial after clarification, skip the table and keep the answer compact.
- If evidence is too weak to compare paths honestly, say so and ask one narrow clarification rather than manufacturing a ranked goal set.

---

## User-visible reply example

`Quick summary first: the current evidence does not point decisively to queue order, retry behavior, or status visibility as the single cause yet. So instead of forcing one path too early, the better next step is to surface 3 candidate goals, compare them briefly, and then pick the first goal with the strongest payoff.

| Goal | What it would clarify | Evidence so far | Best first step? |
|---|---|---|---|
| Inspect queue/worker lease | Determine whether the stall comes from ordering or lease ownership | verified fact: there is a stalled queue symptom; inference: lease/order may be involved | High |
| Inspect retry/backoff | Determine whether failed work is looping and re-entering the queue | verified fact: there is no direct proof of a retry storm yet | Medium |
| Inspect status visibility | Determine whether work is progressing but the reporting layer is incomplete | hypothesis: this may be a visibility gap rather than a real execution bottleneck | Medium |

Verified:
- There is a stalled queue symptom in checked scope.
- The current evidence does not justify collapsing immediately to one path.

Inference:
- Queue order / worker lease is the strongest first candidate because it fits the observed stall most directly so far.

Hypothesis:
- Part of the problem may be status visibility rather than the execution path itself.

Recommended first goal: inspect queue/worker lease first, because it currently has the strongest evidence support and the highest immediate diagnostic value.

If you select that goal and the remaining route is still multi-file and verification-sensitive, keep `/goal` for outcome/proof/scope and use `/plan` only for the route breakdown. In other words: `/goal` = what must be true when this slice is done; `/plan` = how we will execute the slice. Finishing the plan steps alone is still not enough until the selected goal gate is checked.`

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

Without this family, the assistant can answer with one early best-path recommendation or a long prose explanation that still leaves the user to reconstruct the decision surface manually, and after a goal is selected it can still blur `/goal` and `/plan` by overloading the goal with route detail or by treating route completion as if it already proved the goal.

With RULES active, the assistant surfaces real candidate goals earlier when the decision boundary is genuinely multi-path, explains the system in an easy-first structured way, separates checked facts from inference/hypothesis, closes with a recommendation the user can act on immediately, and keeps selected-goal objective ownership distinct from later plan-route breakdown.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
