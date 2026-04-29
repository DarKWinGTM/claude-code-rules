# Operational Failure Handling

> **Current Version:** 1.2
> **Design:** [design/operational-failure-handling.design.md](design/operational-failure-handling.design.md) v1.2
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/operational-failure-handling.changelog.md](changelog/operational-failure-handling.changelog.md)

---

## Rule Statement

**Core Principle: Classify operational failures before retrying, apply matching case profiles, respect bounded same-objective retry budgets, report cooldown guidance honestly, and stop/escalate when retrying cannot add signal.**

This rule owns post-failure retry posture. It does not replace recovery, refusal, emergency, authority, intent-confirmation, or anti-guessing rules.

---

## Core Contract

1. **Classify before retry.** Decide whether the failure is transient, systemic, or deterministic before spending attempts.
2. **Profile first.** If a known case profile matches, use it before generic retry defaults.
3. **Bound retries.** Same user-facing objective keeps one retry budget even if tools, wrappers, providers, or domains change.
4. **Stop when deterministic.** Missing authorization/input, invalid path, unchanged approval denial, policy blocks, malformed requests, and absent dependencies require a real state/input/authorization change before retry.
5. **Escalate cross-domain failure.** Similar failures across 2+ tools/domains or 3 total same-turn occurrences indicate systemic risk; switch to diagnosis or coordination.
6. **Cooldown honesty.** Recommended cooldowns are policy guidance, not proof that Claude slept or will automatically retry later. Provider `Retry-After` wins.
7. **Extensible profiles.** Add future cases as explicit profiles inside the same taxonomy and retry-posture vocabulary.

---

## Failure Classes and Retry Posture

| Failure Class | Meaning | Default Posture | Budget / Cooldown |
|---|---|---|---|
| `POTENTIALLY_TRANSIENT` | may clear without material input/policy change: timeout, temporary network, 429/502/503, short lock contention | `AUTONOMOUS_RETRY_ALLOWED` | up to 2 autonomous retry rounds; 2s then 10s recommended unless provider says otherwise |
| `LIKELY_SYSTEMIC` | broader environment/provider/shared dependency issue: repeated failures, outage, DNS/connectivity class issue | `CONFIRMATION_RETRY_ONLY` or `STOP_AND_ESCALATE` | at most 1 confirmation retry; 30s or observed state change |
| `DETERMINISTIC_NON_RETRIABLE` | same objective will fail until input/state/access/policy changes | `NO_RETRY_UNTIL_CHANGE` | 0 retries; no cooldown until relevant change |

Same-Objective aggregate cap: maximum **3 autonomous retry rounds total** per same user-facing objective in one turn, across all tools/domains. Stop earlier when more attempts increase cost, blast radius, or churn without improving certainty.

Immediate retry is allowed only when: the class/profile permits it, no provider wait blocks it, the failure is not deterministic, the aggregate budget remains, and user/safety boundaries allow autonomous retry.

---

## Case-Specific Profiles

Every profile should define: `case_id`, scope/signals, initial class, retry posture, immediate retry rule, budget/cooldown rule, promotion rule, stop condition, recovery direction, and communication notes.

### Web/search/fetch

| Case | Class / Posture | Required behavior |
|---|---|---|
| `WEB_SEARCH_TIMEOUT` | `POTENTIALLY_TRANSIENT` / `AUTONOMOUS_RETRY_ALLOWED` | allow 1 low-blast-radius probe retry when no provider wait exists; identical repeat promotes to systemic; report real attempts used |
| `WEB_SEARCH_429_WITH_RETRY_AFTER` | transient but provider-constrained / `STOP_AND_ESCALATE` | no immediate retry; surface provider wait; do not pretend waiting occurred |
| `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE` | transient first, systemic after repeat / retry then stop | allow 1 confirmation retry when safe; repeated provider-side signal escalates |
| `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED` | `DETERMINISTIC_NON_RETRIABLE` / `NO_RETRY_UNTIL_CHANGE` | use authenticated/specialized access or ask for accessible source |
| `WEB_FETCH_INVALID_URL_OR_BAD_INPUT` | `DETERMINISTIC_NON_RETRIABLE` / `NO_RETRY_UNTIL_CHANGE` | request corrected URL/input; do not repeat same bad fetch |

