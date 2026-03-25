# Operational Failure Handling

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** 451fb64e-f2a5-43a5-bf98-47f01244f15c (2026-03-12)

---

## 1) Goal

Create one first-class rule chain for generalized technical and operational failure handling so the assistant can:
- classify failure types
- apply bounded retry ceilings
- recommend cooldowns honestly
- stop when retrying no longer changes the outcome
- escalate across tools or domains without resetting budget
- communicate recovery paths without pretending timers or delayed retries were enforced
- apply explicit case-by-case handling where a known failure pattern has a better deterministic response than the generic default
- accept future case additions without redefining the base taxonomy every time

This chain governs policy and decision behavior only. It does not define runtime automation.

---

## 2) Problem Statement

Adjacent rules already cover refusal taxonomy, blocked-response recovery, emergency mode, pre-execution risk review, authority, and verification honesty. The repository still lacked one first-class operational-failure policy for ordinary technical failures after execution starts.

The original v1.0 gap was partially closed by adding generic retry semantics, but one important problem remained:
- generic retry classes alone are not specific enough for recurring real-world cases such as Web Search timeouts, rate limits, private WebFetch targets, invalid URLs, file-not-found conditions, or permission-denied failures
- some cases justify an immediate retry probe
- some cases require an explicit no-immediate-retry rule
- some cases should stop immediately and pivot to a different recovery path
- the rule chain must stay extensible so future operational cases can be added without inventing a new taxonomy each time

Without case-specific profiles, the rule still reads too broadly and risks collapsing into a vague "if failure then retry within budget" pattern.

---

## 3) Scope and Non-Goals

### In Scope
- Post-failure handling for general technical and operational failures across tools, providers, networks, filesystem, authentication flows, approval flows, and environment dependencies.
- Failure classification into:
  - `POTENTIALLY_TRANSIENT`
  - `LIKELY_SYSTEMIC`
  - `DETERMINISTIC_NON_RETRIABLE`
- Same-objective retry ceilings, aggregate same-turn budget ceilings, and recommended cooldown guidance.
- Explicit case-specific profiles that can override generic retry posture for known patterns.
- Stop conditions and escalation behavior when repeated failures indicate broader issues.
- Structured user-facing post-failure communication using a deterministic mini-schema.
- A future-extension contract for adding additional operational cases.

### Out of Scope
- Refusal taxonomy authority (`HARD_BLOCK`, `SOFT_BLOCK`, `WORKFLOW_BLOCK` remain owned by `refusal-classification`).
- Emergency-mode semantics (owned by `emergency-protocol`).
- Pre-execution destructive-intent clarification or confirmation behavior (owned by `functional-intent-verification`).
- Runtime automation that sleeps, waits, or re-runs tools after a timer.
- Hooks, wrappers, or orchestration implementation details.

### Non-Goal Boundary
This chain may define:
- failure classification
- retry ceilings
- immediate-retry eligibility rules
- recommended cooldowns
- stop conditions
- escalation logic
- case-specific overrides
- communication obligations

This chain may not claim that rules themselves can:
- deterministically sleep for N seconds
- enforce timer-based backoff
- guarantee a future retry after waiting
- prove that a cooldown actually elapsed

Deterministic wait-and-retry automation belongs to hooks, wrappers, or the orchestration/runtime layer.

---

## 4) Failure Taxonomy

| Failure Class | Meaning | Common Signals | Default Posture |
|---------------|---------|----------------|-----------------|
| `POTENTIALLY_TRANSIENT` | The failure may clear without a material input or policy change | timeout, temporary network issue, `429` with retry guidance, `502`/`503`, short-lived lock contention | bounded autonomous retry |
| `LIKELY_SYSTEMIC` | The failure likely reflects a broader environment, provider, or shared dependency problem | repeated similar failures across tools/domains, provider outage, DNS failure, environment-wide connectivity failure, repeated auth service unavailability | at most one confirmation retry, then escalate |
| `DETERMINISTIC_NON_RETRIABLE` | Retrying the same objective without a state change will predictably fail again | missing authorization, unsupported operation, invalid path, missing required input, policy block, malformed request, absent dependency/config | no retry until something changes |

### Classification Notes
- The first failure may be uncertain. In that case, one probe retry is allowed to disambiguate transient vs broader failure.
- An identical repeat after a probe retry promotes the condition to `LIKELY_SYSTEMIC` unless there is clear evidence that the failure is deterministic and non-retriable.
- Deterministic missing-input, policy, authorization, approval, or invalid-target problems should not be mislabeled as transient just because the tool returned a generic error string.

---

## 5) Retry Decision Model

