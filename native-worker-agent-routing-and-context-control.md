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
Classify the user’s intent before treating technical material as project work:
- AI/RULES behavior or workflow-compliance analysis
- project fact-checking or codebase inspection
- implementation or refactor execution
- review, audit, or verification
- explanation only

Pasted logs, snippets, paths, or another session’s worker notes are evidence for the current question, not automatic authorization to inspect the referenced project. If the user asks about assistant behavior or RULES behavior, stay in that scope unless project exploration is explicitly requested or a bounded verification need is stated.

Use direct leader handling for trivial, one-step, tightly sequential, low-output, exact interactive-control work, high edit-overlap work, unavailable worker tooling, or explicit user direction. Otherwise run the worker gate before broad codebase searches, large file reads, symbol/path tracing, high-output tests/logs/builds, external docs/provider research, multi-surface governance sweeps, design/security/migration reviews, or safely partitionable implementation.

พูดง่าย ๆ: ถ้างานกว้างจน main session ไม่จำเป็นต้องอ่าน raw ทุกอย่างเอง ให้ใช้ subagent หรือ worker lane ที่เล็กที่สุดไปกรองก่อน แต่ถ้าผู้ใช้ถามเรื่องพฤติกรรมของ AI ก็อย่าไหลไปสำรวจ project เพียงเพราะมี path/log แปะมา.
---
## Core Contract
### 1) Intent-first worker gate
Behavior/RULES questions are answered from the behavior/rule layer first. Project exploration begins only when the user asks for project facts, implementation, or verification, or when checked evidence is required and scope is stated. Another session’s pasted output may show a possible worker use case, but it does not make project inspection the active task. If intent is behavior analysis plus broad evidence review, use a worker lane to analyze the evidence rather than letting the leader absorb it directly.

### 2) Worker-scale gate
Before broad main-session absorption, classify the smallest worker structure that preserves correctness and context efficiency.
Required guidance:
- run this gate before broad reads/searches, noisy command output, multi-surface audit, external research, or safely partitionable implementation
- prefer one standalone subagent-style lane for a bounded independent broad/read/review/filter task before considering Agent Team workflow
- if a worker lane is selected, dispatch/assign it before the leader absorbs raw broad output
- if the leader handles broad worker-fit work directly, state the narrow reason before or alongside the direct action
- saying “an agent could help” is not enough; select a path and act when suitable
- worker routing never removes leader verification responsibility

### 3) Capability-based routing criteria
Route by capability and workload shape, not rigid tool name. Evaluate user intent/scope, context isolation and output noise, broad evidence-filtering need, lane independence, specialist value, parallel value, coordination/dependencies, risk/security/verification burden, edit overlap, whether the leader needs raw evidence or analyzed result, worker availability, and user constraints. Tool names such as `Agent`, `Explore`, repository search, web search, or future workers are implementation details.

### 4) Worker path model
| Work shape | Preferred path |
|---|---|
| trivial, exact, one-step, low-output, tightly sequential | leader directly |
| one bounded research/review/source scan/log-test filter/docs lookup/evidence proof lane | one focused standalone subagent / worker lane |
| two or more independent read-only/filter/comparison lanes | multiple focused standalone subagents |
| shared ownership, dependencies, teammate messaging, implementation plus review/test/docs sync, or durable handoff | official Agent Team / teammates as exceptional escalation |

### 5) Native execution behavior
Worker routing is normal execution behavior, not a special mode. Proactively look for worker-fit slices, keep the worker set minimal, prefer subagent-first handling for broad lanes without shared-team coordination, reuse active/recent standing-role workers before duplicate-looking spawns, put phase/task/objective context in the assignment rather than necessarily in worker identity, and do not over-delegate simple work.

### 6) Team restriction boundary
A user ban on `teammate`, `Agent Team`, or team workflow restricts coordinated team/teammate mechanisms unless the user explicitly broadens the ban. It does **not** automatically ban standalone subagents, `Agent(...)`, `Explore(...)`, read-only reviewer/auditor agents, or comparable worker tools. If Agent Team is disallowed but broad worker-fit work remains, use a standalone subagent when suitable. If all agent/subagent mechanisms are explicitly disallowed, handle directly and state the constraint when broad work would otherwise be delegated.

