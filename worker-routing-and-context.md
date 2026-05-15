# Worker Routing and Context Control

> **Current Version:** 1.0 (merged M11)
> **Design:** [design/worker-routing-and-context.design.md](design/worker-routing-and-context.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/worker-routing-and-context.changelog.md](changelog/worker-routing-and-context.changelog.md)

---

## Rule Statement

**Core Principle: Use the smallest effective standalone worker lane first for broad, research-heavy, roadmap-analysis-heavy, high-context, high-output, or naturally parallel work so the leader session stays the controller and verifier; manage context load as a full lifecycle covering reading, writing, worker routing, and repair; and after worker routing establishes delegation or specialist need, prefer the best-fit visible custom or specialist agent before generic fallback.**

Target outcomes:
- broad raw evidence is filtered before it burdens the leader session
- active documents stay density-safe and cheap to read, edit, diff, and verify later
- active changelog parents stay compact by routing bulky same-chain version detail into indexed shards when needed
- delegation happens only when worker routing selects it, with the best-fit visible specialist chosen afterward

---

## Core Contract

### 1) Intent and scope boundary

Classify the user's intent before treating technical material as project work:
- AI/RULES behavior or workflow-compliance analysis
- project fact-checking or codebase inspection
- implementation or refactor execution
- review, audit, or verification
- explanation only

Pasted logs, snippets, paths, or another session's worker notes are evidence for the current question, not automatic authorization to inspect the referenced project. If the user asks about assistant behavior or RULES behavior, stay in that scope unless project exploration is explicitly requested or a bounded verification need is stated.

Use direct leader handling for trivial, one-step, tightly sequential, low-output, exact interactive-control work, high edit-overlap work, unavailable worker tooling, or explicit user direction. Otherwise run the worker gate before broad codebase searches, large file reads, symbol/path tracing, high-output tests/logs/builds, external docs/provider research, roadmap/phase-matrix analysis, design-improvement research, source comparison, multi-surface governance sweeps, design/security/migration reviews, or safely partitionable implementation.

พูดง่าย ๆ: ถ้างานกว้างจน main session ไม่จำเป็นต้องอ่าน raw ทุกอย่างเอง ให้ใช้ subagent หรือ worker lane ที่เล็กที่สุดไปกรองก่อน แต่ถ้าผู้ใช้ถามเรื่องพฤติกรรมของ AI ก็อย่าไหลไปสำรวจ project เพียงเพราะมี path/log แปะมา.

### 2) Intent-first worker gate

Behavior/RULES questions are answered from the behavior/rule layer first. Project exploration begins only when the user asks for project facts, implementation, or verification, or when checked evidence is required and scope is stated. Another session's pasted output may show a possible worker use case, but it does not make project inspection the active task. If intent is behavior analysis plus broad evidence review, use a worker lane to analyze the evidence rather than letting the leader absorb it directly.

### 3) Worker-scale gate and aggregate read-burst control

Before broad main-session absorption, classify the smallest worker structure that preserves correctness and context efficiency. Several bounded reads can still overload context when combined, especially if lines are dense.

Before reading multiple governance or code surfaces, identify:
- the question being answered
- the authority surface most likely to answer it
- whether exact raw content is needed or a filtered worker handoff is enough
- cumulative output risk across all planned reads, not only per-file line count

Worker-first aggregate-read gate is required before leader raw absorption when any trigger applies:
- 3+ governance surfaces are needed for one claim, sync, release, or no-drift review
- cross-surface release sync, closeout, or release-ready validation is being assembled
- repo-wide search is followed by multi-file reads
- broad code+docs evidence is needed together
- dense/history-bearing active docs would be read as a set
- noisy command output, multi-surface audit, external research, roadmap/phase-matrix analysis, design-improvement research, source comparison, or safely partitionable implementation is planned

Gate behavior:
- treat broad governance/code scans as worker-fit by default when any aggregate trigger applies
- dispatch a standalone read-only worker before the leader absorbs raw aggregate-read evidence unless a narrow direct-handling exception is stated before the broad read starts
- require worker output to return filtered findings, conflicts, exact anchors, evidence strength, and leader verification needs rather than raw dumps

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

### 4) Leader-context protection

