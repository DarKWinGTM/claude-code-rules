# Design - Goal Authoring and Route Support

> **Parent Rule:** [../goal-authoring-and-route-support.md](../goal-authoring-and-route-support.md)
> **Current Version:** 1.3
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/goal-authoring-and-route-support.changelog.md](../changelog/goal-authoring-and-route-support.changelog.md)

---

## Target State

`goal-authoring-and-route-support.md` is the active runtime owner for governed `/goal` authoring, route-support extraction, `Plan reference` discipline, and selected-goal overflow handling into `/plan`.

It separates detailed goal-authoring doctrine from execution continuity and phase/task shaping so the runtime layer can stay compact without duplicating the same `/goal` contract across several root rules. It encodes execution- or user-selected proof layering and route-prerequisite ordering without independently deciding whether a proof obligation belongs to the current goal or a successor.

---

## Scope

This design owns the target-state shape for:
- plain governed goal request handling
- governed-surface sourcing order for `/goal`
- bounded goal artifact construction
- required, current-reachable, and explicitly excluded-or-successor proof-layer construction
- route-prerequisite ordering and explicitly selected terminal-proof preservation
- smallest-sufficient route support
- durable `Plan reference` validity
- subordinate internal helper / route-support behavior
- goal-authoring stop boundaries
- construction of an execution-selected advisory `/goal`
- selected-goal overflow into `/plan`
- `/goal` versus `/plan` authority separation

---

## Runtime Requirements

- Receive direct/candidate/advisory posture from `execution-and-goal-frame.md`; do not independently promote a candidate.
- Keep `/goal` as the objective owner for outcome, proof/checks, scope, and hard guardrails.
- Encode the selected `required_proof_layer`, material `current_reachable_layer`, and explicitly classified excluded or successor layers only when those distinctions affect the goal.
- Evaluate proposed done points before Goal emission against scope, current environment, capability, approval, and an observable proof path; assistant-authored source/code Goals default to a terminal gate with a credible executable path inside the selected scope and currently available or approvable capability rather than an unclosable external dependency.
- For source/code goals, prohibit assistant inference from turning generic completion or verification wording into live Product acceptance; live proof stays excluded or successor unless the user or checked governed authority explicitly selects it.
- Classify proof from explicit done conditions, proof/checks, scope, and checked governing authority rather than operational nouns or Product-facing capability names; implementing diagnostics, deployment-support, recovery, or mutation-capable code does not select live execution or mutation proof by itself.
- Preserve an explicitly selected terminal proof as binding; expose prerequisite or blocker gaps instead of demoting it.
- Repair an assistant-inferred infeasible done point in place when checked evidence shows the current scope cannot close it and no user/governed authority selected it; move the proof to excluded or successor scope without restarting the Goal or looping, while treating difficulty, duration, or remaining implementation work alone as insufficient evidence of infeasibility.
- Order capability and state prerequisites before dependent proof and prevent unchanged checks that cannot add signal.
- Require route support to map planned slices to output, gate, and reachability; the current plan ends at the selected Goal proof while excluded or successor operations stay outside the blocking sequence unless explicitly selected.
- Repair infeasible assistant-authored plan gates in place with the Goal boundary rather than making `/plan` a second objective or forcing a replacement Goal.
- Keep `/plan` as route-only support when overflow route detail or explicit standalone planning is materially needed.
- Keep route-only plan files from reading like completion proof.
- Keep phase/task materialization and execution posture outside this owner.
- Keep metadata linked to this design and the chain changelog.

---

## Boundaries

This design does not own discussion-versus-execution mode selection, continuous execution, next-goal bridge logic, or the decision that proof belongs to the current goal versus a successor; those remain with `execution-and-goal-frame.md` and direct user selection.

It does not own approval, authenticated/private access, or consequential external-action gates; those remain with `action-safety.md`. Evidence-strength and completion-status wording remain with `accurate-communication.md`.

It does not own startup artifact posture, phase/TODO linkage, or live task materialization; those remain with `phase-todo-artifact.md`.

Historical detail remains in changelog, not as a parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, links to this design and its changelog, ships in the active runtime install set when install is in scope, and leaves `execution-and-goal-frame.md` plus `phase-todo-artifact.md` with only their execution/task-surface bridges instead of the full duplicated `/goal` authoring contract.

Case 17 M30/M31/M33/M34 validation must confirm that proposed done points receive a feasibility/reachability check before Goal emission; a source-bounded goal can close at its selected reachable source/local proof while Product proof remains a prerequisite-bearing successor; generic `complete`, `verify`, `working`, or `done` wording and operational capability names such as pinned-host SSH diagnostics or an exact-request recovery path do not select live proof; an assistant-inferred infeasible done point is repaired in place rather than causing a new-Goal or retry loop; only the user or checked governed authority can explicitly keep authenticated live proof as the terminal gate; route prerequisites precede dependent live proof; and simple goals remain compact without mandatory proof-layer ceremony.

---

## P073-12 Runtime Compaction Refinement

Compact Integration and cross-owner consumer wording to canonical owner pointers while preserving activation, local consequence, exact error-prevention literals, body sufficiency, and every existing safety, verification, approval, and stop gate.
