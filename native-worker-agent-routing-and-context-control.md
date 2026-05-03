# Native Worker Agent Routing and Context Control
> **Current Version:** 1.1
> **Design:** [design/native-worker-agent-routing-and-context-control.design.md](design/native-worker-agent-routing-and-context-control.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/native-worker-agent-routing-and-context-control.changelog.md](changelog/native-worker-agent-routing-and-context-control.changelog.md)
---
## Rule Statement
**Core Principle: Use the smallest effective standalone worker lane first for broad, high-context, high-output, or naturally parallel work, so the leader session stays the controller and verifier instead of absorbing every raw search, read, log, test, or review surface itself.**
This rule owns native worker routing, leader-context protection, subagent-first worker-scale decisions, Agent Team escalation boundaries, worker handoff quality, and main-session verification boundaries. It does not replace custom-agent selection, task-list semantics, phase semantics, evidence wording, safety gates, or plugin/shared-board/runtime coordination mechanics.
---
## Intent and Scope Boundary
Before treating technical material as project work, classify the user’s intent:
- AI behavior, RULES behavior, or workflow-compliance analysis
- project fact-checking or codebase inspection
- implementation or refactor execution
- review, audit, or verification
- explanation only

Pasted logs, snippets, paths, or another session’s worker notes are evidence for the user’s current question, not automatic authorization to inspect the referenced project. If the user is asking about assistant behavior or RULES behavior, stay in that behavioral/governance scope unless the user explicitly requests project exploration.

This rule applies when work may benefit from a separate worker lane before the main session absorbs broad context or noisy evidence:
- broad codebase searches, large file reads, symbol/path tracing, or repository exploration
- high-output test, log, build, trace, or operational-failure review
- external documentation, provider/API, release-note, compatibility, or source-trust research
- multi-surface governance sweeps across README, design, changelog, TODO, phase, and patch
- design gathering, option comparison, security/risk review, or migration impact review
- implementation that can be safely split by non-overlapping files, modules, tests, or documentation surfaces
Use direct main-session handling when the task is trivial, one-step, tightly sequential, low-output, requires exact interactive control, has high edit-overlap risk, lacks usable worker tooling, or the user explicitly directs direct handling.

พูดง่าย ๆ: ถ้างานกว้างจน main session ไม่จำเป็นต้องอ่าน raw ทุกอย่างเอง ให้ใช้ subagent หรือ worker lane ที่เล็กที่สุดไปกรองก่อน แต่ถ้าผู้ใช้ถามเรื่องพฤติกรรมของ AI ก็อย่าไหลไปสำรวจ project เพียงเพราะมี path/log แปะมา.
---
## Core Contract
### 1) Intent-first worker gate
Classify intent before broad reading or execution.
Required guidance:
- behavior/RULES questions should be answered from the behavior/rule layer first
- project exploration begins only when the user asks for project facts, implementation, or verification, or when checked evidence is required and scope is stated
- another session’s pasted output may show a possible use case for subagents, but it does not by itself make project inspection the active task
- when intent is behavior analysis plus broad evidence review, use a worker lane to analyze the evidence rather than letting the leader absorb everything directly
### 2) Worker-scale gate
Before broad main-session absorption, classify the smallest worker structure that preserves correctness and context efficiency.
Required guidance:
- run this gate before broad reads, broad searches, noisy command output, multi-surface audit, external research, or safely partitionable implementation
- prefer a standalone subagent-style lane for one bounded independent broad/read/review/filter task before considering Agent Team workflow
- if the gate selects a worker lane, dispatch or assign that lane before the leader absorbs the raw broad output
- if the leader handles broad worker-fit work directly, state the narrow reason before or alongside the direct action
- do not satisfy the gate by merely saying an agent could be useful; select a path and act on it when suitable
- do not use worker routing as a reason to avoid leader verification
### 3) Capability-based routing criteria
Choose the path by required capability and workload shape, not by rigid tool name.
Evaluate:
- user intent and active scope
- context isolation need
- context cost and likely output noise
- broad read/search or evidence-filtering need
- independence of the work lane
- domain/specialist reasoning need
- parallel value and time savings
- coordination need and dependency structure
- risk, security sensitivity, and verification burden
- edit overlap or conflict risk
- whether the leader truly needs raw evidence or only the analyzed result
- worker/tool availability and user-directed constraints

