#!/usr/bin/env python3
"""Phase-016 checked-scope readiness report for memory-context-intelligence.

This helper aggregates the existing phase-007 through phase-015 runtime evidence
into one readiness report. It can run the bounded replay/trial chain or consume
previous JSON reports, and it only claims `usable in checked scope` when the
checked gates pass. It does not install, publish, mutate main RULES, promote main
RULES, perform live web access, or spawn external agent processes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

LIB_ROOT = Path(__file__).resolve().parent
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

import historical_replay
import live_trial

READINESS_MODEL = "phase-016-readiness-v1"
READINESS_WORDING = "usable in checked scope"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_REPLAY_STAGES = ("intake", "signals", "present", "choose", "enrich", "orchestrate", "packet", "emit-preview")
REQUIRED_TRIAL_STAGES = ("intake", "signals", "present", "choose", "enrich", "orchestrate", "packet", "emit")
BOUNDARY_FLAGS = (
    "main_rules_mutation_performed",
    "install_or_publication_performed",
    "live_web_access_performed",
    "external_agent_process_spawned",
)


class ReadinessError(ValueError):
    """Raised when readiness inputs or evidence gates are invalid."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence ready",
        description=(
            "Aggregate phase-007 through phase-015 evidence and report whether the runtime is "
            "usable in checked scope. This is not an install, publication, stable behavior, "
            "production readiness, main RULES promotion, or main RULES merge command."
        ),
    )
    parser.add_argument("--replay-report", help="Optional phase-014 replay JSON report to reuse instead of running replay.")
    parser.add_argument("--trial-report", help="Optional phase-015 trial JSON report to reuse instead of running trial.")
    parser.add_argument(
        "--phase-015-trial-artifact",
        help="Optional existing approved phase-015 /additional/ trial artifact to check for success criteria and rollback notes.",
    )
    parser.add_argument(
        "--main-rules-root",
        help="Optional main RULES source root. When supplied, root-level markdown hashes are checked before/after readiness work.",
    )
    parser.add_argument(
        "--memory-root",
        help="Explicit memsearch memory root used when replay or trial reports are not supplied.",
    )
    parser.add_argument("--scope", action="append", default=[], help="Optional intake scope filter. May repeat.")
    parser.add_argument("--max-shards", type=int, default=3, help="Daily shards to consider through readiness replay/trial.")
    parser.add_argument("--max-records", type=int, default=8, help="Records to emit/analyze through readiness replay/trial.")
    parser.add_argument("--max-chars", type=int, default=6000, help="Total intake sample chars.")
    parser.add_argument("--max-shard-bytes", type=int, default=65536, help="Bytes read per memory shard.")
    parser.add_argument("--max-age-days", type=int, default=30, help="Freshness threshold for latest shard.")
    parser.add_argument("--max-topics", type=int, default=5, help="Maximum topic candidates to consider.")
    parser.add_argument("--topic-id", help="Topic id or rank to choose. Defaults to the first topic.")
    parser.add_argument(
        "--output-mode",
        choices=("auto", "native-first", "bilingual", "fixed"),
        default="auto",
        help="Presentation/choose output mode.",
    )
    parser.add_argument("--language", help="Presentation language hint or fixed-language selector.")
    parser.add_argument(
        "--sources-fixture",
        help="Optional controlled/recorded source fixture for enrichment. Omit for explicit no-live-web skip.",
    )
    parser.add_argument("--max-sources", type=int, default=8, help="Maximum fixture sources to evaluate.")
    parser.add_argument("--owner-domain", help="Explicit owner-domain mapping used when readiness runs packet/trial.")
    parser.add_argument("--main-rule-target", help="Explicit intended main-rule target used when readiness runs packet/trial.")
    parser.add_argument("--additional-name", help="Optional additional-stage trial rule name.")
    parser.add_argument(
        "--additional-relative-path",
        help="Optional safe relative additional-stage path used when readiness runs trial.",
    )
    parser.add_argument(
        "--additional-root",
        help="Selected additional-stage root used for replay dry-run preview and trial preview/write.",
    )
    parser.add_argument(
        "--trial-approved-write",
        action="store_true",
        help="Allow readiness to run the trial stage with an approved write under the selected additional root.",
    )
    parser.add_argument(
        "--allow-overwrite",
        action="store_true",
        help="Allow replacing an existing trial file when --trial-approved-write is also supplied.",
    )
    return parser.parse_args(argv)


