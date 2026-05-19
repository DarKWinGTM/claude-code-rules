# Case 08 — Execution Continuity and Worker Routing

## What this case proves

This case family shows how RULES keep multi-step work moving while routing broad or noisy evidence through the smallest effective worker path.

---

## Scenario family

- Primary family: execution continuity and worker routing
- Current status: governed baseline; checked observed examples present; virtual variants available

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
- use worker routing before broad raw leader-session absorption when the work is large/noisy/multi-surface
- keep worker findings as inputs, not automatic proof

---

## Observed case

Checked observed examples in repo scope:
- the released `v10.16 / P108` wave explicitly compacted worker-routing and redistributed document-density and governance content to the correct owners
- the released `v10.17 / P109` wave explicitly enforced lineage-first continuation so phase-shaped next work cannot jump to a new major by momentum
- these observed effects are recorded in `playground/observed/2026-05.md` as `O-2026-05-03` and `O-2026-05-04`

---

## Virtual variant

- A broad repo audit would require several file reads and noisy outputs.
- Implementation is done, but the next lane is verification and still implied.
- A phase-backed task closes one lane and opens a broader next lane that should be worker-routed.

Expected behavior: keep moving, but route the noisy lane before the main session absorbs raw evidence.

---

## Example dialogue (virtual)

### User
`Audit this repo and tell me what is out of sync.`

### AI without this rule family risk
`I will read everything first.`

### AI with RULES active
`This is broad enough to split into lanes. I will route the large read/audit slice through a worker first, then verify the important anchors before I summarize the result.`

---

## Flow diagram

```text
Broad objective arrives
  ↓
Execution lane is identified
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

---

## Behavior delta

Without this family, the assistant can either stop too early or read too much raw evidence into the main session.

With RULES active, work should keep moving while context-heavy evidence is routed more deliberately.