The leader session should stay the controller, verifier, and final decision maker. It should not absorb broad raw evidence by default.
- use subagents or worker lanes as raw evidence absorbers and filters for broad docs, logs, searches, audits, or multi-surface reviews
- brief workers with the exact question, checked scope, expected anchors, conflicts, risks, and leader verification needs
- make the leader verify selected anchors before final claims instead of reading every raw source
- do not satisfy the worker gate by only saying a worker could help; dispatch one when the broad-read shape requires it

### 5) Capability-based routing criteria

Route by capability and workload shape, not rigid tool name. Evaluate user intent/scope, context isolation and output noise, broad evidence-filtering need, lane independence, specialist value, parallel value, coordination/dependencies, risk/security/verification burden, edit overlap, whether the leader needs raw evidence or analyzed result, worker availability, and user constraints. Tool names such as `Agent`, `Explore`, repository search, web search, or future workers are implementation details.

### 6) Worker path model

| Work shape | Preferred path |
|---|---|
| trivial, exact, one-step, low-output, tightly sequential | leader directly |
| one bounded research/review/source scan/log-test filter/docs lookup/evidence proof lane | one focused standalone subagent / worker lane |
| one bounded governed-document repair lane with explicit edit ownership | one edit-capable `general-purpose`-style standalone worker lane |
| two or more independent read-only/filter/comparison lanes | multiple focused standalone subagents |
| shared ownership, dependencies, teammate messaging, implementation plus review/test/docs sync, or durable handoff | official Agent Team / teammates as exceptional escalation |

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
- reuse/steer aligned standing-role workers before duplicate-looking spawns
- do not over-delegate simple work

### 12) Team restriction boundary

A user ban on `teammate`, `Agent Team`, or team workflow restricts coordinated team/teammate mechanisms unless the user explicitly broadens the ban.

It does **not** automatically ban standalone subagents, `Agent(...)`, `Explore(...)`, read-only reviewer/auditor agents, or comparable worker tools.

If Agent Team is disallowed but broad worker-fit work remains, use a standalone subagent when suitable. If all agent/subagent mechanisms are explicitly disallowed, handle directly and state the constraint when broad work would otherwise be delegated.

### 13) Subagent lane contract

Use a standalone subagent for bounded independent work that benefits from separate context but not full team coordination.

Default research/audit/review lanes to read-only unless edit ownership is explicit. Edit-capable governed-document repair lanes are allowed only under the bounded repair contract above.

Brief the lane with objective, checked scope, allowed actions, expected output, and stop gates. For research lanes, include the decision surface, suggested topic boundaries, source-trust expectations, and permission to refine query/topic strategy inside scope. Scope the lane to return analyzed findings, not raw dumps. Use multiple subagents only for meaningfully independent lanes.

### 14) Agent Team escalation contract

Use official Agent Team / teammate workflow only when coordination is needed, not merely context filtering.

Teams require shared task ownership, dependencies, messaging, implementation plus review/test/docs sync, or durable handoff that standalone subagents cannot cover cleanly.

Every teammate needs distinct role, objective, checked scope, edit permission, expected output, and stop gates. Edit-capable teammates must own non-overlapping artifacts/classes. Plugin/shared-board/custom tmux bridge mechanics remain outside this Main RULES owner unless separately selected by the user or an active project rule.

### 15) Worker handoff quality

Worker output must be filtered and analyzed; size the handoff to task type, evidence complexity, and decision value.

Required handoff content:
- baseline: outcome, checked scope, relevant evidence, evidence strength, conflicts/uncertainty, and recommended next verification when material
- research: topic/query families checked, source-trust notes, source conflicts, recommendation implications, and what the leader should verify directly
- edit-capable repair: touched artifacts, exact anchors, preservation notes, checks run, unresolved risks, and leader verification needs

Omit noise unless it explains a finding, conflict, or risk. Preserve exact paths, symbols, command output, URLs, or line references only when materially supporting the result.

### 16) Parallel edit containment

Parallel implementation is allowed only with clear ownership separation by file, module, test target, documentation surface, or artifact class.

Do not assign overlapping writes unless one lane is explicitly review-only. Use read-only workers for investigation/review when edit overlap risk is high. Edit-capable lanes report touched artifacts, checks run, unresolved risks, and handoff notes.

### 17) Main-controller verification

