# Memory Governance and Session Boundary

> **Current Version:** 1.3
> **Design:** [design/memory-governance-and-session-boundary.design.md](design/memory-governance-and-session-boundary.design.md) v1.3
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/memory-governance-and-session-boundary.changelog.md](changelog/memory-governance-and-session-boundary.changelog.md)

---

## Rule Statement

**Core Principle: Use memory as scoped reusable context rather than active authority, keep root `MEMORY.md` as an active index only, and govern memory applicability by path scope first while treating session IDs as provenance only.**

This rule owns memory-governance semantics, including memory role boundaries, root `MEMORY.md` behavior, active memory taxonomy, path-scope applicability, session provenance behavior, canonical `SCOPE.md` use, matching/specificity rules, and archive lifecycle.

---

## Core Principles

### 1) Memory-Is-Context Principle
Memory may help continuity, orientation, and scoped recall, but it does not outrank live authority.

Required guidance:
- memory must not outrank live user instruction
- memory must not outrank current checked repo/project evidence
- memory must not substitute for a RULES-owned fix when the user explicitly wants the issue solved in RULES
- memory may support continuity only when its scope and relevance gates are satisfied

### 2) Root-Index Principle
Root `MEMORY.md` remains present and acts as the active memory index.

Required guidance:
- root `MEMORY.md` should remain present as the canonical active memory entrypoint
- root `MEMORY.md` should point to active scope indexes and active memory files rather than becoming a long-form content dump
- active root indexing should stay compact and scanable
- archive entries must not remain in the active root index

### 3) Memory Taxonomy Principle
Active memory should be separated by semantic role.

Default model:
- `global/` = broadly reusable active context
- `path/` = active context scoped to a canonical path
- `archive/` = inactive historical or non-default memory

Required guidance:
- treat `global/`, `path/`, and `archive/` as semantically different areas
- do not let archived or stale memory masquerade as active context

### 4) Path-Primary Applicability Principle
Path is the primary applicability key for project-scoped memory.

Required guidance:
- path-scoped memory applies because the current work targets the matching path scope
- path-scoped memory is not limited to the original session that created it
- later sessions may use matching path-scoped memory when relevance and freshness rules still hold

### 5) Session-Provenance Principle
Session IDs record where a memory came from, not why it applies.

Required guidance:
- session IDs may be stored for provenance, audit, or traceability
- session IDs must not be treated as the primary applicability key
- same-session continuity alone must not bypass path mismatch, relevance mismatch, or stale-memory concerns

### 6) Canonical Scope Declaration Principle
Each path scope should use canonical scope metadata through `SCOPE.md`.

Required guidance:
- each path scope directory should contain `SCOPE.md`
- `SCOPE.md` should declare the canonical scope key for the path
- folder names are readable locators only; canonical scope meaning lives in `SCOPE.md`
- do not let folder-name drift silently change scope meaning

### 6.1) Optional Extension Recall Boundary
memsearch or similar extension/plugin recall layers may improve cross-session continuity when available, but they do not become required infrastructure or authority by existing.

Required guidance:
- treat optional recall extensions as supplemental context bridges rather than semantic truth
- when receive-side continuation wants optional recall detail, explicitly check whether the extension is available instead of assuming plugin presence from prior sessions or prior machines
- when such an extension is available, it may accelerate recall after the relevant execution target has been identified from stronger coordination surfaces
- do not let optional recall output outrank checked task/phase/design/implementation evidence when those stronger surfaces already settle the active meaning
- do not design coordination assumptions so active work fails when an optional recall extension is absent
- if such an extension is unavailable or the availability/probe step fails, fall back to native memory plus checked execution surfaces immediately
- coordination ownership for when/how optional recall bridges are used should defer to `shared-execution-coordination.md`

### 7) Archive-Inactive Principle
Archive is not active memory.

Required guidance:
- archived memory should be inactive by default
- archive content must not behave like active current context in normal retrieval/indexing behavior
- archive may still exist for explicit recovery, audit, or restoration workflows

---

## Matching and Specificity Rules

