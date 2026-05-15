# Action Safety
> **Current Version:** 1.0
> **Design:** [design/action-safety.design.md](design/action-safety.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/action-safety.changelog.md](changelog/action-safety.changelog.md)
> **Absorbed:** functional-intent-verification, emergency-protocol, runtime-topology-control, operational-failure-handling

---

## Rule Statement

**Core Principle: Before executing destructive, ambiguous, high-impact, topology-changing, or retry-after-failure actions, classify intent and risk, lock authority and rollback direction, gate destructive or topology-expanding steps on explicit confirmation, accelerate response in genuine emergencies without abandoning evidence or approval gates, and bound retries by failure class with honest cooldown reporting.**

This rule unifies intent verification, destructive-action confirmation, runtime topology control, emergency response posture, and operational failure / retry handling. It does not replace authority/scope precedence, anti-guessing, evidence/zero-hallucination discipline, or refusal/recovery chains.

---

## Part A — Functional Intent Verification

### Core posture
- **Clarify before execute:** do not run destructive or high-impact action until intent is clear. Clarify ambiguous destructive terms; do not treat convenience, cleanliness, cleanup, or assistant preference as authorization.
- **Destructive-Action Confirmation:** deletion, overwrite, and other hard-to-reverse actions require explicit confirmation tied to the actual action and scope, not vague approval language.
- **Cleanup-Is-Not-Authorization:** cleanup, hygiene, isolation, sandbox, or worktree rationale does not authorize deletion or prove a file is disposable. If a file's semantic role is unclear, resolve it through stronger authority surfaces first.
- **Scope and impact first:** for multi-file or irreversible state, identify affected items, explain expected outcome and worst-case impact, and provide rollback direction.
- **Safe default:** without explicit destructive authorization, ask rather than guess; do not escalate review/classification into delete/remove automatically.

### Ambiguous Terms
`copy into` may mean add or replace; `merge` may overwrite; `delete` may mean permanent removal or archive; `replace` may overwrite; `update` may mean edit existing or create a duplicate/version; `clean up` may remove files; `isolate` may discard local files.

### Risk Model

| Operation | Risk | Required behavior |
|---|---|---|
| Delete files/directories | high | confirm and explain scope |
| Overwrite data | high | confirm and give rollback direction |
| Database modify | high | confirm and provide rollback plan |
| High-impact config change | medium | explain impact |
| Install package | low | explain what it does |

Repo files boundary: if the target is a repo file and the justification is cleanup/hygiene/isolation, treat it as high risk even if new or untracked; stronger semantic authority than git state is required before removal can even be proposed.

### Confirmation Protocol
```text
Risky operation → identify type, scope, impact, rollback path
              → explain what happens, affected items, worst case, recovery
              → request explicit confirmation tied to action and scope
              → execute only if confirmed
```

Cleanup/isolation deletion contract: verify whether stronger authority surfaces already define the file's meaning; if cleanup/hygiene/isolation is the only justification, stop and ask. Proceed only when the user explicitly authorizes the delete action itself.

User must explicitly request permanent deletion, force overwrite, or skipping destructive confirmation where one applies. Prefer dry-run/reversible inspection when available.

---

## Part B — Runtime Topology Control

Inspect current topology, lock one authority baseline per role/path, and prefer repair or controlled replacement over additive expansion unless the user explicitly approves a topology change.

### Core posture
- **Stability over expansion:** unknown runtime state is a reason to inspect, not add more parts.
- **One authority at a time:** keep one authoritative owner per role/path unless the user explicitly wants multi-authority topology; one authority does not mean one instance total.
- **Inspect-before-mutate:** identify entities, authority baseline, ambiguities, and unknown-vs-empty state before any topology change.
- **Replace over accumulate:** prefer `REPAIR_IN_PLACE` or controlled `REPLACEMENT_MUTATION` over additive parallel paths; this is not destructive permission.
- **Explicit topology delta:** classify the step before acting; state whether it changes authority or enters multi-authority mode.
- **Approval gate:** `ADDITIVE_EXPANSION`, authority-baseline changes, multi-authority mode, and destructive/high-blast-radius repair/replacement require explicit approval.
- **Multi-authority exception:** scaling, HA, canary, compare, shadow, or user-requested parallel authorities are valid only with purpose, authority boundaries, and retirement/steady-state plan.

