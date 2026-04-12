# Changelog - High Signal Communication

> **Parent Document:** [../high-signal-communication.md](../high-signal-communication.md)
> **Current Version:** 1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-04-11 | **[Promoted high-signal communication into the active rule set](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Removed standalone experimental framing, narrowed the rule to supplementary high-signal filtering mechanisms, and aligned it with the active runtime install set | |
| 1.0 | 2026-04-11 | **[Created standalone experimental high-signal communication rule](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a separate experimental rule that tests extra-content admission, post-draft pruning, and bounded expansion without integrating into the active rule graph | |

---

<a id="version-11"></a>
## Version 1.1: Promoted high-signal communication into the active rule set

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `high-signal-communication.md` from v1.0 to v1.1.
- Updated `design/high-signal-communication.design.md` from v1.0 to v1.1.
- Removed standalone experimental framing so the rule now reads as an active bounded supplementary rule.
- Narrowed the allowed scope to extra-content admission filtering and repetition pruning instead of keeping a broader standalone experiment posture.
- Marked the rule as part of the active runtime install set while preserving the boundary that existing communication, explanation, and presentation owners still win on required content.

### Summary
High-signal communication now behaves as an active bounded supplementary rule instead of a standalone experiment, while staying narrow enough not to replace the main communication-owner chains.

---

<a id="version-10"></a>
## Version 1.0: Created standalone experimental high-signal communication rule

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `high-signal-communication.md` as a standalone experimental communication rule.
- Created `design/high-signal-communication.design.md` as the experimental design companion.
- Limited the experiment to supplementary mechanisms only:
  - extra-content admission gate
  - post-draft pruning pass
  - expansion budget gate
- Explicitly kept the experiment outside the active runtime install set and outside the current communication-owner integration path.

### Summary
Created a standalone experimental high-signal communication rule so its effect can be observed without changing the active rule graph.
