import sys
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from governed_docs.commands.phase_audit import run_phase_audit_command
from governed_docs.commands.present_md import PresentMdPathError, run_present_md_command
from governed_docs.commands.repair_plan import run_repair_plan_command
from governed_docs.commands.release_gate import run_release_gate_command
from governed_docs.commands.review import run_review_command
from governed_docs.commands.scan import run_scan_command
from governed_docs.target_path import TargetPathError

CommandResult = Tuple[int, str, bool]



def help_text() -> str:
    return (
        'Usage: governed-docs <command> <explicit-target-workspace-path> [extra-args]\n'
        'Commands: scan, review, repair-plan, phase-audit, release-gate, present-md'
    )



def command_handlers() -> Dict[str, Callable[..., str]]:
    return {
        'scan': run_scan_command,
        'review': run_review_command,
        'repair-plan': run_repair_plan_command,
        'phase-audit': run_phase_audit_command,
        'release-gate': run_release_gate_command,
        'present-md': run_present_md_command,
    }



def dispatch_command(args: Sequence[str]) -> CommandResult:
    argv: List[str] = list(args)
    if not argv:
        return 1, help_text(), True

    command = argv[0]
    handler = command_handlers().get(command)
    if handler is None:
        return 1, help_text(), True

    target_path = argv[1] if len(argv) > 1 else None
    extra_args = argv[2:]
    try:
        return 0, handler(target_path, *extra_args), False
    except (TargetPathError, PresentMdPathError) as exc:
        return 1, str(exc), True



def main(argv: Optional[Sequence[str]] = None) -> int:
    exit_code, output, is_error = dispatch_command(argv if argv is not None else sys.argv[1:])
    stream = sys.stderr if is_error else sys.stdout
    print(output, file=stream)
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