### 5.1 Same-Objective Model
`same objective` means the same user-facing goal in the same turn, even if the assistant switches tools, providers, wrappers, or domains while pursuing it.

Examples:
- retrying the same search through a different web-capable path is still the same objective
- retrying the same filesystem read through an alternate shell path is still the same objective
- retrying a denied tool call with the exact same parameters after the user denied approval is still the same objective and should not be treated as new evidence

### 5.2 Generic Decision Sequence

```text
Failure occurs
  → classify initial failure
  → check whether a matching case-specific profile exists
  → apply provider guidance if present
  → if clearly deterministic, stop
  → if profile allows immediate retry, use that rule
  → otherwise if uncertain, allow one probe retry
  → if identical repeat, promote to likely systemic unless clearly deterministic
  → if retry remains justified, stay within profile + class + aggregate budgets
  → if budget exhausted or cross-domain repetition appears, stop and escalate
```

### 5.3 Immediate-Retry Gate
Immediate retry is allowed only when all of the following are true:
- the matching case profile explicitly allows it, **or** the failure is still uncertain and qualifies for one low-blast-radius probe retry
- no provider `Retry-After` or equivalent upstream wait requirement blocks immediate retry
- the failure does not already indicate deterministic non-retriability
- the same-objective aggregate budget still permits another attempt
- user instructions or safety boundaries do not prohibit autonomous retry

### 5.4 Aggregate Protections
- Same-objective aggregate retry budget in one turn: **maximum 3 autonomous retry rounds total** across tools and domains.
- Tool or domain switching does **not** reset retry budget.
- Repeated similar failures across **2 or more tools/domains** or **3 total occurrences** in one turn escalate the situation to `LIKELY_SYSTEMIC`.
- Explicit upstream/provider `Retry-After` guidance overrides default cooldown recommendations.
- If the assistant cannot deterministically wait, it must state the recommended cooldown honestly rather than pretending the wait already happened.

### 5.5 Retry Posture Vocabulary
Use one of these postures in the communication layer:
- `AUTONOMOUS_RETRY_ALLOWED`
- `CONFIRMATION_RETRY_ONLY`
- `STOP_AND_ESCALATE`
- `NO_RETRY_UNTIL_CHANGE`

This posture describes what retry behavior is still justified after classification and budget evaluation.

---

## 6) Default Retry Budgets and Cooldowns

These values are generic operational defaults, not timer-enforced guarantees.

| Failure Class | Autonomous Retry Budget | Recommended Cooldown | Default Retry Posture |
|---------------|-------------------------|----------------------|-----------------------|
| `POTENTIALLY_TRANSIENT` | Up to **2 autonomous retry rounds** for the same objective in the same turn | **2s before retry 1**, **10s before retry 2** | `AUTONOMOUS_RETRY_ALLOWED` |
| `LIKELY_SYSTEMIC` | At most **1 confirmation retry** | **30s** or until an external state change is observed | `CONFIRMATION_RETRY_ONLY` |
| `DETERMINISTIC_NON_RETRIABLE` | **0 retries** until input, state, authorization, policy, approval, or context changes | none until a relevant change occurs | `NO_RETRY_UNTIL_CHANGE` |

### 6.1 Budget Interpretation
- The class budget is subordinate to the same-objective aggregate cap of 3 autonomous retry rounds total in the turn.
- A matching case profile may narrow these defaults or add a stricter immediate-stop rule.
- A matching case profile may not silently widen the same-objective aggregate cap.
- The assistant may stop earlier than the default budget if retry blast radius, loop risk, or user instructions make additional retries worse than immediate escalation.

---

## 7) Case-Specific Operational Profiles

### 7.1 Purpose
Case-specific profiles exist so the chain can express deterministic behavior for recurring real-world failure patterns instead of relying only on generic class defaults.

### 7.2 Precedence Order
Apply this order when multiple signals exist:
1. hard policy, authority, and user-instruction boundaries
2. explicit upstream/provider guidance such as `Retry-After`
3. matching case-specific profile
4. generic class defaults

### 7.3 Mandatory Profile Schema
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

### 7.4 Seeded Initial Profiles

#### `WEB_SEARCH_TIMEOUT`
- `applies_to`: Web Search or equivalent search-provider request.
- `match_signals`: timeout, upstream timeout, connection reset, or equivalent transient-search failure without deterministic bad-input evidence.
- `initial_failure_class`: `POTENTIALLY_TRANSIENT`.
- `immediate_retry_rule`: allow **1 immediate probe retry** in the same turn when no provider wait guidance exists and blast radius is low.
- `budget_or_override_rule`: stay inside generic transient and aggregate caps.
- `promotion_rule`: an identical repeat promotes to `LIKELY_SYSTEMIC`.
- `stop_condition`: after promotion, do not keep blind-retrying the same search path.
- `recovery_direction`: either escalate to broader diagnosis or suggest retry after external state improvement.

