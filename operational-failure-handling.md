# Operational Failure Handling

> **Current Version:** 1.2
> **Design:** [design/operational-failure-handling.design.md](design/operational-failure-handling.design.md) v1.2
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/operational-failure-handling.changelog.md](changelog/operational-failure-handling.changelog.md)

---

## Rule Statement

**Core Principle: Handle technical and operational failures with explicit classification, profile-driven case handling, bounded retry ceilings, honest cooldown guidance, and clear stop/escalation behavior without pretending rules can enforce timers or delayed retries.**

This rule governs general post-failure operational behavior. It complements recovery, refusal, and emergency rules, but does not replace their authority.

---

## Core Principles

### 1) Classify-Before-Retry Principle

Do not treat every failure as retriable by default.

Required guidance:
- classify the failure before deciding whether to retry
- distinguish between transient, systemic, and deterministic non-retriable conditions
- avoid retrying just because the first error message looked generic

### 2) Profile-First Principle

When a known operational case matches, use the case profile instead of generic retry language.

Required guidance:
- apply the matching case-specific profile when one exists
- let the profile refine immediate-retry, cooldown, and stop behavior
- fall back to generic class defaults only when no case profile matches

### 3) Bounded-Retry Principle

Retries must have hard ceilings.

Required guidance:
- use the class-specific retry budget as the default ceiling
- stop when the applicable budget is exhausted
- do not keep retrying the same objective without new evidence or a state change

### 4) Same-Objective-Aggregate Budget Principle

One user objective keeps one retry budget even when the tool changes.

Required guidance:
- treat the same user-facing goal as one objective across tools and domains
- do not reset retry count when switching tools, wrappers, or providers
- respect the aggregate same-turn retry cap across the full objective

### 5) Stop-When-Deterministic Principle

If a retry cannot change the result, do not spend more attempts.

Required guidance:
- stop immediately for deterministic non-retriable failures
- do not misclassify missing authorization, invalid input, approval denial, or policy constraints as transient
- require a real input, state, authorization, approval, policy, or context change before retrying again

### 6) Cross-Domain-Escalation Principle

Repeated failure across tools or domains is evidence, not progress.

Required guidance:
- promote repeated similar failures across multiple tools/domains toward systemic classification
- switch from repetitive execution to broader diagnosis when retry evidence stops adding value
- keep escalation inside the same turn when a safer recovery path exists

### 7) Cooldown-Honesty Principle

Recommended cooldowns are policy guidance, not proof that a wait occurred.

Required guidance:
- state recommended cooldowns honestly
- surface provider `Retry-After` guidance when present
- do not claim that the rule itself slept, waited, or will automatically retry later unless a real runtime mechanism exists

### 8) Future-Extensible Profile Principle

The chain must remain able to accept additional operational cases later.

Required guidance:
- add future cases as explicit profiles rather than by inventing new ad hoc retry language each time
- keep future profiles inside the same taxonomy and retry-posture vocabulary unless the chain itself is intentionally redesigned

---

## Failure Classes

| Failure Class | Meaning | Common Signals | Default Retry Posture |
|---------------|---------|----------------|-----------------------|
| `POTENTIALLY_TRANSIENT` | The failure may clear without a material input or policy change | timeout, temporary network issue, `429` with retry guidance, `502`/`503`, short-lived lock contention | `AUTONOMOUS_RETRY_ALLOWED` |
| `LIKELY_SYSTEMIC` | The failure likely reflects a broader environment, provider, or shared dependency problem | repeated similar failures across tools/domains, provider outage, DNS failure, environment-wide connectivity failure, repeated auth service unavailability | `CONFIRMATION_RETRY_ONLY` |
| `DETERMINISTIC_NON_RETRIABLE` | Retrying the same objective without a state change will predictably fail again | missing authorization, unsupported operation, invalid path, missing required input, policy block, malformed request, absent dependency/config, unchanged approval denial | `NO_RETRY_UNTIL_CHANGE` |

Classification notes:
- if the first failure is uncertain, allow at most one probe retry
- an identical repeat after the probe retry promotes the condition to `LIKELY_SYSTEMIC` unless the evidence is clearly deterministic and non-retriable
- generic error wording does not justify retrying deterministic missing-input or authorization problems

---

## Retryability Contract

### Same-Objective Rule
`same objective` means the same user-facing goal in the same turn, even if the assistant changes tools, wrappers, providers, or domains while pursuing it.

