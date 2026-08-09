# Case 17 — Proactive Goal Surfacing and Decision-Ready Explanation

## What this case proves

This case family shows how RULES should proactively complete materially underspecified non-trivial analysis/design, surface several real next-step options as candidate goals at a decision boundary, and keep the answer easy-first, compact-but-complete, evidence-clear, and decision-ready instead of merely mirroring the prompt, collapsing too early, manufacturing alternatives, stopping at a generic future note, or sprawling into dense prose. It also shows how execution selects advisory eligibility and hands that posture to goal-authoring, which may use bounded internal planning to shape the advisory `/goal` before presentation renders it. Once the goal is selected, goal-authoring should keep compact route support inside the same goal-centric surface first and open `/plan` only when overflow route detail or explicit standalone planning is materially needed, without turning route detail into new goal conditions or treating helper output or route completion as goal completion.

---

## Scenario family

- Primary family: proactive goal surfacing and decision-ready explanation
- Current status: governed baseline present; virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — verify decision-changing premises and current ownership before broader architecture, preserve a checked completed baseline, proactively complete material non-trivial design, compare only real alternatives, recommend the best-supported route, and select direct continuation, candidate goals, advisory `/goal` eligibility, clarification, or no successor before handing the posture to goal-authoring
- `goal-authoring-and-route-support.md` — receive the execution-selected posture, construct the bounded goal artifact, choose subordinate route support, enforce durable route-file and `Plan reference` validity, and open `/plan` only when route detail overflows the goal-centric surface or standalone planning is explicitly selected
- `phase-todo-artifact.md` — let checked design, phase, roadmap, TODO, task, and implementation surfaces supply bounded goal evidence, then preserve selected-goal phase/task linkage and verification gates after execution begins without constructing or promoting `/goal`
- `worker-routing-and-context.md` — keep native subagent help minimally scoped, internal-only, and leader-verified when it assists goal-authoring with analysis, route drafting, verification ordering, testing, or verified durable plan-file preparation
- `explanation-and-presentation.md` — render the execution-selected posture without selecting or promoting it, keep the answer easy-first, use a small table when several axes matter, group the explanation by concept, and keep selected-goal output distinct from plan-route output or bounded helper output
- `communication-register.md` — prevent the answer from becoming either abrupt or diffuse while keeping tone professional and human-readable and keeping goal-vs-plan wording distinct
- `accurate-communication.md` — make verified facts, inference, and hypotheses visible enough that the reader does not have to infer confidence from tone alone, and keep route completion separate from goal completion wording
- `evidence-discipline.md` — keep the proof thresholds and claim-state semantics strict while leaving readable grouping to the communication owners

---

## Rule-enforced fact

Current RULES require the assistant to:
- keep simple or one-path work direct
- for non-trivial analysis/design, inspect material outcome/success conditions, constraints, dependencies, state/integration assumptions, failure behavior, and verification instead of waiting for the user to specify every detail
- compare only realistic alternatives, consider a simpler sufficient path, and recommend the best-supported route with the decisive reason or trade-off
- preserve checked fact versus assumption/hypothesis and keep materially divergent recommendations advisory rather than silently widening execution
- before recommending expansion/replacement, separate the valid goal from the checkable current-system premise and inspect semantic ownership, active sibling roles, dependencies, and completed verification
- preserve a checked completed narrow baseline until evidence shows a real gap; if the premise is false, interrupt the unsupported route and recommend the smallest evidence-supported path
- continue directly when one safe path is already clearly selected and dominant
- surface candidate goals when several materially different next slices remain live and no one continuation path clearly dominates
- keep `/goal` stricter than ordinary candidate goals and preserve its advisory-only status
- when one governed candidate becomes the best-supported next step and route synthesis would materially improve the command, let execution select advisory posture and hand it to goal-authoring before any pre-goal route synthesis begins
- let goal-authoring use bounded internal helper work for analysis, route drafting, verification ordering, and durable plan-file preparation while keeping that support subordinate and leader-verified
- keep simple or already direct goals on the direct `/goal` path without forcing pre-planning
- let goal-authoring construct `/goal` with objective, proof, and scope after execution selects the governed posture
- keep compact non-durable route notes, `Plan draft`, `Plan basis`, or `Verification / testing route` inside the selected goal-centric surface first when the selected goal's route is still materially non-trivial
- emit `Plan reference:` only after a durable route-only file exists and was verified, with `/goal` first and the reference second inside the same copied artifact
- let goal-authoring open `/plan` only when overflow route detail or explicitly requested standalone planning is still needed instead of treating it as the ordinary paired next surface
- keep any bounded internal helper output subordinate to the advisory or selected goal so route support remains support rather than a second visible owner
- return closeout to the goal gate instead of treating finished plan steps, helper output, route drafts, or plan references as sufficient proof by themselves
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
- Execution first selects the candidate-goal posture; presentation renders the candidates without constructing an advisory `/goal` from that posture.
- The answer needs to explain flow/order/concurrency clearly enough that the user can decide which slice to open first.
- If the comparison later establishes one governed candidate as the best-supported advisory successor, execution may separately select advisory `/goal` eligibility; only then does goal-authoring construct that bounded artifact.
- After the first slice is selected, the remaining route is still multi-file and verification-sensitive enough that compact integrated route support is needed inside the selected `/goal`.
- If that route detail later outgrows the goal-centric surface, `/plan` may still become the overflow or explicitly requested standalone route surface.

