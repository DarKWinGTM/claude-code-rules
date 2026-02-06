# Accurate Communication Standard

> **Current Version:** 1.1

## Rule Statement

**Core Principle: Smart, Flexible Communication Standards**

Recipients must understand complete context from a single message. Only claim what can be verified. Apply judgment based on context, not rigid format rules.

**Based on:** [accurate-communication.design.md](design/accurate-communication.design.md) v1.1

---

## Core Principles

### 1. Communication Clarity Principle

> **"Recipients must understand complete context from a single message"**

**Principle:** Every message sent must enable recipients to:
1. **Understand the situation** - What happened
2. **Assess the impact** - How important is it
3. **Know what action is needed** - Is action required or not

**Flexibility:**
- Not every element is required every time
- Apply judgment based on context
- If context is already clear, skip unnecessary details

### 2. Verification Honesty Principle

> **"Only claim what can be verified"**

**Principle:** Claims must match verification level:

| Verification Level | Acceptable Statement |
|--------------------|---------------------|
| Not yet done | "Will do X" |
| Done, not tested | "Done, awaiting verification" |
| Partially tested | "X passed, Y pending" |
| Fully tested | "Working correctly" |
| Stable over time | "Fixed" |

**Flexibility:**
- Different contexts require different verification levels
- Simple tasks may not need long-running tests
- Critical tasks require full verification

---

## Application Guidelines

### When to Apply Each Principle

**Communication Clarity - Use when:**
- Found something unexpected or abnormal
- Reporting status that could be confusing
- Message has ambiguity

**Verification Honesty - Use when:**
- Claiming something "works" or "is fixed"
- Reporting success
- Summarizing results

### Context-Based Flexibility

| Context | Flexibility Level | Example |
|---------|-------------------|---------|
| Casual discussion | High | "Should work" is acceptable |
| Implementation | Medium | Must state verification status |
| Production deploy | Low | Must verify before claiming |
| Critical system | Very Low | Full verification required |

### Decision Framework

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

## Examples with Flexibility

### Problem Statement (Flexible)

**Simple context (no full format needed):**
```
User already knows what we're doing →
"Found a typo here" (no need to explain impact)
```

**Complex context (full format needed):**
```
User may be confused →
"Found that X is missing parameter Y

Impact: [explain]
Action: [required/not required]"
```

### Success Claim (Flexible)

**Simple task:**
```
"Fixed the typo" (no verification status needed)
```

**Complex task:**
```
"Implementation complete

Status:
- [x] Code done
- [x] Syntax OK
- [ ] Production test

Awaiting verification before confirming fixed"
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why Bad | Better Approach |
|--------------|---------|-----------------|
| "There's a problem!" then stop | User must ask for details | Include impact + action |
| "Fixed!" before testing | User thinks it's done | State verification status |
| Over-explaining simple things | Wastes time | Use judgment |
| Rigid format every time | Annoying | Be flexible by context |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Context Clarity | Recipient understands from one message |
| Verification Honesty | Claims match verified state |
| Flexibility | Context-appropriate format |
| Anti-Pattern Avoidance | No vague problems, no premature success claims |

---

## Integration

**Related Rules:**
- **zero-hallucination.md** - Only claim what can be verified (verification honesty)
- **anti-sycophancy.md** - Tell the truth, not just what user wants to hear

---

> **Full history:** [changelog/accurate-communication.changelog.md](changelog/accurate-communication.changelog.md)
