# Memory Governance and Session Boundary

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.7
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-08)

---

## 1) Goal

Define one first-class rule chain for memory governance and session-boundary behavior so the assistant:
- uses memory as reusable context rather than as active authority
- keeps root `MEMORY.md` as a compact active index instead of a long-form content dump
- keeps active one-line memory hooks visible in the root index instead of hiding all meaning behind second-layer reads
- compresses repeated path text by declaring one canonical `Scope` and one `Memory base` per path scope
- lists path-scoped entries with clear relative paths under that `Memory base`
- distinguishes `global/`, `path/`, and `archive/` memory roles clearly
- applies path-scoped memory to work on the matching path instead of tying applicability to one original session only
- treats session IDs as provenance rather than as the primary applicability key
- keeps archived memory inactive by default
- defines the governance contract before any actual `/memory` migration happens

This chain should make memory usage deterministic, reviewable, visible enough to be useful in startup context, and less prone to cross-session or cross-project contamination.

---

## 2) Problem Statement

The current RULES stack already has useful adjacent protections:
- `authority-and-scope` keeps fresh user directives above stale assistant framing
- `accurate-communication` and `evidence-grounded-burden-of-proof` keep carry-forward detail from being overstated as verified fact
- compact/post-compact waves already tightened re-anchor behavior after context compaction
- v1.6 memory governance already treats loader warnings, truncation risk, and index bloat as maintenance triggers

But root `MEMORY.md` can still fail in two opposite ways:
- it can repeat long memory-relative paths in every item and waste the active context budget
- it can become a link-only router or second-layer index that hides active memory meaning until another file is read

Observed failure modes this design intends to close:
- memory structure remains implicit, so `MEMORY.md` can drift into a large content dump instead of a compact index
- repeated path fragments such as long `path/home-node-workplace-...` folder names inflate the root index even when all entries share one scope base
- loader warnings, truncation risk, and index-size warnings can be treated as noise instead of immediate memory-index maintenance signals
- compaction can overcorrect into `MEMORY.md` → `SCOPE.md` → secondary index indirection, making the loaded root index much less useful
- fake alias notation such as `path = path` can create markdown links that resolve to the wrong location
- remembered context can leak across unrelated sessions or projects because scope and applicability are under-specified
- session identity is mistaken for applicability even when the real durable scope is the working path/project
- archived or stale memory remains too easy to treat as active truth
- memory can be over-used as a convenience layer even when RULES or current checked evidence should govern instead
- memory cleanup or reorganization can drift before the repository defines the governing contract for how memory is supposed to work

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- memory role boundary relative to RULES, user instruction, and checked evidence
- root `MEMORY.md` contract
- visible active root-index hook semantics
- Memory-base and relative path entry format for path-scoped root sections
- active memory taxonomy (`global/`, `path/`, `archive/`)
- path scope as the primary applicability model
- session ID as provenance only
- canonical `SCOPE.md` contract for each path scope
- matching / specificity rules for path-scoped memory
- lifecycle states such as active, stale, archived, and superseded
- write / recheck / archive governance gates

### 3.2 Out of Scope
- requiring every memory file to move during the same wave
- treating optional external recall tooling as required infrastructure
- changing low-level Claude Code internals or undocumented recursive loader behavior
- making `MEMORY.md` a full content dump
- making root `MEMORY.md` a link-only router with no useful active hooks
- general communication, evidence, or layout rules except where those adjacent chains need narrow integration updates

### 3.2.1 Optional External Recall Boundary
Optional external recall tooling may improve continuity when available, but it does not become required infrastructure or authority by existing.

Required behavior:
- treat optional external recall as a supplemental context bridge rather than semantic truth
- when available, it may accelerate recall after the relevant continuation target has already been identified from stronger surfaces
- optional recall output must not outrank checked task/phase/design/implementation evidence when those stronger surfaces already settle the active meaning
- if optional external recall is unavailable, the general memory model must still function without it
- shared-board / shared-task-list-specific intake, handoff, and cross-session continuation semantics stay outside Main RULES scope

