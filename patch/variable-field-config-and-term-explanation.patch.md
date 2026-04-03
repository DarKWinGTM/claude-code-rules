# Variable, Field, Config, and Internal-Term Explanation Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.6
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that stops RULES from treating raw identifiers as if their names alone already explained the system.

Why this change matters:
- explanation-heavy answers can still become hard to follow when they rely on variables, fields, config keys, enum-like values, or internal labels without first explaining what those identifiers mean
- the existing communication/explanation/presentation owner trio already supports human-language glosses, layered reasoning, and compact structures, but it did not yet state explicitly that identifier-heavy answers must explain role, flow position, and value meaning
- the user-facing problem is not only terminology difficulty; it is that the reader is forced to decode internal names and value semantics mid-argument instead of receiving a short explanation block first

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../accurate-communication.md`
- `../explanation-quality.md`
- `../answer-presentation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement should improve human readability for identifier-heavy explanations without forcing giant glossary blocks into simple answers or weakening the checked-scope / evidence boundary for identifier meaning

---

## 3) Change Items

### Change Item 1
- **Target location:** `accurate-communication` wording owner
- **Change type:** additive

**Before**
```text
The chain required human-language glosses for internal or technical terms, but it did not yet say explicitly that variable names, field names, config keys, enum-like values, or internal labels must be unpacked when the explanation depends on them.
```

**After**
```text
The chain now requires identifier-heavy answers to explain:
- what the identifier is
- what role it plays
- where it sits in the flow when sequence matters
- what important values or states mean
```

### Change Item 2
- **Target location:** `explanation-quality` explanation-flow owner
- **Change type:** additive

**Before**
```text
The chain already supported plain-language paraphrases and layered explanation, but it did not yet provide an explicit explanation pattern for variable-heavy reasoning.
```

**After**
```text
The chain now adds a reusable explanation pattern for identifier-heavy walkthroughs:
1. explain what the identifier is
2. explain what job it does
3. explain where it sits in the flow
4. explain what important values mean
5. then continue into the deeper reasoning path
```

### Change Item 3
- **Target location:** `answer-presentation` presentation-layer owner
- **Change type:** additive

**Before**
```text
The chain already supported compact snapshots, grouped scope blocks, and comparison tables, but it did not yet expose a dedicated pattern for explaining multiple identifiers before deeper reasoning.
```

**After**
```text
The chain now adds a `Variable-Role Pattern` and a canonical compact variable-role shape so identifier-heavy answers can use a short glossary block, grouped bullets, or a small table before the deeper reasoning.
```

### Change Item 4
- **Target location:** master RULES governance surfaces and runtime install state
- **Change type:** additive

**Before**
```text
Master design, README, TODO, changelog, and phase artifacts did not yet record the bounded identifier-explanation refinement wave.
```

**After**
```text
Master governance surfaces now record the refinement wave, and the touched runtime rules are reinstalled into ~/.claude/rules so runtime behavior matches source authority.
```

---

## 4) Verification

- [ ] `accurate-communication` explicitly treats variable names, field names, config keys, enum-like values, and internal labels as clarification-required when the answer depends on them
- [ ] `explanation-quality` provides a reusable explanation-flow pattern for identifier-heavy walkthroughs
- [ ] `answer-presentation` provides a compact glossary / variable-role presentation pattern without forcing it into simple answers
- [ ] master design/README/TODO/changelog/phase surfaces record the new bounded refinement wave
- [ ] touched runtime rules are reinstalled and parity-checked against source

---

## 5) Rollback Approach

If the refinement proves too broad:
- keep the identifier-clarification rule in `accurate-communication` as the wording owner
- narrow the explanation/presentation support patterns so they remain optional helpers rather than reading like mandatory heavy structure
- preserve the patch and phase history rather than silently erasing the refinement wave
- do not revert to treating raw identifiers as if their names alone were sufficient explanation
