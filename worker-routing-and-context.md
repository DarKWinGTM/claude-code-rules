# Worker Routing and Context Control
> **Current Version:** 1.18
> **Design:** [design/worker-routing-and-context.design.md](design/worker-routing-and-context.design.md) v1.18
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/worker-routing-and-context.changelog.md](changelog/worker-routing-and-context.changelog.md)

## Rule Statement

**Core Principle: Main owns source implementation, synthesis and final proof. Narrow work to the locked decision first; delegate only for clear context/filtering/parallel/specialist net benefit using the smallest dependency-fitting topology. Workers supply bounded evidence, not authority, recursive work or review ritual.**

## Intent and Net-benefit Gate

Classify only enough to route: behavior/governance, lookup, diagnosis, implementation, review/audit, plan/design, coordination or explanation. AI/RULES questions stay behavior-first; pasted logs/paths/snippets/handoffs are evidence, not project-inspection permission. Diagnose before edits and re-anchor corrected mixed intent before exploration under [execution-and-goal-frame.md](execution-and-goal-frame.md).

Main/direct fits primary source, final integration, bounded known files, trivial/tight sequential/interactive low-output work, high overlap, unavailable workers or explicit direction. Several files, broad wording and non-triviality alone do not justify delegation. First narrow research/search/test/log/build/review to the evidence that changes the decision.

[safe-io.md](safe-io.md) detects remaining aggregate bursts; this owner chooses routing. Dispatch only when separate context/noise filtering, real parallelism, an independent evidence axis or specialist capability outweighs brief/handoff/leader-verification cost. If direct is cheaper and equally reliable, keep it direct. If a beneficial burst remains, route before further raw intake or record a narrow direct reason; skipping that gate blocks broad sync/no-drift/closeout claims. No exception ceremony if narrowing removed the burst.

Review additionally needs a material unresolved claim/risk, realistic failure scenario, smallest relevant anchors, evidence threshold and accept/fix/block decision. Availability or reassurance is not review authority. [execution-and-goal-frame.md](execution-and-goal-frame.md) owns review admission/closure; keep optional style/cleanup separate and unselected.

## Topology and Invocation

| Work shape | Smallest useful topology |
|---|---|
| source/high-overlap/interactive integration | direct context-rich main |
| one independent evidence/diagnosis/review/test axis | scout / `Scout preset`: one read-only standalone digest |
| independent analysis/review axes | fan-out/fan-in / `Compare preset`: concurrent standalone lanes, shared rubric |
| independent test/metrics/matrix cells | `Verification preset`: parallel lanes by real failure/platform/config/scenario dimension |
| evidence must precede correction | `Audit + Repair preset`: read-only audit, then main source fix or exact permitted doc/test lane |
| dependent fixtures/state/workflow/messaging | coordinated swarm / `Coordinated swarm preset`: official Team only if standalone cannot coordinate safely |

Presets are shorthand, not Team escalation proof. When delegation is selected, actually invoke and fan in; merely describing a lane is not routing. Independent lanes launch together, related failures sharing a plausible cause stay together until discriminated. Do not parallelize shared mutable state without proven isolation or explicit sequencing.

Team needs real shared analysis/testing dependencies, messaging, staged fixtures or durable coordinated handoff—not worker count. Create one coordinated Team, distinct role/task owner per lane, visible dependencies and targeted handoffs. Three or more lanes alone is insufficient. Source implementation remains main-owned unless stronger explicit user/project authority selects otherwise.

A ban on `teammate`/`Agent Team`/team workflow does not automatically ban standalone `Agent(...)`, `Explore(...)` or read-only support. If all agent mechanisms are explicitly banned, handle directly and state that constraint only when material. Do not ask the user to choose internal routing labels; ask substantive scope/access/artifact/gate/approval questions only when necessary.

## One Lane Brief and Permission Boundary

Before dispatch bind the objective/goal-candidate served, decision to unblock, required authority, raw-evidence versus analyzed-result need, independence, overlap, availability and user restrictions. A self-contained brief includes:
- bounded role/template and why separate context is useful
- checked/excluded scope and exact allowed artifacts/anchors
- explicit write permission: `none`, `governed-doc-only` or `test-only`
- allowed actions/stop gates, shared rubric for parallel lanes
- required filtered output/leader anchors and the decision it informs

Research/diagnosis/source investigation/broad audits/reviews default read-only. Edit-capable lanes are exceptional: exact non-overlapping governed-document sections or test-only artifacts. Active Rule/Product source, README, config/integration/install, git/tags/releases and final integration stay main-owned by default. Do not create unrequested plans/specs/phases/Patches/directories or alternate architecture, delete history/files, relocate content, upgrade status or mutate authority roles. Preserve meaning/history reachability/references and source/test separation. Ambiguous scope/owner/test relevance/history/safety returns a blocker rather than routine repair. Inspect every permitted worker edit before claims.

