from pathlib import Path
from typing import Optional, Union

from governed_docs.doctrine_evaluator import evaluate_scan_result
from governed_docs.surface_scanner import scan_governed_surfaces



def run_phase_audit_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    scan_result = scan_governed_surfaces(target_path)
    evaluation = evaluate_scan_result(scan_result)
    phase_findings = [
        finding
        for finding in evaluation.findings
        if finding.problem_class == 'phase-grammar-drift'
    ]
    lines = [
        'governed-docs phase audit report',
        f'Checked scope: {evaluation.checked_scope}',
        f'Findings: {len(phase_findings)}',
    ]
    if phase_findings:
        for finding in phase_findings:
            lines.append(
                f"- {finding.classification} | {finding.problem_class} | {finding.subject}"
            )
    else:
        lines.append('- none')
    return '\n'.join(lines)
