# Generated Artifacts and Hook Posture

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define which generated artifacts the plugin should emit and how hooks may support the system without becoming hidden semantic governance.

## 2) Generated artifact model

The plugin should prefer reviewable generated artifacts over silent mutation.

Recommended artifact families:
- scan record
- governed review packet
- repair-plan artifact
- phase-audit record
- release-gate record
- normalization preview / dry-run artifact
- article presentation preview artifact

Each artifact should preserve:
- checked scope
- doctrine input set
- observed facts
- classification result
- recommended action or gate decision
- preservation notes
- unresolved ambiguity or approval boundary

## 3) Why generated artifacts matter

Generated artifacts make the plugin's work:
- replayable
- inspectable
- auditable
- easier to review before mutation
- less likely to turn support tooling into hidden authority

This is a better fit for RULES than a bot that silently edits docs first and explains later.

## 4) Hook posture

Hooks are allowed only as support surfaces.

### Allowed hook uses
- startup/reminder context
- compact-time maintenance reminders
- stop-time guardrails for stronger closeout wording
- event-triggered diagnostics such as phase filename grammar warnings

### Hook outputs may do
- remind
- trigger a review
- point to likely drift
- gate stronger wording when evidence is absent

### Hook outputs must not do
- silently normalize governed docs
- silently promote plugin findings into RULES truth
- replace the main session's synthesis and approval role
- act as hidden deletion/cleanup authority

## 5) Suggested hook style for v1

V1 should be hook-light:
- reminder-first
- guardrail-second
- no auto-maintenance hook path by default

This keeps the companion operationally helpful without making runtime hook behavior the real owner of governance decisions.

## 6) Before / After behavior for hook risk

### Before
- operators may forget to run a consistency sweep before closeout
- large TODO/SUMMARY drift may remain invisible until late
- malformed phase naming may be noticed only after broader drift accumulates

### After
- lightweight hooks can remind or block stronger claims when a review is missing
- the plugin can surface bounded diagnostics earlier
- the actual repair decision still remains explicit and reviewable

## 7) Non-goals for automation risk

V1 hooks must not:
- edit doc files in the background
- generate new authority surfaces automatically
- remove done/history artifacts by perceived tidiness
- escalate an advisory signal into a semantic truth claim

---

> Hook rule: runtime reminders and bounded guards are acceptable; hidden maintenance authority is not.
