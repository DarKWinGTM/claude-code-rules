# Case 13 — Live Execution Surface Arbitration

## What this case proves

This case family shows how RULES resolve next-work ambiguity when the live task list, `TODO.md`, `phase/SUMMARY.md`, and checked implementation state do not all point to the same next slice.

---

## Scenario family

- Primary family: live execution surface arbitration (`task-list-vs-phase-next-work-selection`)
- Current status: governed baseline; virtual variants available; no checked observed example recorded in repo scope yet

---

## Governing rules

- `phase-todo-artifact.md` — built-in task list as the live execution surface plus TODO/phase separation
- `execution-and-goal-frame.md` — active next-work discovery and safe continuation
- `document-integrity.md` — active entrypoints must stay current and not silently drift
- `authority-and-scope.md` — current checked execution surfaces outrank stale framing or weaker carry-forward context
- `accurate-communication.md` — next-step wording should match the checked execution basis

---

## Rule-enforced fact

Current RULES require the assistant to:
- use the built-in task list first when it clearly expresses the active non-trivial execution slice
- fall back to active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state when task detail is insufficient
- avoid inventing a fresh path when checked execution surfaces already imply the next lane
- preserve phase linkage and verification continuity instead of jumping to whichever surface was read last

---

## Observed case

No checked observed example recorded in repo scope yet.

The family is still grounded because current execution, phase, and document-integrity owners explicitly define how live task state, phase state, and durable tracking should be reconciled.

---

## Virtual variant

- The live task list still shows `verification pending`, while `phase/SUMMARY.md` still emphasizes implementation.
- `TODO.md` mentions a governance-sync slice, but checked implementation state shows the implementation lane is already done.
- A compact carry-forward summary suggests one next step, but the live execution surface points to another.

Expected behavior: choose the next slice from the strongest checked execution surface rather than from the most recently read or most convenient one.

---

## User objective

Continue the correct next slice without drifting into the wrong lane when several execution surfaces point in different directions.

---

## Operational reality

- Several execution surfaces exist at once: built-in task list, active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state.
- They may not all emphasize the same next action.
- One surface is the live execution authority, while others are roadmap, durable context, or implementation evidence.

---

## RULES effect on execution

- Prioritize the live execution surface first when it is clear enough.
- Use phase, TODO, and checked implementation state to resolve ambiguity when task detail is weak or stale.
- Prevent stale or weaker surfaces from silently taking over the next-work decision.

---

## Decision

The next slice should follow the strongest current execution surface, with the live task list first when it is specific enough, and active phase / checked implementation state used to break ties or repair drift.

---

## What AI does next

- Inspect the live task list for the currently unblocked slice.
- Compare it against active phase context and checked implementation state.
- Select the next lane that still belongs to the same objective and continue it instead of opening a fresh one.

---

## Recovery path

- If task wording is too weak, tighten the task so the live execution surface becomes trustworthy again.
- If execution surfaces truly conflict, re-anchor the active phase and next slice explicitly.
- If a real ambiguity remains, ask one narrow clarification instead of drifting into a fresh lane by momentum.

---

## User-visible reply example

`The implementation slice is already done, and the live task surface still shows verification pending, so the correct next move is verification rather than opening a new lane.`

---

## Flow diagram

```text
Several execution surfaces point at different next steps
  ↓
Live task surface is checked first
  ↓
Active phase and implementation state are compared
  ↓
The strongest current execution basis is selected
  ↓
The next lane continues without opening a fresh objective
```

---

## Matrix axes in play

- request type: continuation / verification / governance-sync / phased execution
- evidence state: mixed checked execution signals
- scope clarity: mixed until execution surfaces are reconciled
- risk level: medium
- expected rule response: choose the strongest live execution basis and continue the correct next lane
- turn count: 2-4
- user behavior: clear continue intent with drift-risky supporting surfaces
- evidence source: task list, phase surface, durable TODO, and checked implementation state
- failure mode: stale-surface drift / wrong next-lane selection
- tool discovery or lane shape: direct handling unless broader verification becomes worker-fit
- completion state: continuation after lane arbitration

---

## Behavior delta

Without this family, the assistant can jump to whichever execution surface was read last or whichever one sounds most convenient.

With RULES active, the assistant chooses the next slice from the strongest checked execution basis and keeps the work inside the correct active objective.
