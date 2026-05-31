import sys
from pathlib import Path
from typing import Optional, Sequence, Union

from governed_docs.surface_scanner import scan_governed_surfaces
from governed_docs.target_path import TargetPathError


def format_scan_report(target_path: Path, scan_result) -> str:
    lines = [
        "governed-docs scan report",
        f"Target workspace: {target_path}",
        "Discovered surfaces:",
    ]

    if scan_result.discovered_surfaces:
        for surface in scan_result.discovered_surfaces:
            lines.append(
                f"- {surface.relative_path} | {surface.surface_family} | {surface.inventory_class}"
            )
    else:
        lines.append("- none")

    if scan_result.missing_expected_top_level_surfaces:
        lines.append("Missing expected top-level surfaces:")
        for relative_path in scan_result.missing_expected_top_level_surfaces:
            lines.append(f"- {relative_path}")

    lines.append("No files were edited.")
    return "\n".join(lines)



def run_scan_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    scan_result = scan_governed_surfaces(target_path)
    return format_scan_report(scan_result.target_workspace_path, scan_result)



def main(argv: Optional[Sequence[str]] = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    target_path = args[0] if args else None

    try:
        print(run_scan_command(target_path))
    except TargetPathError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
