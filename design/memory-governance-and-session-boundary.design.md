# Memory Governance and Session Boundary

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)

---

## 1) Goal

Define one first-class rule chain for memory governance and session-boundary behavior so the assistant:
- uses memory as reusable context rather than as active authority
- keeps root `MEMORY.md` as a compact active index instead of a long-form content dump
- distinguishes `global/`, `path/`, and `archive/` memory roles clearly
- applies path-scoped memory to work on the matching path instead of tying applicability to one original session only
- treats session IDs as provenance rather than as the primary applicability key
- keeps archived memory inactive by default
- defines the governance contract **before** any actual `/memory` migration happens

This chain should make memory usage deterministic, reviewable, and less prone to cross-session or cross-project contamination.

---

## 2) Problem Statement

The current RULES stack already has useful adjacent protections:
- `authority-and-scope` keeps fresh user directives above stale assistant framing
- `accurate-communication` and `evidence-grounded-burden-of-proof` keep carry-forward detail from being overstated as verified fact
- compact/post-compact waves already tightened re-anchor behavior after context compaction

But the repository still lacks one semantic owner for memory governance itself.

Observed failure modes this design intends to close:
- memory structure remains implicit, so `MEMORY.md` can drift into a large content dump instead of a compact index
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
- active memory taxonomy (`global/`, `path/`, `archive/`)
- path scope as the primary applicability model
- session ID as provenance only
- canonical `SCOPE.md` contract for each path scope
- matching / specificity rules for path-scoped memory
- lifecycle states such as active, stale, archived, and superseded
- write / recheck / archive governance gates

### 3.2 Out of Scope
- actual migration of live memory files under `~/.claude/projects/.../memory/`
- treating optional extension/plugin recall layers such as memsearch as required infrastructure
- changing the existing live memory directory layout in the same wave that creates the governance contract
- low-level Claude Code internals or undocumented recursive loader behavior
- general communication, evidence, or layout rules except where those adjacent chains need narrow integration updates

### 3.2.1 Optional Extension Recall Boundary
Optional recall extensions such as memsearch may improve continuity when available, but they do not become required infrastructure or authority by existing.

Required behavior:
- treat optional recall extensions as supplemental context bridges rather than semantic truth
- when available, they may accelerate recall after the relevant execution target has already been identified from stronger coordination surfaces
- optional recall output must not outrank checked task/phase/design/implementation evidence when those stronger surfaces already settle the active meaning
- if an optional recall extension is unavailable, fall back to native memory plus checked execution surfaces
- coordination ownership for when/how optional recall bridges are used should defer to `shared-execution-coordination.md`

### 3.3 Boundary Principle
This chain owns **what memory means, how memory scope applies, and how memory should be organized semantically**.

It does not replace:
- `authority-and-scope.md` for overall precedence
- `accurate-communication.md` for wording shape
- `evidence-grounded-burden-of-proof.md` for claim-strength thresholds
- `answer-presentation.md` for compact layout patterns

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
- root `MEMORY.md` should point to active scope indexes and active memory files instead of becoming a large monolithic content dump
- active root indexing should remain compact enough to scan quickly
- archive entries must not remain in the active root index

### 4.3 Scope Taxonomy Principle
Active memory is separated by semantic role:

| Memory Area | Role | Default Status |
|-------------|------|----------------|
| `global/` | broadly reusable active context | active |
| `path/` | active context scoped to a canonical working path | active |
| `archive/` | historical or non-default memory | inactive by default |

### 4.4 Path-Primary Applicability Principle
Path is the primary applicability key for project-scoped memory.

Required behavior:
- path-scoped memory applies because the current work targets the matching path scope
- path-scoped memory is not limited to the original session that created it
- any later session working on the same governed path may use that path-scoped memory when relevance and freshness rules still hold

### 4.5 Provenance-Not-Applicability Principle
Session IDs are provenance only.

Required behavior:
- session IDs may be recorded so the origin of a memory entry or scope can be traced
- session IDs must not be treated as the primary reason that memory applies to later work
- same-session continuity alone must not bypass path mismatch or stale-memory concerns

### 4.6 Canonical Scope Declaration Principle
Every path scope should have canonical scope metadata through `SCOPE.md`.

Required behavior:
- each path scope directory should contain `SCOPE.md`
- `SCOPE.md` should declare the canonical scope key for the path
- the folder name is a readable locator only; `SCOPE.md` is the authoritative scope declaration
- scope metadata should be strong enough to prevent folder-name drift from silently changing applicability meaning

### 4.7 Archive-Inactive Principle
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
The root memory index should remain compact and active-only.

Required behavior:
- organize the root index by active memory areas such as `GLOBAL` and `PATH_SCOPE:<canonical-path>`
- keep one-line hook-style entries where possible
- use the root index to point to active scope indexes and active memory files
- avoid duplicating full memory-file contents in the root index

### 6.2 Path scope layout contract
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

### 6.3 Archive layout contract
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
├── MEMORY.md
├── global/
├── path/
│   └── <readable-scope-folder>/
│       ├── SCOPE.md
│       ├── feedback/
│       ├── project/
│       └── reference/
└── archive/
```

This design defines the governance contract for that target shape.
It does **not** require the live memory tree to be migrated in the same wave that creates the contract.

---

## 9) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| root `MEMORY.md` as a giant content dump | startup context becomes heavy and mixed | keep root `MEMORY.md` as an active index only |
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
| [../project-documentation-standards.md](../project-documentation-standards.md) | Repository doc-role governance remains separate |

---

> Full history: [../changelog/memory-governance-and-session-boundary.changelog.md](../changelog/memory-governance-and-session-boundary.changelog.md)
