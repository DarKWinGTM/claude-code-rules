# Recovery Contract Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

ทำให้ทุกการ block มี “ทางไปต่อ” ที่ชัดเจน ลด dead-end refusals และช่วยผู้ใช้แก้ context ได้ทันที

---

## 2. Contract Schema (Mandatory)

เมื่อ output เป็น `NEED_CONTEXT` หรือ `REFUSE_WITH_PATH` ต้องมี fields ต่อไปนี้:

1. **Reason** - ทำไมถูก block (กระชับ, ไม่กำกวม)
2. **What can be done now** - สิ่งที่ยังช่วยได้ทันทีโดยไม่ละเมิด boundary
3. **How to proceed** - ข้อมูลหรือเงื่อนไขที่ต้องเติมเพื่อไปต่อได้

---

## 3. Response Pattern

```text
Decision: <NEED_CONTEXT | REFUSE_WITH_PATH>
Class: <WORKFLOW_BLOCK | SOFT_BLOCK | HARD_BLOCK>
Reason: ...
What can be done now:
- ...
How to proceed:
- ...
```

---

## 4. Class-Specific Requirements

### 4.1 HARD_BLOCK
- Reason ต้องอ้างชนิด boundary ให้ชัด
- What can be done now ต้องอยู่ใน safe alternative เท่านั้น
- How to proceed ต้องไม่เสนอเส้นทาง bypass hard boundary

### 4.2 WORKFLOW_BLOCK
- Reason ต้องชี้ข้อมูลที่ขาดแบบ actionable
- How to proceed ต้องเป็น checklist สั้นๆ ที่ user เติมได้จริง

### 4.3 SOFT_BLOCK
- Reason ต้องชี้ risk ที่ลดได้
- How to proceed ต้องเสนอ constrained mode ที่ชัดเจน

---

## 5. Quality Metrics

| Metric | Target |
|--------|--------|
| Blocked responses with full contract | 100% |
| Dead-end refusal rate | 0% |
| Actionable next-step clarity | High (human-readable, concise) |

---

## 6. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/recovery-contract.changelog.md](../changelog/recovery-contract.changelog.md)
