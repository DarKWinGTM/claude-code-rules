# RULES Unified Diagram Doctrine Design Spec

> **Status:** Revised design-only specification. This document supersedes the earlier fragmented companion assumption and becomes the active design basis for the current diagram-doctrine correction wave.
>
> **Core direction:** RULES diagrams should be treated as a Kroki-compatible visual lane that preserves whole-system coherence. `design/` remains textual target-state authority, while `diagram/` becomes the governed visual synthesis lane. Governed diagram source must stay Kroki-compatible, support all suitable formats, and diagram structure must not mirror design shards automatically.

## Checked basis

This revised design is grounded in the user's newer direction plus these checked local references:

- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/STRUCTURE.md` — checked global structure/unity surface
- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/TODO.md` — checked diagram-lane governance and historical normalization notes
- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/nodeclaw-main.design.md` — checked subject-level parent/index diagram authority
- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/nodeclaw-main/02-platform-architecture-flow.design.md` — checked integrated subject diagram slice
- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/data-store.design.md` — checked subject-level parent/index diagram authority
- `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/diagram/data-store/01-database-storage-mapping.design.md` — checked integrated subject diagram slice
- `/home/node/workplace/AWCLOUD/CLAUDE/.claude/rules/document-governance.md`
- `/home/node/workplace/AWCLOUD/CLAUDE/.claude/rules/document-integrity.md`
- `/home/node/workplace/AWCLOUD/CLAUDE/.claude/rules/phase-todo-artifact.md`

Observed doctrine from checked NodeClaw scope:
- a project-wide structure surface is useful
- subject diagrams can have their own chain authorities
- subject diagrams may split into child shards when the visual question really separates
- diagram parents stay as gateways/indexes when a chain is broad enough to split
- design truth remains outside generated preview output

---

## 1. Goal / problem statement

The revised goal is to define a **RULES unified diagram doctrine** that keeps diagrams useful as a whole-system visual explanation layer without letting them fragment simply because text design is sharded.

This doctrine must solve four problems:

1. `design/` needs prose/detail sharding for governance and change locality.
2. `diagram/` needs visual coherence and relationship integrity.
3. A one-to-one mirror between design shards and diagram shards creates visual fragmentation.
4. Tooling such as governed-docs must not drive the doctrine before the doctrine itself is settled.

The target outcome is:
- `design/` remains the textual authority lane
- `diagram/` becomes the governed Kroki-compatible visual synthesis lane
- governed diagram source supports all suitable formats, defined as Kroki-compatible + governance-suitable
- diagrams start unified first
- `diagram/STRUCTURE.md` becomes a bodyful whole-project detailed visual structure authority
- subject diagrams behave as zoom-in / decomposition views of the global structure
- diagram splitting happens only when visual complexity justifies it
- inline answer/phase-local text diagrams stay outside governed source truth unless explicitly promoted
- plugin/tooling support remains downstream of the doctrine, not upstream of it

---

## 2. Non-goals / boundaries

This wave is still design-first and intentionally excludes runtime/tooling implementation.

Non-goals:
- no new plugin implementation behavior in this spec
- no claim that old plugin P003 remains selected current truth
- no GitHub push/release claim from this design doc by itself
- no requirement that every RULES design chain must have a diagram
- no claim that one global diagram file is enough for every subject forever
- no preview/manifest/source-hash output becoming semantic authority
- no hidden auto-mutation path from tooling into source truth

Boundaries:
- diagrams may explain design truth, but they do not replace it
- changelog/phase/patch can track diagram work, but they do not own diagram meaning
- generated previews remain view-only support surfaces

---

## 3. Revised doctrine summary

### 3.1 Core principle

**Design text may shard for readability and governance, but diagram structure should optimize for visual coherence first, not for shard symmetry.**

### 3.2 Default posture

For any governed subject:
- create one integrated subject diagram first
- only split the diagram when the diagram itself becomes too complex
- do not split a diagram only because the text design has multiple shards

### 3.3 Global anchor

RULES should have one top-level visual entrypoint:
- `diagram/STRUCTURE.md`

This file should explain:
- the whole RULES repo shape in enough detail for diagram-first understanding
- major document families and their relationships
- authority boundaries between runtime rules, design, changelog, TODO, phase, patch, and diagram
- the highest-level architecture/flow picture needed to orient readers quickly
- the structural decomposition path that later subject diagrams zoom into rather than duplicate arbitrarily

### 3.4 Subject diagrams

Each major subject may have one subject-level diagram by default:
- `diagram/<subject>.design.md`

This file should represent the subject as a coherent whole, not as a small fragment tied to one text heading.

### 3.5 Split posture

If a subject diagram becomes too broad, it may evolve into:
- parent/index diagram authority: `diagram/<subject>.design.md`
- child visual shards: `diagram/<subject>/<NN>-<slice>.design.md`

But this is a later split posture, not the baseline starting posture.

---

## 4. Lane model and authority

### 4.1 `design/`

`design/` remains:
- textual target-state truth
- rationale / constraints / process-order authority
- semantic authority when diagram and text differ

### 4.2 `diagram/`

`diagram/` becomes:
- governed Kroki-compatible visual synthesis lane
- architecture/flow/relationship explanation layer
- a governed documentation lane in its own right, but not the owner of semantic truth over design

### 4.3 Kroki-compatible source contract

For governed diagram source:
- Kroki-compatible is mandatory, not optional
- the allowed breadth is all formats that are both Kroki-compatible and governance-suitable
- governance-suitable means text-source-governable, diff/review-friendly, semantically stable enough for source truth, and portable enough for repo-governed workflow
- inline answer/phase-local text diagrams do not enter this contract automatically

### 4.4 Tooling / plugin surfaces

Tooling such as governed-docs remains:
- downstream renderer/helper path that should obey the source contract
- preview/index helper
- scanner/review support
- drift reporter

Tooling is **not**:
- doctrine owner
- semantic owner
- approval owner
- source-of-truth replacement

### 4.5 Authority hierarchy

For this doctrine:
1. user-selected objective and current instruction
2. active RULES design truth in `design/`
3. active diagram source in `diagram/`
4. changelog/phase/patch as tracking/review surfaces only
5. governed-docs preview/manifest/report output as support-only surfaces

---

## 5. Artifact model

### 5.1 Required global surface

```text
diagram/
  STRUCTURE.md