### Vocabulary
- `runtime entity` = container, server process, target, worker, proxy, background job, or assignment endpoint
- `runtime role` = logical job for a path/workflow/capability
- `runtime authority` = layer authoritative for what should run for a role/path
- `coordination mechanism` = checked mechanism such as passive shared board, local hook, injected context, tmux transport, recall/memsearch, official Agent Team, external plugin/MCP, or unavailable
- `topology-changing action` = creates, removes, replaces, reassigns, duplicates, or reroutes runtime entities
- `repair-in-place` / `replacement mutation` / `additive expansion` / `explicit multi-authority mode` = the four delta classes below

### Delta Classes

| Class | Meaning | Default posture |
|---|---|---|
| `OBSERVE_ONLY` | inspect/report without mutation | default until gates pass |
| `REPAIR_IN_PLACE` | correct current topology without parallel owner | preferred when feasible |
| `REPLACEMENT_MUTATION` | replace/swap current owner in bounded way | allowed when justified/safe |
| `ADDITIVE_EXPANSION` | create additional entities/parallel paths | blocked until justified/approved |

### Mutation gate
Before mutating, identify current entities, authority baseline, ambiguities, delta class, coordination mechanism when relevant, multi-authority state, authorization, and rollback/retirement direction. If any gate is missing, remain `OBSERVE_ONLY` and request evidence/input.### Mechanism-first design gate
Before claiming a coordination/runtime design can deliver awareness, requests, interrupts, state sharing, recall, routing, or mutation, classify the checked mechanism and its capability. Passive boards do not prove live delivery; hooks do not prove cross-session transport; injected context does not prove state mutation; tmux input does not prove semantic acceptance; recall does not prove current truth; teams and plugins/MCPs are limited to documented capability.

### Communication Contract
When topology control matters, report:
```text
topology_posture: <OBSERVE_ONLY | REPAIR_IN_PLACE | REPLACEMENT_MUTATION | ADDITIVE_EXPANSION>
current_entities: ...
authority_baseline: <owner per role/path>
coordination_mechanism: <passive board | local hook | injected context | tmux transport | recall/memsearch | official Agent Team | external plugin/MCP | unavailable | not applicable>
ambiguous_authorities: ...
proposed_delta: ...
approval_state: <not needed | pending | approved>
checked_scope: ...
risk_notes: ...
what_can_be_done_now: ...
how_to_proceed: ...
```
Separate observed topology facts from inferred causes, proposed from approved mutations, and scoped non-findings from absence claims. After mutation, state what was rechecked before success wording.

### Boundaries
Allowed: stay `OBSERVE_ONLY`, use bounded repair/replacement, or use explicit multi-authority mode when selected. Not allowed: debug-by-expansion, accidental parallel authority, implicit authority switch, temporary runtime without retirement plan, silent delta escalation, unapproved additive expansion, or unsupported "topology fixed" claims.

---

## Part C — Emergency Protocol

In genuine emergencies, respond faster and with higher signal, but do not abandon evidence, user authority, safety boundaries, approval gates, or post-emergency verification.

### Emergency activation
Activate only when the user declares an emergency or the situation involves immediate high-impact failure, incident response, production outage, security compromise, data-loss risk, or severe time pressure. Do not activate for ordinary bugs, routine feature work, normal refactors, or convenience urgency.

### Rapid but bounded response
Emergency mode changes pacing and presentation, not authority. Provide the smallest useful action plan first, prioritize containment, diagnosis, and reversible steps, keep explanations high-signal, state assumptions and evidence limits when facts are incomplete, and do not fabricate facts, root causes, or certainty because time is short.

### Approval and safety preservation
User authority remains decisive in non-hard-boundary space. Destructive, security-sensitive, shared-state, credential, production, or external actions still require the relevant approval gates. Hard safety/legal/platform boundaries remain non-overridable. Risk analysis should guide the user, not coerce them.

### Post-emergency recovery
After the immediate action slice, return to systematic verification: record assumptions made under time pressure, identify actions taken and remaining verification, separate containment from permanent fix, create or update follow-up tasks/docs when material, and do not treat emergency workaround success as stable long-term proof.

### Emergency Flow
```text
Emergency detected → switch to rapid mode → state containment/diagnostic actions
                  → execute only approved/safe actions
                  → record assumptions and evidence limits
                  → return to normal verification and recovery workflow
```

### Response Shape
```text
Emergency posture: active
Immediate priority: <contain / diagnose / prevent data loss / restore service>
Known facts: ...
Assumptions or unknowns: ...
Safe actions now: 1. ...
Approval needed for: ...
Post-emergency verification: ...
```