### Local/tool/team

| Case | Class / Posture | Required behavior |
|---|---|---|
| `LOCAL_FILE_NOT_FOUND` | deterministic for same exact path | no same-path retry; verify spelling, search intended path, or ask |
| `LOCAL_PERMISSION_DENIED` | deterministic until permission/access mode changes | no immediate retry; ask for permission, alternate path, or approved escalation |
| `TOOL_APPROVAL_DENIED` | deterministic until user changes approval/method | do not reattempt denied call unchanged; explain safe alternative |
| `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE` | `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE` | no same-role respawn while duplicate/stale state is unresolved; inspect team state first; only respawn if truly absent or distinctly partitioned; separate observed duplicate-looking presence from inference |

---

## Stop and Escalation Contract

Stop autonomous retries when:
- the class/profile is deterministic or blocks immediate retry
- class-specific or aggregate same-objective budget is exhausted
- similar failures appear across 2+ tools/domains or 3 total occurrences
- retries add blast radius, cost, or churn without new evidence

Escalate by switching to broader diagnosis, user coordination for missing state/access/context, an alternate safe recovery path, explicit wait-for-state-change guidance, or hooks/wrappers/orchestration when deterministic delayed retry behavior is required.

---

## Communication Contract

When failure handling materially matters, report:

```text
failure_class: <POTENTIALLY_TRANSIENT | LIKELY_SYSTEMIC | DETERMINISTIC_NON_RETRIABLE>
retry_posture: <AUTONOMOUS_RETRY_ALLOWED | CONFIRMATION_RETRY_ONLY | STOP_AND_ESCALATE | NO_RETRY_UNTIL_CHANGE>
attempts_used: <real used>/<budget>
recommended_cooldown: <2s | 10s | 30s | provider Retry-After | none until state changes>
reason: ...
what_can_be_done_now:
- ...
how_to_proceed:
- ...
```

Required honesty:
- `attempts_used` must reflect real attempts.
- Cooldown is guidance unless an actual runtime wait occurred.
- Provider `Retry-After` must not be replaced by guessed delay.
- If a profile blocked retry or aggregate cap limits the objective, say so.
- This schema is not a second refusal/emergency framework.

---

## Anti-Patterns

| Anti-pattern | Better behavior |
|---|---|
| blind retry loop | classify first and stop at ceilings |
| switching tools to reset budget | keep one same-objective budget |
| treating missing auth/input as transient | classify deterministic |
| pretending cooldown elapsed | state real wait status honestly |
| ignoring `Retry-After` | follow provider guidance |
| generic retry language when profile matches | apply the profile |
| dead-end failure report | give recovery path |
| redefining refusal/emergency classes | defer to their owners |

---

## Verification Checklist

- [ ] failure class is explicit when retry behavior matters
- [ ] matching case profile is applied before generic defaults
- [ ] same-objective and aggregate retry budgets are respected
- [ ] cooldown/wait wording is honest
- [ ] deterministic failures are not retried without state change
- [ ] repeated cross-domain failures escalate instead of looping

---

## Integration

Related rules:
- [recovery-contract.md](recovery-contract.md) - compact recovery wording
- [refusal-minimization.md](refusal-minimization.md) - recoverable alternatives
- [functional-intent-verification.md](functional-intent-verification.md) - blast-radius/intent gates
- [refusal-classification.md](refusal-classification.md), [emergency-protocol.md](emergency-protocol.md) - separate refusal/emergency authority
- [authority-and-scope.md](authority-and-scope.md), [zero-hallucination.md](zero-hallucination.md), [no-variable-guessing.md](no-variable-guessing.md) - authority, factual honesty, and missing-input discipline