### Immediate-Retry Gate
Immediate retry is allowed only when all of the following are true:
- the matching case profile explicitly allows it, **or** the failure is still uncertain and qualifies for one low-blast-radius probe retry
- no provider `Retry-After` or equivalent wait requirement blocks immediate retry
- the failure does not already indicate deterministic non-retriability
- the same-objective aggregate budget still permits another attempt
- user instructions and safety boundaries do not prohibit autonomous retry

### Required behavior
- tool or domain switching does **not** reset retry budget
- repeated similar failures across **2 or more tools/domains** or **3 total occurrences** in one turn escalate to `LIKELY_SYSTEMIC`
- if the first failure is uncertain, allow at most **1 probe retry**
- if the probe retry produces the same failure again, promote the situation to `LIKELY_SYSTEMIC` unless the evidence is clearly deterministic
- explicit upstream/provider `Retry-After` guidance overrides default cooldown recommendations

### Retry posture vocabulary
Use one of these values when operational failure handling is materially relevant:
- `AUTONOMOUS_RETRY_ALLOWED`
- `CONFIRMATION_RETRY_ONLY`
- `STOP_AND_ESCALATE`
- `NO_RETRY_UNTIL_CHANGE`

---

## Default Retry Budgets and Cooldowns

These values are recommended operational policy, not runtime-enforced timers.

| Failure Class | Default Budget | Recommended Cooldown | Notes |
|---------------|----------------|----------------------|-------|
| `POTENTIALLY_TRANSIENT` | Up to **2 autonomous retry rounds** for the same objective in the same turn | **2s before retry 1**, **10s before retry 2** | case profiles may narrow this |
| `LIKELY_SYSTEMIC` | At most **1 confirmation retry** | **30s** or until an external state change is observed | use only if the extra retry can add signal |
| `DETERMINISTIC_NON_RETRIABLE` | **0 retries** until input, state, authorization, approval, policy, or context changes | none until a relevant change occurs | stop immediately |

### Aggregate protection
- same-objective aggregate retry budget in one turn: **maximum 3 autonomous retry rounds total** across tools and domains
- the aggregate cap applies even if class-specific ceilings would otherwise allow another retry
- the assistant may stop earlier than the default ceiling when additional retries would increase cost, churn, or risk without adding useful information

---

## Case-Specific Profiles

### Profile precedence
Apply this order when multiple signals exist:
1. hard policy, authority, and user-instruction boundaries
2. explicit upstream/provider guidance such as `Retry-After`
3. matching case-specific profile
4. generic class defaults

### Mandatory case fields
Every present or future case profile should define:
- `case_id`
- `applies_to`
- `match_signals`
- `initial_failure_class`
- `retry_posture`
- `immediate_retry_rule`
- `budget_or_override_rule`
- `cooldown_policy`
- `promotion_rule`
- `stop_condition`
- `recovery_direction`
- `communication_notes`

### Seeded profiles

#### `WEB_SEARCH_TIMEOUT`
- `initial_failure_class`: `POTENTIALLY_TRANSIENT`
- `retry_posture`: `AUTONOMOUS_RETRY_ALLOWED`
- `immediate_retry_rule`: allow **1 immediate probe retry** in the same turn when no provider wait guidance exists and blast radius is low
- `promotion_rule`: identical repeat promotes to `LIKELY_SYSTEMIC`
- `stop_condition`: after promotion, stop blind retries and escalate
- `communication_notes`: say the timeout may be transient and report real `attempts_used`

#### `WEB_SEARCH_429_WITH_RETRY_AFTER`
- `initial_failure_class`: `POTENTIALLY_TRANSIENT`, constrained by provider guidance
- `retry_posture`: `STOP_AND_ESCALATE` in the current turn when deterministic waiting cannot be enforced
- `immediate_retry_rule`: **no immediate retry**
- `cooldown_policy`: use provider `Retry-After`, not guessed fallback delay
- `stop_condition`: do not spend more same-turn autonomous retries unless a real wait or later state change occurs
- `communication_notes`: say the provider required the wait and say directly if the runtime did not actually wait

#### `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE`
- `initial_failure_class`: `POTENTIALLY_TRANSIENT` on first occurrence
- `retry_posture`: `AUTONOMOUS_RETRY_ALLOWED` initially, then `STOP_AND_ESCALATE` after systemic promotion
- `immediate_retry_rule`: allow **1 immediate confirmation retry** when no provider wait guidance exists and blast radius is low
- `promotion_rule`: repeated same-signal failure or similar failure across alternate web/search paths promotes to `LIKELY_SYSTEMIC`
- `stop_condition`: after promotion, stop blind retries and move to diagnosis or later retry guidance
- `communication_notes`: identify provider-side instability rather than implying user-input error

