#!/usr/bin/env python3
"""Phase-015 bounded live additional-stage trial for memory-context-intelligence.

This helper runs the existing runtime chain over bounded memory input, builds one
candidate packet, and optionally performs one approved write under a selected
additional-stage root. It returns a structured trial report with selected topic,
evidence basis, packet approval state, emission checks, observation notes,
continue/revise/retire disposition, success criteria, and rollback notes.

It never mutates main RULES, installs, publishes, performs live web access, or
spawns external agent processes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

LIB_ROOT = Path(__file__).resolve().parent
if str(LIB_ROOT) not in sys.path:
    sys.path.insert(0, str(LIB_ROOT))

import candidate_packet
import historical_replay
import intake
import orchestration
import presentation
import research_enrichment
import signals

LIVE_TRIAL_MODEL = "phase-015-live-additional-stage-trial-v1"


class LiveTrialError(ValueError):
    """Raised when live trial input or stage execution is invalid."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence trial",
        description=(
            "Run one bounded live additional-stage trial through intake, signals, "
            "present/choose, enrichment, orchestration, packet, and gated emit. "
            "Approved writes require --approved-write and stay under the selected additional root."
        ),
    )
    parser.add_argument(
        "--memory-root",
        help=(
            "Explicit memsearch memory root. If omitted, intake may use "
            "MEMORY_CONTEXT_INTELLIGENCE_MEMORY_ROOT or MCI_MEMORY_ROOT."
        ),
    )
    parser.add_argument("--scope", action="append", default=[], help="Optional intake scope filter. May repeat.")
    parser.add_argument("--max-shards", type=int, default=2, help="Daily shards to consider through intake.")
    parser.add_argument("--max-records", type=int, default=8, help="Records to emit/analyze through the trial.")
    parser.add_argument("--max-chars", type=int, default=6000, help="Total intake sample chars.")
    parser.add_argument("--max-shard-bytes", type=int, default=65536, help="Bytes read per memory shard.")
    parser.add_argument("--max-age-days", type=int, default=30, help="Freshness threshold for latest shard.")
    parser.add_argument("--max-topics", type=int, default=5, help="Maximum topic candidates to consider.")
    parser.add_argument("--topic-id", help="Topic id or rank to choose. Defaults to the first topic.")
    parser.add_argument(
        "--output-mode",
        choices=presentation.OUTPUT_MODES,
        default="auto",
        help="Presentation/choose output mode.",
    )
    parser.add_argument("--language", help="Presentation language hint or fixed-language selector.")
    parser.add_argument(
        "--sources-fixture",
        help="Optional controlled/recorded source fixture for enrichment. Omit for explicit no-live-web skip.",
    )
    parser.add_argument("--max-sources", type=int, default=8, help="Maximum fixture sources to evaluate.")
    parser.add_argument("--owner-domain", required=True, help="Explicit owner-domain mapping for trial packet approval.")
    parser.add_argument("--main-rule-target", required=True, help="Explicit intended main-rule target for trial packet approval.")
    parser.add_argument("--additional-name", help="Optional additional-stage trial rule name.")
    parser.add_argument(
        "--additional-relative-path",
        help="Optional safe relative additional-stage path. Defaults to memory-context-intelligence/<name>.md.",
    )
    parser.add_argument(
        "--additional-root",
        required=True,
        help="Selected additional-stage root for the live trial write or preview.",
    )
    parser.add_argument(
        "--approved-write",
        action="store_true",
        help="Actually write the trial file. Omit for preview/report only.",
    )
    parser.add_argument(
        "--allow-overwrite",
        action="store_true",
        help="Allow replacing an existing emitted trial file. Omit to refuse overwrites.",
    )
    parser.add_argument(
        "--disposition",
        choices=("continue", "revise", "retire"),
        help="Optional explicit trial disposition. Defaults to continue on successful emission, revise otherwise.",
    )
    parser.add_argument(
        "--usefulness-note",
        action="append",
        default=[],
        help="Optional observation note about usefulness. May repeat.",
    )
    parser.add_argument(
        "--risk-note",
        action="append",
        default=[],
        help="Optional observation note about risk. May repeat.",
    )
    parser.add_argument(
        "--required-revision",
        action="append",
        default=[],
        help="Optional required revision note. May repeat.",
    )
    return parser.parse_args(argv)


