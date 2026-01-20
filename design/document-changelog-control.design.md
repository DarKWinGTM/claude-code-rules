# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.3
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

---

## 1) เป้าหมาย (Goal)
- ทำให้เอกสารทุกประเภทมีการควบคุมเวอร์ชันอย่างเป็นระบบ
- ป้องกันความสับสนระหว่าง "changelog แบบละเอียด" และ "สรุปเวอร์ชันแบบย่อ"
- สร้างรูปแบบเดียวที่ใช้ได้กับทั้งไฟล์ changelog และไฟล์เอกสารทั่วไป (เช่น design)

---

## 2) ขอบเขต (Scope)

### 2.1 Single Format Strategy (Universal)
- **ทุกเอกสารใช้รูปแบบเดียวกัน** - Version History (Unified)
- ไม่แยกแบบระหว่าง changelog กับ design doc
- เรียบง่าย สม่ำเสมอ และใช้งานได้จริง

### 2.2 Location
- **สำหรับไฟล์ changelog หลัก**: อยู่ใน `design/changelog/`
- **สำหรับไฟล์ design/เอกสารทั่วไป**: อยู่ที่ส่วนท้ายของไฟล์ (Section สุดท้าย)

---

## 3) หลักการ (Principles)
- **Single Source of Truth**: รายละเอียดแบบเต็มอยู่ที่ไฟล์ changelog หลัก (ถ้ามี)
- **Flexible Compliance**: เลือกใช้ได้ 2 รูปแบบ แต่ต้องมีอย่างน้อย 1 รูปแบบเสมอ
- **Lightweight Footer**: เอกสารทั่วไปมีเฉพาะส่วนย่อและลิงก์ (ถ้ามีไฟล์หลัก)
- **Traceability**: ทุกเวอร์ชันต้องตรวจสอบย้อนกลับได้
- **No Mock Data**: ห้ามใช้ Session ID หรือข้อมูลจำลอง (ต้องใช้ค่าจริงจาก Environment)

### 3.1 Three Design Properties (Mandatory)
1) **Security**: ความน่าเชื่อถือ/ตรวจสอบย้อนกลับได้ (traceability, integrity)
2) **Flexibility**: รองรับรูปแบบหลายแบบ และไม่ล็อก naming เดียว
3) **Operational**: มีกลไกตัดสินใจและ migration ที่ใช้งานได้จริง

---

## 4) Format Standards (Single Universal Format)

### 4.0 Core Requirement (Mandatory)
- **ทุกเอกสารต้องมี Version History** - ใช้รูปแบบเดียวกันหมด
- **Session ID ต้องเป็นค่าจริง** จาก Environment (ไม่ใช้ placeholder หรือ mock)

### 4.1 Universal Format: Version History (Unified)

**ใช้สำหรับทุกเอกสาร** - ไม่ว่าจะเป็น changelog หลัก หรือ design doc ทั่วไป

```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **<Headline>** | <Claude Session ID> |
| | | - <Change 1> | |
| | | - <Change 2> | |
| | | Summary: <One-line summary> | |
| X.X | YYYY-MM-DD | **<Headline>** | <Claude Session ID> |
| | | - <Change 1> | |
| | | - <Change 2> | |
| | | Summary: <One-line summary> | |

> Full history: [changelog.<doc>.md](changelog/changelog.<doc>.md)
```

**หมายเหตุ:**
- **Session ID**: ต้องเป็นค่าจริงจาก Environment (เช่น `S1589`)
- **Full history link**: ใช้เมื่อมี changelog หลักแยกต่างหาก ถ้าไม่มีให้ลบออก

### 4.2 Location Strategy
- **ไฟล์ใน `design/changelog/`**: ทั้งไฟล์เป็น Version History (เริ่มต้นด้วย header ที่เหมาะสม)
- **ไฟล์ design/เอกสารทั่วไป**: Version History อยู่ที่ Section สุดท้ายของไฟล์

---

## 5) Implementation Rules

### 5.1 When to Update
- ทุกครั้งที่เปลี่ยนสาระสำคัญของเอกสาร ต้องเพิ่มเวอร์ชันและลงบันทึก
- ห้ามแก้ไขประวัติเก่า ยกเว้นแก้คำผิดหรือความชัดเจน (ต้องระบุในเวอร์ชันใหม่)
- **Critical**: ห้ามลบหรือตัดทิ้น Version History เดิม (ต้อง preserve ทั้งหมด)

### 5.2 Minimum Compliance (Mandatory)
- ต้องมี **อย่างน้อย 1 รูปแบบ** ที่บันทึกเวอร์ชัน/การเปลี่ยนแปลงได้เสมอ
- ทุก entry ต้องระบุ **Date** ชัดเจน (YYYY-MM-DD หรือมีเวลา)
- Footer Short ต้องมี **Session ID** จริงจาก Environment เพื่อ trace กลับไปยัง Claude Code session
- ถ้ามี changelog หลัก ให้ลิงก์อ้างอิงจากเอกสารทั่วไป

### 5.2.1 design.md <> changelog.md Relationship (Mandatory)

> **Critical Rule:** เมื่อมีทั้ง `design.md` และ `changelog.md` พร้อมกัน ใน project เดียวกัน

**หลักการสำคัญ:**
- ✅ **ทั้งคู่ต้องมีพร้อมกันเสมอ** - design.md และ changelog.md ต้องมีทั้งสองอย่าง
- ✅ **design.md** = Version History (Unified) Navigator (สั้น ๆ 2-3 version)
- ✅ **changelog.md** = Full Changelog (Detailed sections ทุก version)

**จำกัดรูปแบบทันที (Mandatory Format Enforcement):**

| File | รูปแบบที่ต้องใช้ | ห้ามใช้ |
|------|-----------------|-----------|
| **changelog.md** (main) | Full Changelog (Detailed sections) | Version History (Unified) table |
| **design.md** | Version History (Unified) Navigator | Full Changelog sections |

---

### 🔍 คำอธิบาย "Navigator" คืออะไร?

**Version History (Unified) Navigator** คือ:
- ✅ Version History table ที่มี **เฉพาะ 2-3 version ล่าสุด** เท่านั้น
- ✅ แต่ละ entry = **Headline + Summary 1 บรรทัด** (ไม่มี bullet points)
- ✅ มี **link ไปยัง Full Changelog**: `> Full history: [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)`
- ❌ ไม่ใช่ Version History แบบเต็ม (ที่มีทุก version)

---

### 📋 ตัวอย่างแบบเต็ม (Both Files Together)

#### design.md - Section ท้ายไฟล์

