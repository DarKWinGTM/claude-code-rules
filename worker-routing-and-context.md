# Worker Routing and Context Control

> **Current Version:** 1.10 (merged M11)
> **Design:** [design/worker-routing-and-context.design.md](design/worker-routing-and-context.design.md) v1.10
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/worker-routing-and-context.changelog.md](changelog/worker-routing-and-context.changelog.md)

---

## Rule Statement

**Core Principle: Use the smallest effective standalone worker lane first for broad, research-heavy, roadmap-analysis-heavy, high-context, high-output, or naturally parallel work; proactively delegate predictable worker-fit slices before the leader session burns avoidable context; manage context load as a full lifecycle covering reading, writing, worker routing, and repair; and after worker routing establishes delegation or specialist need, prefer the best-fit visible custom or specialist agent before generic fallback.**

Target outcomes:
- broad raw evidence is filtered before it burdens the leader session
- worker-fit tasks are delegated early enough that the leader does not spend context on avoidable raw intake
- active documents stay density-safe and cheap to read, edit, diff, and verify later
- active changelog parents stay compact by routing bulky same-chain version detail into indexed shards when needed
- delegation stays proportional through reusable lane topologies, stronger handoffs, and visible efficiency review signals

---

## Core Contract

### 1) Intent and scope boundary

Classify the user's intent before treating technical material as project work:
- AI/RULES behavior or workflow-compliance analysis
- project fact-checking or codebase inspection
- implementation or refactor execution
- review, audit, or verification
- explanation only

Use the smallest useful intent taxonomy below when the distinction changes routing, clarification, or scope handling:

| Intent class | Meaning | Default routing implication |
|---|---|---|
| behavior/governance | the user is asking how the assistant, RULES, or workflow should behave | stay behavior-first; project exploration needs explicit request or bounded proof need |
| fact lookup | the user wants current checked project facts | inspect the minimal authority surface needed; avoid broad implementation drift |
| diagnosis / root-cause analysis | the user wants to understand why something is happening | diagnosis-first; do not jump to edits before symptom, evidence, and next-best check are framed |
| implementation | the user wants a source/config change | move to execution when scope/path are clear |
| review / audit | the user wants evaluation, risk finding, or consistency checking | preserve checked-scope evidence and worker-filter broad reads when needed |
| plan / design | the user wants strategy, structure, or decision framing | stay discussion-first until the chosen path is clear |
| coordination / workflow | the user wants handoff, routing, lane choice, or process behavior | classify mechanism and worker path before inspecting project surfaces |

Pasted logs, snippets, paths, or another session's worker notes are evidence for the current question, not automatic authorization to inspect the referenced project. If the user asks about assistant behavior or RULES behavior, stay in that scope unless project exploration is explicitly requested or a bounded verification need is stated.

Use direct leader handling for trivial, one-step, tightly sequential, low-output, exact interactive-control work, high edit-overlap work, unavailable worker tooling, or explicit user direction. Otherwise run the worker gate before broad codebase searches, large file reads, symbol/path tracing, high-output tests/logs/builds, external docs/provider research, roadmap/phase-matrix analysis, design-improvement research, source comparison, multi-surface governance sweeps, design/security/migration reviews, or safely partitionable implementation.

พูดง่าย ๆ: ถ้างานกว้างจน main session ไม่จำเป็นต้องอ่าน raw ทุกอย่างเอง ให้ใช้ subagent หรือ worker lane ที่เล็กที่สุดไปกรองก่อน แต่ถ้าผู้ใช้ถามเรื่องพฤติกรรมของ AI ก็อย่าไหลไปสำรวจ project เพียงเพราะมี path/log แปะมา.

### 2) Intent-first worker gate

Behavior/RULES questions are answered from the behavior/rule layer first. Project exploration begins only when the user asks for project facts, implementation, or verification, or when checked evidence is required and scope is stated. Another session's pasted output may suggest a worker use case, but it does not make project inspection the active task.

When one user turn mixes several intents, resolve the dominant execution question first: diagnosis-heavy asks stay diagnosis-first, scope corrections are repaired before project exploration, and one narrow working interpretation is preferred over broad intake questions when it is enough to continue safely.

### 3) Worker-scale gate, proactive delegation matrix, and aggregate read-burst control

Before broad main-session absorption, classify the smallest worker structure that preserves correctness and context efficiency. Several bounded reads can still overload context when combined, especially if lines are dense.

Before broad multi-surface reading, identify the question being answered, the authority surface most likely to answer it, whether exact raw content is needed or a filtered handoff is enough, and whether additional waiting would only spend leader context rather than reduce uncertainty.