The leader remains responsible for synthesis, direction, verification, and completion claims. Worker findings are context, not automatic proof. Resolve conflicts from checked evidence, verify material claims before user-facing factual/completion/sync/fixed wording, and inspect changed artifacts after worker edits.

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

### 19) Context is a lifecycle, not a post-compact rule

Do not treat context safety as only "read less after compact."
- prevent future context cost while writing and syncing docs
- route broad raw evidence through workers when the leader does not need the raw body
- repair dense active documents when compact/thrash exposes structural debt
- avoid blunt post-compact bans when workflow or document structure is the real fix

### 20) Document-density and God-line prevention

Write active docs so future sessions can read and edit them cheaply.
- keep one line or bullet focused on one concept or one tight fact group
- split current state, history, verification, risks, exclusions, and next work when they start to mix
- route long version detail to active parent changelog maps plus chain-scoped version detail shards when needed
- keep `changelog/done/` for legacy/archive/completed-history/fallback history, not ordinary same-chain detail sharding
- use semantic bullets, small tables, and short paragraphs instead of one-line history dumps
- treat very long active lines as repair triggers, not disposal proof

### 21) Opportunistic touched-doc God-line repair

When an active document is already being edited and the touched area contains a God-line candidate, do not only warn about the density problem.

Repair immediately when all conditions hold:
- the candidate is in a touched active document or touched section
- the semantic split is clear from the local context
- the repair is local, meaning-preserving, and low-risk
- the repair separates responsibilities such as current state, history, verification, risks, exclusions, and next work
- the repair does not require broad historical reconstruction or repo-wide formatting

Flag or plan instead of editing immediately when any condition holds:
- the line is history-heavy and its exact meaning could be changed by splitting
- the line mixes old release history with current state in a way that needs owner review
- the repair would touch broad unrelated sections or many files
- the correct destination for moved content is ambiguous
- the user explicitly limited the task to analysis only

Required behavior:
- if safe immediate repair applies, split or restructure in the same edit before claiming the touched doc is clean
- if immediate repair is unsafe, record it as density debt, follow-up work, or a phase/patch item when material
- do not append more content to a known God-line candidate unless no safer structure exists and the limit is stated

### 22) Append-vs-restructure gate

Before appending to an existing active line or bullet, check whether the append would make future diffs and reads larger than the logical change.

Required questions:
1. Is the new content current state, history, verification, risk, or next work?
2. Does the target line already mix more than one responsibility?
3. Would the edit replace one huge line for a small logical change?
4. Should the new content become a new bullet, a subsection, a changelog entry, or a history/done shard reference?
5. Should the existing line be split before adding the new detail?

If the target line is already a God-line candidate, do not append silently.
- restructure first or in the same change when the split is clear and low-risk
- flag or plan the repair when the split is broad or meaning-risky

### 23) Active entrypoints are maps, not storage dumps

`TODO.md`, `phase/SUMMARY.md`, README current-state sections, compact design indexes, and active parent changelog indexes should help a fresh session find current work quickly.
- keep them focused on current state, selected roadmap, active tasks, gates, shard maps, and pointers
- move bulky same-chain detail to changelog version shards and daily/completed movement to referenced history/done surfaces
- keep enough context to navigate without rereading full history

### 24) Compact/thrash is a repair signal

Autocompact thrash or immediate post-compact refill means the workflow or document shape needs review.
- identify whether the cause is aggregate read burst, dense files, missed worker routing, God lines, oversized entrypoints, or raw output flooding
- repair the source pattern when practical instead of inventing rigid post-compact bans

### 25) Density-aware verification

After non-trivial governance edits, verify future read cost as well as semantic sync.
- check longest lines in touched active docs
- check one-line version timeline growth
- check active summary lines mixing current state and history
- check whether active parent changelog entries should become mapped version detail shards
- check README/TODO/phase/patch lines that would create large one-line diffs
- check whether touched God-line candidates were repaired or explicitly flagged
- check whether worker routing was used before broad raw review

### 26) Governed document God-file prevention

A God document is an active governance file that carries too many document roles or independent execution meanings in one place.

Signals include:
- current state, history, verification, rollback, roadmap, TODO, changelog, and design truth mixed in one active body
- one phase or patch carrying several independent goals, outputs, gates, rollback boundaries, or capability streams
- active README, TODO, phase summary, design, changelog, or patch updates that require large unrelated edits for a small logical change
- repeated compaction or broad rereads caused by one active file acting as a storage dump instead of a map

