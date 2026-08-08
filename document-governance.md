# Document Governance
> **Current Version:** 1.17
> **Design:** [design/document-governance.design.md](design/document-governance.design.md) v1.17
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/document-governance.changelog.md](changelog/document-governance.changelog.md)
> **Absorbed:** project-documentation-standards v2.41, document-design-control v1.12, document-changelog-control v4.12, document-patch-control v2.9, unified-version-control-system v1.3

---

## Rule Statement

**Core Principle: Govern documentation through one owner per role: runtime Rules are body-sufficient behavior contracts, design is active textual target-state truth, `diagram/` is the required Kroki-compatible visual lane, changelog owns version/history, TODO and phase own execution state, and patch owns before/after review. Resolve namespace, parent authority, and chain shape before growth; preserve reachable history, compact active entrypoints, portable onboarding, and source-owned install scope.**

พูดง่าย ๆ: README คือ front page, design คือ textual truth, `diagram/` คือ visual lane, changelog คือ version/history, phase/TODO คือ execution, patch คือ before/after review, และแต่ละ role ต้องมี owner เดียว.

---

## Part A — Repository Documentation Baseline

### 1) Required surfaces and roles

| Surface | Primary role |
|---|---|
| `README.md` | overview, onboarding, current-state front page; not detailed history |
| `design/*.design.md`, `design/<slug>/*.design.md` | active target behavior, contract, rationale, and coherent child shards |
| `diagram/STRUCTURE.md` | mandatory compact, bodyful whole-project visual structure authority and diagram entrypoint |
| `diagram/*.design.md`, `diagram/<subject>/*.design.md` | Kroki-compatible integrated subject diagrams and justified visual shards |
| `changelog/*.changelog.md` | active current-version authority, index, map, and navigation |
| `changelog/<chain>/v*.changelog.md` | indexed same-chain version detail |
| `TODO.md` | compact durable current execution index, not the primary live board |
| `phase/SUMMARY.md`, `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, `phase/phase-NNN-NN-NN-*.md` | live staged execution and provenance |
| `patch/<context>.patch.md` or root `<context>.patch.md` | governed before/after review outside live phase planning |
| allowed `history/` / `done/` surfaces | inactive referenced history/detail, never cleanup authority |

Allowed preservation surfaces are `todo/history/`, `todo/done/`, `phase/history/`, `phase/done/`, `patch/done/`, `changelog/done/`, and when diagram rollover is needed, `diagram/history/` plus `diagram/done/`. Active changelog detail shards remain under `changelog/<chain>/v*.changelog.md`. Design has **no default** `design/done/`; it remains active blueprint authority until superseded. Helper/support surfaces such as `template/**`, `support/**`, and `plugin/**` are non-governed unless explicitly promoted.

Completed or inactive status is not junk classification or deletion authorization. Active entrypoints must keep moved history reachable.

### 2) Governance order and role boundaries

Default sync order:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync when affected

Active governed metadata uses real session identifiers, never placeholders.

Role boundaries:
- README describes active capability/current state in user-facing terms; do not make phase/release chronology the capability definition.
- Design owns target state, not changelog history, TODO/phase execution, patch review, or completed-work storage.
- Diagram visually synthesizes project structure but never outranks design semantic truth.
- Changelog owns current version and history, not phase definitions or design target state.
- Phase owns staged execution, not design, patch, or source naming authority; chronology must not become function/class/module/route/config naming.
- Patch owns tactical before/after review, not durable design or live execution.
- Source comments may explain local rationale or point to governed documents, but remain bounded pointers rather than parallel authority.
- Helper/support artifacts do not gain authority from proximity.

Cross-Rule exact repetition is exceptional: a consumer may retain only the minimum literal/order needed to prevent a likely execution, safety, verification, or ordering error; name the canonical owner, keep the copy synchronized, and never create competing or recursive authority.

### 3) Scan and work-shape discipline

Start current-state scans from README, active design parents and needed children, active diagram entrypoints when present, active changelog parents and needed version shards, compact TODO, compact `phase/SUMMARY.md`, active phase/patch files, and checked implementation. Open `done/` or archive only through active references or for history, audit, rollback, provenance, or trace reconstruction.

Before broad governance work, classify it as focused edit, owner-aligned sync, release/no-drift audit, rollover, or before/after patch review. Decompose broad work by owner—design, diagram, runtime, changelog, TODO/phase, patch metadata, release audit—without forcing lanes for a tiny local fix. `worker-routing-and-context.md` owns helper topology; `safe-io.md` owns bounded intake.

### 4) Governed chain model

Before appending, splitting, or normalizing design/changelog, resolve:
- namespace: one folder-scoped chain or shared multi-chain folder
- subject and parent: generic parent is valid when the folder fully scopes one chain; shared folders use a self-identifying semantic parent
- authority: exactly one active parent model; any coexistence is compatibility-only or inactive
- shape: `single-file-bootstrap`, `flat-sibling-shards`, `same-stem-subfolder-normalized`, or `archive-history-fallback`
- transition basis: bootstrap exit, shard-opening basis, append-vs-shard reason, and parent-map update

Keep bootstrap while compact and coherent. Use flat siblings for a folder-scoped chain with only a few coherent slices and a declared parent map. Use same-stem normalization for broad, multi-shard, root-heavy, or God-file-prone chains only after a checked opening basis. Archive/history fallback is inactive and never the ordinary active-detail namespace; do not infer a nested directory from the parent filename.

The parent remains a bodyful authority gateway and declares shape/map. Children remain coherent, reachable, back-linked, and non-duplicative. Classify proposed detail as current state, history, verification, risk, or next work before appending; plan repair when destination or authority is ambiguous.

When examples inform doctrine, keep `observed project shape`, `extracted doctrine`, `selected target form`, and equivalence evidence distinct. Placeholder names are examples; do not claim exact equivalence without checked proof.

### 5) Governed diagram lane

RULES uses dedicated `diagram/` governed infrastructure rather than design shards or plugin previews.
- governed source must always be Kroki-compatible and governance-suitable: text-governable, diff/review-friendly, semantically stable, and portable
- `diagram/STRUCTURE.md` is mandatory, compact, active, and bodyful—not a shallow router—and maps main concepts, source/code/folder topology, authority boundaries, diagram relationships, and deeper routes
- `diagram/<subject>.design.md` is the default integrated zoom-in/decomposition view
- open `diagram/<subject>/` children only for real visual complexity or distinct visual questions; do not mirror design shards automatically
- if diagram and design differ, design remains semantic authority
- inline answer/status/phase diagrams do not become governed source truth automatically; plugin/preview/manifest/report output stays support-only and must not become source truth
- diagram history/done preserves prior state or completed detail; it never authorizes deletion

### 6) Public onboarding and install scope

README/onboarding/install follows `portable-implementation-and-hardcoding-control.md`. Public install scope includes only the current source-owned active runtime set, not every file co-located in a shared destination.

---

## Part B — Design Governance

### 1) Active target-state authority

Design describes implementation-relevant current/next target state, durable rationale, invariants, and contracts. It must not absorb changelog history, phase/TODO execution, patch review, audit snapshots, rollback journals, release timelines, or unrelated domains. Historical explanation belongs in reachable changelog surfaces; retained legacy snapshots are historical/reference-only and outside active design authority.

Design parents remain bodyful gateways; child shards own coherent active target-state slices, identify parent scope, remain mapped/back-linked, and are not history by default. Retiring or superseding a shard requires design/changelog alignment, never quiet removal or reclassification. There is **no default** `design/done/`.

### 2) External requirements and alignment

When external docs, APIs, or provider references materially constrain implementation, normalize the implementation truth into design before or alongside dependent multi-step work. Capture the requirement, constrained component, relevant values/fields/parameters/flows/states/auth/callback/acceptance rules, what is sent/accepted/stored/validated/rejected, and what remains source-side background.

For each governed chain, align design version with runtime `Current Version`, runtime `Design` reference, and changelog `Current Version`. This alignment does not authorize duplicated changelog history. Paired design navigation is limited to `Full history`; do not embed detailed changelog sections or duplicate historical summaries in active design.

### 3) Design God-file repair

God pressure exists when design absorbs unrelated domains or other document roles. Keep current target truth, shard coherent active scope through a compact parent, move history to changelog, keep sequencing in phase and before/after review in patch, and split unrelated domains. Touched unresolved pressure must be repaired or visibly planned/deferred/blocked before sync or closeout.

---

## Part C — Changelog Governance

### 1) Active version authority

Each chain has one active authoritative parent owning current version, index, shard map when present, and forward navigation. Runtime/design/phase/patch/TODO align to it when applicable. Changelog records synchronized history; it must not become design target state, phase planning, TODO tracking, release dashboarding, or README current-state prose.

Same-chain version detail uses self-identifying `changelog/<chain>/v*.changelog.md` shards with one owner and resolvable parent/back links. Preserve exact historical content during migration unless an explicit governed rewrite is selected. `changelog/done/` is only legacy/archive/completed/fallback history for audit, rollback, provenance, or reconstruction—not ordinary active detail, junk, or deletion authority.

Daily TODO/phase movement stays with their history/done owners. README keeps concise current-state signals; detailed version timelines stay in changelog.

### 2) Changelog God-file repair

Keep the parent compact as version/index/map/navigation authority; move bulky same-chain detail to chain-scoped version shards, reserve `done/` for fallback history, and route design/phase/TODO/README content to their owners. Do not append release prose that duplicates active surfaces.

---

## Part D — Patch Governance

### 1) Meaning, location, and change contract

A patch is a governed before/during-execution review artifact showing **what will change**. Each change item identifies a target artifact or stable locator, current/before state, target/after state, and one change type: `additive`, `replacement`, `deletion`, or `restructuring`.

A patch is not a retrospective/phase summary, rollout dashboard, prose-only recap, deletion authority, or generic plan. Active review lives at `patch/<context>.patch.md` or root `<context>.patch.md`; completed history may move to `patch/done/<context>.patch.md` after review closes. Filenames are self-identifying and version-suffix-free; generic `patch.md` is invalid.

### 2) Metadata and alignment

Patch metadata requires `Current Version`, `Session`, `Status`, `Target Design`, and `Full history`. Its changelog metadata requires `Parent Document`, `Current Version`, and `Session`.

Use real session IDs in active artifacts; `LEGACY-*` is historical-only when original data is unavailable. Align patch and patch-changelog versions, resolve `Target Design` to an existing design/version, and perform final patch metadata sync in governance order. Metadata integrity does not make patch version authority or transfer design/phase ownership.

### 3) Reviewability

Every patch includes:
1. Context
2. Analysis
3. Change items
4. Verification
5. Rollback approach

Each change item provides enough comparison detail through before/after snippets, current/target tables, unified diffs, anchored hunks, or scoped command/config replacements. Stable locators may be path, heading, symbol, query, key path, route, command label, schema object/table/column, or another precise anchor.

A non-code/governance-only patch may omit snippets only when it explicitly declares itself non-code/non-snippet, says the surface is conceptual/governance/structural, and keeps runtime edits out of scope.

When external requirements drive the change, point to normalized design truth and summarize only the review-relevant constraint; patch never replaces design or transiently relies on reading memory.

### 4) Patch/phase boundary and God Patch repair

Patch owns before/after review; phase owns live staged execution. `/patch` must not become the live phase-plan namespace, active phase index, or per-phase execution storage. `patch/done/` is inactive history, not junk or default active input.

Keep each patch centered on one coherent review family. Split when targets, change types, review boundaries, or rollback paths diverge; keep execution in phase and history in changelog; preserve reviewability and block closeout while touched God Patch pressure is unresolved or unplanned.

---

## Part E — Unified Version-Control Governance (UDVC-1)

### 1) One mechanism and one authority per role

UDVC-1 is the only version-governance mechanism for governed RULES chains; do not introduce parallel authorities.
- root runtime rule → loaded, active behavior contract
- design → active target-state and rationale authority
- changelog → current version and history authority
- `TODO.md` → durable execution index
- `phase/` → live staged execution
- `patch/` → before/after review

Design cannot replace the runtime body, and changelog claims cannot prove runtime behavior when the root body is missing. README install arrays define the source-owned active runtime set and must not widen it to design/changelog/TODO/phase/patch/support files.

### 2) Runtime metadata and body sufficiency

Root active runtime Rules require:
- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is canonical; `Based on:` is retired in active root metadata.

A README-listed runtime Rule is invalid if metadata-only. It needs a substantive rule statement/behavior contract, operational guidance, relevant boundaries/triggers/anti-patterns/verification/integration, and enough body to differ from a design pointer. Source/runtime parity must include body sufficiency, not hashes alone; check substantive bodies before claiming no-drift, runtime parity, release readiness, or active Rule install success.

A runtime file is eligible for install/parity claims only when it exists at source root, has canonical metadata and substantive body, aligns runtime/design/changelog versions, and stays inside source-owned install scope. Missing metadata/body, mixed `Based on`/`Design`, hash-only proof, or widened install scope invalidates the claim.

---

## Alignment and Repair Gate

Keep applicable versions, real session IDs, parent/map/back links, reachable history, body sufficiency, source-owned install scope, phase/patch boundaries, owner-aligned sync, and portable source/destination wording aligned. Runtime co-location does not grant ownership; resolve owner/project scope before managing or deleting another owner's file.

When a document mixes target state, history, execution, verification, rollback, roadmap, or operations, preserve its primary role and route detail to the correct owner. Preserve history; overload repair is not deletion authority. Touched God pressure must be repaired or visibly planned, deferred, or blocked before sync/closeout.

## Trigger Model

| Trigger | Required handling |
|---|---|
| new chain or version-impacting behavior | establish design/runtime/changelog alignment through UDVC-1 |
| large active design or bulky version history | shard through the declared parent model; use chain-scoped changelog versions for history |
| completed/history detail | move only to allowed referenced history/done surfaces; preserve meaning |
| broad governance/release sync | classify owner-aligned lanes before deep work |
| before/after review need | use patch outside phase planning |
| README release sync | update concise current-state sections, not timelines |
| metadata-only runtime root | treat active install/parity state as invalid |
| public onboarding/install | apply portable binding and source-owned runtime scope |
| mixed-role touched document | repair clear overload or create an owner-specific visible repair slice |

## Anti-Patterns

Avoid role collapse; ambiguous dual parents; archive fallback as active detail; automatic design-to-diagram mirroring; metadata-only runtime roots; unclassified `sync everything`; broad lanes for tiny fixes; install scope widened into governed/support files; machine-local public defaults; completed content treated as junk; and quiet removal/reclassification instead of governed sharding, rollover, split, or history movement.

## Integration

- [document-integrity.md](document-integrity.md) / [phase-todo-artifact.md](phase-todo-artifact.md) — references, preservation, rollover, startup, phase/TODO
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) — binding and onboarding notation
- [worker-routing-and-context.md](worker-routing-and-context.md) / [safe-io.md](safe-io.md) — helper topology and bounded intake
- [accurate-communication.md](accurate-communication.md) / [coding-discipline.md](coding-discipline.md) — claim strength and coding verification
