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

### 1) Design-layer role
Governed design documents define active target behavior, contract, and implementation-relevant truth. They are not changelog/history dumps, but they are the right governed place for external-contract knowledge that later execution still depends on.

### 2) Active-state body rule
Design documents describe the current active target state.

They must not embed:
- detailed version-history tables
- audit snapshots
- remediation logs
- rollout-completion journals
- obsolete pending/activation instructions

Historical detail belongs in changelog files.

### 3) Doc-derived knowledge capture
When external documentation, API specifications, provider references, or comparable implementation authorities materially constrain implementation, the extracted implementation-relevant knowledge must be normalized into the governed design layer before or alongside continued multi-step work that relies on it.

Required guidance:
- do not rely on transient reading memory alone for contract-critical external requirements
- capture implementation-relevant truth in design before treating it as stable context for later execution slices
- capture extracted knowledge, not a copied prose dump of the source document
- if the source determines request parameters, authentication requirements, callback expectations, field semantics, state transitions, acceptance criteria, or integration constraints, make those constraints visible in design
- compact/session continuity limits are part of the reason this capture is required

### 4) Extraction specificity
A design capture derived from docs/specs should be specific enough that later implementation can answer:
- what the external source requires
- which implementation part is constrained
- what values, fields, parameters, flows, states, or acceptance criteria matter
- what should be sent, accepted, stored, validated, or rejected
- which details are active implementation truth versus source-side background that should not be carried forward

### 5) Design-changelog alignment
For governed chains, design version must align with:
- runtime rule `Current Version`
- runtime rule `Design` reference version
- changelog `Current Version`

### 6) Support-artifact boundary
Not every reference artifact belongs in governed design space. If a file is reference-only, prompt-only, media-only, or support-only, it should not remain in ambiguous `.design.md` form unless fully normalized as a governed design document.

Use clearly non-governed placement or naming for support-only artifacts.

### 7) Navigator rule
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
|---|---|
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
- [document-patch-control.md](document-patch-control.md) - patch may record change-surface consequences but does not replace design as target-state truth
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - continued execution should not outrun required external-knowledge capture

---

> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)
