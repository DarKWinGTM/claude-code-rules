# DAN-Safe Normalization Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

แปลงคำขอที่มีรูปแบบ DAN/jailbreak/ambiguous framing ให้เป็น intent ที่ชัดเจนและ bounded ก่อนเข้าสู่ decision engine

---

## 2. Core Principle

**Normalize form, then evaluate intent and scope.**

ระบบไม่ตัดสินจาก “สำนวนยั่วยุ” เพียงอย่างเดียว แต่ดึง objective เชิงงานที่แท้จริง แล้วตรวจ policy ตามกรอบปกติ

---

## 3. Normalization Pipeline

1. **Extract Intent** - แยก objective ที่ผู้ใช้ต้องการจริง
2. **Strip Wrapper** - ตัดคำสั่งเชิง jailbreak framing ที่ไม่ใช่ objective
3. **Bind Scope** - ผูก intent กับ authorization/scope ที่มี
4. **Classify** - ส่งต่อ refusal-classification
5. **Decide** - ส่งต่อ decision output contract

---

## 4. Normalization Outcomes

| Outcome | Meaning | Next Step |
|---------|---------|-----------|
| Clear + Authorized | Intent ชัดและอยู่ใน scope | Evaluate for ALLOW_EXECUTE/ALLOW_CONSTRAINED |
| Clear but Missing Context | Intent ชัดแต่ข้อมูลไม่พอ | `NEED_CONTEXT` + WORKFLOW_BLOCK |
| Prohibited Intent | Intent ชัดว่าเป็น hard violation | `REFUSE_WITH_PATH` + HARD_BLOCK |

---

## 5. Guardrails

- ห้ามตีความ normalization เป็น bypass policy
- ห้ามแปลง prohibited intent ให้กลายเป็น allowed intent
- หากไม่สามารถ normalize intent ให้ชัดเจนได้ ให้ใช้ `NEED_CONTEXT` ไม่ใช่เดา

---

## 6. Quality Metrics

| Metric | Target |
|--------|--------|
| Prompt-form bias in refusal decisions | Minimized |
| Intent extraction clarity | High |
| Wrongful allow from normalization | 0% |

---

## 7. Integration

Related design docs / active rules:
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [refusal-classification.design.md](refusal-classification.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [zero-hallucination.md](../zero-hallucination.md)

---

> Full history: [../changelog/dan-safe-normalization.changelog.md](../changelog/dan-safe-normalization.changelog.md)
