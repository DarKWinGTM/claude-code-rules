# Document Design Control

> **Current Version:** 1.9
> **Design:** [design/document-design-control.design.md](design/document-design-control.design.md) v1.9
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)

---

## Rule Statement

**Core Principle: Governed design documents should preserve the current implementation-relevant target-state truth, and when external documentation, API specifications, provider references, or comparable external implementation authorities materially constrain the build, the extracted implementation-relevant knowledge must be normalized into the design layer before or alongside continued multi-step work that depends on it.**

---

## Core Requirements

### 1) Design-Layer Role

Governed design documents define the active target behavior, contract, and implementation-relevant truth for the project.
They are not changelog/history dumps, but they are the correct governed place to preserve external-contract knowledge that later execution still depends on.

### 2) Active-State Body Rule

Design documents describe the current active target state.
They must not embed:
- detailed version-history tables
- audit snapshots
- remediation logs
- rollout-completion journals
- obsolete pending/activation instructions

Historical detail belongs in changelog files.

### 3) Doc-Derived Knowledge Capture Rule

When external documentation, API specifications, provider references, or comparable implementation authorities materially constrain the implementation, the implementation-relevant extracted knowledge must be normalized into the governed design layer before or alongside continued multi-step work that relies on it.

Required guidance:
- do not rely on transient reading memory alone for contract-critical external requirements
- capture the implementation-relevant truth in design before treating it as stable working context for later execution slices
- capture extracted knowledge, not a copied prose dump of the source document
- if the external source materially determines request parameters, authentication requirements, callback expectations, field semantics, state transitions, acceptance criteria, or integration constraints, those constraints should be made visible in design
- compact/session continuity limits are part of the reason this capture is required; the governed design layer should preserve reusable implementation truth so later execution does not depend on re-reading the same source unnecessarily

### 4) Extraction Specificity Rule

A design capture derived from docs/specs should be specific enough that later implementation can answer:
- what the external source requires
- which part of the implementation is constrained by that requirement
- what values/fields/parameters/flows matter
- what should be sent, accepted, stored, validated, or rejected because of that requirement
- which details are active implementation truth versus source-side background detail that does not need to be carried forward

### 5) Design-Changelog Alignment Rule

For governed chains, design version must align with:
- runtime rule `Current Version`
- runtime rule `Design` reference version
- changelog `Current Version`

### 6) Support-Artifact Boundary

Not every reference artifact belongs in governed design space.
If a file is reference-only, prompt-only, media-only, or support-only, it should not remain in an ambiguous `.design.md` state unless it is fully normalized as a governed design document.

Use clearly non-governed placement or naming for support-only artifacts.

### 7) Navigator Rule

When a paired changelog exists, design documents:
- keep version-history navigation limited to `Full history`
- do not embed detailed changelog sections
- do not duplicate historical summaries inside the active body

---

## Verification Checklist

- [ ] File uses governed design naming only when it is truly a governed design document
- [ ] Required metadata fields are complete
- [ ] Design body is active-state only
- [ ] Historical detail is delegated to changelog
- [ ] External-doc/spec-derived implementation truth is captured in design when later work still depends on it
- [ ] Captured knowledge is normalized and implementation-relevant rather than copied source prose
- [ ] Rule/design/changelog versions are aligned where applicable
- [ ] Links resolve correctly

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Active-state-only design-body compliance | 100% |
| Navigator compliance in paired design docs | 100% |
| External-doc-derived implementation truth captured when material | High |
| Ambiguous governed-looking support artifacts | 0 |
| Broken design/changelog links | 0 |
| Stale historical guidance inside active design bodies | 0 critical cases |

---

## Integration

Related documents:
- [document-changelog-control.md](document-changelog-control.md) - version authority and metadata contract
- [project-documentation-standards.md](project-documentation-standards.md) - repository role boundaries and governed document set
- [phase-implementation.md](phase-implementation.md) - phased execution should reuse normalized design truth rather than transient doc-reading memory
- [document-patch-control.md](document-patch-control.md) - patch artifacts may record change-surface consequences of external requirements but do not replace design as the target-state truth layer
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - continued execution should not outrun required external-knowledge capture when later work still depends on that knowledge

---

> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)
