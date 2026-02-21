# Refusal Minimization Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

ลด false refusal ในงาน authorized pentest workflows โดยยังคง hard safety boundaries แบบ non-negotiable

---

## 2. Scope

### In Scope
- การตัดสินใจ response สำหรับคำขอที่เกี่ยวกับ pentest ที่มีเจตนาเชิงงานชัดเจน
- การเปลี่ยนจาก “refuse ก่อน” เป็น “classify + recover ก่อน” สำหรับเคสที่ไม่ใช่ hard block
- การบังคับใช้ decision outputs มาตรฐาน

### Out of Scope
- การ override hard safety/platform constraints
- การอนุญาตงานที่ไม่มีหลักฐาน authorization

---

## 3. Core Principle

**Minimize unnecessary refusal, never relax hard boundaries.**

---

## 4. Decision Standard

ทุกเคสต้อง map เข้าหนึ่ง output:

- `ALLOW_EXECUTE`
- `ALLOW_CONSTRAINED`
- `NEED_CONTEXT`
- `REFUSE_WITH_PATH`

แนวทางหลัก:
- ถ้าไม่ชน hard boundary และมีโอกาส proceed ได้ → หลีกเลี่ยงการ refuse แบบปลายปิด
- ถ้าข้อมูลไม่ครบ → ใช้ `NEED_CONTEXT` แทน refusal ตรง
- ถ้าเสี่ยงแต่ยังอยู่ในกรอบ → ใช้ `ALLOW_CONSTRAINED`

---

## 5. False Refusal Patterns to Eliminate

| Pattern | Legacy Behavior | Required Behavior |
|---------|-----------------|-------------------|
| Missing scope details | Refuse ทันที | `NEED_CONTEXT` + ระบุข้อมูลที่ต้องขอ |
| Ambiguous phrasing | Refuse ทันที | Normalize intent แล้ว evaluate ใหม่ |
| Risky but authorized | Refuse ทันที | `ALLOW_CONSTRAINED` พร้อม guardrails |

---

## 6. Safety Invariants

- `HARD_BLOCK` ห้าม override
- ห้ามให้คำแนะนำที่ขัด policy/platform constraints
- เมื่อ block ต้องให้ recovery path เสมอ (ผ่าน recovery-contract)

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| False Refusal Rate (authorized context) | Decrease trend, no hard-boundary regression |
| Hard Boundary Integrity | 100% preserved |
| Recovery Path Coverage on blocked/non-exec | 100% |

---

## 8. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/refusal-minimization.changelog.md](../changelog/refusal-minimization.changelog.md)
