# File Disposal Authority and Delete Guard Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md) v2.4
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that closes one repeated RULES failure pattern:
- the assistant sees a new/untracked file
- cleanup/hygiene logic gets overread as disposal authority
- git working state is treated like semantic truth
- isolation rationale gets used like deletion authorization
- master surfaces and governed history are skipped before a removal conclusion

Why this matters:
- this repository already uses master surfaces and governed history as semantic authority
- the current rules already contain most of the needed owner domains, but the handoff between them was too weak
- the fix should tighten existing owners rather than creating a new first-class doctrine chain

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../authority-and-scope.md`
- `../project-documentation-standards.md`
- `../strict-file-hygiene.md`
- `../artifact-initiation-control.md`
- `../functional-intent-verification.md`
- `../evidence-grounded-burden-of-proof.md`
- `../no-variable-guessing.md`
- `../document-consistency.md`
- `../zero-hallucination.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the refinement must strengthen owner handoffs without inventing a duplicate new rule surface
- git-state observations must remain usable as local evidence without being promoted to semantic authority
- startup classification, hygiene, and destructive confirmation must remain distinct rather than collapsing into one overloaded owner

---

## 3) Change Items

### Change Item 1
- **Target location:** `authority-and-scope` precedence owner
- **Change type:** additive

**Before**
```text
The chain defined only the generic authority ladder and did not explicitly state that checked master/governed repo surfaces outrank git working state when classifying file meaning.
```

**After**
```text
The chain now adds a repository-governed semantic-authority bridge:
1. current user request
2. checked master surfaces
3. checked governed owner chains
4. git working state as observed local evidence only
5. cleanup/isolation/hygiene heuristics last
```

### Change Item 2
- **Target location:** `project-documentation-standards` repository-role owner
- **Change type:** additive

**Before**
```text
The chain described the semantic roles of README/design/changelog/TODO/phase/patch surfaces, but it did not explicitly require those surfaces to be consulted before a newly encountered file was treated as junk/disposable/non-governed.
```

**After**
```text
The chain now requires master-surface consultation before junk/disposal classification and defines the minimum lookup set for that check.
```

### Change Item 3
- **Target location:** `strict-file-hygiene` hygiene owner
- **Change type:** replacement

**Before**
```text
Junk-file wording could still be overread as cleanup authority.
```

**After**
```text
The chain now explicitly states that hygiene governs creation/duplication control only and does not authorize deletion of newly encountered or untracked repo files.
```

### Change Item 4
- **Target location:** `artifact-initiation-control` startup owner
- **Change type:** additive

**Before**
```text
`not required` posture could still be misread as a disposal conclusion for an already-present or newly encountered file.
```

**After**
```text
The chain now keeps startup classification separate from disposal conclusions and requires unresolved new-file meaning to stay unresolved until stronger authority is checked.
```

### Change Item 5
- **Target location:** `functional-intent-verification` destructive-confirmation owner
- **Change type:** replacement

**Before**
```text
The runtime file was effectively a header-only stub, so the design-level delete confirmation contract was not active in the runtime owner.
```

**After**
```text
The runtime chain now materializes destructive-confirmation behavior and explicitly blocks cleanup/isolation/worktree/sandbox rationale from acting as deletion authorization.
```

### Change Item 6
- **Target location:** evidence/reference companion owners
- **Change type:** additive

**Before**
```text
Weak local evidence rules already existed, but they did not explicitly map git working-state observations to disposal-classification limits.
```

**After**
```text
The companion owners now explicitly keep git-state observations in the weak local-evidence lane and require master-surface / governed-reference checks before file-disposal conclusions.
```

### Change Item 7
- **Target location:** master governance surfaces
- **Change type:** additive

**Before**
```text
Master design/README/changelog/TODO/phase surfaces did not yet record this bounded refinement wave.
```

**After**
```text
Master governance surfaces now record the file-disposal-authority and delete-guard refinement so repo-level doctrine and history stay synchronized.
```

---

## 4) Verification

- [x] `authority-and-scope` explicitly keeps repo-governed semantic authority above git-state cleanup heuristics
- [x] `project-documentation-standards` explicitly requires master-surface consultation before junk/disposal classification
- [x] `strict-file-hygiene` explicitly blocks hygiene wording from acting as deletion authority
- [x] `artifact-initiation-control` explicitly keeps startup classification separate from disposal conclusions
- [x] `functional-intent-verification` now contains a real runtime body and blocks cleanup/isolation delete authorization
- [x] evidence/reference companion owners explicitly keep git-state signals in the weak local-evidence lane
- [x] master design/README/TODO/changelog/phase surfaces can record the bounded refinement wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve the repo-governed semantic-authority bridge in `authority-and-scope`
- preserve the new runtime body in `functional-intent-verification`
- narrow companion wording before removing the new constraints entirely
- do not revert to behavior where git state, cleanup instinct, or isolation rationale can substitute for checked semantic authority and explicit delete confirmation