#### `WEB_SEARCH_429_WITH_RETRY_AFTER`
- `applies_to`: Web Search or equivalent provider request returning rate-limit guidance.
- `match_signals`: `429` plus explicit `Retry-After` or equivalent provider cooldown signal.
- `initial_failure_class`: `POTENTIALLY_TRANSIENT`, but constrained by provider guidance.
- `immediate_retry_rule`: **no immediate retry**.
- `budget_or_override_rule`: do not consume additional autonomous retries unless a real wait or later state change occurs.
- `cooldown_policy`: use provider `Retry-After` value instead of generic defaults.
- `promotion_rule`: repeated rate-limit failures after required wait may indicate broader systemic quota pressure.
- `stop_condition`: if deterministic waiting cannot be enforced in the current runtime, stop same-turn autonomous retry and report the required wait honestly.
- `recovery_direction`: tell the user the exact provider cooldown and what would make a later retry meaningful.

#### `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE`
- `applies_to`: Web Search or equivalent provider request with upstream provider failure.
- `match_signals`: `502`, `503`, `504`, provider unavailable, or equivalent server-side search failure.
- `initial_failure_class`: `POTENTIALLY_TRANSIENT` on first occurrence.
- `immediate_retry_rule`: allow **1 immediate confirmation retry** when no wait guidance exists and blast radius is low.
- `promotion_rule`: repeated same-signal failure or similar failure across alternate web/search paths promotes to `LIKELY_SYSTEMIC`.
- `stop_condition`: after promotion, stop blind retries and move to diagnosis or later retry guidance.
- `recovery_direction`: communicate that provider-side instability is suspected rather than implying user-input error.

#### `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED`
- `applies_to`: WebFetch or equivalent unauthenticated fetch path.
- `match_signals`: private page, authenticated target, access denied due to missing auth, or tool limitation on authenticated URLs.
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE`.
- `immediate_retry_rule`: **no immediate retry**.
- `stop_condition`: do not retry the same unauthenticated fetch path until authorization or tool capability changes.
- `recovery_direction`: use an authenticated/specialized access path or ask the user for an accessible source.

#### `WEB_FETCH_INVALID_URL_OR_BAD_INPUT`
- `applies_to`: WebFetch or equivalent web request.
- `match_signals`: malformed URL, unsupported scheme, obviously invalid target, or user input that cannot resolve.
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE`.
- `immediate_retry_rule`: **no immediate retry**.
- `stop_condition`: do not retry until the URL or input is corrected.
- `recovery_direction`: request the corrected URL or supported target form.

#### `LOCAL_FILE_NOT_FOUND`
- `applies_to`: local file read/fetch/open attempt.
- `match_signals`: path does not exist, file missing, or absolute target path cannot be resolved.
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` for the same exact path.
- `immediate_retry_rule`: **no retry on the same path**.
- `stop_condition`: repeated reads of the same missing path are not justified.
- `recovery_direction`: verify path spelling, search for the intended file, or ask the user for the corrected path.

#### `LOCAL_PERMISSION_DENIED`
- `applies_to`: local file or resource access.
- `match_signals`: permission denied, sandbox denial, or equivalent unreadable target without new authorization.
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` until permission or access mode changes.
- `immediate_retry_rule`: **no immediate retry**.
- `stop_condition`: do not re-run the same denied access path unless permission context actually changes.
- `recovery_direction`: ask for permission change, alternate readable path, or user-approved escalation.

#### `TOOL_APPROVAL_DENIED`
- `applies_to`: tool execution requiring approval.
- `match_signals`: explicit user denial of the requested tool call or permission prompt.
- `initial_failure_class`: `DETERMINISTIC_NON_RETRIABLE` until the user changes approval state or chooses another method.
- `immediate_retry_rule`: **no immediate retry of the denied call**.
- `stop_condition`: the same denied tool call must not be re-attempted unchanged.
- `recovery_direction`: explain the alternative non-denied path or ask whether the user wants a different method.

---

## 8) Stop and Escalation Contract

Stop autonomous retries when any of the following is true:
- the failure is classified as `DETERMINISTIC_NON_RETRIABLE`
- the applicable case profile says no immediate retry or no same-turn retry is justified
- the applicable class budget is exhausted
- the same-objective aggregate budget is exhausted
- the same or strongly similar failure appears across 2 or more tools/domains
- 3 total occurrences in one turn indicate the issue is broader than a one-off transient
- repeated retries would increase blast radius, cost, or operational churn without adding new information

