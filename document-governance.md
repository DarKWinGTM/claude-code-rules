# Document Governance
> **Current Version:** 1.16
> **Design:** [design/document-governance.design.md](design/document-governance.design.md) v1.16
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
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

### 5.2) Governed chain model
Before appending, splitting, or normalizing a design/changelog chain, resolve:
- namespace: one folder-scoped chain or a shared multi-chain folder
- subject and active parent: a generic parent is valid for one folder-scoped chain; shared folders use a self-identifying semantic parent derived from the actual subject
- authority: exactly one active parent model; any coexisting parent is explicitly compatibility-only or inactive
- shape: `single-file-bootstrap`, `flat-sibling-shards`, `same-stem-subfolder-normalized`, or `archive-history-fallback`
- transition basis: bootstrap exit trigger, shard-opening basis, append-vs-shard reason, and parent-index update need

Keep bootstrap while the parent is compact and coherent. Flat siblings fit a folder that already scopes one chain and only a few coherent slices; the parent declares the shape and shard map. Same-stem normalization is preferred for broad, multi-shard, root-heavy, or God-file-prone chains only after a checked opening basis. Archive/history fallback is inactive and never the ordinary active-detail namespace. Do not infer a nested directory from the parent filename alone.

The parent remains the bodyful authority gateway and names the active shape/map. Child/detail shards remain reachable, coherent, back-linked, and non-duplicative. Before appending, classify the detail as current state, history, verification, risk, or next work; plan repair instead when destination or authority is ambiguous.

When an example informs the decision, keep `observed project shape`, `extracted doctrine`, and `selected target form` distinct. Placeholder names remain examples, and exact equivalence must not be claimed without checked proof.

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
README/onboarding/install artifacts apply the canonical binding and notation contract in `portable-implementation-and-hardcoding-control.md`. This document owner additionally keeps public install scope limited to the current source-owned active runtime set rather than every file in a shared destination.

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
Apply the governed-chain model in Part A. A design parent remains a bodyful target-state authority gateway; child shards own coherent active target-state slices, identify parent scope, remain reachable through the parent map, and do not become history by default. Retiring or superseding a shard requires governed design/changelog alignment, not quiet removal or reclassification.

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

### 2) Version-detail sharding and fallback history
Apply the governed-chain model in Part A. The active changelog parent owns current version, index, map, and navigation. Each version detail has one active owner, uses a self-identifying version/topic filename when sharded, and keeps resolvable parent/back links. Preserve exact historical content during migration unless an explicit governed rewrite is selected.

`changelog/done/` is inactive legacy/archive/completed/fallback history for audit, rollback, provenance, or trace reconstruction. It is not the ordinary same-chain detail namespace, junk classification, or deletion authority.

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

### 5) Runtime validation gate
A README-listed active runtime file is eligible for parity/install claims only when it exists at source root, carries `Current Version`, `Design`, `Session`, and `Full history`, has a substantive runtime body, and aligns runtime/design/changelog versions. Missing files/metadata, metadata-only roots, hash-only checks, mixed `Based on`/`Design`, or install scope widened into governed/support surfaces invalidate the claim.

---

## Cross-Document Alignment and God-File Prevention
Keep applicable versions, canonical metadata and real session IDs, history/parent/map/back links, runtime body sufficiency, source-owned install scope, phase/patch boundaries, owner-aligned sync lanes, and portable source/destination wording aligned. Shared runtime co-location does not grant ownership; classify, manage, or delete another owner's file only after owner/project scope is verified.

When an active document mixes target state, history, execution, verification, rollback, roadmap, or operations, keep its primary role and route detail to the owning design shard, changelog shard/fallback, TODO/phase history, phase/patch split, or README current-state surface. Preserve history; overload repair is not deletion authority. Touched God pressure must be repaired or visibly planned, deferred, or blocked before sync/closeout.

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
| public onboarding/install docs | apply the portability owner while preserving source-owned runtime install scope |
| touched governed doc with mixed roles | repair clear overload now or create an explicit owner-specific repair slice |

---

## Anti-Patterns
Avoid README/design/changelog/phase/patch role collapse; `changelog/done/` as ordinary active detail; metadata-only runtime roots; unclassified `sync everything` sweeps; unnecessary broad lanes for tiny fixes; runtime install scope widened into governed/support files; public guidance that violates the portability owner; completed/inactive content treated as junk; or quiet removal/reclassification instead of governed sharding, rollover, split, or history movement.

---

## Integration
Related owners:
- [document-integrity.md](document-integrity.md) / [phase-todo-artifact.md](phase-todo-artifact.md) — references, rollover, startup, phase/TODO
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) — binding and public onboarding notation
- [worker-routing-and-context.md](worker-routing-and-context.md) / [safe-io.md](safe-io.md) — broad governance lanes and bounded reads
- [accurate-communication.md](accurate-communication.md) / [coding-discipline.md](coding-discipline.md) — claim strength and coding verification
