# Runtime Topology Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** 77d0802a-fd64-4023-a66d-88c165ccca12 (2026-03-14)

---

## 1) Goal

Define one first-class rule chain for runtime topology mutation posture so runtime changes stay controlled, authority-aligned, and resistant to debug-by-expansion across containers, runtime targets, local dev servers, background jobs, workers, proxies, and similar runtime entities.

The target behavior is principle-first:
- preserve controlled topology evolution over exploratory expansion
- inspect current runtime state before mutating topology
- keep one authority baseline per role/path by default
- prefer replacement or consolidation over additive accumulation
- require explicit approval before topology-changing actions

---

## 2) Problem Statement

Runtime work drifts when unclear state is answered with expansion instead of inspection.

Observed failure patterns:
- starting another container, server, target, worker, or proxy “just to test” before verifying the current owner
- creating parallel authorities accidentally while debugging
- treating unknown current state as permission to expand topology
- switching authority baselines implicitly mid-debugging
- leaving temporary runtime entities behind with no retirement plan
- claiming runtime topology is fixed without verifying the post-mutation state

Without a dedicated topology-control chain, adjacent rules can enforce safety, authority, and evidence quality while still leaving runtime mutation posture under-specified.

---

## 3) Scope and Non-Goals

### In Scope
- Runtime-topology mutation posture and sequencing discipline.
- Inventory-first reasoning about current runtime entities before topology mutation.
- Authority-baseline declaration per runtime role/path.
- Classification of topology deltas as inspect-only, repair-in-place, replacement mutation, or additive expansion.
- Explicit handling of deliberate multi-authority runtime modes.
- Approval sensitivity for topology-changing actions.
- Topology-specific reporting obligations before and after mutation.

### Out of Scope
- Retry classes, cooldown policy, and failure ceilings (owned by `operational-failure-handling`).
- Local path/config lookup mechanics (owned by `no-variable-guessing`).
- Generic evidence phrasing and claim-strength policy (owned by `accurate-communication`).
- Global precedence hierarchy (owned by `authority-and-scope`).
- Generic confirmation mechanics (owned by `functional-intent-verification`).
- Refusal taxonomy or emergency-mode behavior.

### Boundary Statement
This chain owns runtime-topology mutation posture only.
It does not redefine refusal, emergency, authority, retry, or general communication frameworks.

---

## 4) Runtime Topology Model

| Term | Meaning |
|------|---------|
| `runtime entity` | A concrete running or runnable unit such as a container, server process, runtime target, worker, proxy, background job, or assignment endpoint |
| `runtime role` | The logical job a runtime entity performs for a path, workflow, or capability |
| `runtime authority` | The layer that is currently authoritative for what should run for a given role/path |
| `topology-changing action` | Any action that creates, removes, replaces, reassigns, duplicates, or reroutes runtime entities |
| `repair-in-place` | Correcting an existing runtime entity/path without creating a parallel runtime owner |
| `replacement mutation` | Swapping or replacing the current runtime owner in a controlled way |
| `additive expansion` | Creating additional runtime entities or parallel runtime paths beyond the current topology |
| `explicit multi-authority mode` | A deliberate, user-approved state where parallel authorities are intentionally allowed for a bounded purpose such as scaling, HA, canary, compare, or shadow execution |

Authority model notes:
- **One authority at a time** means one authoritative owner per role/path by default, not one runtime instance total.
- Multiple instances may exist under one explicit authority without violating this rule.
- If multiple authorities are intentional, the change must enter explicit multi-authority mode rather than happening accidentally through debugging drift.

---

## 5) Core Principles

### 5.1 Stability-Over-Expansion Principle
Do not trade clarity for momentum by adding more runtime parts before the current topology is understood.

Required guidance:
- treat unknown runtime state as a reason to inspect, not a reason to expand
- stabilize the currently relevant topology before exploring alternatives
- prefer fewer moving runtime parts when the goal is diagnosis rather than scaling