When stopping, the assistant should escalate inside the same turn by shifting to one or more of these behaviors when helpful:
- broader diagnosis instead of repeating the same tool action
- user-directed coordination for missing state, authorization, approval, or context
- alternate safe recovery path
- explicit wait-for-state-change recommendation
- wrapper, hook, or orchestration recommendation when deterministic delayed retry behavior is required

This escalation layer must reuse recoverable-path language rather than ending with a dead-end failure report.

---

## 9) Communication Contract

### 9.1 Mandatory Mini-Schema
When operational failure handling is materially relevant, responses should expose this post-failure schema:

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

### 9.2 Honesty Requirements
- `recommended_cooldown` must be framed as guidance, not proof that a wait occurred.
- If no deterministic waiting mechanism exists, the assistant must say so directly.
- If provider `Retry-After` guidance exists, surface it explicitly instead of substituting a guessed delay.
- `attempts_used` must reflect real attempts, not planned attempts.
- Recovery text should reuse the compact recovery-style wording already established by `recovery-contract`.
- When a matching case profile blocked immediate retry, the explanation should say that the stop was case-specific, not arbitrary.

### 9.3 Escalation Communication
When the posture changes from retry to escalation:
- say why the classification changed
- say why further autonomous retries are not justified
- say what safe immediate action remains available
- say what change would make another attempt meaningful
- if a specific case profile matched, say what that profile changed compared with the generic default

---

## 10) Case Extension and Precedence Contract

This chain is intentionally extensible.
Future cases may be added without redefining the base taxonomy, provided they follow all of the following rules:
- a new case profile must use the mandatory case schema from section 7.3
- a new case profile must map into the existing failure-class taxonomy
- a new case profile must use the existing retry-posture vocabulary unless the chain itself is intentionally redesigned
- a new case profile may narrow generic retry behavior, shorten budgets, or add stricter stop conditions
- a new case profile may not silently exceed the same-objective aggregate retry cap
- explicit provider guidance still overrides the profile
- hard authority, safety, and user-instruction boundaries still override the profile
- if no case profile matches, the generic model remains the fallback

---

## 11) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Required Behavior |
|--------------|--------------|-------------------|
| blind retry looping | wastes turns and hides root cause | classify first and stop at bounded ceilings |
| tool switching to reset budget | disguises repeated failure as fresh progress | keep one same-objective budget across tools/domains |
| treating missing auth/input as transient | creates false hope and noisy retries | classify as `DETERMINISTIC_NON_RETRIABLE` |
| pretending a cooldown elapsed | violates verification honesty | report the recommended cooldown and actual limitation honestly |
| ignoring provider `Retry-After` | discards authoritative guidance | prefer upstream retry guidance over defaults |
| generic retry language when a matching case profile exists | makes the rule feel vague and under-specified | apply the matching case-specific profile explicitly |
| dead-end failure report | leaves no recovery path | provide `what_can_be_done_now` and `how_to_proceed` |
| redefining refusal classes here | creates parallel authority | keep refusal taxonomy in `refusal-classification` |
| using emergency semantics for ordinary failures | blurs mode boundaries | keep emergency handling in `emergency-protocol` |

---

## 12) Quality Metrics

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

## 13) Integration

| Document | Relationship |
|----------|--------------|
| [../operational-failure-handling.md](../operational-failure-handling.md) | Runtime implementation of this design |
| [recovery-contract.design.md](recovery-contract.design.md) | Reuse compact recovery wording for `reason`, `what_can_be_done_now`, and `how_to_proceed` |
| [refusal-minimization.design.md](refusal-minimization.design.md) | Preserve recoverable-path preference over premature stop |
| [functional-intent-verification.design.md](functional-intent-verification.design.md) | Reuse loop/scale/blast-radius awareness when retries increase operational impact |
| [refusal-classification.design.md](refusal-classification.design.md) | Keeps refusal taxonomy authority separate |
| [emergency-protocol.design.md](emergency-protocol.design.md) | Keeps emergency-mode semantics separate from ordinary operational failure handling |
| [authority-and-scope.design.md](authority-and-scope.design.md) | Keeps authority precedence outside this chain |
| [zero-hallucination.design.md](zero-hallucination.design.md) | Keeps verification honesty and evidence standards outside this chain |
| [no-variable-guessing.design.md](no-variable-guessing.design.md) | Keeps anti-guessing constraints outside this chain |

---

> Full history: [../changelog/operational-failure-handling.changelog.md](../changelog/operational-failure-handling.changelog.md)
