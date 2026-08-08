# Worker Routing and Context Control

> **Current Version:** 1.15 (merged M11)
> **Design:** [design/worker-routing-and-context.design.md](design/worker-routing-and-context.design.md) v1.15
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/worker-routing-and-context.changelog.md](changelog/worker-routing-and-context.changelog.md)

---

## Rule Statement

**Core Principle: Use the smallest effective standalone worker lane first for broad, research-heavy, roadmap-analysis-heavy, high-context, high-output, or naturally parallel work; proactively delegate predictable worker-fit slices before the leader session burns avoidable context; manage context load as a full lifecycle covering reading, writing, worker routing, and repair; when selected non-trivial plan-backed or goal-backed work is execution-ready, prefer the smallest effective Subagent-Driven execution path before inline fallback; and after worker routing establishes delegation or specialist need, prefer the best-fit visible custom or specialist agent before generic fallback.**

---

## Core Contract

### 1) Intent and scope boundary
Classify only as deeply as routing requires: behavior/governance, fact lookup, diagnosis, implementation, review/audit, plan/design, coordination/workflow, or explanation. Stay behavior-first for AI/RULES questions; keep diagnosis before edits; inspect project state only when the user requests project facts/implementation/verification or a stated bounded proof need requires it.

Pasted logs, paths, snippets, or worker notes are evidence for the active question, not project-inspection authorization. When intents mix, resolve the dominant execution question and repair scope corrections before exploration.

Direct handling fits trivial, one-step, tightly sequential, low-output, interactive, high-overlap, worker-unavailable, or explicitly user-directed work. Broad searches/reads, noisy tests/logs/builds, external research, roadmap/source comparison, governance/security/migration review, or safely partitionable implementation pass the worker gate first.

### 3) Worker-scale gate after workload detection
`safe-io.md` owns aggregate read/output burst detection. When that gate fires—or when non-I/O work is independently broad, research-heavy, naturally parallel, or safely partitionable—choose the smallest worker topology that preserves correctness and context efficiency.

Before dispatch, identify the objective, required evidence/authority, whether the leader needs raw evidence or an analyzed result, lane independence, edit overlap, worker availability, and user constraints. Prefer one read-only standalone lane for one bounded evidence axis; fan out only for genuinely independent branches; use audit-then-repair when findings must precede a safe bounded edit; escalate to Agent Team only for shared ownership or coordination dependencies.

Dispatch before further raw leader intake. Require a filtered handoff with outcome, checked scope, conflicts/uncertainty, exact anchors, evidence strength, and leader verification needs. The leader remains responsible for selected-anchor verification. Repeated rereads or clarification churn means tighten the brief or topology rather than absorb more raw content.

If Safe I/O detected a worker-fit burst, skipping worker routing blocks broad sync, no-drift, closeout, or release-ready claims unless a narrow direct-handling exception is recorded. Valid exceptions are narrow known files, exact edit/verification ranges, tightly sequential or interactive work, high edit overlap, unavailable worker tooling, explicit user direction, or another stated narrow reason.

### 5) Capability-based routing criteria

Route by capability and workload shape, not rigid tool name. Evaluate user intent/scope, context isolation and output noise, broad evidence-filtering need, lane independence, specialist value, parallel value, coordination/dependencies, risk/security/verification burden, edit overlap, whether the leader needs raw evidence or analyzed result, worker availability, and user constraints. Tool names such as `Agent`, `Explore`, repository search, web search, or future workers are implementation details.

### 6) Work-shape topology selection
| Work shape | Topology / preset | Preferred path |
|---|---|---|
| trivial, exact, low-output, sequential | direct | leader directly |
| one broad evidence axis | scout / `Scout preset` | one focused standalone lane returning a digest and anchors |
| independent read-only axes | fan-out/fan-in / `Compare preset` | focused lanes using a shared rubric, then leader synthesis |
| findings must precede a safe fix | `Audit + Repair preset` | read-only audit, then one bounded non-overlapping repair lane |
| defined test/log/runtime gate | `Verification preset` | evidence lane while implementation ownership stays elsewhere |
| shared ownership/dependencies | coordinated swarm / `Coordinated swarm preset` | official Agent Team only when standalone lanes are insufficient |

Presets are planning shorthand, not Team escalation proof; choose the smallest dependency-fitting topology.

### 7) Research orchestration gate

