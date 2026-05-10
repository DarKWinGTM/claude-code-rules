# Changelog - Context Load and Document Density Control

> **Parent Document:** [../context-load-and-document-density-control.md](../context-load-and-document-density-control.md)
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-05-10 | **[Added opportunistic touched-doc God-line repair](#version-11)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Refined the active owner so clear low-risk touched God-line candidates are repaired in the same edit while broad or meaning-risky repairs are flagged or planned. | |
| 1.0 | 2026-05-10 | **[Created context-load and document-density control](#version-10)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Added a runtime owner for leader-context protection, worker-first broad reading, aggregate read-burst awareness, God-line prevention, append-vs-restructure gates, and compact/thrash repair signals. | |

---

<a id="version-11"></a>
## Version 1.1: Added opportunistic touched-doc God-line repair

**Date:** 2026-05-10
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Required immediate local repair when a touched active-doc God-line candidate has a clear, low-risk semantic split.
- Added boundaries for broad, history-heavy, ambiguous, or meaning-risky density debt so those cases are flagged or planned instead of silently rewritten.
- Strengthened append-vs-restructure behavior so known God-line candidates do not receive more append-only content unless a safer structure is unavailable and the limit is stated.
- Updated verification expectations to check repaired or explicitly flagged touched-doc God-line candidates.

### Summary
The context-load and document-density owner now treats clear touched-doc God-line repair as an operational behavior, not only a warning or future cleanup note.

---

<a id="version-10"></a>
## Version 1.0: Created context-load and document-density control

**Date:** 2026-05-10
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Created `context-load-and-document-density-control.md` as a new active runtime rule.
- Created `design/context-load-and-document-density-control.design.md` as the target-state design companion.
- Defined leader-context protection as a lifecycle requirement, not only a post-compact precaution.
- Added worker-first broad raw evidence filtering as the preferred shape for context-heavy reads.
- Added aggregate read-burst awareness so several bounded reads are evaluated together.
- Added document-density and God-line prevention doctrine for active governance docs.
- Added append-vs-restructure gates for dense active summary lines.
- Defined compact/thrash as a repair signal for workflow or document structure.

### Summary
Context-load and document-density control now has its own runtime owner so broad reading, dense writing, worker routing, and compact/thrash repair can be managed as one process.
