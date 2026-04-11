# Table Format and Usage

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.4
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-11)

---

## 1) Goal

Preserve the previously developed custom table-format experiment for later redesign without keeping it active in the current RULES enforcement path.

This design now serves as a retained reference for future work rather than an active target-state doctrine that current answer behavior must enforce.

---

## 2) Problem Statement

The custom table-format experiment became too detailed and operationally heavy for current needs.

The user wants:
- the experiment kept in the repository
- the experiment removed from active RULES behavior for now
- related active rules cleaned so they do not continue to depend on suspended custom table semantics
- general support for using tables when helpful to remain intact

So the problem is no longer how to harden this custom table doctrine.
The problem is how to preserve it without leaving stale active dependencies behind.

---

## 3) Current Scope

### 3.1 In Scope
- preserving the suspended custom table-format experiment in-repo outside the root active rule area
- removing its active enforcement role from the current RULES path
- making suspension status explicit
- keeping future reactivation possible through a later bounded wave

### 3.2 Out of Scope
- defining the next replacement table doctrine now
- keeping this chain in the root active rule area or runtime install
- making adjacent active rules defer to this file while suspended

---

## 4) Suspended-State Model

### 4.1 Suspension Principle
This chain is retained but suspended.

Required behavior:
- do not treat this chain as an active runtime owner right now
- do not keep active rules dependent on it while it is suspended
- preserve it as a future reference candidate rather than deleting it

### 4.2 Active-System Boundary
While suspended:
- active presentation behavior remains in `answer-presentation.md`
- active explanation behavior remains in `explanation-quality.md`
- table use may still happen when helpful, but not under this custom table-format doctrine

### 4.3 Reactivation Principle
If a future table-format wave is opened later:
- reintroduce active ownership explicitly
- re-evaluate the old experiment instead of assuming it should come back unchanged
- reinstall only after the reactivation wave is clearly approved and synchronized

---

## 5) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| keeping a suspended custom rule in the active install set | stale doctrine still behaves like active truth | remove it from the active rule set while retaining the file |
| leaving active rules dependent on a suspended experiment | hidden drift remains in the system | clean defer/reference links out of active rules |
| deleting the experiment entirely when the user asked to preserve it | loses future reference value | keep it in-repo as suspended material |
| treating the old experiment as automatically correct for future reuse | future work gets anchored to stale detail | treat it as historical input for a later redesign |

---

## 6) Integration

Related chains:
- `answer-presentation.md`
- `explanation-quality.md`
- `authority-and-scope.md`
- `memory-governance-and-session-boundary.md`
