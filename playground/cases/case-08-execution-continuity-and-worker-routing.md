# Case 08 — Execution Continuity and Worker Routing

## What this case proves

This case family shows how RULES keep multi-step work moving while routing broad or noisy evidence through the smallest effective worker path.

---

## Scenario family

- Primary family: execution continuity and worker routing
- Current status: transcript-grounded observed examples present; virtual variants available

---

## Governing rules

- `execution-and-goal-frame.md` — discussion vs execution, goal/output/gate framing, and safe continuation
- `worker-routing-and-context.md` — worker-first routing for broad, noisy, or context-heavy work
- `phase-todo-artifact.md` — phase linkage and staged execution surfaces
- `safe-io.md` — bounded reads and output handling during broad work
- `accurate-communication.md` — progress wording without false completion

---

## Rule-enforced fact

Current RULES require the assistant to:
- continue active execution when safe next work is already implied
- decompose broad objectives into lanes before deep drift
- use worker routing before broad raw leader-session absorption when the work is large, noisy, or multi-surface
- keep worker findings as inputs, not automatic proof

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/0242764f-4e83-4651-bc03-3cc5c1055cd1.jsonl`
- Anchor hints: `internal_routing_failure`, `สิ่งที่ evidence ตัวนี้พิสูจน์ได้จริง`, `Diagnose gateway not-yet-product`
- Observed effect: after grounding the diagnosis to what the evidence actually proved, the assistant routed the broader follow-up investigation through a read-only lane instead of absorbing the full audit into the main session.
- Scope note: this proves worker-routed continuation in that checked session; it does not mean every follow-up must become a worker lane.

Supporting repo-scope observed examples are also recorded in `playground/observed/2026-05.md` as `O-2026-05-03` and `O-2026-05-04`.

---

## Virtual variant

- A broad repo audit would require several file reads and noisy outputs.
- Implementation is done, but the next lane is verification and still implied.
- A phase-backed task closes one lane and opens a broader next lane that should be worker-routed.

Expected behavior: keep moving, but route the noisy lane before the main session absorbs raw evidence.

---

## User objective

Keep a multi-step task moving without stalling early or flooding the main session with broad raw evidence.

---

## Operational reality

- The next safe slice is often already implied by the active goal or checked state.
- Some follow-up lanes are broad, noisy, or multi-surface enough that the main session should not absorb all raw evidence directly.
- Progress and delegation both need to stay tied to the same objective.

---

## RULES effect on execution

- Continue active execution when the next slice is already clear.
- Decompose broad objectives into lanes before deep drift.
- Use worker routing before broad raw leader-session absorption when the next lane is noisy or large.

---

## Decision

Continue the objective, but route the broad follow-up lane through the smallest effective worker path before reading everything directly.

---

## What AI does next

- Identify the current lane and the next implied lane.
- If the next lane is broad, delegate filtered reading or audit work first.
- Verify the returned anchors before stronger user-facing claims.

---

## Recovery path

- If the scope is still mixed, narrow the question before deeper execution.
- If the worker result is partial, run the next targeted check instead of absorbing raw bulk evidence by momentum.

---

## User-visible reply example

`The next safe move is to continue the diagnosis, but the follow-up audit is broad enough that I should route it through a read-only worker first.`

---

## Flow diagram

```text
Broad follow-up work appears
  ↓
Current execution lane is identified
  ↓
Worker-fit gate is checked
  ↓
Raw evidence is filtered in a smaller lane
  ↓
Leader verifies anchors and continues the main objective
```

---

## Matrix axes in play

- request type: broad audit / implementation / verification / continuation
- evidence state: mixed but progressing
- scope clarity: broad until lane decomposition is made explicit
- risk level: medium
- expected rule response: continue safely and route broad evidence through the smallest effective worker path
- turn count: 3
- user behavior: clear request with expanding evidence scope
- evidence source: tool output plus transcript anchor
- failure mode: context-flood risk
- tool discovery or lane shape: worker-routed read-only follow-up
- completion state: execution continues after filtered evidence returns

---

## Behavior delta

Without this family, the assistant can either stop too early or read too much raw evidence into the main session.

With RULES active, work keeps moving while context-heavy evidence is routed more deliberately.
