# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 10.65
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Shard Directory:** [design/](design/)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

The active target model for candidate `v10.65` keeps the same 19 body-sufficient source-owned Runtime Rules while adding proof-reachability, operational-capability-name classification, task reconciliation, authenticated/private capability, deterministic retry, reachable-source, and supplied-rendered-artifact evidence contracts across six existing owners. Released `v10.64` remains the latest published baseline and retains verified Patch chronology plus the repository-only `script/patch-timeline.mjs` Tool outside the Runtime Rule installation payload.

---

## 2) Current Active-State Summary

Current target-state priorities:
- keep successor posture ownership deterministic: `execution-and-goal-frame.md` selects direct/candidate/advisory/clarification/none, `goal-authoring-and-route-support.md` constructs the selected goal and route support, and `explanation-and-presentation.md` renders it
- evaluate diagram posture after design only when structure, visual authority, diagram relationships, visual topology, or existing diagram correctness changes; ordinary design edits may use `not required`
- classify `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE` in action safety, block unchanged retry while unresolved, and leave reuse/steer/wait/partition/respawn decisions to worker routing
- keep one complete canonical owner per mechanism and compact consumers to activation, local consequence, exact error-prevention literal/order, or handoff only
- separate a valid goal from its checkable factual premise, proposed path, and requested action before material expansion or replacement
- verify current semantic ownership, active sibling roles, readers/writers, state, dependencies, and completed proof when a false premise would materially change architecture, behavior, risk, or scope
- keep a checked completed narrow implementation as the active baseline until evidence shows its scope or gate is defective; use a discriminating check when evidence remains incomplete
- preserve the valid goal when correcting a false premise, explain the consequence of the unsupported path, and recommend the smallest evidence-supported route
- distinguish allowed-direction acceptance, factual confirmation, and best-route endorsement; invalidated assistant advice must be explicitly withdrawn/revised with the failed premise, contrary evidence, corrected recommendation, and remaining gate
- non-trivial analysis/design should complete the material decision surface, compare only realistic alternatives, consider a simpler sufficient path, and recommend the best-supported route without fabricating project facts, forcing disagreement, or replacing user authority
- migration/cutover closes only after positive target proof and proportionate negative former-path inactivity proof show exactly one active authority, no active bridge/fallback/dual path, and no normal quarantine read
- governed Patch chronology derives from one verified original-creation UTC instant while retaining a semantic slug; filename and `Created At` remain equivalent and no Patch ID/index exists
- new Patch creation captures the instant once, creates exclusively, emits exact direct references, and preserves creation identity across revisions and governed moves
- legacy Patch migration remains evidence/hash-bound, updates only resolved exact references, blocks ambiguous or colliding rows, preserves suspended archives, and requires explicit verify/rollback rather than automatic fallback
- `script/patch-timeline.mjs` is dependency-free repository tooling for inventory, evidence audit, planning, creation, apply, verification, and rollback; it never enters the ordered 19-Rule Runtime payload
- governed Goal construction evaluates proposed done points for reachability before emission, distinguishes required proof, current reachable proof, successor/excluded proof, and route prerequisites, and repairs assistant-inferred infeasible Goal/plan gates in place; source/code goals cannot infer live acceptance from generic completion wording or operational Product-facing capability names, while a live terminal gate explicitly selected by the user or checked governed authority remains binding
- execution closes a source/local Goal at its selected reachable layer, surfaces genuinely distinct downstream Product proof as a prerequisite-bearing successor, and stops unavailable explicitly required live proof without unchanged retry
- live task reconciliation closes satisfied implementation and source/non-live verification tasks before optional live/rendered observation is surfaced as an unselected successor; required unavailable live proof remains visibly blocked with a resume condition
- authenticated/private access starts with target, network, tool/session, authorization, approval, and bounded-substitute preflight; one evidence-backed correction may run before deterministic `NO_RETRY_UNTIL_CHANGE`
- guest/login or `401` shows required authentication was not established; `403` shows refusal while authentication-versus-authorization cause remains unresolved; none alone proves the authenticated Product is broken
- external verification ranks only reachable authorized claim-fit sources after capability preflight, while approval, credential, and retry ownership remains with action safety
- screenshots, Rendered HTML, rendered text/semantic witnesses, sanitized console/log/network exports, and authenticated harness evidence remain useful only within their witness-specific proof boundaries
- runtime rules stay as body-sufficient active behavior contracts
- one complete canonical owner should retain each mechanism; consumers keep only activation, local consequence, handoff, or the minimum synchronized exact copy needed to prevent a likely execution, safety, verification, or ordering error
- supporting explanation stays opt-in and non-repetitive, but becomes required when silence would hide material risk, ambiguity, irreversible consequence, verification limits, required confirmation/recovery, or a necessary next action
- source implementation and final integration stay leader-owned by default; helper lanes remain bounded to research, evidence filtering, diagnosis, audit/review, independent testing, test-only authoring, or explicitly assigned non-overlapping governed-document synchronization
- new user-visible objective, materially wider scope, durable standing-role/Team expansion, or different coordination architecture remains advisory until selected; inside a selected objective, the smallest justified bounded helper topology is internally invokable under the canonical routing owner without widening source/objective authority
- invocation follows work shape: one standalone agent for one independent axis; parallel standalone agents launched together for independent test/metrics/matrix cells; teammates only for shared dependencies, staged coordinated testing, cross-lane messaging, or durable role ownership
- reuse or steer an aligned active worker before spawning another; group potentially related failures in one diagnosis lane; return helper results through leader fan-in, selected-anchor verification, source repair, and proportionate rerun
- operational runtime workers/jobs/entities remain distinct from Claude subagents and Agent Team teammates
- authorized bounded destructive action remains blocked on exact action-and-scope confirmation and guardrails; malicious or unauthorized destructive activity may follow the refusal hard-block path
- only the smallest safe reversible emergency containment or diagnostic action may precede full startup when delay materially increases immediate harm, and normal governance must resume immediately afterward
- `implemented` remains intermediate while material verification is pending; terminal disposition is `verified`, `deferred`, `blocked`, `not applicable`, or `out of scope`
- ordinary public read-only lookup remains evidence gathering; consequential authenticated/private, mutating, sending, purchasing, deployment, shared-state, sensitive-data, meaningful-cost, or terms-acceptance actions remain approval-sensitive
- active runtime/design doctrine must outrank older completed phase/patch wording when chronology conflicts
- governed design/changelog chains must classify chain shape before appending or sharding detail
- folder-scoped single-chain namespaces may use `design/design.md` or `changelog/changelog.md` when the folder already fully identifies one chain
- each chain must still keep exactly one active parent model: generic parent or semantic parent, never both
- single-design chains should stay `single-file-bootstrap` until a checked `bootstrap_exit_trigger` and `shard_opening_basis` justify same-stem shards
- flat sibling shards are valid when the current folder already scopes the chain and only a few coherent slices are needed
- broad mature design/changelog chains should still strongly prefer compact parent indexes plus active same-stem child shard paths
- checked example structure must stay distinct from extracted doctrine and the selected target form when governance recommendations are derived from another project or chain
- `docs_analysis` must record observed project shape, extracted doctrine, selected target form, equivalence-claim basis, namespace scope, parent model choice, and single-parent authority basis when normalization work is in scope
- chronology/supersession review must stay explicit when active doctrine and reachable completed history discuss the same normalization rule
- compact `/goal` suggestions should stay light or be omitted entirely for trivial non-governed next steps
- candidate goals should be the preferred shape for multi-path successor recommendations when several meaningful directions remain live
- candidate goals may also surface at real decision boundaries when several materially different next slices remain live and no one continuation path clearly dominates
- when meaningful successor work is already visible, a generic future note such as `ถ้าจะไปต่อ...`, `next step would be ...`, or `implementation wave ใหม่` should not remain the final shape by itself; the assistant should resolve that successor state into direct continuation, candidate goals, advisory next goal, or advisory `/goal`
- if checked execution surfaces expose only a broad successor label but already provide enough material to derive a smaller bounded next slice, the assistant should derive that smaller slice instead of echoing the broad label back unchanged
- goal-shaped and recommendation-shaped natural-language scaffold should follow the dominant language of the active exchange by default even when the user did not issue a direct language instruction; an explicit language request is a stronger override
- exact literals such as `/goal`, file paths, version tags, code identifiers, and query parameters should remain exact where exactness matters instead of making the whole block read as an exact literal
- wrapper-only translation is insufficient: if the wrapper switches language but the goal/recommendation body stays in another language beyond preserved exact literals, the visible surface is still misaligned
- correction reasoning should start from the system logic or mechanism that best explains the symptom before narrowing into local fix scope
- supplier/model/path-specific narrowing should be treated as a scope hypothesis to prove from evidence rather than as the default first recommendation
- shared mechanisms should be evaluated before local exceptions, and local exceptions should be used only when the evidence supports a real local doctrine difference
- recommendation strength should match proof strength: provisional scope should stay provisional until corroboration supports a narrower owner decision
- compact `/goal` suggestions should be allowed only when a bounded governed-work successor objective is clear, measurable, provable in transcript, and better than direct continuation
- governed-surface context for `/goal` should become mandatory only for repo-governed multi-step, phase-backed, design-impacting, doc-sync, release-sync, runtime-rule-impacting, or materially current-state/review-sensitive work
- governed `/goal` suggestions should source design first, then current phase/task/TODO/checked implementation state, with changelog/patch/README included only when they materially shape completion, review, or current-state impact
- when several candidate goals remain live, only the best-supported governed candidate should be promoted into advisory `/goal` form; the others may stay prose goals
- advisory `/goal` creation for governed non-trivial or route-heavy work may conditionally run an internal planning / plan-mode-style pass before final goal emission when route synthesis materially improves the command
- that integrated planning pass may use native subagent assistance for analysis, route drafting, verification ordering, and optional plan-file reference synthesis while remaining internal-only and subordinate to leader-owned normalization
- simple or already direct goals should still emit `/goal` directly without forcing planning for every request
- when a durable route artifact is useful, a plan file may be referenced from the emitted goal or surrounding explanation, but the plan file must remain route-only and must not become objective authority
- the visible output for route-heavy governed goal requests should remain one goal-centric surface rather than two sideways `/goal` and `/plan` branches
- compact route notes, plan basis, verification route hints, or plan references may appear only as subordinate support inside or adjacent to the advisory `/goal`, not as a separate competing surface
- once one governed goal is selected, `/plan` should remain available only as an overflow or explicitly requested route surface when route detail no longer fits the integrated goal-centric surface
- route complexity such as multi-file work, multiple owner surfaces, ambiguous sequencing, or meaningful verification/release-sync decomposition may still justify `/plan`, but only after the selected goal exists and only when standalone route ownership materially helps
- selected governed non-trivial or route-heavy goals may also use conditional internal native subagent assistance for analysis, verification, testing, or bounded route drafting when that support keeps the existing `/goal` surface compact and evidence-grounded
- that assistance remains internal helper behavior only, not a new user-facing command or a replacement objective surface
- main-controller synthesis, visible proof wording, and goal-gate closeout remain leader-owned even when helper lanes or integrated route drafts contribute evidence
- closeout after planning should still prove the selected goal gate instead of treating completed plan steps, plan-file completion, or helper output as sufficient evidence by themselves
- phase identity selection should stay lineage-first: current active phase update first, existing-family child phase second, new major only after visible why-not-current / why-not-child-phase evidence
- forward-valid phase grammar should explicitly allow `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- observed alphanumeric phase forms such as `phase-NNN-NNa` should remain preserved as legacy-only until a later doctrine explicitly normalizes them
- deeper hybrid forms such as `phase-NNN-NN-NNb` should not be treated as forward-valid grammar by default
- Claude Code helper installs should prefer project-local `.claude/rules/` as the primary runtime target, use owner-aware manifest cleanup, and avoid overclaiming unsupported non-native harnesses for that install surface
- AI explanation should stay meaning-first: explain what an identifier is, what it does, and what changes if it changes before leaning on raw field or variable names alone
- non-trivial answers should usually open with one short plain-language summary, use a small table when several axes matter, continue with grouped explanation by concept, and end with a concise decision-ready close
- flow/process/queue/order/concurrency explanations may prefer an overview → small table → grouped explanation → concise summary shape when that structure reduces cognitive load
- nested keys should normally be explained parent → child, and UI mental model versus storage model should stay explicit when that distinction matters to understanding
- readable grouping of verified fact, inference, and hypothesis belongs to the communication owners, while proof thresholds and evidence semantics stay with `evidence-discipline.md`
- `TODO.md` and `phase/SUMMARY.md` stay compact bodyful active entrypoints, with exact pre-rollover snapshots and `history/` / `done/` references preserving completed detail
- current version, map, and navigation authority stay in active parent changelogs; indexed active same-chain version detail stays in chain-scoped version shards; `changelog/done/` remains inactive reference/provenance history rather than a fallback owner
- concern, factual claim, goal request, proposal, and assistant next action should stay separated before endorsement or continuation
- a governed `playground/` family may show how RULES change AI behavior in practice, but it must keep `rule-enforced fact`, `observed case`, and `virtual variant` visibly separate
- transcript-derived observed cases inside the playground must include exact checked paths and anchor hints rather than loose storytelling
- playground examples should prefer more realistic multi-turn traces when they help show how RULES alter the assistant path
- playground scenario coverage may include a language-aware candidate-goal promotion family so dominant-session-language ownership, candidate-goal-first successor recommendations, and selective `/goal` promotion remain inspectable as operational behavior
- candidate goals, promoted `/goal`, recommendation labels, and recap/closing lines should follow the dominant session language end-to-end, with English preserved only for exact literals such as command names, file paths, version tags, and code-level identifiers unless the user explicitly selects another language style
- playground scenario coverage may also include an end-to-end language-aligned goal surface family so wrapper labels, candidate-goal headings, promoted `/goal`, and recap lines can be inspected operationally rather than only as doctrine text
- governed behavior playground material stays outside the runtime install payload unless a later explicit doctrine changes that boundary
- worker-first/context-safe reading still starts from parent indexes and then follows the declared smallest relevant shard or detail surface
- README capability/current-state sections should stay front-page readable by explaining active doctrine and current-state behavior directly rather than replaying phase/release execution chronology as the meaning of the capability itself

Historical release-by-release detail lives in [../changelog/changelog.md](../changelog/changelog.md), not in this active target-state parent.

---

## 3) Shard Map

Open the smallest shard that answers the question.

- [repository-model.design.md](design/repository-model.design.md) — active surface roles and normalized documentation model
- [runtime-architecture.design.md](design/runtime-architecture.design.md) — 19-rule runtime inventory and category view
- [governance-contracts.design.md](design/governance-contracts.design.md) — metadata, sync order, startup, phase, rollover, and memory contracts
- [installer-architecture.design.md](design/installer-architecture.design.md) — project-local Claude Code helper install contract, cleanup boundary, and verification model
- [playground-architecture.design.md](design/playground-architecture.design.md) — governed playground family role, fact/observed/virtual separation, coverage model, and update flow
- [templates.design.md](design/templates.design.md) — standard templates for runtime, design, and changelog artifacts
- [verification-and-integration.design.md](design/verification-and-integration.design.md) — master verification checklist and related-chain integration

---

## 4) Compact Parent Boundary

This parent is the active authority gateway for the RULES system design.

It should remain compact enough to:
- expose current architecture and normalization direction quickly
- point readers to the correct child shard without broad raw absorption
- avoid becoming a history dump, template dump, or umbrella God file

Child shards under [design/](design/) remain active target-state truth, not archive or `done/` history.

---

## 5) Verification Orientation

Release validation for this master design chain should confirm:
- this parent remains compact and body-sufficient
- child shards are reachable and role-correct
- runtime/design/changelog versions align
- the six proof/auth/evidence/task triads advance together while the other 13 Runtime Rules remain byte-identical and the ordered inventory stays exactly 19
- Cases 17/12/04 plus matrix/coverage exercise reachable closure, explicit live-gate selection, task-list successor separation, authenticated capability, deterministic retry, and supplied-artifact proof limits
- forward-valid phase grammar explicitly includes `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- observed alphanumeric phase forms are classified explicitly as legacy-only or normalized by selected doctrine rather than left ambiguous
- observed project shape, extracted doctrine, selected target form, and any equivalence-claim basis stay distinct when checked examples ground governance recommendations
- history/release detail stays with changelog authority instead of re-accumulating in active design truth

---

## 6) Integration

Primary related surfaces:
- [../README.md](../README.md)
- [../changelog/changelog.md](../changelog/changelog.md)
- [../TODO.md](../TODO.md)
- [../phase/SUMMARY.md](../phase/SUMMARY.md)
