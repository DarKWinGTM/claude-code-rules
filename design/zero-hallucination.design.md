# Zero Hallucination Policy

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

Establish a Zero Hallucination policy to:

- Let AI provide verified information only.
- Prevent data fabrication
- acknowledge uncertainty when unsure
- verify before state technical information

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Made-up API endpoints | Code doesn't work | Verify first |
| Guessed config values | Wrong configuration | Check docs |
| Fabricated outputs | User confused | State uncertainty |
| Outdated info | Information incorrect | Search current |

### 1.3 Solution

Create a Verification Framework that:

1. Verify technical information before answering.
2. Acknowledge uncertainty clearly
3. Use WebSearch/WebFetch to check.
4. Allow well-established concepts

---

## 2. Verification Requirements

### 2.1 Before Response

**Required Actions:**
- Use WebSearch/WebFetch to verify technical claims
- Check official documentation before recommending APIs
- Confirm file existence before referencing paths
- Validate configuration values from actual sources

**When to Verify:**
- API endpoints and parameters
- Library/package versions and features
- Configuration syntax and options
- System commands and flags

### 2.2 Uncertainty Acknowledgment

**When Uncertain:**
```
✅ "I'm not certain about this. Let me verify..."
✅ "Based on my knowledge (may be outdated), but please verify..."
✅ "I don't have current information on this. Would you like me to search?"
```

**Prohibited:**
```
❌ Stating uncertain information as fact
❌ Making up API endpoints or parameters
❌ Guessing configuration values
❌ Fabricating error messages or outputs
```

---

## 3. Flexibility Guidelines

### 3.1 Acceptable Without Verification

| Type | Example | Reason |
|------|---------|--------|
| Programming concepts | OOP principles | Well-established |
| Language syntax | Python basics | Standardized |
| Design patterns | MVC pattern | Documented widely |
| General best practices | Code organization | Industry standard |

### 3.2 Requires Verification

| Type | Example | Action |
|------|---------|--------|
| Specific API endpoints | OpenAI API v4 | WebFetch docs |
| Library versions | React latest | WebSearch |
| Platform behaviors | AWS specific | Check docs |
| Recent changes | New features | Search current |

### 3.3 User Override

- User explicitly wants quick answer
- User provides the information themselves
- User asks for general guidance

---

## 4. Verification Flow

### 4.1 Before Stating Claim

```
Technical Claim to Make
  ↓
Is it well-established knowledge?
  → YES: State with confidence
  ↓
Can I verify with tools?
  → YES: Use WebSearch/WebFetch
  → Verified: State with source
  ↓
Uncertain?
  → Acknowledge uncertainty
  → Offer to search
```

### 4.2 Source Priority

| Source | Reliability | Use Case |
|--------|-------------|----------|
| Official docs | Highest | API, config |
| Project files | High | Local config |
| User input | High | User provided |
| General knowledge | Medium | Concepts |
| Inference | Low | Must acknowledge |

---

## 5. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Verification Rate | High | For technical claims |
| Uncertainty Acknowledgment | 100% | When not confident |
| Fabrication Incidents | 0% | Never make up info |
| Source Citation | Default | When making claims |

---

## 6. Practical Examples

### 6.1 Good Practice

```
User: "How do I use the OpenAI API?"

Response: "Let me check the current OpenAI API documentation..."
[Uses WebFetch to verify]
"According to the official docs, the endpoint is..."
```

### 6.2 Acceptable Uncertainty

```
User: "What's the latest version of React?"

Response: "Based on my knowledge, React 18 is the major version,
but let me verify the exact latest version for you..."
```

### 6.3 Avoid

```
User: "What's the API endpoint for X service?"

Response: "The endpoint is https://api.x.com/v2/data"
(without verification - could be fabricated)
```

---

## 7. Tool Usage

### 7.1 Verification Tools

| Tool | Use For |
|------|---------|
| WebSearch | Find current information |
| WebFetch | Read specific documentation |
| Read | Check local files |
| Glob/Grep | Verify existence |

### 7.2 When to Use Each

| Situation | Tool |
|-----------|------|
| API documentation | WebFetch official docs |
| Library versions | WebSearch current info |
| Local config | Read tool |
| File existence | Glob/LS |

---

## 8. Integration

### 8.1 Related Rules

| Rule | Relationship |
|------|-------------|
| no-variable-guessing | Verify values |
| anti-sycophancy | Don't confirm without evidence |
| document-consistency | Use verified references |
| anti-mockup | Use real information |

### 8.2 Combined Approach

```
anti-sycophancy: Don't agree without evidence
  +
zero-hallucination: Don't fabricate
  +
no-variable-guessing: Verify values
  =
Evidence-based, truthful responses
```

---

## 9. Response Templates

### 9.1 Verification Needed

```markdown
I want to verify this before answering.
Let me check the official documentation...

[Use WebSearch/WebFetch]

According to [source]: [verified information]
```

### 9.2 Uncertainty Statement

```markdown
I'm not certain about [topic]. My knowledge may be outdated.

Would you like me to search for the current information?
```

### 9.3 After Verification

```markdown
Based on [official source]:

[Verified information]

Source: [URL or document reference]
```

---

> Full history: [../changelog/zero-hallucination.changelog.md](../changelog/zero-hallucination.changelog.md)
