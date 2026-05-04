# Custom Agent Selection Priority

> **Current Version:** 1.3
> **Design:** [design/custom-agent-selection-priority.design.md](design/custom-agent-selection-priority.design.md) v1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/custom-agent-selection-priority.changelog.md](changelog/custom-agent-selection-priority.changelog.md)

---

## Rule Statement

**Core Principle: When a visible custom or specialist agent clearly fits the worker capability already selected by native worker routing, prefer the best-fit specialist before generic handling or broader fallback agents.**

This rule owns custom-agent selection priority, best-fit specialist preference, capability-fit selection, and the distinction between discovery problems and selection behavior after worker routing has already determined that delegation or specialist handling is appropriate.

---

## Core Contract

### 1) Primary specialist pool
Treat visible user custom agents in `~/.claude/agents/` as the primary specialist pool when a task clearly matches one of them.

### 2) Capability-fit before generic
If worker routing identifies a needed capability and a task has a clear specialist fit, prefer the best-fit custom user agent before generic direct handling or broader built-in/plugin fallback when the custom agent is more specific and user-intended. Select by required capability and domain fit, not by hardcoded tool-name matching.

### 3) No forced delegation
Do not delegate just because an agent exists. Delegation requires worker routing to have selected delegation or specialist handling, strong domain/capability fit, real specialist value, proportionate coordination overhead, and no stronger user, safety, or execution boundary selecting another path. Specialist availability never proves delegation need by itself.

### 3.1) Routing-Before-Selection Principle
Worker routing and custom-agent selection are separate decisions.
Required guidance:
- use `native-worker-agent-routing-and-context-control.md` first to decide user intent, worker capability, and whether work is direct, one standalone subagent, multiple subagents, or Agent Team escalation
- use this rule only after that routing decision to choose the best available specialist/custom agent for the selected worker path and capability
- do not use custom-agent availability alone as proof that delegation is appropriate
- do not use this rule to escalate standalone subagent work into Agent Team workflow
- do not make this rule the owner of broad-work context-control, intent classification, or worker-scale decisions

### 3.2) Reuse-Before-Spawn Principle
When a matching worker, teammate, or active specialist already covers the same role and objective, reuse that agent before spawning another one.

Required guidance:
- check whether an active or recently spawned worker already owns materially the same role
- prefer steering or reusing that worker over creating a duplicate-looking lane
- add another worker only when the work is explicitly partitioned and the new role is meaningfully distinct
- use role names that let the user tell why each worker exists

### 4) Discovery Boundary Principle
This rule does not pretend undiscovered agents are available. It governs **selection among available candidates**, not runtime file-loading behavior.

---

## Selection Order Contract

After worker routing has determined that delegation or specialist handling is appropriate:
1. identify the required worker capability and domain scope
2. check for a clear best-fit user custom agent
3. if one fits, prefer it unless a stronger reason selects another worker path
4. otherwise consider project, built-in, or plugin specialists that fit the capability
5. if no specialist adds meaningful value, use the non-specialist worker path selected by routing or return to direct handling

Preferred order when candidates are available:

| Candidate Type | Default Preference |
|----------------|--------------------|
| Best-fit user custom agent | Highest specialist preference |
| Best-fit project custom agent | High when visible and clearly better fit |
| Best-fit built-in agent | Fallback specialist path |
| Best-fit plugin agent | Fallback specialist or tooling path |
| Non-specialist standalone worker lane | Default when context isolation matters but no specialist fits |
| Direct handling | Default only when no worker or specialist advantage is clear |

---

## Delegation Trigger Model

Prefer a custom user agent only when worker routing has selected a delegated/specialist path and all conditions hold: the task strongly matches the agent’s documented domain, the agent is visible/available in the current session, the selected path needs that capability, specialist handling materially helps, and direct/generic handling would be broader or weaker.

Do not prefer a custom user agent when the task is trivial, falls into an explicit deferral/not-for boundary, the runtime has not discovered the agent, the user asks for another path, the user bans the relevant worker mechanism, a standalone worker lane is sufficient and this would escalate into Agent Team workflow, or an active worker already covers the same role without overlap.

---

## Direct Handling vs Specialist Handling

Direct handling remains acceptable when the task is simple/local, no specialist clearly improves the answer, the question is too broad to map to one specialist cleanly, or the user explicitly wants direct handling.

Specialist handling is preferred when worker routing has selected a delegated/specialist path, the required capability and domain fit are strong and specific, the custom agent has clearer scope or expertise than the generic path, and the user’s installed specialist pool is obviously intended to own that task family.

---

## Anti-Pattern Boundary

Avoid these selection failures:
- ignoring a clear custom specialist after routing already selected specialist handling
- delegating to a custom agent without strong capability fit
- using custom-agent availability as the routing decision
- using this rule to escalate subagent-fit work into Agent Team workflow
- spawning a second same-role worker without a distinct partition
- treating built-ins/plugins as automatically superior to user custom agents when a visible user specialist fits better
- pretending an undiscovered agent is available
- over-delegating trivial work

Better behavior: let native routing decide worker scale first, then select the best visible specialist for that selected capability; reuse aligned active workers before spawn; keep direct handling for simple tasks.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Clear-best-fit custom specialist preferred when available | High |
| Capability-fit specialist selection | High |
| Generic direct handling despite strong visible custom fit after delegation is appropriate | Low |
| Over-delegation of trivial work | Low |
| Agent Team escalation caused by selection rule alone | 0 critical cases |
| Confusion between routing and specialist selection | 0 critical cases |
| Confusion between discovery failure and selection choice | 0 critical cases |
| Built-in/plugin overuse when a user custom agent is clearly better fit | Low |

---

## Integration
Related rules: `native-worker-agent-routing-and-context-control.md` owns intent, worker capability, worker scale, and leader-context control before this rule selects the best-fit specialist; `authority-and-scope.md` preserves user override; `functional-intent-verification.md` keeps execution confirmation separate from delegation choice; communication and anti-sycophancy rules keep specialist choice calm and evidence-based.

---
