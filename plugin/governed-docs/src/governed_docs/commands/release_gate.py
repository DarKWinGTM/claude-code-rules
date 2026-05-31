from pathlib import Path
from typing import Optional, Union

from governed_docs.doctrine_evaluator import evaluate_scan_result
from governed_docs.release_gate import evaluate_release_gate
from governed_docs.surface_scanner import scan_governed_surfaces



def run_release_gate_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    scan_result = scan_governed_surfaces(target_path)
    evaluation = evaluate_scan_result(scan_result)
    verdict = evaluate_release_gate(evaluation, verification_passed=True)
    lines = [
        'governed-docs release gate report',
        f'Checked scope: {verdict.checked_scope}',
        f'Verdict: {verdict.verdict}',
    ]
    if verdict.notes:
        lines.append('Notes:')
        for note in verdict.notes:
            lines.append(f'- {note}')
    return '\n'.join(lines)
