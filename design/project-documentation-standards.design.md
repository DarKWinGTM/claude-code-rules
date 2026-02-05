# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1) Goal (เป้าหมาย)

- กำหนดมาตรฐานเอกสารสำหรับทุก project ให้มีความสม่ำเสมอกัน
- ระบุว่าเมื่อไหรต้องใช้ rule ใดในการสร้างเอกสาร
- ทำให้ทุก project มีเอกสารครบถ้วนตามมาตรฐานที่กำหนด
- ลดความสับสนในการเขียนและจัดการเอกสาร

---

## 2) Scope (ขอบเขต)

### 2.1 Projects Covered

- ทุก project ใหม่ที่เริ่มต้น
- ทุก project ที่มีการอัปเดต design หรือ specification
- ทุก project ที่ต้องการ version tracking

### 2.2 Standards Defined

- ระบุว่าเอกสารใดบ้างต้องมีในแต่ละ project
- กำหนดว่าเมื่อไหรต้องใช้ rule ใด
- ระบุ compliance checklist สำหรับตรวจสอบ
- กำหนด onboarding process สำหรับ project ใหม่

---

## 3) Required Documents (เอกสารที่จำเป็นต้องมี)

### 3.1 Core Documents (เอกสารหลัก)

| Document | Required When | Purpose | Rule Reference |
|----------|---------------|---------|----------------|
| **README.md** | ทุก project | Project overview, quick start, installation | Standard practice |
| **design.md** | เมื่อมี design specs | Architecture, standards, specifications | [document-design-control.md](../document-design-control.md) v1.1 |
| **changelog.md** | เมื่อต้อง version tracking | Version history, changes tracking | [document-changelog-control.md](../document-changelog-control.md) v4.3 |
| **TODO.md** | เมื่อมี tasks | Task tracking, progress management | [todo-standards.design.md](todo-standards.design.md) v1.0 |
| **patch.md** | เมื่อต้องทำ Monkey Patch | Transition plan, complex state changes | [document-patch-control.md](../document-patch-control.md) v1.0 |

### 3.2 Decision Tree (ต้นไม้ตัดสินใจ)

```
Project เริ่มต้น?
  ↓ YES
สร้าง README.md (overview + quick start)
  ↓
มี design/specifications?
  ↓ YES → สร้าง design.md (ตาม document-design-control.md)
  ↓ NO
ต้องการ track versions?
  ↓ YES → สร้าง changelog.md (ตาม document-changelog-control.md)
  ↓ NO
มี tasks ที่ต้องทำ?
  ↓ YES → สร้าง TODO.md (ตาม todo-standards.design.md)
  ↓ NO
ต้องทำ Monkey Patch หรือ Complex Migration?
  ↓ YES → สร้าง *.patch.md (ตาม document-patch-control.md)
  ↓ NO
Project พร้อมใช้งาน
```

---

## 4) Document Rules Applied (กฎเกณฑ์ที่ใช้)

### 4.1 Rule Integration

เมื่อสร้างเอกสารแต่ละประเภท ต้องปฏิบัติตาม rule ที่เกี่ยวข้อง:

| Rule | เมื่อไหรต้องใช้ | ข้อกำหนดสำคัญ |
|------|------------------|-------------------|
| **document-design-control.md** | สร้าง .design.md files | - ใช้ suffix `.design.md`<br>- อยู่ใน `./design/`<br>- Navigator format |
| **document-changelog-control.md** | สร้าง version tracking | - Version History (Unified) table<br>- Real Session IDs<br>- ไม่ใช้ placeholders |
| **todo-standards.design.md** | สร้าง TODO.md | - P0-P3 priorities<br>- timestamps (Created/Started/Completed)<br>- Completed/In Progress/Pending sections |
| **document-patch-control.md** | สร้าง .patch.md files | - Format `.patch.md`<br>- Structure (5 sections)<br>- Lifecycle states |

### 4.2 Cross-Reference Standards

เอกสารทั้งหมดต้องมีการเชื่อมโยงกัน:

