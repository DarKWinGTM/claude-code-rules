# Design - Phase, TODO, and Artifact Initiation

> **Parent Rule:** [../phase-todo-artifact.md](../phase-todo-artifact.md)
> **Current Version:** 1.16
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/phase-todo-artifact.changelog.md](../changelog/phase-todo-artifact.changelog.md)

---

## Target State

`phase-todo-artifact.md` is the active runtime owner for startup artifact posture, phase execution, TODO durability, and live task tracking.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for artifact initiation control, phase implementation, and TODO standards.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P099 refinement: this owner must now also preserve phase-backed lane structuring and lane-aware live task shaping for broad worker-fit execution without making delegation itself a phase-owned decision.

P100 refinement: this owner may compress repeated phase-context, lane-aware task, and task-update presentation, but it must keep startup posture, lineage, durable-vs-live tracking, visible phase linkage, lane-aware task shaping, and verification-slice behavior explicit.

P101 refinement: this owner should now make the compact active-entrypoint shape of `TODO.md` and `phase/SUMMARY.md` more explicit while preserving `history/` / `done/` as normalized overflow paths.

P102 refinement: this owner should now require a compact `docs_analysis` form when governed design/changelog normalization work must choose between staying in a bootstrap parent, opening flat sibling shards, or escalating to same-stem nested normalization.

P103 refinement: this owner should now extend `docs_analysis` so checked example shape, extracted doctrine, selected target form, and equivalence-claim basis are recorded separately before assistants present a normalization choice as if it were observed project truth.

P104 refinement: this owner should now extend `docs_analysis` so chain scope kind, actual chain subject, selected parent filename, parent naming basis, compatibility-parent role, bootstrap exit trigger, and shard-opening basis are recorded before assistants normalize design/changelog structure.

P105 refinement: this owner should now replace master-only generic-parent assumptions with namespace-scope analysis so `docs_analysis` can choose generic parent or semantic parent explicitly while still recording one active parent model only.

P107 refinement: this owner should now preserve how a compact advisory `/goal` command is sourced from checked Goal/Output/Gate/Verification surfaces without introducing a new durable tracking schema.

P109 refinement: this owner must now preserve ordered phase identity selection as a target-state invariant: current active phase update first, existing-family subphase second, new major third, ask/record basis when unsettled. New-major selection must require checked evidence that current-phase and subphase fit were ruled out.

P113 refinement: this owner should now make governed-surface `/goal` sourcing design-first by default, require that heavy governed context appears only for repo-governed successor work, and include changelog/patch/README only when they materially shape completion, release/current-state truth, or before/after review boundaries.

P114 refinement: this owner should now preserve candidate-goal shaping before `/goal` promotion so several live successor directions can stay compact goal options, while the promoted governed `/goal` still comes from the existing design-first sourcing order and material-only execution/release inputs.

P116 refinement: this owner should now treat `Done when` / `Prove with` / `Scope` / `Keep` / `Stop after` as concept slots rather than mandatory English surface labels so emitted `/goal` wording can follow the dominant session language while preserving exact literals where needed.

P117 refinement: this owner should now let checked phase/roadmap/TODO surfaces shape compact candidate goals at real decision boundaries when several unselected next slices remain live and no one continuation path clearly dominates.

P118 refinement: this owner should now derive the smallest bounded successor slice from checked goal/output/gate/touched-surface context when phase/roadmap/TODO wording stays too broad, and should not leave successor output at generic future-note level when a smaller truthful next slice is already derivable.

P119 refinement: this owner should now make the emitted `/goal` scaffold follow the dominant language of the active exchange by default even without a direct language instruction, treat explicit language requests as a stronger override, preserve exact literals token-by-token including query parameters, and prevent whole-command exact-literal drift when only the surrounding scaffold should localize.

P121 refinement: this owner should now preserve a governed selected-goal to `/plan` bridge so execution surfaces can escalate route-heavy work into planning only when the route is materially non-trivial, keep phase/task linkage tied back to the selected goal, and return closeout to the goal gate instead of the route state alone.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Preserve ordered phase identity selection and visible lineage-basis recording; do not let future compression reduce current-phase → subphase → new-major into unordered criteria.
- Preserve phase-backed lane structure and lane-aware task shaping while leaving worker-scaling and bounded-I/O behavior to `worker-routing-and-context.md` and `safe-io.md`.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
