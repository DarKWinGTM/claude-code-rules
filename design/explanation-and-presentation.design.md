# Design - Explanation and Presentation

> **Parent Rule:** [../explanation-and-presentation.md](../explanation-and-presentation.md)
> **Current Version:** 1.6
> **Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835
> **Full history:** [../changelog/explanation-and-presentation.changelog.md](../changelog/explanation-and-presentation.changelog.md)

---

## Target State

`explanation-and-presentation.md` is the active runtime owner for plain-language explanation, scan-friendly presentation, diagram discipline, and concise action framing.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for answer presentation, explanation quality, no-frame diagrams, and response closing.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P098 refinement: this owner must now also preserve target-state doctrine for plain-language explanation, visible intent-read response shapes, root-cause walkthroughs, and concise action framing.

P107 refinement: this owner should now preserve a compact advisory `Suggested /goal:` closing shape when another owner has already decided that a bounded, provable successor objective should be surfaced as a command rather than as ordinary prose alone.

P110 refinement: this owner should now preserve meaning-first identifier walkthroughs so code/config/system explanation starts from what an identifier is, what it does, and what changes if it changes, explains nested keys parent → child, and keeps UI mental model versus storage model explicit when that distinction prevents user confusion.

P113 refinement: this owner should now keep advisory `Suggested /goal:` output compact by default, avoid governed-surface framing for trivial non-governed next steps, and include only the material surfaced details that define completion, proof, scope, or review when a governed `/goal` command is actually warranted.

P114 refinement: this owner should now preserve a candidate-goal presentation shape before command promotion, keep promoted `/goal` wording aligned to the dominant session language by default, and maintain a clear presentation boundary between prose goal options and the single governed candidate that is actually promoted into command form.

P116 refinement: this owner should now keep the visible wrapper labels and output examples language-neutral or dominant-session-language-driven instead of hardcoding English-first user-facing templates around non-English goal output.

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
