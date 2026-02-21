# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1) Goal (เป้าหมาย)

- กำหนดมาตรฐาน version tracking ที่ใช้งานได้จริงและตรวจสอบย้อนหลังได้
- แก้ความขัดแย้งระหว่าง “ทุกไฟล์ต้องมีตาราง” กับแนวทาง Navigator ของ design docs
- กำหนดกติกาเดียวสำหรับกรณีทั่วไป (OR compliance) และกรณีมีไฟล์คู่ design/changelog
- บังคับใช้ Session ID จริงเพื่อ trace กลับไปที่ session ได้

---

## 2) Scope (ขอบเขต)

### 2.1 Documents Covered

- Rules documents (`*.md`)
- Design documents (`*.design.md` หรือ `design.md`)
- Changelog documents (`*.changelog.md` หรือ `changelog.md`)

### 2.2 Problem This Design Resolves

- ความซ้ำซ้อนของประวัติระหว่าง design และ changelog
- ข้อกำหนดที่ตีกันเองระหว่าง table-only กับ navigator-only
- การใช้ Session ID แบบ placeholder ที่ตรวจสอบย้อนกลับไม่ได้

---

## 3) Core Principles (หลักการ)

1. **Traceability First**
   - ทุกเอกสารต้องมีเส้นทาง trace เวอร์ชันที่ชัดเจนเสมอ

2. **Flexible Compliance (OR)**
   - เอกสารผ่านเกณฑ์เมื่อมีอย่างน้อยหนึ่งข้อ:
     - (A) มี `Version History (Unified)` table ในไฟล์
     - (B) มีลิงก์ไปยัง authoritative changelog

3. **Pair Behavior is Explicit**
   - เมื่อมีทั้ง `design.md` และ `changelog.md` ในขอบเขตเดียวกัน ต้องใช้ separation แบบชัดเจน

4. **No Mock Session IDs**
   - ห้ามใช้ `<Session ID>`, `TBD`, หรือค่าจำลอง

5. **History Preservation**
   - ห้ามลบ/ทับ history เดิมโดยไม่บันทึกการเปลี่ยนแปลงใหม่

---

## 4) Core Requirements (ข้อกำหนดหลัก)

### 4.1 Traceable Version Path (Mandatory)

ทุกเอกสารต้องมี traceable version path แบบ OR:

- **Option A:** มี `Version History (Unified)` table ในเอกสารนั้น
- **Option B:** มี `> Full history: ...` ที่ชี้ไป changelog หลัก

### 4.2 Session ID Integrity

- Session ID ต้องเป็นค่าจริงจาก environment/session ปัจจุบัน
- รองรับรูปแบบ UUID (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) หรือ `SXXXX`
- ข้อมูล legacy ให้ใช้ `LEGACY-XXX` เฉพาะ entry ย้อนหลังเท่านั้น

### 4.3 History Preservation

- ห้ามลบ history เดิม
- หากแก้ความผิดพลาดของ history เดิม ให้เพิ่ม entry ใหม่เพื่ออธิบาย correction
- ทุก entry ต้องมี Date + Session ID

### 4.4 design.md <> changelog.md Pair Rule (Mandatory)

เมื่อมีทั้ง design/changelog คู่กันในขอบเขตเดียวกัน:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| **design.md** / `*.design.md` | Navigator link-only (`> Full history: ...`) | Full changelog sections, version table/entries ในไฟล์เดียวกัน |
| **changelog.md** / `*.changelog.md` | Detailed sections (UPPER) + `Version History (Unified)` table (LOWER) | มีแค่ detailed sections หรือมีแค่ table อย่างเดียว |

### 4.5 Navigator Definition

Navigator หมายถึง:

- ✅ มีเฉพาะลิงก์ไป authoritative changelog
- ❌ ไม่มีตาราง version history ในไฟล์ design
- ❌ ไม่มี version entries ในไฟล์ design

---

## 5) Format Standards (รูปแบบมาตรฐาน)

### 5.1 Full Changelog Format

```markdown
# Changelog - <Document Name>

> **Parent Document:** [<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <Real Session ID>

---

## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Real Session ID>

### Changes
- <Detailed change 1>
- <Detailed change 2>

### Summary
<One-line summary>

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[<Headline>](#version-xy)** | <Real Session ID> |
| | | Summary: <One-line summary> | |
```

### 5.2 Design Navigator Format

```markdown
---

> Full history: [changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

### 5.3 Non-Pair Documents (OR Compliance)

หากไม่มีไฟล์คู่ design/changelog:

- จะใช้ table-in-file หรือ link-only อย่างใดอย่างหนึ่งก็ได้
- แนะนำให้ใช้ table-in-file เมื่อเอกสารยังสั้นและแก้น้อย

---

## 6) File Organization Patterns

### Pattern 1: Simple (No subdirectories)

```text
./
├── design.md
├── changelog.md
└── src/
```

### Pattern 2: Mixed/Complete

```text
./
├── design/
│   └── *.design.md
├── changelog/
│   ├── changelog.md
│   └── *.changelog.md
└── src/
```

### Decision Rule

```text
Has design/ or changelog/ directory?
├─ YES → Pattern 2
└─ NO  → Pattern 1
```

---

## 7) Compliance Checklist

- [ ] เอกสารมี traceable path แบบ OR แล้ว
- [ ] Session IDs เป็นค่าจริง (ไม่ placeholder)
- [ ] หากเป็น design/changelog pair ใช้ separation ถูกต้อง
- [ ] changelog file มีทั้ง detailed sections + summary table
- [ ] ไม่มีการลบ history เดิม
- [ ] ลิงก์อ้างอิงทั้งหมดใช้งานได้จริง

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Traceable version path coverage | 100% |
| Session ID integrity | 100% real values |
| Pair-rule compliance | 100% when pair exists |
| History preservation | 100% |
| Cross-reference validity | 100% |

---

## 9) Related Documents

| Document | Purpose |
|----------|---------|
| [../document-changelog-control.md](../document-changelog-control.md) | Rule definition from this design |
| [../document-design-control.md](../document-design-control.md) | Design document format constraints |
| [../document-consistency.md](../document-consistency.md) | Cross-reference and consistency checks |

---

## 10) Implementation Notes

### 10.1 Common Pitfalls

- ใส่ตาราง version ใน design doc ทั้งที่มี changelog คู่แล้ว
- เขียน changelog แบบมีแค่ detailed sections โดยไม่มี summary table
- ใช้ placeholder Session ID
- แก้ history เก่าโดยไม่เพิ่ม correction entry ใหม่

### 10.2 Migration Guidance

- ถ้าไฟล์เดิมมี table ใน design doc และมี changelog คู่แล้ว → ย้าย full history ไป changelog แล้วเหลือ navigator link ใน design
- ถ้า changelog เดิมมีแค่รูปแบบเดียว (table หรือ detailed อย่างเดียว) → เติมอีกส่วนให้ครบทั้งสองส่วน

---

> Full history: [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md)