def load_json_report(path_value: str | None, label: str) -> dict[str, Any] | None:
    if not path_value:
        return None
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise ReadinessError(f"{label} must be a JSON object report.")
    return loaded


def stage_map(report: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not isinstance(report, dict):
        return {}
    stages = report.get("stage_statuses", [])
    if not isinstance(stages, list):
        return {}
    return {
        str(stage.get("stage")): stage
        for stage in stages
        if isinstance(stage, dict) and stage.get("stage") is not None
    }


def stage_ok(report: dict[str, Any] | None, stage: str) -> bool:
    return bool(stage_map(report).get(stage, {}).get("ok"))


def stage_status(report: dict[str, Any] | None, stage: str) -> str | None:
    value = stage_map(report).get(stage, {}).get("status")
    return str(value) if value is not None else None


def require_run_inputs(args: argparse.Namespace, *, for_trial: bool) -> None:
    missing: list[str] = []
    if not args.memory_root:
        missing.append("--memory-root")
    if for_trial:
        for name, flag in (
            (args.owner_domain, "--owner-domain"),
            (args.main_rule_target, "--main-rule-target"),
            (args.additional_root, "--additional-root"),
        ):
            if not name:
                missing.append(flag)
    if missing:
        raise ReadinessError(
            "Readiness needs either supplied JSON reports or the inputs to run the missing stage(s): "
            + ", ".join(missing)
        )


def build_replay_report(args: argparse.Namespace) -> dict[str, Any]:
    require_run_inputs(args, for_trial=False)
    replay_args = argparse.Namespace(
        memory_root=args.memory_root,
        scope=args.scope,
        max_shards=args.max_shards,
        max_records=args.max_records,
        max_chars=args.max_chars,
        max_shard_bytes=args.max_shard_bytes,
        max_age_days=args.max_age_days,
        max_topics=args.max_topics,
        topic_id=args.topic_id,
        output_mode=args.output_mode,
        language=args.language,
        sources_fixture=args.sources_fixture,
        max_sources=args.max_sources,
        owner_domain=args.owner_domain,
        main_rule_target=args.main_rule_target,
        additional_name=args.additional_name,
        additional_relative_path=args.additional_relative_path,
        additional_root=args.additional_root,
        skip_emit_preview=False,
    )
    return historical_replay.build_replay_report(replay_args)


def build_trial_report(args: argparse.Namespace) -> dict[str, Any]:
    require_run_inputs(args, for_trial=True)
    trial_args = argparse.Namespace(
        memory_root=args.memory_root,
        scope=args.scope,
        max_shards=args.max_shards,
        max_records=args.max_records,
        max_chars=args.max_chars,
        max_shard_bytes=args.max_shard_bytes,
        max_age_days=args.max_age_days,
        max_topics=args.max_topics,
        topic_id=args.topic_id,
        output_mode=args.output_mode,
        language=args.language,
        sources_fixture=args.sources_fixture,
        max_sources=args.max_sources,
        owner_domain=args.owner_domain,
        main_rule_target=args.main_rule_target,
        additional_name=args.additional_name,
        additional_relative_path=args.additional_relative_path,
        additional_root=args.additional_root,
        approved_write=args.trial_approved_write,
        allow_overwrite=args.allow_overwrite,
        disposition=None,
        usefulness_note=[],
        risk_note=[],
        required_revision=[],
    )
    return live_trial.build_live_trial_report(trial_args)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main_rules_markdown_snapshot(root_value: str | None) -> dict[str, Any]:
    if not root_value:
        return {
            "checked": False,
            "ok": None,
            "root": None,
            "file_count": 0,
            "digest": None,
            "files": [],
            "note": "Main RULES root hash check was not requested.",
        }
    root = Path(root_value).expanduser()
    if not root.is_dir():
        return {
            "checked": True,
            "ok": False,
            "root": str(root),
            "file_count": 0,
            "digest": None,
            "files": [],
            "note": "Configured main RULES root does not exist or is not a directory.",
        }
    files = []
    for path in sorted(root.glob("*.md"), key=lambda item: item.name):
        if path.is_file():
            files.append({"relative_path": path.name, "sha256": file_sha256(path)})
    aggregate = hashlib.sha256()
    for item in files:
        aggregate.update(str(item["relative_path"]).encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(str(item["sha256"]).encode("utf-8"))
        aggregate.update(b"\0")
    return {
        "checked": True,
        "ok": True,
        "root": str(root),
        "file_count": len(files),
        "digest": aggregate.hexdigest(),
        "files": files,
        "note": "Root-level main RULES markdown snapshot captured for checked-scope unchanged audit.",
    }


def compare_main_rules_snapshots(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    checked = bool(before.get("checked")) and bool(after.get("checked"))
    same_digest = checked and before.get("ok") and after.get("ok") and before.get("digest") == after.get("digest")
    return {
        "checked": checked,
        "ok": bool(same_digest),
        "root": before.get("root") or after.get("root"),
        "before_digest": before.get("digest"),
        "after_digest": after.get("digest"),
        "before_file_count": before.get("file_count"),
        "after_file_count": after.get("file_count"),
        "note": (
            "Root-level main RULES markdown hashes are unchanged in checked scope."
            if same_digest
            else "Root-level main RULES markdown unchanged audit did not pass or was not checked."
        ),
    }


def path_contains_markers(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {
            "path": str(path),
            "exists": False,
            "contains_success_criteria": False,
            "contains_rollback_notes": False,
        }
    material = path.read_text(encoding="utf-8")
    return {
        "path": str(path),
        "exists": True,
        "contains_success_criteria": "## Success criteria" in material,
        "contains_rollback_notes": "## Rollback notes" in material,
    }


def live_trial_artifact_summary(args: argparse.Namespace, trial_report: dict[str, Any]) -> dict[str, Any]:
    checked_paths: list[dict[str, Any]] = []
    if args.phase_015_trial_artifact:
        checked_paths.append(path_contains_markers(Path(args.phase_015_trial_artifact).expanduser()))
    emission = trial_report.get("emission", {}) if isinstance(trial_report.get("emission"), dict) else {}
    destination_path = emission.get("destination_path")
    if destination_path and emission.get("additional_emission_performed"):
        destination = Path(str(destination_path)).expanduser()
        if not any(item.get("path") == str(destination) for item in checked_paths):
            checked_paths.append(path_contains_markers(destination))

    ok = any(
        bool(item.get("exists"))
        and bool(item.get("contains_success_criteria"))
        and bool(item.get("contains_rollback_notes"))
        for item in checked_paths
    )
    return {
        "checked": bool(checked_paths),
        "ok": ok,
        "artifacts": checked_paths,
        "note": (
            "At least one approved live additional-stage trial artifact was checked with success criteria and rollback notes."
            if ok
            else "No checked live additional-stage trial artifact currently satisfies the phase-015 artifact evidence gate."
        ),
    }


def top_level_flag(report: dict[str, Any], flag: str) -> bool:
    if bool(report.get(flag)):
        return True
    for key in ("no_write_authority_boundary_audit", "live_trial_boundary_audit"):
        audit = report.get(key)
        if isinstance(audit, dict) and bool(audit.get(flag)):
            return True
    return False


def boundary_flags(replay_report: dict[str, Any], trial_report: dict[str, Any]) -> dict[str, bool]:
    return {flag: top_level_flag(replay_report, flag) or top_level_flag(trial_report, flag) for flag in BOUNDARY_FLAGS}


def command_map() -> dict[str, dict[str, str]]:
    return {
        "status": {"purpose": "Show local command map and boundaries.", "writes": "none"},
        "intake": {"purpose": "Read bounded memsearch summaries from an explicit memory root.", "writes": "none"},
        "signals": {"purpose": "Generate internal signals and topic candidates from intake JSON.", "writes": "none"},
        "present": {"purpose": "Render list-first topic presentation.", "writes": "none"},
        "choose": {"purpose": "Record exactly one selected topic as structured stdout state.", "writes": "none"},
        "enrich": {"purpose": "Use controlled source fixtures when research is needed.", "writes": "none"},
        "orchestrate": {"purpose": "Compose deterministic runtime-local lane findings.", "writes": "none"},
        "packet": {"purpose": "Build a reviewable candidate packet.", "writes": "none"},
        "emit": {"purpose": "Preview or explicitly emit /additional/ trial material.", "writes": "only with --approved-write"},
        "replay": {"purpose": "Run deterministic phase-014 historical replay.", "writes": "none; dry-run preview only"},
        "trial": {"purpose": "Run phase-015 bounded live additional-stage trial.", "writes": "only with --approved-write under selected additional root"},
        "ready": {"purpose": "Aggregate phase-007 through phase-015 checked evidence.", "writes": "none unless --trial-approved-write is explicitly supplied"},
    }


def usage_config_guidance() -> dict[str, Any]:
    return {
        "selected_invocation_surface": "bash ./bin/memory-context-intelligence ready",
        "required_for_chain_run": [
            "--memory-root <memory-root>",
            "--owner-domain <domain>",
            "--main-rule-target <rule.md>",
            "--additional-root <additional-root>",
            "--main-rules-root <rules-root>",
        ],
        "optional_reuse_inputs": ["--replay-report <replay.json>", "--trial-report <trial.json>"],
        "optional_live_trial_artifact_check": "--phase-015-trial-artifact <existing-additional-trial.md>",
        "configuration": [
            "Memory input is late-bound through --memory-root or intake environment variables; no package memory root default is used.",
            "Additional-stage writes stay under the selected --additional-root and require explicit approval flags.",
            "Readiness can run without writing by using supplied replay/trial reports plus an existing trial artifact check.",
            "Main RULES unchanged evidence is checked only when --main-rules-root is supplied.",
        ],
    }


def package_path_checks() -> dict[str, Any]:
    paths = {
        "plugin_json": PACKAGE_ROOT / ".claude-plugin" / "plugin.json",
        "cli": PACKAGE_ROOT / "bin" / "memory-context-intelligence",
        "skill": PACKAGE_ROOT / "skills" / "analysis" / "SKILL.md",
        "agents_dir": PACKAGE_ROOT / "agents",
        "runtime_readme": PACKAGE_ROOT / "README.md",
    }
    return {name: {"path": str(path), "exists": path.exists()} for name, path in paths.items()}


def phase_evidence_record(
    replay_report: dict[str, Any],
    trial_report: dict[str, Any],
    artifact_summary: dict[str, Any],
) -> list[dict[str, Any]]:
    replay_stages = stage_map(replay_report)
    trial_stages = stage_map(trial_report)
    package_checks = package_path_checks()
    phase_007_ok = all(item["exists"] for item in package_checks.values())
    return [
        {
            "phase": "007",
            "evidence": "isolated runtime package scaffold",
            "ok": phase_007_ok,
            "checks": package_checks,
        },
        {
            "phase": "008",
            "evidence": "bounded safe memsearch intake",
            "ok": stage_ok(replay_report, "intake") and stage_ok(trial_report, "intake"),
            "stage_status": {"replay": stage_status(replay_report, "intake"), "trial": stage_status(trial_report, "intake")},
        },
        {
            "phase": "009",
            "evidence": "internal signal extraction and topic generation",
            "ok": stage_ok(replay_report, "signals") and stage_ok(trial_report, "signals"),
            "stage_status": {"replay": stage_status(replay_report, "signals"), "trial": stage_status(trial_report, "signals")},
        },
        {
            "phase": "010",
            "evidence": "topic presentation and choose flow",
            "ok": all(stage_ok(replay_report, stage) and stage_ok(trial_report, stage) for stage in ("present", "choose")),
            "stage_status": {
                "replay_present": stage_status(replay_report, "present"),
                "replay_choose": stage_status(replay_report, "choose"),
                "trial_present": stage_status(trial_report, "present"),
                "trial_choose": stage_status(trial_report, "choose"),
            },
        },
        {
            "phase": "011",
            "evidence": "optional controlled research enrichment",
            "ok": stage_ok(replay_report, "enrich") and stage_ok(trial_report, "enrich"),
            "stage_status": {"replay": stage_status(replay_report, "enrich"), "trial": stage_status(trial_report, "enrich")},
        },
        {
            "phase": "012",
            "evidence": "runtime-local bounded orchestration",
            "ok": stage_ok(replay_report, "orchestrate") and stage_ok(trial_report, "orchestrate"),
            "stage_status": {"replay": stage_status(replay_report, "orchestrate"), "trial": stage_status(trial_report, "orchestrate")},
        },
        {
            "phase": "013",
            "evidence": "candidate packet building and gated additional-stage emission path",
            "ok": stage_ok(replay_report, "packet") and stage_ok(trial_report, "packet") and stage_ok(trial_report, "emit"),
            "stage_status": {
                "replay_packet": stage_status(replay_report, "packet"),
                "trial_packet": stage_status(trial_report, "packet"),
                "trial_emit": stage_status(trial_report, "emit"),
            },
        },
        {
            "phase": "014",
            "evidence": "deterministic historical replay validation with dry-run emit preview only",
            "ok": replay_report.get("status") in {"replay-completed", "replay-completed-with-adjustments"}
            and all(stage_ok(replay_report, stage) for stage in REQUIRED_REPLAY_STAGES)
            and bool((replay_report.get("no_write_authority_boundary_audit") or {}).get("authority_boundary_ok")),
            "status": replay_report.get("status"),
        },
        {
            "phase": "015",
            "evidence": "bounded live additional-stage trial evidence",
            "ok": trial_report.get("status") in {"trial-emitted", "trial-preview"}
            and all(stage_ok(trial_report, stage) for stage in REQUIRED_TRIAL_STAGES)
            and bool(artifact_summary.get("ok")),
            "status": trial_report.get("status"),
            "trial_artifact": artifact_summary,
        },
    ]


def replay_result_summary(replay_report: dict[str, Any]) -> dict[str, Any]:
    audit = replay_report.get("no_write_authority_boundary_audit", {})
    return {
        "status": replay_report.get("status"),
        "selected_topic": replay_report.get("selected_topic", {}),
        "required_stages_ok": {stage: stage_ok(replay_report, stage) for stage in REQUIRED_REPLAY_STAGES},
        "emit_preview_dry_run": audit.get("emit_preview_dry_run") if isinstance(audit, dict) else None,
        "authority_boundary_ok": audit.get("authority_boundary_ok") if isinstance(audit, dict) else None,
        "adjustments_needed_before_phase_015": replay_report.get("adjustments_needed_before_phase_015", []),
    }


def live_trial_result_summary(trial_report: dict[str, Any], artifact_summary: dict[str, Any]) -> dict[str, Any]:
    emission = trial_report.get("emission", {}) if isinstance(trial_report.get("emission"), dict) else {}
    audit = trial_report.get("live_trial_boundary_audit", {}) if isinstance(trial_report.get("live_trial_boundary_audit"), dict) else {}
    return {
        "status": trial_report.get("status"),
        "trial_disposition": trial_report.get("trial_disposition"),
        "selected_live_topic": trial_report.get("selected_live_topic", {}),
        "required_stages_ok": {stage: stage_ok(trial_report, stage) for stage in REQUIRED_TRIAL_STAGES},
        "candidate_packet_approved_for_trial_write": trial_report.get("candidate_packet_approved_for_trial_write"),
        "emission_status": emission.get("status"),
        "approved_write": emission.get("approved_write"),
        "additional_emission_performed": emission.get("additional_emission_performed"),
        "destination_relative_path": emission.get("destination_relative_path"),
        "artifact_summary": artifact_summary,
        "boundary_audit": audit,
    }


def build_verification_record(
    phase_record: list[dict[str, Any]],
    main_rules_audit: dict[str, Any],
) -> dict[str, Any]:
    return {
        "phase_007_through_015": [
            {"phase": item["phase"], "evidence": item["evidence"], "ok": item["ok"]} for item in phase_record
        ],
        "focused_end_to_end_stages": {
            "intake": next(item for item in phase_record if item["phase"] == "008")["ok"],
            "signals": next(item for item in phase_record if item["phase"] == "009")["ok"],
            "present_choose": next(item for item in phase_record if item["phase"] == "010")["ok"],
            "enrich": next(item for item in phase_record if item["phase"] == "011")["ok"],
            "orchestrate": next(item for item in phase_record if item["phase"] == "012")["ok"],
            "packet": bool(next(item for item in phase_record if item["phase"] == "013")["ok"]),
            "emit_trial_path": bool(next(item for item in phase_record if item["phase"] == "015")["ok"]),
            "main_rules_unchanged": bool(main_rules_audit.get("ok")),
        },
        "main_rules_unchanged_audit": main_rules_audit,
    }


def readiness_gates(
    *,
    phase_record: list[dict[str, Any]],
    flags: dict[str, bool],
    main_rules_audit: dict[str, Any],
) -> dict[str, Any]:
    failed = [f"phase-{item['phase']}" for item in phase_record if not item.get("ok")]
    boundary_violations = [flag for flag, value in flags.items() if value]
    if not main_rules_audit.get("ok"):
        failed.append("main-rules-unchanged")
    ok = not failed and not boundary_violations
    return {
        "ok": ok,
        "failed_gates": failed,
        "boundary_violations": boundary_violations,
    }


def boundary_audit_summary(
    flags: dict[str, bool],
    main_rules_audit: dict[str, Any],
    trial_report: dict[str, Any],
) -> dict[str, Any]:
    emission = trial_report.get("emission", {}) if isinstance(trial_report.get("emission"), dict) else {}
    return {
        "main_rules_merge_status": "main RULES merge has not happened",
        "main_rules_unchanged_checked": bool(main_rules_audit.get("checked")),
        "main_rules_unchanged": bool(main_rules_audit.get("ok")),
        "main_rules_mutation_performed": flags["main_rules_mutation_performed"],
        "install_or_publication_performed": flags["install_or_publication_performed"],
        "marketplace_release_performed": False,
        "live_web_access_performed": flags["live_web_access_performed"],
        "external_agent_process_spawned": flags["external_agent_process_spawned"],
        "stable_behavior_claimed": False,
        "broad_production_readiness_claimed": False,
        "main_rules_promotion_claimed": False,
        "trial_additional_emission_performed": bool(emission.get("additional_emission_performed")),
        "trial_destination_path": emission.get("destination_path"),
    }


def known_limitations() -> list[str]:
    return [
        "Readiness means usable in checked scope only; it does not claim stable behavior or broad production readiness.",
        "No install, package publication, marketplace release, or runtime activation proof is claimed.",
        "No main RULES promotion, merge, or mutation is performed by readiness mode.",
        "Replay keeps additional-stage emission as dry-run preview only.",
        "Trial writes require explicit approval and stay under the selected additional root.",
        "External research remains fixture-backed; live web access is not performed.",
        "Native-agent orchestration is deterministic and runtime-local; external agent processes are not spawned.",
        "Exact local paths in reports are checked-scope facts, not reusable defaults.",
    ]


def build_readiness_report(args: argparse.Namespace) -> dict[str, Any]:
    main_rules_before = main_rules_markdown_snapshot(args.main_rules_root)
    replay_report = load_json_report(args.replay_report, "Replay report") or build_replay_report(args)
    trial_report = load_json_report(args.trial_report, "Trial report") or build_trial_report(args)
    main_rules_after = main_rules_markdown_snapshot(args.main_rules_root)
    main_rules_audit = compare_main_rules_snapshots(main_rules_before, main_rules_after)

    artifact_summary = live_trial_artifact_summary(args, trial_report)
    phase_record = phase_evidence_record(replay_report, trial_report, artifact_summary)
    flags = boundary_flags(replay_report, trial_report)
    gates = readiness_gates(phase_record=phase_record, flags=flags, main_rules_audit=main_rules_audit)
    status = READINESS_WORDING if gates["ok"] else "readiness-blocked"

    return {
        "tool": "memory-context-intelligence",
        "mode": "ready",
        "status": status,
        "readiness_model": READINESS_MODEL,
        "final_readiness_wording_used": READINESS_WORDING if gates["ok"] else "not usable in checked scope",
        "readiness_scope": "checked local runtime package plus supplied replay/trial/main RULES evidence",
        "selected_invocation_surface": {
            "command": "ready",
            "command_map": command_map(),
        },
        "usage_config_guidance": usage_config_guidance(),
        "verification_record": build_verification_record(phase_record, main_rules_audit),
        "phase_007_015_evidence_record": phase_record,
        "replay_result_summary": replay_result_summary(replay_report),
        "live_trial_result_summary": live_trial_result_summary(trial_report, artifact_summary),
        "boundary_audit_summary": boundary_audit_summary(flags, main_rules_audit, trial_report),
        "readiness_gates": gates,
        "known_limitations_unsupported_paths": known_limitations(),
        "not_claimed": [
            "stable behavior",
            "broad production readiness",
            "install or publication",
            "marketplace release",
            "main RULES promotion",
            "main RULES merge",
            "main RULES mutation",
        ],
        "main_rules_merge_statement": "main RULES merge has not happened",
        "live_web_access_performed": flags["live_web_access_performed"],
        "external_agent_process_spawned": flags["external_agent_process_spawned"],
        "main_rules_mutation_performed": flags["main_rules_mutation_performed"],
        "install_or_publication_performed": flags["install_or_publication_performed"],
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = build_readiness_report(args)
    except (OSError, json.JSONDecodeError, ReadinessError, historical_replay.HistoricalReplayError, live_trial.LiveTrialError) as exc:
        print(f"memory-context-intelligence ready: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
