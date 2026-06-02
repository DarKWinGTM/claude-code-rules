# RULES Diagram Infrastructure Doctrine

> **Status:** Adopted target-state doctrine basis for the current RULES diagram infrastructure refinement
> **Scope:** `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
> **Basis:** extends the released diagram-lane model from `v10.37 / P129`
> **Observed pattern source:** NodeClaw-platform governed docs structure

---

## 1) Goal

Turn the current good diagram/doc pattern into explicit RULES doctrine.

พูดง่าย ๆ: จากเดิมที่ `diagram/` และ `diagram/STRUCTURE.md` เป็นของที่ใช้งานได้ดีอยู่แล้ว ให้ RULES ยกระดับสิ่งนี้เป็น **required governed-docs infrastructure** แบบชัดเจน โดยใน RULES diagram docs ต้องอยู่ใต้ `diagram/` เท่านั้น และต้องมี `diagram/STRUCTURE.md` เป็น root entrypoint เสมอ.

The doctrine should preserve three things together:
- `design/**` remains semantic / target-state authority
- `diagram/**` becomes the required visual/mapping/routing document family
- compact parent + `history/` + `done/` governance remains preservation infrastructure rather than cleanup

---

## 2) Selected design direction

### 2.1 Required diagram family

For governed project documentation in RULES:
- diagram docs are not an optional companion layer anymore
- the diagram family lives under `diagram/` only
- `diagram/STRUCTURE.md` is mandatory
- deeper diagram docs, when needed, also stay under `diagram/`

Not allowed as steady-state diagram authority:
- diagram authority split across `design/`, `phase/`, `TODO`, or ad hoc root markdown files
- plugin/preview/manifest outputs treated as the diagram source of truth
- inline answer/phase-local diagrams silently becoming repository diagram authority

### 2.2 Authority boundary

The doctrine must stay explicit that:
- `design/**` owns semantic truth and target-state meaning
- `diagram/**` owns visual structure, topology, mapping, and navigation
- if text design and diagram conflict, `design/**` wins semantically
- diagram docs visualize, map, and route existing doctrine; they do not replace it

---

## 3) `diagram/STRUCTURE.md` target role

`diagram/STRUCTURE.md` is the required whole-project diagram-side entrypoint.

It should be defined as all of the following at once:

### 3.1 Concept map
It names the main concepts of the project and shows how they relate at a whole-project level.

### 3.2 Source / topology map
It maps source-file zones, code-path families, folders, directories, and major subsystems so a reader can see where the important parts of the project live.

### 3.3 Relationship hub
It links the diagram family together and shows which deeper diagrams relate to which other diagrams.

Important: it does **not** need to inline the full detail of every child diagram. Its job is to show:
- what each related diagram covers
- how it connects to other diagrams
- when the reader should go there next

### 3.4 Boundary ledger
It should clearly state what it owns and what it does not own:
- diagram-side structure / topology / visual routing = yes
- semantic target-state truth = no, that remains `design/**`
- changelog history = no
- phase execution detail = no
- TODO ownership = no

### 3.5 Active parent surface
It must stay compact enough to function as an active entrypoint rather than becoming a history dump or a giant catalog of copied child-diagram content.

---

## 4) Required content responsibilities for `STRUCTURE.md`

The doctrine should require `diagram/STRUCTURE.md` to cover these categories:

1. **Purpose / scope**
   - what this file is for
   - what it is not for

2. **Project concept inventory**
   - main concepts/modules/capsules of the project

3. **Folder / code-path mapping**
   - where the major concepts live in the repo
   - enough mapping to orient a maintainer quickly

4. **Topology / relationship diagram**
   - a diagram that shows how the major parts relate

5. **Diagram-to-diagram relationship map**
   - which detailed diagrams exist
   - which concept or subsystem each one covers
   - which diagrams depend on or relate to which others

6. **Authority / boundary section**
   - design vs diagram vs changelog vs phase vs TODO vs patch ownership

7. **Navigation guidance**
   - where to go next for deeper diagram detail

---

## 5) Child diagram doctrine

Detailed diagrams may exist under `diagram/`, but they should follow these rules:
- they are children of the same diagram family
- they are discoverable from `diagram/STRUCTURE.md`
- they are opened because a concept, subsystem, or relationship view actually needs deeper visual treatment
- they should not exist only because text design shards exist

Good reasons to add child diagrams:
- a subsystem has enough internal structure that the root structure map would become noisy
- a relationship domain needs a focused view of its own
- a separate visual question exists that deserves a bounded diagram

Bad reasons to add child diagrams:
- symmetry with text files alone
- plugin/tooling convenience alone
- turning every heading into a diagram file
- using child diagrams to avoid keeping `STRUCTURE.md` current

---

## 6) History / done infrastructure pattern

The observed NodeClaw pattern should be generalized into doctrine.

### 6.1 Active parent stays current
Active parent files stay compact and navigable.

### 6.2 `history/` preserves prior active state
`history/` keeps prior snapshots, rollover state, and audit/provenance detail.

### 6.3 `done/` preserves completed detail
`done/` keeps completed closeout detail that should remain reachable but not active by default.

### 6.4 Preservation, not cleanup
Moving material into `history/` or `done/` is preservation work, not deletion authority.

If diagram infrastructure later needs its own `diagram/history/` or `diagram/done/` surfaces, they should follow the same principle:
- active parent for navigation
- history for prior state / audit
- done for completed evidence

---

## 7) Adopted doctrine changes in RULES

This doctrine now makes these changes explicit:

- `diagram/` is a required governed-docs family for RULES
- `diagram/STRUCTURE.md` is mandatory and root-scoped
- diagram docs are `diagram/`-scoped only
- `STRUCTURE.md` must own concept map + repo mapping + topology + diagram navigation responsibilities
- child diagrams remain subordinate members of the same family
- NodeClaw-style compact-parent plus `history/` / `done/` preservation pattern becomes the selected infrastructure model
- design authority remains primary for semantic truth

---

## 8) Non-goals

This doctrine wave should **not** do these things:
- make diagram docs semantic authority over design
- require every possible subsystem to immediately have its own diagram file
- turn `STRUCTURE.md` into a full implementation spec
- let plugin previews/manifests become diagram source truth
- make `history/` / `done/` into cleanup disposal paths
- reopen unrelated plugin or rendering work as part of the doctrine definition alone

---

## 9) Resulting target posture

Under this doctrine, a governed project should read like this:
- `design/**` tells you what the system means
- `diagram/STRUCTURE.md` tells you how the project is shaped
- child diagrams tell you where to zoom in
- `history/` and `done/` preserve the past without polluting the active parent

That is the infrastructure pattern we want RULES to state explicitly.
