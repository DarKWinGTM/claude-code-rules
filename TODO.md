# Claude Code Rules - TODO

> **Last Updated:** 2026-03-11

---

## ✅ Completed

- [x] UDVC-1 design/runtime/changelog synchronization baseline applied across governance chains.
- [x] Changelog-layer metadata normalization completed (mandatory headers + active-session integrity).
- [x] WS-1 to WS-6 hardening execution slices completed and synchronized in master governance docs.
- [x] Authorized adversarial workflow rule suite completed (`refusal-minimization`, `refusal-classification`, `recovery-contract`, `dan-safe-normalization`).
- [x] Core documentation-control standards implemented and maintained (`document-changelog-control`, `document-design-control`, `document-patch-control`, `project-documentation-standards`, `todo-standards`).
- [x] Align patch documents to UDVC-1 metadata contract (`patches/consistency-rule-enhancement.patch.md`, `patches/legacy-rules-migration.patch.md`).
- [x] Run final consistency audit across design/rule/changelog/TODO/patch layers (triad, links, anchors, sessions, TODO compliance).
- [x] Create runtime `unified-version-control-system.md` and align related governance references after design/changelog-first rollout.
- [x] Create runtime `explanation-quality.md` and align master rule inventory after design/changelog-first rollout.
- [x] Complete anti-poisoning cleanup wave across README, master design, governance templates, runtime metadata policy, and support-artifact boundary handling.
- [x] Apply balanced concise-summary patch to `accurate-communication` and `explanation-quality`, then install updated runtime rules.
- [x] Extend patch workflow to support flexible phased implementation planning and add a reusable non-governed root-level template.
- [x] Create first-class `phase-implementation` rule chain, realign patch/documentation authority boundaries, rewrite the root helper as readable markdown, and install updated runtime rules.
- [x] Refine role-specific checklists so `phase-implementation` validates phased execution-planning quality while `document-patch-control` validates governed patch/review quality.
- [x] Create first-class `answer-presentation` rule chain and integrate it into the active runtime inventory, master design, README, changelog, and installed runtime rules.
- [x] Make `/phase` the live namespace for phased execution: require `phase/SUMMARY.md`, require child phase files under `phase/`, and keep `/patches` separate from the live phase-plan workspace.
- [x] Strengthen `phase-implementation` reviewability: require each child phase to show explicit design-to-phase extraction mapping and a review-oriented flow diagram that explains what part is being enhanced, developed, migrated, validated, or replaced.
- [x] Strengthen `phase/SUMMARY.md` reviewability: require an overview flow diagram for the whole phase set and expand the template with a fuller canonical child-phase example.
- [x] Add a summary-level design extraction table to `phase/SUMMARY.md` so reviewers can map design sources → phase files → derived work → target outcomes before reading individual phases.
- [x] Add a reviewer checklist block to each child phase so review can quickly confirm source correctness, flow clarity, phase boundaries, dependencies, and evidence readiness.
- [x] Standardize child-phase review outcomes with shared sign-off status, reviewer severity, and reviewer disposition values.
- [x] Add a summary-level review aggregate table to `phase/SUMMARY.md` so approvers can see per-phase sign-off status, severity, disposition, and blocker/follow-up state from one place.
- [x] Define a completion boundary and stop rule for the phase-planning model, and narrow communication rules so completed work does not force artificial extra options or endless follow-up suggestions.
- [x] Refine option-offering guidance so next-step options are suggested only when genuinely useful and not treated as a mandatory ending pattern.

---

## 📋 Tasks To Do

### Current Governance Execution
- [ ] (none)

### Deferred Enhancements
- [ ] Automated validation script for documentation compliance (deferred by user).
- [ ] Integration testing for design/changelog/rule/TODO integration paths (deferred by user).

---

## 📜 History

