# Document Design Control

> **Current Version:** 1.10
> **Design:** [design/document-design-control.design.md](design/document-design-control.design.md) v1.10
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)

---

## Rule Statement

**Core Principle: Governed design documents should preserve the current implementation-relevant target-state truth, stay active blueprint authority rather than completed-work `done/` surfaces, and normalize implementation-relevant external-doc/spec/provider knowledge before or alongside continued multi-step work that depends on it.**

---

## Core Requirements

### Design-layer role and active body
Governed design documents define current target behavior, contract, and implementation-relevant truth, including external-contract knowledge later execution still depends on. They are not changelog/history dumps, completed-work records, audit snapshots, remediation logs, rollout journals, obsolete activation notes, or detailed version-history tables.
Active design bodies should describe what the system should be now or next target-state, not how every prior wave got there. If historical detail is still useful for audit, rollback, or provenance, keep it reachable through changelog governance rather than embedding it as active blueprint content.

Historical explanation belongs in changelog surfaces, including `changelog/done/` when inactive history separation is needed. `design/` remains active blueprint authority and has no default `design/done`; active target truth stays in current design files until superseded or removed from target state. Retained legacy snapshots must be labeled historical/reference-only and kept outside active design authority.

### Doc-derived knowledge capture
When external docs, API specs, provider references, or comparable authorities materially constrain implementation, normalize the extracted implementation truth into governed design before or alongside multi-step work that relies on it. Capture requirements, not copied prose, and do not rely on transient reading memory for contract-critical requirements.

A useful capture should make later implementation able to answer:
- what the external source requires and which implementation part is constrained
- what values, fields, parameters, flows, states, auth/callback rules, or acceptance criteria matter
- what should be sent, accepted, stored, validated, rejected, or kept out of active target truth
- which details are source-side background rather than implementation truth to carry forward

### Alignment and support boundary
For governed chains, design version must align with the runtime rule `Current Version`, runtime rule `Design` reference version, and changelog `Current Version`. Design alignment is target-state alignment, not permission to duplicate changelog history inside the design body.
Reference-only, prompt-only, media-only, or support-only artifacts should not remain ambiguous `.design.md` files unless fully normalized as governed design; use clearly non-governed placement/naming instead. This prevents support artifacts from masquerading as active target-state authority.
When a paired changelog exists, design navigation is limited to `Full history`; do not embed detailed changelog sections or duplicate historical summaries in the active body.

---

## Verification Checklist

- [ ] Governed design naming is used only for true governed design documents, with complete metadata and resolving links.
- [ ] Design body is active-state only; historical detail goes to changelog/`changelog/done`, not default `design/done`.
- [ ] External-doc/spec-derived implementation truth is normalized into design when later work depends on it.
- [ ] Rule/design/changelog versions align where applicable.
- [ ] Support-only artifacts are not left in ambiguous governed-looking design form.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Active-state design body, navigator, and version alignment | 100% |
| External-doc-derived implementation truth captured when material | High |
| Ambiguous governed-looking support artifacts or broken links | 0 |
| Stale history or default `design/done` usage in active blueprint docs | 0 critical cases |

---

## Integration

Related documents:
- [document-changelog-control.md](document-changelog-control.md) - version authority and metadata contract
- [project-documentation-standards.md](project-documentation-standards.md) - repository role boundaries, governed document set, and completed documentation surface model
- [phase-implementation.md](phase-implementation.md) - phased execution should reuse normalized design truth rather than transient doc-reading memory
- [document-patch-control.md](document-patch-control.md) - patch may record change-surface consequences but does not replace design as target-state truth
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - continued execution should not outrun required external-knowledge capture

---

> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)
