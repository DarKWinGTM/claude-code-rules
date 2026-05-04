# Project Documentation Standards
> **Current Version:** 2.32
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.32
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
---
## Rule Statement
**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, `/phase`, `/patch`, completed history surfaces, and non-governed helper/support or extension-package artifacts; resolve startup posture before governed work drifts; declare patch participation in live phase when patch is in scope; keep public onboarding/install guidance portable.**
---
## Required Document Set
| Document | Required when | Purpose | Owner |
|---|---|---|---|
| `README.md` | always | overview/onboarding | standard practice |
| `design/*.design.md` | design/spec required | active target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | version trace required | active version authority, current index, and navigation | `document-changelog-control` |
| `changelog/done/*.changelog.md` | completed/older history should leave active scans | inactive history for audit/rollback/provenance/trace | `document-changelog-control` |
| `TODO.md` | tracking required | durable execution tracking | `todo-standards` |
| `phase/SUMMARY.md` | phased work required | live phase summary/index | `phase-implementation` |
| `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md` | multi-stage detail required | active execution detail | `phase-implementation` |
| `phase/done/phase-NNN-*.md`, `phase/done/phase-NNN-NN-*.md` | completed phase detail retained outside active scans | inactive completed phase history | `phase-implementation` |
| `patch/<context>.patch.md` or root `<context>.patch.md` | patch/review required | active review artifact outside phase | `document-patch-control` |
| `patch/done/<context>.patch.md` | completed patch artifact retained outside active scans | inactive completed patch history | `document-patch-control` |
| `phase-implementation-template.md` | reusable authoring aid needed | readable helper | non-governed helper |
| `support/**/*.md`, `plugin/**`, equivalent | optional reference/extension needed | support/extension content | non-governed support |
---
## Authority and Sync
- Changelog is the single version authority per governed chain.
- Design/rule/phase/patch metadata align with authoritative changelog state where applicable.
- Root helpers, support artifacts, and extension-package assets do not become chain authority unless intentionally normalized into a governed chain.
- Governance update order: design → runtime rule → changelog → TODO → patch metadata final sync when affected.
- Active metadata must use real session identifiers; placeholders are not allowed in active metadata.
---
## Role Boundaries
- Changelog owns current version/history authority; `changelog/done/` is inactive older/completed history, and changelog is not phase-definition storage.
- Design owns active target-state truth and has no default `design/done/` surface.
- Phase planning belongs to `phase-implementation.md`; `phase/SUMMARY.md` plus active `phase/phase-NNN-*.md` / `phase/phase-NNN-NN-*.md` files form the live phase workspace, while `phase/done/` is inactive completed history. `phase/SUMMARY.md` preserves phase-family lineage when it affects later major-vs-subphase decisions.
- Patch artifacts are self-identifying before/after review artifacts outside live phase planning; `patch/done/` is inactive completed patch history, and live phase execution must not be stored in patch artifacts. Design and patch artifacts need not point back to phase.
- `TODO.md` is durable tracking; Claude Code's built-in task list is live in-session tracking and does not replace durable/governed surfaces or define phases.
- Runtime installs target only the current project/source-owned active runtime rule files. Design, changelog, TODO, phase, patch, support, helper, and extension-package surfaces are not runtime-rule install targets unless a later explicit gate selects them. Naming an install destination does not widen the current source-owned install set.
- Shared runtime destinations may contain other project/plugin-owned runtime files; current repo docs must not classify, manage, or delete them unless owner/project scope is selected or verified. Runtime co-location is an observation, not ownership authority.
- `phase-implementation-template.md`, support/package assets, optional skills/agents, plugin scaffolds, scripts, and hooks are helper/support surfaces, not root governance authority unless intentionally normalized. Reusable support assets stay portable unless explicitly machine-scoped.
---
## Completed Documentation Surface Governance
Completed surfaces reduce active scan bloat without deleting governed history.
- Allowed inactive history: `phase/done/`, `patch/done/`, and `changelog/done/`.
- Not default: `design/done/`; design remains active blueprint/target-state authority.
- Current-state scans start with active design/changelog/TODO, `phase/SUMMARY.md`, active phase/patch files, and checked implementation state.
- Open `done/` or archive surfaces only for history, audit, rollback, provenance, or trace reconstruction.
- Completed status is not junk classification or deletion authorization, and active surfaces must keep enough pointers for history to be found.
- Do not let `done/` history replace active summary/index surfaces: `phase/SUMMARY.md`, active changelog index/current version, and active patch/review artifacts remain the first current-state lookup layer.
---
## Startup Artifact Gate
Before meaningful governed work, `artifact-initiation-control` resolves relevant surfaces as `use existing`, `create now`, `ask now`, or `not required`; this happens before later sync order.
Required companions remain non-optional when triggered: design for material target behavior/contract/policy, changelog for governed version/history, `TODO.md` for durable tracked work, `/phase` for staged execution, `/patch` for before/after review, and built-in tasks for live non-trivial visibility.
For phased/staged repos, live tasks follow current phase, phase family, order/dependencies, authored next-phase context, and checked lineage; unopened future phases stay context only. Phase creation/selection defers to `phase-implementation.md`, and greenfield baseline alone does not require a patch.