```
project-documentation-standards.md (This rule)
  ↓ ระบุว่าใช้ rule ไหนเมื่อไหร

document-design-control.md
  ↓ กำหนดรูปแบบ .design.md

document-changelog-control.md
  ↓ กำหนดรูปแบบ version tracking

todo-standards.design.md
  ↓ กำหนดรูปแบบ TODO/tasks

document-patch-control.md
  ↓ กำหนดรูปแบบ Patch/Migration
```

### 4.3 Versioning Authority (อำนาจการกำหนดเวอร์ชัน)

- **Single Source of Truth:** `changelog.md` คือแหล่งอ้างอิงเดียวของ Version Number
- **Synchronization Rule:**
  - เมื่อแก้ไข Design document → ต้องอัพเดท Changelog เสมอ
  - เลข Version ใน Header ของเอกสาร (Design/Rule) ต้องตรงกับ Changelog ล่าสุด
  - ห้ามอัพเดท Design โดยไม่อัพเดท Changelog
  - ห้ามใช้ Version Number ที่ไม่ตรงกับ Changelog

---

## 5) Project Start Checklist (checklist เริ่ม project)

### 5.1 Before Starting (ก่อนเริ่ม)

- [ ] **Determine project type** - Simple vs Complex vs Design-heavy
- [ ] **Identify required documents** - ใช้ decision tree ใน Section 3.2
- [ ] **Plan documentation structure** - จำเป็นไฟล์เดียว หรือหลายไฟล์
- [ ] **Set up directory structure** - `./design/`, `./changelog/`, `./patches/` ถ้าจำเป็น

### 5.2 During Setup (ระหว่าง setup)

- [ ] **Create README.md** - Project overview, quick start
- [ ] **If design needed:** Create `design.md` following document-design-control.md
  - [ ] File named `*.design.md`
  - [ ] Located in `./design/`
  - [ ] Has Document Control section
  - [ ] Has changelog link at end
- [ ] **If version tracking needed:** Create `changelog.md` following document-changelog-control.md
  - [ ] Version History (Unified) format
  - [ ] Real Session IDs (no placeholders)
  - [ ] Detailed sections (UPPER) + Table (LOWER)
- [ ] **If tasks needed:** Create `TODO.md` following todo-standards.design.md
  - [ ] Priority levels (P0-P3)
  - [ ] Timestamps (Created/Started/Completed)
  - [ ] Status sections (Completed/In Progress/Pending)
- [ ] **If patch needed:** Create `*.patch.md` following document-patch-control.md
  - [ ] Extension `.patch.md`
  - [ ] 5 mandatory sections (Context, Analysis, Plan, etc.)

### 5.3 Verification (ตรวจสอบ)

- [ ] **All Session IDs are real UUIDs** - No `<Session ID>`, `TBD`, or placeholders
- [ ] **All cross-references work** - Test all links
- [ ] **Format compliance** - All documents follow their respective rules
- [ ] **No duplicate files** - Follow strict-file-hygiene.md

---

## 6) Onboarding Integration (การเชื่อมโยงกับ onboarding)

### 6.1 New Projects

Projects ใหม่ต้อง acknowledge:

1. **Documentation Standards Read** ✅
   - อ่านและเข้าใจ project-documentation-standards.md
   - เข้าใจว่าต้องมีเอกสารอะไรบ้าง

2. **Rule Compliance** ✅
   - รู้จักว่าจะใช้ rule ไหนเมื่อไหร
   - สามารถดูดอกจาก checklist ใน Section 5

3. **Format Standards** ✅
   - เข้าใจรูปแบบเอกสารแต่ละประเภท
   - สามารถดูตัวอย่างจาก rule ที่เกี่ยวข้อง

### 6.2 Project Template (optional)

สามารถสร้าง project template ที่มี:

```
project-template/
├── README.md (template)
├── design/
│   └── .gitkeep
├── changelog/
│   └── .gitkeep
└── .claude/
    └── rules/
        └── project-documentation-standards.md
```

---

