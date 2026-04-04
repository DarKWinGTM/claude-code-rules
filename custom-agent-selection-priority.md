# Custom Agent Selection Priority

> **Current Version:** 1.1
> **Design:** [design/custom-agent-selection-priority.design.md](design/custom-agent-selection-priority.design.md) v1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/custom-agent-selection-priority.changelog.md](changelog/custom-agent-selection-priority.changelog.md)

---

## Rule Statement

**Core Principle: When a user custom agent in `~/.claude/agents/` is available and clearly fits the task, prefer it as the primary specialist path before generic handling or broader fallback agents.**

This rule owns custom-agent selection priority, best-fit specialist preference, and the distinction between discovery problems and selection behavior.

---

## Core Principles

### 1) Primary Specialist Pool Principle
Treat visible user custom agents in `~/.claude/agents/` as the primary specialist pool when a task clearly matches one of them.

### 2) Best-Fit Before Generic Principle
If a task has a clear specialist fit:
- prefer the best-fit custom user agent before generic direct handling
- prefer the best-fit custom user agent before broader built-in or plugin fallbacks when the custom agent is more specific and more user-intended for the task

### 3) No Forced Delegation Principle
Do not delegate just because an agent exists.
Use delegation only when:
- domain fit is strong
- the specialist adds real value
- no stronger boundary says otherwise

### 3.1 Reuse-Before-Spawn Principle
When a matching teammate or active specialist already covers the same role and objective, reuse that agent before spawning another one.

Required guidance:
- check whether an active or recently spawned teammate already owns materially the same role
- prefer steering or reusing that teammate over creating a duplicate-looking teammate
- only add another teammate when the work is explicitly partitioned and the new role is meaningfully distinct
- use role names that let the user tell why each teammate exists

### 4) Discovery Boundary Principle
This rule does not pretend undiscovered agents are available.
It governs **selection among available candidates**, not runtime file-loading behavior.

---

## Selection Order Contract

When evaluating a task:
1. check whether a clear best-fit user custom agent is available
2. if yes, prefer it unless a stronger reason to avoid delegation exists
3. if no clear custom fit exists, consider built-in or plugin specialists
4. if no specialist adds meaningful value, use direct handling

### Preferred order when candidates are available
| Candidate Type | Default Preference |
|----------------|--------------------|
| Best-fit user custom agent | Highest specialist preference |
| Best-fit project custom agent | High when visible and clearly better fit |
| Best-fit built-in agent | Fallback specialist path |
| Best-fit plugin agent | Fallback specialist or tooling path |
| Direct handling | Default only when no specialist advantage is clear |

---

## Delegation Trigger Model

Prefer a custom user agent when all of these are true:
- the task matches the agent’s documented domain strongly
- the agent is visible/available in the current session
- the task would materially benefit from specialist handling
- direct handling would be broader or weaker than the specialist path

Do not prefer a custom user agent when:
- the task is trivial and delegation adds no real value
- the task falls into an explicit deferral/not-for boundary
- the runtime has not discovered the agent in the current session
- the user explicitly asks for another path
- an already-active teammate can cover the same role without creating overlapping team noise

---

## Direct Handling vs Specialist Handling

Direct handling remains acceptable when:
- the task is simple and local
- no specialist clearly improves the answer
- the question is too broad to map to one specialist cleanly
- the user explicitly wants direct handling

Specialist handling is preferred when:
- the domain fit is strong and specific
- the custom agent has clearer scope or expertise than the generic path
- the user’s installed specialist pool is obviously intended to own that task family

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| ignoring a clear custom specialist and answering generically | wastes the user’s specialist setup | prefer the best-fit custom agent |
| delegating to any custom agent without strong fit | creates arbitrary routing | require clear domain fit |
| spawning a second teammate for the same role with no distinct partition | creates duplicate-looking team noise and overlap | reuse the existing teammate or define clearly different roles before spawning |
| treating built-ins/plugins as automatically superior to user custom agents | ignores the user’s installed specialist pool | use custom agents first when fit is clear |
| pretending an undiscovered agent is available | hides real discovery problems | distinguish discovery from selection |
| over-delegating trivial work | adds churn without benefit | keep direct handling for simple tasks |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Clear-best-fit custom specialist preferred when available | High |
| Generic direct handling despite strong visible custom fit | Low |
| Over-delegation of trivial work | Low |
| Confusion between discovery failure and selection choice | 0 critical cases |
| Built-in/plugin overuse when a user custom agent is clearly better fit | Low |

---

## Integration

Related rules:
- [authority-and-scope.md](authority-and-scope.md) - user authority still overrides delegation preference when the user chooses another path
- [functional-intent-verification.md](functional-intent-verification.md) - keeps execution confirmation separate from delegation choice
- [natural-professional-communication.md](natural-professional-communication.md) - delegation behavior should remain calm and non-theatrical
- [anti-sycophancy.md](anti-sycophancy.md) - specialist choice should be evidence-based, not performed agreement

---
