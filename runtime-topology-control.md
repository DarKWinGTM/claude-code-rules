# Runtime Topology Control

> **Current Version:** 1.1
> **Design:** [design/runtime-topology-control.design.md](design/runtime-topology-control.design.md) v1.1
> **Session:** 77d0802a-fd64-4023-a66d-88c165ccca12
> **Full history:** [changelog/runtime-topology-control.changelog.md](changelog/runtime-topology-control.changelog.md)

---

## Rule Statement

**Core Principle: Preserve runtime clarity by inspecting current topology, locking one authority baseline per role/path, and preferring replacement or consolidation over additive expansion unless the user explicitly approves a topology change.**

This rule governs runtime mutation posture and topology discipline. It complements adjacent safety, authority, and failure-handling rules, but does not replace their authority.

---

## Core Principles

### 1) Stability-Over-Expansion Principle
Do not trade topology clarity for momentum by adding runtime parts before the current topology is understood.

Required guidance:
- treat unknown runtime state as a reason to inspect, not a reason to expand
- stabilize the existing topology before exploring additive alternatives
- avoid topology growth as a default debugging move

### 2) One-Authority-At-A-Time Principle
Keep one authoritative runtime owner per role/path by default unless the user explicitly wants a multi-authority topology.

Required guidance:
- identify which layer is authoritative for what should run
- do not let topology mutation implicitly switch authority baseline
- enter explicit multi-authority mode before allowing deliberate parallel authorities
- do not confuse one authority with one runtime instance total

### 3) Inspect-Before-Mutate Principle
Inventory, map, and verify the existing runtime state before any topology-changing action.

Required guidance:
- identify current relevant runtime entities before mutation
- identify the active authority baseline per role/path
- surface ambiguous or conflicting authorities explicitly
- distinguish unknown state from empty state

### 4) Replace-Over-Accumulate Principle
When change is needed, prefer repair-in-place or controlled replacement over additive accumulation of parallel runtime paths.

Required guidance:
- prefer `REPAIR_IN_PLACE` or `REPLACEMENT_MUTATION` when they satisfy the objective safely
- justify additive expansion only when replacement or consolidation is insufficient
- do not read this principle as permission for destructive replacement without approval

### 5) Explicit-Topology-Delta Principle
If a topology change is proposed, state the delta clearly.

Required guidance:
- classify the step as `OBSERVE_ONLY`, `REPAIR_IN_PLACE`, `REPLACEMENT_MUTATION`, or `ADDITIVE_EXPANSION`
- say explicitly when the step also changes authority baseline or enters explicit multi-authority mode
- do not silently escalate from a smaller delta class into a larger one

### 6) Approval-Gated Topology Change Principle
Additive or authority-changing topology actions require explicit user approval.

Required guidance:
- require explicit approval before additive expansion
- require explicit approval before authority-baseline changes that alter the active owner for a role/path
- treat high-blast-radius repair/replacement as confirmation-sensitive
- keep confirmation mechanics delegated to `functional-intent-verification.md`

### 7) Explicit Multi-Authority Exception Principle
Scaling, HA, canary, compare, shadow, or user-requested parallel authorities are valid exceptions, but they must be explicit rather than accidental.

Required guidance:
- require a stated purpose for parallel authorities
- require explicit authority boundaries for the multi-authority state
- require a retirement plan or steady-state plan before creating temporary parallel topology
- do not allow multi-authority mode to emerge implicitly from debugging drift

---

## Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Required Action |
|--------|-----------------|-----------------|
| unclear current topology | unknown owner, stale runtime state, unclear active unit | inspect current runtime entities and authority baseline before mutating |
| conflicting authorities | two or more plausible sources of truth for the same role/path | stop and clarify authority before topology change |
| proposal to start another runtime unit | “spin up another container/server/worker/target to test” | classify as `ADDITIVE_EXPANSION` and require justification + approval |
| proposal to replace an existing unit | restart, rebind, swap current owner, move assignment | declare replacement delta and local rollback direction first |
| deliberate parallel-runtime request | scaling, HA, canary, compare, shadow, side-by-side validation | enter explicit multi-authority mode and define purpose + boundaries |
| temporary debug runtime | short-lived extra runtime for investigation | require explicit retirement plan before creation |
| post-mutation success claim | “fixed”, “aligned”, “working now” | verify post-mutation topology and report checked scope before claiming success |