```markdown
# Document Changelog & Versions History Control

## 0) Document Control
> **Current Version:** 3.9
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

... (เนื้อหา design) ...

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 3.9 | 2026-01-20 | **[Added design.md <> changelog.md Relationship Rule](changelog.md#L863)** | a77b77ae... |
| | | Summary: Enforced clear separation between design (navigator) and changelog (full) | |
| 3.8 | 2026-01-20 | **[Clarified changelog.md Location Patterns](changelog.md#L820)** | a77b77ae... |
| | | Summary: Fixed AI confusion about master changelog location | |
| 3.7 | 2026-01-20 | **[Standardized on Line Number Links](changelog.md#L750)** | a77b77ae... |
| | | Summary: Line Number format for precise changelog navigation | |

> Full history: [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)
```

#### changelog.md - ไฟล์แยก

```markdown
# Changelog - Main

> **Parent Document:** [design.md](design.md)
> **Current Version:** 3.9
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Version 3.9: Added design.md <> changelog.md Relationship Rule

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added Section 5.2.1: Mandatory design.md <> changelog.md relationship
- changelog.md MUST be Full Changelog (not Version History table)
- design.md MUST be Version History (Unified) Navigator
- Applies to all patterns (Simple/Mixed) when both files exist
- Added mechanism diagram and linking examples

### Summary
Enforced clear separation between design (navigator) and changelog (full)

### Links
- Design: [design.md#version-39](design.md#version-39)

---

## Version 3.8: Clarified changelog.md Location Patterns

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added location pattern to Reserved Terms: root vs changelog/ subdirectory
- Pattern 1: changelog.md at root IS the master changelog
- Pattern 2: changelog/changelog.md IS the master changelog (not root)
- Updated Decision Tree with master changelog location for each pattern
- Added WARNING about duplicate changelog.md files

### Summary
Fixed AI confusion about which changelog.md is the master

### Links
- Design: [design.md#version-38](design.md#version-38)

---

## Version 3.7: Standardized on Line Number Links

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Standardized Navigator link format to `#Lxx` (Line Number)
- Added Navigator Link Format section with GitHub/GitLab/Bitbucket support
- Updated Best Practice: emphasized Line Number format as primary
- Updated Format Compliance Metrics: Platform Support specified
- Removed alternative anchor format - focus on Git platforms

### Summary
Line Number format for precise changelog navigation