### 5.2 One-Authority-At-A-Time Principle
Keep one authoritative runtime owner per role/path by default unless the user explicitly wants a multi-authority topology.

Required guidance:
- identify which layer is authoritative for what should run
- do not let topology mutation implicitly switch authority baseline
- enter explicit multi-authority mode before allowing deliberate parallel authorities
- do not interpret this principle as a ban on multiple instances under one explicit authority

### 5.3 Inspect-Before-Mutate Principle
Inventory, map, and verify the existing runtime state before any topology-changing action.

Required guidance:
- identify current relevant runtime entities before mutation
- identify the active authority baseline per role/path
- surface ambiguous or conflicting authorities explicitly
- distinguish unknown state from empty state

### 5.4 Replace-Over-Accumulate Principle
When change is needed, prefer repair-in-place or controlled replacement over additive accumulation of parallel runtime paths.

Required guidance:
- prefer repair-in-place or replacement mutation when they satisfy the objective safely
- justify additive expansion only when replacement or consolidation is insufficient
- do not read this principle as permission for destructive replacement without approval

### 5.5 Explicit-Topology-Delta Principle
If a topology change is proposed, state the delta clearly.

Required guidance:
- classify the step as `OBSERVE_ONLY`, `REPAIR_IN_PLACE`, `REPLACEMENT_MUTATION`, or `ADDITIVE_EXPANSION`
- say explicitly when the step also changes authority baseline or enters explicit multi-authority mode
- do not silently escalate from a smaller delta class into a larger one

### 5.6 Approval-Gated Topology Change Principle
Additive or authority-changing topology actions require explicit user approval.

Required guidance:
- require explicit approval before additive expansion
- require explicit approval before authority-baseline changes that alter the active owner for a role/path
- treat high-blast-radius repair/replacement as confirmation-sensitive
- keep confirmation mechanics delegated to `functional-intent-verification`

### 5.7 Explicit Multi-Authority Exception Principle
Scaling, HA, canary, compare, shadow, or user-requested parallel authorities are valid exceptions, but they must be explicit rather than accidental.

Required guidance:
- require a stated purpose for parallel authorities
- require explicit authority boundaries for the multi-authority state
- require a retirement plan or steady-state plan before creating temporary parallel topology
- do not allow multi-authority mode to emerge implicitly from debugging drift

---

## 6) Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Required Action |
|--------|-----------------|-----------------|
| unclear current topology | unknown owner, stale runtime state, unclear active unit | inspect current runtime entities and authority baseline before mutating |
| conflicting authorities | two or more plausible sources of truth for the same role/path | stop and clarify authority before topology change |
| proposal to start another runtime unit | “spin up another container/server/worker/target to test” | classify as additive expansion and require justification + approval |
| proposal to replace an existing unit | restart, rebind, swap current owner, move assignment | declare replacement delta and local rollback direction first |
| deliberate parallel-runtime request | scaling, HA, canary, compare, shadow, side-by-side validation | enter explicit multi-authority mode and define purpose + boundaries |
| temporary debug runtime | short-lived extra runtime for investigation | require explicit retirement plan before creation |
| post-mutation success claim | “fixed”, “aligned”, “working now” | verify post-mutation topology and report checked scope before claiming success |

---

## 7) Topology Mutation Classes

| Class | Meaning | Default Posture |
|------|---------|-----------------|
| `OBSERVE_ONLY` | Inspect and report current runtime topology without mutation | default until mutation gates are satisfied |
| `REPAIR_IN_PLACE` | Correct the current runtime topology without creating a parallel owner | preferred when feasible |
| `REPLACEMENT_MUTATION` | Replace or swap the current runtime owner in a controlled way | allowed when justified and bounded |
| `ADDITIVE_EXPANSION` | Create additional runtime entities or parallel runtime paths | blocked until justified and explicitly approved |

