# Custom Agent Selection Priority

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-04)

---

## 1) Goal

Define one first-class rule chain for custom agent selection priority so the assistant:
- treats visible user custom agents in `~/.claude/agents/` as the primary specialist pool when they are available
- prefers the best-fit custom specialist before generic handling when a task clearly matches the worker capability selected by native routing
- keeps delegation selective and justified rather than forcing agents into every task
- uses this chain after worker routing determines intent, required capability, and worker scale
- prefers reuse-before-spawn when an existing worker already covers the same role
- separates discovery/loading concerns from selection/invocation concerns

This chain should improve real custom-agent usage without pretending that runtime discovery itself is controlled by prompt rules.

---

## 2) Problem Statement

The system can have several candidate handling paths:
- user custom agents in `~/.claude/agents/`
- project-visible agents
- built-in agents
- plugin agents when installed
- non-specialist standalone worker lanes
- direct main-session handling

Without a first-class selection-priority owner, the assistant may answer directly or choose a broader fallback even when a visible user custom specialist clearly fits the needed capability.

Observed failure modes this design intends to close:
- the assistant answers directly even when a clear custom specialist exists after worker routing selected specialist handling
- custom user agents are treated like optional edge tools rather than the user’s preferred specialist pool
- built-in or plugin paths absorb specialist tasks too easily
- overlapping workers are spawned when an existing worker already covers the same role
- discovery/loading problems are confused with selection behavior among already-visible candidates
- custom-agent availability is treated as the worker-routing decision instead of a downstream specialist-selection input
- specialist selection accidentally escalates standalone subagent-fit work into Agent Team workflow

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- Selection priority between user custom agents, built-ins, plugins, non-specialist worker lanes, and direct handling
- Best-fit specialist preference when domain/capability fit is clear
- Reuse-before-spawn guidance when an existing worker already covers the same role
- Delegation boundaries so custom agents are preferred but not forced
- Distinction between discovery success and selection behavior
- Guidance for when generic handling remains acceptable

### 3.2 Out of Scope
- Intent classification and worker-scale routing
- Agent Team escalation decisions
- `CLAUDE.md` edits
- Runtime discovery/loading mechanics for `~/.claude/agents/`
- YAML/frontmatter parsing rules
- Session-start loading behavior
- Hook/settings-based startup health checks or deterministic hook enforcement
- Agent file content design itself beyond what is needed for selection policy
- Plugin implementation, runtime install, or sync into `~/.claude/rules/`

### 3.3 Boundary Principle
This chain owns **how the assistant should prioritize already-available custom agents during task selection after worker routing selects delegation or specialist handling and identifies the required capability**.
It does not claim to own whether the runtime has successfully discovered those agents in the first place, and it does not own intent classification, broad-work worker-scale routing, Agent Team escalation, or leader-context control.

---

## 4) Custom Agent Priority Model

### 4.1 Primary specialist pool principle
When custom user agents are available and a task clearly matches one of them, treat the user custom-agent pool in `~/.claude/agents/` as the primary specialist pool.

### 4.2 Capability-fit before generic principle
If worker routing identifies a needed capability and a task has a clear specialist fit:
- prefer the best-fit custom user agent before answering through generic direct handling
- prefer the best-fit custom user agent before built-in or plugin paths that are broader or less user-specific
- select by task capability and domain fit rather than by exact tool-name mapping

### 4.3 No forced delegation principle
Do not delegate just because an agent exists.
Delegation should still require:
- worker routing has already selected delegation or specialist handling
- a clear domain/capability fit
- a meaningful advantage over direct handling
- no stronger reason to stay local/generic

### 4.3.1 Routing-before-selection principle
Worker routing and custom-agent selection are separate layers.

Required guidance:
- `native-worker-agent-routing-and-context-control.md` decides intent, required worker capability, and direct leader / subagent / multi-subagent / Agent Team scale
- this chain chooses the best visible specialist/custom agent after that route is appropriate
- custom-agent availability alone must not become proof that delegation is the correct worker scale
- this chain must not be used to escalate subagent-fit work into Agent Team workflow

### 4.3.2 Reuse-before-spawn principle
When a matching worker or active specialist already covers the same role and objective, reuse that agent before spawning another one.

Required guidance:
- check whether an active or recently spawned worker already owns materially the same role
- prefer steering or reusing that worker over creating a duplicate-looking worker
- only add another worker when the work is explicitly partitioned and the new role is meaningfully distinct
- use role names that let the user tell why each worker exists

### 4.4 Discovery boundary principle
If the runtime has not discovered a custom agent in the current session, this chain does not pretend that the agent is available.
The chain governs selection among visible/available candidates, not loader behavior.

---

## 5) Selection Order Contract

After worker routing determines that delegation or specialist handling is appropriate, the assistant should reason in this order:

