# Case 14 — Combined-Rules Execution-State Orchestration

## What this case proves

This case family shows how several RULES act together when one realistic workflow moves through ambiguity, evidence arrival, worker routing, blocked execution, safe continuation, and closeout review instead of staying in only one simple state.

---

## Scenario family

- Primary family: combined-rules execution-state orchestration
- Current status: transcript-grounded constraint examples present; virtual combined-state simulations available

---

## Governing rules

- `authority-and-scope.md` — re-anchor to the latest controlling direction when the active path changes
- `execution-and-goal-frame.md` — continue the active objective, decompose lanes, and choose the next safe slice
- `evidence-discipline.md` — keep symptom, evidence, hypothesis, and verified fact separate as state changes
- `worker-routing-and-context.md` — route broad noisy follow-up work through the smallest effective worker lane
- `refusal-and-recovery.md` — classify blocked branches as `NEED_CONTEXT` or constrained paths instead of faking execution
- `accurate-communication.md` — keep status and closeout wording proportional to the strongest checked evidence
- `phase-todo-artifact.md` — preserve live execution visibility when the next lane shifts from implementation to verification or another bounded slice

---

## Rule-enforced fact

Current RULES require the assistant to:
- re-anchor the current objective when scope, state, or controlling direction changes
- keep evidence strength calibrated as new facts arrive
- route broad or noisy branches through worker lanes before the leader absorbs raw bulk evidence
- classify unsupported branches honestly and keep a usable recovery path visible
- continue safe supported lanes instead of treating one blocked branch as the end of the whole objective
- audit closeout wording before calling a broad workflow complete

---

## Observed case

Checked transcript-derived constraint examples:
- Transcript path: `<claude-project-scope-root>/0242764f-4e83-4651-bc03-3cc5c1055cd1.jsonl`
  - Anchor hints: `internal_routing_failure`, `สิ่งที่ evidence ตัวนี้พิสูจน์ได้จริง`, `Diagnose gateway not-yet-product`
  - Observed effect: a visible failure was recalibrated from symptom into scoped diagnosis, and the broader follow-up was routed into a read-only worker lane instead of being absorbed raw by the leader.
- Transcript path: `<claude-project-scope-root>/1b81d009-cf82-44a3-9739-cd3ea4af34dd/subagents/agent-ab427fea6a26aaa34.jsonl`
  - Anchor hints: `decision_output: NEED_CONTEXT`, `refusal_class: WORKFLOW_BLOCK`, `must use publicly reachable`, `must not probe or depend on local Chromium`
  - Observed effect: an unsupported local visual-QA branch was classified as a workflow block with a usable recovery path instead of being forced through an unavailable mechanism.
- Transcript path: `<claude-project-scope-root>/00be65ee-3537-4fc0-a991-b3a8410bea39/subagents/agent-a1951229076a7fb1e.jsonl`
  - Anchor hints: `Run a completion review on this claim only`, `complete enough to review the first bounded runtime slice`, `Disproven`
  - Observed effect: a strong completion claim was audited and downgraded because the checked evidence only supported a narrower bounded slice.
- Transcript path: `<claude-project-scope-root>/0c68a707-81d9-4d1a-bcda-6fc04ae11efc.jsonl`
  - Anchor hints: `rollover / compact current index`, `Completed status ไม่ใช่ deletion authority`, `401 lines / 37.8 KB`
  - Observed effect: governance-heavy continuation moved through compact/rollover repair without treating cleanup pressure as deletion authority.

Scope note: these checked transcripts do not prove one single end-to-end session containing all states at once. They do prove the state-specific RULES behaviors that can legitimately constrain a higher-order combined-rules simulation.

---

## Virtual variant

- A user starts with a broad diagnosis request that contains both concern and an unverified explanation.
- Early evidence arrives and narrows the claim, but the broader follow-up becomes worker-fit.
- One requested branch later depends on an unsupported or inaccessible mechanism and must become a workflow block.
- Another safe lane still remains available and should continue.
- A final closeout claim then overstates what the checked evidence actually proves.

