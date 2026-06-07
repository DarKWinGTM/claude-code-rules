# Document Governance
> **Current Version:** 1.15
> **Design:** [design/document-governance.design.md](design/document-governance.design.md) v1.15
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/document-governance.changelog.md](changelog/document-governance.changelog.md)
> **Absorbed:** project-documentation-standards v2.41, document-design-control v1.12, document-changelog-control v4.12, document-patch-control v2.9, unified-version-control-system v1.3

---

## Rule Statement

**Core Principle: Govern governed documentation as one deterministic system: keep active runtime rules body-sufficient, keep design as active textual target-state truth, keep `diagram/` as the required governed Kroki-compatible visual infrastructure lane for project structure mapping, require governed diagram source to stay Kroki-compatible and governance-suitable, require `diagram/STRUCTURE.md` as the compact active diagram-side entrypoint, keep changelog as version/history authority, resolve namespace scope and choose one active parent model before appending or sharding detail, allow generic parents when the current folder fully scopes one chain, keep bootstrap-first behavior until checked triggers justify shards, classify governed design/diagram/changelog chain shape before opening or expanding shard structure, keep patch as before/after review outside live phase planning, recognize governance/release-sync work shapes before deep execution, preserve compact active entrypoints with referenced history surfaces, and keep public onboarding/install guidance portable.**

This rule unifies repository documentation baseline, design/changelog/patch role boundaries, completed-surface governance, and UDVC-1 version-control discipline. It keeps one clear owner per document role so active docs remain understandable, auditable, and cheap to maintain.

พูดง่าย ๆ: README คือ front page, design คือ textual truth, `diagram/` คือ visual lane, changelog คือ version/history, patch คือ before/after review, runtime root rules ต้องมี body จริง, และทุกอย่างต้องไม่แย่งกันเป็น authority เดียวกันมั่ว ๆ.

---

## Part A — Repository Documentation Baseline

### 1) Required document set
Use one deterministic documentation baseline across the repository.

