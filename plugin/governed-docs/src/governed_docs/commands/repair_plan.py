from pathlib import Path
from typing import Optional, Union

from governed_docs.doctrine_evaluator import evaluate_scan_result
from governed_docs.generated_artifacts import build_repair_plan_artifact
from governed_docs.repair_planner import plan_repairs
from governed_docs.surface_scanner import scan_governed_surfaces



def run_repair_plan_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    scan_result = scan_governed_surfaces(target_path)
    evaluation = evaluate_scan_result(scan_result)
    repair_plan = plan_repairs(evaluation)
    return build_repair_plan_artifact(repair_plan)
