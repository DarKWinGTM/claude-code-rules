# Safe-First Active Runtime Compression Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.08
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.08 / P100`.

It packages a safe-first compression/refactor wave across selected active runtime owners so repeated explanation, recap, examples, and secondary reminder blocks can be reduced without weakening the behavior that the active RULES system depends on.

---

## Analysis

The released `v10.07 / P099` wave improved proactive delegation and lane-aware continuation, and P100 applies the next safe-first pass to compact repeated explanatory text in the current merged 18-rule runtime set without weakening its active mechanisms.

The main risk in P100 is not under-compression. The main risks are:
- blurring owner boundaries, especially across `worker-routing-and-context.md` and `safe-io.md`
- weakening phase/task semantics in `phase-todo-artifact.md`
- weakening refusal taxonomy or response contract in `refusal-and-recovery.md`
- converting portability or evidence wording into vague reminders instead of explicit behavior
- overwriting fresh history/done compaction artifacts as if they were disposable or scratch surfaces

---

## Change Items

### 1) Low-blast-radius calibration pass

- **Target artifact:** `execution-and-goal-frame.md`
- **Change type:** safe-first deletion plus compression
- **Current state:** the file contains a small meta-evaluation block and some repeated continuation framing that can be tightened.
- **Target state:** low-risk non-mechanism text is removed and repeated continuation wording is tightened while mode selection, visible intent read, selective clarification, goal/output/gate, and lane continuation remain explicit.
- **Review point:** do not weaken startup gate, mode selection, or worker-routing bridge semantics.

### 2) Worker-routing and I/O burst boundary pair

- **Target artifact:** `worker-routing-and-context.md`, `safe-io.md`
- **Change type:** safe-first compression
- **Current state:** these files intentionally share a split boundary between burst detection and routing topology, but repeated reminders and recap material remain around that split.
- **Target state:** repeated explanatory text is compressed while `safe-io.md` still owns burst triggers and `worker-routing-and-context.md` still owns topology, delegation matrix, and handoff quality.
- **Review point:** preserve the co-owner split explicitly.

### 3) Phase/task semantics cluster

- **Target artifact:** `phase-todo-artifact.md`
- **Change type:** safe-first compression
- **Current state:** the file carries repeated phase-context, lane-aware task, and live-task update wording.
- **Target state:** repeated task-shaping language is consolidated while startup posture, lineage, lane-aware live tasks, and verification-slice behavior remain explicit.
- **Review point:** do not weaken phase-linked live task semantics.

### 4) Communication compression pair

- **Target artifact:** `accurate-communication.md`, `communication-register.md`
- **Change type:** safe-first compression
- **Current state:** these files contain repeated operational checklists, examples, and reminder prose around wording quality and tone.
- **Target state:** the files become more compact while still preserving claim-state wording, evidence-strength distinctions, operator-friendly examples, natural professional tone, and truth-over-pleasing behavior.
- **Review point:** keep claim-state distinctions and anti-sycophancy behavior explicit.

### 5) Smaller independent owners

- **Target artifact:** `portable-implementation-and-hardcoding-control.md`, `refusal-and-recovery.md`
- **Change type:** safe-first compression
- **Current state:** each file contains repeated presentation layers around a still-important mechanism.
- **Target state:** repeated framing is reduced while portability classification and refusal taxonomy/response contract remain explicit.
- **Review point:** do not turn these into vague summary-only rules.

### 6) Companion chains and release surfaces

- **Target artifact:** touched design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P100 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.07 / P099` as the current released wave.
- **Target state:** master surfaces identify `v10.08 / P100` as the active safe-first compression wave until release verification passes.
- **Review point:** keep runtime install count at 18 unless a separate install-scope change is explicitly validated.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Preserve-mechanism validation confirms that triggers, taxonomies, decision flows, response contracts, owner-local operational behaviors, and phase/task/worker linkage semantics remain intact in checked scope.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- Git diff has no whitespace errors.
- GitHub release `v10.08` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P100 is active and not yet released.

Phase/patch startup state is open. Runtime-owner compression plus touched companion/master-surface sync are complete in source scope. Runtime install/parity validation is complete; push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P100 is reversed after release, restore the prior `v10.07 / P099` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat runtime destination extras or fresh history/done compaction artifacts as deletion targets during rollback.
