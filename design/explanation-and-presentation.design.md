# Design - Explanation and Presentation

> **Parent Rule:** [../explanation-and-presentation.md](../explanation-and-presentation.md)
> **Current Version:** 1.17
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/explanation-and-presentation.changelog.md](../changelog/explanation-and-presentation.changelog.md)

---

## Target State

`explanation-and-presentation.md` is the active runtime owner for plain-language explanation, scan-friendly presentation, inline diagram discipline, and concise action framing.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for answer presentation, explanation quality, inline no-frame diagrams, and response closing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for plain-language explanation, visible intent-read response shapes, root-cause walkthroughs, and concise action framing.

P107 refinement: this owner should now preserve a compact advisory `Suggested /goal:` closing shape when another owner has already decided that a bounded, provable successor objective should be surfaced as a command rather than as ordinary prose alone.

P110 refinement: this owner should now preserve meaning-first identifier walkthroughs so code/config/system explanation starts from what an identifier is, what it does, and what changes if it changes, explains nested keys parent → child, and keeps UI mental model versus storage model explicit when that distinction prevents user confusion.

P113 refinement: this owner should now keep advisory `Suggested /goal:` output compact by default, avoid governed-surface framing for trivial non-governed next steps, and include only the material surfaced details that define completion, proof, scope, or review when a governed `/goal` command is actually warranted.

P114 refinement: this owner should now preserve a candidate-goal presentation shape before command promotion, keep promoted `/goal` wording aligned to the dominant session language by default, and maintain a clear presentation boundary between prose goal options and the single governed candidate that is actually promoted into command form.

P116 refinement: this owner should now keep the visible wrapper labels and output examples language-neutral or dominant-session-language-driven instead of hardcoding English-first user-facing templates around non-English goal output.

P117 refinement: this owner should now encode the default non-trivial answer shape more explicitly as plain-language summary first, small-table-when-useful for multi-axis explanation, grouped explanation by concept, and concise decision-ready close without turning trivial answers into a mandatory template.

P118 refinement: this owner should now treat generic future-note closeout as insufficient when a governed next-step surface is already visible, and should preserve closing shapes that name the successor goal/output/gate directly instead of leaving the next action in broad prose.

P119 refinement: this owner should now require wrapper labels, promoted `/goal` body text, and recommendation-shaped scaffold around preserved exact literals to stay aligned to the dominant language of the active exchange by default, treat explicit language requests as a stronger override, preserve exact literals token-by-token including query parameters, and reject wrapper-only translation as insufficient visible alignment.

P123 refinement: this owner should now preserve compact `Plan draft` / `Verification / testing route` wording for goal-owned internal helper use, keep that helper output visibly subordinate to the selected goal and its referenced plan file, and avoid letting the visible `/goal` surface inflate into a mini-`/plan` or orchestration narrative.

P124 refinement: this owner should now preserve a plan-backed advisory `/goal` presentation shape so a pre-goal planning pass prepares the full route file first and may surface compact `Plan draft`, `Verification / testing route`, or `Plan reference` context before or around the emitted goal without turning the visible goal surface into a mini-`/plan` or a second objective layer.

P125 refinement: this owner should now preserve an integrated goal-with-plan-reference presentation shape so governed `/goal` output stays one goal-centric visible surface, the emitted goal remains compact, the detailed route stays in the referenced plan file, and `/plan` appears only for overflow, later route revision, or explicitly requested standalone route handling.

P130 refinement: this owner should now require promoted or selected governed `/goal` output to use a prepared full detailed plan file as route support, keep the emitted `/goal` compact, surface a `Plan reference` as the normal route-context companion, and keep the referenced plan file visibly subordinate to the goal rather than a second objective surface or completion proof.

P121 refinement: this owner should now preserve a goal-to-plan explanation shape only for explicit standalone planning, later route revision, or overflow beyond an already referenced plan file, while keeping visible output objective-vs-route separate and anchoring closeout wording back to the goal gate when route work finishes first.

P122 refinement: this owner should now preserve a compact explicit `/plan` next-surface recommendation shape only when that explicit standalone-planning or later-overflow path is actually needed instead of the plan-backed goal reference alone.

P128 refinement: this owner should now keep inline answer/status/phase-local text-diagram discipline clearly separate from repository `diagram/` lane doctrine so no-frame formatting rules do not silently become source authority for governed visual documents.

P129 refinement: this owner should now keep inline answer/status/phase-local text diagrams explicitly outside mandatory Kroki-compatible governance unless they are deliberately promoted into the governed `diagram/` lane.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
