# Phase 002-03 - Tighten Default Mode and Correction Boundaries

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 002-03
> **Status:** Completed
> **Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2
> **Design References:** [../design/natural-professional-communication.design.md](../design/natural-professional-communication.design.md)
> **Patch References:** n/a

---

## Objective

Align default assistant mode and disagreement posture with the new communication doctrine.

## Why this phase exists

Natural professional communication depends not only on wording and explanation, but also on what the assistant defaults to when no style request exists and how it corrects the user without flattery or harshness.

## Design Extraction

- Source requirement: the default communication mode should be neutral professional and non-character-driven
- Derived execution work: update `authority-and-scope` and `anti-sycophancy`; validate evidence-owner boundaries remain stable
- Target outcome: default mode and constructive correction posture are consistent with the doctrine

## Flow Diagram

Primary communication chains aligned
  → update neutral default mode behavior
  → update constructive correction posture
  → review evidence-owner boundaries
  → default style and disagreement posture align to the doctrine

## Reviewer Checklist

- [x] `authority-and-scope` defines neutral professional default mode unless the user requests otherwise
- [x] `anti-sycophancy` reinforces calm, useful, non-flattering correction behavior
- [x] `zero-hallucination` and `evidence-grounded-burden-of-proof` remain evidence owners
- [x] No new ownership overlap is introduced

## Verification

- `authority-and-scope` updated
- `anti-sycophancy` updated
- evidence-owner boundaries reviewed

## Exit Criteria

- default mode and correction posture both align with the communication doctrine without weakening evidence discipline