#### `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED`
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE`
- `retry_posture`: `NO_RETRY_UNTIL_CHANGE`
- `immediate_retry_rule`: **no immediate retry**
- `stop_condition`: do not retry the same unauthenticated fetch path until authorization or tool capability changes
- `recovery_direction`: use an authenticated/specialized access path or ask the user for an accessible source

#### `WEB_FETCH_INVALID_URL_OR_BAD_INPUT`
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE`
- `retry_posture`: `NO_RETRY_UNTIL_CHANGE`
- `immediate_retry_rule`: **no immediate retry**
- `stop_condition`: do not retry until the URL or input is corrected
- `recovery_direction`: request the corrected URL or supported target form

#### `LOCAL_FILE_NOT_FOUND`
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` for the same exact path
- `retry_posture`: `NO_RETRY_UNTIL_CHANGE`
- `immediate_retry_rule`: **no retry on the same path**
- `stop_condition`: repeated reads of the same missing path are not justified
- `recovery_direction`: verify path spelling, search for the intended file, or ask the user for the corrected path

#### `LOCAL_PERMISSION_DENIED`
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` until permission or access mode changes
- `retry_posture`: `NO_RETRY_UNTIL_CHANGE`
- `immediate_retry_rule`: **no immediate retry**
- `stop_condition`: do not re-run the same denied access path unless permission context actually changes
- `recovery_direction`: ask for permission change, alternate readable path, or user-approved escalation

