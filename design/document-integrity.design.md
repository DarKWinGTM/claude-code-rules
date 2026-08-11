# Design - Document Integrity

> **Parent Rule:** [../document-integrity.md](../document-integrity.md)
> **Current Version:** 1.14
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
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

P148 refinement: Patch timeline migration requires an evidence- and SHA-256-bound manifest, exact-target reference resolution, correct relative-path recomputation, serialized/wildcard exclusions, suspended-archive preservation sentinels, explicit apply approval, exclusive owner-only manifest/journal output where supported, a rollback journal persisted before mutation, atomic reference replacement, post-apply former-path inactivity proof, and explicit journal/hash-gated rollback across unchanged, staged, or applied states. Ambiguous creation evidence remains blocked rather than inferred from mtime/ctime or indirect chronology.

P151 refinement: this owner must distinguish selected Runtime payload parity from full-project convergence in the Active Project Root. Payload/candidate/tag/release/fresh-clone equality proves only its named subset and cannot authorize root replacement. Full-project convergence checks relevant Runtime, governed, source/config, scripts/tests, plugin/support/tooling, generated-input, mode, and classified modified/untracked surfaces; split or unexplained state blocks no-drift and closeout wording.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Treat source-comment citations to governed docs as reference surfaces that need checked-path and checked-role maintenance when nearby behavior changes.
- Consume the Active Project Root authority from `authority-and-scope.md`; do not redefine root selection locally.
- Keep Runtime payload parity and full-project convergence as separate proof layers, preserve local-only/unclassified state pending owner decision, and block closeout while source/governed authority is split across locations.
- Keep metadata linked to this design and the chain changelog.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Former root rules absorbed into this chain are not active runtime authorities after the current compact 19-Rule set is selected.

Historical detail remains in changelog or execution-disconnected quarantine/provenance surfaces, not as parallel runtime authority, active input, or automatic fallback.

---

## Verification

Release validation should confirm the parent runtime file exists in the Active Project Root, has substantive body content, links to this design and its changelog, and matches the installed runtime copy when runtime install is in scope. It must report Runtime payload parity separately from full-project convergence and block whole-project/no-drift wording while relevant local source, governed, plugin, support, tooling, generated-input, mode, or classified working state remains split or unexplained.
