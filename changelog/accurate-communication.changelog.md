# Changelog - Accurate Communication Standard

> **Parent Document:** [../accurate-communication.md](../accurate-communication.md)
> **Current Version:** 2.5
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.5 | 2026-04-03 | **[Added recommended-option wording for multi-path next actions](#version-25)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 2.4 | 2026-04-03 | **[Added continuation-first execution guidance to accurate-communication](#version-24)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 2.3 | 2026-04-02 | **[Scoped exact environment values as local facts in technical snapshots](#version-23)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Extended accurate-communication so exact paths, ports, hosts, and similar environment-specific values in snapshots must remain scoped local facts rather than reading like portable defaults | |
| 2.2 | 2026-03-27 | **[Added natural-professional wording calibration to accurate-communication](#version-22)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| | | Summary: Extended accurate-communication with natural-professional, anti-robotic, signal-over-ceremony wording guidance so technically correct answers also read more like calm human professional communication | |
| 2.1 | 2026-03-17 | **[Added stage-progression and whole-set wording guidance to accurate-communication](#version-21)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | Summary: Extended accurate-communication so answers can state when the next useful move is the next stage and can explain that the full relevant set should be shown before narrowing into a smaller slice | |
| 2.0 | 2026-03-15 | **[Extended accurate-communication for easier reader-facing terminology glosses](#version-20)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | Summary: Extended accurate-communication with stronger guidance and examples for directly glossing internal or technical terminology in plain language when that materially improves reader understanding | |
| 1.9 | 2026-03-15 | **[Added human-language glossary guidance for easier explanatory communication](#version-19)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | Summary: Extended accurate-communication with guidance and examples for directly glossing internal or technical terminology in plain language when that materially improves reader understanding | |
| 1.8 | 2026-03-15 | **[Added richer partial-evidence wording examples for technical status reporting](#version-18)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | Summary: Extended accurate-communication with richer example coverage for mixed exact/partial facts and scoped environment summaries so technical status wording is easier to apply without overclaiming | |
| 1.7 | 2026-03-14 | **[Added bounded technical snapshot wording for partial-evidence status reporting](#version-17)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | Summary: Extended accurate-communication so technical snapshots now separate exact captured facts, partial checked facts, and inferred implications without pretending incomplete evidence is exact capture | |
| 1.6 | 2026-03-12 | **[Added evidence-threshold communication guidance and contradiction-wording guardrails](#version-16)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | Summary: Strengthened accurate-communication so verified fact, inference, hypothesis, unresolved uncertainty, and scoped non-findings now have explicit wording guidance, and the rule now directly forbids saying the user is wrong/mistaken/confused without cited contrary evidence | |
| 1.5 | 2026-03-11 | **[Made next-step options context-beneficial rather than default](#version-15)** | 92fed037-8ba9-48a6-95c4-e1085f28bb32 |
| | | Summary: Refined accurate-communication so next-step options are offered only when genuinely helpful and not as a mandatory ending pattern | |
| 1.4 | 2026-03-11 | **[Prevented artificial next-step options after completed work](#version-14)** | 92fed037-8ba9-48a6-95c4-e1085f28bb32 |
| | | Summary: Narrowed accurate-communication so completed tasks do not trigger invented extra options when no real next action is needed | |
| 1.3 | 2026-03-09 | **[Added high-signal summary and clear-next-step communication guidance](#version-13)** | b1fc974f-b7df-4f24-9080-c941153612ca |
| | | Summary: Strengthened accurate-communication so explanation-heavy answers end with concise synthesis and explicit next-step guidance without rigid sentence caps | |
| 1.2 | 2026-03-08 | **[Normalized accurate-communication design to active-state navigator behavior](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Rewrote the design artifact to active-state-only guidance, removed embedded history-table behavior, and aligned the chain to the cleanup-wave metadata model | |
| 1.1 | 2026-02-06 | **[Redesign as Flexible Principles](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | - Changed from rigid rules to smart principles | |
| | | - Added context-based flexibility guidelines | |
| | | Summary: Redesigned for practical, flexible use | |
| 1.0 | 2026-02-06 | **[Initial Design](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | - Created as rigid rules (too strict) | |
| | | Summary: Initial version - later deemed too rigid | |

---

<a id="version-25"></a>
## Version 2.5: Added recommended-option wording for multi-path next actions

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `accurate-communication.md` from v2.4 to v2.5.
- Updated `design/accurate-communication.design.md` from v2.4 to v2.5.
- Added wording guidance so when multiple reasonable next actions are shown, the better-supported option is named first as the recommendation.
- Added a requirement to include one short plain-language `Why this first` reason after the recommendation.
- Added example and anti-pattern coverage so option lists no longer omit the preferred path when the checked reasoning already supports one.

### Summary
Accurate-communication now keeps multi-option next-step guidance easier to act on by explicitly naming the recommended path and the reason it should happen first.

---

<a id="version-24"></a>
## Version 2.4: Added continuation-first execution guidance to accurate-communication

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `accurate-communication.md` from v2.3 to v2.4.
- Updated `design/accurate-communication.design.md` from v2.3 to v2.4.
- Added an explicit continuation-first execution guidance section so active requested work continues by default when no clarification, approval, or stronger rule-owned gate blocks it.
- Clarified that next-step narration should not interrupt active work when the assistant can safely continue the same objective directly.
- Narrowed closing guidance so options remain available only when a real user decision or materially divergent path exists.

### Summary
Accurate-communication now explicitly prefers continuing safe active work over pausing for optional mid-process next-step prompts.

---

<a id="version-23"></a>
## Version 2.3: Scoped exact environment values as local facts in technical snapshots

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `accurate-communication.md` from v2.2 to v2.3.
- Updated `design/accurate-communication.design.md` from v2.2 to v2.3.
- Added wording guidance so exact local paths, ports, hosts, and similar environment-specific values in technical snapshots stay scoped as observed local facts.
- Added explicit deferral to `portable-implementation-and-hardcoding-control.md` for broader portable-default and anti-hardcoding ownership.

### Summary
Extended accurate-communication so machine-specific environment values in technical snapshots stay evidence-scoped instead of reading like portable defaults.

---

<a id="version-22"></a>
## Version 2.2: Added natural-professional wording calibration to accurate-communication

**Date:** 2026-03-27
**Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2

### Changes
- Updated `accurate-communication.md` from v2.1 to v2.2.
- Updated `design/accurate-communication.design.md` from v2.1 to v2.2.
- Added explicit natural-professional wording guidance so technically correct answers also avoid robotic, ceremonial, or over-produced phrasing.
- Added direct guidance against exaggerated enthusiasm, fake empathy, and ritualized openings when they do not help the user.
- Added new examples and anti-patterns for calm, human-readable professional wording.

### Summary
Extended accurate-communication with natural-professional, anti-robotic, signal-over-ceremony wording guidance so technically correct answers also read more like calm human professional communication.

---

<a id="version-21"></a>
## Version 2.1: Added stage-progression and whole-set wording guidance to accurate-communication

**Date:** 2026-03-17
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Updated `accurate-communication.md` from v2.0 to v2.1.
- Updated `design/accurate-communication.design.md` from v2.0 to v2.1.
- Added wording guidance so responses can state clearly when the next useful move is the next stage/state rather than deeper explanation in the same scope.
- Added wording guidance so the full relevant set can be presented before narrowing into smaller sub-items.
- Added examples for moving to the next state and showing the whole set first.

### Summary
Extended accurate-communication so answers can state when the next useful move is the next stage and can explain that the full relevant set should be shown before narrowing into a smaller slice.

---

<a id="version-20"></a>
## Version 2.0: Extended accurate-communication for easier reader-facing terminology glosses

**Date:** 2026-03-15
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Updated `accurate-communication.md` from v1.9 to v2.0.
- Updated `design/accurate-communication.design.md` from v1.9 to v2.0.
- Strengthened wording guidance for directly glossing internal or technical terms in plain language when that materially improves understanding.
- Added explicit runtime examples for user-facing paraphrases around routing-mode and customer-supplied-runtime terminology.
- Preserved the evidence-honesty boundary so these glosses clarify terminology without weakening technical truth or claim-state discipline.

### Summary
Extended accurate-communication with stronger human-language gloss guidance so answers can explain internal or technical terms more clearly without weakening evidence or claim-state discipline.

---

<a id="version-19"></a>
## Version 1.9: Added human-language glossary guidance for easier explanatory communication

**Date:** 2026-03-15
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Updated `accurate-communication.md` from v1.8 to v1.9.
- Updated `design/accurate-communication.design.md` from v1.8 to v1.9.
- Added wording guidance for directly glossing internal or technical terms in plain language when that materially improves understanding.
- Added explicit example coverage for human-language paraphrases such as explaining routing-mode and runtime-orchestration terms in user-facing language.
- Preserved the existing evidence-honesty boundary so these glosses clarify terminology without replacing technical truth.

### Summary
Extended accurate-communication with human-language gloss guidance so answers can explain internal or technical terms more clearly without weakening evidence or claim-state discipline.

---

<a id="version-18"></a>
## Version 1.8: Added richer partial-evidence wording examples for technical status reporting

**Date:** 2026-03-15
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Updated `accurate-communication.md` from v1.7 to v1.8.
- Updated `design/accurate-communication.design.md` from v1.7 to v1.8.
- Added richer example coverage for mixed exact and partial facts inside one bounded technical snapshot.
- Added a scoped environment-summary example for technical status reports where the full runtime state is not fully captured.
- Strengthened the practical example bank so partial-evidence wording is easier to apply in real troubleshooting and verification updates without implying exact capture.

### Summary
Extended accurate-communication with richer example coverage for mixed exact/partial facts and scoped environment summaries so technical status wording is easier to apply without overclaiming.

---

<a id="version-17"></a>
## Version 1.7: Added bounded technical snapshot wording for partial-evidence status reporting

**Date:** 2026-03-14
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Updated `accurate-communication.md` from v1.6 to v1.7.
- Updated `design/accurate-communication.design.md` from v1.6 to v1.7.
- Added a bounded technical snapshot wording principle for compact diagnostic and technical status reporting.
- Defined explicit wording separation between exact captured facts, partial checked facts, and inferred implications.
- Added preferred wording patterns such as `From the checked scope, ...` and `I could not capture the exact request, but ...` for partial-but-verified reporting.
- Extended the application model and decision framework so troubleshooting, progress, and verification updates keep evidence boundaries visible inside compact snapshots.
- Added anti-pattern coverage for pretending exact capture from partial evidence.
- Updated examples and quality metrics to reinforce honest partial-evidence status reporting.

### Summary
Extended accurate-communication so technical snapshots now separate exact captured facts, partial checked facts, and inferred implications without pretending incomplete evidence is exact capture.

---

<a id="version-16"></a>
## Version 1.6: Added evidence-threshold communication guidance and contradiction-wording guardrails

**Date:** 2026-03-12
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `accurate-communication.md` from v1.5 to v1.6.
- Updated `design/accurate-communication.design.md` from v1.4 to v1.6 and corrected the prior runtime/design metadata drift.
- Added explicit evidence-threshold wording guidance for:
  - verified fact
  - observed local fact
  - evidence-backed inference
  - working hypothesis
  - unresolved uncertainty
  - scoped non-findings
- Added a contradiction-wording guardrail that forbids saying the user is wrong, mistaken, or confused without cited contrary evidence.
- Clarified that contradiction wording should stay claim-focused by default rather than person-focused.
- Added scoped negative-result honesty language so limited non-findings are not phrased as global absence.

### Summary
Strengthened accurate-communication so the wording layer now exposes evidence strength honestly and no longer permits person-directed contradiction language without contrary evidence.

---

<a id="version-15"></a>
## Version 1.5: Made next-step options context-beneficial rather than default

**Date:** 2026-03-11
**Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32

### Changes
- Updated `accurate-communication.md` from v1.4 to v1.5.
- Updated `design/accurate-communication.design.md` from v1.4 to v1.5.
- Clarified that direct next actions or option lists should be offered only when they genuinely help the user.
- Clarified that multiple explicit options are for materially useful continuation paths, not a required ending style.
- Preserved the rule that completed work with no real next action should not invent extra options.

### Summary
Refined accurate-communication so next-step options are helpful when useful, but not mandatory or artificially generated when the response can end cleanly.

---

<a id="version-14"></a>
## Version 1.4: Prevented artificial next-step options after completed work

**Date:** 2026-03-11
**Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32

### Changes
- Updated `accurate-communication.md` from v1.3 to v1.4.
- Updated `design/accurate-communication.design.md` from v1.3 to v1.4.
- Clarified that when work is already complete and no real next action is needed, the response should not invent extra options.
- Preserved the ability to present direct next actions or short options only when there is a real continuation path.

### Summary
Refined accurate-communication so completed work can end cleanly without artificial extra options, reducing endless follow-up expansion.

---

<a id="version-13"></a>
## Version 1.3: Added high-signal summary and clear-next-step communication guidance

**Date:** 2026-03-09
**Session:** b1fc974f-b7df-4f24-9080-c941153612ca

### Changes
- Updated `accurate-communication.md` from v1.2 to v1.3.
- Updated `design/accurate-communication.design.md` from v1.2 to v1.3.
- Added explicit guidance to prefer synthesis over repetition in explanation-heavy responses.
- Added concise-closing guidance focused on:
  - high-signal summary quality
  - no rigid sentence cap
  - direct next action when one clear path exists
  - short explicit options when multiple reasonable next steps exist
- Added anti-pattern coverage for repetitive summaries and endings with no clear next path.

### Summary
Strengthened accurate-communication so responses can stay explanatory while still ending with concise synthesis and a clear path forward.

---

<a id="version-12"></a>
## Version 1.2: Normalized accurate-communication design to active-state navigator behavior

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `design/accurate-communication.design.md` from v1.1 to v1.2.
- Rewrote the design document into active-state design guidance.
- Removed embedded version-history-table behavior from the design artifact.
- Normalized the design document to pair-model expectations where detailed history lives in the changelog only.
- Prepared the chain for runtime header normalization under the cleanup-wave metadata model.

### Summary
Converted the accurate-communication design artifact into active-state-only guidance so it no longer behaves like a mixed design-plus-history document.

---

<a id="version-11"></a>
## Version 1.1: Redesign as Flexible Principles

**Date:** 2026-02-06
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Changed from rigid format rules to smart, flexible principles
- Introduced two core principles:
  1. Communication Clarity Principle: "The receiver must understand the complete context from a single message."
  2. Verification Honesty Principle: "Claim only what can be proven."
- Added context-based flexibility guidelines
- Added decision framework for when to apply each principle
- Added anti-patterns to avoid

### Summary
Redesigned from rigid rules to smart, flexible principles that can be applied with judgment based on context.

### Rationale
User feedback: "Want to create rules that are smart, flexible, and usable, not rigid and stupid rules."

---

<a id="version-10"></a>
## Version 1.0: Initial Design

**Date:** 2026-02-06
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created initial design with rigid format requirements
- Required specific format for all problem statements
- Required specific format for all success claims

### Summary
Initial version created with rigid rules - later redesigned to be more flexible.

### Issues Found
- Rules were too rigid and format-focused
- Did not allow for context-based judgment
- Would be annoying to follow strictly