#### `TOOL_APPROVAL_DENIED`
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` until the user changes approval state or chooses another method
- `retry_posture`: `NO_RETRY_UNTIL_CHANGE`
- `immediate_retry_rule`: **no immediate retry of the denied call**
- `stop_condition`: the same denied tool call must not be re-attempted unchanged
- `recovery_direction`: explain the alternative non-denied path or ask whether the user wants a different method

#### `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE`
- `initial_failure_class`: `LIKELY_SYSTEMIC` until current team state is inspected
- `retry_posture`: `STOP_AND_ESCALATE`
- `immediate_retry_rule`: **no immediate respawn of a same-role teammate**
- `budget_or_override_rule`: do not spend autonomous retries by spawning overlapping teammates while duplicate-looking state remains unresolved
- `cooldown_policy`: none until state changes; inspect first rather than waiting blindly
- `promotion_rule`: repeated same-role respawn attempts without inspecting current team state remain systemic churn, not progress
- `stop_condition`: stop when the duplicate-looking agent may still be active, stale in UI/team state, or not yet cleanly removed
- `recovery_direction`: inspect current team membership/state, request shutdown or cleanup when needed, and only respawn if the role is truly absent or the new teammate has a clearly distinct partitioned job
- `communication_notes`: separate observed duplicate-looking presence from inference about whether the duplicate is real overlap or stale state

### Future profile additions
Future cases may be added, but they must:
- use the mandatory case fields above
- stay inside the existing failure-class taxonomy
- stay inside the existing retry-posture vocabulary unless the chain itself is intentionally redesigned
- narrow generic retry behavior when needed, not silently bypass the aggregate retry cap
- defer to provider guidance and higher authority boundaries when those exist

---

## Stop and Escalation Contract

Stop autonomous retries when any of the following is true:
- the failure is `DETERMINISTIC_NON_RETRIABLE`
- the applicable case profile says no immediate retry or no same-turn retry is justified
- the class-specific budget is exhausted
- the same-objective aggregate retry budget is exhausted
- the same or strongly similar failure appears across 2 or more tools/domains
- 3 total occurrences in the turn indicate a broader issue
- repeated retries would increase blast radius, cost, or operational churn without improving certainty

When stopping, escalate inside the same turn when helpful by moving to one or more of these paths:
- broader diagnosis instead of repeating the same action
- user coordination for missing state, authorization, approval, or context
- alternate safe recovery path
- explicit wait-for-state-change recommendation
- recommendation to use hooks, wrappers, or orchestration when deterministic delayed retry behavior is required

This rule defines stop conditions and escalation logic. It does **not** claim that the rule itself can sleep, back off on a timer, or guarantee future retry execution.

---

## Communication Contract

### Mandatory mini-schema
When operational failure handling is materially relevant, use this deterministic post-failure schema:

```text
failure_class: <POTENTIALLY_TRANSIENT | LIKELY_SYSTEMIC | DETERMINISTIC_NON_RETRIABLE>
retry_posture: <AUTONOMOUS_RETRY_ALLOWED | CONFIRMATION_RETRY_ONLY | STOP_AND_ESCALATE | NO_RETRY_UNTIL_CHANGE>
attempts_used: <used>/<budget>
recommended_cooldown: <2s | 10s | 30s | provider Retry-After | none until state changes>
reason: ...
what_can_be_done_now:
- ...
how_to_proceed:
- ...
```

### Required honesty
- `attempts_used` must reflect real attempts, not planned attempts
- `recommended_cooldown` is guidance, not proof that waiting occurred
- if no deterministic waiting mechanism exists, say so directly instead of implying that the assistant already waited
- if provider `Retry-After` guidance exists, surface it explicitly instead of guessing a replacement delay
- if the aggregate cap is the real limiter, make that clear in `reason` or `how_to_proceed`
- if a matching case profile prevented immediate retry, explain that explicitly instead of using vague language

### Boundary statement
This mini-schema is an operational-failure contract, not a second refusal framework.
It does not redefine `HARD_BLOCK`, `SOFT_BLOCK`, or `WORKFLOW_BLOCK`, and it does not replace `emergency-protocol`.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| blind retry looping | wastes attempts and hides root cause | classify first and stop at bounded ceilings |
| tool switching to reset budget | disguises repeated failure as fresh progress | keep one same-objective budget across tools/domains |
| treating missing auth/input as transient | creates noisy retries and false hope | classify as `DETERMINISTIC_NON_RETRIABLE` |
| pretending a cooldown elapsed | violates verification honesty | state the recommended cooldown and actual runtime limitation honestly |
| ignoring provider `Retry-After` | discards authoritative guidance | prefer upstream retry guidance over defaults |
| generic retry language when a matching case profile exists | makes the rule vague and under-specified | apply the matching case-specific profile explicitly |
| dead-end failure report | leaves the user without a next move | provide `what_can_be_done_now` and `how_to_proceed` |
| redefining refusal classes here | creates parallel authority | keep refusal taxonomy in `refusal-classification.md` |
| using emergency semantics for ordinary failures | blurs mode boundaries | keep emergency behavior in `emergency-protocol.md` |

---

## Flexibility Boundary

Allowed flexibility:
- fewer retries than the default ceiling when retry cost, loop risk, or blast radius is high
- stricter retry behavior when the user asks for no autonomous retries or a narrower policy
- earlier escalation when cross-domain evidence already shows the issue is broader than a one-off transient
- provider-specific cooldown guidance instead of default delays
- future case profiles that narrow or specialize the generic model without breaking the shared taxonomy

Not allowed:
- exceeding the class ceiling or aggregate same-turn ceiling by default
- claiming that rules deterministically slept or will automatically retry after a timer
- using tool switching to bypass retry limits
- inventing cooldown values when authoritative provider guidance exists
- ignoring a matching case profile and falling back to vague generic retry language
- duplicating refusal, emergency, authority, or anti-guessing authority that already belongs to other rules

Deterministic delayed retry automation belongs to hooks, wrappers, or the orchestration/runtime layer.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Failure classification clarity | High |
| Same-objective retry-bound adherence | 100% |
| Aggregate retry-cap adherence | 100% |
| Honest cooldown communication | 100% |
| Dead-end failure reports | 0% |
| Case-profile application when matched | High |
| Seeded case-profile coverage | High |
| Refusal/emergency authority duplication | 0 critical cases |

---

## Integration

Related rules:
- [recovery-contract.md](recovery-contract.md) - reuse compact recovery wording for `reason`, `what_can_be_done_now`, and `how_to_proceed`
- [refusal-minimization.md](refusal-minimization.md) - prefer recoverable paths over premature stop
- [functional-intent-verification.md](functional-intent-verification.md) - stop earlier when retry loops or blast radius increase operational risk
- [refusal-classification.md](refusal-classification.md) - keeps refusal taxonomy authority separate
- [emergency-protocol.md](emergency-protocol.md) - keeps emergency-mode semantics separate
- [authority-and-scope.md](authority-and-scope.md) - keeps authority precedence outside this rule
- [zero-hallucination.md](zero-hallucination.md) - wait/cooldown claims must stay honest and verified
- [no-variable-guessing.md](no-variable-guessing.md) - do not guess missing inputs or configuration during recovery
