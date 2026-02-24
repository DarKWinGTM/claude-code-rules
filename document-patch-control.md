# Document Patch Control

> **Current Version:** 1.2
> **Based on:** [document-patch-control.design.md](design/document-patch-control.design.md) v1.2
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)

---

## Rule Statement

**Core Principle: Patch documents must follow the same deterministic metadata and version-governance contract as other governed documents (UDVC-1).**

Patch documents describe transition execution from current state to target design state, while changelog remains version authority for patch history.

---

## Core Requirements

### 1) Naming and Location

- Patch filename format: `<context>.patch.md`
- Recommended location: `patches/`
- Do not use version suffixes in filenames

### 2) Mandatory Metadata

Each patch document must include:

- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history` link

Each patch changelog must include:

- `Parent Document`
- `Current Version`
- `Session`

### 3) Patch Content Structure

Patch documents must include, at minimum:

1. Context (current vs target)
2. Analysis (risk and dependencies)
3. Implementation plan (phased)
4. Verification criteria
5. Rollback approach

### 4) Session Integrity

- Active patch metadata must use real session IDs
- Placeholder markers are not allowed in active metadata
- `LEGACY-*` is allowed only for historical records when original session data is unavailable

### 5) Version Alignment

- Patch `Current Version` must align with patch changelog `Current Version`
- `Target Design` reference must resolve to existing design document/version
- Patch metadata synchronization follows governance order with final patch sync when affected

### 6) Synchronization Order

For governed updates involving patch metadata:

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (if affected)

---

## Compliance Checklist

- [ ] Filename uses `.patch.md` format
- [ ] Patch metadata fields are complete
- [ ] Patch changelog metadata fields are complete
- [ ] Session metadata is real (no placeholders)
- [ ] Patch version aligns with patch changelog version
- [ ] Target design reference resolves correctly
- [ ] Full-history links resolve correctly

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Patch metadata completeness | 100% |
| Active placeholder session markers | 0 |
| Patch ↔ changelog version alignment | 100% |
| Patch ↔ target design reference validity | 100% |
| Broken patch history links | 0 |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.6 | Version authority and metadata contract |
| [project-documentation-standards.md](project-documentation-standards.md) v1.7 | Project-level document governance |
| [todo-standards.md](todo-standards.md) v2.1 | Execution tracking alignment |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