For broad external research, roadmap/phase-matrix analysis, design-improvement research, provider/API comparison, or source-heavy recommendation work, the leader should define the decision objective and split it into the smallest useful topic lanes before any raw source or roadmap evidence flood enters the leader context.
- identify the decision the research or roadmap analysis should improve, not only the search tool to run
- decompose by independent topic, evidence type, provider, risk area, design axis, phase candidate, dependency, verification gate, or competing approach when that lowers context load or improves coverage
- allow each research lane to refine search topics, query families, and source-selection strategy inside its assigned scope
- prefer one research lane when the question has one coherent evidence axis; use multiple lanes only when topics are meaningfully independent
- require each lane to return analyzed findings with checked scope, source quality, conflicts, implications, and leader verification needs
- the leader should synthesize across lanes, inspect only selected high-value evidence when needed, and avoid treating subagent findings as proof by themselves

### 8) Mechanism-first coordination design

Before proposing broad coordination, worker-runtime, or cross-session behavior, classify the actual mechanism instead of assuming a transport exists.
- identify whether the checked mechanism is a passive shared board, local hook, injected context, tmux transport, recall/memsearch, official Agent Team, external plugin/MCP, or unavailable/unsupported mechanism
- match design claims to checked capability: passive boards store state, hooks react locally, injected context informs prompts, tmux transports text, recall retrieves context, official teams coordinate teammates, and plugins/MCPs provide their documented APIs
- do not design runtime mutation, delivery guarantees, or cross-session authority from an imagined hook, hidden transport, or plugin feature that has not been checked
- keep plugin/shared-board exact grammar outside Main RULES unless an owning plugin or explicit authority surface is selected

### 9) Edit-capable governed-document repair lane

A native edit-capable governed-document repair lane may use a `general-purpose`-style worker only when the leader assigns explicit bounded scope, exact artifacts or sections, and non-overlapping edit ownership.
- broad audits and reviews remain read-only unless edit ownership is explicit
- repair only the assigned governed documents and anchors
- preserve meaning, history reachability, cross-references, and authority-role boundaries
- do not delete files, remove history, relocate content, upgrade status, or mutate authority roles
- stop and return risks when scope, ownership, or meaning preservation becomes ambiguous
- leader verification of changed artifacts is required before sync, no-drift, closeout, or release-ready claims

Edit-capable repair handoffs must include touched artifacts, exact anchors, preservation notes, checks run, unresolved risks, and leader verification needs.

### 10) Standing-role reuse and lifecycle audit

Use stable role-based workers or teammates across phases when the responsibility remains materially the same. Phase or task identifiers are assignment context, not worker identity.
- prefer standing role names for recurring responsibilities
- steer an existing active/recent aligned standing-role worker before spawning a duplicate-looking role
- spawn a new worker only for a genuinely new role, audited unavailability, explicit user-selected separate lane, or simultaneous distinct scope
- when simultaneous lanes need separation, name lanes by real responsibility, surface, or output rather than phase ID alone
- do not report active duplicate overlap, safe absence, or cleanup-ready stale presence from unverified UI residue, stale task state, or memory alone
- keep shared-board grammar and plugin/tmux/session display mechanics outside Main RULES ownership

Audit checked coordination evidence at the smallest useful scope before reuse, spawn, respawn, shutdown, or duplicate/overlap reporting.

Audit fields: `requested_role`, `objective`, `checked_scope`, `observed_state` (`active`, `recent`, `stale`, `missing`, `unavailable`, or `not found in checked scope`), `role_owner`, `objective_alignment`, `decision`, `reason`.

Decision rules:
- active/recent + same standing role + next phase assignment -> steer existing role
- active/recent + same role + same objective -> reuse or steer
- active/recent + same role + different objective -> keep distinct only with explicit lane boundary
- stale or missing -> verify before claiming active duplicate or safe absence
- unavailable -> stop for state, input, or authorization before respawn as needed
- not found in checked scope -> report scoped non-finding; spawn only when the checked scope is sufficient
- phase change alone -> reuse or steer standing role, not phase-suffixed spawn
- one broad independent lane with no matching worker -> focused standalone subagent preferred
- three or more distinct lanes with shared dependencies -> Agent Team / teammates only when justified

### 11) Native and selected-goal execution
Worker routing is normal execution behavior: identify worker-fit slices proactively, keep the worker set minimal, prefer standalone lanes before shared-team coordination, reuse aligned standing roles, and do not over-delegate simple work. If the goal owner requests a bounded authoring/helper lane, route it without turning its output into a new objective surface.