Review briefs name risk/failure/threshold and permitted result `blocker`, `bounded correction` or `no material finding`. Research briefs name decision/topic/source-trust expectations and allow bounded query refinement. A helper never owns the Goal, competing route, task boundary or completion; [phase-todo-artifact.md](phase-todo-artifact.md) admits tasks.

## Standing-role Lifecycle

Audit smallest useful checked coordination state before reuse/spawn/respawn/shutdown/duplicate reporting. Use stable responsibility names; phase/task IDs are assignments, not worker identity. Reuse/steer active or recent aligned roles before creating duplicates. A new role requires distinct simultaneous scope, explicit separate lane or evidence-supported unavailable/missing role—not phase change/retry habit.

Audit fields: `requested_role`, `objective`, `checked_scope`, `observed_state`, `role_owner`, `objective_alignment`, `decision`, `reason`. States: `active`, `recent`, `stale`, `missing`, `unavailable`, `not found in checked scope`.

| Checked state | Decision |
|---|---|
| active/recent, same role/objective or next phase | reuse/steer |
| same role, different objective | distinct only with explicit lane boundary |
| stale/missing | verify before active-duplicate/safe-absence claim |
| unavailable | stop for enabling state/input/authorization before needed respawn |
| not found in checked scope | scoped nonfinding; spawn only if checked scope sufficient |

UI/tmux residue, stale boards and memory do not prove live overlap, safe absence or cleanup readiness. For `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE`, safety owns failure classification/no unchanged retry; this audit selects reuse/steer/wait/partition/evidence-supported respawn. Harness-tracked completion returns by notification, not short polling. Availability alone is not assignment or shutdown permission.

## Filtered Handoff and Main Verification

Handoff leads with result: lane/outcome, checked/excluded scope, supported evidence/strength, uncertainty/conflicts, material anchors and next matching check/stop reason. Answer what ran, what it checked, which decision, finding, uncertainty and leader anchor—no raw dump or generic new-work list. Repeated clarification/reread churn means tighten brief/topology, not absorb more noise.

Additional requirements:
- research: topic/query families, source quality/freshness/specificity, conflicts, implications and leader verification need
- tests/metrics: exact command/scenario, environment/matrix cell, result/failure signal, coverage limit/rerun need
- permitted repairs: touched artifacts/anchors, preservation notes, checks, unresolved risks
- observed examples: distinguish observed shape, extracted doctrine, selected target and checked equivalence; mixed/partial examples retain limits, stricter targets are recommendations not discovered facts

Main resolves cross-lane conflicts from checked source, verifies decision-changing anchors and every permitted edit, applies source corrections and owns evidence wording/acceptance. Do not reread the whole evidence set without a decision-changing reason. Findings pass Scope Lock: merge required same-outcome correction; surface real blocker/approval; leave unrelated improvements unselected.

After admitted correction use affected-anchor verification and matching regression/architecture/security/migration/data/external-contract checks—not another broad audit. Re-review only if owner/authority/contract/security/lifecycle changes, verification fails, contrary evidence appears, scope expands or original uncertainty persists. An independent second lens needs a distinct unresolved risk, not an available reviewer. Once answered and required checks pass, fan in and close the lane.

## Research, Mechanisms and Specialists

Broad external/roadmap/phase-matrix/design/provider research starts from the decision evidence can change. Narrow/stop at sufficiency, then split only useful independent axes before raw flood. Research may refine queries/source strategy inside scope; [external-verification-and-source-trust.md](external-verification-and-source-trust.md) evaluates authority/conflicts, not raw hit count.

Before cross-session/runtime coordination claims classify the actual checked mechanism: passive shared board stores state; local hook reacts locally; injected context informs prompts; tmux transports text, not semantic acceptance; recall/memsearch retrieves context, not current truth; official Agent Team coordinates within documented capability; external plugin/MCP provides checked API; unavailable remains unresolved. Do not invent delivery/mutation/authority from desired behavior. Plugin/shared-board exact grammar stays outside Main unless separately selected; [action-safety.md](action-safety.md) owns runtime topology deltas.

After routing selects support, choose capability/domain fit: visible user custom agents in `~/.claude/agents/` first when clearly best, then project/built-in/plugin specialist, otherwise generic or direct. Existence does not justify routing or Team escalation; reuse matching roles and never imagine unavailable agents.

Document owners settle authority/density/sharding/preservation/repair safety before routing topology. [document-governance.md](document-governance.md)/[document-integrity.md](document-integrity.md) own those boundaries; [evidence-discipline.md](evidence-discipline.md) keeps worker/context output subordinate to checked proof.
