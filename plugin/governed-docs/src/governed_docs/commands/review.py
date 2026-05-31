from pathlib import Path
from typing import Optional, Union

from governed_docs.doctrine_evaluator import evaluate_scan_result
from governed_docs.surface_scanner import scan_governed_surfaces



def run_review_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    scan_result = scan_governed_surfaces(target_path)
    evaluation = evaluate_scan_result(scan_result)
    lines = [
        "governed-docs review report",
        f"Checked scope: {evaluation.checked_scope}",
        f"Findings: {len(evaluation.findings)}",
    ]
    for finding in evaluation.findings:
        lines.append(
            f"- {finding.classification} | {finding.problem_class} | {finding.subject}"
        )
    return "\n".join(lines)
