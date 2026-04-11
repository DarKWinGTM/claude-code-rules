# Changelog - Table Format and Usage

> **Parent Document:** [../suspend/table-format-and-usage.md](../suspend/table-format-and-usage.md)
> **Current Version:** 1.4
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.4 | 2026-04-11 | **[Reframed the file fully as suspended reference material](#version-14)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Removed stale active-owner detail from the retained file and rewrote it as suspended reference material for later redesign only | |
| 1.3 | 2026-04-11 | **[Suspended custom table-format rule from active RULES enforcement](#version-13)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Kept the file for later redesign, but removed it from the active RULES enforcement path and restored adjacent chains to general table support without custom format enforcement | |
| 1.2 | 2026-04-11 | **[Added character-level no-box enforcement and send-time self-check](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Hardened the central table owner so generic table requests still require the canonical no-frame style, box-drawing frame characters are treated as non-compliant in ordinary assistant answers, and visible output shape must be checked before send | |
| 1.1 | 2026-04-11 | **[Made boxed/full-frame/Unicode box-drawing table prohibition explicit](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Tightened the central table owner so ordinary assistant answers now explicitly forbid boxed/full-frame/Unicode box-drawing tables while keeping the canonical no-frame style and clarifying that `|` separators remain allowed | |
| 1.0 | 2026-04-11 | **[Created first-class table-format-and-usage rule chain](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a new design/runtime/changelog triad that centralizes ordinary answer-table usage, default style, list-versus-table boundary, bounded markdown-table exceptions, and table anti-pattern ownership | |

---

<a id="version-14"></a>
## Version 1.4: Reframed the file fully as suspended reference material

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage.md` from v1.3 to v1.4.
- Updated `design/table-format-and-usage.design.md` from v1.3 to v1.4.
- Removed stale active-owner and custom-format detail from the retained file body.
- Rewrote the file/design pair so they now describe suspended status, active-system boundary, and later reactivation only.
- Preserved the file in-repo as future reference material without returning it to the active install set.

### Summary
Table-format-and-usage now reads as suspended reference material only, so the retained file no longer leaves stale active-detail drift behind.

---

<a id="version-13"></a>
## Version 1.3: Suspended custom table-format rule from active RULES enforcement

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage.md` from v1.2 to v1.3.
- Updated `design/table-format-and-usage.design.md` from v1.2 to v1.3.
- Reframed the file as a retained-but-suspended custom table-format experiment instead of an active RULES owner.
- Removed active rule-chain dependency on this file from `answer-presentation` and `explanation-quality`.
- Kept the file in the repository for later redesign rather than deleting it.

### Summary
Table-format-and-usage is now preserved as a future design candidate, but it is no longer part of the active RULES enforcement path.

---

<a id="version-12"></a>
## Version 1.2: Added character-level no-box enforcement and send-time self-check

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage.md` from v1.1 to v1.2.
- Updated `design/table-format-and-usage.design.md` from v1.1 to v1.2.
- Added explicit wording that a generic request for a table still requires the canonical no-frame format rather than leaving style optional.
- Added character-level no-box enforcement so box-drawing frame characters such as `┌`, `┐`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`, and `│` are treated as non-compliant in ordinary assistant answers.
- Added a send-time visible-shape self-check so the assistant should rewrite framed table output before sending instead of trusting an internal label such as "plain no-frame".

### Summary
Table-format-and-usage now hardens no-box enforcement by treating box-drawing frame characters as non-compliant in ordinary assistant answers and by requiring one last visible-shape check before send.

---

<a id="version-11"></a>
## Version 1.1: Made boxed/full-frame/Unicode box-drawing table prohibition explicit

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage.md` from v1.0 to v1.1.
- Updated `design/table-format-and-usage.design.md` from v1.0 to v1.1.
- Replaced the earlier generic anti-heavy-frame wording with an explicit prohibition for boxed, full-frame, and Unicode box-drawing tables in ordinary assistant answers.
- Clarified that the canonical no-frame house style may still use `|` separators and `-` separator lines, so the prohibition targets frame weight rather than the mere use of pipe characters.
- Preserved markdown-table syntax as a bounded syntax/artifact exception rather than an ordinary answer default.

### Summary
Table-format-and-usage now makes the no-box rule explicit for ordinary assistant answers while keeping the selected plain aligned no-frame format as the required default and clarifying that pipe separators themselves remain allowed.

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
