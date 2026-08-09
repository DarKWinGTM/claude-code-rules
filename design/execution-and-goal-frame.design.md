# Design - Execution and Goal Frame

> **Parent Rule:** [../execution-and-goal-frame.md](../execution-and-goal-frame.md)
> **Current Version:** 1.32
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
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

P137 refinement is superseded by P144: selected work still receives an internal execution-posture decision, but source implementation remains leader-owned and helper routing is limited by `worker-routing-and-context.md`.

P139 refinement: this owner should now treat plain goal requests as enough to trigger planning-depth resolution, choose the smallest sufficient route support automatically for governed work, keep durable `Plan reference` valid only after a route-only plan file already exists in checked scope or was successfully written in the same flow, and keep selected goal/plan execution posture internally chosen rather than exposed as a default user-facing mode choice.

P140 refinement: this owner should now preserve selected design-slice obligation coverage so execution extracts implementation-relevant semantic obligations from the bounded governed design slice, uses them for task/verification/continuation logic, and refuses headline-output-only closeout while selected invariants, failure modes, or dependency semantics remain uncovered without explicit status.

P141 refinement: this owner should now preserve a goal-authoring stop boundary so governed `/goal` or route-only plan-support authoring ends at the emitted goal artifact plus subordinate route support when execution was not yet selected, while execution-posture selection remains a later internal transition and no default `Subagent-Driven` / `Inline Execution` menu is surfaced at authoring closeout.

P143 refinement: this owner should now preserve progress narration as navigation rather than ceremony so non-trivial progress updates can show `Current` / `Done so far` / `In progress` / `Remaining` / `Blockers / Notes` / `Next` when helpful, but status narration must not become a stop reason or milestone-only pause when safe continuation exists.

P121 refinement: this owner should now preserve an explicit goal-to-plan bridge so `/goal` remains the objective owner, `/plan` remains the route owner, governed non-trivial goals may bridge into planning without forcing plans for every goal, and route completion alone cannot substitute for goal-gate closeout.

P122 refinement: this owner should now preserve explicit `/plan` next-surface recommendation once a selected governed goal remains route-heavy, so the assistant does not leave the route in broad prose after the goal is already chosen.

P144 refinement: leader-owned source implementation is the default after a selected goal enters execution; bounded helper lanes may support research, diagnosis, review, parallel testing, test-only authoring, or exact governed-doc work but remain evidence inputs. Execution must hand helper-fit work to `worker-routing-and-context.md` for actual topology selection and invocation rather than stopping at lane description. Public read-only external lookup is evidence gathering rather than an approval-sensitive external mutation. Genuine emergencies may perform only the smallest safe reversible containment/diagnostic slice before startup when delay increases immediate harm, then immediately return to normal governance and recovery synchronization.

P146 refinement: this owner must make non-trivial analysis/design proactively complete the material decision surface by checking outcome, success conditions, constraints, dependencies, state/integration assumptions, failure behavior, verification, real alternatives, and simpler sufficient paths; recommend the best-supported route without fabrication, overdesign, or user-authority takeover. Migration execution remains open until `action-safety.md` convergence gates—target verification, cutover, former-path disconnection, bridge retirement, quarantine separation, and inactivity proof—are resolved.

P147 refinement: this owner must separate goal, checkable premise, proposed path, and requested action before material expansion; inspect current ownership, sibling roles, consumers, dependencies, and completed verification; protect a verified narrow baseline from unsupported reopening; proactively interrupt a false-premise route while preserving the valid goal; and use a narrow discriminating check when evidence remains incomplete. Broader architecture is evidence-earned and must carry its own state, migration, failure, and verification obligations.

Case 17 refinement: this owner must distinguish proof reachable within the current execution state from terminal proof gated by approval, environment state, or unavailable capability; complete all independent reachable proof before stopping; preserve whether gated proof remains part of the current Goal or forms a distinct successor live-verification Goal; retain the exact terminal proof obligation and resume condition; and prevent unchanged retries when no approval, state, or capability change can produce new evidence.

P073-12 refinement: this owner is the sole decision boundary for direct continuation, candidate-goal surfacing, advisory `/goal` eligibility, clarification, or no successor. It hands the selected posture to `goal-authoring-and-route-support.md` for construction and to `explanation-and-presentation.md` for rendering.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Preserve lane decomposition and next-lane continuation semantics without taking delegation or bounded-I/O ownership away from `worker-routing-and-context.md` and `safe-io.md`.
- Preserve proactive completeness for non-trivial analysis/design while keeping simple work direct and recommendations evidence-calibrated and advisory.
- Preserve selected design-slice obligation extraction and the rule that uncovered obligations continue execution instead of allowing headline-output-only closeout.
- Preserve reachable-proof closure so a blocked terminal check does not cause other independent current checks to be skipped.
- Preserve the boundary between current-Goal proof and a distinct successor live-verification Goal; required current proof cannot be reclassified merely to enable closeout.
- Preserve terminal proof obligations, prerequisite approval/state/capability, observable pass/fail signal, and meaningful resume trigger across a legitimate stop.
- Preserve stop behavior when unchanged approval/state/capability gates make another attempt non-discriminating, while leaving retry classification and approval mechanics with their canonical owners.
- Preserve migration continuation until the canonical convergence owner’s cutover, disconnection, retirement, quarantine-separation, and inactivity-proof gates close.
- Preserve ordered phase-shaped continuation handling so current-phase reuse and truthful subphase fit are evaluated before any new-major phase selection.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact active runtime set is selected.

Historical detail remains in changelog or execution-disconnected quarantine/provenance surfaces, never as parallel runtime authority, fallback, or generated execution input.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.

Semantic review must also confirm both proof-reachability branches: required live proof keeps the current Goal blocked, while genuinely distinct later live proof is preserved as an unselected successor Goal. The runtime text must require reachable checks before stopping and must not promise retries without an enabling approval, state, or capability change.
