# Document Governance
> **Current Version:** 1.23
> **Design:** [design/document-governance.design.md](design/document-governance.design.md) v1.23
> **Session:** 4a8d9ac0-ecf9-40c4-961e-634583157b6c
> **Full history:** [changelog/document-governance.changelog.md](changelog/document-governance.changelog.md)
> **Absorbed:** project-documentation-standards v2.41, document-design-control v1.12, document-changelog-control v4.12, document-patch-control v2.9, unified-version-control-system v1.3

## Rule Statement

**Core Principle: One artifact owns each role: runtime behavior, textual design, visual structure, version/history, execution or before/after review. Resolve chain authority before growth; preserve substantive active bodies and reachable inactive history without turning preservation into runtime fallback.**

พูดง่าย ๆ: README บอกภาพรวม; design บอกเป้าหมาย; diagram แสดงโครงสร้าง; changelog เก็บ version/history; TODO/phase ติดตามงาน; Patch ใช้ review สิ่งที่จะเปลี่ยน.

## Roles, Navigation and Sync

| Authority | Role and valid form |
|---|---|
| `README.md` | current capability/overview/onboarding/front page, not detailed release chronology |
| `design/*.design.md`, `design/<slug>/*.design.md` | active target behavior/contracts/rationale and coherent child slices |
| `diagram/STRUCTURE.md` | mandatory compact bodyful whole-project visual structure/entrypoint |
| `diagram/*.design.md`, `diagram/<subject>/*.design.md` | Kroki-compatible integrated subject diagrams/justified visual shards |
| `changelog/*.changelog.md` | one active current-version/index/map/navigation parent |
| `changelog/<chain>/v*.changelog.md` | indexed self-identifying same-chain version detail |
| `TODO.md` | compact durable current index, not primary live board |
| `phase/SUMMARY.md`, `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, `phase/phase-NNN-NN-NN-*.md` | live staged execution/provenance, not target truth |
| `patch/YYYY-MM-DDTHH-mm-ssZ--<semantic-slug>.patch.md` | chronological before/during-execution review, not live phase planning |

Allowed inactive preservation: `todo/history/`, `todo/done/`, `phase/history/`, `phase/done/`, `patch/done/`, `changelog/done/`; diagram rollover may use `diagram/history/` and `diagram/done/`. Design has **no default** `design/done/`: a child stays active blueprint until explicitly superseded. `template/**`, `support/**`, `plugin/**` remain support/non-governed unless explicitly promoted. Completed/inactive is not junk or deletion authority; active parents keep history reachable.

Default sync: design → diagram when materially triggered → runtime rule → changelog → TODO → affected Patch metadata final sync. This is ownership/dependency order, not recurrence after every attempt. Design/approval prerequisites precede dependent implementation; [execution-and-goal-frame.md](execution-and-goal-frame.md) owns result-sync cadence. Markdown Runtime Rules are source implementation, not final-result bookkeeping. Use real session identifiers. [phase-todo-artifact.md](phase-todo-artifact.md) owns initiation/lineage and task-evidence handoff; no artifact opens merely because another exists.

Synthesize settled decisions and actual results by role, leading with the selected direction and the rationale, proof, limits and pending obligations needed to understand and maintain it. Exploratory or unselected approaches are supporting context where they still explain material trade-offs, constraints, recovery or costly rediscovery, not equal-weight current choices or a transcript; their mere existence need not create another artifact. Design owns the selected target; changelog the material change/history; phase/TODO execution/proof/remaining obligations. Update affected owners/references only; no semantic/reference delta needs no artificial diff. Preserve meaningful history without copying tentative iterations/task logs into every document, manufacturing a final-only success narrative or creating a retrospective checklist Patch. A triggered Patch remains prospective before/during execution.

Start scans at README, compact active design/changelog parents and selected children, diagram entrypoint when applicable, TODO, phase summary/active children, selected Patch and implementation. Open history/done/archive through references or a history/audit/rollback/provenance need. Classify broad work as focused edit, owner-aligned sync, release/no-drift audit, rollover or review; split by actual owners without tiny-fix lanes. Capture/routing belongs to [safe-io.md](safe-io.md) and [worker-routing-and-context.md](worker-routing-and-context.md).

Design cannot absorb chronology/audit snapshots/execution/rollback journals; changelog cannot become target design/roadmap/TODO/README prose; phase cannot become design/Patch or source naming authority; Patch cannot become generic plans/retrospective summaries. Source comments are bounded rationale/references, not parallel policy. Cross-Rule repetition is exceptional: retain only a synchronized literal/order/local consequence preventing a likely execution/safety/proof error and name its complete owner.

Active parents/maps/manifests/install/generated inputs select current authority only. History/done/quarantine is reachable provenance, not active resolution, automatic fallback, generated input or normal runtime/install discovery. [document-integrity.md](document-integrity.md) owns reference/inactivity and losslessness checks.

## Design and Changelog Chain Selection

Before append/split/normalize resolve namespace, actual subject, one active parent, shape and opening basis:
- a fully folder-scoped single chain may use a generic parent; shared multi-chain folders need semantic self-identifying parents
- coexistence is explicitly compatibility-only or inactive, never ambiguous dual authority
- `single-file-bootstrap`: retain while compact/coherent
- `flat-sibling-shards`: few coherent folder-scoped slices with declared parent map
- `same-stem-subfolder-normalized`: broad/multi-shard/root-heavy/God-pressure chain with checked opening basis
- `archive-history-reference-only`: inactive reference, never ordinary active detail/fallback

Record bootstrap exit/shard opening/append basis and map updates; do not infer nested directories from a filename. Parents stay bodyful gateways declaring shape/map; children identify scope, backlink, remain reachable/coherent/nonduplicative. Classify proposed detail as current state/history/verification/risk/next work before growth. Owner ambiguity stops the affected append, not unrelated safe work.

Keep observed project example, extracted doctrine, selected target and verified equivalence separate. Placeholder examples and stricter inspired targets are not facts about the observed project.

### Design requirements

Design holds implementation-relevant current/next behavior, invariants, contracts and durable rationale. Normalize external requirements before/alongside dependent multi-step implementation: constrained component, values/fields/flows/states/auth/callback/acceptance, sent/accepted/stored/validated/rejected forms and background limits. Do not rely on transient reading alone.

Align design version with runtime `Current Version`/`Design` and changelog authority; paired navigation uses `Full history`, not copied historical sections. Retirement/supersession requires explicit design/changelog alignment, not quiet reclassification. For mixed domains/roles shard coherent active truth through the parent, route history to changelog and sequencing/review to phase/Patch.

### Changelog requirements

One active parent owns current version/index/map/forward routes. Indexed chain-scoped version shards retain exact history during migration unless governed rewriting is selected. `changelog/done/` is inactive archive/provenance for audit/deliberate rollback analysis, not ordinary detail, automatic resolution or restoration authority. Keep daily TODO/phase movement with their owners and README concise. Repair bulky parents by mapped version shards, not duplicate release dashboards.

## Governed Diagram Lane

Use dedicated `diagram/`, not design children or plugin previews as visual authority. Source is always Kroki-compatible: portable, text-governable, review/diff-friendly and semantically stable. Bodyful `diagram/STRUCTURE.md` maps concepts, source/code/folder topology, authority boundaries, relationships and deeper routes—not a shallow router.

Default zoom-in is integrated `diagram/<subject>.design.md`; subfolders open only for real visual complexity/distinct questions, never automatic design-shard mirrors. Design outranks conflicting visual meaning. Inline answer/status/phase diagrams and preview/manifest/report output do not become governed truth by proximity. Preserve prior visual history through allowed history/done without deletion-by-status.

## Patch Review and Creation Identity

A Patch shows **what will change** before/during execution. Each item has target/stable locator, before/current, after/target, and one type: `additive`, `replacement`, `deletion`, `restructuring`. Keep Context, Analysis, Change items, Verification and Rollback approach. Use snippets/tables/diffs/anchored hunks/command replacements sufficient to compare; locators may be path/heading/symbol/key/route/schema/query/command.

A governance-only Patch may omit snippets only when explicitly non-code/non-snippet/conceptual-structural and runtime edits are excluded. External constraints point to normalized design, not a transient source-reading memory. One coherent review family per Patch; divergent targets/types/review/rollback require proportionate split. `/patch` never owns live phase storage/index; `patch/done/` is inactive retained review history.

### Exact filename

Active `patch/YYYY-MM-DDTHH-mm-ssZ--<semantic-slug>.patch.md`; completion may move to `patch/done/` without altering chronology. UTC to seconds, `--` chronology/meaning separator, lowercase ASCII kebab-case slug:
```regex
^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z--[a-z0-9]+(?:-[a-z0-9]+)*\.patch\.md$
```

Timestamp is verified original creation, not edit/phase/release/completion/copy/move time. Revisions preserve it. No Patch ID/registry/`patch/INDEX.md`, generic `patch.md`, version/copy/final/collision suffix or guessed timestamp.

### Metadata and evidence

Required Patch fields: `Current Version`, `Session`, `Status`, `Created At`, `Creation Evidence`, `Target Design`, `Full history`; companion changelog: `Parent Document`, `Current Version`, `Session`. `Created At` is matching `YYYY-MM-DDTHH:mm:ssZ`, derived with filename from one captured UTC instant. Create exclusively; fail on collision.

Admissible evidence: direct creator event, creation-confirming transcript event, verified filesystem birthtime not contradicted by copy/restore, or authoritative external/operator creation evidence. mtime/ctime, alphabetical/directory order, Phase/date, changelog date alone, Git first-add without creation proof and session UUID are insufficient. Missing evidence remains legacy and blocks an evidence-complete row.

Align Patch/companion versions and existing target design/version; `LEGACY-*` is historical-only. Metadata does not transfer version/design/phase authority. Suspended archives preserve legacy names only while unchanged, inactive and execution/discovery-disconnected. [document-integrity.md](document-integrity.md) owns hash-bound manifest/journal/rename/reference/rollback proof. Repository Tool `script/patch-timeline.mjs` and tests/fixtures stay outside Runtime installation.

## UDVC-1 Runtime Eligibility

UDVC-1 is the only governed RULES version mechanism; the role ledger remains one authority per role. Design/changelog cannot replace a missing runtime body or prove its behavior. README install arrays define only the source-owned active Runtime set, not design/changelog/TODO/phase/Patch/support or all co-located destination files.

Active root Runtime Rules require `Current Version`, `Design`, `Session`, `Full history`; `Design:` is canonical, `Based on:` retired. Eligibility requires source-root existence, canonical aligned metadata, substantive rule/operational guidance and relevant boundaries/triggers/anti-patterns/proof/integration—not metadata or a pointer alone. Missing body, mixed metadata, widened payload or hash-only checks invalidate install/parity/release-ready claims. Verify body sufficiency in addition to bytes/modes.

Public README/onboarding/install separates portable source and destination under [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md). Resolve other-owner scope before managing shared runtime files.

## Repair and Integrity Gate

Keep meaning, versions/sessions, parent/map/backlinks, reachable history, current-only inputs, body sufficiency and source-owned install scope aligned. Touched mixed-role/God pressure needs safe local repair or a visible owner-specific planned/deferred/blocked disposition before sync/closeout. History preservation is mandatory, not deletion authority. [document-integrity.md](document-integrity.md) verifies propagation/rollover; [coding-discipline.md](coding-discipline.md) and [accurate-communication.md](accurate-communication.md) govern tested completion claims.