Startup decision model:
```text
Meaningful governed work begins
  ↓
resolve design / changelog / TODO / live task list / phase / patch posture
  ↓
use existing, create now, ask now, or explicitly mark not required
  ↓
continue only after required posture is resolved enough for the active slice
```
---
## New or Unclear File Classification
When a new/unclear file appears during governed work, keep role unresolved until checked rather than turning uncertainty into cleanup/disposal logic.
- Check master surfaces and relevant governed owner chains first; minimum active lookup when applicable is `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, relevant active `phase/`, and relevant active `patch/`.
- Consult `phase/done/`, `patch/done/`, or `changelog/done/` only for history/audit/rollback/provenance/trace needs.
- Destination/runtime files outside the current source-owned active runtime install set require owner/project scope resolution before classification.
- Git state and runtime co-location are observed local evidence only; disposal requires stronger semantic authority plus destructive-execution permission.
- `not required` does not mean `safe to remove`.
---
## Public Onboarding and Install Guidance
README/onboarding/install docs stay portable by default.
Required guidance:
- prefer repo-root-relative source guidance for cloneable/self-contained repos
- do not present workstation absolute paths or internal umbrella roots as public defaults
- distinguish source-side notation from destination/runtime notation
- use placeholders or contract labels for destination/runtime paths
- when naming runtime install scope, identify the current project/source-owned active runtime rule set rather than the whole shared destination directory
- exact local paths may appear only as checked local facts, local examples, or machine-scoped contracts
- for repo-root commands, prefer `./` or `<repo-root>` over a workstation path
- source-side guidance answers where the artifact is cloned or which repo-root context a command uses; destination/runtime guidance answers where installed/runtime artifacts belong
- if an exact local value must appear for debugging or audit, label it as local-only and do not let it become the reusable public default
---
## Cross-Document Alignment
- Shared governed docs/templates, public onboarding, and support/extension source stay portable; exact local values are only local observations or explicit machine-scoped contracts.
- Portable defaults defer to `portable-implementation-and-hardcoding-control.md`; source/destination and cross-reference consistency defer to `document-consistency.md`.
- Required document set, versions, metadata, full-history links, parent links, and active session IDs align with the governing chain. Active metadata must use real session identifiers; placeholders are not valid in active governed artifacts.
- Phase records preserve live phase workspace boundaries, current/future phase distinction, and enough lineage for major-vs-subphase decisions.
- Patch artifacts stay outside live phase namespace, remain before/after review surfaces, and show phase-to-patch linkage when patch participates.
- Built-in task lists remain live tracking, normally reused/extended within one active objective, and never downgrade required design/changelog/TODO/phase/patch surfaces.
- Shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES scope; helper/support/extension artifacts stay non-governed unless intentionally promoted. If those mechanisms need authority later, promote them through an explicit governed chain rather than by side-effect reference.
---
## Verification Checklist
- [ ] Required document set, versions, metadata, full-history/parent links, and active session IDs align.
- [ ] Startup posture is resolved; required governed companions and live task tracking are not downgraded.
- [ ] Active design/changelog, phase, patch, TODO, and completed-history boundaries remain distinct.
- [ ] Phase lineage and phase file selection defer to `phase-implementation.md`.
- [ ] Patch surfaces stay self-identifying, before/after-oriented, and outside live phase planning.
- [ ] Public onboarding/support artifacts stay portable and source-vs-destination wording is distinct.
- [ ] Runtime install scope is limited to current project/source-owned active runtime rule files.
- [ ] Other-owner runtime files and unclear files are not classified, managed, or deleted without owner/project scope and stronger authority.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Document coverage, metadata, version, and links | 100% |
| Design/changelog/phase/patch/TODO role boundaries | 100% |
| Completed-history inactive-surface boundary | 100% |
| Startup posture and phase-to-patch linkage when in scope | 100% |
| Public onboarding portability and source/destination clarity | High |
| Runtime install and shared-destination owner boundaries | 100% |
---
## Integration
| Rule | Relationship |
|---|---|
| [artifact-initiation-control.md](artifact-initiation-control.md) v1.7 | startup artifact-resolution owner |
| [document-changelog-control.md](document-changelog-control.md) v4.8 | version authority and `changelog/done/` completed history boundary |
| [document-design-control.md](document-design-control.md) v1.10 | design structure and no-default-`design/done/` boundary |
| [document-patch-control.md](document-patch-control.md) v2.7 | patch boundary, before/after contract, and `patch/done/` completed history boundary |
| [phase-implementation.md](phase-implementation.md) v2.26 | phased execution semantics, major-vs-subphase lineage selection, and `phase/done/` completed history boundary |
| [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) v1.2 | portable shared-artifact defaults |
| [document-consistency.md](document-consistency.md) v1.8 | source/destination and source-owned/shared-destination reference consistency |
| [todo-standards.md](todo-standards.md) v2.17 | TODO structure and startup bridge |
| [design/rules-plugin-extension.design.md](design/rules-plugin-extension.design.md) | historical plugin-extension boundary; active plugin/runtime coordination is not Main RULES doctrine |
---
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
