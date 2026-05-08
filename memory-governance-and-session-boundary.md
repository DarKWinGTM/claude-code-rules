# Memory Governance and Session Boundary
> **Current Version:** 1.7
> **Design:** [design/memory-governance-and-session-boundary.design.md](design/memory-governance-and-session-boundary.design.md) v1.7
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/memory-governance-and-session-boundary.changelog.md](changelog/memory-governance-and-session-boundary.changelog.md)
---
## Rule Statement
**Core Principle: Use memory as scoped reusable context rather than active authority, keep root `MEMORY.md` as a compact but still meaning-visible active index, compress repeated scope paths with one declared `Memory base` per path scope, and govern applicability by path scope first while treating session IDs as provenance only.**
This rule owns memory role boundaries, taxonomy, root index behavior, path matching, visible root-index compaction, Session-Provenance, `SCOPE.md`, optional recall, and archive lifecycle.
---
## Core Contract
- **Memory-Is-Context:** memory may orient continuity, but it must not outrank live user instruction, current checked repo/project evidence, or a RULES-owned fix the user explicitly requests.
- **Root index only:** root `MEMORY.md` is the active entrypoint and should index active memory files without storing long-form bodies. Loader warnings, truncation risk, or root-index bloat are maintenance signals, not reasons to delete memory content.
- **Visible active hooks:** root `MEMORY.md` must preserve enough one-line memory meaning for active context use. It must not become a link-only router that hides all useful memory behind second-layer reads.
- **Scope-relative compaction:** when a path scope has repeated long paths, root `MEMORY.md` should declare the canonical `Scope` and one `Memory base`, then list entries below as paths relative to that base.
- **No fake aliases:** do not use fake markdown alias syntax such as `path = path` with links that resolve to the wrong location. If entries are relative to `Memory base`, mark them as inline code or otherwise make the base relationship explicit.
- **No repeated path manifest:** avoid repeating the full memory-relative scope folder in every entry when one scope-level `Memory base` preserves the same meaning with less context cost.
- **Taxonomy:** `global/`, `path/`, and `archive/` mean broadly reusable context, canonical path-scoped context, and inactive historical/non-default memory.
- **Path-primary applicability:** project memory applies because current work targets the matching path scope, not because it came from the same session. Matching still requires relevance and freshness.
- **Session-Provenance:** session IDs support audit/traceability only; same-session continuity must never bypass path, relevance, or staleness checks.
- **Canonical scope:** each path scope should have `SCOPE.md`; folder names are locators, while canonical scope meaning lives in metadata.
- **Optional recall:** memsearch or similar tooling can supplement handoff/continuity when available, but it is not required infrastructure or semantic truth. Check availability, use only after stronger execution surfaces identify the target, and fall back to native memory plus checked surfaces when absent/insufficient.
- **Archive inactive:** archived memory is historical by default and must not behave like active context unless explicitly restored or used for audit/recovery. Archive entries must not remain in the active root index.
---
## Matching and Specificity
Use path specificity before session provenance.

| Situation | Default result |
|---|---|
| exact path match | applies if relevant and fresh enough |
| descendant under scoped path | may apply |
| ancestor/umbrella path only | does not auto-apply by default |
| sibling path | does not apply |
| broader and more-specific match | more-specific scope wins |

Do not let an umbrella workspace silently absorb child-project memory. Stale, unrelated, superseded, or archived memory should not be used merely because path matches.
---
## `MEMORY.md` Root Index Contract
Root `MEMORY.md` should organize active entries by `GLOBAL` and `PATH_SCOPE:<canonical-path>` or equivalent, keep compact one-line hooks, and avoid full memory bodies.

For path-scoped sections, use this shape when path repetition is large:

```text
## PATH_SCOPE: <short readable scope name>
Scope: `<canonical absolute project path>`
Memory base: `path/<readable-scope-folder>/`
Entries below are relative to Memory base.

### Root
- `SCOPE.md` — <one-line active hook>

### feedback/
- `feedback_example.md` — <one-line active hook>

### project/
- `project_example.md` — <one-line active hook>
```

Required behavior:
- keep one active hook per entry in root `MEMORY.md` when the memory is active and useful for context
- group entries under `Root`, `feedback/`, `project/`, `reference/`, or another real relative subfolder when that improves scanability
- use inline relative file paths under the declared `Memory base` unless a real markdown link is kept fully resolvable from root `MEMORY.md`
- keep `Scope` as the human/path applicability anchor and `Memory base` as the file-location compression anchor
- do not move active meaning into only `SCOPE.md`, a second-layer index, or an opaque folder pointer
- do not delete, archive, or hide active memory merely to reduce root index size

If the loader reports size, truncation, or entry-length warnings, treat it as index maintenance work:
- compact repeated path text with Memory-base sections first
- shorten overly long hooks while preserving the active meaning
- move long detail into topic files rather than the root index
- split or archive stale inactive entries with reachable pointers when history matters
- preserve path-scope pointers and do not delete memory content merely because the active index is too large

Path scope layout may be:

```text
path/<readable-scope-folder>/
  SCOPE.md
  feedback/
  project/
  reference/
```

`SCOPE.md` declares canonical scope. Folder naming alone is not authority. Archive may mirror active taxonomy, but archived entries must leave the active root index.
---
## Freshness, Write Gates, and Lifecycle
Applicable memory is not current verified repo truth. Memory may justify scoped historical/context statements, but exact current-state claims require recheck when material, with stricter checks for stale/archived memory. Write memory only for durable reusable context; do not write temporary task residue, transient status, or details derivable from code/docs/git. If the issue belongs in RULES, fix RULES rather than substituting memory.

Lifecycle labels may include `active`, `stale`, `archived`, and `superseded`; stale/superseded entries must not look active.

Recommended target shape:

```text
/memory
  MEMORY.md
  global/
  path/<readable-scope-folder>/
    SCOPE.md
    feedback/
    project/
    reference/
  archive/
```

This defines the target model; it does not require migrating the live tree in the same wave.
---
## Verification Checklist
- [ ] root `MEMORY.md` remains active index, not content dump or link-only router
- [ ] active root entries keep one-line hooks visible enough for context use
- [ ] path-scoped sections use one `Scope` and one `Memory base` when repeated paths would bloat the index
- [ ] entries under a `Memory base` use clear relative paths, not fake markdown aliases
- [ ] path-scoped memory uses Path-Primary applicability
- [ ] session IDs are provenance only
- [ ] ancestor-path bleed is avoided
- [ ] archived entries are inactive and absent from active index
- [ ] exact current-state claims from memory are rechecked when material
- [ ] optional recall does not outrank checked task/phase/design/implementation evidence
---
## Integration
Related rules: `authority-and-scope.md` keeps memory below live authority; `accurate-communication.md` owns memory-derived wording; `evidence-grounded-burden-of-proof.md` owns evidence thresholds; `project-documentation-standards.md` owns repo document-role governance; `safe-file-reading.md` and `governed-document-rollover-control.md` provide the bounded-read and active-entrypoint maintenance posture when root indexes grow too large.
---
