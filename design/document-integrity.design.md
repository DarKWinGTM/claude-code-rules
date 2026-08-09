# Design - Document Integrity

> **Parent Rule:** [../document-integrity.md](../document-integrity.md)
> **Current Version:** 1.12
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/document-integrity.changelog.md](../changelog/document-integrity.changelog.md)

---

## Target State

`document-integrity.md` is the active runtime owner for cross-reference consistency, rollover integrity, hygiene boundaries, and no-delete-by-cleanup discipline.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for document consistency, governed rollover, file hygiene, shard links, and active entrypoint integrity.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on former root files.

P101 refinement: this owner should now verify normalized same-stem parent/shard pairs, compact-entrypoint visibility, and prevent archive/history reference material from silently becoming the active owner or automatic resolution path.

P102 refinement: this owner should now verify declared chain shape, flat sibling shard maps, and no-orphan/no-mixed-mode drift for chains that intentionally stay in a folder-scoped sibling-shard form before escalating to same-stem nested normalization.

P103 refinement: this owner should now verify that observed project shape, extracted doctrine, selected target form, and equivalence-claim basis do not collapse into one unsupported sync/no-drift claim when examples are used as doctrine evidence.

P104 refinement: this owner should now verify actual chain subject, selected parent filename, compatibility-parent role, bootstrap exit trigger, and shard-opening basis so generic compatibility parents and semantic active parents do not remain ambiguous competing owners.

P105 refinement: this owner should now verify namespace-scope-based generic-parent selection and enforce one active parent model per chain so folder-scoped generic parents are allowed without reintroducing dual-parent ambiguity.

P108 refinement: this owner should now absorb document-density, compact-thrash, God-line/God-file repair, and delegated governed-document repair doctrine that was previously duplicated inside worker-routing, while preserving preservation-first and no-delete semantics.

P135 refinement: this owner should now allow a route-only plan file required by the selected governed `/goal` authoring contract when it will be referenced exactly from the emitted copied goal artifact, while still rejecting speculative checkpoint/work-summary files, duplicate authority artifacts, and version-suffixed plan copies.

P138 refinement: this owner should now treat governed-doc citations in source comments as checked references, requiring update or removal when referenced paths, sections, or authority roles change, and preventing stale comment links from being treated as harmless local code detail.

P144 refinement: required governed startup artifacts are selected by the active owner `phase-todo-artifact.md`; references to retired absorbed owner names remain historical provenance only.

P146 refinement: migration-complete and no-drift integrity must verify applicable manifests, imports/dependencies, config, build/deployment inputs, tests/test discovery, generated-input declarations, and acceptance surfaces select only current authority. Quarantine, history, and `done/` may remain reachable provenance references but must not remain active, fallback, generated, or normally discovered inputs.

P073-12 refinement: conditionally selected diagram surfaces count as governed startup artifacts only when `phase-todo-artifact.md` selects them; document-integrity verifies their references but does not become a second diagram trigger owner.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Treat source-comment citations to governed docs as reference surfaces that need checked-path and checked-role maintenance when nearby behavior changes.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact 19-Rule set is selected.

Historical detail remains in changelog or execution-disconnected quarantine/provenance surfaces, not as parallel runtime authority, active input, or automatic fallback.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