Classification notes:
- classify the delta before mutation recommendation
- if the correct class is uncertain, default to `OBSERVE_ONLY`
- do not silently shift from `REPAIR_IN_PLACE` to `ADDITIVE_EXPANSION`
- explicit multi-authority mode is a runtime mode layered on top of the chosen delta class, not a silent default

---

## 8) Approval and Change Gate

Before mutating runtime topology, identify all of the following:
- current relevant runtime entities
- active authority baseline per role/path
- ambiguous or conflicting authorities
- proposed delta class
- whether explicit multi-authority mode is being entered
- whether the user has explicitly authorized the topology change
- rollback or retirement direction for the current step

Gate behavior:
- `OBSERVE_ONLY` requires no topology-change approval.
- `REPAIR_IN_PLACE` or `REPLACEMENT_MUTATION` may proceed only when requested scope is clear, authority baseline is explicit, and no higher-risk confirmation rule blocks the action.
- `ADDITIVE_EXPANSION` requires explicit justification plus explicit user approval.
- Explicit multi-authority mode requires explicit user approval plus a stated purpose and boundary plan.
- Destructive or high-blast-radius steps still defer to `functional-intent-verification` for confirmation mechanics.

---

## 9) Communication Contract

When topology mutation is materially relevant, communication should expose:

```text
topology_posture: <OBSERVE_ONLY | REPAIR_IN_PLACE | REPLACEMENT_MUTATION | ADDITIVE_EXPANSION>
current_entities:
- ...
authority_baseline: <authoritative layer for this objective>
ambiguous_authorities:
- ...
proposed_delta:
- ...
approval_state: <not needed | pending approval | approved>
checked_scope:
- ...
risk_notes:
- ...
what_can_be_done_now:
- ...
how_to_proceed:
- ...
```

Communication requirements:
- separate observed topology facts from inferred causes
- separate proposed mutations from approved mutations
- state explicitly when expansion or explicit multi-authority mode is pending user approval
- report checked scope honestly rather than turning local non-findings into stronger absence claims
- after mutation, state what was re-checked before claiming success

---

## 10) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| debug-by-expansion | multiplies topology drift and diagnosis noise | inspect and stabilize existing topology first |
| accidental parallel authority | creates hidden conflicts about what should run | keep one authority baseline per role/path by default |
| implicit authority switch | changes runtime ownership without explicit decision | declare the authority baseline before mutation |
| temporary runtime without retirement plan | leaves stale runtime debris behind | define retirement or steady-state plan before creation |
| silent delta escalation | turns repair into expansion without user awareness | state the exact topology delta before acting |
| unsupported “topology fixed” claim | overstates completion confidence | verify post-mutation state and report checked scope |

---

## 11) Quality Metrics

| Metric | Target |
|--------|--------|
| Inspect-before-mutate adherence | 100% |
| Authority-baseline clarity | High |
| Unjustified additive expansion | 0 critical cases |
| Accidental multi-authority drift | 0 critical cases |
| Topology-delta clarity before mutation | High |
| Post-mutation verification clarity | High |
| Unsupported “topology fixed” claims | 0 critical cases |

---

## 12) Integration

| Document | Relationship |
|----------|--------------|
| [../runtime-topology-control.md](../runtime-topology-control.md) | Runtime implementation of this design |
| [functional-intent-verification.design.md](functional-intent-verification.design.md) | Keeps confirmation mechanics and blast-radius confirmation external to this chain |
| [authority-and-scope.design.md](authority-and-scope.design.md) | Keeps precedence hierarchy and authority override semantics external to this chain |
| [no-variable-guessing.design.md](no-variable-guessing.design.md) | Keeps inspected-scope local evidence lookup discipline external to this chain |
| [accurate-communication.design.md](accurate-communication.design.md) | Keeps claim-strength wording aligned with verified topology state |
| [operational-failure-handling.design.md](operational-failure-handling.design.md) | Keeps retry, cooldown, and escalation policy separate when topology actions fail |

---

> Full history: [../changelog/runtime-topology-control.changelog.md](../changelog/runtime-topology-control.changelog.md)
