# Design - Execution and Goal Frame

> **Parent Rule:** [../execution-and-goal-frame.md](../execution-and-goal-frame.md)
> **Current Version:** 1.22
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/execution-and-goal-frame.changelog.md](../changelog/execution-and-goal-frame.changelog.md)

---

## Target State

`execution-and-goal-frame.md` is the active runtime owner for discussion/execution mode selection, continuous execution, goal framing, and next-work boundaries.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for execution continuity, goal-set review, priority balance, and completion-to-next-goal framing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for discussion/execution mode selection, visible intent read, selective clarification, repair re-anchor, and next-work boundaries.

P099 refinement: this owner must now also preserve broad-objective decomposition before deep execution, worker-fit next-lane continuation, and lane-aware continuation boundaries while keeping delegation and read/output control with `worker-routing-and-context.md` and `safe-io.md`.

P100 refinement: this owner may remove non-mechanism meta-evaluation text and tighten repeated continuation wording, but it must keep mode selection, intent recheck, visible intent read, selective clarification, goal/output/gate framing, next-lane continuation, and the worker-routing bridge explicit.

P101 refinement: this owner should now preserve the active goal while holding unverified proposal premises as candidate paths and retire stale premises after user correction before continuation.

P107 refinement: this owner should now make explicit when a supported next-goal recommendation may be translated into an advisory Claude Code `/goal` command, while keeping direct continuation as the default when the next slice is already safe and implied.

P109 refinement: this owner must now preserve ordered handling for phase-shaped continuation so execution momentum continues the current active phase first, then an existing-family subphase, and only then a new major phase when checked evidence rules out the earlier identities.

P113 refinement: this owner should now keep `/goal` suggestions concise for trivial non-governed next steps, but require governed-surface context for bounded repo-governed successor objectives and source that context from design first, then active execution surfaces, with changelog/patch/README included only when they materially shape completion, review, or current-state impact.

P114 refinement: this owner should now treat successor recommendations as candidate goals first when several meaningful directions remain live, and allow promotion from candidate goal to advisory `/goal` only when one governed candidate becomes the best-supported bounded successor under the existing governed-work-only bridge.

P116 refinement: this owner should now make dominant-session-language behavior end-to-end across candidate-goal labels, promoted `/goal`, surrounding recommendation labels, and recap/closing lines while preserving exact literals that should remain exact instead of translating them for cosmetic consistency.

P117 refinement: this owner should now allow candidate-goal surfacing at real decision boundaries where several materially different next slices remain live and no one continuation path clearly dominates, while still preserving direct continuation when one path is already clearly selected and safe.

P118 refinement: this owner should now reject generic future-note closeout when meaningful successor work is already visible, require conversion into the correct next-step surface, and derive a smaller truthful successor slice when checked execution surfaces already provide more than a broad future label.

P119 refinement: this owner should now infer the default language for goal-shaped next-step surfaces from the user's main working language across the active exchange even without a direct language instruction, treat an explicit language request as a stronger override, preserve exact literals token-by-token including query parameters, and reject wrapper-only translation where the `/goal` or recommendation body remains in another language beyond those preserved literals.

P123 refinement: this owner should now preserve that selected or promoted governed `/goal` work may conditionally use internal native subagent assistance for analysis, verification, testing, and bounded plan drafting without creating a new user-facing command, while still keeping `/goal` as the objective owner, `/plan` as the route owner, and leader-owned synthesis/proof wording as the completion authority.

P124 refinement: this owner should now allow advisory governed `/goal` creation to conditionally run an internal pre-goal planning pass before final goal emission when route synthesis materially improves the command, let native subagents help with analysis, route drafting, verification ordering, and optional plan-file reference synthesis, keep simple goals on the direct `/goal` path, and keep plan-backed route material subordinate to `/goal` objective ownership and leader-owned goal proof.

P125 refinement: this owner should now preserve an integrated goal-with-planning visible surface so route-heavy governed `/goal` work may use internal planning / plan-mode-style support before or around final goal emission, keep compact route support inside or adjacent to that goal-centric surface, and reserve `/plan` for overflow or explicitly requested standalone route handling instead of the ordinary paired next surface.

P134 refinement: this owner should now require any durable route-plan pointer for a plan-backed governed `/goal` to travel inside the same copyable goal artifact instead of living only in surrounding explanation, while keeping `/goal` as the objective owner, keeping the plan file route-only, and allowing adjacent route notes only when they are not the sole durable plan pointer.

P135 refinement: this owner should now require actual governed `/goal` authoring with durable route support to write the route-only plan file before final goal emission, ban save-plan and rerun-`/goal` loops when no real stop gate exists, and treat failed plan-file writes as blockers rather than emitting a fake `Plan reference`.

P136 refinement: this owner should now require copied durable-plan-backed governed `/goal` artifacts to keep `/goal` first and `Plan reference:` second inside the same copied artifact, while preserving the P135 plan-file-first authoring contract and rejecting detached-preface presentation of the plan reference.

P137 refinement: this owner should now preserve an automatic execution-posture decision for selected non-trivial plan-backed or goal-backed work so execution prefers Subagent-Driven first, delegates topology to worker-routing-and-context.md, delegates live task shaping to phase-todo-artifact.md, and preserves Inline Execution only as a checked direct-handling exception when more effective.

P139 refinement: this owner should now treat plain goal requests as enough to trigger planning-depth resolution, choose the smallest sufficient route support automatically for governed work, keep durable `Plan reference` valid only after a route-only plan file already exists in checked scope or was successfully written in the same flow, and keep selected goal/plan execution posture internally chosen rather than exposed as a default user-facing mode choice.

P121 refinement: this owner should now preserve an explicit goal-to-plan bridge so `/goal` remains the objective owner, `/plan` remains the route owner, governed non-trivial goals may bridge into planning without forcing plans for every goal, and route completion alone cannot substitute for goal-gate closeout.

P122 refinement: this owner should now preserve explicit `/plan` next-surface recommendation once a selected governed goal remains route-heavy, so the assistant does not leave the route in broad prose after the goal is already chosen.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Preserve lane decomposition and next-lane continuation semantics without taking delegation or bounded-I/O ownership away from `worker-routing-and-context.md` and `safe-io.md`.
- Preserve ordered phase-shaped continuation handling so current-phase reuse and truthful subphase fit are evaluated before any new-major phase selection.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