---

## Topology Mutation Contract

### Runtime Topology Vocabulary

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

### Delta Classes

| Class | Meaning | Default Posture |
|------|---------|-----------------|
| `OBSERVE_ONLY` | Inspect and report current runtime topology without mutation | default until mutation gates are satisfied |
| `REPAIR_IN_PLACE` | Correct the current runtime topology without creating a parallel owner | preferred when feasible |
| `REPLACEMENT_MUTATION` | Replace or swap the current runtime owner in a controlled way | allowed when justified and bounded |
| `ADDITIVE_EXPANSION` | Create additional runtime entities or parallel runtime paths | blocked until justified and explicitly approved |

### Mutation Gate

Before mutating runtime topology, identify all of the following:
- current relevant runtime entities
- active authority baseline per role/path
- ambiguous or conflicting authorities
- proposed delta class
- whether explicit multi-authority mode is being entered
- whether the user has explicitly authorized the topology change
- rollback or retirement direction for the current step

If one or more gates are missing, default to `OBSERVE_ONLY` and request the missing input or evidence.

### Explicit Multi-Authority Mode

Explicit multi-authority mode is valid only for deliberate scaling, HA, canary, compare, shadow, or other user-requested parallel-authority topologies.

Required guidance:
- state why parallel authorities are needed
- state which authority owns which role/path
- state the retirement plan or steady-state plan before creating temporary parallel topology

---

## Approval-Sensitive Actions

This rule marks the following actions as approval-sensitive:
- `ADDITIVE_EXPANSION`
- authority-changing topology mutations
- entering explicit multi-authority mode
- destructive or high-blast-radius repair/replacement steps

Additional guidance:
- `OBSERVE_ONLY` requires no topology-change approval.
- `REPAIR_IN_PLACE` or `REPLACEMENT_MUTATION` may proceed only when requested scope is clear, authority baseline is explicit, and no higher-risk confirmation rule blocks the action.
- Confirmation mechanics remain owned by `functional-intent-verification.md`.

---

## Communication Contract

When topology-mutation control is materially relevant, use this schema:

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

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| debug-by-expansion | multiplies topology drift and diagnosis noise | inspect and stabilize existing topology first |
| accidental parallel authority | creates hidden conflicts about what should run | keep one authority baseline per role/path by default |
| implicit authority switch | changes runtime ownership without explicit decision | declare the authority baseline before mutation |
| temporary runtime without retirement plan | leaves stale runtime debris behind | define retirement or steady-state plan before creation |
| silent delta escalation | turns repair into expansion without user awareness | state the exact topology delta before acting |
| unsupported “topology fixed” claim | overstates completion confidence | verify post-mutation state and report checked scope |

---

## Flexibility Boundary

Allowed flexibility:
- remain at `OBSERVE_ONLY` when uncertainty is material
- choose `REPAIR_IN_PLACE` or `REPLACEMENT_MUTATION` when that preserves clarity and rollback better than expansion
- use explicit multi-authority mode when the user clearly wants scaling, HA, canary, compare, shadow, or another deliberate parallel-authority topology

Not allowed:
- `ADDITIVE_EXPANSION` without explicit justification and approval
- implicit authority switching during topology mutation
- temporary runtime creation without a retirement or steady-state plan
- turning not-found-in-checked-scope into proof that topology is absent
- claiming topology is fixed without post-mutation verification

---

## Quality Metrics

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

## Integration

Related rules:
- [functional-intent-verification.md](functional-intent-verification.md) - keeps confirmation mechanics and blast-radius confirmation external to this chain
- [authority-and-scope.md](authority-and-scope.md) - keeps precedence hierarchy and authority override semantics external to this chain
- [no-variable-guessing.md](no-variable-guessing.md) - keeps inspected-scope topology facts verified from checked local evidence without guesswork
- [accurate-communication.md](accurate-communication.md) - keeps claim strength aligned with verified topology state
- [operational-failure-handling.md](operational-failure-handling.md) - keeps retry, cooldown, and escalation policy separate when topology actions fail

---