Worker-first aggregate-read gate is required before leader raw absorption when a broad trigger applies, such as 3+ governance surfaces for one claim, cross-surface sync/closeout/release-readiness review, repo-wide search plus multi-file reads, broad code+docs evidence, dense active-doc bursts, noisy command output, broad external research, roadmap/design-improvement analysis, source comparison, or safely partitionable implementation.

When the gate fires, treat the work as worker-fit by default, dispatch the read-only worker before broad raw intake unless a narrow direct-handling exception is stated, and require the handoff to return filtered findings, conflicts, exact anchors, evidence strength, and leader verification needs.

Proactive delegation trigger matrix:

| Signal | Typical shape | Default response |
|---|---|---|
| predictable single-question broad scan | one question needs search + several follow-up reads | dispatch one scout/filter lane before leader raw intake |
| independent evidence branches | compare two or more sources, filesets, or risk lanes | split into separate read-only lanes and synthesize later |
| audit-then-repair shape | findings must be identified before a bounded fix is safe | use an audit lane first, then a bounded repair lane if needed |
| high-output diagnosis | failing tests/logs/builds plus source inspection | delegate log/output triage before leader deep reads |
| leader budget would be spent on repetition | rereads, offset hopping, or repeated raw clarification would dominate | delegate early instead of waiting for more raw intake |

Skipping the gate blocks broad sync, no-drift, closeout, or release-ready claims unless a narrow direct-handling exception is stated.

Density warning signals include:
- many active governance files read in one burst
- long markdown lines that carry several concepts
- repeated reads after compact that refill context quickly
- bounded line ranges with unusually high character count

General routing guidance:
- when the work is broad research or multidimensional roadmap analysis, first map the objective into topic/phase/risk lanes before deciding whether one or multiple subagents fit
- prefer one standalone subagent-style lane for a bounded independent broad/read/review/filter/research task before considering Agent Team workflow
- if a worker lane is selected, dispatch/assign it before the leader absorbs raw broad output
- direct leader handling remains valid for narrow known files, exact edit or verification ranges, tightly sequential interactive-control work, unavailable worker tooling, or explicit user direction
- if the leader handles broad worker-fit work directly, state the narrow reason before or alongside the direct action
- saying "an agent could help" is not enough; select a path and act when suitable
- worker routing never removes leader verification responsibility

### 4) Leader-context protection and budget

The leader session should stay the controller, verifier, and final decision maker. It should not absorb broad raw evidence by default.
- use subagents or worker lanes as raw evidence absorbers and filters for broad docs, logs, searches, audits, or multi-surface reviews
- brief workers with the exact question, checked scope, expected anchors, conflicts, risks, and leader verification needs
- make the leader verify selected anchors before final claims instead of reading every raw source
- do not satisfy the worker gate by only saying a worker could help; dispatch one when the broad-read shape requires it

Leader context budget is a planning budget, not a promise about exact token counts.
- spend leader context on control decisions, synthesis, and anchor verification before spending it on raw bulk evidence
- default target: one compact handoff plus selected anchor checks per lane, not lane-sized raw dumps
- if the leader would need to personally read several medium bodies, several noisy reruns, or more than one unresolved raw evidence branch, delegation should happen before more raw intake
- when the budget is already being spent on repetitive searching, rereading, or clarifying weak handoffs, tighten the brief or switch topology rather than absorbing more raw content

### 5) Capability-based routing criteria

Route by capability and workload shape, not rigid tool name. Evaluate user intent/scope, context isolation and output noise, broad evidence-filtering need, lane independence, specialist value, parallel value, coordination/dependencies, risk/security/verification burden, edit overlap, whether the leader needs raw evidence or analyzed result, worker availability, and user constraints. Tool names such as `Agent`, `Explore`, repository search, web search, or future workers are implementation details.

### 6) Work-shape topology selection

| Work shape | Topology | Preferred path |
|---|---|---|
| trivial, exact, one-step, low-output, tightly sequential | direct | leader directly |
| one broad question with one main evidence axis | scout | one focused standalone subagent / worker lane |
| two or more independent evidence branches with no shared writes | fan-out / fan-in | multiple focused standalone subagents with leader synthesis |
| findings must be filtered before a bounded fix is safe | audit + repair pair | read-only audit lane followed by one bounded edit-capable repair lane |
| implementation plus dependent review/test/docs sync or shared ownership | coordinated swarm | official Agent Team / teammates as exceptional escalation |

Lane templates and swarm presets:
- `Scout preset`: one lane answers one broad question and returns a decision-ready digest plus anchors.
- `Compare preset`: two or more read-only lanes compare independent sources or options with the same rubric.
- `Audit + Repair preset`: one audit lane narrows exact anchors, then one bounded repair lane edits only that scope.
- `Verification preset`: one lane checks tests/logs/runtime evidence for a defined gate while implementation ownership stays elsewhere.
- `Coordinated swarm preset`: use a small shared-dependency role set only when standalone lanes are insufficient.