Required repair posture:
- redistribute content to the owner that matches its role before appending more detail
- use design sharding for large active target-state truth
- use active parent changelog shard maps plus `changelog/<chain>/v*.changelog.md` for same-chain version detail overload
- reserve `changelog/done/` for legacy, archive, completed-history, or explicit fallback history
- use `todo/history` / `todo/done` and `phase/history` / `phase/done` for accumulated movement or completed detail
- split God Phase and God Patch candidates by bounded goal, output, gate, rollback, or review boundary
- repair clear low-risk touched-document overload locally; flag or open a governed phase/patch when the split is broad or meaning-risky

Do not treat God-file classification as cleanup or deletion authority.

### 27) Automatic God Artifact Control Loop

When God-line, God-document, God-phase, God-patch, TODO, design, changelog, README, or summary pressure is found in touched governed scope, choose an action mode.

Action modes:
- `REPAIR_NOW`: clear, local, meaning-preserving, low-risk touched-scope split
- `DELEGATE_REPAIR`: context-heavy but bounded repair assigned to an edit-capable worker
- `PLAN_IN_CURRENT_PHASE`: real repair belongs to the active phase or implied execution slice
- `OPEN_REPAIR_PATCH`: reviewable before/after change needs patch packaging
- `OPEN_NEW_PHASE_OR_SUBPHASE`: distinct goal, output, gate, release, rollback, or capability boundary exists
- `BLOCK_CLOSEOUT`: touched-scope pressure remains unresolved or unplanned
- `ASK_ONLY_IF_AMBIGUOUS`: owner, meaning, or approval basis changes the safe path

Required loop:
1. detect the God artifact pressure
2. classify document family, owner, risk, and repair boundary
3. route content to the correct owner surface
4. repair now when `REPAIR_NOW` applies
5. otherwise create or extend the smallest visible governed repair slice
6. verify repaired or planned state before sync, no-drift, closeout, or release-ready claims

Do not ask the user to restate the repair instruction when the route is clear. Ask only when ambiguity or approval sensitivity changes the action.

### 28) Delegated governed-document repair route

Context-heavy God-line or God-document repair may be delegated to an edit-capable worker only when the repair is bounded, meaning-preserving, and assigned to exact artifacts or anchors.

Delegated repair must not:
- delete files or governed history
- summarize away, reinterpret, or status-upgrade content
- relocate content or mutate authority roles
- lose history/done reachability or break cross-references
- perform destructive action

Route to visible planning, blocking, or ask state instead of worker edits when repair is:
- ambiguous, history-heavy, authority-shifting, or broad
- destructive or limited by a user analysis-only request

Leader verification remains required before clean sync, no-drift, closeout, or release-ready wording

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
Writing active docs?
  → YES: apply touched-doc God-line repair, append-vs-restructure, and density checks
  → NO: preserve checked-scope evidence boundaries
  ↓
God artifact pressure found in touched scope?
  → YES: classify owner/risk, then repair now, delegate bounded repair, or create a visible repair slice
  → NO: continue
  ↓
Compact/thrash or high-density output appears?
  → YES: diagnose source pattern and repair document/workflow shape