Required surfaces when applicable:
- `README.md` — overview / onboarding / current-state front page
- `design/*.design.md` — active target behavior / contract / blueprint
- `design/<slug>/*.design.md` — active child target-state shards for large designs
- `diagram/STRUCTURE.md` — mandatory compact active Kroki-compatible whole-project visual structure authority and diagram entrypoint
- `diagram/*.design.md` — Kroki-compatible integrated subject-level diagram documents in the dedicated visual lane
- `diagram/<subject>/*.design.md` — Kroki-compatible child visual shards when visual complexity justifies a split
- `diagram/history/` and `diagram/done/` — referenced prior-state and completed-detail preservation surfaces when diagram infrastructure is rolled over
- `changelog/*.changelog.md` — active parent version authority, current index, shard map when present, and navigation
- `changelog/<chain>/v*.changelog.md` — indexed same-chain version detail shards
- `changelog/done/*.changelog.md` — legacy/archive/completed-history/fallback changelog detail
- `TODO.md` — compact durable current execution index
- `todo/history/` and `todo/done/` — referenced TODO history/detail surfaces
- `phase/SUMMARY.md` plus `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, and `phase/phase-NNN-NN-NN-*.md` — live staged execution
- `phase/history/` and `phase/done/` — referenced/inactive phase history
- `patch/<context>.patch.md` or root `<context>.patch.md` — active review artifact outside phase
- `patch/done/` — inactive completed patch history
- helper/support surfaces such as `template/**`, `support/**`, `plugin/**` remain non-governed unless explicitly promoted

### 2) Governance update order
Default governed sync order:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync when affected

Active metadata must use real session identifiers; placeholders are not allowed in active governed artifacts.

### 3) Role boundaries
Each document family keeps one primary role.
- **README** is the current front page, not the history book
- README capability/current-state sections should explain active doctrine and current-state behavior in user-facing terms, not retell phase/release execution chronology as the meaning of the capability itself
- **design** is active target-state truth and durable rationale/contract owner, not changelog history, phase execution, patch review, or completed-work storage
- **diagram** is the required governed Kroki-compatible visual infrastructure lane for project structure mapping and diagram routing, not semantic truth over design
- **changelog** is current version/history authority, not phase-definition storage
- **TODO** is the compact durable current-state execution index, not the primary live board
- **phase** is live staged execution and provenance, not design, patch, or code naming authority
- **patch** is before/after review outside live phase planning, not the durable design contract or staged execution owner
- **source comments** may point to governed design, phase, or patch docs when useful, but they stay navigational/contextual and do not become a new authority layer
- phase chronology may explain provenance, but it must not become source-code naming authority for functions, classes, modules, routes, or config keys
- **helper/support** artifacts do not become authority just because they exist near governed files

### 4) Completed documentation surfaces
Completed surfaces reduce active scan bloat without deleting governed history.
- allowed inactive/referenced history: `todo/history/`, `todo/done/`, `phase/history/`, `phase/done/`, `patch/done/`, `changelog/done/`, and when the diagram family rolls over, `diagram/history/` plus `diagram/done/`
- active changelog detail shards under `changelog/<chain>/v*.changelog.md` remain reachable through the active parent changelog
- design has **no default** `design/done/`; design remains active blueprint authority until superseded
- completed status is not junk classification or deletion authorization
- active entrypoints must keep enough pointers so moved history remains reachable

### 5) Current-state scan order
Current-state scans should start from active entrypoints and checked implementation state:
- `README.md`
- active design parent indexes and needed child shards
- active diagram structure/subject surfaces when a governed diagram lane exists
- active parent changelogs and needed version-detail shards
- compact `TODO.md`
- compact `phase/SUMMARY.md`
- active phase / patch files
- checked implementation state

Open `done/` or archive surfaces only through active references or for history, audit, rollback, provenance, or trace reconstruction.

### 5.1) Governance and release-sync work-shape recognition
When work touches several governed surfaces, classify the work shape before deep execution.
- distinguish focused document edit, owner-aligned sync, broad release-ready/no-drift audit, history rollover, and before/after patch review
- decompose broad governance or release-sync objectives into owner-aligned lanes such as design truth update, diagram truth update, runtime rule sync, changelog sync, TODO/phase sync, patch metadata final sync, or release audit
- use this decomposition to preserve role boundaries and reduce reread churn
- `worker-routing-and-context.md` owns whether a lane becomes a worker and `safe-io.md` owns bounded file/command absorption during multi-surface review
- do not force lane decomposition or delegation for tiny local sync or one-surface metadata fixes

### 5.2) Governed design/changelog chain-shape classification
Before appending new target-state or version-detail content into a governed design/changelog parent, classify the active chain naming basis and chain shape first.

Named shapes:
- `single-file-bootstrap`
- `flat-sibling-shards`
- `same-stem-subfolder-normalized`
- `archive-history-fallback`

Required guidance:
- first decide whether the current folder is the full namespace for one chain or a shared folder that contains several chains
- if the current folder fully scopes one chain, a generic parent such as `design/design.md` or `changelog/changelog.md` is valid
- if the current folder contains several chains, use a subject-derived semantic parent filename so the chain stays self-identifying inside that shared folder
- placeholder examples are illustrative only; they must not be copied forward as mandatory literal active filenames unless the checked chain subject actually matches the example
- one chain must keep exactly one active parent model: generic parent or semantic parent, never both at the same time
- use `single-file-bootstrap` only while the parent remains compact, coherent, and not yet detail-heavy enough to justify active shards
- if a chain still has one compact design body and no checked `bootstrap_exit_trigger`, keep it bootstrap-first instead of opening a same-stem shard directory early
- `flat-sibling-shards` is allowed when the current folder already acts as the chain namespace and only a few coherent slices are needed; the compact parent stays the authority gateway and names the active shard map
- `same-stem-subfolder-normalized` remains the strong-preferred form for broad, root-heavy, multi-shard, or God-file-prone chains once checked `shard_opening_basis` justifies the split
- `archive-history-fallback` remains inactive by default and must not become the ordinary active detail namespace by momentum
- do not create a same-stem nested shard directory merely because a parent named `design.md` or `changelog.md` exists; first check whether the current folder already scopes the chain and whether a real shard-opening basis exists
- when a parent has active shards, it should expose the selected chain shape, shard map, append-vs-shard posture, and the checked reason why the chain no longer stays bootstrap-only

### 5.2.1) Append-vs-restructure-and-shard gate
Before appending to an active governed design/changelog parent, decide whether the detail still belongs in the parent or whether it should trigger restructuring, a new sibling/child shard, or a history/done reference instead.

Required guidance:
- classify whether the new detail is current state, history, verification, risk, or next work
- do not append silently when the target line already mixes several responsibilities or would create a very large diff for a small logical change
- when the target is a compact governed design/changelog parent, resolve namespace scope, actual chain subject, parent model choice, active-versus-compatibility coexistence, current chain shape, and shard-opening basis before adding more detail
- if the folder already fully scopes one chain, generic parents such as `design/design.md` or `changelog/changelog.md` may remain active bootstrap parents until checked triggers justify broader structure
- if the folder is shared by several chains, prefer a self-identifying semantic parent
- keep older completed-history wording historical only when chronology conflicts; active runtime/design doctrine still controls current interpretation unless an active surface selects otherwise
- flag or plan the repair instead of appending when the split or destination remains broad, meaning-risky, or authority-ambiguous

### 5.3) Observed project shape versus extracted doctrine versus selected target form
When a checked project, subsystem, repo, or prior governed chain is used to justify a documentation shape, keep three meanings separate:
- `observed project shape` = the structure actually verified in the checked example
- `extracted doctrine` = the reusable governance principle inferred from that observed shape
- `selected target form` = the normalized structure intentionally chosen for the current governed chain

Keep owner and naming decisions separate from those three meanings when they materially affect structure:
- `actual chain subject` = the real topic/capsule/component the current chain is about
- `selected parent filename` = the active filename chosen for this chain, whether generic or semantic
- `parent model choice` = whether the chain uses a generic parent or a semantic parent
- `single-parent authority basis` = why that one active parent model is the correct choice for this chain

Required guidance:
- do not describe an extracted doctrine as the literal observed project pattern unless checked evidence confirms that equivalence
- a checked example may ground a recommendation without proving that the current selected target form is the only valid design
- if the checked example and the selected target form differ, say both explicitly and name why the target form is still being selected
- keep the selected parent filename aligned to namespace scope and the actual chain subject instead of to a placeholder example name, unless the checked subject really matches that name
- if a folder already fully scopes one chain, a generic parent may be the selected active owner; if the folder is shared, a semantic parent is usually the clearer choice
- if both a generic parent and a semantic parent exist for one chain, only one may remain active authority; the other must be explicitly compatibility-only or inactive
- if reachable completed phase, patch, or changelog detail preserves an older released doctrine, active runtime/design doctrine plus the latest released baseline still control current interpretation; older history remains provenance unless an active surface selects it as current authority
- chain-shape selection for the current repo is governed by checked current need plus active doctrine, not by loose analogy to an example project
- if equivalence between the observed example and the selected target form is not checked, avoid wording such as `project-style`, `the project uses this exact form`, or equivalent claim-collapsing phrasing

Preferred wording:
- `In the checked file/output, the observed project shape is ...`
- `The extracted doctrine is ...`
- `For this RULES chain, the selected target form is ...`
- `The checked evidence grounds this recommendation, but it does not prove this is the only valid design.`

### 5.4) Governed diagram lane
For RULES, use a dedicated `diagram/` lane as required governed-docs infrastructure instead of forcing diagrams into `design/**` shards or plugin-owned preview surfaces.

Required guidance:
- `design/` stays textual target-state authority; `diagram/` is the visual synthesis and project-structure mapping lane
- governed diagram source must be Kroki-compatible always
- supported diagram formats are all formats that are both Kroki-compatible and governance-suitable
- governance-suitable means the source is text-governable, diff/review-friendly, semantically stable enough for source truth, and portable enough for repo-governed workflow
- `diagram/STRUCTURE.md` is mandatory as the compact active bodyful whole-project visual structure authority, not a shallow link/index router
- `diagram/STRUCTURE.md` must map main project concepts, source/code/folder/directory topology, authority boundaries, and diagram-to-diagram relationships while routing readers to deeper diagram files without needing to inline every child diagram body
- `diagram/<subject>.design.md` is the default bodyful integrated subject diagram and should act as a zoom-in / decomposition view of the global structure
- child visual shards under `diagram/<subject>/` open only when visual complexity or genuinely different visual questions justify the split
- do not mirror design shards automatically just because text design already split
- if design and diagram differ, `design/` remains semantic authority
- inline answer/status/phase-local text diagrams do not become governed `diagram/` source truth automatically
- plugin/preview/manifest/report output stays support-only and must not become source truth
- if the diagram family later needs rollover, `diagram/history/` preserves prior active state and `diagram/done/` preserves completed detail; these surfaces remain preservation infrastructure rather than cleanup authority

### 6) Public onboarding and install portability
README/onboarding/install docs stay portable by default.
- prefer repo-root-relative source guidance for cloneable/self-contained repos
- do not present workstation absolute paths or internal umbrella roots as public defaults
- distinguish source-side notation from destination/runtime notation
- use placeholders or contract labels for destination/runtime paths
- when naming runtime install scope, identify the current source-owned active runtime rule set rather than the whole shared destination directory
- exact local paths may appear only as checked local facts, local examples, or machine-scoped contracts
- if an exact local value must appear for debugging or audit, label it as local-only and do not let it become the reusable default

---

## Part B — Design Governance

### 1) Design as active target-state authority
Governed design documents define the current implementation-relevant target-state truth.
- design bodies should describe what the system should be now or next, not how every prior wave got there
- active design is not a changelog/history dump, completed-work record, audit snapshot, rollback journal, or detailed release timeline
- if historical detail is still useful, keep it reachable through changelog governance rather than embedding it as active design body
- retained legacy snapshots must be labeled historical/reference-only and kept outside active design authority

### 2) No default `design/done`
`design/` remains active blueprint authority and has no default `design/done` surface. Active target truth stays in current design files until superseded or removed from target state.

### 3) Governed design sharding
Large active design documents may use:
- compact parent index at `design/<slug>.design.md`
- governed child shards under `design/<slug>/*.design.md`
- flat sibling child shards beside a compact parent when the current folder already acts as the chain namespace and a same-stem nested folder would be redundant too early

Required guidance:
- if the current folder fully scopes one chain, `design/design.md` may be the active parent index and authority gateway
- if the current folder is shared by several chains, use `design/<slug>.design.md` so the chain stays self-identifying in that shared folder
- broad or God-file-prone active design chains should strongly prefer a same-stem normalized path pair once checked shard-opening basis justifies that split
- if the chain still has one compact design body, keep the chosen active parent as `single-file-bootstrap` until a checked `bootstrap_exit_trigger` justifies shards
- flat sibling child shards are allowed only when the current folder already scopes the chain; the compact parent must declare that mode and name the active shard map
- the parent file remains the active design index and authority gateway, not a placeholder or link-only router
- generic and semantic active parents must not compete as steady-state owners for the same chain
- child shards remain active target-state truth by default, not inactive history or changelog substitutes
- the parent index should preserve purpose, authority, current target-state summary, shard map, selected chain shape, and enough context to choose relevant shards without broad raw absorption
- each child shard should identify parent scope, own one coherent target-state slice, and avoid duplicating/conflicting with sibling authority
- child shards should carry parent backlink plus version/session and stable section/provenance fields when practical
- broad shard audits should use shard maps, targeted reads, and worker filtering when context-heavy
- retiring or superseding shard content requires governed design/changelog alignment rather than quiet removal or reclassification

### 4) External-doc-derived knowledge capture
When external docs, API specs, or provider references materially constrain implementation, normalize the extracted implementation truth into governed design before or alongside continued multi-step work that depends on it.

A good capture should make later implementation able to answer:
- what the external source requires and which implementation part is constrained
- what values, fields, parameters, flows, states, auth/callback rules, or acceptance criteria matter
- what should be sent, accepted, stored, validated, rejected, or kept out of active target truth
- which details are source-side background rather than implementation truth to carry forward

### 5) Design alignment boundary
For governed chains, design version must align with:
- runtime rule `Current Version`
- runtime rule `Design` reference version
- changelog `Current Version`

Design alignment is target-state alignment, not permission to duplicate changelog history inside the active design body.
When a paired changelog exists, design navigation is limited to `Full history`; do not embed detailed changelog sections or duplicate historical summaries in the active body.

### 6) Design God-file prevention
A design document becomes a God file when it stops being active target-state truth and absorbs changelog history, phase execution, TODO tracking, patch review, audit notes, rollback journals, or multiple unrelated design domains.

Repair posture:
- keep current implementation-relevant target state in design
- shard large active target-state scope through a compact parent index and coherent child shards
- move historical explanation to changelog governance instead of active design body
- keep phase sequencing and patch before/after review in their owning surfaces
- split unrelated design domains instead of expanding one parent index into an umbrella design dump

---

## Part C — Changelog Governance

### 1) Active parent changelog authority
Each governed chain keeps one active authoritative parent changelog.
It owns:
- current version authority
- current index
- shard map when present
- forward navigation

Runtime, design, phase, patch, and TODO sync align to the parent changelog version state when applicable. Changelog records shipped/synchronized history and version authority; it should not become phase-definition storage, duplicate active design target-state truth, or serve as README current-state content.

### 2) Chain-scoped version detail shards
Large governed chains may split detailed version sections into chain-scoped version detail shards under `changelog/<chain>/vX.YY-short-topic.changelog.md`.

Required guidance:
- if the current folder fully scopes one chain, `changelog/changelog.md` may be the active parent authority, index, shard map, and navigation surface
- if the current folder is shared by several chains, use `changelog/<chain>.changelog.md` so the chain stays self-identifying in that shared folder
- broad or God-file-prone active changelog chains should strongly prefer a same-stem normalized path pair once checked shard-opening basis justifies that split
- if the chain still has one compact changelog body, keep the chosen active parent as `single-file-bootstrap` until a checked `bootstrap_exit_trigger` or version-detail pressure justifies shards
- flat sibling version-detail shards are allowed when the current folder already scopes the chain and only a small number of coherent version-detail files is needed; the compact parent must declare that mode and name the active shard map
- generic and semantic active parents must not compete as steady-state owners for the same chain
- place same-chain detailed entries in `changelog/<chain>/vX.YY-short-topic.changelog.md` when sharding is needed, or in flat sibling version files beside the parent when flat sibling mode is explicitly selected
- use self-identifying shard filenames that include version and short topic
- keep parent-to-shard and shard-to-parent links resolvable
- version shards should carry parent backlink plus parent-document/reference metadata and stable provenance fields when practical
- keep one version-detail entry in one active shard or in the parent, not duplicated as competing authority
- preserve exact historical content during migration unless an explicit governed rewrite is selected
- do not create a God directory where the parent no longer tells readers which shard owns which version detail

### 3) `changelog/done/` boundary
`changelog/done/` remains allowed for legacy, archive, completed-history, or explicit fallback cases where chain-scoped version shards are not the right shape.
- it is inactive by default
- it is used only for history, audit, rollback, provenance, or trace reconstruction
- it is never deletion authority or junk classification
- it is not the default ordinary same-chain detail-shard namespace

### 4) Changelog vs daily movement boundary
Daily-first rollover for `TODO.md` and `phase/SUMMARY.md` stays with their dedicated owners. Changelog history remains version authority and should not absorb ordinary TODO/phase daily movement by default.

README remains the current-state front page for overview, install, active count, latest refinement, and current quality signals. Detailed version timelines belong in changelog governance, not README release-sync dumps.

### 5) Changelog God-file prevention
A changelog becomes a God file when current version authority turns into phase planning, design target-state storage, TODO tracking, release dashboarding, or detailed history that makes the active changelog hard to scan.

Repair posture:
- keep the active parent changelog as current version, index, shard map, and navigation authority
- move bulky same-chain version detail into chain-scoped version shards when active scans bloat
- use `changelog/done/` only for legacy/archive/completed-history/fallback cases
- keep design target state in design, phase execution in phase, TODO tracking in TODO, and current front-page status in README
- avoid appending release prose that duplicates active README, TODO, phase, or patch content

---

## Part D — Patch Governance

### 1) Patch meaning and location
A patch is a governed before/during-execution change artifact showing **what will change**.
It must let a reviewer identify:
- target artifact or stable target location
- current/before state
- target/after state
- change type: `additive`, `replacement`, `deletion`, or `restructuring`

A patch is not a retrospective summary, phase summary, rollout dashboard, prose-only recap, deletion authority, or generic plan with unclear before/after delta.

Allowed locations:
- `patch/<context>.patch.md` for active review
- `patch/done/<context>.patch.md` for inactive completed history
- root `<context>.patch.md` when top-level placement is clearer

Filenames must be self-identifying and version-suffix-free; generic `patch.md` is not allowed.

### 2) Patch metadata and alignment
Patch metadata must include:
- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history`

Patch changelog metadata must include:
- `Parent Document`
- `Current Version`
- `Session`

Integrity requirements:
- active patch metadata must use real session IDs; placeholders are not allowed
- `LEGACY-*` is allowed only for historical records when original session data is unavailable
- patch `Current Version` must align with patch changelog `Current Version`
- `Target Design` must resolve to an existing design document/version
- patch metadata synchronization follows governance order with final patch sync when affected
- metadata alignment proves review-surface integrity only; it does not make patch the version authority or move design/phase responsibilities into patch

### 3) Patch structure and reviewability
Every governed patch must include:
1. Context
2. Analysis
3. Change items
4. Verification
5. Rollback approach

Each concrete change item must show:
- target artifact or stable target location
- change type
- current/before state
- target/after state
- enough comparison detail for review

Preferred comparison forms include before/after snippets, current/target tables, unified diff blocks, patch hunk sections with target path and anchors, or scoped command/config replacement blocks.

Acceptable target locators include file path, section heading, function/class/query name, config key path, route/endpoint name, command block label, or schema object/table/column reference. If line numbers are unstable, use the most precise stable locator.

Non-code or governance-only patches may omit snippets only when they explicitly say the patch is non-code/non-snippet, the change surface is conceptual/governance/structural, and concrete runtime edits are intentionally out of scope.

### 4) External-requirement basis in patch
When a change is constrained by external docs, API specs, or provider references, the patch should make the implementation-relevant basis visible enough for review.
- point to normalized design truth when design already owns the extracted requirement
- patch may summarize the change-driving requirement but must not replace design as target-state truth
- if external requirements determine request parameters, authentication, callbacks, acceptance criteria, field semantics, or integration constraints, make that basis legible in context/analysis
- do not rely on transient doc-reading memory alone for later review passes

### 5) Patch vs phase authority split
Patch owns tactical before/after review. Phase owns live staged execution.
`/patch` must not become:
- the live phase-plan namespace
- the active phase summary/index
- per-phase execution file storage

`patch/done/` is inactive completed patch history, not junk or default active input.

### 6) God Patch prevention
A God Patch is a patch artifact that tries to review several unrelated before/after changes, execution phases, release history, TODO state, and rollback plans in one file.

Repair posture:
- keep each patch centered on a coherent review target or change family
- split patch artifacts when target artifacts, change types, review boundaries, or rollback paths diverge
- keep live phased execution in `/phase`, not in `/patch`
- keep detailed version history in changelog, not in patch body
- move completed patch detail to `patch/done/` only after active review closes
- preserve reviewability after any split
- block patch closeout while touched-scope God Patch pressure remains unrepaired or unplanned

---

## Part E — Unified Version-Control Governance (UDVC-1)

### 1) Single governance mechanism
UDVC-1 is the only version-governance mechanism for governed RULES chains.
- do not introduce parallel version authorities
- keep each governed chain aligned through runtime, design, and changelog surfaces
- use changelog as version/history authority, design as active target-state authority, and root runtime rule as active behavior contract

### 2) Single authority per chain role
Each governed chain has distinct roles:
- root runtime rule → active behavior contract loaded by runtime
- design → active target-state, rationale, and design authority
- changelog → current version and version history authority
- `TODO.md` → durable execution tracking
- `phase/` → live staged execution
- `patch/` → before/after review artifact

Required guidance:
- design cannot replace the runtime body for an active installed rule
- changelog claims do not prove runtime behavior exists when the root body is missing
- README install arrays define the source-owned active runtime set and do not widen scope to design/changelog/TODO/phase/patch files

### 3) Runtime header contract
Root active runtime rules use canonical metadata:
- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the canonical design reference label. `Based on:` is retired in active root runtime metadata.

### 4) Active runtime body sufficiency
A README-listed active runtime rule is invalid if it is metadata-only.
Minimum body requirements:
- substantive rule statement or equivalent behavior contract
- operational guidance that can affect runtime behavior
- relevant boundaries, triggers, anti-patterns, verification, or integration guidance
- enough body content to distinguish active runtime behavior from a design pointer

Required guidance:
- source/runtime parity must include body sufficiency, not only hash equality
- a root runtime file with only title/version/design/session metadata cannot satisfy active rule-install claims
- body sufficiency should be checked before claiming no-drift, runtime parity, release readiness, or active rule install success

### 5) Validation model
For each README-listed active runtime file:
```text
Active runtime file listed
  ↓
File exists at source root?
  → NO: install set invalid
  → YES: continue
  ↓
Canonical metadata includes Current Version, Design, Session, Full history?
  → NO: metadata invalid
  → YES: continue
  ↓
Substantive runtime body exists after metadata?
  → NO: metadata-only stub; runtime install invalid
  → YES: continue
  ↓
Runtime/design/changelog versions align?
  → NO: chain sync invalid
  → YES: eligible for runtime parity/install claim
```

### 6) UDVC anti-patterns
Avoid:
- active runtime root files that only point to design
- treating design bodies as installed runtime behavior
- changelog entries that say runtime updated while the root runtime body is empty
- parity checks that compare hashes but ignore semantic body sufficiency
- mixed `Based on` and `Design` labels in active root metadata
- README install scope drifting into design/changelog/TODO/phase/patch surfaces

---

## Cross-Document Alignment and God-File Prevention

### 1) Cross-document alignment
Keep these aligned across the governed chain when applicable:
- versions
- metadata
- full-history links
- parent links
- active parent changelog shard maps and version-detail shard back-links
- active session IDs
- source/runtime parity and body sufficiency
- phase-vs-patch boundaries
- broad governance/release-sync lanes staying inside their owner surfaces or tightly coupled sync slices
- source/destination wording in public onboarding
- runtime install scope limits to current source-owned active rule files

### 2) Active metadata must be real
Active governed artifacts must use real session identifiers. Placeholder markers are not valid in active metadata.

### 3) Runtime destination scope boundary
Shared runtime destinations may contain other project/plugin-owned runtime files. Current repo docs must not classify, manage, or delete them unless owner/project scope is selected or verified. Runtime co-location is an observation, not ownership authority.

### 4) Governed document God-file prevention
A God file appears when one active document becomes owner for several roles at once.
Common overload roles include target-state design, release history, execution tracking, verification proof, rollback detail, roadmap, and operational notes.

Required repair posture:
- identify the document's primary role before appending content
- move or link content to the owning surface when it belongs elsewhere
- shard active design truth when design scope is genuinely large
- shard bulky same-chain changelog version detail under `changelog/<chain>/v*.changelog.md` while preserving parent authority
- roll accumulated daily movement or completed detail into allowed history/done surfaces
- split phase and patch files when their goals/outputs/gates/rollback/review boundaries diverge
- keep README current-state focused and delegate history to governed owner chains
- preserve history and owner scope; God-file repair is not deletion authority

### 5) Automatic God-artifact planning
A detected God artifact must have an owner outcome before governed work can be called synchronized.
- repair clear touched-scope overload in the owning document when safe
- route broader repair to design sharding, changelog version-detail sharding, changelog/done fallback history, TODO history/done, phase split, patch split, or README current-state reduction
- create or extend a visible repair slice when the repair is real but not safe to complete immediately
- keep planned repair compact and owner-specific instead of turning another surface into a God file
- block closeout when touched-scope God pressure has no repaired, planned, deferred, or blocked owner state

---

## Trigger Model

| Trigger | Required handling |
|---|---|
| new governed chain or version-impacting behavior | establish design/changelog/runtime alignment through UDVC-1 |
| large active design body | use compact parent design index plus coherent child shards |
| bulky same-chain version history | keep active parent changelog authority and offload detail into `changelog/<chain>/v*.changelog.md` |
| ordinary completed/history detail | move into allowed `history/` / `done/` surfaces without deleting meaning |
| broad governance/release-sync request touches several owner surfaces | classify the work shape and decompose it into owner-aligned sync or audit lanes before deep execution |
| before/after review need | use patch outside live phase planning |
| README release sync | update current-state sections, not long version timelines |
| metadata-only runtime root | treat as invalid active runtime install state |
| public onboarding/install docs | keep source-side and destination/runtime guidance distinct and portable |
| touched governed doc with mixed roles | repair clear overload now or create an explicit owner-specific repair slice |

---

## Anti-Patterns

Avoid:
- using README as a changelog timeline dump
- using design as completed-history storage or default `design/done`
- using changelog as phase planner or TODO tracker
- using patch as a live phase workspace
- treating `changelog/done/` as ordinary same-chain shard storage by default
- active runtime roots that are metadata-only stubs
- broad governance/release-sync sweeps with no work-shape classification
- one generic `sync everything` lane that blurs design/changelog/TODO/phase/patch ownership
- forcing delegation or broad multi-surface lane decomposition for a tiny one-surface fix
- letting runtime install scope drift into design/changelog/TODO/phase/patch/helper surfaces
- mixing source-side and destination/runtime wording in public install guidance
- treating completed/inactive surfaces as junk or deletion authority
- quiet file removal or authority reclassification when the correct response is sharding, rollover, split, or explicit history movement

---

## Integration

Related rules:
- [document-integrity.md](document-integrity.md) - cross-reference consistency, rollover/hygiene boundaries, and no-drift checks
- [phase-todo-artifact.md](phase-todo-artifact.md) - startup artifact posture, live phase semantics, TODO/live-task doctrine
- [accurate-communication.md](accurate-communication.md) - evidence-strength wording for sync/parity/readiness claims
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable shared-artifact defaults and public onboarding portability
- [worker-routing-and-context.md](worker-routing-and-context.md) - worker scale and lane routing for broad governance/release-sync work
- [safe-io.md](safe-io.md) - bounded file reading and parent-index/shard-first reading behavior
- [coding-discipline.md](coding-discipline.md) - coding verification depth when phase/changelog/closeout claims depend on tested behavior
