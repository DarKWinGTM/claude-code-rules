# Design - Document Integrity

> **Parent Rule:** [../document-integrity.md](../document-integrity.md)
> **Current Version:** 1.4
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/document-integrity.changelog.md](../changelog/document-integrity.changelog.md)

---

## Target State

`document-integrity.md` is the active runtime owner for cross-reference consistency, rollover integrity, hygiene boundaries, and no-delete-by-cleanup discipline.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for document consistency, governed rollover, file hygiene, shard links, and active entrypoint integrity.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P101 refinement: this owner should now verify normalized same-stem parent/shard pairs, compact-entrypoint visibility, and prevent archive fallback from silently becoming the active owner path.

P102 refinement: this owner should now verify declared chain shape, flat sibling shard maps, and no-orphan/no-mixed-mode drift for chains that intentionally stay in a folder-scoped sibling-shard form before escalating to same-stem nested normalization.

P103 refinement: this owner should now verify that observed project shape, extracted doctrine, selected target form, and equivalence-claim basis do not collapse into one unsupported sync/no-drift claim when examples are used as doctrine evidence.

P104 refinement: this owner should now verify actual chain subject, selected parent filename, compatibility-parent role, bootstrap exit trigger, and shard-opening basis so generic compatibility parents and semantic active parents do not remain ambiguous competing owners.

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
