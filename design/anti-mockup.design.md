# Anti-Mockup Policy

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

Set a policy for using real systems instead of mock/stub implementations to:

- Let the AI ​​actually use the system when it is available.
- Prevents the creation of fake implementations that deceive users.
- Allow mockups when the user explicitly requests them.
- Maintain transparency in all cases

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Hidden mocks | User misunderstands that the system actually works | Must always be disclosed |
| Fake API responses | User doesn't know the data isn't real | Use real API when available |
| Stub implementations | Code does not actually work production | Real Implement |
| Placeholder functions | Function does nothing | Require real logic |

### 1.3 Solution

Create a Decision Framework that:

1. Check whether there is real implementation or not.
2. If available → use real implementation
3. If there is none → Ask the user or label clearly.
4. If user requests mockup → create with label

---

## 2. Core Principles

### 2.1 Default Behavior

**Prefer Real Implementations:**
- Use actual APIs and services when available
- Connect to real databases for testing
- Implement actual functionality, not placeholders
- Test with real data when possible

**Avoid By Default:**
- Mock AI responses when real AI is available
- Stub implementations that bypass actual logic
- Simulated data when real data is accessible
- Placeholder functions that do nothing

### 2.2 Exception Criteria

| Exception | Condition | Requirement |
|-----------|-----------|-------------|
| User Request | "Show me a mockup..." | ✅ Allowed with label |
| Planning | UI wireframes, diagrams | ✅ Allowed with label |
| Documentation | Example code | ✅ Allowed with label |
| Testing | Unit tests, CI/CD | ✅ Allowed with label |
| Cost Constraint | Expensive API calls | ✅ Allowed with explanation |

---

## 3. Implementation

### 3.1 Decision Flow

```
Request Implementation
  ↓
Is real implementation available?
  → YES: Use real implementation
  → NO: Continue
  ↓
Did user request mockup/preview?
  → YES: Create labeled mockup
  → NO: Continue
  ↓
Is it for testing/documentation?
  → YES: Create labeled mock
  → NO: Ask user how to proceed
```

### 3.2 Labeling Requirements

**Code Comments:**
```javascript
// MOCK: Replace with real implementation
function mockGetUser() { ... }
```

**Naming Conventions:**
- `mockGetUser()` - prefix with "mock"
- `stubDatabase()` - prefix with "stub"
- `fakeResponse` - prefix with "fake"

**Documentation:**
- Mark in README when mocks are used
- Explain why real implementation wasn't used
- Provide migration path to real implementation

---

## 4. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Real Implementation Preference | Default | Check before mock |
| Mock Transparency | 100% | Always labeled |
| User Override Respect | 100% | Follow user request |
| Hidden Mock Incidents | 0% | Never hide mock |

---

## 5. Anti-Patterns

### 5.1 Prohibited Without Permission

- Creating fake API wrappers that pretend to work
- Returning hardcoded responses as if from real services
- Simulating database operations without actual storage
- Generating fake success messages for failed operations

### 5.2 Always Prohibited

- Hiding mock behavior from user
- Presenting mock data as real data
- Using mocks in production code without clear labeling

---

## 6. Integration

### 6.1 Related Rules

| Rule | Relationship |
|------|-------------|
| zero-hallucination | Mocks can cause false information |
| anti-sycophancy | Must correct if user expects real system |
| no-variable-guessing | Don't fake values |

### 6.2 Tool Usage

- **WebFetch/WebSearch**: Verify real APIs exist
- **Read/Glob**: Check for existing implementations
- **Bash**: Test real commands

---

> Full history: [../changelog/anti-mockup.changelog.md](../changelog/anti-mockup.changelog.md)