def stage_entry(stage: str, status: str, *, ok: bool, summary: dict[str, Any] | None = None) -> dict[str, Any]:
    return historical_replay.stage_entry(stage, status, ok=ok, summary=summary)


def as_clean_list(values: list[str] | None) -> list[str]:
    result: list[str] = []
    for value in values or []:
        text = str(value or "").strip()
        if text:
            result.append(text)
    return result


def default_observation_notes(
    *,
    selected_topic: dict[str, Any] | None,
    emitted: bool,
    destination_path: str | None,
    usefulness_notes: list[str],
    risk_notes: list[str],
    required_revisions: list[str],
) -> dict[str, list[str]]:
    title = selected_topic.get("title") if isinstance(selected_topic, dict) else None
    usefulness = as_clean_list(usefulness_notes) or [
        (
            f"The live trial emitted a reviewable additional-stage rule for `{title}` with trace/source evidence retained."
            if emitted and title
            else "The trial produced a reviewable candidate path, but no live file was emitted."
        ),
        "The emitted material keeps trial-only status visible before any phase-016 usability or main RULES promotion claim.",
    ]
    risk = as_clean_list(risk_notes) or [
        "Additional-stage material can be over-trusted if its trial-only boundary is not preserved.",
        "The command path does not mutate main RULES, but rollback of the emitted trial file still needs explicit action-and-scope confirmation.",
    ]
    revisions = as_clean_list(required_revisions) or [
        "No phase-015 blocking revision is required if the emitted file remains trial-only and future behavior observation stays scoped.",
        "Future revision or promotion should be based on observed additional-stage behavior, not on emission success alone.",
    ]
    if destination_path:
        revisions.append(f"Review the emitted trial file before phase-016 closeout: {destination_path}")
    return {
        "usefulness": usefulness,
        "risk": risk,
        "required_revisions": revisions,
    }


def rollback_notes(destination_path: str | None) -> list[str]:
    notes = [
        "Rollback means retiring, replacing, or removing only the emitted additional-stage trial file, not changing main RULES.",
        "Deletion or replacement of the emitted trial file requires explicit action-and-scope confirmation.",
        "If revision is selected, prefer a new distinct trial file unless overwrite is explicitly approved for the same destination.",
        "Main RULES rollback is not needed because this command does not mutate main RULES.",
    ]
    if destination_path:
        notes.insert(0, f"Emitted trial file: {destination_path}")
    return notes


def material_checks(emit_report: dict[str, Any] | None) -> dict[str, Any]:
    if not isinstance(emit_report, dict):
        return {
            "destination_path": None,
            "emitted_file_exists": False,
            "material_contains_success_criteria": False,
            "material_contains_rollback_notes": False,
        }

    destination_path = emit_report.get("destination_path")
    material = str(emit_report.get("preview_material") or "")
    exists = False
    if destination_path:
        destination = Path(str(destination_path))
        exists = destination.exists()
        if exists:
            material = destination.read_text(encoding="utf-8")

    return {
        "destination_path": destination_path,
        "destination_relative_path": emit_report.get("destination_relative_path"),
        "emitted_file_exists": exists,
        "material_contains_success_criteria": "## Success criteria" in material,
        "material_contains_rollback_notes": "## Rollback notes" in material,
        "bytes_planned_or_written": emit_report.get("bytes_planned"),
    }


