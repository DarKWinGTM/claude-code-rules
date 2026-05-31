from governed_docs.finding_models import DoctrineEvaluation, DoctrineFinding


WARNING_PREFIX_MAP = {
    "legacy-phase-identifier": (
        "legacy-but-allowed",
        "phase-grammar-drift",
        "Observed legacy phase identifier remains allowed historical evidence but not forward-valid doctrine.",
    ),
    "ambiguous-authority": (
        "ambiguous-needs-basis",
        "role-drift",
        "Observed authority ownership is ambiguous and needs an explicit governing basis.",
    ),
    "safe-auto-repair": (
        "safe-auto-repair",
        "structure-drift",
        "Observed drift appears deterministic and low-risk enough for bounded auto-repair if policy later allows it.",
    ),
    "blocked-preservation-risk": (
        "blocked",
        "preservation-risk",
        "Observed drift touches preservation-sensitive surfaces and must remain blocked until explicitly reviewed.",
    ),
    "rollover-pressure": (
        "drift",
        "rollover-pressure",
        "Observed active entrypoint pressure suggests rollover or redistribution work is needed.",
    ),
    "release-sync-drift": (
        "drift",
        "release-sync-drift",
        "Observed release-facing surfaces disagree or imply stronger status than the checked evidence supports.",
    ),
}


def warning_to_finding(scanner_warning: str):
    if ":" not in scanner_warning:
        return None

    prefix, subject = scanner_warning.split(":", 1)
    if prefix not in WARNING_PREFIX_MAP:
        return None

    classification, problem_class, reason = WARNING_PREFIX_MAP[prefix]
    return DoctrineFinding(
        subject=subject,
        classification=classification,
        problem_class=problem_class,
        reason=reason,
        evidence=[scanner_warning],
    )



def evaluate_scan_result(scan_result) -> DoctrineEvaluation:
    findings = []

    for surface in scan_result.discovered_surfaces:
        if surface.inventory_class == "active authority surface":
            findings.append(
                DoctrineFinding(
                    subject=f"Active governed surface present: {surface.relative_path}",
                    classification="compliant",
                    problem_class=None,
                    reason="The governed surface exists in the checked target path.",
                    evidence=[surface.relative_path, surface.surface_family, surface.inventory_class],
                )
            )

    for relative_path in scan_result.missing_expected_top_level_surfaces:
        findings.append(
            DoctrineFinding(
                subject=f"Missing expected top-level surface: {relative_path}",
                classification="drift",
                problem_class="structure-drift",
                reason="A required governed surface is missing from the checked target path.",
                evidence=[relative_path],
            )
        )

    for scanner_warning in scan_result.scanner_warnings:
        finding = warning_to_finding(scanner_warning)
        if finding is not None:
            findings.append(finding)

    return DoctrineEvaluation(
        target_workspace_path=scan_result.target_workspace_path,
        checked_scope=scan_result.checked_scope,
        findings=findings,
        mutated=False,
    )
