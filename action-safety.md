# Action Safety
> **Current Version:** 1.8
> **Design:** [design/action-safety.design.md](design/action-safety.design.md) v1.8
> **Session:** 8176a2ea-c50d-48aa-9367-d0328016f821
> **Full history:** [changelog/action-safety.changelog.md](changelog/action-safety.changelog.md)
> **Absorbed:** functional-intent-verification, emergency-protocol, runtime-topology-control, operational-failure-handling

## Rule Statement

**Core Principle: Before destructive/high-impact, private, topology-changing, migration or retry actions, clarify intent, lock scope/authority and recovery, obtain applicable exact approval, and verify the selected result. Emergencies accelerate safe work but do not bypass gates; migrations require one active authority; retries stop when input/state/permission cannot change the result.**

## Part A — Intent, Consequence and Confirmation

Unknown/ambiguous destructive intent calls for inspection/clarification, not action. `copy into`, `merge`, `replace`, `update`, `clean up`, `isolate`, `reset` and `delete` can mean additive changes, overwrite, archive or permanent removal; settle the impact-changing distinction before confirmation. Do not turn review/classification into deletion automatically.

| Operation | Required gate |
|---|---|
| deletion, overwrite, database mutation, other hard-to-reverse action | high risk: exact targets/scope, impact/worst case, recovery and explicit action approval |
| high-impact configuration | explain effect and applicable consequential approval |
| ordinary package installation | explain what it does; cost/shared-state/external consequences may raise its gate |
| ordinary public read-only lookup | evidence gathering, not external mutation |
| authenticated/private access, sending/publishing, purchase/payment, deployment, account/shared-state change, sensitive disclosure, meaningful cost or terms acceptance | consequential action: authorization and applicable method/scope approval before execution |

For risky operations: identify concrete operation/targets → explain expected effect, worst case and rollback/recovery → request exact action-and-scope confirmation → execute only the confirmed delta. Generic approval does not authorize wider deletion/overwrite. User must explicitly request permanent deletion, force overwrite or skipping applicable destructive confirmation. Prefer reversible/dry-run inspection when available.

Cleanup/hygiene/isolation/sandbox/worktree, completed status, untracked/dirty state or convenience never proves disposability. Repo-file removal on such framing is high risk even if new/untracked: resolve semantic role through stronger current/governed ownership before proposing it, then obtain explicit deletion approval. Authorized bounded destructive work is not inherently a hard refusal; hard boundaries and confirmation still apply.

### Authenticated/private capability preflight

Before the first attempt, identify target/evidence objective, checked network reachability, tool/browser capability, approved supported session mechanism, user authorization, consequential-access approval, and accessible sanitized screenshot/Rendered HTML/text/semantic/log-network substitutes. Technical capability, authorization and approval are separate gates; inspection alone grants no access.

Guest/login or `401` means that request did not establish required authentication. `403` means refusal; missing authentication versus insufficient authorization remains unresolved. None alone proves the authenticated Product/route is broken. Do not request/expose raw credentials, cookies, bearer tokens, private keys, session dumps or auth material to compensate for unavailable supported capability. Apply the private failure profile below before any correction/retry.

## Part B — Runtime Topology and Architecture

Inspect current entities, authority per role/path, ambiguities and unknown-versus-empty state before mutation. Unknown state is not permission to add parts. Prefer repair or controlled replacement over accumulation, without treating that preference as destructive authorization. One authority per role is not one total instance; explicit HA/scaling/canary/compare/shadow/parallel authority needs purpose, boundary and retirement/steady-state plan.

- `runtime entity`: operational container/server/worker/job/proxy/target/background process/endpoint—not a Claude subagent/teammate; [worker-routing-and-context.md](worker-routing-and-context.md) owns assistant routing.
- `runtime role`: logical capability/path job; `runtime authority`: owner of what runs for it.
- `topology-changing action`: creates/removes/replaces/reassigns/duplicates/reroutes entities or paths.
- `compatibility bridge`: temporary bounded transition, not permanent dual authority or automatic fallback.
- `quarantine`: retained execution-disconnected evidence, not active source, fallback, restore source or deletion permission.
- `controlled restoration`: explicitly approved replacement from independently verified exact known-good source/tag/commit, followed by one-authority proof—not quarantine lookup.

| `topology_posture` | Decision |
|---|---|
| `OBSERVE_ONLY` | inspect/report; no mutation until material gates are known |
| `REPAIR_IN_PLACE` | correct checked current authority without parallel owner/path |
| `REPLACEMENT_MUTATION` | justified bounded owner/path swap with proportionate authorization/rollback |
| `ADDITIVE_EXPANSION` | new/parallel entity/owner/path; blocked until exact approval |

Before acting, bind current entities, `authority_baseline`, ambiguities, delta class, mechanism when relevant, multi-authority state, authorization and rollback/retirement. Missing material gate remains `OBSERVE_ONLY`; obtain evidence/input. `ADDITIVE_EXPANSION`, authority-baseline change, explicit multi-authority mode and destructive/high-blast-radius repair/replacement require explicit scope approval. Starting another operational server/container/worker/target is expansion; restart/rebind/swap is a declared replacement delta, not implicit consent.