def build_blocked_report(
    *,
    status: str,
    reason: str,
    stage_statuses: list[dict[str, Any]],
    reports: list[dict[str, Any] | None],
    selected_topic: dict[str, Any] | None = None,
    packet_report: dict[str, Any] | None = None,
    emit_report: dict[str, Any] | None = None,
) -> dict[str, Any]:
    checks = material_checks(emit_report)
    emitted = bool(emit_report and emit_report.get("additional_emission_performed"))
    disposition = "revise"
    packet = packet_report.get("candidate_packet", {}) if isinstance(packet_report, dict) else {}
    return {
        "tool": "memory-context-intelligence",
        "mode": "trial",
        "status": status,
        "live_trial_model": LIVE_TRIAL_MODEL,
        "selected_live_topic": selected_topic or {},
        "candidate_packet_approved_for_trial_write": False,
        "candidate_packet_status": packet_report.get("status") if isinstance(packet_report, dict) else None,
        "candidate_packet_stop_gates": packet.get("stop_gates", []) if isinstance(packet, dict) else [],
        "emission": emit_report or {"status": "not-emitted", "reason": reason},
        "emission_checks": checks,
        "observation_notes": default_observation_notes(
            selected_topic=selected_topic,
            emitted=emitted,
            destination_path=checks.get("destination_path"),
            usefulness_notes=[],
            risk_notes=[],
            required_revisions=[reason],
        ),
        "trial_disposition": disposition,
        "success_criteria": packet.get("success_criteria", []) if isinstance(packet, dict) else [],
        "rollback_notes": rollback_notes(checks.get("destination_path")),
        "stage_statuses": stage_statuses,
        "live_trial_boundary_audit": {
            "additional_emission_performed": emitted,
            "main_rules_mutation_performed": any(bool(report.get("main_rules_mutation_performed")) for report in reports if isinstance(report, dict)),
            "install_or_publication_performed": any(bool(report.get("install_or_publication_performed")) for report in reports if isinstance(report, dict)),
            "live_web_access_performed": any(bool(report.get("live_web_access_performed")) for report in reports if isinstance(report, dict)),
            "external_agent_process_spawned": any(bool(report.get("external_agent_process_spawned")) for report in reports if isinstance(report, dict)),
        },
        "notes": [
            reason,
            "No main RULES mutation, install, publication, live web access, or external agent process spawning was requested by live-trial mode.",
        ],
        "live_web_access_performed": False,
        "external_agent_process_spawned": False,
        "additional_emission_performed": emitted,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def build_live_trial_report(args: argparse.Namespace) -> dict[str, Any]:
    stage_statuses: list[dict[str, Any]] = []
    source_fixture = historical_replay.load_json_fixture(args.sources_fixture)

    intake_args = argparse.Namespace(
        memory_root=args.memory_root,
        scope=args.scope,
        max_shards=args.max_shards,
        max_records=args.max_records,
        max_chars=args.max_chars,
        max_shard_bytes=args.max_shard_bytes,
        max_age_days=args.max_age_days,
    )
    intake_report = intake.build_report(intake_args)
    stage_statuses.append(
        stage_entry(
            "intake",
            str(intake_report.get("status")),
            ok=intake_report.get("status") in {"available", "stale"},
            summary={
                "records": len(intake_report.get("records", []) or []),
                "daily_shards_considered": (intake_report.get("source", {}) or {}).get("daily_shards_considered", []),
                "bounded_subset_only": (intake_report.get("scope", {}) or {}).get("bounded_subset_only"),
            },
        )
    )

    signals_report = signals.build_report(intake_report, max_records=args.max_records, max_topics=args.max_topics)
    stage_statuses.append(
        stage_entry(
            "signals",
            str(signals_report.get("status")),
            ok=signals_report.get("status") in {"available", "low-confidence"},
            summary=signals_report.get("limits", {}),
        )
    )

    presentation_report = presentation.build_presentation(
        signals_report,
        output_mode=args.output_mode,
        language=args.language,
    )
    stage_statuses.append(
        stage_entry(
            "present",
            str(presentation_report.get("status")),
            ok=presentation_report.get("status") == "available",
            summary={"topics_presented": len(presentation_report.get("topic_list", []) or [])},
        )
    )

    reports: list[dict[str, Any] | None] = [intake_report, signals_report, presentation_report]
    try:
        selected_topic_id = historical_replay.choose_replay_topic(signals_report, args.topic_id)
        selection_report = presentation.build_selection(
            signals_report,
            topic_id=selected_topic_id,
            output_mode=args.output_mode,
            language=args.language,
        )
        stage_statuses.append(
            stage_entry(
                "choose",
                str(selection_report.get("status")),
                ok=selection_report.get("status") == "selected",
                summary={"selected_topic_id": selection_report.get("selected_topic_id")},
            )
        )
        selected_topic = selection_report.get("selected_topic", {}) if isinstance(selection_report.get("selected_topic"), dict) else {}
        reports.append(selection_report)

        enrichment_report = research_enrichment.build_enrichment(
            selection_report,
            source_fixture=source_fixture,
            max_sources=args.max_sources,
        )
        stage_statuses.append(
            stage_entry(
                "enrich",
                str(enrichment_report.get("status")),
                ok=enrichment_report.get("status") in {"research-skipped", "research-enriched"},
                summary={
                    "decision": (
                        (enrichment_report.get("enrichment_decision") or {}).get("gate_result")
                        or (enrichment_report.get("enrichment_decision") or {}).get("result")
                    )
                    if isinstance(enrichment_report.get("enrichment_decision"), dict)
                    else None,
                    "live_web_access_performed": enrichment_report.get("live_web_access_performed"),
                },
            )
        )
        reports.append(enrichment_report)

        orchestration_report = orchestration.build_orchestration(
            intake_report=intake_report,
            signals_report=signals_report,
            selection_report=selection_report,
            enrichment_report=enrichment_report,
            max_sources=args.max_sources,
        )
        stage_statuses.append(
            stage_entry(
                "orchestrate",
                str(orchestration_report.get("status")),
                ok=orchestration_report.get("status") in {"orchestrated", "orchestrated-with-stop-gates"},
                summary=orchestration_report.get("result_summary", {}),
            )
        )
        reports.append(orchestration_report)

        packet_report = candidate_packet.build_candidate_packet(
            orchestration_report["phase_013_candidate_input"],
            owner_domain=args.owner_domain,
            main_rule_target=args.main_rule_target,
            additional_name=args.additional_name,
            additional_relative_path=args.additional_relative_path,
        )
        packet = packet_report["candidate_packet"]
        stop_gates = packet.get("stop_gates", []) or []
        packet_approved = not stop_gates
        stage_statuses.append(
            stage_entry(
                "packet",
                str(packet_report.get("status")),
                ok=packet_approved,
                summary={
                    "candidate_packet_built": packet_report.get("candidate_packet_built"),
                    "approved_for_trial_write": packet_approved,
                    "stop_gate_count": len(stop_gates),
                },
            )
        )
        reports.append(packet_report)
        if not packet_approved:
            return build_blocked_report(
                status="trial-blocked",
                reason="Candidate packet has stop gates; approved additional-stage write was not attempted.",
                stage_statuses=stage_statuses,
                reports=reports,
                selected_topic=selected_topic,
                packet_report=packet_report,
            )

        emit_report = candidate_packet.emit_additional(
            packet_report,
            additional_root=args.additional_root,
            approved_write=args.approved_write,
            allow_overwrite=args.allow_overwrite,
        )
        emitted = bool(emit_report.get("additional_emission_performed"))
        stage_statuses.append(
            stage_entry(
                "emit",
                str(emit_report.get("status")),
                ok=emit_report.get("status") in {"preview", "emitted"},
                summary={
                    "approved_write": emit_report.get("approved_write"),
                    "additional_emission_performed": emit_report.get("additional_emission_performed"),
                    "destination_relative_path": emit_report.get("destination_relative_path"),
                },
            )
        )
        reports.append(emit_report)
    except (
        LiveTrialError,
        historical_replay.HistoricalReplayError,
        presentation.SelectionError,
        candidate_packet.CandidatePacketError,
    ) as exc:
        stage_statuses.append(stage_entry("downstream-chain", "blocked", ok=False, summary={"reason": str(exc)}))
        return build_blocked_report(
            status="trial-blocked",
            reason=str(exc),
            stage_statuses=stage_statuses,
            reports=reports,
        )

    checks = material_checks(emit_report)
    emitted_and_checked = emitted and bool(checks.get("emitted_file_exists"))
    material_ready = bool(checks.get("material_contains_success_criteria")) and bool(
        checks.get("material_contains_rollback_notes")
    )
    disposition = args.disposition or ("continue" if emitted_and_checked and material_ready else "revise")

    evidence_basis = packet.get("signal_evidence_basis", {}) if isinstance(packet, dict) else {}
    observation_notes = default_observation_notes(
        selected_topic=selected_topic,
        emitted=emitted,
        destination_path=checks.get("destination_path"),
        usefulness_notes=args.usefulness_note,
        risk_notes=args.risk_note,
        required_revisions=args.required_revision,
    )
    status = "trial-emitted" if emitted_and_checked else "trial-preview"

    return {
        "tool": "memory-context-intelligence",
        "mode": "trial",
        "status": status,
        "live_trial_model": LIVE_TRIAL_MODEL,
        "bounded_live_input": {
            "memory_root_source": (intake_report.get("source", {}) or {}).get("memory_root_source"),
            "daily_shards_discovered": (intake_report.get("source", {}) or {}).get("daily_shards_discovered"),
            "daily_shards_considered": (intake_report.get("source", {}) or {}).get("daily_shards_considered", []),
            "scope_filters": (intake_report.get("scope", {}) or {}).get("filters", []),
            "records_sampled": len(intake_report.get("records", []) or []),
            "bounded_subset_only": True,
        },
        "selected_live_topic": {
            "topic_id": selection_report.get("selected_topic_id"),
            "title": selected_topic.get("title"),
            "confidence": selected_topic.get("confidence"),
            "evidence_label": selected_topic.get("evidence_label"),
            "source_signal_ids": selected_topic.get("source_signal_ids", []),
        },
        "selected_topic_evidence_basis": {
            "trace_anchor_count": evidence_basis.get("trace_anchor_count", 0),
            "source_anchor_count": evidence_basis.get("source_anchor_count", 0),
            "trace_anchors": evidence_basis.get("trace_anchors", []),
            "source_anchors": evidence_basis.get("source_anchors", []),
            "evidence_label": evidence_basis.get("evidence_label"),
            "evidence_strength_note": evidence_basis.get("evidence_strength_note"),
        },
        "candidate_packet_approved_for_trial_write": packet_approved,
        "candidate_packet_status": packet_report.get("status"),
        "candidate_packet_stop_gates": stop_gates,
        "owner_domain_mapping": packet.get("owner_domain_mapping", {}),
        "emission": {
            "status": emit_report.get("status"),
            "approved_write": emit_report.get("approved_write"),
            "allow_overwrite": emit_report.get("allow_overwrite"),
            "additional_root": emit_report.get("additional_root"),
            "destination_path": emit_report.get("destination_path"),
            "destination_relative_path": emit_report.get("destination_relative_path"),
            "additional_emission_performed": emit_report.get("additional_emission_performed"),
            "main_rules_mutation_performed": emit_report.get("main_rules_mutation_performed"),
            "install_or_publication_performed": emit_report.get("install_or_publication_performed"),
        },
        "emission_checks": checks,
        "observation_notes": observation_notes,
        "trial_disposition": disposition,
        "success_criteria": packet.get("success_criteria", []),
        "rollback_notes": rollback_notes(checks.get("destination_path")),
        "stage_statuses": stage_statuses,
        "live_trial_boundary_audit": {
            "approved_write_requested": bool(args.approved_write),
            "additional_emission_performed": emitted,
            "emitted_file_exists": bool(checks.get("emitted_file_exists")),
            "material_contains_success_criteria": bool(checks.get("material_contains_success_criteria")),
            "material_contains_rollback_notes": bool(checks.get("material_contains_rollback_notes")),
            "main_rules_mutation_performed": any(bool(report.get("main_rules_mutation_performed")) for report in reports if isinstance(report, dict)),
            "install_or_publication_performed": any(bool(report.get("install_or_publication_performed")) for report in reports if isinstance(report, dict)),
            "live_web_access_performed": any(bool(report.get("live_web_access_performed")) for report in reports if isinstance(report, dict)),
            "external_agent_process_spawned": any(bool(report.get("external_agent_process_spawned")) for report in reports if isinstance(report, dict)),
        },
        "notes": [
            "Live trial uses bounded memory intake and deterministic runtime-local helpers only.",
            "Approved write creates one trial-stage file under the selected additional root when --approved-write is supplied.",
            "Live trial output is phase-015 evidence only; it is not a phase-016 usable-release claim or main RULES promotion approval.",
        ],
        "live_web_access_performed": False,
        "external_agent_process_spawned": False,
        "additional_emission_performed": emitted,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report = build_live_trial_report(args)
    except (OSError, json.JSONDecodeError, LiveTrialError) as exc:
        print(f"memory-context-intelligence trial: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