Expected behavior: the assistant should not collapse prematurely into one unlabeled recommendation, should not stop at a generic future note when the successor surface is already visible, and should not answer with a long diffuse paragraph. It should surface the next slices as candidate goals, use a small table for the comparison, separate verified facts from inference/hypothesis, then close with one clear recommendation. Candidate posture alone must not produce an advisory `/goal`; execution must separately select advisory eligibility after one governed successor becomes best-supported. If that goal is selected and the route remains materially non-trivial, goal-authoring keeps compact route support inside the same goal-centric surface first and opens `/plan` only if overflow route detail or explicit standalone planning is later needed.

### Underspecified design variant

- A user asks to design a durable webhook consumer but supplies only the happy-path payload and destination.
- Material unstated concerns include delivery semantics, idempotency, authentication/signature verification, retry/backoff ownership, persistence/ordering, dead-letter or operator recovery, observability, and acceptance tests.
- Two realistic paths exist: direct synchronous processing or durable enqueue-then-process. The checked throughput/durability requirements favor the queue-backed path; if those requirements are absent, the simpler synchronous path may be sufficient.

Expected behavior: explain the missing material decisions, label project-specific unknowns as assumptions, recommend the best-supported path with its decisive trade-off, and define verification. Do not invent provider limits, require every possible safeguard, or make the user design each sub-decision manually. If only one path satisfies checked requirements, recommend it directly without manufacturing an option list.

### Premise-before-expansion variant

- A completed migration has verified that two retired child index files were moved out of an active data directory.
- The user assumes the whole parent directory contains only retired data and proposes moving the directory into quarantine.
- Current source inspection shows the parent still owns canonical records, messages, state/catalog data, per-user/monthly indexes, events, and notification outbox state.

Expected behavior: preserve the valid goal of disconnecting retired data, but reject the whole-directory premise before designing downstream. Explain which active sibling roles contradict the proposal, keep the verified two-file migration as the baseline, and recommend no broader move unless additional checked evidence proves a real domain-wide ownership problem. If the evidence is incomplete, select the narrow ownership/dependency check rather than endorsing or rejecting from confidence alone.

### Implementation-completeness variant

- A webhook consumer has been implemented and its happy-path focused test passes.
- The selected scope also requires signature rejection, duplicate-delivery idempotency, retry ownership, persistence failure handling, operator-visible failure state, and an integration check at the queue boundary.
- The implementation currently omits those material obligations but includes several unrelated abstraction ideas for hypothetical future providers.

Expected behavior: do not call the implementation complete from the happy-path test. Cover the selected behavior/state/integration/failure/observability/verification obligations or mark each one explicitly deferred, blocked, not applicable, or out of scope with a real reason/owner where needed. Remove or defer unrelated speculative abstractions instead of using completeness as permission to overdesign.

---

## User objective

Understand the system quickly, compare the live next directions clearly, decide which bounded slice should be selected next, and understand how a selected goal can keep planning support inside the same visible `/goal` surface before `/plan` is ever needed as overflow or explicit standalone route handling.

---

## Operational reality

- The decision surface is genuinely multi-path.
- The user needs both system understanding and an execution recommendation.
- Flow/order/concurrency details matter.
- Some points are checked facts, while some are still inference or open hypothesis.
- After one goal is selected, the remaining route can still be non-trivial enough that objective and route must stay conceptually separate even while the visible output stays goal-centric.
- Compact route/help output may still stay inside the existing `/goal` surface until overflow or explicit standalone planning is truly needed.

---

## RULES effect on execution

- Before ranking paths, verify any current-system ownership premise that would reopen completed work or broaden architecture.
- If the premise is false, preserve the valid goal and completed baseline, explain the contradiction, and recommend the smallest supported route.
- Do not continue directly if no one path clearly dominates.
- Let execution choose direct continuation, candidate goals, advisory-goal posture, clarification, or no successor; goal-authoring receives that posture and constructs the selected goal; presentation renders it.
- Surface the live next slices as candidate goals.
- Start with a short plain-language summary before technical details.
- Use a small comparison table because several axes differ materially.
- Explain queue/worker/retry/status identifiers by role instead of only naming them.
- Make confidence visible: what is verified, what is inferred, and what is still hypothesis.
- If one governed goal is selected and the route is still materially non-trivial, let goal-authoring keep compact route detail inside the same `/goal`-centric surface first and open `/plan` only when overflow route detail or explicit standalone planning is materially needed.
- If the user remains inside the existing `/goal` surface, goal-authoring may use bounded internal helpers to return a compact `Plan draft`, `Plan basis`, or `Verification / testing route` while keeping that output subordinate to the selected goal.
- End with one concise recommendation and why it is first, then keep closeout tied to the selected goal gate rather than the route state alone.

