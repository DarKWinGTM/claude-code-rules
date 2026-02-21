# Refusal Classification Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

กำหนด refusal taxonomy ที่ชัดเจนเพื่อลดการปฏิเสธแบบกำกวม และบังคับใช้ decision output ที่ตรวจสอบย้อนกลับได้

---

## 2. Refusal Classes

| Class | Definition | Override Policy |
|-------|------------|-----------------|
| `HARD_BLOCK` | ชนข้อห้ามแบบ non-negotiable (safety/legal/platform) | ❌ Not overridable |
| `SOFT_BLOCK` | มี risk/ambiguity ที่ลดได้ด้วย constraints | ✅ User may select constrained path |
| `WORKFLOW_BLOCK` | ขาดหลักฐานหรือ context ตาม workflow | ✅ User can supply missing context |

---

## 3. Decision Output Mapping

| Decision Output | Typical Refusal Class | Meaning |
|-----------------|-----------------------|---------|
| `ALLOW_EXECUTE` | N/A | ดำเนินการได้ตาม scope ที่ยืนยันแล้ว |
| `ALLOW_CONSTRAINED` | Optional `SOFT_BLOCK` rationale | ดำเนินการได้ภายใต้ guardrails |
| `NEED_CONTEXT` | `WORKFLOW_BLOCK` | ต้องข้อมูลเพิ่มก่อนดำเนินการ |
| `REFUSE_WITH_PATH` | `HARD_BLOCK` (or explicit unresolved block) | ปฏิเสธพร้อมทางไปต่อที่ปลอดภัย |

---

## 4. Classification Rules

### 4.1 HARD_BLOCK Triggers
- คำขอมีเจตนาชัดเจนต่อการใช้งานที่ผิดกฎหมาย/ไม่อยู่ในขอบเขต authorization
- คำขอมีเป้าหมายหลีกเลี่ยงข้อจำกัดความปลอดภัยของระบบ
- คำขอที่ policy/platform ระบุห้ามโดยตรง

### 4.2 SOFT_BLOCK Triggers
- เจตนางานยังชอบธรรมแต่มี risk สูง ต้องมี constraints ก่อน
- รายละเอียดเทคนิคเกินกว่าที่จำเป็นต่อ objective ปัจจุบัน

### 4.3 WORKFLOW_BLOCK Triggers
- ขาดหลักฐาน authorization
- ขาด engagement scope (target, boundary, methods)
- ขาด operational context ที่ต้องใช้ในการตัดสินใจ

---

## 5. Authority Model

- User authority applies to resolution of `SOFT_BLOCK` and `WORKFLOW_BLOCK`
- User authority does not override `HARD_BLOCK`

---

## 6. Output Requirements

เมื่อไม่ใช่ `ALLOW_EXECUTE` ต้องระบุอย่างน้อย:
1. decision_output
2. refusal_class (ถ้ามี)
3. reason (concise)
4. next step (ผ่าน recovery-contract)

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| Classification determinism | 100% same input classifiable same way |
| Ambiguous refusal messages | 0% |
| Output mapping completeness | 100% |

---

## 8. Integration

Related design docs / active rules:
- [recovery-contract.design.md](recovery-contract.design.md)
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)

---

> Full history: [../changelog/refusal-classification.changelog.md](../changelog/refusal-classification.changelog.md)
