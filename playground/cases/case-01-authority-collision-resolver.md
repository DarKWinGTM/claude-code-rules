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

## Example dialogue (virtual)

### User
`You can use option A.`

### AI without this rule family risk
`Got it. I will continue with option A.`

### User
`Actually, switch to option B now.`

### AI with RULES active
`My working read is that the latest instruction replaces the earlier option. I will use option B unless a hard boundary blocks it.`

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