### 3.3 Boundary Principle
This chain owns what memory means, how memory scope applies, and how root memory indexing should stay compact without hiding active meaning.

It does not replace:
- `authority-and-scope.md` for overall precedence
- `accurate-communication.md` for wording shape
- `evidence-grounded-burden-of-proof.md` for claim-strength thresholds
- `answer-presentation.md` for compact layout patterns
- `safe-file-reading.md` for bounded file-reading mechanics

---

## 4) Core Memory Model

### 4.1 Role Boundary Principle
Memory is reusable context, not active authority.

Required behavior:
- memory must not outrank live user instruction
- memory must not outrank current checked repo/project evidence
- memory must not substitute for a RULES-owned system fix when the user explicitly wants the issue solved in RULES
- memory may help orientation, historical continuity, and scoped recall when its applicability rules are satisfied

### 4.2 Root Index Principle
Root `MEMORY.md` remains present and acts as the canonical active index.

Required behavior:
- root `MEMORY.md` stays present as the entrypoint to active memory
- root `MEMORY.md` should index active memory files instead of becoming a large monolithic content dump
- active root indexing should remain compact enough to scan quickly
- active one-line memory hooks should remain visible enough that loaded context still has useful meaning
- loader warnings, truncation warnings, and entry-length/index-bloat warnings should trigger maintenance of the root index
- maintenance should first reduce repeated path text with scope-level `Memory base` sections where applicable
- maintenance should compact hooks, move long detail into topic files, split or archive stale inactive entries, and preserve path-scope pointers
- index maintenance must not delete memory content merely because the active root index is too large
- archive entries must not remain in the active root index

### 4.3 Root Visibility Principle
Root compaction must not hide memory.

Required behavior:
- do not turn root `MEMORY.md` into only links to `SCOPE.md`, secondary indexes, or folders
- keep one active hook per active memory entry unless the entry is explicitly stale, archived, or intentionally removed from active root context
- preserve enough hook text for the assistant to know why the memory may matter before opening the target file
- if detail is too long, shorten the hook rather than replacing it with an opaque pointer

### 4.4 Scope-Relative Index Principle
Repeated path prefixes should be declared once per scope.

Required behavior:
- each path-scoped section may declare `Scope: <canonical absolute path>` for applicability
- each path-scoped section may declare `Memory base: path/<readable-scope-folder>/` for file-location compression
- entries below that base may use inline relative paths such as `feedback/feedback_example.md`
- relative entries should be grouped by actual subfolder when it improves scanability
- the base relationship must be stated explicitly; do not rely on fake alias notation
- markdown links are allowed only when they resolve correctly from root `MEMORY.md`

### 4.5 Scope Taxonomy Principle
Active memory is separated by semantic role:

| Memory Area | Role | Default Status |
|-------------|------|----------------|
| `global/` | broadly reusable active context | active |
| `path/` | active context scoped to a canonical working path | active |
| `archive/` | historical or non-default memory | inactive by default |

### 4.6 Path-Primary Applicability Principle
Path is the primary applicability key for project-scoped memory.

Required behavior:
- path-scoped memory applies because the current work targets the matching path scope
- path-scoped memory is not limited to the original session that created it
- any later session working on the same governed path may use that path-scoped memory when relevance and freshness rules still hold

### 4.7 Provenance-Not-Applicability Principle
Session IDs are provenance only.

Required behavior:
- session IDs may be recorded so the origin of a memory entry or scope can be traced
- session IDs must not be treated as the primary reason that memory applies to later work
- same-session continuity alone must not bypass path mismatch or stale-memory concerns

### 4.8 Canonical Scope Declaration Principle
Every path scope should have canonical scope metadata through `SCOPE.md`.

Required behavior:
- each path scope directory should contain `SCOPE.md`
- `SCOPE.md` should declare the canonical scope key for the path
- the folder name is a readable locator only; `SCOPE.md` is the authoritative scope declaration
- scope metadata should be strong enough to prevent folder-name drift from silently changing applicability meaning

### 4.9 Archive-Inactive Principle
Archived memory is not active memory.

