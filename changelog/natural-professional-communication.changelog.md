# Changelog - Natural Professional Communication

> **Parent Document:** [../natural-professional-communication.md](../natural-professional-communication.md)
> **Current Version:** 1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-04-09 | **[Added purpose-before-detail guidance for operational answers](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.1 | 2026-04-08 | **[Rejected metaphor-heavy abstraction as a default professional style](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.0 | 2026-03-27 | **[Created first-class natural-professional-communication rule chain](#version-10)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| | | Summary: Created a new communication-style doctrine rule so the assistant now has one explicit semantic owner for natural professional, non-robotic, non-character-driven default communication | |

---

<a id="version-12"></a>
## Version 1.2: Added purpose-before-detail guidance for operational answers

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `natural-professional-communication.md` from v1.1 to v1.2.
- Updated `design/natural-professional-communication.design.md` from v1.1 to v1.2.
- Added a purpose-before-detail principle so diagnosis, test, recommendation, proposal, and implementation-update answers now say what they are doing directly instead of making the reader wait through warm-up framing.
- Added trigger, example, and anti-pattern coverage against openings that delay the operational point.

### Summary
Natural-professional-communication now treats purpose-before-detail wording as part of sounding like a strong human operator rather than a warm-up-heavy scripted assistant.

---

<a id="version-11"></a>
## Version 1.1: Rejected metaphor-heavy abstraction as a default professional style

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `natural-professional-communication.md` from v1.0 to v1.1.
- Updated `design/natural-professional-communication.design.md` from v1.0 to v1.1.
- Added guidance that professional wording should not drift into metaphor-heavy or management-style abstraction when a direct human-readable action/result statement would be clearer.
- Added anti-pattern coverage against abstract wording that sounds professional but still makes the reader decode what practically changed.

### Summary
Natural-professional-communication now treats direct human-readable wording as the professional default and rejects metaphor-heavy abstraction as a default style.

---

<a id="version-10"></a>
## Version 1.0: Created first-class natural-professional-communication rule chain

**Date:** 2026-03-27
**Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2

### Changes
- Created `design/natural-professional-communication.design.md` as the target-state doctrine for natural professional communication.
- Created runtime `natural-professional-communication.md` as a first-class rule defining:
  - the default natural professional register
  - signal-over-ceremony wording
  - non-robotic / non-character-driven default behavior
  - warmth calibration without fake-empathy drift
  - anti-performative communication boundaries
- Positioned the chain as a communication-style owner that works with, rather than replacing, wording, explanation, presentation, authority, and evidence owners.

### Summary
Created a first-class natural-professional-communication rule chain so the system now has one explicit semantic owner for calm, human-readable, non-robotic, non-character-driven default communication.