```

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| user asks about AI/RULES behavior while providing logs/snippets | classify as behavior/governance first; do not auto-explore project |
| broad search/read, aggregate governance/code read burst, or repository exploration | dispatch standalone worker or state narrow direct-handling reason before broad absorption |
| broad roadmap/phase-matrix analysis | use a focused read-only planning/review lane when multiple design, TODO, phase, risk, or dependency surfaces need synthesis |
| coordination design or cross-session behavior proposal | classify the actual mechanism first, then keep claims within checked capability |
| high-output test/log/build evidence | prefer worker filtering before leader reads raw noisy output |
| multi-surface governance audit | use a focused audit worker or multiple standalone workers when scope is broad |
| phase changes but the worker responsibility remains the same | reuse or steer the standing-role worker; put phase context in the assignment |
| reuse, spawn, respawn, shutdown, or duplicate/overlap report | audit checked coordination evidence and report scoped state before deciding |
| simultaneous same-role lanes | name lanes by responsibility, surface, or output rather than phase ID alone |
| context-heavy God-line/God-document repair | use a bounded edit-capable repair lane only with explicit scope, edit ownership, and preservation constraints |
| external docs/API/provider research | use worker lane when source volume or comparison cost is high, with source-trust expectations in the assignment |
| broad design-improvement research | map independent topic lanes first, then dispatch one or more focused subagents before leader raw websearch absorption |
| independent parallel research lanes | use multiple subagents when coordination need stays low and topics are meaningfully separable |
| implementation plus review/test/docs sync with dependencies | consider Agent Team only when shared coordination is truly needed |
| teammate/Agent Team is banned | use standalone subagent if agents are not broadly banned |
| trivial local task | handle directly; do not force delegation |
| high edit overlap | avoid parallel edit lanes; consider read-only investigation instead |
| visible custom agent matches selected worker capability | prefer best-fit specialist before generic fallback |
| God artifact pressure in touched scope | choose an action mode (REPAIR_NOW, DELEGATE_REPAIR, PLAN_IN_CURRENT_PHASE, OPEN_REPAIR_PATCH, OPEN_NEW_PHASE_OR_SUBPHASE, BLOCK_CLOSEOUT, ASK_ONLY_IF_AMBIGUOUS) |
| compact/thrash or post-compact refill | diagnose source pattern and repair document/workflow shape |

---

## Anti-Patterns

Avoid:
- treating pasted project paths/logs as permission to inspect code
- leader absorbing broad raw search/read/log/test/roadmap evidence by default
- skipping the worker-first aggregate-read gate before broad governance/code scans
- leader running broad design-improvement websearch or phase-roadmap synthesis directly when research/planning lanes would filter it better
- routing by tool name alone
- assuming an unverified hook, transport, recall, board, team, plugin, or MCP mechanism can deliver coordination behavior
- saying agents could help without dispatching when worker-fit is present
- treating teammate/Agent Team bans as standalone-subagent bans
- escalating to Agent Team when one subagent would cover the work
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
- reading several "bounded" files without considering aggregate output size
- appending release/history details to an already huge active line
- noticing a low-risk touched God-line candidate but only warning while continuing to edit around it
- treating line count as safe when characters per line are high
- using post-compact restrictions as the main solution when document structure or worker routing is the real cause
- turning active entrypoints into history books
- treating `changelog/done/` as the default storage route for ordinary same-chain version detail
- delegating ambiguous, history-heavy, authority-shifting, broad, destructive, or analysis-only repair to worker edits
- claiming no-drift or release readiness without checking body sufficiency and density risks when relevant

Better behavior: classify intent and worker scale first, dispatch the smallest fitting lane or state the narrow direct-handling reason, select the best-fit visible specialist for the chosen capability, keep Agent Team escalation for true shared coordination, ask the question first, route broad raw evidence through workers, write docs for future reads, repair density debt when it appears, and require leader verification before completion wording.

---

## Integration

Related rules:
- [safe-io.md](safe-io.md) - bounded file reading plus sharded design and changelog parent-map read order
- [safe-io.md](safe-io.md) - bounded command output handling
- [document-integrity.md](document-integrity.md) - TODO/phase active-entrypoint rollover
- [document-governance.md](document-governance.md) - compact design indexes and child shards
- [document-governance.md](document-governance.md) - active parent changelogs, chain-scoped version detail shards, fallback history boundaries
- [document-integrity.md](document-integrity.md) - cross-reference, parent/shard links, no-drift verification
- [document-governance.md](document-governance.md) - document roles and active runtime install scope
- [coding-discipline.md](coding-discipline.md) - code-side analogy for God-function/God-file pressure
- [evidence-discipline.md](evidence-discipline.md) - keeps partial reads and worker findings evidence-bounded
- [external-verification-and-source-trust.md](external-verification-and-source-trust.md) - source trust, corroboration, and external-evidence conflict handling for research lanes
- [authority-and-scope.md](authority-and-scope.md) - user override for specialist choice
- [action-safety.md](action-safety.md) - execution confirmation separate from delegation choice
- execution-continuity must not bypass the worker gate; TODO/phase rules shape live tracking and phase context; evidence, accurate-communication, and zero-hallucination chains keep worker and leader claims calibrated; communication/anti-sycophancy rules keep specialist choice calm and evidence-based
