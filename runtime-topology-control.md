# Runtime Topology Control
> **Current Version:** 1.1
> **Design:** [design/runtime-topology-control.design.md](design/runtime-topology-control.design.md) v1.1
> **Session:** 77d0802a-fd64-4023-a66d-88c165ccca12
> **Full history:** [changelog/runtime-topology-control.changelog.md](changelog/runtime-topology-control.changelog.md)
---
## Rule Statement
**Core Principle: Preserve runtime clarity by inspecting current topology, locking one authority baseline per role/path, and preferring repair or controlled replacement over additive expansion unless the user explicitly approves a topology change.**
This rule governs runtime mutation posture without replacing safety, authority, anti-guessing, or failure-handling rules.
---
## Core Contract
1. **Stability over expansion:** unknown runtime state is a reason to inspect, not add more runtime parts.
2. **One authority at a time:** keep one authoritative runtime owner per role/path unless the user explicitly wants multi-authority topology; one authority does not mean one instance total.
3. **Inspect-before-mutate:** identify current entities, authority baseline, ambiguous/conflicting authorities, and unknown-vs-empty state before topology change.
4. **Replace over accumulate:** prefer `REPAIR_IN_PLACE` or controlled `REPLACEMENT_MUTATION` over additive parallel paths; this is not destructive permission.
5. **Explicit topology delta:** classify the step before acting and state whether it changes authority or enters multi-authority mode.
6. **Approval gate:** `ADDITIVE_EXPANSION`, authority-baseline changes, multi-authority mode, and destructive/high-blast-radius repair/replacement require explicit approval or stronger confirmation owner.
7. **Explicit multi-authority exception:** scaling, HA, canary, compare, shadow, or user-requested parallel authorities are valid only with purpose, authority boundaries, and retirement/steady-state plan.
---
## Trigger Model
- Unclear topology: inspect current entities and authority baseline before mutating.
- Conflicting authorities: stop and clarify owner per role/path.
- Starting another server/container/worker/target: classify as `ADDITIVE_EXPANSION`, justify, and request approval.
- Restarting/rebinding/swapping current owner: declare replacement delta and rollback direction first.
- Scaling/HA/canary/compare/shadow: enter explicit multi-authority mode with boundaries.
- Temporary debug runtime: define retirement plan before creation.
- Post-mutation success claim: verify topology and checked scope before claiming success.
---
## Vocabulary and Delta Classes
Key terms:
- `runtime entity` = runnable unit such as container, server process, target, worker, proxy, background job, or assignment endpoint
- `runtime role` = logical job for a path/workflow/capability
- `runtime authority` = layer authoritative for what should run for a role/path
- `topology-changing action` = creates, removes, replaces, reassigns, duplicates, or reroutes runtime entities
- `repair-in-place` = corrects existing path/entity without parallel owner
- `replacement mutation` = swaps current owner in a controlled way
- `additive expansion` = adds entities or parallel paths beyond current topology
- `explicit multi-authority mode` = deliberate user-approved parallel authorities for scaling/HA/canary/compare/shadow

| Class | Meaning | Default posture |
|---|---|---|
| `OBSERVE_ONLY` | inspect/report without mutation | default until gates pass |
| `REPAIR_IN_PLACE` | correct current topology without parallel owner | preferred when feasible |
| `REPLACEMENT_MUTATION` | replace/swap current owner in bounded way | allowed when justified/safe |
| `ADDITIVE_EXPANSION` | create additional entities/parallel paths | blocked until justified/approved |

Mutation gate: before mutating, identify current entities, authority baseline, ambiguities, delta class, multi-authority state, authorization, and rollback/retirement direction. If any gate is missing, remain `OBSERVE_ONLY` and request evidence/input.
---
## Communication Contract
When topology control matters, report:
```text
topology_posture: <OBSERVE_ONLY | REPAIR_IN_PLACE | REPLACEMENT_MUTATION | ADDITIVE_EXPANSION>
current_entities:
- ...
authority_baseline: <owner per role/path>
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
Separate observed topology facts from inferred causes, proposed from approved mutations, and scoped non-findings from absence claims. After mutation, state what was rechecked before success wording.
---
## Boundaries and Verification
Allowed: stay `OBSERVE_ONLY`, use bounded repair/replacement, or use explicit multi-authority mode when selected.

Not allowed: debug-by-expansion, accidental parallel authority, implicit authority switch, temporary runtime without retirement plan, silent delta escalation, unapproved additive expansion, global absence from scoped non-finding, or unsupported “topology fixed” claims.

Verification checklist:
- [ ] current runtime entities and authority baseline identified before mutation
- [ ] topology delta classified
- [ ] additive/authority-changing actions have explicit approval
- [ ] multi-authority mode has purpose, boundaries, and retirement/steady-state plan
- [ ] post-mutation success claim cites checked scope
---
## Integration
Related rules: `functional-intent-verification.md` owns confirmation/blast-radius gates; `authority-and-scope.md` owns precedence; `no-variable-guessing.md` owns inspected-scope facts; `accurate-communication.md` owns claim strength; `operational-failure-handling.md` owns retry/cooldown escalation.
---