For selected non-trivial plan/goal work that is execution-ready and taskable, `Subagent-Driven` is the internal first preference: normally one standalone lane per bounded task. Choose rather than ask the user between `Subagent-Driven` and `Inline Execution`; if context is insufficient, ask one substantive question about work, scope, access, artifact, or approval.

Use `Inline Execution` when the slice is smaller, safer, tightly sequential, low-output, high-overlap, interactive, worker-unavailable, or explicitly user-directed, and keep the reason visible. Preserve these exact routing labels only when workflow behavior or artifact wording requires them. Task shaping defers to `phase-todo-artifact.md`; leader verification remains mandatory before completion, sync, fixed, or release-ready wording.

### 12) Team restriction boundary

A user ban on `teammate`, `Agent Team`, or team workflow restricts coordinated team/teammate mechanisms unless the user explicitly broadens the ban.

It does **not** automatically ban standalone subagents, `Agent(...)`, `Explore(...)`, read-only reviewer/auditor agents, or comparable worker tools.

If Agent Team is disallowed but broad worker-fit work remains, use a standalone subagent when suitable. If all agent/subagent mechanisms are explicitly disallowed, handle directly and state the constraint when broad work would otherwise be delegated.

### 13) Subagent lane contract

Use a standalone subagent for bounded independent work that benefits from separate context but not full team coordination.

Default research/audit/review lanes to read-only unless edit ownership is explicit. Edit-capable governed-document repair lanes are allowed only under the bounded repair contract above.

A lane brief should minimally say:
- lane template or preset being used (`scout`, `compare`, `audit + repair`, `verification`, or another clearly named bounded role)
- objective and why this lane exists
- checked scope and excluded scope
- allowed actions and stop gates
- required evidence/output shape, including exact anchors the leader should verify
- what decision or next action the handoff should unblock

For research lanes, include the decision surface, suggested topic boundaries, source-trust expectations, and permission to refine query/topic strategy inside scope. Scope the lane to return analyzed findings, not raw dumps. Use multiple subagents only for meaningfully independent lanes.

A goal-support lane also names the goal/candidate it serves and returns subordinate support only, never competing route authority or completion proof.

### 14) Agent Team escalation contract

Use official Agent Team / teammate workflow only when coordination is needed, not merely context filtering.

Teams require shared task ownership, dependencies, messaging, implementation plus review/test/docs sync, or durable handoff that standalone subagents cannot cover cleanly.

Every teammate needs distinct role, objective, checked scope, edit permission, expected output, and stop gates. Edit-capable teammates must own non-overlapping artifacts/classes. Plugin/shared-board/custom tmux bridge mechanics remain outside this Main RULES owner unless separately selected by the user or an active project rule.

### 15) Worker handoff quality and stronger contract

Worker output must be filtered and analyzed; size the handoff to task type, evidence complexity, and decision value.

Every handoff should let the leader answer five questions quickly: what lane ran, what it checked, what it found, what remains uncertain, and what the leader should verify or decide next.

Required handoff content:
- baseline: lane/preset name, outcome, checked scope, relevant evidence, evidence strength, conflicts/uncertainty, excluded scope, and recommended next verification when material
- research: topic/query families checked, source-trust notes, source conflicts, recommendation implications, and what the leader should verify directly
- edit-capable repair: touched artifacts, exact anchors, preservation notes, checks run, unresolved risks, and leader verification needs

Handoff quality rules:
- lead with the decision-ready result, not the raw journey
- preserve exact paths, symbols, command output, URLs, or line references only when they materially support the result
- include the stop reason when the lane ended because scope, approval, or evidence limits were reached
- name the next best action instead of forcing the leader to reconstruct the lane's intent from raw notes
- if a handoff is causing repeated clarification turns, treat that as routing debt and tighten the brief or change topology

Delegation efficiency and success signals are audit heuristics, not hidden-telemetry requirements: prefer early delegation before raw evidence piles up, anchor-first handoffs instead of dumps, reuse before respawn, one-pass unblocks when possible, and verification closure through selected anchors rather than full rereads.

### 15.1) Observed example versus selected target separation in handoffs
When a worker or leader uses another project, subsystem, or prior chain as evidence for documentation normalization, the handoff must distinguish:
- what was observed in the checked example
- what doctrine was extracted from that observation
- what target form is selected for the current RULES chain
- whether exact equivalence between the observed example and the selected target was verified