Presets are planning shorthands, not proof that a Team Agent workflow is required; choose the smallest topology that matches the dependency shape.

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

### 11) Native execution behavior

Worker routing is normal execution behavior, not a special mode.
- proactively look for worker-fit slices
- keep the worker set minimal
- prefer subagent-first handling for broad lanes without shared-team coordination
- goal-owned internal helper use may route bounded analysis, verification, testing, or compact plan-draft slices through standalone subagents when that lowers context cost without creating a new public surface
- reuse/steer aligned standing-role workers before duplicate-looking spawns
- do not over-delegate simple work

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

For goal-owned internal helper use, the lane brief should also name the selected goal the helper serves, whether the lane is analysis, verification, testing, or bounded plan drafting, and that returned material remains subordinate to the selected goal rather than becoming route authority by itself.

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

The leader remains responsible for synthesis, direction, verification, and completion claims. Worker findings are context, not automatic proof. Resolve conflicts from checked evidence, verify material claims before user-facing factual/completion/sync/fixed wording, inspect changed artifacts after worker edits, and do not treat helper-produced plan draft, test triage, or verification notes as goal-completion proof until the leader verifies the relevant anchors/checks.

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

Worker-routing owns only the routing decision for document-heavy work: direct handling, read-only audit lane, bounded edit-capable repair lane, or Team escalation.

Document-density, God-line/God-file, active-entrypoint, parent/shard/changelog, compact/thrash, and no-drift repair doctrine lives in `document-integrity.md` and `document-governance.md`.

When those document signals appear, apply the document-owner rules first; return here only to decide whether a worker lane is needed. Do not delegate document edits when analysis-only scope, owner ambiguity, meaning risk, history preservation, or destructive risk makes the repair unsafe.

---

---

## Decision Flow

```text
Work starts or next slice is discovered
  ↓
Classify intent
  → AI/RULES behavior: stay behavior/governance first
  → project fact/implementation/review: continue
  → unclear and outcome-changing: clarify or state working scope
  ↓
Broad, noisy, context-heavy, multi-surface, or parallelizable?
  → NO: leader handles directly
  → YES: continue
  ↓
Would raw leader intake mainly spend context budget rather than reduce uncertainty?
  → YES: choose the smallest useful topology and delegate first
  → NO: continue
  ↓
Is it broad research/source comparison/roadmap-analysis/design-improvement evidence gathering?
  → YES: map research or roadmap lanes, then use one or more focused standalone subagents when lanes are independent
  → NO: continue
  ↓
One bounded independent lane can filter, research, review, or own a governed-document repair scope?
  → YES: use one focused standalone subagent or bounded edit-capable repair lane
  → NO: continue
  ↓
Independent read-only lanes can run without shared ownership?
  → YES: use multiple focused standalone subagents
  → NO: continue
  ↓
Needs shared ownership, dependencies, messaging, or implementation/review/test/docs sync?
  → YES: Agent Team / teammates only if allowed and justified
  → NO: leader handles directly with narrow reason
  ↓
After worker scale decided, select best-fit visible specialist when capability fits
  ↓
Document-heavy repair or active-doc pressure appears?
  → YES: apply `document-integrity.md` / `document-governance.md` first, then decide whether direct handling, audit lane, or bounded repair lane is appropriate
  → NO: continue
```

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| user asks about AI/RULES behavior while providing logs/snippets | classify as behavior/governance first; do not auto-explore project |
| compact or corrective prompt where visible intent repair would reduce drift | state a short working scope before broadening the search or lane count |
| symptom-heavy ask with mixed logs/snippets and possible implementation implications | default to diagnosis-first; do not auto-jump into edits |
| predictable single-question broad scan | use the `Scout preset` before the leader absorbs search results plus follow-up reads |
| leader context budget would be spent on rereads, offset hopping, or repeated raw clarification | delegate early or tighten the brief/topology before more raw intake |
| broad search/read, aggregate governance/code read burst, or repository exploration | dispatch standalone worker or state narrow direct-handling reason before broad absorption |
| broad roadmap/phase-matrix analysis | use a focused read-only planning/review lane when multiple design, TODO, phase, risk, or dependency surfaces need synthesis |
| coordination design or cross-session behavior proposal | classify the actual mechanism first, then keep claims within checked capability |
| high-output test/log/build evidence | prefer worker filtering before leader reads raw noisy output |
| multi-surface governance audit | use a focused audit worker or multiple standalone workers when scope is broad |
| findings must be narrowed before a safe bounded fix | use the `Audit + Repair preset` instead of mixing investigation and edits in one raw lane |
| phase changes but the worker responsibility remains the same | reuse or steer the standing-role worker; put phase context in the assignment |
| reuse, spawn, respawn, shutdown, or duplicate/overlap report | audit checked coordination evidence and report scoped state before deciding |
| simultaneous same-role lanes | name lanes by responsibility, surface, or output rather than phase ID alone |
| context-heavy governed-document repair | apply `document-integrity.md` / `document-governance.md` first, then use a bounded edit-capable repair lane only with explicit scope, edit ownership, and preservation constraints |
| external docs/API/provider research | use worker lane when source volume or comparison cost is high, with source-trust expectations in the assignment |
| broad design-improvement research | map independent topic lanes first, then dispatch one or more focused subagents before leader raw websearch absorption |
| independent parallel research lanes | use multiple subagents when coordination need stays low and topics are meaningfully separable |
| implementation plus review/test/docs sync with dependencies | consider Agent Team only when shared coordination is truly needed |
| teammate/Agent Team is banned | use standalone subagent if agents are not broadly banned |
| trivial local task | handle directly; do not force delegation |
| high edit overlap | avoid parallel edit lanes; consider read-only investigation instead |
| visible custom agent matches selected worker capability | prefer best-fit specialist before generic fallback |
| repeated weak handoffs or clarification churn | treat it as routing debt; improve the brief or change topology rather than adding more raw context |

