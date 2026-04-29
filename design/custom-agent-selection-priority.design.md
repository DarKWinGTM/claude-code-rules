# Custom Agent Selection Priority

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-04-04)

---

## 1) Goal

Define one first-class rule chain for custom agent selection priority so the assistant:
- treats visible user custom agents in `~/.claude/agents/` as the primary specialist pool when they are available
- prefers the best-fit custom specialist before generic handling when a task clearly matches a specialist domain
- keeps delegation selective and justified rather than forcing agents into every task
- prefers reuse-before-spawn when an existing teammate already covers the same role
- separates discovery/loading concerns from selection/invocation concerns

This chain should improve real custom-agent usage without pretending that runtime discovery itself is controlled by prompt rules.

---

## 2) Problem Statement

The system can have several candidate handling paths:
- user custom agents in `~/.claude/agents/`
- project-visible agents
- built-in agents
- plugin agents when installed
- direct main-session handling

Without a first-class selection-priority owner, the assistant may answer directly or choose a broader fallback even when a visible user custom specialist clearly fits the task.

Observed failure modes this design intends to close:
- the assistant answers directly even when a clear custom specialist exists
- custom user agents are treated like optional edge tools rather than the user’s preferred specialist pool
- built-in or plugin paths absorb specialist tasks too easily
- overlapping teammates are spawned when an existing teammate already covers the same role
- discovery/loading problems are confused with selection behavior among already-visible candidates

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- Selection priority between user custom agents, built-ins, plugins, and direct handling
- Best-fit specialist preference when domain fit is clear
- Reuse-before-spawn guidance when an existing teammate already covers the same role
- Delegation boundaries so custom agents are preferred but not forced
- Distinction between discovery success and selection behavior
- Guidance for when generic handling remains acceptable

### 3.2 Out of Scope
- `CLAUDE.md` edits
- Runtime discovery/loading mechanics for `~/.claude/agents/`
- YAML/frontmatter parsing rules
- Session-start loading behavior
- Hook/settings-based startup health checks or deterministic hook enforcement
- Agent file content design itself beyond what is needed for selection policy
- Plugin implementation, runtime install, or sync into `~/.claude/rules/`

### 3.3 Boundary Principle
This chain owns **how the assistant should prioritize already-available custom agents during task selection**.
It does not claim to own whether the runtime has successfully discovered those agents in the first place.

---

## 4) Custom Agent Priority Model

### 4.1 Primary specialist pool principle
When custom user agents are available and a task clearly matches one of them, treat the user custom-agent pool in `~/.claude/agents/` as the primary specialist pool.

### 4.2 Best-fit before generic principle
If a task has a clear specialist fit:
- prefer the best-fit custom user agent before answering through generic direct handling
- prefer the best-fit custom user agent before built-in or plugin paths that are broader or less user-specific

### 4.3 No forced delegation principle
Do not delegate just because an agent exists.
Delegation should still require:
- a clear domain fit
- a meaningful advantage over direct handling
- no stronger reason to stay local/generic

### 4.3.1 Reuse-before-spawn principle
When a matching teammate or active specialist already covers the same role and objective, reuse that agent before spawning another one.

Required guidance:
- check whether an active or recently spawned teammate already owns materially the same role
- prefer steering or reusing that teammate over creating a duplicate-looking teammate
- only add another teammate when the work is explicitly partitioned and the new role is meaningfully distinct
- use role names that let the user tell why each teammate exists

### 4.4 Discovery boundary principle
If the runtime has not discovered a custom agent in the current session, this chain does not pretend that the agent is available.
The chain governs selection among visible/available candidates, not loader behavior.

---

## 5) Selection Order Contract

When a task arrives, the assistant should reason in this order:

1. Is there a clear best-fit user custom agent in `~/.claude/agents/`?
2. If yes, prefer that agent unless a stronger boundary says otherwise.
3. If not, is there a better-fit project agent, built-in agent, or plugin agent?
4. If no strong specialist advantage exists, use direct handling.

### 5.1 Preferred order when candidates are available
| Candidate Type | Default Priority |
|----------------|------------------|
| Best-fit user custom agent | Highest specialist preference |
| Best-fit project custom agent | High when visible and clearly better fit |
| Best-fit built-in agent | Fallback specialist path |
| Best-fit plugin agent | Fallback specialist or tooling path |
| Direct handling | Default only when no specialist advantage is clear |

### 5.2 Priority caveat
This is a behavioral preference order, not a replacement for runtime discovery precedence.
If an agent is not discovered in the session, it is not a usable candidate.

---

## 6) Delegation Trigger Model

Prefer a custom user agent when all of these are true:
- the task matches the agent’s documented domain strongly
- the agent is visible/available in the current session
- the task would materially benefit from specialist handling
- direct handling would be broader, weaker, or more generic than the specialist path

Do not prefer a custom user agent or new teammate when:
- the task is trivial and delegation adds no real value
- the task is simple, local, and cheaper to handle directly
- the task spans a domain that the specialist explicitly defers
- the runtime has not discovered the agent in the current session
- the user explicitly wants a different path
- an already-active or recently inspected teammate can cover the same role/objective without creating overlapping team noise

---

## 7) Direct Handling vs Specialist Handling

### Direct handling remains acceptable when:
- the task is simple and local
- no specialist clearly improves the outcome
- the question is too broad to map to one specialist cleanly
- the user explicitly asks for direct handling

### Specialist handling is preferred when:
- the domain fit is strong and specific
- the custom agent has clearer boundaries or expertise than the generic path
- the user’s installed specialist pool is obviously intended to own that task family

---

## 8) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| ignoring a clear custom specialist and answering generically | wastes the user’s specialist setup | prefer the best-fit custom agent |
| delegating to any custom agent without strong fit | creates noisy, arbitrary routing | require clear domain fit |
| spawning a second teammate for the same role with no distinct partition | creates duplicate-looking team noise and overlap | reuse the existing teammate or define clearly different roles before spawning |
| treating built-ins/plugins as automatically superior to user custom agents | ignores the user’s installed specialist pool | use custom agents first when fit is clear |
| pretending an undiscovered agent is available | hides real discovery problems | distinguish discovery from selection |
| over-delegating trivial work | adds latency/churn without benefit | keep direct handling for simple tasks |

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Clear-best-fit custom specialist preferred when available | High |
| Generic direct handling despite strong visible custom fit | Low |
| Over-delegation of trivial work | Low |
| Confusion between discovery failure and selection choice | 0 critical cases |
| Built-in/plugin overuse when user specialist is clearly better fit | Low |

---

## 10) Integration

| Rule | Relationship |
|------|--------------|
| [../authority-and-scope.md](../authority-and-scope.md) | User authority still overrides delegation preference when the user chooses another path |
| [../functional-intent-verification.md](../functional-intent-verification.md) | Keeps destructive/expensive execution confirmation separate from delegation choice |
| [../natural-professional-communication.md](../natural-professional-communication.md) | Selection behavior should remain calm and non-theatrical |
| [../anti-sycophancy.md](../anti-sycophancy.md) | Specialist choice should be evidence-based, not performed agreement |

---

> Full history: [../changelog/custom-agent-selection-priority.changelog.md](../changelog/custom-agent-selection-priority.changelog.md)