```

Purpose:
- whole-project structure in enough detail for diagram-first understanding
- cross-family relationships
- authority and dependency boundaries across the repo
- orientation for new readers
- stable top-level visual entrypoint
- the global structure that subject diagrams later zoom into or decompose

### 5.2 Default subject surface

```text
diagram/
  <subject>.design.md
```

Purpose:
- one integrated Kroki-compatible diagram document for the subject
- a zoom-in / decomposition view of the global structure rather than a disconnected fragment
- enough explanatory notes to understand the picture without scattering meaning across too many tiny files

### 5.3 Optional split surface

```text
diagram/
  <subject>.design.md
  <subject>/
    00-document-control.design.md
    01-<visual-slice>.design.md
    02-<visual-slice>.design.md
```

This split is allowed only after a real split trigger is met.

### 5.4 Optional governance support surfaces

Allowed when the diagram lane is actively governed:
- `diagram/TODO.md`
- `diagram/changelog/`

Not implied by default:
- `diagram/phase/`
- `diagram/patch/`

Execution and review still belong to root `phase/` and `patch/` unless a later explicit doctrine selects otherwise.

---

## 6. Unity-first split rules

### 6.1 When a diagram should stay whole

Keep one integrated subject diagram when:
- the subject still answers one main visual question
- the diagram is readable as one whole
- splitting would force the reader to reconstruct the system mentally from several tiny pieces
- the split would merely mirror text headings instead of improving visual understanding

### 6.2 When a diagram may split

Split only when at least one of these becomes true:
- the diagram becomes visually crowded enough that readability drops materially
- there are clearly different visual questions, such as topology vs storage mapping vs request lifecycle
- the audience or review context genuinely differs by slice
- one visual slice changes independently enough that it deserves its own maintenance path

### 6.3 What is not enough reason to split

These are explicitly insufficient:
- the design text has many shards
- the text headings look neat when mirrored
- tooling would be easier to implement
- naming symmetry would look cleaner
- the diagram lane wants to behave exactly like the design lane

---

## 7. Parent/index versus body rules

### 7.1 Before split

`diagram/<subject>.design.md` should be a **bodyful integrated subject diagram**.

It should not start life as an empty index by default.

### 7.2 After split

When split is justified:
- `diagram/<subject>.design.md` becomes the parent/index gateway
- child files become the direct visual bodies
- the parent must explain why the split exists and link the active shard map

### 7.3 Global structure surface

`diagram/STRUCTURE.md` is different:
- it is expected to stay a direct bodyful whole-project detailed visual structure surface
- it should carry enough structural depth that readers can understand the project through the diagram-first view as much as practical
- it should not become a shallow link-only router unless the project reaches a much larger complexity class later

---

## 8. Relationship between design and diagram

The mapping rule is intentionally many-to-one where useful.

Examples:
- several design shards may map into one integrated subject diagram
- several subject diagrams may roll up into one `diagram/STRUCTURE.md`

This is the key difference from the earlier fragmented companion assumption.

Diagram design should answer:
- what belongs together visually
- what relationship the reader needs to see at once
- what whole picture would be lost if the content were broken apart too early

Text design should answer:
- what belongs together semantically
- what changes together
- what needs local written detail

The two lanes are related, but they are not obligated to shard in the same pattern.

---

## 9. Plugin/tooling implication model

Until the revised doctrine is approved and normalized into active RULES surfaces:
- plugin-first implementation should remain paused
- old fragmented companion assumptions should not remain active current-state claims

When tooling returns later, it should support this revised doctrine by:
- recognizing `diagram/STRUCTURE.md`
- recognizing integrated subject diagrams under `diagram/*.design.md`
- treating governed diagram source as mandatory Kroki-compatible
- supporting all formats that are both Kroki-compatible and governance-suitable
- supporting split child shards only when the diagram lane actually uses them
- keeping preview/manifest/report output non-authoritative
- reporting drift, not silently reshaping source doctrine

Tooling should not assume:
- every diagram lives in `design/**`
- every subject diagram is a companion shard
- every diagram split follows design shard boundaries

---

## 10. Migration / rollback posture

This doctrine implies a two-part correction posture.

### 10.1 Preserve as historical basis

Keep the earlier design/plan artifacts as historical context, but treat them as superseded by this revised doctrine where they conflict.

### 10.2 Withdraw fragmented active assumptions

Any active current-state claim that says or implies:
- diagrams must stay inside `design/**` as the only allowed source lane
- same-stem per-topic design companions are the baseline
- plugin P003 behavior is the active current model

should be rolled back or demoted before the revised doctrine is presented as implemented truth.

---

## 11. Future verification model

A future implementation wave should prove:

1. diagram lane surfaces exist and are governed correctly
2. `diagram/STRUCTURE.md` works as the top-level visual anchor
3. subject diagrams start integrated by default
4. split only happens with a real shard-opening basis
5. preview output remains support-only
6. design remains semantic truth
7. plugin/tooling does not reintroduce fragmented companion assumptions by default

---

## 12. Recommendation summary

Recommended active doctrine now:

- create a dedicated RULES `diagram/` lane
- require `diagram/STRUCTURE.md` as the top-level whole-project visual anchor
- make `diagram/<subject>.design.md` the default integrated subject diagram shape
- allow same-stem child shards only after visual complexity justifies the split
- keep `design/` as textual target-state authority
- keep tooling/plugin behavior downstream of the doctrine
- withdraw plugin-first fragmented companion assumptions before re-entering implementation

Final doctrine sentence:

**RULES diagrams are a visual lane of their own: they synthesize design truth into a coherent whole, start unified by default, and split only when visual complexity genuinely requires it.**