| Date | Changes |
|------|---------|
| 2026-03-11 | Refined option-offering guidance: updated `accurate-communication` and `explanation-quality` so next-step options are suggested only when genuinely useful, materially helpful, and tied to a real continuation path rather than being treated as a mandatory ending pattern. |
| 2026-03-11 | Finalized the phase-planning model boundary: updated `phase-implementation` with an explicit Definition of Done and stop rule, updated `phase-implementation-template.md` with the same completion boundary, and narrowed `accurate-communication` plus `explanation-quality` so completed work no longer forces artificial next-step options when no real continuation is needed. |
| 2026-03-11 | Added summary-level review aggregation: updated `phase-implementation` so `phase/SUMMARY.md` must include a review summary table, expanded `phase-implementation-template.md` with that table in both the summary template and example section, and recorded the enhancement in TODO history. |
| 2026-03-11 | Standardized child-phase review outcomes: updated `phase-implementation` so child phases use one sign-off status vocabulary plus reviewer severity/disposition fields, expanded `phase-implementation-template.md` with those review-outcome fields in both the child template and canonical example, and recorded the enhancement in TODO history. |
| 2026-03-11 | Added reviewer-ready child-phase validation: updated `phase-implementation` so each child phase must include a reviewer checklist block, expanded `phase-implementation-template.md` with that checklist in both the child template and canonical example, and recorded the enhancement in TODO history. |
| 2026-03-11 | Added summary-level design extraction mapping: updated `phase-implementation` so `phase/SUMMARY.md` must include a design extraction summary table, expanded `phase-implementation-template.md` with that table in both the template and example sections, and recorded the enhancement in TODO history. |
| 2026-03-11 | Strengthened `SUMMARY.md` and child-phase reviewability: updated `phase-implementation` so `phase/SUMMARY.md` must include an overview flow diagram for the full phase set, expanded `phase-implementation-template.md` with that summary-level diagram plus a fuller canonical child-phase example, and recorded the enhancement in TODO history. |
| 2026-03-11 | Strengthened phase reviewability: updated `phase-implementation` so each child phase must explicitly map design source → derived execution work and include a review-oriented flow diagram, updated `phase-implementation-template.md` to require those sections in child phase files, and recorded the enhancement in TODO history. |
| 2026-03-11 | Moved live phased execution to `/phase`: updated `phase-implementation` to require `phase/SUMMARY.md` plus child phase files under `phase/`, updated `document-patch-control` and `project-documentation-standards` so `/patches` is no longer the live phase namespace, rewrote `phase-implementation-template.md` to demonstrate the new `/phase` structure, refreshed `README.md`, and recorded the rollout in TODO history. |
| 2026-03-10 | Created first-class `answer-presentation` rule chain: added `design/answer-presentation.design.md`, `answer-presentation.md`, and `changelog/answer-presentation.changelog.md`; updated `design/design.md` and `README.md` to 26 active runtime rules; and installed the new presentation-layer runtime rule into `~/.claude/rules/answer-presentation.md`. |
| 2026-03-10 | Refined role-specific checklist boundaries: updated `phase-implementation` to v1.1 with a dedicated execution-planning validation checklist, updated `document-patch-control` to v1.7 with a dedicated patch-governance checklist, clarified that the two checklists serve different roles, and preserved the patch ≠ phase boundary. |
| 2026-03-10 | Created first-class `phase-implementation` rule chain: added `design/phase-implementation.design.md`, `phase-implementation.md`, and `changelog/phase-implementation.changelog.md`; refocused `document-patch-control` to governance/metadata role only; updated `project-documentation-standards` to distinguish phase rule vs patch instance vs root helper; rewrote `phase-implementation-template.md` into readable practical markdown with richer phase status, action points, design references, and TODO/changelog companion guidance; updated `design/design.md` + `README.md` to 25 active runtime rules; and installed updated runtime rules into `~/.claude/rules/`. |
| 2026-03-10 | Corrected flexible phase template placement to the RULES root: updated `document-patch-control` to v1.5, updated `project-documentation-standards` to v2.0, created `phase-implementation-template.md` at root, refreshed `design/design.md`, and reinstalled the updated runtime rules into `~/.claude/rules/`. |
| 2026-03-10 | Extended the patch workflow for flexible phased implementation planning: updated `document-patch-control` to v1.4, updated `project-documentation-standards` to v1.9, and at that time introduced a non-governed reusable phase template under the temporary historical path `support/phase-implementation-template.md`; this was later corrected to the root `phase-implementation-template.md` location. |
| 2026-03-09 | Applied balanced concise-summary patch to `accurate-communication` and `explanation-quality`: updated both design/runtime/changelog chains, refreshed `design/design.md` inventory references, and installed the updated runtime rules into `~/.claude/rules/`. |
| 2026-03-08 | Completed anti-poisoning cleanup wave: rewrote `README.md` to overview-only scope, refactored `design/design.md` to active-state-only guidance, normalized governance design/runtime docs to the canonical `Design + Session + Full history` model, converted `design/accurate-communication.design.md` to navigator-style active design content, and reclassified `design/image.prompt.design.md` into support-only `support/image-prompts.md`. |
| 2026-03-07 | Upgraded active `explanation-quality` chain to v1.2: updated `design/explanation-quality.design.md`, `explanation-quality.md`, and `changelog/explanation-quality.changelog.md` with negative triggers, closing-summary behavior, decision usefulness checks, and required next-step option endings; synchronized `design/design.md` and `changelog/changelog.md`. |
| 2026-03-07 | Completed runtime rollout for `explanation-quality`: created `explanation-quality.md` (v1.1), synchronized `design/explanation-quality.design.md` + `changelog/explanation-quality.changelog.md` (v1.1), updated `design/design.md` and `README.md` to active-state inventory, and closed the pending TODO rollout task. |
| 2026-03-07 | Created `design/explanation-quality.design.md` + `changelog/explanation-quality.changelog.md` (v1.0), updated `design/design.md` to register pending activation state, and queued runtime `explanation-quality.md` materialization for later approval. |
| 2026-02-24 | Completed runtime rollout closure for unified version controller: created `unified-version-control-system.md` (v1.1), synchronized `changelog/unified-version-control-system.changelog.md` (v1.1), updated `design/design.md` to active-state indexing, and closed pending TODO rollout task. |
| 2026-02-24 | Created `design/unified-version-control-system.design.md` + `changelog/unified-version-control-system.changelog.md` (v1.0) and queued runtime `unified-version-control-system.md` creation as pending by request. |
| 2026-02-24 | Reconfirmed single-standard version governance scope in master docs: updated `design/design.md` (UDVC-1 unified mechanism across design/changelog/TODO/patch), `changelog/changelog.md` v3.6, and synchronized TODO execution history. |
| 2026-02-23 | Completed final consistency audit across design/rule/changelog/TODO/patch layers: patch metadata contract closure, active-session placeholder removal (`design/accurate-communication.design.md`), and legacy changelog `#version-*` anchor normalization. |
| 2026-02-23 | Aligned `patches/consistency-rule-enhancement.patch.md` and `patches/legacy-rules-migration.patch.md` to UDVC-1 metadata contract (mandatory fields, version/session/history-link alignment) and created `changelog/consistency-rule-enhancement.changelog.md` authority file. |
| 2026-02-23 | Simplified `TODO.md` to canonical `todo-standards` structure (`Completed`, `Tasks To Do`, `History`) and removed dashboard/priority overhead artifacts. |
| 2026-02-23 | Completed changelog metadata normalization sweep: mandatory header completion, parent-reference normalization, and active-session placeholder removal in changelog layer. |
| 2026-02-22 | Completed WS-1..WS-6 hardening synchronization slices and aligned governance references across design/runtime/changelog artifacts. |
| 2026-02-21 | Completed authorized adversarial workflow suite design+rules+changelog chain rollout. |
| 2026-02-01 | Completed legacy rule migration and patch-control standard integration baseline. |
| 2026-01-21 | Completed master design/changelog restructuring and rules-template standardization baseline. |
