# Action Policy and Release Gate

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the plugin's action policy, explicit approval boundary, automation-risk non-goals, and release-gate behavior.

## 2) Explicit target-path precondition

Before any action mode runs, the plugin should require one explicit target workspace path.

Policy:
- user-facing commands must name the workspace root they want inspected or maintained
- ambient cwd is not trusted as a substitute
- missing path is a hard stop
- ambiguous, non-existent, or out-of-scope path is a hard stop
- release-gate, normalize, repair-plan, and phase-audit all inherit this same rule

Why this matters:
- one session may carry several nearby repos at once
- governed document families often share the same filenames across projects
- a companion that guesses the target path creates the wrong kind of automation risk

## 3) Supported action modes

### Mode A — advisory

Behavior:
- detect and report only
- no edits

Best for:
- ambiguous semantics
- high preservation risk
- early scan/review passes

### Mode B — guarded-execute

Behavior:
- detect and classify
- prepare repair package
- allow bounded execution only after policy or approval allows it

This is the **default v1 posture**.

Best for:
- most governed maintenance work
- cross-surface drift repair
- release/closeout support
- bounded deterministic normalization that still needs explicit review discipline

### Mode C — bounded auto-normalize

Behavior:
- apply deterministic low-risk normalization directly

Allowed only when all of these are true:
- the target doctrine is already explicit
- the file ownership is not ambiguous
- no deletion/rename/history-risk is involved
- the action is reversible or easily reviewable

## 3) What counts as safe bounded normalization

Candidate safe classes include:
- backlink synchronization
- shard-map synchronization
- missing pointer insertion
- compact formatting reshaping
- release wording refresh from already-verified facts
- generated maintenance packet regeneration

## 4) What must remain approval-only

The plugin must not auto-fix these classes in v1:
- governed file renames
- phase lineage reassignment
- authority reclassification
- history/done relocation when preservation meaning is unclear
- destructive cleanup
- release-ready wording when proof is incomplete
- grammar promotion from legacy-only observation into forward-valid doctrine
- any operation where the target workspace path was omitted or inferred from ambient cwd

## 5) Release-gate model

The plugin should support a governed-doc release gate that asks:
- are touched release-facing surfaces aligned?
- do wording claims match checked evidence strength?
- do install/parity/body-sufficiency proofs exist where required?
- do parent/shard and current-version surfaces agree?
- is any touched drift still unresolved enough to block closeout?

Possible release-gate outcomes:
- `pass`
- `pass-with-notes`
- `rework`
- `blocked`

## 6) Before / After behavior for automation risk

### Before
- operators may overclaim completion from source edits or partial sync
- deterministic low-risk doc normalization still costs repeated manual effort
- risky changes and safe changes are not always separated early enough

### After
- the plugin can separate safe bounded normalization from approval-sensitive repair
- stronger release wording can be gated by checked evidence
- low-risk normalization can be proposed or applied without implying broader semantic authority

## 7) Explicit v1 non-goals

V1 does not try to:
- become a full autonomous documentation maintainer
- normalize every irregularity automatically
- infer missing authority decisions from convenience
- generalize the action policy into a universal framework before RULES-specific use validates it

---

> Policy rule: v1 should be helpful enough to reduce repetitive manual maintenance, but never aggressive enough to outrun the authority and preservation boundaries that RULES already defines.