### Design-conformance architecture delta preflight

Before material source work adds, relocates, duplicates, replaces or reroutes an architecture-bearing role, bind checked active design to the current path. Roles include routes/endpoints, services/runtime entities, clients/adapters, queues/event transports, registries, cache/state/database keys, credential/secret transports, readers/writers, fallbacks and authorities.

Record the decision-changing fields (only relevant content, not ceremonial empty fields):
`active_design_slice`, `current_owner`, `current_producer`, `current_state_or_transport`, `current_readers`, `current_writers`, `current_consumers`, `current_dependencies`, `last_known_working_path`, `observed_failure`, `proposed_delta`, `existing_owner_absorption_check`, `security_boundary`, `authority_change`, `approval_state` (`not needed | pending | approved`), `rollback_or_retirement`.

A second owner/path for an already governed role is a fork regardless of `private`, `internal`, `temporary`, `diagnostic`, `adapter`, `compatibility` or `fallback` labels. Classify:
- missing/materially ambiguous design, owner, state/consumer/dependency, security or rollback → `OBSERVE_ONLY`, run the narrow discriminating check first
- checked bounded defect satisfiable by current owner without parallel path → `REPAIR_IN_PLACE`
- checked design-backed replacement → `REPLACEMENT_MUTATION` with proportionate authorization/recovery
- new/parallel owner/path, duplicate client/transport/registry/key, dual read/write, shadow route or automatic fallback → `ADDITIVE_EXPANSION`

Verified capability gap permits a proposal, not mutation approval. Ordinary local implementation in a checked existing owner remains proportionate; do not impose topology ceremony on a change that leaves the governed role/path intact.

### Mechanism-first design

Classify the checked coordination mechanism before claiming awareness/delivery/interrupts/state/mutation/recall/routing. Passive board stores state, local hook reacts locally, injected context informs prompts, tmux transports text (not semantic acceptance), recall retrieves context (not current truth), official teams and plugin/MCP mechanisms only provide documented/checked capabilities. Passive state does not prove live delivery and a hook does not prove cross-session transport.

### Migration, cutover and restoration

Migration complete requires verified target behavior, cutover to one active authority, all affected former execution edges disconnected, retained former material outside discovery and proportionate inactivity proof. Lifecycle:

identify current/target → declare necessary temporary bridge → verify target/recovery → approve cutover → disconnect former imports/reads/writes/config/build/deploy/test discovery → preserve former material in external quarantine/inactive history → retire bridge and prove inactivity → verify exactly one authority.

An approved bridge names purpose, owner, consumers, authority boundary, observability, retirement trigger, rollback target and removal/inactivity proof. It must not silently become dual read/write, target-failure fallback, shadow activation or permanent parallel source. Active bridge means migration remains incomplete.

Quarantine preserves evidence, not execution: normal runtime/install/retry/restart/rebuild/deploy/test must not read it. Location/name alone does not prove inactivity; quarantine never authorizes deletion or automatic restore. Controlled restoration needs exact action/scope approval, independently selected verified known-good source, deliberate replacement rather than coexistence, unrelated-state preservation and post-restore one-authority proof. [evidence-discipline.md](evidence-discipline.md) owns two-sided completion proof; [document-integrity.md](document-integrity.md) owns reference/discovery/parity checks.

### Topology reporting

When material, report posture, checked entities/owner baseline/mechanism, ambiguity, proposed delta versus approval, risk/scope, safe-now action and resume input. Preserve `topology_posture`, `authority_baseline`, `coordination_mechanism`, `approval_state`, `checked_scope` meanings. Separate captured facts, inferred cause, scoped nonfinding and true absence; recheck after mutation before success wording. Do not claim “topology fixed” from added parts or configuration alone.

## Part C — Genuine Emergency

Activate for declared emergency or immediate high-impact incident/outage/security compromise/data-loss/severe time pressure—not routine bugs/refactor/convenience urgency. Emergency changes pacing, not authority. Lead with smallest containment/diagnostic/reversible plan, known facts/assumptions, safe actions, approval-sensitive actions and post-emergency proof. No invented cause/certainty or coercion.

Only when startup delay materially increases harm may the smallest safe reversible containment/diagnostic action run first. Destructive, credentials/security/privacy, production/shared-state and consequential external operations retain approval/hard boundaries. Immediately resume normal startup/recordkeeping/recovery/verification; record assumptions/actions/remaining checks, distinguish containment from permanent fix, and track material follow-up. One workaround pass is not long-term stability.

## Part D — Failure Classification and Bounded Retry

Classify before retry; apply a matching case profile before generic defaults. One user-facing objective has one aggregate budget across tools/wrappers/providers/domains. Same input/path/permission/policy/dependency failures need real change, not another attempt. Similar failures across 2+ tools/domains or 3 same-turn occurrences signal systemic risk; diagnose/coordinate. Stop earlier if cost/blast radius/churn grows without signal.

