# Context Load and Document Density Control

> **Current Version:** 1.0
> **Design:** [design/context-load-and-document-density-control.design.md](design/context-load-and-document-density-control.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/context-load-and-document-density-control.changelog.md](changelog/context-load-and-document-density-control.changelog.md)

---

## Rule Statement

**Core Principle: Manage context load as a full lifecycle across reading, writing, worker routing, and repair, so broad raw evidence is filtered before it burdens the leader session and active documents are written in a density-safe shape that stays cheap to read, edit, diff, and verify later.**

This rule owns context-load strategy, aggregate read-burst control, leader-context protection, document-density discipline, God-line prevention, append-vs-restructure decisions, and compact/thrash repair signals. It does not replace safe file reading, worker routing, document role governance, rollover, or evidence rules.

---

## Core Contract

### 1) Context is a lifecycle, not a post-compact rule

Do not treat context safety as only “read less after compact.” Context pressure is shaped by how documents are written, how broad evidence is routed, and how active entrypoints are maintained.

Required guidance:
- prevent future context cost while writing and syncing docs
- route broad raw evidence through workers when the leader does not need the raw body
- repair dense active documents when compact/thrash exposes structural debt
- avoid blunt post-compact bans when a better workflow or document structure solves the cause

### 2) Leader-context protection

The leader session should stay the controller, verifier, and final decision maker. It should not absorb broad raw evidence by default.

Required guidance:
- use subagents or worker lanes as raw evidence absorbers and filters for broad docs, logs, searches, audits, or multi-surface reviews
- brief workers with the exact question, checked scope, expected anchors, conflicts, risks, and leader verification needs
- make the leader verify selected anchors before final claims instead of reading every raw source
- do not satisfy the worker gate by only saying a worker could help; dispatch one when the broad-read shape requires it

### 3) Aggregate read-burst control

Several bounded reads can still overload context when combined, especially if lines are dense.

Before reading multiple governance surfaces, identify:
- the question being answered
- the authority surface most likely to answer it
- whether exact raw content is needed or a filtered worker handoff is enough
- cumulative output risk across all planned reads, not only per-file line count

Density warning signals include:
- many active governance files read in one burst
- long markdown lines that carry several concepts
- repeated reads after compact that refill context quickly
- bounded line ranges with unusually high character count

### 4) Document-density and God-line prevention

Write active docs so future sessions can read and edit them cheaply.

A God line is a long line that carries multiple responsibilities such as current state, history, version timeline, caveats, verification, exclusions, and next steps in one paragraph or bullet.

Required guidance:
- keep one line or bullet focused on one concept or one small group of tightly related facts
- split current state, history, verification, risks, and exclusions into separate bullets or sections when they grow
- move long version timelines or historical detail to changelog/history surfaces instead of appending them to active summary lines
- use semantic bullets, small tables, and short paragraphs instead of one-line history dumps
- treat very long active lines as repair triggers, not as proof the content is disposable

### 5) Append-vs-restructure gate

Before appending to an existing active line or bullet, check whether the append would make future diffs and reads larger than the logical change.

Required questions:
1. Is the new content current state, history, verification, risk, or next work?
2. Does the target line already mix more than one responsibility?
3. Would the edit replace one huge line for a small logical change?
4. Should the new content become a new bullet, a subsection, a changelog entry, or a history/done shard reference?
5. Should the existing line be split before adding the new detail?

If the target line is already a God-line candidate, restructure first or in the same change instead of appending again.

### 6) Active entrypoints are maps, not storage dumps

`TODO.md`, `phase/SUMMARY.md`, README current-state sections, and compact design indexes should help a fresh session find current work quickly.

Required guidance:
- keep active entrypoints focused on current state, selected roadmap, active tasks, gates, and pointers
- store detailed version history in changelog, not active summaries
- store daily movement or completed detail in referenced history/done shards when rollover owners require it
- keep enough context in active maps to navigate without rereading every historical detail

