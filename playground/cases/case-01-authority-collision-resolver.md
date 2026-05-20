# Case 01 — Authority Collision Resolver

## What this case proves

This case family shows how RULES keep user authority, hard boundaries, stale framing, and post-compact continuation from being silently mixed together.

---

## Scenario family

- Primary family: authority collision resolver
- Current status: governed baseline; virtual variants available; no checked observed example recorded in repo scope yet

---

## Governing rules

- `authority-and-scope.md` — authority order and fresh-directive precedence
- `execution-and-goal-frame.md` — re-anchor after scope correction or post-compact drift risk
- `accurate-communication.md` — working-interpretation wording and evidence-strength language
- `evidence-discipline.md` — user concern/direction is not automatic factual proof
- `memory-governance-and-session-boundary.md` — remembered context needs current-state recheck before exact-fact wording

---

## Rule-enforced fact

Current RULES require the assistant to:
- preserve hard-boundary constraints over user direction when they truly conflict
- otherwise follow the latest user instruction over stale assistant options or stale continuation momentum
- re-anchor after user correction instead of continuing from an obsolete frame
- treat memory and carried-forward context as scoped continuity help, not as current verified truth by default

---

## Observed case

No checked observed example recorded in repo scope yet.

The family is still grounded because the governing rules explicitly define the authority order, stale-frame repair, and post-compact recheck posture.

---

## Virtual variant

- User first chooses option A, then later says to switch to option B.
- A previous summary implies one path, but a fresh user instruction changes the objective.
- Memory says a file/path existed earlier, but the current repo state may have changed.

In all three branches, the assistant should prefer the current authority basis over stale framing.

---

## User objective

Resolve a mid-stream instruction change where the latest user direction replaces an earlier branch or stale continuation frame.

---

## Operational reality

- The active objective is still in the same work family, but the controlling direction changed.
- Older assistant framing, compacted carry-forward context, or remembered state may still point at the previous branch.
- The risk is not missing information alone; the real risk is continuing from an obsolete authority basis.

---

## RULES effect on execution

- Re-check authority order before continuing.
- Retire stale option momentum once a fresher controlling instruction arrives.
- Keep memory and carried-forward context as continuity help, not as current verified truth.

---

## Decision

The latest valid user instruction becomes the active path unless a real hard boundary blocks it.

---

## What AI does next

- Restate the current working interpretation.
- Drop the stale branch as the execution basis.
- Continue from the updated direction, or ask one narrow clarification only if a real conflict remains.

---

## Recovery path

- If the old and new directions still collide materially, clarify the exact active branch.
- If the previous path depended on remembered repo state, re-check the current state before stronger factual wording.

---

## User-visible reply example

`My working read is that your latest instruction replaces the earlier branch, so I will continue with option B unless a real hard boundary blocks it.`

---

## Flow diagram

```text
Earlier assistant framing
  ↓
Fresh user directive arrives
  ↓
Authority order is re-checked
  ↓
Stale option is retired
  ↓
Current user-directed path continues
```

---

## Matrix axes in play

- request type: coordination / implementation / correction
- evidence state: user direction plus partial current evidence
- scope clarity: mixed until re-anchored
- risk level: medium when stale framing could misdirect work
- expected rule response: re-anchor and continue from the current authority basis

---

## Behavior delta

Without this rule family, the assistant can continue from its own previous framing too long.

With RULES active, the assistant should stop treating earlier framing as truth once the user gives a newer controlling direction.