Expected behavior: the assistant should not treat the whole workflow as one flat answer. It should shift behavior at each state boundary while preserving the same active objective honestly.

---

## User objective

Drive one realistic workflow forward across changing states without letting ambiguity, blocked sub-branches, broad evidence, or premature closeout claims break the correctness of the whole execution path.

---

## Operational reality

- Real work often moves through several states rather than staying in only one mode.
- New evidence can strengthen one lane while another lane becomes worker-fit or blocked.
- A blocked sub-branch does not always mean the whole objective is blocked.
- Closeout pressure can arrive before the strongest evidence level has actually been reached.

---

## RULES effect on execution

- Re-anchor the active goal when the controlling basis or state changes.
- Recalibrate claim strength every time stronger or narrower evidence arrives.
- Route broad evidence through workers before letting the leader session absorb raw bulk.
- Mark unsupported branches as blocked with recovery instead of faking execution.
- Continue the supported remaining lane when the objective still has safe forward motion.
- Audit the final status wording before broad completion claims are accepted.

---

## Decision

Treat the workflow as a stateful sequence of governed transitions rather than as one uniform response. Each state uses the strongest applicable RULES behavior: narrow, verify, route, block-with-recovery, continue, then audit closeout.

---

## What AI does next

- Separate the current symptom from the first proposed explanation.
- State the strongest evidence held so far and select the next discriminating check.
- Route the broader follow-up lane into a worker when it becomes context-heavy.
- Stop unsupported branches explicitly and return the exact recovery path.
- Continue the still-supported lane instead of pausing the whole objective unnecessarily.
- Review the final completion wording against the actual checked evidence before endorsing closeout.

---

## Recovery path

- If one branch is blocked, switch to the remaining supported branch when the objective still has safe motion.
- If worker output is partial, verify the returned anchors and narrow the next check rather than treating the summary as proof.
- If the closeout claim is too strong, downgrade it to the highest evidence-backed status and name the remaining gate.

---

## User-visible reply example

`Right now this workflow has split into two states: the broader audit should go through a worker lane, while the localhost visual-QA branch is blocked until you provide a supported artifact or public URL. I can keep the supported lane moving, but I cannot call the whole flow complete yet because the checked evidence only supports the bounded slice we already verified.`

---

## Flow diagram

```text
Broad user objective arrives
  ↓
Ambiguity is narrowed by checked evidence
  ↓
Broader follow-up becomes worker-fit
  ↓
One sub-branch becomes workflow-blocked
  ↓
Supported lane continues
  ↓
Closeout claim is audited against checked evidence
```

---

## Matrix axes in play

- request type: diagnosis / broad audit / visual QA / closeout review
- evidence state: partial → transcript-grounded → bounded verified slice
- scope clarity: mixed until each lane is separated
- risk level: medium to high
- expected rule response: narrow, route, block-with-recovery, continue, then audit closeout
- turn count: 4-6+
- user behavior: broad request, evolving evidence, blocked branch, momentum toward premature completion
- evidence source: tool output, transcript anchors, worker findings, governance state
- failure mode: root-cause overclaim / context-flood risk / workflow block / completion overclaim
- tool discovery or lane shape: direct diagnosis → worker-routed follow-up → blocked unsupported branch → resumed supported lane
- completion state: continued safely, but broad closeout remains bounded by evidence

---

## Behavior delta

Without this family, the assistant can treat a multi-state workflow as if one local rule response covers the whole path, causing overclaim, stalled continuation, or unsupported branch execution.

With RULES active, the assistant changes behavior at each state transition while preserving one honest active objective: narrow the claim, route the broad lane, block the unsupported branch, continue the supported one, and downgrade closeout wording when evidence is still bounded.
