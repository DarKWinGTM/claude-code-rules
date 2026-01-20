# Strict File Hygiene Design

## 0) Document Control

> **Parent Rule:** [strict-file-hygiene.md](strict-file-hygiene.md)
> **Current Version:** 1.2

---

## 1) เป้าหมาย (Goal)
- ลดไฟล์ขยะที่ AI สร้างเองโดยไม่จำเป็น
- รักษา Single Source of Truth ให้ชัดเจน
- ทำให้โครงสร้างโฟลเดอร์สะอาดและค้นหาได้ง่าย

---

## 2) ปัญหาที่ต้องแก้ (Problem)
- AI สร้างไฟล์ v2/summary/plan โดยไม่ได้ขอ
- เกิดความสับสนว่าไฟล์ไหนคือของจริง
- เพิ่มภาระในการดูแลและทำความสะอาด repo

---

## 3) ขอบเขต (Scope)

### 3.1 Allowed (อนุญาต)
- ไฟล์ที่จำเป็นต่อการทำงานของระบบ (code/config/runtime assets)
- เอกสารที่ user ขอแบบชัดเจน
- ไฟล์ชั่วคราวใน `/tmp` (ควรล้างเมื่อเสร็จ)

### 3.2 Not Allowed (ห้ามสร้าง)
- ไฟล์เวอร์ชันซ้ำ เช่น `file-v2`, `_final`, `plan-2026`
- checkpoint/summary/plan ที่ user ไม่ได้ขอ
- proactive docs เช่น README/PLAN/TODO โดยไม่ขอ
- ไฟล์ “สรุปงาน/สรุปการเปลี่ยนแปลง” ที่ไม่ได้ร้องขอ

---

## 4) หลักการ (Principles)
- **Code is Pollution**: สร้างไฟล์เท่าที่จำเป็นเท่านั้น
- **Single Source of Truth**: มีแหล่งอ้างอิงหลักเพียงหนึ่งเดียว
- **Temporary Everything**: แผน/สรุปอยู่ในแชท ไม่ใช่ไฟล์

---

## 5) Decision Flow (Mandatory)

```text
Need new file
  ↓
Is it functional code/config?
  → YES: allow (create or edit existing)
  ↓ NO
Did user explicitly ask for this doc/file?
  → YES: allow
  ↓ NO
Is it a duplicate/version/summary/plan?
  → YES: block
  ↓
Default: ask user first
```

---

## 6) Operational Rules

### 6.1 Existing File First
- ถ้ามีไฟล์เดิมอยู่แล้ว → **แก้ไฟล์เดิมเท่านั้น**
- ห้ามสร้างไฟล์ใหม่เพื่อเลี่ยงการแก้ของเดิม

### 6.2 Ask When Unclear
- ถ้าไม่ชัดว่าเอกสารจำเป็นจริงหรือไม่ → **ถามก่อนเสมอ**

### 6.3 Exception Handling
- ถ้าจำเป็นต้องสร้างไฟล์ใหม่ (เช่น standard doc ที่ user ขอ)
  - ระบุเหตุผลสั้น ๆ ก่อนสร้าง
  - ใช้ชื่อไฟล์ตามมาตรฐานโฟลเดอร์นั้น ๆ

---

## 7) Integration กับ Rule อื่น

| Related Rule | เหตุผลที่เกี่ยวข้อง | การประสานการทำงาน |
|---|---|---|
| document-consistency | ลดไฟล์ซ้ำซ้อน | อ้างอิงไฟล์หลักเท่านั้น |
| no-variable-guessing | ห้ามเดาความต้องการไฟล์ | ถ้าไม่ชัดให้ถาม |
| authority-and-scope | เคารพคำสั่งผู้ใช้ | ถ้าผู้ใช้สั่งให้สร้าง ให้ทำ |

---

## 8) Quality Metrics

| Metric | Target |
|---|---|
| Duplicate Files Created | 0 |
| Unrequested Docs | 0 |
| Clarification Asked When Unclear | 100% |

---

## 9) Anti-Patterns
- สร้าง `design-v2.md` แทนแก้ `design.md`
- สร้าง `PLAN.md` โดยไม่ได้ขอ
- สร้าง `SUMMARY.md` หลังจบงานโดยอัตโนมัติ

---

## 10) Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-01-20 | **Added Version History (Unified)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Migrated from old changelog format to Version History (Unified) | |
| | | Summary: Added version tracking for design document | |
| 1.2 | 2026-01-20 | **Added Document Control and Operational Rules** | LEGACY-001 |
| | | - เพิ่ม Document Control, Operational Rules, Integration และ Metrics | |
| 1.1.0 | 2026-01-19 | **Simplified analysis** | LEGACY-001 |
| | | - Simplified analysis, removed multi-hat/multi-agent | |
| 1.0.0 | 2026-01-19 | **Initial design** | LEGACY-001 |
| | | - Initial design |
