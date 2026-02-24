# Accurate Communication Standard Design

> **Version:** 1.1
> **Date:** 2026-02-06
> **Purpose:** Standardize clear and accurate communication with flexibility
> **Status:** 🟡 **IN PROGRESS** - Design Phase

---

## 0. Document Control

> **Parent Scope:** Claude Code Rules - Communication Standards
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## 1. Problem Statement

### 1.1 Background

During work found Communication patterns that confuse users:

| Pattern | Example | Problem |
|---------|---------|---------|
| Vague problem statement | "There's a problem!" (not explained) | User doesn't know what to do |
| Premature success claim | "Fixed!" (no test) | User thinks it's finished |

### 1.2 Design Philosophy

**Need rules:**
- ✅ Smart and flexible
- ✅ Can be used in many contexts.
- ✅ There are supporting principles (principles, not rigid rules)
- ❌ It's not a fixed/stupid rule.

---

## 2. Core Principles

### 2.1 The Communication Clarity Principle

> **"The receiver must understand the context completely from a single message"**

**Principles:** Every message sent must provide the recipient:
1. **Understand the situation** - What happened?
2. **Assess the impact** - How important is it?
3. **Know what you have to do** - action required or not?

**resilient:**
- It is not necessary to have every element every time.
- Use judgment according to context
- If the context is already clear, you can skip it.

### 2.2 The Verification Honesty Principle

> **"Claim only things that can be proven"**

**Principle:** Claim must match verification level:

| Verified Level | Can speak |
|----------------|-------------|
| Haven't done it yet | "Will do X" |
| Already done, not yet tested | "Already done, waiting to verify" |
| Test partially passed | "X passed, Y waited" |
| Test fully passed | "Can work" |
| Stable over time | "Fixed" |

**resilient:**
- Different context, different verification level.
- Simple task may not require long-run testing.
- Critical task requires full verification.

---

## 3. Application Guidelines

### 3.1 When to Apply Each Principle

**Communication Clarity - Use when:**
- Found something unusual or unexpected
- Report potentially confusing status
- There is ambiguity in the message.

**Verification Honesty - Use when:**
- Claim that something "works" or is "fixed"
- Success report
- Summary of results

### 3.2 Context-Based Flexibility

| Context | Flexibility Level | Example |
|---------|-------------------|---------|
| Casual discussion | High | "Probably works" |
| Implementation | Medium | Must tell verification status |
| Production deploy | Low | Must verify before claiming |
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

**Simple context (no need for full format):**
```
User already knows what they are doing →
"Found a typo here" (no need to say impact)
```

**Complex context (must be full format):**
```
User may be confused →
"It was found that X does not have parameter Y

Impact: [Explain]
Action: [Must do/Don't do]"
```

### 4.2 Success Claim (Flexible)

**Simple task:**
```
"The typo has been fixed" (no verification status required)
```

**Complex task:**
```
"Implementation finished.

Status:
- [x] Code done
- [x] Syntax OK
- [ ] Production test

Wait for verification before confirming that it is fixed"
```

---

## 5. Anti-Patterns to Avoid

| Anti-Pattern | Why Bad | Better Approach |
|--------------|---------|-----------------|
| "There's a problem!" then stops | User must continue asking | Tell impact + action as well |
| "Fixed!" before testing | User thinks it's finished | Tells verification status |
| Over-explaining simple things | Waste time | Use good judgment |
| Rigid format every time | Annoying | Flexible by context |

---

## 6. Summary: Smart Rules, Not Rigid Rules

| Aspect | Rigid Rule (❌) | Smart Principle (✅) |
|--------|-----------------|---------------------|
| Format | Must use format X every time | Use the format that suits the context |
| Verification | Must test every level | Test according to criticality |
| Detail | Must tell every element | Tell as much as necessary |
| Flexibility | None | Yes based on context |

**Core Message:**

> **Communicate so that the recipient understands completely + claim things that can be proven**
>
> Use your judgment according to the context, not just follow the format.

---

## 7. Version History

| Version | Date | Changes | Session |
|---------|------|---------|---------|
| 1.1 | 2026-02-06 | Redesign as flexible principles | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| 1.0 | 2026-02-06 | Initial design - too rigid | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |

---

> **Full history:** [changelog/accurate-communication.changelog.md](../changelog/accurate-communication.changelog.md)
