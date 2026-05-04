# Memory Governance and Session Boundary
> **Current Version:** 1.5
> **Design:** [design/memory-governance-and-session-boundary.design.md](design/memory-governance-and-session-boundary.design.md) v1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/memory-governance-and-session-boundary.changelog.md](changelog/memory-governance-and-session-boundary.changelog.md)
---
## Rule Statement
**Core Principle: Use memory as scoped reusable context rather than active authority, keep root `MEMORY.md` as an active index only, and govern applicability by path scope first while treating session IDs as provenance only.**
This rule owns memory role boundaries, taxonomy, root index behavior, path matching, Session-Provenance, `SCOPE.md`, optional recall, and archive lifecycle.
---
## Core Contract
- **Memory-Is-Context:** memory may orient continuity, but it must not outrank live user instruction, current checked repo/project evidence, or a RULES-owned fix the user explicitly requests.
- **Root index only:** root `MEMORY.md` is the active entrypoint and should point to active scope indexes/files, not store long-form bodies. Archive entries must not remain in the active root index.
- **Taxonomy:** `global/`, `path/`, and `archive/` mean broadly reusable context, canonical path-scoped context, and inactive historical/non-default memory.
- **Path-primary applicability:** project memory applies because current work targets the matching path scope, not because it came from the same session. Matching still requires relevance and freshness.
- **Session-Provenance:** session IDs support audit/traceability only; same-session continuity must never bypass path, relevance, or staleness checks.
- **Canonical scope:** each path scope should have `SCOPE.md`; folder names are locators, while canonical scope meaning lives in metadata.
- **Optional recall:** memsearch or similar tooling can supplement handoff/continuity when available, but it is not required infrastructure or semantic truth. Check availability, use only after stronger execution surfaces identify the target, and fall back to native memory plus checked surfaces when absent/insufficient.
- **Archive inactive:** archived memory is historical by default and must not behave like active context unless explicitly restored or used for audit/recovery.
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
## `MEMORY.md` and Scope Layout
Root `MEMORY.md` should organize active entries by `GLOBAL` and `PATH_SCOPE:<canonical-path>` or equivalent, use compact one-line hooks, point to active scope indexes/files, and avoid full memory bodies.

Path scope layout may be:
```text
path/<readable-scope-folder>/{SCOPE.md,feedback/,project/,reference/}
```
`SCOPE.md` declares canonical scope. Folder naming alone is not authority. Archive may mirror active taxonomy, but archived entries must leave the active root index.
---
## Freshness, Write Gates, and Lifecycle
Applicable memory is not current verified repo truth. Memory may justify scoped historical/context statements, but exact current-state claims require recheck when material, with stricter checks for stale/archived memory. Write memory only for durable reusable context; do not write temporary task residue, transient status, or details derivable from code/docs/git. If the issue belongs in RULES, fix RULES rather than substituting memory.

Lifecycle labels may include `active`, `stale`, `archived`, and `superseded`; stale/superseded entries must not look active.

Recommended target shape:
```text
/memory
├── MEMORY.md
├── global/
├── path/<readable-scope-folder>/{SCOPE.md,feedback/,project/,reference/}
└── archive/
```
This defines the target model; it does not require migrating the live tree in the same wave.
---
## Verification Checklist
- [ ] root `MEMORY.md` remains active index, not content dump
- [ ] path-scoped memory uses Path-Primary applicability
- [ ] session IDs are provenance only
- [ ] ancestor-path bleed is avoided
- [ ] archived entries are inactive and absent from active index
- [ ] exact current-state claims from memory are rechecked when material
- [ ] optional recall does not outrank checked task/phase/design/implementation evidence
---
## Integration
Related rules: `authority-and-scope.md` keeps memory below live authority; `accurate-communication.md` owns memory-derived wording; `evidence-grounded-burden-of-proof.md` owns evidence thresholds; `project-documentation-standards.md` owns repo document-role governance.
---
