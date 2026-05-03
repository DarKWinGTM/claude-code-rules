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

## Core Principles

### 1) Primary Specialist Pool Principle
Treat visible user custom agents in `~/.claude/agents/` as the primary specialist pool when a task clearly matches one of them.

### 2) Capability-Fit Before Generic Principle
If worker routing identifies a needed capability and a task has a clear specialist fit:
- prefer the best-fit custom user agent before generic direct handling
- prefer the best-fit custom user agent before broader built-in or plugin fallbacks when the custom agent is more specific and more user-intended for the capability
- select by the task’s required capability and domain fit, not by hardcoded tool-name matching

### 3) No Forced Delegation Principle
Do not delegate just because an agent exists.
Use delegation only when:
- worker routing has selected delegation or specialist handling
- domain/capability fit is strong
- the specialist adds real value
- no stronger boundary says otherwise

### 3.1 Routing-Before-Selection Principle
Worker routing and custom-agent selection are separate decisions.

Required guidance:
- use `native-worker-agent-routing-and-context-control.md` to decide user intent, worker capability, and whether the work should be handled directly, by one standalone subagent, by multiple subagents, or by an Agent Team escalation
- use this rule after that routing decision to choose the best available specialist or custom agent for the selected worker path and required capability
- do not use custom-agent availability alone as proof that delegation is appropriate
- do not use this rule to escalate standalone subagent work into Agent Team workflow
- do not make this rule the owner of broad-work context-control, intent classification, or worker-scale decisions

### 3.2 Reuse-Before-Spawn Principle
When a matching worker, teammate, or active specialist already covers the same role and objective, reuse that agent before spawning another one.

Required guidance:
- check whether an active or recently spawned worker already owns materially the same role
- prefer steering or reusing that worker over creating a duplicate-looking lane
- only add another worker when the work is explicitly partitioned and the new role is meaningfully distinct
- use role names that let the user tell why each worker exists

### 4) Discovery Boundary Principle
This rule does not pretend undiscovered agents are available.
It governs **selection among available candidates**, not runtime file-loading behavior.

---

## Selection Order Contract

After worker routing has determined that delegation or specialist handling is appropriate:
1. identify the required worker capability and domain scope
2. check whether a clear best-fit user custom agent is available
3. if yes, prefer it unless a stronger reason selects another worker path
4. if no clear custom fit exists, consider project, built-in, or plugin specialists that fit the capability
5. if no specialist adds meaningful value, return to direct handling or the non-specialist worker path selected by routing

### Preferred order when candidates are available
| Candidate Type | Default Preference |
|----------------|--------------------|
| Best-fit user custom agent | Highest specialist preference |
| Best-fit project custom agent | High when visible and clearly better fit |
| Best-fit built-in agent | Fallback specialist path |
| Best-fit plugin agent | Fallback specialist or tooling path |
| Non-specialist standalone worker lane | Default when context isolation matters but no specialist fit exists |
| Direct handling | Default only when no worker or specialist advantage is clear |

---

## Delegation Trigger Model

Prefer a custom user agent when worker routing has selected a delegated or specialist path and all of these are true:
- the task matches the agent’s documented domain strongly
- the agent is visible/available in the current session
- the selected worker path needs the agent’s capability
- the task would materially benefit from specialist handling
- direct handling or a generic worker lane would be broader or weaker than the specialist path

Do not prefer a custom user agent when:
- the task is trivial and delegation adds no real value
- the task falls into an explicit deferral/not-for boundary
- the runtime has not discovered the agent in the current session
- the user explicitly asks for another path
- the user has banned the relevant worker mechanism broadly enough to include that agent type
- a standalone worker lane is sufficient and this selection would unnecessarily escalate into Agent Team workflow
- an already-active worker can cover the same role without creating overlapping noise

---

## Direct Handling vs Specialist Handling

Direct handling remains acceptable when:
- the task is simple and local
- no specialist clearly improves the answer
- the question is too broad to map to one specialist cleanly
- the user explicitly wants direct handling

Specialist handling is preferred when:
- worker routing has selected a delegated or specialist path
- the required capability and domain fit are strong and specific
- the custom agent has clearer scope or expertise than the generic path
- the user’s installed specialist pool is obviously intended to own that task family

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| ignoring a clear custom specialist and answering generically | wastes the user’s specialist setup | prefer the best-fit custom agent after routing selects specialist handling |
| delegating to any custom agent without strong capability fit | creates arbitrary routing | require clear domain and capability fit |
| using custom-agent availability as the routing decision | confuses specialist selection with workload routing | let `native-worker-agent-routing-and-context-control.md` decide intent, capability, and worker scale first |
| using this rule to escalate subagent-fit work into Agent Team workflow | over-tasks simple worker lanes | keep Agent Team escalation owned by worker routing and only for coordination need |
| spawning a second worker for the same role with no distinct partition | creates duplicate-looking noise and overlap | reuse the existing worker or define clearly different roles before spawning |
| treating built-ins/plugins as automatically superior to user custom agents | ignores the user’s installed specialist pool | use custom agents first when fit is clear |
| pretending an undiscovered agent is available | hides real discovery problems | distinguish discovery from selection |
| over-delegating trivial work | adds churn without benefit | keep direct handling for simple tasks |

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

Related rules:
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - owns intent, required worker capability, worker-scale routing, and leader-context control before this rule selects a best-fit specialist
- [authority-and-scope.md](authority-and-scope.md) - user authority still overrides delegation preference when the user chooses another path
- [functional-intent-verification.md](functional-intent-verification.md) - keeps execution confirmation separate from delegation choice
- [natural-professional-communication.md](natural-professional-communication.md) - delegation behavior should remain calm and non-theatrical
- [anti-sycophancy.md](anti-sycophancy.md) - specialist choice should be evidence-based, not performed agreement

---
