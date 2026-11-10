# Memory Governance and Session Boundary
> **Current Version:** 2.1
> **Design:** [design/memory-governance-and-session-boundary.design.md](design/memory-governance-and-session-boundary.design.md) v2.1
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/memory-governance-and-session-boundary.changelog.md](changelog/memory-governance-and-session-boundary.changelog.md)

## Rule Statement

**Core Principle: Memory is scoped context, not active authority. Keep `MEMORY.md` compact and meaning-visible; apply path specificity/relevance/freshness before session provenance, preserving useful history rather than pruning for size.**

## Applicability and Lifecycle

Memory cannot outrank live direction, checked project evidence or a selected RULES fix. Session IDs are provenance/audit, not scope/freshness exceptions. `SCOPE.md` declares canonical path meaning; folder names locate, not authorize.

| Path relation | Applicability, subject to relevance/freshness |
|---|---|
| exact match | applies |
| descendant | may apply |
| ancestor/umbrella only | no automatic child-project application |
| sibling | does not apply |
| broad and specific match | specific scope wins |

Path match is not current truth. Recheck material values/symbols/state, especially stale/archive context. Distinguish `active`, `stale`, `archived`, `superseded`; the latter three cannot look active. `global/` is broadly reusable, `path/` canonical scoped, `archive/` inactive/non-default. Remove archived entries from the active index; use them only for explicit restoration/audit/recovery, not silent current context.

Optional recall/memsearch supplements stronger design/phase/tasks/TODO/implementation after they identify the target. If absent/insufficient, immediately use native memory plus checked surfaces. Recall is neither required infrastructure nor truth.

## Meaning-visible Root Index

`MEMORY.md` gives one concise meaning hook per useful active file, not long bodies or an opaque second index. Group `GLOBAL` and `PATH_SCOPE:<canonical-path>` or equivalent. Declare repeated `Scope` (applicability) and `Memory base` (relative location) once:

```text
## PATH_SCOPE: <short scope name>
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

Use inline paths relative to that base or genuinely resolvable links from `MEMORY.md`; no fake `path = path` aliases or repeated manifests. Group real subfolders when useful. Do not hide all meaning in `SCOPE.md`, another index or a folder pointer.

Loader size/truncation/entry warnings trigger maintenance: compact repeated paths, shorten hooks without losing meaning, move bodies to topic files, and classify genuinely stale material into reachable history. Never delete/archive/hide useful active memory just to shrink. [Integrity](document-integrity.md) owns preservation; [I/O](safe-io.md) bounds intake.

## Write Gate and Target Shape

Save durable reusable user/feedback/project/reference context, not task residue or code/docs/git-derived facts. Check existing entries before duplication. Fix RULES-owned issues in RULES, not memory. [Authority](authority-and-scope.md), [evidence](evidence-discipline.md) and [wording](accurate-communication.md) govern recall/use.

Target: `/memory/MEMORY.md`, `global/`, `path/<readable-scope-folder>/SCOPE.md` with `feedback/`, `project/`, `reference/`, and inactive `archive/`. This does not select live-tree migration/pruning; mutation needs scope/preservation approval. [Document governance](document-governance.md) owns repository roles; memory is not another project authority.
