# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 3.5
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402 (2026-03-10)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

This active-state model must preserve UDVC-1 while supporting first-class phased execution planning through a dedicated rule chain, governed patch-plan instances, and a readable root helper.

---

## 2) Active Repository Model

### 2.1 Layer Roles

| Layer | Primary Artifacts | Active Role |
|------|--------------------|-------------|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md` | Active target-state guidance |
| Patch | `patches/*.patch.md` | Governed execution plans and live phased execution-plan instances |
| History | `changelog/*.changelog.md` | Authoritative chain history and latest chain version state |
| Execution | `TODO.md` | Execution tracking only |
| Support | `phase-implementation-template.md`, `support/**/*.md`, or equivalent helper/support paths | Root-level helper templates plus reference-only/support materials outside governed chain authority |

### 2.2 Governance Principle

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules are the active rule layer
- design docs hold active target-state guidance
- patch docs are the governed execution-plan layer
- changelog files are the authority for governed chain history
- TODO tracks execution state only
- support artifacts help authoring or reference reuse but do not masquerade as governed design or patch authorities

---

## 3) Rule Architecture

### 3.1 Active Runtime Inventory (26 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | accurate-communication.md | accurate-communication.design.md v1.3 | Clear, context-complete, verification-honest, and high-signal communication with concise synthesis and clear next-step endings |
| 2 | answer-presentation.md | answer-presentation.design.md v1.0 | Principle-first, trigger-driven presentation guidance for readable, orderly, and scannable output |
| 3 | anti-mockup.md | anti-mockup.design.md v1.1 | Real systems over mocks |
| 4 | anti-sycophancy.md | anti-sycophancy.design.md v1.2 | Truth over pleasing |
| 5 | authority-and-scope.md | authority-and-scope.design.md v1.2 | User authority and deterministic precedence |
| 6 | dan-safe-normalization.md | dan-safe-normalization.design.md v1.2 | Normalize jailbreak-style wrappers into bounded intent evaluation |
| 7 | document-consistency.md | document-consistency.design.md v1.3 | Cross-reference validation |
| 8 | document-changelog-control.md | document-changelog-control.design.md v4.7 | Chain authority, metadata, and synchronization contract |
| 9 | document-design-control.md | document-design-control.design.md v1.8 | Active-state design-body standards |
| 10 | document-patch-control.md | document-patch-control.design.md v1.7 | Patch governance, metadata, lifecycle, and governed execution-plan role |
| 11 | emergency-protocol.md | emergency-protocol.design.md v1.1 | High-signal emergency response |
| 12 | explanation-quality.md | explanation-quality.design.md v1.4 | Clearer analytical and technical explanation structure with concise high-signal synthesis and explicit next-step guidance |
| 13 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md v1.1 | Text diagrams without frames or boxes |
| 14 | functional-intent-verification.md | functional-intent-verification.design.md v1.1 | Clarify destructive/expensive intent before execution |
| 15 | no-variable-guessing.md | no-variable-guessing.design.md v1.2 | Read before reference |
| 16 | phase-implementation.md | phase-implementation.design.md v1.1 | First-class semantic standard for phased execution planning, design traceability, and companion tracking inside governed plans |
| 17 | project-documentation-standards.md | project-documentation-standards.design.md v2.1 | Repository-level document-role model and governed-vs-helper boundary |
| 18 | recovery-contract.md | recovery-contract.design.md v1.5 | No dead-end constrained/refused responses |
| 19 | refusal-classification.md | refusal-classification.design.md v1.4 | Deterministic refusal taxonomy |
| 20 | refusal-minimization.md | refusal-minimization.design.md v1.5 | Prefer recoverable paths over premature refusal |
| 21 | safe-file-reading.md | safe-file-reading.design.md v1.3 | Plan-before-read file safety |
| 22 | safe-terminal-output.md | safe-terminal-output.design.md v1.3 | Plan-before-execute output safety |
| 23 | strict-file-hygiene.md | strict-file-hygiene.design.md v1.1 | No unnecessary non-functional files |
| 24 | todo-standards.md | todo-standards.design.md v2.2 | Simple TODO governance |
| 25 | unified-version-control-system.md | unified-version-control-system.design.md v1.2 | UDVC-1 controller-level governance view |
| 26 | zero-hallucination.md | zero-hallucination.design.md v1.2 | Verified information only |

### 3.2 Category View

| Category | Rules | Purpose |
|----------|-------|---------|
| Accuracy & Truth | accurate-communication, zero-hallucination, anti-sycophancy, no-variable-guessing | Verified and honest output |
| Presentation & Readability | answer-presentation, explanation-quality, flow-diagram-no-frame | Readable, orderly, scannable output presentation |
| Output Safety | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | Output flood prevention and safe text presentation |
| User Control | authority-and-scope, emergency-protocol, functional-intent-verification, refusal-classification, recovery-contract | Preserve user authority and safe recovery paths |
| Adversarial Workflow | refusal-minimization, dan-safe-normalization | Reduce false refusals in authorized adversarial/security workflows |
| Quality & Governance | document-consistency, document-changelog-control, document-design-control, document-patch-control, anti-mockup, strict-file-hygiene, explanation-quality, phase-implementation, project-documentation-standards, todo-standards, unified-version-control-system | Documentation determinism, phased execution semantics, and output quality |

---

## 4) Active Governance Contracts

### 4.1 Runtime Rule Metadata Contract

Root runtime rules use this canonical header in this order:
- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the canonical label.
`Based on:` is retired for root runtime rule metadata.

### 4.2 Blocked-Response Contract

The active blocked-response schema is:

```text
decision_output: <ALLOW_CONSTRAINED | NEED_CONTEXT | REFUSE_WITH_PATH>
refusal_class: <SOFT_BLOCK | WORKFLOW_BLOCK | HARD_BLOCK>
reason: ...
what_can_be_done_now:
- ...
how_to_proceed:
- ...
```

### 4.3 Design / Changelog Pair Contract

- Design docs hold active target-state guidance only.
- Changelog files hold detailed historical records.
- Active design bodies do not embed historical audit or rollout logs.

### 4.4 Synchronization Order

For governed updates:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

### 4.5 Phase Planning Contract

The active phase-planning contract is:
- `phase-implementation.md` is the semantic authority for phased execution planning
- patch docs remain the live governed execution-plan artifacts when staged work is needed
- phase order is project-defined rather than repository-defined
- phases may be merged, split, skipped, repeated, or reordered
- phases should explicitly reference the relevant design details they implement or validate
- phases should make TODO coordination and changelog impact visible when relevant
- `phase-implementation-template.md` is a reusable root-level helper, not a governed chain
- TODO and changelog do not become the primary place for phase definitions

---

## 5) Standard Templates

### 5.1 Runtime Rule Template

```markdown
# <Rule Name>