### Links
- Design: [design.md#version-37](design.md#version-37)
```

---

### 📊 เปรียบเทียบรูปแบบที่ถูกต้อง vs ผิด

| ไฟล์ | ✅ ถูกต้อง (Navigator + Full) | ❌ ผิด (Full ไปหมด) |
|-------|-------------------------------|---------------------|
| **design.md** | มี Version History table 2-3 entries + link | ไม่มี Version History หรือมีแบบเต็ม |
| **changelog.md** | มี Detailed sections ทุก version | ไม่มีหรือมีแค่ Version History table |

---

**ใช้ได้กับทุก Pattern:**

| Pattern | design.md | changelog.md |
|---------|-----------|--------------|
| **1 (Simple)** | `./design.md` (Navigator - 2-3 versions) | `./changelog.md` (Full - all versions) |
| **2 (Mixed)** | `./design/*.design.md` (Navigator - 2-3 versions) | `./changelog/changelog.md` (Full - all versions) |

---

**⚠️ ห้ามทำ:**
- ❌ สร้าง changelog.md ที่มีเฉพาะ Version History (Unified) table (เมื่อมี design.md คู่กัน)
- ❌ สร้าง design.md ที่มี Full Changelog sections (ต้องเป็น Navigator เท่านั้น)
- ❌ มีเพียงไฟล์เดียว (ต้องมีทั้ง design.md และ changelog.md พร้อมกัน)

### 5.3 Session ID Requirement (Anti-Mockup Policy)

#### 5.3.1 Session ID คืออะไร?
**Session ID** คือ **ตัวระบุเฉพาะสำหรับ Claude Code session ปัจจุบัน** ใช้สำหรับ:
- ตรวจสอบย้อนกลับได้ว่าการแก้ไขนี้มาจาก session ไหน
- ลิงก์ไปยังประวัติการสนทนาใน Claude Code
- หลักฐานยืนยันการทำงาน (audit trail)

#### 5.3.2 Session ID อยู่ที่ไหน?
Session ID อยู่ใน **`<env>` tags** ที่ระบบส่งมาให้ทุกครั้งที่มีการสนทนา:

```xml
<env>
Session ID: a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
Time: [timestamp]
</env>
```

#### 5.3.3 วิธีดึง Session ID ที่ถูกต้อง
1. ✅ อ่าน `<env>` tags **ใน session ปัจจุบัน** เท่านั้น
2. ✅ คัดลอก `Session ID` ตัวเต็ม (UUID format) มาใช้
3. ❌ ห้ามใช้ Session ID จาก session เก่า
4. ❌ ห้ามสร้าง/แต่ง Session ID เอง

#### 5.3.4 รูปแบบ Session ID ที่ถูกต้อง
Session ID เป็น **UUID format** (36 characters):
```
a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

#### 5.3.5 ตัวอย่าง Session ID จริง (Session ปัจจุบัน)
```
Session ID: a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
Date: 2026-01-20
```

### 5.4 Naming Rules (Flexible)

#### 5.4.1 Changelog File Naming
**รูปแบบที่แนะนำ**: `<doc>.changelog.md`

**ตัวอย่าง**:
- `anti-mockup.changelog.md`
- `document-changelog-control.changelog.md`
- `safe-file-reading.changelog.md`

**ข้อดี**:
- สั้น ชัดเจน อ่านง่าย
- Sort files ง่าย (A-Z)
- รู้ทันทีว่าเป็น changelog (`.changelog.md`)

#### 5.4.2 Location Options (ยืดหยุ่นตามบริบท)

| ตำแหน่ง | รูปแบบ | ใช้เมื่อ |
|---------|---------|---------|
| `design/changelog/<doc>.changelog.md` | แบบมี subdir | design docs ที่มี changelog หลายไฟล์ |
| `changelog/<doc>.changelog.md` | แบบ subdir ระดับ root | โปรเจกต์มี changelog รวมอยู่ที่เดียว |
| `<doc>.changelog.md` | แบบ same directory | เอกสารเดียวที่มี changelog แยก |

**ตัวอย่าง Full Path**:
- `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/design/changelog/anti-mockup.changelog.md`
- `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/changelog/document-changelog-control.changelog.md`

#### 5.4.3 Design Documents (Non-Changelog)
- ใช้ **Version History (Unified)** ที่ส่วนท้ายไฟล์เท่านั้น
- ไม่ต้องสร้างไฟล์ changelog แยก (ถ้าไม่จำเป็น)

---

### 5.5 เมื่อไหรควรสร้าง Changelog แบบเต็ม (.changelog.md)?

#### 5.5.1 Changelog แบบเต็มคืออะไร?
**Changelog แบบเต็ม** คือไฟล์แยกที่บันทึกประวัติการเปลี่ยนแปลงอย่างละเอียด ใช้ชื่อ `<doc>.changelog.md`

#### 5.5.2 เมื่อไหรควรสร้าง Changelog แบบเต็ม?

| สถานการณ์ | ควรสร้าง .changelog.md หรือไม่? | เหตุผล |
|----------|------------------------------|---------|
| Design doc มี version น้อย (< 5) | ❌ ไม่ต้อง | Version History ในไฟล์เดียวพอ |
| Design doc มีการอัปเดตบ่อย | ✅ ควรสร้าง | แยก history ออกมาก่อนจะยาวเกินไป |
| Design doc มีการเปลี่ยนแปลงซับซ้อน | ✅ ควรสร้าง | ต้องการบันทึกรายละเอียดมาก |
| Design doc ใช้งานร่วมกันหลายคน | ✅ ควรสร้าง | Track การเปลี่ยนแปลงแยกจากเนื้อหา |
| Design doc สั้นๆ อธิบายครั้งเดียว | ❌ ไม่ต้อง | ใช้ Version History ในไฟล์เดียวพอ |

#### 5.5.3 โครงสร้าง Changelog แบบเต็ม

**ไฟล์**: `<doc>.changelog.md`

> **หมายเหตุสำคัญ**: Full changelog **ไม่มี Version History (Unified) table** เพื่อหลีกเลี่ยงความซ้ำซ้อนกับ design.md
> - **design.md** = มี Version History (Unified) เป็น Navigator
> - **<doc>.changelog.md** = มี Detailed sections เท่านั้น

```markdown
# Changelog - <Document Name>

> **Parent Document:** [<doc>.md](<path to doc>)
> **Current Version:** X.Y
> **Session:** <Session ID>

---

## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Session ID>

### Changes
- <Change 1 - detailed description>
- <Change 2 - detailed description>
- <Change 3 - detailed description>

### Summary
<One-line summary>

### Links (Optional)
- Issue: #123
- PR: #456
- Commit: abc123

---

## Version X.X: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Session ID>

### Changes
- <Change 1 - detailed description>
- <Change 2 - detailed description>

### Summary
<One-line summary>
```

#### 5.5.4 การเชื่อมโยงระหว่าง Design Doc และ Changelog แบบเต็ม

**ใน Design Doc** (ส่วนท้าย - แสดง version ล่าสุด 2-3 version + Navigator links):
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[<Short headline>](<doc>.changelog.md#L1)** | <Session ID> |
| | | Summary: <One-line summary> | |
| X.X | YYYY-MM-DD | **[<Short headline>](<doc>.changelog.md#L15)** | <Session ID> |
| | | Summary: <One-line summary> | |

> Full history: [<doc>.changelog.md](<doc>.changelog.md)
```

**Navigator Link Format: `#Lxx`**
- ใช้ **Line Number format**: `<doc>.changelog.md#L1`, `<doc>.changelog.md#L15`
- รองรับโดย GitHub, GitLab, Bitbucket
- ระบุตำแหน่งแม่นยำไปยังบรรทัดนั้นใน changelog

**ใน Changelog แบบเต็ม** (`<doc>.changelog.md`):
- **ไม่มี Version History (Unified) table** - เพื่อหลีกเลี่ยงความซ้ำซ้อน
- มี **Detailed sections เท่านั้น** - แต่ละ version เป็น section แยกกัน
- มี link กลับไปยัง parent document:
  ```markdown
  > Parent Document: [<doc>.md](../<doc>.md)
  ```

**ความแตกต่าง:**
| ประเภท | มี Version History Table? | จำนวน Version | รายละเอียด |
|----------|---------------------------|--------------|-----------|
| **Design Doc** | ✅ มี (เป็น Navigator) | 2-3 version ล่าสุด | Summary สั้นๆ + links |
| **Changelog แบบเต็ม** | ❌ ไม่มี | ทุก version | Detailed sections เท่านั้น |

#### 5.5.5 ระดับความละเอียด (Detail Level Guidelines)

##### 5.5.5.1 Brief Entry (สำหรับ Design Doc)
**ใช้สำหรับ:** Version History ที่อยู่ใน design documents (แสดง 2-3 version ล่าสุด)

**รูปแบบ:**
```markdown
| X.Y | YYYY-MM-DD | **<Short Headline>** | <Session ID> |
| | | Summary: <One-line summary> | |
```

**ระดับความละเอียด:**
- **Headline**: สั้น ๆ เห็นแล้นเข้าใจ (1 บรรทัด)
- **Summary**: สรุปสั้นๆ ให้เข้าใจแนวคิด (1 บรรทัด)
- **ไม่ต้องมี** bullet points แยกย่อย
- **มี link**: `> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)`

**ตัวอย่าง:**
```markdown
| 3.4 | 2026-01-20 | **Simplified File Organization Patterns** | a77b77ae... |
| | | Summary: Reduced from 5 patterns to 3, clarified migration path | |
```

##### 5.5.5.2 Detailed Entry (สำหรับ Changelog แบบเต็ม)
**ใช้สำหรับ:** Full changelog files (`<doc>.changelog.md`) - แสดงทุก version

> **หมายเหตุ**: Full changelog ไม่มี Version History (Unified) table
> - ใช้ **Detailed sections** แทน - แต่ละ version เป็น section แยกกัน
> - Navigator อยู่ใน design.md แทน

**รูปแบบ (Detailed Section):**
```markdown
## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Session ID>

### Changes
- <Change 1 - detailed description>
- <Change 2 - detailed description>
- <Change 3 - detailed description>

### Summary
<One-line summary>

### Links (Optional)
- Issue: #123
- PR: #456
- Commit: abc123
```

**ระดับความละเอียด:**
- **Headline**: สั้น แต่ชัดเจน
- **Bullet points**: รายการเปลี่ยนแปลงแต่ละข้อ (จำนวนไม่จำกัด)
- **Summary**: สรุปภาพรวม (1 บรรทัด)
- **สามารถมี** เพิ่มเติม:
  - Breaking changes (ถ้ามี)
  - อ้างอิง Issue/PR/Commit (ถ้าจำเป็น)
  - หมวดหมู่อื่นๆ ตามความเหมาะ

**ตัวอย่าง:**
```markdown
## Version 3.4: Simplified File Organization Patterns to 3

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Removed Pattern 1 (design/ with changelog/ inside) - merged into Pattern 2
- Removed Pattern 3 (Small Project) - merged into Pattern 1
- Removed Pattern 4 (duplicate of Pattern 2)
- Renumbered Pattern 5 → Pattern 3 (Legacy)
- Updated Decision Tree: check for ./changelog/ or ./design/ → Pattern 2

### Summary
Patterns reduced from 5 to 3 for clarity.

### Links
- Design: [design.md#version-34](../design.md#version-34)
```

##### 5.5.5.3 การเชื่อมโยงระหว่าง Brief และ Detailed

**การทำงานร่วมกัน:**
```
design.md (Version History - Navigator)
  ├─ Version 3.4 → [link](video.changelog.md#L1) → video.changelog.md (Detailed)
  ├─ Version 3.3 → [link](video.changelog.md#L15) → video.changelog.md (Detailed)
  └─ Version 3.2 → [link](video.changelog.md#L30) → video.changelog.md (Detailed)

video.changelog.md (Detailed Sections Only - No Table)
  ├─ Version 3.4 section (full details)
  ├─ Version 3.3 section (full details)
  └─ Version 3.2 section (full details)
```

**Best Practice:**
- **Design doc** ใช้ Version History (Unified) เป็น Navigator (2-3 version ล่าสุด)
  - Brief entries: headline + 1-line summary
  - Navigator links: `<doc>.changelog.md#Lxx` (Line Number format - รองรับ GitHub/GitLab/Bitbucket)
- **Full changelog** ไม่มี Version History (Unified) table
  - Detailed sections เท่านั้น - แต่ละ version เป็น section แยกกัน
  - Section headers: `## Version X.Y: <Headline>`
- **Session ID** ต้องเป็นค่าจริงจาก Environment เสมอ

**ประโยชน์ของแนวทางนี้:**
- ✅ **ไม่ซ้ำซ้อน**: Version History (Unified) อยู่ที่เดียว (design.md)
- ✅ **ชัดเจน**: design.md = navigator, changelog.md = details
- ✅ **ง่าย**: Full changelog โฟกัสที่เนื้อหาเต็มเท่านั้น
- ✅ **แม่นยำ**: Line Number links ชี้ตรงไปยัง version นั้นๆ ใน changelog

### 5.6 Change Classification
- **Major**: เปลี่ยนโครงสร้าง/แนวทางหลัก → เพิ่ม version หลัก (X.0)
- **Minor**: เพิ่ม/ปรับเนื้อหาสำคัญ → เพิ่ม version ย่อย (X.Y)
- **Patch**: แก้ถ้อยคำ/ความชัดเจน → เพิ่ม patch (X.Y.Z)

---

### 5.7 Legacy Changelog Auto-Migration System

#### 5.7.1 วัตถุประสงค์
ระบบ **Auto-Migration** ที่ตรวจจับและแปลง changelog รูปแบบเก่าให้เป็น **Version History (Unified)** โดยอัตโนมัติ เมื่อมีการ entry ไปยัง project

#### 5.7.2 Legacy Changelog Formats ที่ระบบรองรับ

| Format ที่ระบบรู้จัก | ตัวอย่าง | Migration Strategy |
|---------------------|---------|-------------------|
| **Simple date-change list** | `| Date | Change |` | Parse → แปลงเป็น Version History |
| **Version list without Session ID** | `| Version | Date | Changes |` | เพิ่ม Session ID column |
| **Changelog section without table** | Markdown list | Parse → แปลงเป็น table |
| **No changelog at all** | ไม่มี section | สร้าง Version History ใหม่ (v1.0) |

#### 5.7.3 Auto-Migration Workflow

```text
Entry → Project ที่ Active
  ↓
System เจอไฟล์ design/doc
  ↓
ตรวจสอบ: มี Version History (Unified) หรือยัง?
  ↓
  ├─ มีแล้ว → ไม่ต้องทำอะไร ✅
  │
  └─ ยังไม่มี / รูปแบบเก่า → เริ่ม Migration Process
      ↓
    1. Detect Legacy Format
    2. Parse Existing Data
    3. Transform to Version History (Unified)
    4. Add Session ID (จาก current session)
    5. Append to File (ส่วนท้าย)
    6. Log Migration ✅
```

#### 5.7.4 Migration Rules (Data Preservation)

| Rule | Description |
|------|-------------|
| **No Data Loss** | ประวัติเก่าทั้งหมดต้องถูก preserve |
| **Incremental Version** | เริ่ม version ถัดจาก version เก่าสุด |
| **Session ID Filling** | เติม Session ID จำลองสำหรับ entry เก่า (เช่น `LEGACY-001`) |
| **Current Session** | entry ใหม่ใช้ Session ID ปัจจุบัน |
| **Backup First** | สร้าง backup ก่อน migrate (ถ้าระบบรองรับ) |

#### 5.7.5 Migration Examples

**Example 1: Simple Date-Change List → Version History (Unified)**

**Before (Legacy)**:
```markdown
## Changelog
| Date | Change |
|------|--------|
| 2026-01-15 | Initial version |
| 2026-01-16 | Updated content |
```

**After (Migrated)**:
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-01-16 | **Updated Content** | LEGACY-001 |
| | | - Updated content from legacy format | |
| 1.0 | 2026-01-15 | **Initial Version** | LEGACY-001 |
| | | - Initial version (migrated from legacy) | |
| 2.0 | 2026-01-20 | **Auto-Migration** | a77b77ae... |
| | | - Migrated from legacy changelog format | |
```

**Example 2: No Changelog → Initialize**

**Before**: ไม่มี changelog section

**After (Migrated)**:
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial Version Tracking** | a77b77ae... |
| | | - Initial version tracking started | |
```

#### 5.7.6 Detection Patterns (Regex)

| Pattern | Description | Regex Example |
|---------|-------------|---------------|
| Table with Date column | Detect changelog table | `\| Date \|` |
| Version column without Session ID | Detect incomplete format | `\| Version \|.*\|\s*\| Date \|` (แต่ไม่มี Session ID) |
| Changelog section | Detect section header | `^#+\s*[Cc]hangelog` |
| No changelog | No match found | N/A |

#### 5.7.7 On-Demand Trigger (ไม่ Batch Scan)

**เมื่อไหร่ระบบจะทำงาน?**
- ✅ เมื่อ AI entry ไปยัง project นั้นครั้งแรก
- ✅ เมื่อเปิดไฟล์ design/doc ขึ้นมาแก้ไข
- ❌ ไม่ไป scan ทุกไฟล์ใน project เลย
- ❌ ไม่ migrate ถ้าไม่มีการใช้งาน

**Flow**:
```
User/AI → "แก้ไฟล์นี้หน่อย" → Open file
  ↓
System → "มี Version History หรือยัง?"
  ↓
  └─ ยัง → "Detect format → Migrate → Done ✅"
```

#### 5.7.8 Implementation Notes

**สำหรับ AI/System ที่จะ implement:**

1. **Check First**: ตรวจสอบว่ามี `## Version History (Unified)` หรือยัง
2. **Detect Format**: ใช้ regex/pattern matching ดูว่า format เดิมเป็นแบบไหน
3. **Parse Data**: ดึงข้อมูลเก่าออกมา (date, version, changes)
4. **Transform**: แปลงเป็น Version History (Unified) format
5. **Assign Session IDs**:
   - Entry เก่า → `LEGACY-XXX` (sequential)
   - Entry ใหม่ → Session ID ปัจจุบัน
6. **Append**: เพิ่มลงท้ายไฟล์ (section สุดท้าย)
7. **Log Migration**: บันทึกว่าได้ migrate แล้ว

**Error Handling**:
- ถ้า parse ไม่สำเร็จ → สร้าง Version History ใหม่ (v1.0)
- ถ้า format ไม่รู้จัก → สร้าง Version History ใหม่ (v1.0)
- ถ้ามีข้อมูลเสียหาย → preserve ทุกอย่างที่อ่านได้

---

## 6) Decision Matrix (Detailed)

| Context | Recommended Format | Minimum Required | Notes |
|---|---|---|---|
| New document with no changelog | Footer Short | Versions History (Short) | ต้องมีอย่างน้อย 1 รูปแบบทันที |
| Existing changelog doc | Detailed + Summary | Detailed + Summary | ต้องอัปเดตทั้งสองส่วนเสมอ |
| Design doc with parent changelog | Footer Short + link | Footer Short | ลิงก์เป็น optional แต่แนะนำ |
| Micro update (typo/clarity) | Patch (X.Y.Z) | 1 format | ระบุว่าเป็น Patch ใน summary |
| Structural change | Major (X.0) | 1 format | ควรเขียน rationale สั้น ๆ |
| Sensitive/regulated docs | Detailed + Summary | 1 format | แนะนำละเอียดเสมอ |

---

## 7) Rule Interaction (Document Consistency)

- **Single Source of Truth**: หากมี changelog หลัก ให้ใช้เป็น reference เดียว
- **Cross‑reference check**: ทุกลิงก์ `changelog.<doc>.md` ต้องอ้างถึงไฟล์ที่มีอยู่จริง
- **No duplicated history**: ห้ามคัดประวัติเต็มซ้ำหลายไฟล์
- **Naming flexibility**: เปลี่ยน naming ได้ แต่ต้องอัปเดต link ให้สอดคล้องทุกจุด

---

## 8) Legacy Docs Policy

### 8.1 Legacy without history
- เพิ่ม **Versions History (Short)** ที่ท้ายเอกสารทันที
- ระบุสถานะว่าเริ่ม tracking จาก version ใด

### 8.2 Legacy with scattered history
- ย้ายรายละเอียดทั้งหมดไปยัง **changelog หลัก** (ถ้ามี)
- เอกสารเดิมเก็บเพียง footer แบบย่อ

### 8.3 Migration Rule
- ห้ามลบประวัติเดิมแบบไม่อ้างอิง
- ต้องมีลิงก์ย้อนกลับไป changelog หลักเสมอ

---

## 9) ตัวอย่างอ้างอิง (Reference)

### 9.1 Master Changelog (ไฟล์หลัก)
**`changelog.md`** = Master/Main changelog โดยปริยาย
- ใช้สำหรับบันทึกการเปลี่ยนแปลงหลักของ project/ระบบ
- เป็นจุดรวม (aggregate) ของการเปลี่ยนแปลงทั้งหมด
- ถ้าไม่มี changelog อื่นๆ ให้ลิงก์มาที่ไฟล์นี้

### 9.2 Specific Document Changelogs
ไฟล์ changelog สำหรับเอกสารเฉพาะ:
- `video.changelog.md`
- `document-changelog-control.changelog.md`
- `safe-file-reading.changelog.md`

ใช้เมื่อ:
- เอกสารมีการอัปเดตบ่อย
- ต้องการแยกประวัติออกจาก master changelog
- design doc ขนาดใหญ่และซับซ้อน

### 9.3 File Organization Patterns (ตัวอย่างรูปแบบต่างๆ)

#### Pattern 1: Simple Project (ไม่มี ./changelog/ และ ./design/)
```
./
├── README.md
├── design.md                 ← Version History ท้ายไฟล์ (ถ้ามี)
├── changelog.md              ← Master changelog at ROOT
└── src/
```
**ใช้เมื่อ:** Project ไม่มีทั้ง `./changelog/` และ `./design/` - ใช้ root level เท่านั้น
**หมายเหตุ:** `changelog.md` ที่ root level คือ Master changelog
**⚠️ เมื่อใดที่มี `./changelog/` หรือ `./design/` ขึ้นมา ให้ migrate ไป Pattern 2 ทันที**

#### Pattern 2: Mixed (มีทั้ง design และ changelog) - **รูปแบบสมบูรณ์ที่สุด**
```
./
├── design/
│   ├── anti-mockup.design.md   ← Version History ท้ายไฟล์
│   ├── safe-file-reading.design.md
│   └── ...
├── changelog/
│   ├── changelog.md         ← Master changelog (INSIDE changelog/)
│   ├── video.changelog.md
│   └── api.changelog.md
└── src/
```
**ใช้เมื่อ:** Project มีทั้ง design docs และ specific changelogs - **นี่คือรูปแบบที่ดีที่สุด**
- design/ เก็บ design documents แยกจาก code
- changelog/ เก็บ changelogs แยกจาก design
- `changelog/changelog.md` (not root `changelog.md`) คือ Master changelog

#### Pattern 3: Legacy (มี ./changelog/ แต่ไม่มี ./design/ - Anti-Pattern)
```
./
├── changelog/
│   ├── changelog.md
│   └── video.changelog.md
└── ... (ไม่มี design/ subdir)
```
**หมายเหตุ:** นี่เป็น anti-pattern **ควร migrate ไป Pattern 2 เสมอ** (สร้าง ./design/ เพื่อให้ครบถ้วน)

#### สรุป Decision Tree:

```
มี ./changelog/ หรือ ./design/ ไหม?
├─ มี → ✅ ใช้ Pattern 2 (Mixed - ideal/complete)
│         → Master changelog = changelog/changelog.md
└─ ไม่มี → ใช้ Pattern 1 (Simple - root level only)
         → Master changelog = changelog.md at root

⚠️ MIGRATION RULE: เมื่อใดที่มี ./changelog/ หรือ ./design/ เริ่มมี
                 → migrate ไป Pattern 2 ทันที (เพื่อความสมบูรณ์)

⚠️ IMPORTANT: ห้ามมีทั้ง `./changelog.md` และ `./changelog/changelog.md` พร้อมกัน (ซ้ำซ้อน)
```

#### ตัวอย่าง Full Path:

| Pattern | Master Changelog | Specific Changelogs | Design Docs |
|---------|-----------------|---------------------|-------------|
| **1 (Simple)** | `./changelog.md` (root) | (ไม่มี) | `./design.md` (root) |
| **2 (Mixed - Ideal)** | `./changelog/changelog.md` | `./changelog/video.changelog.md` | `./design/*.design.md` |
| **3 (Legacy)** | `./changelog/changelog.md` | `./changelog/video.changelog.md` | (ไม่มี - migrate to 2) |

### 9.4 Design Documents with Version History
- ไฟล์ `.design.md` ทุกไฟล์ควรมี Version History (Unified) ที่ส่วนท้าย

### 9.5 Reserved Terms & Protected Keywords

#### 9.5.1 วัตถุประสงค์
ป้องกันความสับสน ความคลาดเคลิ่อน และความไม่สม่ำเสมอในการตั้งชื่อไฟล์และ section โดยกำหนด **Reserved Terms** ที่มีความหมายพิเศษ

#### 9.5.2 Reserved File Names (Master Files)

| Reserved Term | Location Pattern | ความหมาย | ห้ามใช้สำหรับ |
|--------------|-----------------|-----------|-----------------|
| `changelog.md` | Root level only (`./changelog.md`) | Master changelog at root | Other changelog files, or if using Pattern 2 |
| `changelog/changelog.md` | Inside `./changelog/` directory | Master changelog in subdir | Other changelog files |
| `design.md` | Root level only (`./design.md`) | Master design doc at root | Other design files |

**กฎ:**
- ห้ามตั้งชื่อไฟล์เป็น `changelog.md` หรือ `design.md` ถ้าไม่ใช่ Master file
- ใช้รูปแบบ `<doc>.changelog.md` หรือ `<doc>.design.md` แทน

**Pattern 1 (Simple):** `./changelog.md` = Master changelog
**Pattern 2 (Mixed):** `./changelog/changelog.md` = Master changelog
**⚠️ IMPORTANT:** ห้ามมีทั้ง `./changelog.md` และ `./changelog/changelog.md` พร้อมกัน (ซ้ำซ้อน)

#### 9.5.3 Reserved File Suffixes

| Reserved Suffix | ความหมาย | ตัวอย่างที่ถูกต้อง | ห้ามใช้สำหรับ |
|----------------|-----------|-------------------|-----------------|
| `.design.md` | Design document | `anti-mockup.design.md` | ไฟล์ที่ไม่ใช่ design |
| `.changelog.md` | Changelog file | `video.changelog.md` | ไฟล์ที่ไม่ใช่ changelog |

**กฎ:**
- Suffix เหล่านี้สงวนไว้สำหรับประเภทที่ระบุเท่านั้น
- อย่าใช้ suffix เหล่านี้กับไฟล์ประเภทอื่น (เช่น `config.changelog.md` ผิด)

#### 9.5.4 Reserved Section Names

| Reserved Term | ความหมาย | รูปแบบที่ถูกต้อง | ห้ามใช้แทน |
|--------------|-----------|---------------------|-------------|
| `Version History (Unified)` | ตาราง version history | Section header | `Changelog`, `Change Log`, `History` |

**กฎ:**
- ทุก Version History ต้องใช้ชื่อ section `## Version History (Unified)` เท่านั้น
- ห้ามใช้ชื่อแทร เช่น `## Changelog`, `## Changes`, `## History`

#### 9.5.5 Reserved Table Columns

| Column Name | จำเป็นต้อง | ห้ามใช้ชื่อแทน |
|-------------|-------------|------------------|
| `Version` | ✅ เวอร์ชัน (X.Y, X.Y.Z) | `Ver`, `Rev`, `V` |
| `Date` | ✅ วันที่ (YYYY-MM-DD) | `Time`, `Updated`, `When` |
| `Changes` | ✅ รายละเอียดการเปลี่ยนแปลง | `Description`, `What`, `Notes` |
| `Session ID` | ✅ UUID จาก Environment | `ID`, `Session`, `UUID` |

#### 9.5.6 Protected Keywords

| Keyword | ความหมาย | ใช้เมื่อ |
|---------|-----------|----------|
| `LEGACY-XXX` | Session ID สำหรับ entry เก่า | Auto-migration เท่านั้น |
| `Unified` | รูปแบบ Version History | Section name เท่านั้น |

#### 9.5.7 Enforcement Rules

**Auto-Detection (when AI enters project):**
1. ตรวจสอบชื่อไฟล์ทับกับ Reserved Terms
2. ถ้าพบการใช้ชื่อสงวน → แจ้งเตือนและขอให้เปลี่ยนชื่อ
3. ตรวจสอบ section names ในไฟล์ design/changelog
4. ถ้าพบ section ที่ไม่ใช่ `Version History (Unified)` → แจ้งเตือน

**Migration Auto-Correction:**
```text
เจอไฟล์ชื่อ `changelog.md` แต่ไม่ใช่ master?
→ แนะนำให้เปลี่ยนเป็น `main.changelog.md` หรือ `<project>.changelog.md`

เจอ section `## Changelog` ในไฟล์?
→ Auto-migrate ไป `## Version History (Unified)`
```

#### 9.5.8 Quick Reference Card

```
✅ ถูกต้อง:
- video.changelog.md
- anti-mockup.design.md
- ## Version History (Unified)
- changelog.md (master changelog - location independent)

❌ ผิด:
- changelog.md (not master - ใช้ชื่อนี้ถ้าไม่ใช่ master เท่านั้น)
- config.changelog.md (wrong suffix usage)
- ## Changelog (wrong section name)
- design.md (not master)
```

**หมายเหตุ:** `changelog.md` เป็น master changelog เสมอ ไม่ว่าจะอยู่ที่ไหน:
- `./changelog.md` (root - Pattern 1)
- `./changelog/changelog.md` (Pattern 3 - anti-pattern)
- `./changelog/changelog.md` (Pattern 2 - ideal)

Location ไม่ส่งผลต่อ master status แต่ **Pattern 2 (Mixed - มีทั้ง design/ และ changelog/)** คือรูปแบบที่สมบูรณ์ที่สุด

---

## 10) Quality Metrics

### 10.1 Core Metrics (Mandatory)

| Metric | Target | หมายเหตุ |
|---|---|---|
| **Version History Presence** | 100% | ทุกเอกสารต้องมี Version History (Unified) |
| **Session ID Accuracy** | 100% No Mock | ต้องเป็นค่าจริงจาก <env> (ถ้าไม่มีใช้ LEGACY-XXX) |
| **Date Completeness** | 100% | ทุก entry ต้องมี Date (YYYY-MM-DD) |
| **History Preservation** | 100% | ห้ามลบ/แก้ไข Version History เดิม |
| **Version Classification** | 100% | ใช้ Major/Minor/Patch ถูกต้อง |
| **Naming Format** | Recommended | ใช้ `<doc>.changelog.md` (แต่ไม่บังคับ) |

### 10.2 Migration Metrics (Auto-Migration)

| Metric | Target | หมายเหตุ |
|---|---|---|
| **Legacy Format Detection** | 100% | ตรวจจับ legacy format ทั้ง 4 แบบ |
| **Data Preservation** | 100% | ไม่สูญหายข้อมูลเก่า |
| **On-Demand Only** | 100% | ไม่ batch scan ทุกไฟล์ |
| **LEGACY Session ID** | Consistent | ใช้ `LEGACY-001`, `LEGACY-002` ฯลฯ |

### 10.3 Format Compliance Metrics

| Metric | Target | หมายเหตุ |
|---|---|---|
| **Design Doc Table Structure** | 100% | design.md ต้องมี Version History (Unified) table |
| **Full Changelog Structure** | 100% | changelog แบบเต็มใช้ Detailed sections เท่านั้น (ไม่มี table) |
| **Column Completeness** | 100% | design.md table ต้องมี Version, Date, Changes, Session ID |
| **Navigator Links Format** | `#Lxx` | design.md → changelog.md#Lxx (Line Number) |
| **Platform Support** | GitHub/GitLab/Bitbucket | Line Number links รองรับโดย Git platforms |
| **Cross-Reference** | Required | Full changelog ต้อง link กลับ design.md |

---

## 11) Changelog (Unified)

### Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.3 | 2026-01-20 | **Clarify changelog.md MUST have BOTH: detailed sections + Version History Unified table** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - User clarified: changelog.md format has UPPER part (detailed sections) + LOWER part (summary table) | |
| | | - Updated format table: changelog.md = Detailed sections (UPPER) + Version History Unified table (LOWER) | |
| | | - Updated comparison table to reflect correct format | |
| | | - Updated example to show BOTH parts of changelog.md | |
| | | - Added link to changelog at end of rules files (NOT Version History section) | |
| | | - Rules files rely on Git for history, NOT Version History sections | |
| | | Summary: changelog.md has BOTH detailed sections AND Version History Unified table | |
| 4.2 | 2026-01-20 | **Clarify changelog.md CAN have "## Version History" header** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Clarified distinction: "## Version History" HEADER is allowed, summary TABLE is not | |
| | | - Updated format table: changelog.md may optionally have "## Version History" header | |
| | | - changelog.md MUST NOT use summary table format (Version | Date | Changes | Session ID) | |
| | | - Updated example to show changelog.md with "## Version History" header + detailed sections | |
| | | - Fixed confusion: HEADER ≠ TABLE format | |
| | | Summary: changelog.md can have "## Version History" section header, but not the summary table | |
| 4.1 | 2026-01-20 | **Clarify design.md = ONLY link, NO version table** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added ⚠️ CRITICAL section: design.md Should NOT Have Version History Table | |
| | | - Changed Navigator definition: design.md has ONLY Full history link | |
| | | - Updated example to show design.md with NO table, only link | |
| | | - Added \"Why This Design?\" explanation for Single Source of Truth | |
| | | - Clarified design.md is specification document, NOT a changelog | |
| | | Summary: Made it crystal clear - design.md provides ONLY navigation link | |
| 4.0 | 2026-01-20 | **Clarified Navigator Format with Complete Examples** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added explicit rule: Both design.md and changelog.md MUST exist together | |
| | | - Added "What is Navigator?" explanation section with clear bullets | |
| | | - Added complete example showing BOTH files side by side | |
| | | - Added comparison table: Correct vs Incorrect format | |
| | | - Emphasized: design.md = 2-3 entries only, changelog.md = all versions | |
| | | Summary: Made Navigator format crystal clear to prevent AI confusion | |
| 3.9 | 2026-01-20 | **Added design.md <> changelog.md Relationship Rule** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 5.2.1: Mandatory design.md <> changelog.md relationship | |
| | | - changelog.md MUST be Full Changelog (not Version History table) | |
| | | - design.md MUST be Version History (Unified) Navigator | |
| | | - Applies to all patterns (Simple/Mixed) when both files exist | |
| | | - Added mechanism diagram and linking examples | |
| | | Summary: Enforced clear separation between design (navigator) and changelog (full) | |
| 3.8 | 2026-01-20 | **Clarified changelog.md Location Patterns** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added location pattern to Reserved Terms: root vs changelog/ subdirectory | |
| | | - Pattern 1: changelog.md at root IS the master changelog | |
| | | - Pattern 2: changelog/changelog.md IS the master changelog (not root) | |
| | | - Updated Decision Tree with master changelog location for each pattern | |
| | | - Added WARNING about duplicate changelog.md files | |
| | | Summary: Fixed AI confusion about which changelog.md is the master | |
| 3.7 | 2026-01-20 | **Standardized on Line Number Links (#Lxx)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Standardized Navigator link format to `#Lxx` (Line Number) | |
| | | - Added Navigator Link Format section with GitHub/GitLab/Bitbucket support | |
| | | - Updated Best Practice: emphasized Line Number format as primary | |
| | | - Updated Format Compliance Metrics: Platform Support specified | |
| | | - Removed alternative anchor format - focus on Git platforms | |
| 3.6 | 2026-01-20 | **Removed Redundant Version History from Full Changelogs** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Removed Version History (Unified) table from full changelog files | |
| | | - Version History (Unified) now only exists in design.md (as Navigator) | |
| | | - Full changelog files contain detailed sections only (no summary table) | |
| | | - Navigator links use format: `<doc>.changelog.md#Lxx` | |
| | | - Updated Section 5.5.3: Full changelog structure (removed table) | |
| | | - Updated Section 5.5.4: Navigator links with line numbers | |
| | | - Updated Section 5.5.5.2: Detailed Entry format (sections, not table) | |
| | | - Updated Section 5.5.5.3: Best practices for non-redundant design | |
| 3.5 | 2026-01-20 | **Added Detail Level Guidelines** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 5.5.5: ระดับความละเอียด (Detail Level Guidelines) | |
| | | - Brief Entry format for design docs (headline + 1-line summary) | |
| | | - Detailed Entry format for full changelogs (bullet points + summary) | |
| | | - Link relationship: design.md → <doc>.changelog.md | |
| | | - Best practices for maintaining brief vs detailed entries | |
| 3.4 | 2026-01-20 | **Simplified File Organization Patterns to 3** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Removed Pattern 1 (design/ with changelog/ inside) - merged into Pattern 2 | |
| | | - Removed Pattern 3 (Small Project) - merged into Pattern 1 | |
| | | - Removed Pattern 4 (duplicate of Pattern 2) | |
| | | - Renumbered Pattern 5 → Pattern 3 (Legacy) | |
| | | - Updated Decision Tree: check for ./changelog/ or ./design/ → Pattern 2 | |
| | | - Updated Quick Reference Card with new pattern numbers | |
| | | - Clarified that Pattern 2 (Mixed) is the ideal/complete format | |
| 3.3 | 2026-01-20 | **Added Reserved Terms & Protected Keywords** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 9.5: Reserved Terms & Protected Keywords | |
| | | - Reserved file names: changelog.md, design.md (master only) | |
| | | - Reserved suffixes: .design.md, .changelog.md | |
| | | - Reserved section name: Version History (Unified) | |
| | | - Reserved table columns: Version, Date, Changes, Session ID | |
| | | - Protected keywords: LEGACY-XXX, Unified | |
| | | - Added enforcement rules and auto-detection | |
| | | - Added Quick Reference Card for do's and don'ts | |
| 3.2 | 2026-01-20 | **Fixed Pattern 2 & Clarified Migration Path** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Fixed Pattern 2: Simple project without ./changelog/ and ./design/ | |
| | | - Clarified: When ./changelog/ or ./design/ appears → migrate to Pattern 4 | |
| | | - Updated Decision Tree: check for ./changelog/ or ./design/ first | |
| | | - Updated Full Path table for Pattern 2 (no subdir) | |
| | | - Pattern 5 renamed to "Legacy - Anti-Pattern" | |
| | | - Emphasized Pattern 4 as ideal/complete format | |
| 3.1 | 2026-01-20 | **Fixed Pattern Logic & Added Anti-Pattern** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Fixed Pattern 2: Simple project without changelog subdir | |
| | | - Added Pattern 5: Legacy (changelog/ without design/ = anti-pattern) | |
| | | - Updated Decision Tree with correct logic | |
| | | - Added anti-pattern warning and migration guidance | |
| | | - Updated Full Path table with Design Docs column | |
| 3.0 | 2026-01-20 | **Fixed Changelog Location Logic** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Fixed: changelog.md (master) must be in changelog/ subdir | |
| | | - Updated all 4 patterns with correct file locations | |
| | | - Updated Decision Tree with changelog/ logic | |
| | | - Updated Full Path table with changelog/ paths | |
| 2.9 | 2026-01-20 | **Added File Organization Patterns** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added 4 file organization patterns with examples | |
| | | - Added Decision Tree for when to use which pattern | |
| | | - Clarified: changelog.md อยู่รวม design.md (ถ้ามี ./design/) | |
| | | - Added comparison table for all patterns | |
| | | - Prevents confusion about file locations | |
| 2.8 | 2026-01-20 | **Fixed Terminology Consistency** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Removed "Version History (Short)" term (conflicting with Single Format) | |
| | | - Unified to use "Version History (Unified)" for both design docs and changelogs | |
| | | - Clarified difference: design doc (2-3 versions) vs full changelog (all versions) | |
| | | - Added comparison table for design doc vs full changelog | |
| 2.7 | 2026-01-20 | **Clarified Master Changelog Convention** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Defined `changelog.md` as master/main changelog (by default) | |
| | | - Separated master changelog from specific document changelogs | |
| | | - Added Section 9.1: Master Changelog definition | |
| | | - Added Section 9.2: Specific Document Changelogs | |
| | | - Updated path examples with changelog.md as master | |
| 2.6 | 2026-01-20 | **Updated References & Quality Metrics** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Updated Section 9: Reference examples with new naming format | |
| | | - Changed from `changelog.<doc>.md` to `<doc>.changelog.md` | |
| | | - Added full path examples with correct format | |
| | | - Restructured Section 10: Quality Metrics (3 categories) | |
| | | - Added Migration Metrics (Auto-Migration specific) | |
| | | - Added Format Compliance Metrics | |
| 2.5 | 2026-01-20 | **Legacy Changelog Auto-Migration System** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 5.7: Legacy Changelog Auto-Migration | |
| | | - Added legacy format detection (4 types supported) | |
| | | - Added auto-migration workflow (on-demand, no batch scan) | |
| | | - Added migration examples with before/after | |
| | | - Added regex patterns for detection | |
| | | - Added data preservation rules | |
| 2.4 | 2026-01-20 | **Added Full Changelog Design** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Section 5.5: "เมื่อไหรควรสร้าง Changelog แบบเต็ม" | |
| | | - Added decision matrix: when to create .changelog.md | |
| | | - Added full changelog structure template | |
| | | - Added integration guide between design doc and changelog | |
| 2.3 | 2026-01-20 | **Improved Naming Convention** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Changed from `changelog.<doc>.md` to `<doc>.changelog.md` | |
| | | - Added naming rationale (shorter, clearer, easier to sort) | |
| | | - Added flexible location options table | |
| | | - Added full path examples | |
| 2.2 | 2026-01-20 | **Session ID Definition & Guidelines** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added comprehensive Session ID definition (Section 5.3) | |
| | | - Specified where to find Session ID (<env> tags) | |
| | | - Added correct extraction method (current session only) | |
| | | - Added UUID format specification (36 characters) | |
| | | - Added real Session ID example from current session | |
| 2.1 | 2026-01-20 | **Single Universal Format** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Simplified to single format for all documents (Version History Unified only) | |
| | | - Removed Footer Short format (unnecessary complexity) | |
| | | - Added Session ID column directly in Version History table | |
| | | - Added Full history link as optional footer | |
| 2.0 | 2026-01-20 | **Sophisticated Framework Upgrade + Anti-Mockup Enforcement** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Session ID Requirement: ต้องใช้ค่าจริงจาก Environment (No Mock) | |
| | | - Added History Preservation Rule: ห้ามลบ Version History เดิม | |
| | | - Clarified Session ID extraction from <env> tags | |
| | | - Session ID Example: S1589 (2026-01-20 09:06 GMT+7) | |
| 1.7 | 2026-01-20 | **Unified Changelog Structure** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Merged Version History + Summary into single unified block | |
| | | - Summary now embedded per version (no separate section) | |
| 1.6 | 2026-01-20 08:51 +0700 | **Detailed Changelog Format Standardization** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Replaced version list with structured Version History table | |
| | | - Added summary table format for short changelog | |
| | | - Enforced Session ID in Footer Short | |
| | | - Enforced explicit Date/Time in all entries | |
| 1.5 | 2026-01-20 | **Format Extensions** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Added Version History table + Footer Short Session ID + Date requirement | |
| 1.4 | 2026-01-20 | **Three Design Properties** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Security / Flexibility / Operational added as mandatory properties | |
| 1.3 | 2026-01-20 | **Decision & Policy Additions** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Decision Matrix, Rule Interaction, Legacy Docs Policy | |
| 1.2 | 2026-01-20 | **Compliance & Classification** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Minimum Compliance, Change Classification, Metrics | |
| 1.1 | 2026-01-20 | **Flexibility Note** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Naming is recommended, not mandatory | |
| 1.0 | 2026-01-20 | **Initial design document** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Baseline design structure created | |