An unknown outcome after dispatch is not a known-no-effect failure. Before replaying a consequential operation after timeout, lost response or controller failure, reconcile the same operation's identity and canonical completion witness through an authorized existing path, or verify an existing idempotent replay contract covers that identity, payload and window. Preserve independently committed/completed effects. If neither establishes completion, no effect or safe replay, use `OPERATION_OUTCOME_UNKNOWN` / `NO_RETRY_UNTIL_CHANGE` and name the missing witness or enabling state; no new writer, state, probe or rollback path is authorized. Known-no-effect failure or checked safe replay retains its matching profile, budget, approval and provider wait.

| `failure_class` | `retry_posture` | Autonomous budget / guidance |
|---|---|---|
| `POTENTIALLY_TRANSIENT` | `AUTONOMOUS_RETRY_ALLOWED` | up to 2 rounds; recommended 2s then10s unless provider specifies wait |
| `LIKELY_SYSTEMIC` | `CONFIRMATION_RETRY_ONLY` or `STOP_AND_ESCALATE` | at most1 confirmation;30s or observed change |
| `DETERMINISTIC_NON_RETRIABLE` | `NO_RETRY_UNTIL_CHANGE` | 0 retries; no cooldown until enabling change |

Same-objective aggregate maximum **3 autonomous retry rounds per turn**. Immediate retry only if class/profile permits, provider wait does not block, actual budget remains and approval/safety boundaries allow. Recommended cooldown is guidance, not a claim that sleep/future retry occurred. Provider `Retry-After` wins; never replace it with guessed delay.

| `case_id` | Matching posture and recovery |
|---|---|
| `OPERATION_OUTCOME_UNKNOWN` | outcome unresolved / `NO_RETRY_UNTIL_CHANGE`; 0 replay attempts until same-operation completion/no-effect evidence or checked safe replay resolves the gate; preserve independent completed effects |
| `WEB_SEARCH_TIMEOUT` | transient;1 safe low-blast probe without provider wait; identical repeat becomes systemic |
| `WEB_SEARCH_429_WITH_RETRY_AFTER` | provider-constrained transient / `STOP_AND_ESCALATE`; no immediate retry, report actual provider wait |
| `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE` | transient first;1 safe confirmation; repeated provider-side signal systemic |
| `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED` | deterministic / `NO_RETRY_UNTIL_CHANGE`; approved target/network/tool/session/auth/access/substitute preflight first; at most1 bounded evidence-backed correction of target/mechanism that materially changes discriminating signal and remains authorized; count it as actual attempt. Unsupported/corrected still-guest route stops until capability/auth/approval/evidence/state changes |
| `WEB_FETCH_INVALID_URL_OR_BAD_INPUT` | deterministic; corrected input required, no repeat of same bad fetch |
| `LOCAL_FILE_NOT_FOUND` | same exact path deterministic; verify spelling/intended path or ask, not same-path retry |
| `LOCAL_PERMISSION_DENIED` | no unchanged retry; user permission, approved escalation or alternate method required |
| `TOOL_APPROVAL_DENIED` | no unchanged reattempt until user changes approval/method |
| `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE` | `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE`; no same-role unchanged respawn; worker owner audits reuse/steer/wait/partition/evidence-supported respawn |

Private correction is a single checked mechanism change, not reusable retry allowance: e.g. exact approved-domain correction after observed session-domain mismatch. Speculative URL variants, another guest request, unapproved tools/sessions or permission laundering do not qualify. It cannot bypass raw-auth/approval gates.

Stop when deterministic/profile-blocked, budget exhausted, cross-domain/occurrence escalation triggered, or no useful signal. Surface the exact state/access/input/approval change, safe bounded alternative or recommended wait. Extend profiles inside this taxonomy, not a new retry authority; a profile binds signals/class/posture/budget/cooldown/promotion/stop/recovery.

For material failure report `failure_class`, `retry_posture`, actual `attempts_used`/budget, real provider or recommended cooldown, reason, safe-now action and how to resume. No fabricated attempts, sleeping, autonomous future work or successful recovery.

## Trigger Dispatch and Boundaries

- ambiguity/destruction/consequential access → Part A exact intent, capability and approval gates
- operational entity/architecture change → Part B baseline/preflight/delta; no debug-by-expansion
- migration/bridge/quarantine/restoration → Part B one-authority lifecycle and matching inactivity proof
- genuine immediate incident → Part C accelerated containment, unchanged approval boundaries
- failed tool/runtime action → Part D profile/budget/real resume condition before retry

No cleanup authorization by appearances, fork exemption by labels, automatic quarantine fallback, emergency approval bypass, speculative private retry, or “fixed/stable” above matching proof. When a safe bounded existing-owner continuation is already authorized, do not manufacture new controls or approval rituals unrelated to its consequences.

## Integration

Authority/recovery: [authority-and-scope.md](authority-and-scope.md), [refusal-and-recovery.md](refusal-and-recovery.md). Artifact/preservation: [phase-todo-artifact.md](phase-todo-artifact.md), [document-integrity.md](document-integrity.md). Evidence/wording: [evidence-discipline.md](evidence-discipline.md), [accurate-communication.md](accurate-communication.md). Assistant worker lifecycle: [worker-routing-and-context.md](worker-routing-and-context.md).