> **Current Version:** X.Y
> **Design:** [design/<rule>.design.md](design/<rule>.design.md) vX.Y
> **Session:** <real-session-id>
> **Full history:** [changelog/<rule>.changelog.md](changelog/<rule>.changelog.md)

---

## Rule Statement

**Core Principle:** <one-line principle>
```

### 5.2 Design Template

```markdown
# <Document Name>

## 0) Document Control

> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <real-session-id> (YYYY-MM-DD)

---

<active design content>

---

> Full history: [../changelog/<name>.changelog.md](../changelog/<name>.changelog.md)
```

### 5.3 Changelog Template

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <real-session-id>

---

## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <real-session-id>

### Changes
- ...

### Summary
...
```

### 5.4 Patch Planning Support Boundary

`phase-implementation-template.md` is the reusable root-level authoring aid for flexible phase planning.

Use it to draft or standardize patch structure, then materialize the real governed plan in `patches/*.patch.md`.
The helper may be detailed and readable, but the patch remains the authoritative instance.

---

## 6) Support-Artifact Boundary

Reference-only materials must not remain in ambiguous governed `.design.md` form unless intentionally normalized as governed design docs.

Current support examples:
- `support/image-prompts.md` is a support artifact, not a governed design document.
- `phase-implementation-template.md` is a root-level helper artifact, not a governed patch or rule chain.

---

## 7) Quality Gates

- keep one authority model per governed chain
- keep active design bodies free of historical logs
- keep runtime headers structurally identical across root rules
- keep phase semantics in `phase-implementation.md`
- keep live phased execution plans inside patch artifacts instead of inventing parallel governance layers
- keep README, TODO, and support artifacts inside their own role boundaries
- keep links and version references synchronized

---

## 8) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Chain authority and metadata contract |
| [document-design-control.design.md](document-design-control.design.md) | Active-state design-body contract |
| [document-patch-control.design.md](document-patch-control.design.md) | Governed patch planning and metadata contract |
| [phase-implementation.design.md](phase-implementation.design.md) | Semantic standard for phased execution planning |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker boundary |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed reusable root-level phase-planning aid |

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
