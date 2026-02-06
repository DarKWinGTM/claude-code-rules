# Accurate Communication Standard Design

> **Version:** 1.1
> **Date:** 2026-02-06
> **Purpose:** Standardize clear and accurate communication with flexibility
> **Status:** 🟡 **IN PROGRESS** - Design Phase

---

## 0. Document Control

> **Parent Scope:** Claude Code Rules - Communication Standards
> **Current Version:** 1.1
> **Session:** (current session)

---

## 1. Problem Statement

### 1.1 Background

ระหว่างการทำงานพบ communication patterns ที่ทำให้ user สับสน:

| Pattern | Example | Problem |
|---------|---------|---------|
| Vague problem statement | "มีปัญหา!" (ไม่อธิบาย) | User ไม่รู้ว่าต้องทำอะไร |
| Premature success claim | "Fixed!" (ไม่มี test) | User คิดว่าเสร็จแล้ว |

### 1.2 Design Philosophy

**ต้องการกฏที่:**
- ✅ Smart และยืดหยุ่น
- ✅ ใช้ได้จริงในหลาย context
- ✅ มีหลักการรองรับ (principles, not rigid rules)
- ❌ ไม่ใช่กฏแบบตายตัว/ถือๆ โง่ๆ

---

## 2. Core Principles

### 2.1 The Communication Clarity Principle

> **"ผู้รับสารต้องเข้าใจ context ครบถ้วนจากข้อความเดียว"**

**หลักการ:** ทุกข้อความที่ส่งออกต้องให้ผู้รับ:
1. **เข้าใจสถานการณ์** - เกิดอะไรขึ้น
2. **ประเมินผลกระทบได้** - สำคัญแค่ไหน
3. **รู้ว่าต้องทำอะไร** - action required หรือไม่

**ยืดหยุ่น:**
- ไม่จำเป็นต้องมีทุก element ทุกครั้ง
- ใช้วิจารณญาณตาม context
- หาก context ชัดเจนอยู่แล้ว ข้ามได้

### 2.2 The Verification Honesty Principle

> **"อ้างสิ่งที่พิสูจน์ได้เท่านั้น"**

**หลักการ:** Claim ต้องตรงกับ verification level:

| Verified Level | สามารถพูดได้ |
|----------------|-------------|
| ยังไม่ได้ทำ | "จะทำ X" |
| ทำแล้ว ยังไม่ test | "ทำแล้ว รอ verify" |
| Test ผ่านบางส่วน | "X ผ่าน, Y รอ" |
| Test ผ่านครบ | "ทำงานได้" |
| Stable over time | "แก้ไขแล้ว" |

**ยืดหยุ่น:**
- Context ต่างกัน verification level ต่างกัน
- Simple task อาจไม่ต้อง long-run test
- Critical task ต้องการ full verification

---

## 3. Application Guidelines

### 3.1 When to Apply Each Principle

**Communication Clarity - ใช้เมื่อ:**
- พบสิ่งผิดปกติหรือ unexpected
- รายงานสถานะที่อาจสับสน
- มี ambiguity ใน message

**Verification Honesty - ใช้เมื่อ:**
- Claim ว่าบางสิ่ง "ทำงานได้" หรือ "แก้ไขแล้ว"
- รายงานความสำเร็จ
- สรุปผลลัพธ์

### 3.2 Context-Based Flexibility

| Context | Flexibility Level | Example |
|---------|-------------------|---------|
| Casual discussion | High | "น่าจะ work" ได้ |
| Implementation | Medium | ต้องบอก verification status |
| Production deploy | Low | ต้อง verify ก่อน claim |
| Critical system | Very Low | Full verification required |

### 3.3 Decision Framework

```
Before communicating findings/status:

1. Is context clear to the recipient?
   → No: Add context
   → Yes: Proceed

2. Could this be misunderstood?
   → Yes: Clarify impact/action
   → No: Proceed

3. Am I claiming success?
   → Yes: What's verified? State honestly
   → No: Proceed
```

---

## 4. Examples with Flexibility

### 4.1 Problem Statement (Flexible)

**Simple context (ไม่ต้อง full format):**
```
User รู้อยู่แล้วว่ากำลังทำอะไร →
"เจอ typo ตรงนี้ครับ" (ไม่ต้องบอก impact)
```

**Complex context (ต้อง full format):**
```
User อาจสับสน →
"พบว่า X ไม่มี parameter Y

Impact: [อธิบาย]
Action: [ต้องทำ/ไม่ต้องทำ]"
```

### 4.2 Success Claim (Flexible)

**Simple task:**
```
"แก้ typo แล้วครับ" (ไม่ต้อง verification status)
```

**Complex task:**
```
"Implementation เสร็จแล้ว

Status:
- [x] Code done
- [x] Syntax OK
- [ ] Production test

รอ verify ก่อน confirm ว่า fixed"
```

---

## 5. Anti-Patterns to Avoid

| Anti-Pattern | Why Bad | Better Approach |
|--------------|---------|-----------------|
| "มีปัญหา!" แล้วหยุด | User ต้องถามต่อ | บอก impact + action ด้วย |
| "Fixed!" ก่อน test | User คิดว่าเสร็จ | บอก verification status |
| Over-explaining simple things | Waste time | ใช้วิจารณญาณ |
| Rigid format ทุกครั้ง | Annoying | Flexible by context |

---

## 6. Summary: Smart Rules, Not Rigid Rules

| Aspect | Rigid Rule (❌) | Smart Principle (✅) |
|--------|-----------------|---------------------|
| Format | ต้องใช้ format X ทุกครั้ง | ใช้ format ที่เหมาะกับ context |
| Verification | ต้อง test ทุก level | Test ตามความ critical |
| Detail | ต้องบอกทุก element | บอกเท่าที่จำเป็น |
| Flexibility | ไม่มี | มี based on context |

**Core Message:**

> **สื่อสารให้ผู้รับเข้าใจครบถ้วน + อ้างสิ่งที่พิสูจน์ได้**
>
> ใช้วิจารณญาณตาม context ไม่ใช่ follow format อย่างเดียว

---

## 7. Version History

| Version | Date | Changes | Session |
|---------|------|---------|---------|
| 1.1 | 2026-02-06 | Redesign as flexible principles | (current) |
| 1.0 | 2026-02-06 | Initial design - too rigid | (current) |

---

> **Full history:** [changelog/accurate-communication.changelog.md](../changelog/accurate-communication.changelog.md)