### 7) Subagent lane contract
Use a standalone subagent for bounded independent work that benefits from separate context but not full team coordination. Default research/audit/review lanes to read-only unless edit ownership is explicit. Brief the lane with objective, checked scope, allowed actions, expected output, and stop gates. Scope it to return analyzed findings, not raw dumps. Use multiple subagents only for meaningfully independent lanes.

### 8) Agent Team escalation contract
Use official Agent Team / teammate workflow only when coordination is needed, not merely context filtering. Teams require shared task ownership, dependencies, messaging, implementation plus review/test/docs sync, or durable handoff that standalone subagents cannot cover cleanly. Every teammate needs distinct role, objective, checked scope, edit permission, expected output, and stop gates. Edit-capable teammates must own non-overlapping artifacts/classes. Plugin/shared-board/custom tmux bridge mechanics remain outside this Main RULES owner unless separately selected by the user or an active project rule.

### 9) Worker handoff quality
Worker output must be filtered and analyzed. Do not impose a fixed generic limit such as “under 300 words”; size handoff to task type, evidence complexity, and decision value. Include outcome, checked scope, relevant evidence, evidence strength, conflicts/uncertainty, and recommended next verification when material. Omit noise unless it explains a finding, conflict, or risk. Preserve exact file paths, symbols, command output, URLs, or line references only when materially supporting the result.

### 10) Parallel edit containment
Parallel implementation is allowed only with clear ownership separation by file, module, test target, documentation surface, or artifact class. Do not assign overlapping writes unless one lane is explicitly review-only. Use read-only workers for investigation/review when edit overlap risk is high. Edit-capable lanes report touched artifacts, checks run, unresolved risks, and handoff notes.

### 11) Main-controller verification
The leader remains responsible for synthesis, direction, verification, and completion claims. Worker findings are context, not automatic proof. Resolve conflicts from checked evidence, verify material claims before user-facing factual/completion/sync/fixed wording, and inspect changed artifacts after worker edits.
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
One bounded independent lane can filter/research/review it?
  → YES: use one focused standalone subagent
  → NO: continue
  ↓
Independent read-only lanes can run without shared ownership?
  → YES: use multiple focused standalone subagents
  → NO: continue
  ↓
Needs shared ownership, dependencies, messaging, or implementation/review/test/docs sync?
  → YES: Agent Team / teammates only if allowed and justified
  → NO: leader handles directly with narrow reason
```
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

## Anti-Pattern Boundary
Avoid: treating pasted project paths/logs as permission to inspect code; leader absorbing all broad raw search/read/log/test output by default; routing by tool name alone; saying agents could help without dispatching when worker-fit is present; treating teammate/Agent Team bans as standalone-subagent bans; escalating to Agent Team when one subagent would cover the work; fixed handoff caps; raw worker dumps; duplicate same-role worker spawn; overlapping parallel edits; treating worker summaries as proof; or importing plugin/shared-board grammar into Main RULES.

Better behavior: classify intent and worker scale first, dispatch the smallest fitting lane or state the narrow direct-handling reason, keep Agent Team escalation for true shared coordination, and require leader verification before completion wording.
---
## Verification Checklist
- [ ] User intent was classified before project exploration or broad evidence absorption
- [ ] Broad work used a standalone worker lane or had a narrow direct-handling reason
- [ ] Routing used intent, required capability, and workload shape, not rigid tool-name rules
- [ ] Smallest effective worker structure was selected
- [ ] Agent Team / teammate workflow was used only when shared coordination was truly needed and allowed
- [ ] A teammate/Agent Team ban was not treated as a standalone-subagent ban unless the user broadened it
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
Related rules: `custom-agent-selection-priority.md` selects the best specialist only after routing establishes delegation need; execution-continuity must not bypass the worker gate; TODO/phase rules shape live tracking and phase context; evidence, accurate-communication, and zero-hallucination chains keep worker and leader claims calibrated.
---
> **Full history:** [changelog/native-worker-agent-routing-and-context-control.changelog.md](changelog/native-worker-agent-routing-and-context-control.changelog.md)