---

## Part D — Operational Failure Handling

Classify failures before retrying, apply matching case profiles, respect bounded same-objective retry budgets, report cooldown guidance honestly, and stop/escalate when retrying cannot add signal.

### Core posture
- **Classify before retry:** decide whether the failure is transient, systemic, or deterministic before spending attempts.
- **Profile first:** if a known case profile matches, use it before generic retry defaults.
- **Bound retries:** one same user-facing objective keeps one retry budget even if tools, wrappers, providers, or domains change.
- **Stop when deterministic:** missing authorization/input, invalid path, unchanged approval denial, policy blocks, malformed requests, and absent dependencies require real state/input/authorization change before retry.
- **Escalate cross-domain failure:** similar failures across 2+ tools/domains or 3 total same-turn occurrences indicate systemic risk; switch to diagnosis or coordination.
- **Cooldown honesty:** recommended cooldowns are policy guidance, not proof that Claude slept or will retry later. Provider `Retry-After` wins.
- **Extensible profiles:** add new cases as explicit profiles inside the same taxonomy and retry-posture vocabulary.

### Failure Classes and Retry Posture

| Failure Class | Meaning | Default Posture | Budget / Cooldown |
|---|---|---|---|
| `POTENTIALLY_TRANSIENT` | timeout, temporary network, 429/502/503, short lock contention; may clear without material change | `AUTONOMOUS_RETRY_ALLOWED` | up to 2 autonomous retry rounds; 2s then 10s recommended unless provider says otherwise |
| `LIKELY_SYSTEMIC` | repeated failures, outage, DNS/connectivity, provider/shared dependency issue | `CONFIRMATION_RETRY_ONLY` or `STOP_AND_ESCALATE` | at most 1 confirmation retry; 30s or observed state change |
| `DETERMINISTIC_NON_RETRIABLE` | same objective fails until input/state/access/policy changes | `NO_RETRY_UNTIL_CHANGE` | 0 retries; no cooldown until relevant change |

Same-objective aggregate cap: maximum **3 autonomous retry rounds total** per user-facing objective in one turn, across all tools/domains. Stop earlier when more attempts increase cost, blast radius, or churn without improving certainty. Immediate retry is allowed only when class/profile permits it, no provider wait blocks it, the failure is not deterministic, the budget remains, and user/safety boundaries allow it.

### Case-Specific Profiles
Each profile defines `case_id`, signals, initial class, retry posture, immediate retry rule, budget/cooldown, promotion rule, stop condition, recovery direction, and communication notes.

#### Web/search/fetch

| Case | Class / Posture | Required behavior |
|---|---|---|
| `WEB_SEARCH_TIMEOUT` | `POTENTIALLY_TRANSIENT` / `AUTONOMOUS_RETRY_ALLOWED` | allow 1 low-blast-radius probe retry when no provider wait exists; identical repeat promotes to systemic; report real attempts used |
| `WEB_SEARCH_429_WITH_RETRY_AFTER` | transient but provider-constrained / `STOP_AND_ESCALATE` | no immediate retry; surface provider wait; do not pretend waiting occurred |
| `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE` | transient first, systemic after repeat | allow 1 safe confirmation retry; repeated provider-side signal escalates |
| `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED` | `DETERMINISTIC_NON_RETRIABLE` / `NO_RETRY_UNTIL_CHANGE` | use authenticated/specialized access or ask for accessible source |
| `WEB_FETCH_INVALID_URL_OR_BAD_INPUT` | `DETERMINISTIC_NON_RETRIABLE` / `NO_RETRY_UNTIL_CHANGE` | request corrected URL/input; do not repeat same bad fetch |

#### Local/tool/team

| Case | Class / Posture | Required behavior |
|---|---|---|
| `LOCAL_FILE_NOT_FOUND` | deterministic for same exact path | no same-path retry; verify spelling, search intended path, or ask |
| `LOCAL_PERMISSION_DENIED` | deterministic until permission/access mode changes | no immediate retry; ask for permission, alternate path, or approved escalation |
| `TOOL_APPROVAL_DENIED` | deterministic until user changes approval/method | do not reattempt denied call unchanged; explain safe alternative |
| `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE` | `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE` | no same-role respawn while duplicate/stale state is unresolved; inspect team state first; only respawn if truly absent or distinctly partitioned; separate observed duplicate-looking presence from inference |

