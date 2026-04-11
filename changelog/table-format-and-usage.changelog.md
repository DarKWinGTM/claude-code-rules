# Changelog - Table Format and Usage

> **Parent Document:** [../table-format-and-usage.md](../table-format-and-usage.md)
> **Current Version:** 1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-04-11 | **[Created first-class table-format-and-usage rule chain](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a new design/runtime/changelog triad that centralizes ordinary answer-table usage, default style, list-versus-table boundary, bounded markdown-table exceptions, and table anti-pattern ownership | |

---

<a id="version-10"></a>
## Version 1.0: Created first-class table-format-and-usage rule chain

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `design/table-format-and-usage.design.md` as the active target-state design for centralized table semantics.
- Created runtime `table-format-and-usage.md` as a first-class rule defining:
  - ordinary answer-table ownership
  - table-when-tabular usage boundaries
  - list/prose alternatives for sequence, status, and non-tabular content
  - the selected light plain aligned no-frame default style
  - anti-pattern rejection for boxed/full-frame and generic markdown-pipe defaults in ordinary answers
  - explicit markdown-source and explicit-request exceptions
- Positioned the chain as the semantic owner that adjacent presentation and explanation chains defer to rather than co-owning in full.
- Explicitly kept memory out of table-policy ownership so RULES remain the active authority.

### Summary
Created a first-class `table-format-and-usage` rule chain so ordinary answer-table behavior now has one durable semantic owner instead of remaining split across adjacent presentation and explanation owners.
