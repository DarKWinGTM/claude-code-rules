# Phase 067-01 - Clarify legacy history authority boundaries

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 067-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/design.md](../design/design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/legacy-history-authority-boundary-clarification.patch.md](../patch/legacy-history-authority-boundary-clarification.patch.md)

---

## Objective

Clarify that older shared-board / session-title rollout records in RULES history remain historical context only and do not override the current active RULES authority boundary.

## Why this phase exists

The active RULES cleanup already narrowed current doctrine correctly, but some older master/history records could still read broader than the current boundary.
The remaining job is not to rewrite the past; it is to make the present authority boundary easier to read:
- current active doctrine stays in the active runtime/design surfaces
- older coordination-flavored rollout records remain historical context only
- the clarification should stay inside RULES master/history surfaces without reopening plugin/package work

## Action points / execution checklist

- [x] add a bounded historical-only clarification to the master design/overview surfaces
- [x] add a bounded clarification entry to `TODO.md`
- [x] add a bounded clarification wave to `phase/SUMMARY.md`
- [x] record the clarification wave in `changelog/changelog.md`
- [x] keep the wave RULES-side only without reopening plugin/package edits

## Verification

- [x] active RULES authority still points to the current runtime/design surfaces rather than older coordination-history wording
- [x] older shared-board/session-title records now read as historical context only where the clarification was added
- [x] touched master/history surfaces record the clarification coherently
- [x] no plugin/package files were touched by this wave

## Exit criteria

- [x] readers can distinguish current active RULES authority from legacy coordination-flavored history more easily
- [x] the clarification wave remains bounded to RULES-side master/history surfaces
