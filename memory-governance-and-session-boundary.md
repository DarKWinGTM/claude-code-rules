# Memory Governance and Session Boundary
> **Current Version:** 2.0
> **Design:** [design/memory-governance-and-session-boundary.design.md](design/memory-governance-and-session-boundary.design.md) v2.0
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/memory-governance-and-session-boundary.changelog.md](changelog/memory-governance-and-session-boundary.changelog.md)

## Rule Statement

**Core Principle: Memory is relevant scoped context, not active authority. Keep `MEMORY.md` compact and meaning-visible; apply path specificity/relevance/freshness before session provenance, and preserve history without pruning useful memory for size alone.**

## Applicability and Lifecycle

Memory never outranks live direction, current checked project evidence or a user-selected RULES fix. Session IDs are provenance/audit only; same/recent session cannot bypass scope/staleness. `SCOPE.md` declares canonical path meaning; folder names locate files, not authority.

| Path relation | Applicability, subject to relevance/freshness |
|---|---|
| exact match | applies |
| descendant | may apply |
| ancestor/umbrella only | no automatic child-project application |
| sibling | does not apply |
| broad and specific match | specific scope wins |

Even path-matched memory is not verified current truth. Recheck material exact values/symbols/state, especially stale/archived context. Keep `active`, `stale`, `archived`, `superseded` distinct; stale/superseded cannot look active. `global/` is broadly reusable, `path/` canonical scoped, `archive/` inactive historical/non-default. Archive leaves the active root index and is used only for explicit restoration/audit/recovery, never silently current.

Optional memsearch/recall may supplement continuity after stronger design/phase/tasks/TODO/checked implementation identifies the target. Check availability; fall back immediately to native memory plus checked surfaces when absent/insufficient. Recall is neither required infrastructure nor semantic truth.

## Meaning-visible Root Index

`MEMORY.md` is the active entrypoint: one concise meaning hook per active useful file, not long bodies or an opaque link-only second-layer router. Group `GLOBAL` and `PATH_SCOPE:<canonical-path>` or equivalent. For repeated long scoped paths declare `Scope` once (applicability) and `Memory base` once (relative file location); list real subfolders/entries beneath:

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

Use inline relative paths under the declared base, or genuine fully resolvable links from `MEMORY.md`. No fake `path = path` aliases or repeated full manifests. Group `Root`, `feedback/`, `project/`, `reference/` or actual subfolders when helpful. Do not hide all active meaning in `SCOPE.md`, another index or a folder pointer.

Loader size/truncation/entry warnings trigger maintenance: compact repeated paths first, shorten hooks without losing meaning, move long bodies to topic files; classify genuinely stale inactive material for reachable history. Never delete/archive/hide active useful memory merely to shrink the root. [document-integrity.md](document-integrity.md) owns preservation/no-delete and [safe-io.md](safe-io.md) bounded intake.

## Write Gate and Target Shape

Write only durable reusable user/feedback/project/reference context, not transient task/status residue or facts derivable from code/docs/git. Check relevant existing memory before adding duplicates. RULES-owned issues are fixed in RULES, not substituted with memory. Memory recall and wording stay under [authority-and-scope.md](authority-and-scope.md), [evidence-discipline.md](evidence-discipline.md) and [accurate-communication.md](accurate-communication.md).

Target layout: `/memory/MEMORY.md`, `global/`, `path/<readable-scope-folder>/SCOPE.md` with `feedback/`, `project/`, `reference/`, and inactive `archive/`. This contract does not require migrating/pruning the live tree in the current wave; real mutations need their selected scope and preservation gate. [document-governance.md](document-governance.md) retains repository document roles, not memory as another project authority.
