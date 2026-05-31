from governed_docs.generated_artifacts import RepairPlan, RepairPlanItem


def recommendation_for_finding(finding):
    if finding.classification == "drift" and finding.problem_class == "structure-drift":
        return "open-repair-patch", "review-required", [
            "Repair should stay reviewable before any mutation.",
        ]

    if finding.classification == "safe-auto-repair":
        return "bounded-normalize-candidate", "policy-check", [
            "Candidate remains reviewable and subject to executor policy before any mutation.",
        ]

    if finding.classification == "blocked":
        return "block-closeout", "manual-resolution", [
            "Blocked findings must not auto-progress into normalization or closeout.",
        ]

    if finding.classification == "ambiguous-needs-basis":
        return "ask-for-basis", "basis-required", [
            "A governing basis must be selected before repair planning can narrow the path.",
        ]

    if finding.classification == "legacy-but-allowed":
        return "report-only", "not-required", [
            "Legacy evidence should remain visible without forcing repair by default.",
        ]

    return "report-only", "not-required", []



def plan_repairs(doctrine_evaluation) -> RepairPlan:
    items = []
    for finding in doctrine_evaluation.findings:
        recommended_action, approval_boundary, preservation_notes = recommendation_for_finding(
            finding
        )
        items.append(
            RepairPlanItem(
                subject=finding.subject,
                classification=finding.classification,
                problem_class=finding.problem_class,
                recommended_action=recommended_action,
                approval_boundary=approval_boundary,
                evidence=list(getattr(finding, 'evidence', [])),
                preservation_notes=preservation_notes,
            )
        )

    return RepairPlan(
        target_workspace_path=doctrine_evaluation.target_workspace_path,
        checked_scope=doctrine_evaluation.checked_scope,
        items=items,
        mutated=False,
    )
