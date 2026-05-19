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
- Transcript path: `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/0242764f-4e83-4651-bc03-3cc5c1055cd1.jsonl`
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

## Example dialogue

### Dialogue label
`virtual trace patterned on a checked transcript-derived observed case`

### Turn 1 — User
`PAYG customer auth is failing. Here is the error payload. What do we do next?`

### Turn 1 — AI without this rule family risk
`I’ll read everything in the repo here and tell you the answer after that.`

### Turn 1 — AI with RULES active
`I can start with the checked symptom now, but if the next slice turns broad I’ll split it into a smaller read-only lane instead of flooding the main session with raw evidence.`

### Turn 2 — Evidence, correction, or blocker
`The checked session shows both the error payload and a later re-anchoring section around what the evidence actually proves.`

### Turn 2 — AI without this rule family risk
`I still need to pull the full codebase into the main thread before I can say anything useful.`

### Turn 2 — AI with RULES active
`The diagnosis can stay scoped here. The broader verifier-path audit is the noisy slice, so that part should go through a smaller investigation lane first.`

### Turn 3 — Next-step narrowing / recovery / closeout
`The read-only lane returns filtered anchors for the verifier path and its likely dependencies.`

### Turn 3 — AI with RULES active
`Now I can verify the important anchors in the main session and continue the actual objective without losing context budget on the raw bulk read.`

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
