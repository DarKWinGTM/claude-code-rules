# Design - Document Governance

> **Parent Rule:** [../document-governance.md](../document-governance.md)
> **Current Version:** 1.8
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/document-governance.changelog.md](../changelog/document-governance.changelog.md)

---

## Target State

`document-governance.md` is the active runtime owner for repository document roles, design/changelog/patch governance, and runtime rule version control.

It consolidates previously separate rule chains into one body-sufficient runtime rule while preserving the behavior needed at execution time.

---

## Scope

This design owns the target-state shape for project documentation standards, design control, changelog control, patch control, and UDVC-1.

The runtime rule should stay compact enough to load as an active rule, but substantive enough to guide behavior without relying on deleted legacy root files.

P099 refinement: this owner must now also preserve governance/release-sync work-shape recognition and owner-aligned lane decomposition for broad multi-surface sync or release-readiness passes.

P101 refinement: this owner should now strongly prefer same-stem parent/index + shard paths for broad design/changelog chains while keeping `changelog/done/` as legacy/archive/fallback rather than the normal active detail path.

P102 refinement: this owner should now explicitly classify governed chain shape, allow flat sibling shards when the current folder already scopes the chain, and require visible append-vs-shard posture before parent design/changelog authorities absorb more detail.

P103 refinement: this owner should now keep observed project shape, extracted doctrine, and selected target form distinct so normalized RULES doctrine is not described as the literal project pattern unless checked equivalence evidence exists.

P104 refinement (superseded for folder-scoped single-chain namespaces by P105/P106): this owner should now resolve master-chain versus subject-chain parent naming before shape selection, reserve generic master parents for master-chain or compatibility-only roles, require subject-derived semantic parent filenames for non-master chains, and make bootstrap-first plus explicit shard-opening justification part of the target state.

P105 refinement: this owner should now allow `design/design.md` and `changelog/changelog.md` when the current folder already fully scopes one chain, while requiring exactly one active parent model per chain so generic and semantic parents do not coexist as active owners.

P106 refinement: this owner should now state explicitly that P105 supersedes the older P104 master-only/generic-parent restriction for folder-scoped single-chain namespaces, while still preserving the active bootstrap-first and shard-opening discipline from the released baseline.

P108 refinement: this owner should now absorb the append-vs-restructure-and-shard decision gate from worker-routing so governed parent-authority growth, shard-opening basis, and parent-model choice stay with the document-governance owner rather than the routing owner.

---

## Runtime Requirements

- Keep the root runtime rule as the active behavior contract.
- Preserve absorbed-rule semantics that affect real execution decisions.
- Keep metadata linked to this design and the chain changelog.
- Preserve owner-aligned sync-lane recognition while leaving worker-scaling and bounded multi-surface reads to `worker-routing-and-context.md` and `safe-io.md`.
- Avoid reintroducing split root rules unless a future governed phase selects that structure.

---

## Boundaries

Legacy root rules absorbed into this chain are not active runtime authorities after the compact 18-rule set is selected.

Historical detail remains in changelog or backup/provenance surfaces, not as parallel runtime authority.

---

## Verification

Release validation should confirm the parent runtime file exists at source root, has substantive body content, links to this design, links to its changelog, and matches the installed runtime copy when runtime install is in scope.