---

## Anti-Patterns

Avoid:
- treating pasted project paths/logs as permission to inspect code
- assuming a short or corrective user turn is implementation authorization when it was really a scope repair or diagnosis request
- waiting until after the leader has already absorbed most raw evidence to decide that delegation would have helped
- leader absorbing broad raw search/read/log/test/roadmap evidence by default
- skipping the worker-first aggregate-read gate before broad governance/code scans
- leader running broad design-improvement websearch or phase-roadmap synthesis directly when research/planning lanes would filter it better
- routing by tool name alone
- assuming an unverified hook, transport, recall, board, team, plugin, or MCP mechanism can deliver coordination behavior
- saying agents could help without dispatching when worker-fit is present
- treating teammate/Agent Team bans as standalone-subagent bans
- escalating to Agent Team when one subagent would cover the work
- choosing a bigger topology than the dependency shape actually needs
- fixed handoff caps, raw worker dumps, duplicate same-role worker spawn, or overlapping parallel edits
- naming workers by phase ID alone when the standing role did not change
- reporting active duplicate overlap, safe absence, stale-worker cleanup, shutdown, or respawn without checked coordination evidence
- importing shared-board grammar, session-short-id prefixes, creator-owner hooks, hidden registries, package tmux bridge behavior, or exact teammate display modes into Main RULES required behavior
- assigning edit-capable governed-document repair without bounded ownership and preservation constraints
- treating worker summaries as proof or importing plugin/shared-board grammar into Main RULES
- ignoring a clear custom specialist after routing already selected specialist handling
- delegating to a custom agent without strong capability fit
- using custom-agent availability as the routing decision
- using specialist-selection rules to escalate subagent-fit work into Agent Team workflow
- spawning a second same-role worker without a distinct partition
- treating built-ins/plugins as automatically superior to user custom agents when a visible user specialist fits better
- pretending an undiscovered agent is available
- over-delegating trivial work
- tolerating repeated weak handoffs instead of fixing the brief or switching topology
- reading several "bounded" files without considering aggregate output size
- delegating ambiguous, history-heavy, authority-shifting, broad, destructive, or analysis-only governed-document repair to worker edits before the document-owner rules say the repair is safe

Better behavior: classify intent and worker scale first, delegate predictable worker-fit slices before the leader burns context, dispatch the smallest fitting lane or state the narrow direct-handling reason, select the best-fit visible specialist for the chosen capability, keep Agent Team escalation for true shared coordination, ask the question first, route broad raw evidence through workers, and require leader verification before completion wording.

---

## Integration

Related rules:
- [safe-io.md](safe-io.md) - bounded file reading plus sharded design and changelog parent-map read order
- [safe-io.md](safe-io.md) - bounded command output handling
- [document-integrity.md](document-integrity.md) - active-entrypoint rollover, density repair, governed-document repair safety, and no-drift verification
- [document-governance.md](document-governance.md) - compact design/changelog parent authority, shard decisions, and active runtime install scope
- [evidence-discipline.md](evidence-discipline.md) - keeps partial reads and worker findings evidence-bounded
- [external-verification-and-source-trust.md](external-verification-and-source-trust.md) - source trust, corroboration, and external-evidence conflict handling for research lanes
- [authority-and-scope.md](authority-and-scope.md) - user override for specialist choice
- [action-safety.md](action-safety.md) - execution confirmation separate from delegation choice
- execution-continuity must not bypass the worker gate; TODO/phase rules shape live tracking and phase context; evidence, accurate-communication, and zero-hallucination chains keep worker and leader claims calibrated; communication/anti-sycophancy rules keep specialist choice calm and evidence-based
