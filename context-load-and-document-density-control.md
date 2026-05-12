# Context Load and Document Density Control

> **Current Version:** 1.4
> **Design:** [design/context-load-and-document-density-control.design.md](design/context-load-and-document-density-control.design.md) v1.4
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/context-load-and-document-density-control.changelog.md](changelog/context-load-and-document-density-control.changelog.md)

---

## Rule Statement

**Core Principle: Manage context load as a full lifecycle.**

This lifecycle covers reading, writing, worker routing, and repair.

Target outcomes:
- broad raw evidence is filtered before it burdens the leader session
- active documents stay density-safe and cheap to read, edit, diff, and verify later

This rule owns:
- context-load strategy, aggregate read-burst control, and leader-context protection
- document-density discipline, God-line prevention, and opportunistic touched-doc God-line repair
- append-vs-restructure decisions and compact/thrash repair signals

It does not replace safe file reading, worker routing, document role governance, rollover, or evidence rules.

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

Aggregate governance/code read bursts are worker-gated before broad leader absorption.

Before reading multiple governance or code surfaces, identify:
- the question being answered
- the authority surface most likely to answer it
- whether exact raw content is needed or a filtered worker handoff is enough
- cumulative output risk across all planned reads, not only per-file line count

Worker-first filtering is required before leader raw absorption when any trigger applies:
- 3+ governance surfaces are needed for one claim, sync, release, or no-drift review
- cross-surface release sync, closeout, or release-ready validation is being assembled
- repo-wide search is followed by multi-file reads
- broad code+docs evidence is needed together
- dense/history-bearing active docs would be read as a set

The worker handoff should return:
- filtered findings
- conflicts
- exact anchors
- leader verification needs

Skipping the gate blocks broad sync, no-drift, closeout, or release-ready claims unless a narrow direct-handling exception is stated.

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

### 5) Opportunistic touched-doc God-line repair

When an active document is already being edited and the touched area contains a God-line candidate, do not only warn about the density problem.

Repair immediately when all conditions hold:
- the candidate is in a touched active document or touched section
- the semantic split is clear from the local context
- the repair is local, meaning-preserving, and low-risk
- the repair separates responsibilities such as current state, history, verification, risks, exclusions, and next work
- the repair does not require broad historical reconstruction or repo-wide formatting

Flag or plan instead of editing immediately when any condition holds:
- the line is history-heavy and its exact meaning could be changed by splitting
- the line mixes old release history with current state in a way that needs owner review
- the repair would touch broad unrelated sections or many files
- the correct destination for moved content is ambiguous
- the user explicitly limited the task to analysis only

Required behavior:
- if safe immediate repair applies, split or restructure in the same edit before claiming the touched doc is clean
- if immediate repair is unsafe, record it as density debt, follow-up work, or a phase/patch item when material
- do not append more content to a known God-line candidate unless no safer structure exists and the limit is stated

### 6) Append-vs-restructure gate

Before appending to an existing active line or bullet, check whether the append would make future diffs and reads larger than the logical change.

Required questions:
1. Is the new content current state, history, verification, risk, or next work?
2. Does the target line already mix more than one responsibility?
3. Would the edit replace one huge line for a small logical change?
4. Should the new content become a new bullet, a subsection, a changelog entry, or a history/done shard reference?
5. Should the existing line be split before adding the new detail?

If the target line is already a God-line candidate, do not append silently.

Required handling:
- restructure first or in the same change when the split is clear and low-risk
- flag or plan the repair when the split is broad or meaning-risky

### 7) Active entrypoints are maps, not storage dumps

`TODO.md`, `phase/SUMMARY.md`, README current-state sections, and compact design indexes should help a fresh session find current work quickly.

Required guidance:
- keep active entrypoints focused on current state, selected roadmap, active tasks, gates, and pointers
- store detailed version history in changelog, not active summaries
- store daily movement or completed detail in referenced history/done shards when rollover owners require it
- keep enough context in active maps to navigate without rereading every historical detail

### 8) Compact/thrash is a repair signal

Autocompact thrash or immediate post-compact refill means the workflow or document shape needs review.

Required response:
- identify whether the cause is restored context, aggregate read burst, high-density files, worker-gate miss, God lines, oversized entrypoints, or raw output flooding
- repair the source pattern when practical: route broad reads to workers, split dense touched lines, roll over active entrypoints, or narrow the authority surface
- do not create a rigid “after compact never read X” policy unless a specific owner requires it

### 9) Density-aware verification