### Default matching model
Use path specificity before session provenance.

| Situation | Default Result |
|-----------|----------------|
| exact path match | applies |
| descendant path under the scoped path | may apply |
| ancestor / umbrella path only | does not auto-apply by default |
| sibling path | does not apply |
| more-specific path scope and broader path scope both match | more-specific scope wins |

Required guidance:
- an umbrella workspace path must not silently absorb all child-project memory by default
- even matching scope still requires topical relevance to the active objective
- stale, unrelated, or superseded memory should not be used just because the path matches

---

## `MEMORY.md` Contract

### Root `MEMORY.md`
Treat root `MEMORY.md` as an active index only.

Required guidance:
- organize the root index by active memory areas such as `GLOBAL` and `PATH_SCOPE:<canonical-path>`
- prefer one-line hook-style entries where possible
- use the root index to point to active scope indexes and active memory files
- avoid duplicating full memory-file bodies in the root index

### Path scope layout
A path scope may use a structure like:

```text
path/<readable-scope-folder>/
  SCOPE.md
  feedback/
  project/
  reference/
```

Required guidance:
- the path scope directory groups memory by semantic type
- canonical scope is declared in `SCOPE.md`
- folder naming alone must not be the only scope authority

### Archive layout
Required guidance:
- archive may mirror active taxonomy when helpful
- archive entries must not stay in the active root index
- archive remains a historical storage layer, not a second active namespace

---

## Freshness and Write Gates

### Freshness boundary
Applicable memory is not the same as currently verified fact.

Required guidance:
- memory may orient the assistant or justify scoped historical statements
- exact current-state claims still require fresh recheck when material
- stale or archived memory should be treated with stricter recheck expectations

### Write gate
Write memory only when it is durable and reusable.

Required guidance:
- prefer writing memory only for durable context that will help future work
- do not write temporary task residue, transient status notes, or details that are already directly derivable from code/docs/git when those are the real authority
- if the real problem belongs in RULES, fix RULES rather than substituting a memory write for the governing fix

### Lifecycle states
Suggested lifecycle states:
- `active`
- `stale`
- `archived`
- `superseded`

Required guidance:
- stale or superseded memory should not remain indistinguishable from active memory
- archive/retire behavior should reduce contamination risk without silently erasing recoverable history

---

## Recommended Target Shape

The governed target model is:

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

This rule defines the governance contract for that target shape.
It does **not** require the live memory tree to be migrated in the same wave that creates the contract.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| root `MEMORY.md` as a giant content dump | startup context becomes heavy and mixed | keep root `MEMORY.md` as an active index only |
| session ID treated as the main reason memory applies | reuse across matching future sessions becomes brittle and confusing | use path as the primary applicability key and session IDs as provenance |
| umbrella ancestor path auto-matches every child project | cross-project bleed increases | require exact or clearly governed broader scope behavior |
| archive kept in active index | stale memory keeps behaving like current truth | keep archive inactive by default |
| folder name acting as the only scope authority | path renames or normalization drift can silently change meaning | keep canonical scope in `SCOPE.md` |
| memory used as a substitute for RULES ownership | governance problems get hidden inside persistence | fix RULES first when the issue belongs in RULES |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Root `MEMORY.md` stays active-index-only | High |
| Path-scoped memory uses path-primary applicability | High |
| Session IDs remain provenance-only | High |
| Ancestor-path bleed incidents | 0 critical cases |
| Archive entries left in active root index | 0 critical cases |
| Memory used as substitute for RULES-owned fixes | 0 critical cases |

---

## Integration

Related rules:
- [authority-and-scope.md](authority-and-scope.md) - overall precedence stays there; memory applicability defers here
- [accurate-communication.md](accurate-communication.md) - wording for memory-derived context and recheck disclosure stays there
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - evidence thresholds for memory-derived claims stay there
- [answer-presentation.md](answer-presentation.md) - compact memory-status / scope-re-anchor layout stays there
- [project-documentation-standards.md](project-documentation-standards.md) - repository document-role governance remains separate

---