### Stop, Escalation, and Communication
Stop autonomous retries when the class/profile is deterministic or blocks immediate retry, any retry budget is exhausted, similar failures appear across 2+ tools/domains or 3 total occurrences, or retries add blast radius/cost/churn without new evidence. Escalate to broader diagnosis, user coordination for missing state/access/context, an alternate safe recovery path, or explicit wait-for-state-change guidance.

When failure handling materially matters, report:
```text
failure_class: <POTENTIALLY_TRANSIENT | LIKELY_SYSTEMIC | DETERMINISTIC_NON_RETRIABLE>
retry_posture: <AUTONOMOUS_RETRY_ALLOWED | CONFIRMATION_RETRY_ONLY | STOP_AND_ESCALATE | NO_RETRY_UNTIL_CHANGE>
attempts_used: <real used>/<budget>
recommended_cooldown: <2s | 10s | 30s | provider Retry-After | none until state changes>
reason: ...
what_can_be_done_now: ...
how_to_proceed: ...
```
Honesty: `attempts_used` must reflect real attempts; cooldown is guidance unless an actual runtime wait occurred; provider `Retry-After` must not be replaced by guessed delay; blocked profiles and aggregate caps must be named.

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| destructive or hard-to-reverse action | apply Part A confirmation protocol; identify scope, impact, rollback first |
| ambiguous destructive term (`copy into`, `merge`, `clean up`, `isolate`, etc.) | clarify intent before acting |
| cleanup/hygiene/isolation framing on repo file | treat as high risk; require stronger semantic authority and explicit delete authorization |
| unclear topology or conflicting authorities | inspect entities/baseline; clarify owner before mutating |
| starting another server/container/worker/target | classify `ADDITIVE_EXPANSION`; justify; request approval |
| restart/rebind/swap current owner | declare replacement delta and rollback direction first |
| scaling/HA/canary/compare/shadow | enter explicit multi-authority mode with boundaries and retirement plan |
| temporary debug runtime | define retirement plan before creation |
| coordination/runtime design claim | classify checked mechanism before claiming delivery, mutation, or authority behavior |
| post-mutation success claim | verify topology and checked scope before claiming success |
| genuine emergency | activate emergency posture; lead with containment; preserve approval gates |
| operational failure | classify before retry; apply matching profile; respect retry budget |
| repeated cross-domain failures | escalate to diagnosis or coordination instead of looping |
| provider `Retry-After` present | surface provider wait; do not pretend waiting occurred |

---

## Anti-Patterns

Avoid: cleanup/hygiene/isolation/worktree rationale used as deletion authority; vague approval standing in for action-and-scope-tied destructive confirmation; debug-by-expansion or accidental parallel authority; implicit authority switch, silent delta escalation, or unapproved additive expansion; temporary runtime without retirement plan; unsupported "topology fixed" claims after mutation; emergency language used to bypass destructive-action confirmation; guessing root cause under pressure; treating temporary mitigation as permanent fix; skipping documentation of assumptions and pending verification; overriding user direction outside hard-boundary constraints; retrying deterministic failures without state change; claiming retries occurred when no real attempt happened; replacing provider `Retry-After` with a guessed delay; looping past the aggregate retry cap; same-role respawn while duplicate/stale team-agent state is unresolved.

Better behavior: classify intent, lock authority, gate destructive or expanding moves on explicit confirmation, accelerate emergencies without abandoning evidence, and bound retries by class with honest reporting.

---

## Integration

Related rules:
- [authority-and-scope.md](authority-and-scope.md) - user authority, hard-boundary precedence, and repo-governed semantic precedence
- [phase-todo-artifact.md](phase-todo-artifact.md) - keeps `not required` from meaning deletion authorization
- [document-integrity.md](document-integrity.md) - creation/duplication hygiene only; never deletion authority
- [evidence-discipline.md](evidence-discipline.md) - inspected-scope facts and local lookup mechanics
- [evidence-discipline.md](evidence-discipline.md) - no guessing under pressure or in retry/cooldown reporting
- [accurate-communication.md](accurate-communication.md) - evidence-strength wording for status, mutation success, and retry attempts
- [worker-routing-and-context.md](worker-routing-and-context.md) - worker/coordination routing before broad absorption
- refusal/recovery chains own blocked-path and safety outcomes; this rule defers to them when a hard boundary or safe-recovery path applies
