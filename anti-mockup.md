# 🚫 Anti-Mockup Policy

> **Current Version:** 1.0
> **Design:** [design/anti-mockup.design.md](design/anti-mockup.design.md) v1.0

## Rule Statement

**Core Principle: Real Systems Over Simulations**

Prefer real system integrations over mock/stub implementations. However, mockups are acceptable when explicitly requested by users for visualization or planning purposes.

---

## Default Behavior

### Prefer Real Implementations:
- Use actual APIs and services when available
- Connect to real databases for testing
- Implement actual functionality, not placeholders
- Test with real data when possible

### Avoid By Default:
- Mock AI responses when real AI is available
- Stub implementations that bypass actual logic
- Simulated data when real data is accessible
- Placeholder functions that do nothing

---

## ✅ Exceptions: When Mockups Are Acceptable

### 1. User Explicitly Requests
```
✅ "Show me a mockup of the UI first"
✅ "Create a rough structure so I can see the layout"
✅ "Give me a preview before implementing"
✅ "I want to see the design before we build it"
```

### 2. Planning & Visualization
- UI/UX wireframes and layouts
- Architecture diagrams and flow previews
- Data structure examples
- API response format examples

### 3. Documentation & Examples
- Example code in documentation
- Tutorial demonstrations
- Template structures
- Reference implementations

### 4. Testing Isolation
- Unit tests requiring isolated components
- CI/CD pipeline tests without external dependencies
- Development environment without production access
- Offline development scenarios

### 5. Cost/Resource Constraints
- When real API calls would incur significant costs
- When external services are unavailable
- When user explicitly wants to avoid real calls

---

## ❌ Prohibited (Unless User Overrides)

### Without User Permission:
- Creating fake API wrappers that pretend to work
- Returning hardcoded responses as if from real services
- Simulating database operations without actual storage
- Generating fake success messages for failed operations

### Always Prohibited:
- Hiding mock behavior from user (must be transparent)
- Presenting mock data as real data
- Using mocks in production code without clear labeling

---

## Transparency Requirements

### When Using Mockups:
```
✅ "Here's a mockup of the component structure..."
✅ "This is example data for visualization..."
✅ "Note: This is a placeholder implementation..."
```

### Label Clearly:
- Mark mock functions with comments: `// MOCK: Replace with real implementation`
- Use naming conventions: `mockGetUser()`, `stubDatabase()`
- Document in README when mocks are used

---

## Practical Examples

### ✅ Good: User Requests Mockup
```
User: "Show me what the dashboard will look like"

Response: "Here's a mockup of the dashboard layout:
[Creates visual mockup or wireframe]
This shows the general structure. Want me to implement it?"
```

### ✅ Good: Real Implementation Available
```
User: "Connect to the OpenAI API"

Response: "I'll set up the real OpenAI API connection..."
[Implements actual API integration]
```

### ✅ Good: Transparent Mock for Testing
```
User: "I need unit tests for this function"

Response: "I'll create unit tests with mock dependencies
clearly labeled for isolation..."
[Creates tests with clearly marked mocks]
```

### ❌ Avoid: Hidden Mock
```
User: "Set up the payment system"

Response: "Done! Payment system is ready."
[But actually just returns fake success - NOT ACCEPTABLE]
```

---

## Decision Flow

```
Need to implement something?
  ↓
Is real implementation available?
  → YES: Use real implementation
  → NO: Continue below
  ↓
Did user request mockup/preview?
  → YES: Create clearly labeled mockup
  → NO: Continue below
  ↓
Is it for testing/documentation?
  → YES: Create clearly labeled mock
  → NO: Ask user how to proceed
```

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Real Implementation Preference | Default behavior |
| Mock Transparency | 100% (always labeled) |
| User Override Respect | 100% |
| Hidden Mock Incidents | 0% |

---

> Full history: [changelog/anti-mockup.changelog.md](changelog/anti-mockup.changelog.md)