Required behavior:
- archived memory should be inactive by default
- archive content must not behave like active current context in normal retrieval/indexing behavior
- archive may still exist for historical recovery, audit, or later reactivation when explicitly needed

---

## 5) Matching and Specificity Model

### 5.1 Default Matching Rules
Use path specificity before session provenance.

| Situation | Default Result |
|-----------|----------------|
| exact path match | applies |
| descendant path under the scoped path | may apply |
| ancestor / umbrella path only | does not auto-apply by default |
| sibling path | does not apply |
| more-specific path scope and broader path scope both match | more-specific scope wins |

### 5.2 Ancestor-Scope Caution
An umbrella workspace path must not silently absorb all child-project memory by default.

Required behavior:
- broader ancestor scopes should not auto-apply just because the current work happens somewhere below them
- if broader coverage is intentionally desired, it should be explicit in the governing scope contract rather than assumed from path ancestry alone

### 5.3 Relevance Gate
Even matching scope is not enough by itself.

Required behavior:
- remembered context should still be checked for topical relevance to the active objective
- remembered context should not be used just because the path matches if the content is stale, unrelated, or superseded by fresher checked evidence

---

## 6) `MEMORY.md` and Scope-Index Contract

### 6.1 Root `MEMORY.md` contract
The root memory index should remain compact, active-only, and useful when loaded.

Required behavior:
- organize the root index by active memory areas such as `GLOBAL` and `PATH_SCOPE:<canonical-path>`
- keep one-line hook-style entries where possible
- avoid duplicating full memory-file contents in the root index
- avoid repeating one long memory-relative scope folder in every entry
- keep active hook meaning visible in the root index rather than hiding all meaning behind another index layer

### 6.2 Path scope section format
A path scope with repeated long paths should use one base declaration and relative entries.

Recommended format:

```text
## PATH_SCOPE: <readable scope name>
Scope: `<canonical absolute path>`
Memory base: `path/<readable-scope-folder>/`
Entries below are relative to Memory base.

### Root
- `SCOPE.md` — Canonical path scope for this memory area.

### feedback/
- `feedback_topic.md` — One-line active hook.

### project/
- `project_topic.md` — One-line active hook.
```

Required behavior:
- `Scope` is the applicability anchor
- `Memory base` is the location-compression anchor
- entries under the base are relative paths, preferably inline code unless markdown links are fully resolvable
- group entries by real subfolder when doing so improves scanability
- do not use fake aliases such as `path = path` because markdown links will not resolve through that alias
- do not introduce `MEMORY.md -> SCOPE.md -> INDEX.md` routing merely to shrink the active root file

### 6.3 Path scope layout contract
A path scope may use a structure like:

```text
path/<readable-scope-folder>/
  SCOPE.md
  feedback/
  project/
  reference/
```

Required behavior:
- the path scope directory groups memory by semantic type
- actual memory entries may continue using the existing `name` / `description` / `type` frontmatter baseline
- scope is inherited from the containing path scope plus canonical `SCOPE.md`, rather than requiring the folder name itself to act as the only authority

### 6.4 Archive layout contract
Archive should preserve recoverability without polluting active context.

Required behavior:
- archive may mirror the active taxonomy when helpful
- archive entries must not stay in the active root index
- archive remains a historical storage layer, not a second active memory namespace

---

## 7) Freshness, Recheck, and Write Governance

### 7.1 Freshness Boundary Principle
Applicable memory is not the same as currently verified fact.

Required behavior:
- remembered context may orient the assistant or justify scoped historical statements
- exact current-state claims still require fresh recheck against current checked evidence when material
- stale or archived memory should be treated with stricter recheck expectations

### 7.2 Write Gate Principle
Write memory only when it is durable and reusable.

Required behavior:
- prefer writing memory only for durable context that will help future work
- do not write temporary task residue, transient status notes, or details already derivable directly from code/docs/git when those are the real authority
- if the real problem belongs in RULES, fix RULES rather than substituting a memory write for the system fix