## 7) Compliance Metrics (ตัวชี้วัดความสอดคล้อง)

### 7.1 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Required documents presence | 100% | Checklist ใน Section 5 |
| Rule compliance | 100% | Follow respective rules |
| Session ID accuracy | 100% | Real UUIDs only |
| Cross-reference validity | 100% | All links work |
| Format consistency | 100% | Follow document-design-control.md |

### 7.2 Compliance Levels

**Minimum Compliance (ต่ำสุด):**
- README.md มีในทุก project
- เอกสารอื่นๆ ตามที่ project ต้องการ

**Recommended Compliance (แนะนำ):**
- ทุกเอกสาร follow format ตาม rule ที่เกี่ยวข้อง
- มี changelog.md สำหรับ version tracking
- มี TODO.md สำหรับ task tracking
- ทุก Session ID เป็น real UUID

---

## 8) Examples (ตัวอย่าง)

### 8.1 Simple Project (project เล็ก)

```
simple-project/
├── README.md           # Project overview, quick start
└── src/
```

**ใช้เฉพาะ:** README.md

### 8.2 Standard Project (project มาตรฐาน)

```
standard-project/
├── README.md           # Project overview, quick start
├── design.md           # Architecture, specifications
├── TODO.md             # Task tracking
└── src/
```

**ใช้:** README.md + design.md + TODO.md

### 8.3 Complex Project (project ซับซ้อน)

```
complex-project/
├── README.md
├── design/
│   ├── design.md       # Master design
│   ├── api.design.md   # API design
│   └── database.design.md  # Database design
├── changelog/
│   ├── changelog.md    # Master changelog
│   └── api.changelog.md    # API changelog
├── patches/            # (Optional) Patch docs
│   └── db-migration.patch.md
├── TODO.md
└── src/
```

**ใช้:** README.md + multiple design.md + changelog.md + TODO.md

---

## 9) Related Documents (เอกสารที่เกี่ยวข้อง)

| Document | Purpose | Link |
|----------|---------|------|
| **document-design-control.md** | Design document standards | [../document-design-control.md](../document-design-control.md) v1.1 |
| **document-changelog-control.md** | Version tracking system | [../document-changelog-control.md](../document-changelog-control.md) v4.3 |
| **todo-standards.design.md** | TODO/task standards | [todo-standards.design.md](todo-standards.design.md) v1.0 |
| **document-patch-control.md** | Patch document standards | [../document-patch-control.md](../document-patch-control.md) v1.0 |
| **strict-file-hygiene.md** | No unrequested files | [../strict-file-hygiene.md](../strict-file-hygiene.md) v1.2 |

---

## 10) Implementation Notes (บันทึกการนำไปใช้)

### 10.1 When to Apply

**Project Start:**
- ใช้ checklist ใน Section 5 เพื่อกำหนดเอกสารที่ต้องการ

**Document Creation:**
- ใช้ rule ที่เกี่ยวข้องกับเอกสารที่สร้าง

**Updates:**
- เมื่อมีการเปลี่ยนแปลง ใช้ changelog.md ตาม document-changelog-control.md

### 10.2 Common Pitfalls (ข้อผิดพลาดที่พบบ่อย)

- ❌ ไม่สร้าง README.md - ทุก project ควรมี
- ❌ ใช้ placeholder Session IDs - ต้องใช้ real UUID
- ❌ ไม่ follow format ตาม rule - ทำให้เอกสารไม่สม่ำเสมอ
- ❌ สร้างไฟล์ที่ไม่จำเป็น - violate strict-file-hygiene.md

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-02-01 | **[Added Patches Directory Support](changelog/project-documentation-standards.changelog.md#version-12)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Added ./patches/ directory support for complex projects | |
| 1.1 | 2026-02-01 | **[Added Document Patch Control Integration](changelog/project-documentation-standards.changelog.md#version-11)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Integrated Document Patch Control standards | |
| 1.0 | 2026-01-21 | **[Initial Version](changelog/project-documentation-standards.changelog.md#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Initial release of Project Documentation Standards | |

> Full history: [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
