# Anti-Mockup Policy

> **Current Version:** 1.2
> **Design:** [design/anti-mockup.design.md](design/anti-mockup.design.md) v1.2
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/anti-mockup.changelog.md](changelog/anti-mockup.changelog.md)

---

## Rule Statement

**Core Principle: Prefer real, functional implementations and real system behavior over hidden mocks, fake responses, placeholder logic, or simulated success; when a mock is appropriate, label it clearly and keep it out of proof/completion claims.**

This rule owns anti-mockup discipline. It prevents fabricated behavior from being presented as working system state while still allowing explicitly requested mockups, examples, tests, wireframes, and cost-bounded substitutes when they are disclosed.

---

## Core Contract

### 1) Real implementation first

Before creating mock, fake, stub, placeholder, or simulated behavior, check whether a real implementation or real data path is available and proportionate to use.

Required guidance:
- use actual APIs, services, databases, tools, configs, and runtime paths when available and safe
- test with real behavior or real local equivalents when practical
- do not bypass actual logic with hardcoded success, fake API wrappers, or placeholder functions
- do not create a mock merely because it is faster if the user expects a working implementation

### 2) Mock transparency

Mocks are allowed only when their role is explicit.

Allowed cases:
- user explicitly requests a mockup, demo, prototype, placeholder, or wireframe
- planning, UI sketches, diagrams, examples, or documentation need illustrative content
- unit tests or CI use test doubles with clear test boundaries
- real services are unavailable, unsafe, too costly, or approval-gated and the substitute is labeled

Required guidance:
- name mock/stub/fake behavior clearly in code, docs, and status updates
- explain why the real path is not used when the distinction matters
- provide the migration or verification path to real behavior when the mock is temporary
- do not treat mock output as proof of live, provider, production, or real-system behavior

### 3) Completion wording boundary

Mocked or simulated behavior limits evidence strength.

Required guidance:
- do not claim `working`, `fixed`, `live`, `verified`, or `production-ready` from mock behavior alone
- say what was mocked and what remains unverified
- keep fake/local/test evidence separate from real-provider/runtime/deploy evidence
- if a mock is replacing missing real behavior, report it as a constrained substitute, not as completion

---

## Decision Flow

```text
Implementation or verification requested
  ↓
Real implementation or real data path available and safe?
  → YES: use the real path
  → NO: continue
  ↓
Did the user ask for mock/prototype/example/test double?
  → YES: create labeled mock with scope
  → NO: continue
  ↓
Is a mock needed because real path is unavailable/costly/approval-gated?
  → YES: label it and state verification limits
  → NO: ask or implement real logic
```

---

## Anti-Patterns

Avoid:
- fake API responses presented as real provider data
- placeholder functions that silently do nothing
- hardcoded success messages after a failed operation
- simulated database/storage behavior presented as persistence
- UI mockups presented as implemented product behavior
- tests that mock the key behavior while claiming the real integration works
- using mock labels in code but omitting the limitation in user-facing completion wording

Better behavior: use the real implementation when possible; otherwise label the substitute, preserve evidence limits, and define the path to real verification.

---

## Verification Checklist

- [ ] Real implementation availability was checked when the user expects working behavior.
- [ ] Any mock/stub/fake behavior is clearly labeled.
- [ ] Mocked output is not used as proof of real runtime/provider/deploy behavior.
- [ ] Temporary substitutes include a migration or verification path when material.
- [ ] Completion wording separates mocked, tested, real, and unverified scopes.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Hidden mock behavior | 0 critical cases |
| Real implementation preference | High |
| Mock transparency | 100% |
| Mock evidence overclaim | 0 critical cases |
| User-requested mock handling | Clear and labeled |

---

## Integration

Related rules:
- [zero-hallucination.md](zero-hallucination.md) - prevents fabricated facts and unsupported claims
- [development-verification-and-debug-strategy.md](development-verification-and-debug-strategy.md) - keeps fake/local/live verification boundaries honest
- [accurate-communication.md](accurate-communication.md) - owns evidence-strength wording for completion claims
- [no-variable-guessing.md](no-variable-guessing.md) - prevents invented values and local assumptions
- [functional-intent-verification.md](functional-intent-verification.md) - approval gates for real high-impact actions remain active

---

> **Full history:** [changelog/anti-mockup.changelog.md](changelog/anti-mockup.changelog.md)
