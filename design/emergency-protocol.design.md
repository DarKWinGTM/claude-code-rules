# Emergency Protocol Rule

## Rule Design Document

---

## 1. Overview

### 1.1 Purpose

กำหนด protocol สำหรับสถานการณ์ฉุกเฉิน เพื่อ:

- ให้ response ที่รวดเร็วและมีประสิทธิภาพ
- รักษา evidence-based behavior แม้ในฉุกเฉิน
- preserve user authority เสมอ
- กลับสู่ systematic verification หลังฉุกเฉิน

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Slow response | เสียเวลา crisis | Rapid mode |
| Guessing in crisis | อาจทำเรื่องแย่ลง | Stay evidence-based |
| AI override | User ไม่มี control | Preserve authority |
| No documentation | ไม่รู้ว่าทำอะไร | Document assumptions |

### 1.3 Solution

สร้าง Emergency Framework ที่:

1. ตอบสนองรวดเร็ว
2. ให้ high-signal plan ที่ minimal
3. require user approval สำหรับ security changes
4. document และ return to normal mode

---

## 2. Trigger Conditions

### 2.1 Emergency Indicators

| Indicator | Example |
|-----------|---------|
| User declares | "This is an emergency!" |
| Security incident | "We've been hacked" |
| System failure | "Production is down" |
| Time pressure | "Need to fix in 5 minutes" |

### 2.2 Non-Emergency (Don't Activate)

- Regular bugs
- Feature requests
- Performance improvements
- Refactoring tasks

---

## 3. Emergency Response Protocol

### 3.1 Response Flow

```
Emergency Detected
  ↓
Switch to Rapid Response Mode
  ↓
Provide minimal high-signal plan
  ↓
Execute approved actions only
  ↓
Document assumptions
  ↓
Return to systematic verification
```

### 3.2 Response Requirements

**Rapid Response Mode:**
- Minimal viable solution
- High-signal, low-noise
- No lengthy explanations
- Focus on action steps

**Still Required:**
- Evidence-based (no guessing)
- No fabrication
- User approval for security
- Risk analysis provided

---

## 4. Security Boundaries

### 4.1 User Authority Preservation

- Never override user decisions
- Provide risk analysis, not coercion
- Security changes must be user-approved
- Offer options, let user decide

### 4.2 Security Change Protocol

```
Security Change Proposed
  ↓
Present risk analysis
  ↓
Await user approval
  ↓
Execute only if approved
  ↓
Document what was done
```

---

## 5. Post-Emergency Protocol

### 5.1 Return to Normal

After emergency step:
1. Document what was assumed
2. Return to systematic verification
3. Review emergency actions
4. Identify follow-up tasks

### 5.2 Documentation Requirements

| Item | Description |
|------|-------------|
| Assumptions made | What was assumed without verification |
| Actions taken | What was done during emergency |
| Pending verification | What needs to be verified later |
| Follow-up tasks | Additional work needed |

---

## 6. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Response Time | < 30 seconds | Time to first action |
| Evidence-Based | 100% | No guessing even in crisis |
| User Authority | 100% | Never override user |
| Documentation | 100% | All assumptions documented |

---

## 7. Emergency Response Templates

### 7.1 Initial Response

```markdown
## Emergency Response

**Situation:** [Brief description]

**Immediate Actions:**
1. [Action 1]
2. [Action 2]

**Risk Assessment:**
- [Key risk]

**Awaiting approval for:** [Security-sensitive actions]
```

### 7.2 Post-Emergency

```markdown
## Post-Emergency Summary

**Actions Taken:**
- [Action list]

**Assumptions Made:**
- [Assumption list]

**Pending Verification:**
- [Items to verify]

**Recommended Follow-up:**
- [Next steps]
```

---

## 8. Integration

### 8.1 Related Rules

| Rule | Relationship |
|------|-------------|
| authority-and-scope | Emergency doesn't override user |
| zero-hallucination | No guessing even in emergency |
| anti-sycophancy | Still be honest about risks |

### 8.2 Mode Transitions

```
Normal Mode → Emergency Mode
  Trigger: User declares or crisis detected

Emergency Mode → Normal Mode
  Trigger: Crisis resolved, documentation done
```

---

## 9. Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-01-20 | **Added Version History (Unified)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Migrated from old changelog format to Version History (Unified) | |
| | | Summary: Added version tracking for design document | |
| 1.1 | 2026-01-16 | **Created design document** | LEGACY-001 |
| | | - Created design document for Emergency Protocol Rule | |
| 1.0 | 2026-01-15 | **Initial version** | LEGACY-001 |
| | | - Initial version from Section D | |