Tool names such as `Agent`, `Explore`, repository search, web search, or future worker mechanisms are implementation details. The rule should identify the needed worker capability first, then choose the smallest available mechanism that can provide it.
### 4) Worker path model
| Work shape | Preferred path |
|---|---|
| trivial, exact, one-step, low-output, or tightly sequential work | leader session directly |
| one bounded independent research, review, source scan, log/test filter, docs lookup, evidence analysis, or proof-check lane | one focused standalone subagent / worker lane |
| two or more independent read-only/filter/comparison lanes with low coordination need | multiple focused standalone subagents |
| coordinated lanes needing shared task ownership, dependencies, teammate messaging, implementation plus review/test/docs sync, or durable handoff | official Agent Team / teammates as an exceptional escalation |
### 5) Native execution behavior
Worker routing is part of normal execution behavior, not a special mode that waits for the user to request agents.
Required guidance:
- proactively look for worker-fit slices during real work
- keep the worker set as small as possible
- prefer subagent-first handling for broad read/search/audit/review lanes that do not need shared team coordination
- reuse an active or recent standing role worker before spawning a duplicate-looking lane
- put phase/task/objective context in the assignment, not necessarily in the worker identity
- do not over-delegate simple work where coordination overhead is higher than benefit
### 6) Team restriction boundary
A user ban on `teammate`, `Agent Team`, or team workflow restricts coordinated team/teammate mechanisms unless the user explicitly broadens the ban.
Required guidance:
- do not treat a teammate/Agent Team ban as a ban on all standalone subagents, `Agent(...)`, `Explore(...)`, read-only reviewer agents, auditor agents, or comparable worker tools
- if Agent Team is disallowed but broad worker-fit work remains, use a standalone subagent lane when suitable
- if all agent/subagent mechanisms are explicitly disallowed, handle directly and state the constraint when broad work would otherwise be delegated
### 7) Subagent lane contract
Use a standalone subagent for bounded independent work that benefits from separate context but does not need full team coordination.
Required guidance:
- default research, audit, and review lanes to read-only unless edit ownership is explicit
- brief the subagent with objective, checked scope, allowed actions, expected output, and stop gates
- keep each lane scoped enough that it can return analyzed findings instead of raw dumps
- use multiple subagents only when lanes are meaningfully independent
### 8) Agent Team escalation contract
Use an official Agent Team / teammate structure only when the work needs coordination rather than only context filtering.
Required guidance:
- use teams only when lanes require shared task ownership, dependencies, messaging, implementation plus review/test/docs sync, or durable handoff that standalone subagents cannot cover cleanly
- every teammate should have a distinct role, objective, checked scope, edit permission, expected output, and stop gates
- edit-capable teammates must own non-overlapping artifacts or artifact classes
- the leader must inspect changed artifacts before claiming completion
- plugin, shared-board, and custom tmux bridge mechanics remain outside this Main RULES owner unless separately selected by the user or an active project rule
### 9) Worker handoff quality
Worker output must be filtered and analyzed, not raw transcript dump.
Required guidance:
- do not impose a fixed generic limit such as “under 300 words”
- size the handoff to the task type, evidence complexity, and decision value
- include the outcome, checked scope, relevant evidence, evidence strength, conflicts or uncertainty, and recommended next verification when material
- omit noisy or irrelevant evidence unless it explains a finding, conflict, or risk
- preserve exact file paths, symbols, command outputs, URLs, or line references only when they materially support the result
### 10) Parallel edit containment
Parallel implementation is allowed only when ownership is separated clearly.
Required guidance:
- split edit lanes by file, module, test target, documentation surface, or artifact class
- do not assign overlapping writes to multiple workers unless one lane is explicitly review-only
- use read-only workers for investigation/review when edit overlap risk is high
- require edit-capable lanes to report touched artifacts, checks run, unresolved risks, and handoff notes
### 11) Main-controller verification
The leader session remains responsible for synthesis, direction, verification, and completion claims.
Required guidance:
- worker findings are useful context, not automatic proof
- resolve conflicting worker findings from checked evidence
- verify material claims before user-facing factual, completion, synchronization, or fixed/stable wording
- inspect actual changed artifacts after worker edits before reporting completion
---
## Trigger Model
| Trigger | Required behavior |
|---|---|
| user asks about AI/RULES behavior while providing logs/snippets | classify as behavior/governance first; do not auto-explore project |
| broad search/read or repository exploration | dispatch standalone worker or state narrow direct-handling reason before broad absorption |
| high-output test/log/build evidence | prefer worker filtering before leader reads raw noisy output |
| multi-surface governance audit | use a focused audit worker or multiple standalone workers when scope is broad |
| external docs/API/provider research | use worker lane when source volume or comparison cost is high |
| independent parallel research lanes | use multiple subagents when coordination need stays low |
| implementation plus review/test/docs sync with dependencies | consider Agent Team only when shared coordination is truly needed |
| teammate/Agent Team is banned | use standalone subagent if agents are not broadly banned |
| trivial local task | handle directly; do not force delegation |
| high edit overlap | avoid parallel edit lanes; consider read-only investigation instead |
---
## Decision Flow
```text
Work starts or next slice is discovered
  ↓
What is the user intent?
  → AI/RULES behavior: stay behavior/governance first
  → project fact/implementation/review: continue
  → unclear and outcome-changing: clarify or state working scope
  ↓
Is it broad, noisy, context-heavy, multi-surface, or parallelizable?
  → NO: leader handles directly
  → YES: continue
  ↓
Can one bounded independent lane filter/research/review it?
  → YES: use one focused standalone subagent
  → NO: continue
  ↓
Can independent read-only lanes run in parallel without shared ownership?
  → YES: use multiple focused standalone subagents
  → NO: continue
  ↓
Does it need shared ownership, dependencies, messaging, or implementation/review/test/docs sync?
  → YES: Agent Team / teammates only if allowed and justified
  → NO: leader handles directly with narrow reason
```
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| treating pasted project paths/logs as automatic permission to inspect project code | classify the user’s active intent first |
| leader absorbs all broad raw search/read/log/test output by default | classify worker scale first and delegate or justify direct handling |
| routing by tool name alone | route by intent, required capability, context cost, independence, risk, and coordination need |
| saying agents could help but not dispatching any worker | actually assign the smallest fitting lane when worker-fit is present |
| treating a teammate/Agent Team ban as a ban on standalone subagents | keep coordinated-team restriction separate from standalone worker tools |
| escalating to Agent Team when one subagent would cover the work | use subagent-first unless shared coordination is required |
| fixed handoff cap such as 300 words | size handoff to evidence complexity and decision value |
| worker raw dump | return analyzed findings, checked scope, evidence strength, and next verification |
| duplicate same-role worker spawn | reuse/steer standing role worker when aligned |
| parallel workers editing overlapping files | split ownership or make one lane review-only |
| treating worker summary as proof of completion | leader verifies artifacts and material claims |
| using worker routing to import plugin/shared-board grammar into Main RULES | keep runtime/plugin coordination mechanics in their own owners |
---
## Verification Checklist
- [ ] User intent was classified before project exploration or broad evidence absorption
- [ ] Broad work used a standalone worker lane or had a narrow direct-handling reason
- [ ] Routing decision was based on intent, required capability, and workload shape, not rigid tool-name rules
- [ ] Smallest effective worker structure was selected
- [ ] Agent Team / teammate workflow was used only when shared coordination was truly needed and allowed
- [ ] Research/review lanes were read-only unless edit ownership was explicit
- [ ] Edit-capable lanes had non-overlapping ownership
- [ ] Worker handoff was analyzed and proportionate, not raw dump or fixed word cap
- [ ] Leader verified material claims and changed artifacts before completion wording
- [ ] Custom-agent selection was delegated to `custom-agent-selection-priority.md` after routing established delegation need
---
## Quality Metrics
| Metric | Target |
|---|---|
| Intent-first classification before broad work | High |
| Broad-work worker-gate application | High |
| Subagent-first broad-work handling | High |
| Agent Team over-escalation | Low |
| Main-session raw context overload | Low |
| Delegation-by-capability clarity | High |
| Over-delegation of trivial work | Low |
| Worker handoff signal quality | High |
| Parallel edit overlap | 0 critical cases |
| Leader verification before completion claims | 100% |
---
## Integration
Related rules:
- [custom-agent-selection-priority.md](custom-agent-selection-priority.md) - selects the best available specialist/custom agent after this rule determines worker routing and required capability
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - execution continuity must recheck intent and must not bypass the worker-scale gate when the next slice is broad or high-output
- [todo-standards.md](todo-standards.md) - live task list remains the active execution-tracking surface for non-trivial work
- [phase-implementation.md](phase-implementation.md) - phase context shapes worker assignments when phase-backed work is active
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - worker and leader claims remain evidence-calibrated
- [accurate-communication.md](accurate-communication.md) - handoff and completion wording must match checked evidence
- [zero-hallucination.md](zero-hallucination.md) - worker output must not become invented certainty
---
> **Full history:** [changelog/native-worker-agent-routing-and-context-control.changelog.md](changelog/native-worker-agent-routing-and-context-control.changelog.md)