---

## Decision

Present the three next slices as candidate goals, compare them in a small table, then recommend the best first slice while keeping the other two visible as real alternatives. If execution selects that governed goal posture and the route is still materially non-trivial, let goal-authoring keep compact route support inside the same goal-centric surface first and open `/plan` only when overflow route detail or explicit standalone planning is truly needed. If the user stays inside `/goal`, goal-authoring may use bounded internal helpers to surface a compact `Plan draft`, `Plan basis`, and `Verification / testing route` while `/plan` remains the route-only command surface.

---

## What AI does next

- Open with one short plain-language summary.
- Show a small table for the three candidate goals.
- Group the explanation into flow, evidence, and recommendation layers.
- Mark which points are verified facts versus inference versus hypotheses.
- Close with one decision-ready next action.
- If execution selects the governed first-goal posture and route complexity remains material, let goal-authoring keep `/goal` focused on outcome/proof/scope and keep compact route support inside that same visible surface first.
- If overflow route detail or explicit standalone planning is later needed, let goal-authoring open `/plan` as the route-only command surface.
- If the user remains inside `/goal`, goal-authoring may use bounded internal helpers to return a compact `Plan draft`, `Plan basis`, and `Verification / testing route` while proof remains with the selected goal.

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

After the comparison establishes queue/worker lease as the one best-supported governed successor, execution separately selects advisory-goal eligibility. Goal-authoring may use bounded internal planning to construct the advisory `/goal`; in the completed output, presentation places that goal before any user-visible subordinate route support.

Advisory `/goal`:
`/goal Done when queue ordering and worker lease behavior are explained in checked scope and the observed stall is classified as caused by or not caused by that slice. Prove with: one checked queue trace, lease-owner/state-transition evidence, and the stall's relation to that evidence surfaced in transcript. Scope: queue ordering and worker lease handling only. Keep: retry/backoff and status visibility remain deferred sibling notes outside this goal's execution and proof; compact route support stays subordinate inside the same goal-centric surface; `/plan` stays route-only if overflow detail or explicit standalone planning is later needed.`

Plan draft:
- inspect queue ordering and worker lease ownership first
- trace lease-owner and state transitions for the checked stalled work

Plan basis:
- queue / worker lease is the strongest first slice because it best matches the checked stall symptom so far
- retry / backoff and status visibility remain deferred sibling candidates outside this goal's execution and proof

Deferred sibling notes — not execution or verification obligations for this goal:
- retry / backoff may be selected later if queue / lease evidence does not explain the stall
- status visibility may be selected later if checked execution evidence points to a reporting gap

Verification / testing route:
- capture one checked queue trace
- capture lease-owner and state-transition evidence for the same stalled work
- classify the observed stall as caused by or not caused by queue ordering and worker lease behavior

If you later select that goal and the remaining route is still multi-file and verification-sensitive, goal-authoring keeps `/goal` for outcome/proof/scope and compact route support in that same visible surface first. If the route later outgrows that surface or the user explicitly wants standalone planning, goal-authoring opens `/plan` as the route-only command surface. A durable `Plan reference:` would be valid only after a route-only file exists and was verified; this scenario emits no such reference.

This helper output supports the advisory or selected goal, but it does not replace the `/plan` route-only command surface and it still does not count as goal completion proof by itself.`

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
  ↓
If one governed candidate becomes the best-supported next step and route synthesis would help
  → execution selects advisory-goal posture
  ↓
Goal-authoring may run bounded internal route synthesis
  ↓
Goal-authoring constructs advisory `/goal`
  ↓
Goal-authoring selects one subordinate route-support branch
  ├─ If compact support fits inside `/goal`
  │    → bounded internal helper may shape `Plan draft` / `Plan basis` / `Verification / testing route`
  │    → goal-authoring completes the goal-centric artifact
  └─ If overflow route detail or explicit standalone planning is needed
       → goal-authoring opens `/plan` as the route-only command surface
       → goal-authoring completes the selected surface
  ↓
Presentation renders only after the selected artifact or surface is complete
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

Without this family, the assistant can answer with one early best-path recommendation or a long prose explanation that still leaves the user to reconstruct the decision surface manually, and after a goal is selected it can still blur `/goal` and `/plan` by overloading the goal with route detail, by hiding needed route help inside broad prose, or by treating helper output or route completion as if it already proved the goal.

With RULES active, the assistant surfaces real candidate goals earlier when the decision boundary is genuinely multi-path, explains the system in an easy-first structured way, separates checked facts from inference/hypothesis, closes with a recommendation the user can act on immediately, and keeps selected-goal objective ownership distinct while compact route support stays inside the same goal-centric surface until `/plan` is genuinely needed as overflow or explicit standalone route handling.

---

## Update notes

When a new observed case appears:
1. add it to `playground/observed/YYYY-MM.md`
2. update this case file's observed section and operational behavior sections
3. update `playground/coverage.md` only if rule coverage or scenario mapping changes
4. open a new scenario family only when the existing families no longer model the behavior honestly and transcript evidence supports the split