### 7) Compact/thrash is a repair signal

Autocompact thrash or immediate post-compact refill means the workflow or document shape needs review.

Required response:
- identify whether the cause is restored context, aggregate read burst, high-density files, worker-gate miss, God lines, oversized entrypoints, or raw output flooding
- repair the source pattern when practical: route broad reads to workers, split dense lines, roll over active entrypoints, or narrow the authority surface
- do not create a rigid “after compact never read X” policy unless a specific owner requires it

### 8) Density-aware verification

After non-trivial governance edits, verify not only semantic sync but also future read cost.

Useful checks:
- longest lines in touched active docs
- one-line version timeline growth
- active summary lines mixing current state and history
- README/TODO/phase/patch lines that would create large one-line diffs
- whether worker routing was used before broad raw review

Density checks are practical repair triggers. They are not deletion authority and not a substitute for semantic correctness.

---

## Decision Flow

```text
Need broad evidence or doc sync
  ↓
Define the question and authority surface
  ↓
Broad raw content likely?
  → YES: dispatch worker/filter lane unless a narrow direct reason exists
  → NO: read targeted anchor directly
  ↓
Writing active docs?
  → YES: apply append-vs-restructure and density checks
  → NO: preserve checked-scope evidence boundaries
  ↓
Compact/thrash or high-density output appears?
  → YES: diagnose source pattern and repair document/workflow shape
```

---

## Anti-Patterns

Avoid:
- leader-session raw absorption of broad docs, logs, or governance surfaces by momentum
- reading several “bounded” files without considering aggregate output size
- appending release/history details to an already huge active line
- treating line count as safe when characters per line are high
- using post-compact restrictions as the main solution when document structure or worker routing is the real cause
- turning active entrypoints into history books
- claiming no-drift or release readiness without checking body sufficiency and density risks when relevant

Better behavior: ask the question first, route broad raw evidence through workers, write docs for future reads, and repair density debt when it appears.

---

## Verification Checklist

- [ ] Broad raw reads were routed through a worker/filter lane or a narrow direct-handling reason was stated.
- [ ] Multi-file read plans considered aggregate output and line density, not only per-file line count.
- [ ] Active docs avoid God-line appends and split mixed responsibilities when needed.
- [ ] Current state, history, verification, risks, and next work are not collapsed into one dense line.
- [ ] Active entrypoints remain compact maps with pointers to detailed history/done/changelog surfaces.
- [ ] Compact/thrash triggered diagnosis and repair of workflow or document structure.
- [ ] Density checks were included in non-trivial governance closeout when touched docs could grow.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Leader raw broad-context absorption | Low |
| Worker filtering before broad reads | High |
| Aggregate read-burst awareness | High |
| God-line / single-line history dump creation | Low / 0 critical cases |
| Active entrypoint map clarity | High |
| Compact/thrash repair response | High |
| Future-read and diff maintainability | High |

---

## Integration

Related rules:
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - owns worker scale and delegation before broad leader absorption
- [safe-file-reading.md](safe-file-reading.md) - owns bounded file reading and sharded design read order
- [safe-terminal-output.md](safe-terminal-output.md) - owns bounded command output handling
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - owns TODO/phase active-entrypoint rollover
- [document-design-control.md](document-design-control.md) - owns compact design indexes and child shards
- [document-consistency.md](document-consistency.md) - owns cross-reference and no-drift verification
- [project-documentation-standards.md](project-documentation-standards.md) - owns document roles and active runtime install scope
- [maintainable-code-structure-and-decomposition.md](maintainable-code-structure-and-decomposition.md) - provides the code-side analogy for God-function/God-file pressure
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - keeps partial reads and worker findings evidence-bounded

---

> **Full history:** [changelog/context-load-and-document-density-control.changelog.md](changelog/context-load-and-document-density-control.changelog.md)