1. What worker capability and domain scope did routing select?
2. Is there a clear best-fit user custom agent in `~/.claude/agents/` for that capability?
3. If yes, prefer that agent unless a stronger boundary selects another worker path.
4. If not, is there a better-fit project agent, built-in agent, or plugin agent?
5. If no strong specialist advantage exists, return to direct handling or the non-specialist worker path selected by routing.

### 5.1 Preferred order when candidates are available
| Candidate Type | Default Priority |
|----------------|------------------|
| Best-fit user custom agent | Highest specialist preference |
| Best-fit project custom agent | High when visible and clearly better fit |
| Best-fit built-in agent | Fallback specialist path |
| Best-fit plugin agent | Fallback specialist or tooling path |
| Non-specialist standalone worker lane | Default when context isolation matters but no specialist fit exists |
| Direct handling | Default only when no worker or specialist advantage is clear |

### 5.2 Priority caveat
This is a behavioral preference order, not a replacement for runtime discovery precedence.
If an agent is not discovered in the session, it is not a usable candidate.

---

## 6) Delegation Trigger Model

Prefer a custom user agent when all of these are true:
- worker routing selected delegation or specialist handling
- the selected path needs the agent’s capability
- the task matches the agent’s documented domain strongly
- the agent is visible/available in the current session
- the task would materially benefit from specialist handling
- direct handling would be broader, weaker, or more generic than the specialist path

Do not prefer a custom user agent or new worker when:
- the task is trivial and delegation adds no real value
- the task is simple, local, and cheaper to handle directly
- the task spans a domain that the specialist explicitly defers
- the runtime has not discovered the agent in the current session
- the user explicitly wants a different path
- the user has banned the relevant worker mechanism broadly enough to include that agent type
- an already-active or recently inspected worker can cover the same role/objective without creating overlap
- selection would unnecessarily escalate a standalone subagent-fit task into Agent Team workflow

---

## 7) Direct Handling vs Specialist Handling

### Direct handling remains acceptable when:
- the task is simple and local
- no specialist clearly improves the outcome
- the question is too broad to map to one specialist cleanly
- the user explicitly asks for direct handling

### Specialist handling is preferred when:
- worker routing has selected a delegated or specialist path
- the required capability/domain fit is strong and specific
- the custom agent has clearer boundaries or expertise than the generic path
- the user’s installed specialist pool is obviously intended to own that task family

---

## 8) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| ignoring a clear custom specialist and answering generically after delegation is appropriate | wastes the user’s specialist setup | prefer the best-fit custom agent |
| delegating to any custom agent without strong capability fit | creates noisy, arbitrary routing | require clear domain/capability fit |
| using custom-agent availability as the routing decision | confuses worker-scale routing with specialist selection | let `native-worker-agent-routing-and-context-control.md` decide intent, capability, and worker scale first |
| escalating subagent-fit work into Agent Team workflow from selection logic | over-tasks a small worker lane | leave Agent Team escalation to worker routing and require real coordination need |
| spawning a second worker for the same role with no distinct partition | creates duplicate-looking noise and overlap | reuse the existing worker or define clearly different roles before spawning |
| treating built-ins/plugins as automatically superior to user custom agents | ignores the user’s installed specialist pool | use custom agents first when fit is clear |
| pretending an undiscovered agent is available | hides real discovery problems | distinguish discovery from selection |
| over-delegating trivial work | adds latency/churn without benefit | keep direct handling for simple tasks |

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Clear-best-fit custom specialist preferred when available | High |
| Capability-fit specialist selection | High |
| Generic direct handling despite strong visible custom fit after delegation is appropriate | Low |
| Over-delegation of trivial work | Low |
| Agent Team escalation caused by selection rule alone | 0 critical cases |
| Confusion between routing and specialist selection | 0 critical cases |
| Confusion between discovery failure and selection choice | 0 critical cases |
| Built-in/plugin overuse when user specialist is clearly better fit | Low |

---

## 10) Integration

| Rule | Relationship |
|------|--------------|
| [../native-worker-agent-routing-and-context-control.md](../native-worker-agent-routing-and-context-control.md) | Owns intent, required worker capability, worker-scale routing, and leader-context control before this chain selects a best-fit specialist |
| [../authority-and-scope.md](../authority-and-scope.md) | User authority still overrides delegation preference when the user chooses another path |
| [../functional-intent-verification.md](../functional-intent-verification.md) | Keeps destructive/expensive execution confirmation separate from delegation choice |
| [../natural-professional-communication.md](../natural-professional-communication.md) | Selection behavior should remain calm and non-theatrical |
| [../anti-sycophancy.md](../anti-sycophancy.md) | Specialist choice should be evidence-based, not performed agreement |

---

> Full history: [../changelog/custom-agent-selection-priority.changelog.md](../changelog/custom-agent-selection-priority.changelog.md)
