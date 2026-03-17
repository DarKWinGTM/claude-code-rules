# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.3
> **Session:** 77d0802a-fd64-4023-a66d-88c165ccca12 (2026-03-17)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

This active-state model must preserve UDVC-1 while supporting first-class phased execution planning through a dedicated rule chain, governed patch-plan instances, a readable root helper, and one-way source synthesis from design and relevant patch inputs into the live phase layer.

---

## 2) Active Repository Model

### 2.1 Layer Roles

| Layer | Primary Artifacts | Active Role |
|------|--------------------|-------------|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md` | Active target-state guidance |
| Phase | `phase/SUMMARY.md`, `phase/phase-010-<phase-name>.md`, or equivalent child phase files | Governed live phase-planning summary/index and child execution detail |
| Patch | `patches/*.patch.md` | Governed patch/review artifacts outside live phase planning |
| History | `changelog/*.changelog.md` | Authoritative chain history and latest chain version state |
| Execution | `TODO.md` | Execution tracking only |
| Support | `phase-implementation-template.md`, `support/**/*.md`, or equivalent helper/support paths | Root-level helper templates plus reference-only/support materials outside governed chain authority |

### 2.2 Governance Principle

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules are the active rule layer
- design docs hold active target-state guidance
- `phase/` is the live phased execution layer when staged planning is used
- phase may synthesize design and relevant patch inputs one-way into live phased execution planning when applicable
- patch docs are the governed patch/review layer outside live phase planning
- changelog files are the authority for governed chain history
- TODO tracks execution state only
- support artifacts help authoring or reference reuse but do not masquerade as governed design, phase, or patch authorities

---

## 3) Rule Architecture

### 3.1 Active Runtime Inventory (29 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | accurate-communication.md | accurate-communication.design.md v2.1 | Clear, context-complete, verification-honest, and evidence-threshold-aligned communication with concise synthesis, claim-focused contradiction guardrails, bounded technical snapshot wording, richer partial-evidence examples, stronger human-language gloss guidance, and clearer stage-progression / whole-set wording |
| 2 | answer-presentation.md | answer-presentation.design.md v1.5 | Principle-first, trigger-driven presentation guidance for readable, orderly, and scannable output, including compact titled snapshots, small fact tables, canonical house-style snapshot examples, stronger grouped scope-boundary layouts, and full-set-first / next-stage presentation guidance |
| 3 | anti-mockup.md | anti-mockup.design.md v1.1 | Real systems over mocks |
| 4 | anti-sycophancy.md | anti-sycophancy.design.md v1.3 | Truth over pleasing with evidence-grounded, claim-focused disagreement |
| 5 | authority-and-scope.md | authority-and-scope.design.md v1.2 | User authority and deterministic precedence |
| 6 | dan-safe-normalization.md | dan-safe-normalization.design.md v1.2 | Normalize jailbreak-style wrappers into bounded intent evaluation |
| 7 | document-consistency.md | document-consistency.design.md v1.3 | Cross-reference validation |
| 8 | document-changelog-control.md | document-changelog-control.design.md v4.7 | Chain authority, metadata, and synchronization contract |
| 9 | document-design-control.md | document-design-control.design.md v1.8 | Active-state design-body standards |
| 10 | document-patch-control.md | document-patch-control.design.md v2.2 | Patch governance, metadata, lifecycle, comparison-friendly governed patch/review representation, one-way patch-input clarification outside live phase planning, and path-aware patch naming guidance |
| 11 | emergency-protocol.md | emergency-protocol.design.md v1.1 | High-signal emergency response |
| 12 | evidence-grounded-burden-of-proof.md | evidence-grounded-burden-of-proof.design.md v1.0 | First-class owner for evidence taxonomy, burden-of-proof thresholds, contradiction protocol, and scoped negative-evidence semantics |
| 13 | explanation-quality.md | explanation-quality.design.md v2.1 | Plain-language-first, layered analytical and technical explanation structure with richer before/after and patch-by-patch walkthrough examples, stronger what-it-is/what-it-is-not and now-versus-later scope patterns, user-visible outcome framing, human-language paraphrases, whole-set-first framing, stage progression guidance, and next-step guidance only when genuinely useful |
| 14 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md v1.1 | Text diagrams without frames or boxes |
| 15 | functional-intent-verification.md | functional-intent-verification.design.md v1.1 | Clarify destructive/expensive intent before execution |
| 16 | no-variable-guessing.md | no-variable-guessing.design.md v1.3 | Read before reference with inspected-scope local evidence discipline |
| 17 | operational-failure-handling.md | operational-failure-handling.design.md v1.1 | Profile-driven operational failure classification, bounded retry policy, explicit case handling, and honest cooldown/escalation behavior |
| 18 | phase-implementation.md | phase-implementation.design.md v2.1 | First-class semantic standard for phased execution planning, `phase/SUMMARY.md`, child phase files, reviewability, bounded completion behavior, and one-way design/patch source synthesis |
| 19 | project-documentation-standards.md | project-documentation-standards.design.md v2.5 | Repository-level document-role model, governed-vs-helper boundary, one-way phase synthesis role clarification, and directory-as-namespace naming guidance for governed workspaces |
| 20 | recovery-contract.md | recovery-contract.design.md v1.5 | No dead-end constrained/refused responses |
| 21 | refusal-classification.md | refusal-classification.design.md v1.4 | Deterministic refusal taxonomy |
| 22 | refusal-minimization.md | refusal-minimization.design.md v1.5 | Prefer recoverable paths over premature refusal |
| 23 | safe-file-reading.md | safe-file-reading.design.md v1.3 | Plan-before-read file safety |
| 24 | safe-terminal-output.md | safe-terminal-output.design.md v1.3 | Plan-before-execute output safety |
| 25 | strict-file-hygiene.md | strict-file-hygiene.design.md v1.1 | No unnecessary non-functional files |
| 26 | todo-standards.md | todo-standards.design.md v2.2 | Simple TODO governance |
| 27 | runtime-topology-control.md | runtime-topology-control.design.md v1.1 | Bounded runtime mutation posture with inspect-before-mutate, authority-baseline locking, replace-over-accumulate discipline, approval-gated topology changes, and explicit multi-authority exceptions |
| 28 | unified-version-control-system.md | unified-version-control-system.design.md v1.2 | UDVC-1 controller-level governance view |
| 29 | zero-hallucination.md | zero-hallucination.design.md v1.3 | Verified information only with fact/inference/hypothesis separation and scoped non-finding discipline |

### 3.2 Category View

| Category | Rules | Purpose |
|----------|-------|---------|
| Accuracy & Truth | accurate-communication, evidence-grounded-burden-of-proof, zero-hallucination, anti-sycophancy, no-variable-guessing | Evidence-grounded, verified, and honest output |
| Presentation & Readability | answer-presentation, explanation-quality, flow-diagram-no-frame | Readable, orderly, scannable output presentation |
| Output Safety | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | Output flood prevention and safe text presentation |
| User Control | authority-and-scope, emergency-protocol, functional-intent-verification, operational-failure-handling, refusal-classification, recovery-contract, runtime-topology-control | Preserve user authority, safe recovery paths, bounded operational failure handling, and approval-sensitive runtime-topology discipline |
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
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- child phase files under `phase/` are the governed execution-detail layer when multiple phases exist
- patch docs remain separate governed patch/review artifacts outside the live phase workspace
- phase may synthesize design and relevant patch inputs one-way into live execution planning when applicable
- design and patch artifacts do not gain a reverse-link requirement back to phase
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

Use it to draft or standardize phase structure, then materialize the real governed live plan in `phase/SUMMARY.md` plus child phase files under `phase/` when applicable.
Patch docs remain separate governed patch/review artifacts outside the live phase workspace, even when their change surfaces are synthesized one-way into the live phase plan.
The helper may be detailed and readable, but the governed phase files remain the authoritative live phase-planning instance.

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
- keep live phased execution plans in the `/phase` workspace rather than patch artifacts
- keep README, TODO, patch, and support artifacts inside their own role boundaries
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