After non-trivial governance edits, verify not only semantic sync but also future read cost.

Useful checks:
- longest lines in touched active docs
- one-line version timeline growth
- active summary lines mixing current state and history
- README/TODO/phase/patch lines that would create large one-line diffs
- touched God-line candidates that were repaired or explicitly flagged
- whether worker routing was used before broad raw review

Density checks are practical repair triggers. They are not deletion authority and not a substitute for semantic correctness.

---

### 10) Governed document God-file prevention

A God document is an active governance file that carries too many document roles or independent execution meanings in one place.

Signals include:
- current state, history, verification, rollback, roadmap, TODO, changelog, and design truth mixed in one active body
- one phase or patch carrying several independent goals, outputs, gates, rollback boundaries, or capability streams
- active README, TODO, phase summary, design, changelog, or patch updates that require large unrelated edits for a small logical change
- repeated compaction or broad rereads caused by one active file acting as a storage dump instead of a map

Required repair posture:
- redistribute content to the owner that matches its role before appending more detail
- use design sharding for large active target-state truth
- use changelog or `changelog/done/` for version history overload
- use `todo/history` / `todo/done` and `phase/history` / `phase/done` for accumulated movement or completed detail
- split God Phase and God Patch candidates by bounded goal, output, gate, rollback, or review boundary
- repair clear low-risk touched-document overload locally; flag or open a governed phase/patch when the split is broad or meaning-risky

Do not treat God-file classification as cleanup or deletion authority. The response is role-aware redistribution, sharding, rollover, splitting, or explicitly tracked repair.

### 11) Automatic God Artifact Control Loop

God artifact findings are not report-only observations during governed work.

When God-line, God-document, God-phase, God-patch, TODO, design, changelog, README, or summary pressure is found in touched governed scope, choose an action mode.

Action modes:
- `REPAIR_NOW`: clear, local, meaning-preserving, low-risk touched-scope split
- `PLAN_IN_CURRENT_PHASE`: real repair belongs to the active phase or implied execution slice
- `OPEN_REPAIR_PATCH`: reviewable before/after change needs patch packaging
- `OPEN_NEW_PHASE_OR_SUBPHASE`: distinct goal, output, gate, release, rollback, or capability boundary exists
- `BLOCK_CLOSEOUT`: touched-scope pressure remains unresolved or unplanned
- `ASK_ONLY_IF_AMBIGUOUS`: owner, meaning, or approval basis changes the safe path

Required loop:
1. detect the God artifact pressure
2. classify document family, owner, risk, and repair boundary
3. route content to the correct owner surface
4. repair now when `REPAIR_NOW` applies
5. otherwise create or extend the smallest visible governed repair slice
6. verify repaired or planned state before sync, no-drift, closeout, or release-ready claims

Do not ask the user to restate the repair instruction when the route is clear.
Ask only when ambiguity or approval sensitivity changes the action.

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
  → YES: apply touched-doc God-line repair, append-vs-restructure, and density checks
  → NO: preserve checked-scope evidence boundaries
  ↓
God artifact pressure found in touched scope?
  → YES: classify owner/risk, then repair now or create a visible repair slice
  → NO: continue
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
- noticing a low-risk touched God-line candidate but only warning while continuing to edit around it
- treating line count as safe when characters per line are high
- using post-compact restrictions as the main solution when document structure or worker routing is the real cause
- turning active entrypoints into history books
- claiming no-drift or release readiness without checking body sufficiency and density risks when relevant

Better behavior: ask the question first, route broad raw evidence through workers, write docs for future reads, and repair density debt when it appears.

---

## Verification Checklist
- [ ] Touched active documents were checked for God-file pressure and repaired, redistributed, or flagged when material.

- [ ] Broad raw reads were routed through a worker/filter lane or a narrow direct-handling reason was stated.
- [ ] Aggregate governance/code read-burst triggers used worker-first filtering before leader raw absorption.
- [ ] Multi-file read plans considered aggregate output and line density, not only per-file line count.
- [ ] Active docs avoid God-line appends and split mixed responsibilities when needed.
- [ ] Clear low-risk God-line candidates in touched active docs were repaired in the same edit.
- [ ] Broad, history-heavy, or meaning-risky God-line candidates were flagged or planned instead of silently appended.
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
| Worker-first aggregate-read gate compliance | High |
| Aggregate read-burst awareness | High |
| God-line / single-line history dump creation | Low / 0 critical cases |
| Unrepaired clear touched-doc God-line candidates | Low / 0 critical cases |
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