Required guidance:
- do not say `project X uses this pattern` when the checked evidence only supports `this pattern is the selected target inspired by project X`
- if the example is mixed, transitional, bootstrap-shaped, or only partially checked, carry that limit forward into the handoff
- if the current recommendation is stricter than the checked example, state that the stricter form is a selected target, not a discovered fact about the example
- leader verification must confirm that example-shaped wording does not overclaim checked project truth before sync, no-drift, closeout, or release-ready wording

### 16) Parallel edit containment

Parallel implementation is allowed only with clear ownership separation by file, module, test target, documentation surface, or artifact class.

Do not assign overlapping writes unless one lane is explicitly review-only. Use read-only workers for investigation/review when edit overlap risk is high. Edit-capable lanes report touched artifacts, checks run, unresolved risks, and handoff notes.

### 17) Main-controller verification

The leader remains responsible for synthesis, direction, verification, and completion claims. Worker findings and helper/route/test outputs are context, not proof. Resolve conflicts from checked evidence, inspect worker edits, and verify material anchors before factual, completion, sync, fixed, or goal-completion wording.

### 18) Custom agent selection after routing

Routing decides worker scale; custom-agent selection chooses the best specialist afterward.
- treat visible user custom agents in `~/.claude/agents/` as the primary specialist pool when a task clearly matches one
- prefer capability/domain fit over tool-name matching
- do not delegate merely because an agent exists; worker routing must already have selected delegation or specialist handling
- do not use custom-agent availability alone as proof that delegation is appropriate
- do not use this section to escalate standalone subagent work into Agent Team workflow
- reuse an active/recent matching worker before spawning another unless the new lane is explicitly partitioned
- discovery still depends on visible/available agents, not imagined runtime availability

Selection order after routing selects delegation/specialist handling:
1. identify the required worker capability and domain scope
2. check for a clear best-fit user custom agent
3. otherwise consider project, built-in, or plugin specialists that fit the capability
4. if no specialist adds meaningful value, keep the non-specialist worker path already selected or return to direct handling

Prefer a custom user agent only when worker routing has already selected a delegated/specialist path and the fit, value, and scope are materially stronger than the generic path.

### 19) Document-context routing boundary
Document owners decide authority, density, sharding/rollover, preservation, and repair safety first; this rule then chooses direct, audit, bounded repair, or Team topology. Analysis-only scope, owner ambiguity, meaning/history risk, or destructive risk blocks delegated document edits.

---

## Trigger Model

| Routing trigger | Required behavior |
|---|---|
| AI/RULES behavior question with project evidence | stay behavior-first unless project inspection is explicitly needed |
| one bounded evidence axis | use one scout/filter lane |
| independent evidence branches | use compare/fan-out lanes |
| findings must precede a safe fix | use audit then bounded repair |
| broad research | split by decision-relevant topics and require source-trust/conflict reporting |
| shared ownership or dependent implementation/review/test work | consider Agent Team only when standalone lanes are insufficient |
| phase changes but responsibility remains | reuse or steer the standing-role worker |
| reuse/spawn/duplicate report | audit checked coordination state before deciding |
| high edit overlap or interactive work | keep edits direct and use read-only workers when useful |
| teammate/Agent Team ban | standalone subagents remain allowed unless agents are broadly banned |
| matching specialist exists after routing | prefer the best-fit visible specialist |
| weak handoff or clarification churn | tighten the brief or change topology |

---

## Anti-Patterns

Avoid routing by tool name or agent availability; absorbing worker-fit raw evidence before dispatch; escalating beyond the dependency shape; treating Team bans as standalone-agent bans; overlapping edits or duplicate roles without partition; inventing mechanism capability; delegating ambiguous/destructive governed repair; accepting raw handoffs as proof; or tolerating weak handoffs instead of fixing the brief/topology.

---

## Integration

Related owners:
- [safe-io.md](safe-io.md) — burst detection and bounded I/O
- [document-governance.md](document-governance.md) / [document-integrity.md](document-integrity.md) — document authority and repair safety before routing
- [external-verification-and-source-trust.md](external-verification-and-source-trust.md) — research source trust and conflicts
- [evidence-discipline.md](evidence-discipline.md) — worker findings remain evidence-bounded
- [execution-and-goal-frame.md](execution-and-goal-frame.md) / [phase-todo-artifact.md](phase-todo-artifact.md) — continuation and live task shaping