### 7.3 Lifecycle Principle
Memory should have visible state rather than becoming permanent active clutter.

Suggested active-state model:
- `active`
- `stale`
- `archived`
- `superseded`

Required behavior:
- stale or superseded memory should not remain indistinguishable from active memory
- archive/retire decisions should reduce contamination risk without silently erasing recoverable history

---

## 8) Recommended Target Shape

The target semantic model for a governed memory root is:

```text
/memory
  MEMORY.md
  global/
  path/
    <readable-scope-folder>/
      SCOPE.md
      feedback/
      project/
      reference/
  archive/
```

The target active root index should keep useful hook text while reducing repeated path text:

```text
## PATH_SCOPE: RULES repository
Scope: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
Memory base: `path/home-node-workplace-AWCLOUD-TEMPLATE-RULES/`
Entries below are relative to Memory base.

### Root
- `SCOPE.md` — Canonical path scope for RULES repository memory.

### feedback/
- `feedback_rules_runtime_should_not_install_readme_todo.md` — Runtime install excludes README/TODO/design/changelog/phase/patch.
```

This design defines the governance contract for that target shape. It does not require the live memory tree to be migrated in the same wave that creates the contract.

---

## 9) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| root `MEMORY.md` as a giant content dump | startup context becomes heavy and mixed | keep root `MEMORY.md` as an active index only |
| root `MEMORY.md` as a link-only router | loaded context loses active memory meaning | keep visible one-line hooks in the root index |
| repeating the same long memory base in every scoped entry | wastes root context budget | declare one `Memory base` per scope and use relative entries |
| fake alias links such as `path = path` | markdown links resolve incorrectly | use explicit `Memory base` text and inline relative paths |
| hiding active memory in second-layer indexes by default | future sessions must guess what to read before memory is useful | keep active hooks visible at root; read details only when needed |
| session ID treated as the main reason memory applies | reuse across matching future sessions becomes brittle and confusing | use path as the primary applicability key and session IDs as provenance |
| umbrella ancestor path auto-matches every child project | cross-project bleed increases | require exact or clearly governed broader scope behavior |
| archive kept in active index | stale memory keeps behaving like current truth | keep archive inactive by default |
| folder name acting as the only scope authority | path renames or normalization drift can silently change meaning | keep canonical scope in `SCOPE.md` |
| memory used as a substitute for RULES ownership | governance problems get hidden inside persistence | fix RULES first when the issue belongs in RULES |

---

## 10) Quality Metrics

| Metric | Target |
|--------|--------|
| Root `MEMORY.md` stays active-index-only | High |
| Active root hooks remain visible and useful | High |
| Repeated scope paths are compressed with Memory-base sections | High when path repetition creates bloat |
| Fake alias or broken relative-link patterns | 0 critical cases |
| Link-only hidden-memory root indexes | 0 critical cases |
| Path-scoped memory uses path-primary applicability | High |
| Session IDs remain provenance-only | High |
| Ancestor-path bleed incidents | 0 critical cases |
| Archive entries left in active root index | 0 critical cases |
| Memory used as substitute for RULES-owned fixes | 0 critical cases |

---

## 11) Integration

| Rule | Relationship |
|------|--------------|
| [../authority-and-scope.md](../authority-and-scope.md) | Precedence stays there; memory applicability defers here |
| [../accurate-communication.md](../accurate-communication.md) | Wording for memory-derived context and recheck disclosure stays there |
| [../evidence-grounded-burden-of-proof.md](../evidence-grounded-burden-of-proof.md) | Evidence thresholds for memory-derived claims stay there |
| [../answer-presentation.md](../answer-presentation.md) | Compact memory-status / scope-re-anchor layout stays there |
| [../safe-file-reading.md](../safe-file-reading.md) | Bounded reading and oversized root-index maintenance signals stay there |
| [../project-documentation-standards.md](../project-documentation-standards.md) | Repository doc-role governance remains separate |

---

> Full history: [../changelog/memory-governance-and-session-boundary.changelog.md](../changelog/memory-governance-and-session-boundary.changelog.md)
