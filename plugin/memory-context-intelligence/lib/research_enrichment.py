#!/usr/bin/env python3
"""Optional research enrichment for one selected memory-context topic.

This helper consumes the phase-010 choose-flow output for exactly one selected
candidate topic and either skips enrichment with an explicit reason or evaluates
bounded, controlled source records supplied by the caller. It does not perform
live web access, run native-agent orchestration, build candidate packets, write
/additional/, install anything, or mutate main RULES.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_\-]{2,}", re.IGNORECASE)

STOPWORDS = {
    "about",
    "after",
    "and",
    "before",
    "candidate",
    "context",
    "flow",
    "for",
    "from",
    "into",
    "local",
    "memory",
    "rule",
    "rules",
    "selected",
    "signal",
    "that",
    "the",
    "this",
    "topic",
    "when",
    "with",
}

RESEARCH_NEED_KEYWORDS = (
    "best practice",
    "broader support",
    "external",
    "freshness",
    "governance",
    "industry",
    "policy",
    "presentation strategy",
    "research",
    "safety",
    "source trust",
    "standard",
    "widely shared",
)

LOCAL_ONLY_KEYWORDS = (
    "local naming",
    "local path",
    "local repository",
    "local repo",
    "local sync",
    "purely local",
    "repo topology",
    "workspace path",
)

TRUST_TIERS = {
    "official": (1, "primary official technical authority"),
    "official_docs": (1, "primary official technical authority"),
    "standard": (1, "primary standard or specification"),
    "spec": (1, "primary standard or specification"),
    "maintainer": (2, "maintainer or repository authority"),
    "institutional": (2, "institutional engineering guidance"),
    "engineering_guide": (3, "reputable secondary engineering explanation"),
    "reputable_secondary": (3, "reputable secondary technical explanation"),
    "tutorial": (4, "tutorial or blog source"),
    "blog": (4, "tutorial or blog source"),
    "forum": (5, "weak or anecdotal source"),
    "social": (5, "weak or anecdotal source"),
    "unknown": (5, "unknown or weak-accountability source"),
}

WEAK_TIER_THRESHOLD = 4
HARD_CONSTRAINT_TIER_THRESHOLD = 2


class EnrichmentError(ValueError):
    """Raised when enrichment input is malformed."""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence enrich",
        description=(
            "Consume one phase-010 selected topic report and optionally enrich it "
            "from controlled/recorded source fixtures. No live web access or writes."
        ),
    )
    parser.add_argument(
        "--selection-report",
        default="-",
        help="Path to phase-010 choose JSON. Use '-' or omit to read JSON from stdin.",
    )
    parser.add_argument(
        "--sources-fixture",
        help=(
            "Optional JSON fixture containing recorded sources for research-needed topics. "
            "If omitted, research-needed topics return a skip/blocked decision instead of live lookup."
        ),
    )
    parser.add_argument(
        "--max-sources",
        type=int,
        default=8,
        help="Maximum controlled source records to evaluate, capped at 20.",
    )
    return parser.parse_args(argv)


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))


def load_json_input(path_value: str) -> dict[str, Any]:
    if path_value == "-":
        loaded = json.load(sys.stdin)
    else:
        path = Path(path_value).expanduser()
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise EnrichmentError("JSON input must be an object.")
    return loaded


def load_sources_fixture(path_value: str | None, max_sources: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not path_value:
        return [], {"provided": False, "source_count": 0, "bounded_subset_only": True}

    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)

    if isinstance(loaded, dict):
        raw_sources = loaded.get("sources", [])
        fixture_meta = {
            "provided": True,
            "fixture_path": str(path),
            "fixture_name": loaded.get("name"),
            "recorded_at": loaded.get("recorded_at"),
        }
    elif isinstance(loaded, list):
        raw_sources = loaded
        fixture_meta = {"provided": True, "fixture_path": str(path)}
    else:
        raise EnrichmentError("Sources fixture must be an object with sources[] or a list of sources.")

    if not isinstance(raw_sources, list):
        raise EnrichmentError("Sources fixture 'sources' value must be a list.")

    safe_max_sources = clamp(max_sources, 1, 20)
    sources = [item for item in raw_sources if isinstance(item, dict)][:safe_max_sources]
    fixture_meta.update(
        {
            "source_count": len(sources),
            "raw_source_count": len(raw_sources),
            "max_sources_evaluated": safe_max_sources,
            "bounded_subset_only": len(raw_sources) > len(sources),
        }
    )
    return sources, fixture_meta


def selected_topic_from_report(selection_report: dict[str, Any]) -> dict[str, Any]:
    selected_topic = selection_report.get("selected_topic")
    if not isinstance(selected_topic, dict):
        raise EnrichmentError("Selection report must contain exactly one selected_topic object.")
    if selection_report.get("selection_required_before_carry_forward") is True:
        raise EnrichmentError("Selection report still requires user selection before carry-forward.")
    if selected_topic.get("carry_forward_allowed") is False:
        raise EnrichmentError("Selected topic is not marked carry-forward allowed.")
    return selected_topic


def topic_text(topic: dict[str, Any]) -> str:
    fields = (
        "title",
        "purpose",
        "why_surfaced",
        "expected_behavior_impact",
        "high_level_mechanism",
        "expected_output",
        "research_need",
    )
    values: list[str] = []
    for field in fields:
        value = topic.get(field)
        if isinstance(value, dict):
            values.append(json.dumps(value, ensure_ascii=False))
        elif value is not None:
            values.append(str(value))
    return "\n".join(values)


def interpret_research_need(topic: dict[str, Any]) -> dict[str, Any]:
    direct = topic.get("research_required")
    if isinstance(direct, bool):
        return {
            "research_needed": direct,
            "gate_result": "research-needed" if direct else "skip-research",
            "reason": "Selected topic carries explicit research_required flag.",
            "basis": ["selected_topic.research_required"],
        }

    research_need = topic.get("research_need")
    if isinstance(research_need, dict):
        for key in ("required", "needed", "research_needed"):
            if isinstance(research_need.get(key), bool):
                needed = bool(research_need[key])
                return {
                    "research_needed": needed,
                    "gate_result": "research-needed" if needed else "skip-research",
                    "reason": str(research_need.get("reason") or "Selected topic carries structured research_need decision."),
                    "basis": [f"selected_topic.research_need.{key}"],
                }
        decision = str(research_need.get("decision", "")).lower()
        if decision in {"needed", "research-needed", "required"}:
            return {
                "research_needed": True,
                "gate_result": "research-needed",
                "reason": str(research_need.get("reason") or "Structured research_need decision requires broader support."),
                "basis": ["selected_topic.research_need.decision"],
            }
        if decision in {"not-needed", "skip", "skip-research", "local-only"}:
            return {
                "research_needed": False,
                "gate_result": "skip-research",
                "reason": str(research_need.get("reason") or "Structured research_need decision says the topic is local-only."),
                "basis": ["selected_topic.research_need.decision"],
            }

    lowered = topic_text(topic).lower()
    local_matches = [keyword for keyword in LOCAL_ONLY_KEYWORDS if keyword in lowered]
    if local_matches:
        return {
            "research_needed": False,
            "gate_result": "skip-research",
            "reason": "Topic appears local-only, so external support would not materially change the decision.",
            "basis": [f"matched local-only keyword: {item}" for item in local_matches[:3]],
        }

    research_matches = [keyword for keyword in RESEARCH_NEED_KEYWORDS if keyword in lowered]
    if research_matches:
        return {
            "research_needed": True,
            "gate_result": "research-needed",
            "reason": "Topic depends on broader support beyond local memory signals.",
            "basis": [f"matched research keyword: {item}" for item in research_matches[:4]],
        }

    return {
        "research_needed": False,
        "gate_result": "skip-research",
        "reason": "No explicit or heuristic signal shows external research is needed for this selected topic.",
        "basis": ["no explicit research_required flag", "no broader-support keyword match"],
    }


def extract_keywords(text: str, limit: int = 6) -> list[str]:
    seen: set[str] = set()
    keywords: list[str] = []
    for match in TOKEN_RE.finditer(text.lower()):
        token = match.group(0).strip("-_")
        if token in STOPWORDS or token.isdigit() or token in seen:
            continue
        seen.add(token)
        keywords.append(token)
        if len(keywords) >= limit:
            break
    return keywords


def source_query_plan(topic: dict[str, Any], decision: dict[str, Any]) -> dict[str, Any]:
    keywords = extract_keywords(topic_text(topic))
    title = str(topic.get("title") or "selected memory-context topic")
    if not decision["research_needed"]:
        return {
            "required": False,
            "decision_surface": title,
            "query_families": [],
            "preferred_source_families": [],
            "reason": "Research plan not opened because the enrichment gate skipped research.",
        }

    compact_keywords = " ".join(keywords[:4]) or title
    return {
        "required": True,
        "decision_surface": title,
        "query_families": [
            {
                "label": "primary authority",
                "query": f"{compact_keywords} official documentation standard guidance",
                "purpose": "Look for primary, normative, or maintainer-owned constraints before weaker commentary.",
            },
            {
                "label": "practice and rationale",
                "query": f"{compact_keywords} engineering practice rationale tradeoffs",
                "purpose": "Check whether reputable engineering guidance supports the proposed mechanism.",
            },
            {
                "label": "conflicts and limits",
                "query": f"{compact_keywords} limitations pitfalls conflicting guidance",
                "purpose": "Look for conflicting evidence and weak-source caveats before strengthening the topic.",
            },
        ],
        "preferred_source_families": [
            "primary official documentation, standards, or specs",
            "maintainer or institutional engineering guidance",
            "reputable secondary technical explanations",
            "weak/accountability-light sources only as context, not hard constraints",
        ],
        "reason": "Research-needed topics need source-trust and conflict review before candidate packet building.",
    }


def normalize_source_type(source: dict[str, Any]) -> str:
    raw = str(source.get("source_type") or source.get("type") or "unknown").lower().replace("-", "_").strip()
    return raw or "unknown"


def trust_for_source(source: dict[str, Any]) -> tuple[int, str]:
    source_type = normalize_source_type(source)
    if isinstance(source.get("trust_tier"), int):
        tier = clamp(int(source["trust_tier"]), 1, 5)
        label = str(source.get("trust_label") or TRUST_TIERS.get(source_type, TRUST_TIERS["unknown"])[1])
        return tier, label
    return TRUST_TIERS.get(source_type, TRUST_TIERS["unknown"])


def list_value(source: dict[str, Any], key: str) -> list[str]:
    value = source.get(key, [])
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_source(source: dict[str, Any], index: int) -> dict[str, Any]:
    tier, trust_label = trust_for_source(source)
    source_id = str(source.get("id") or f"source-{index:03d}")
    freshness = str(source.get("freshness") or source.get("freshness_class") or "unknown").lower()
    if freshness in {"fresh", "current", "recent"}:
        freshness_class = "current"
    elif freshness in {"stale", "outdated"}:
        freshness_class = "stale"
    else:
        freshness_class = "unknown"

    conflicts = list_value(source, "conflicts")
    limitations = list_value(source, "limitations") + list_value(source, "weaknesses")
    supports = list_value(source, "supports") + list_value(source, "claims")
    constraints = list_value(source, "constraints")
    stance = str(source.get("stance") or "supports").lower()
    conflicting = bool(conflicts) or stance in {"conflicts", "contradicts", "mixed"}

    return {
        "id": source_id,
        "title": source.get("title") or source_id,
        "url": source.get("url"),
        "source_type": normalize_source_type(source),
        "trust_tier": tier,
        "trust_label": trust_label,
        "freshness": {
            "classification": freshness_class,
            "published": source.get("published") or source.get("published_at"),
            "checked_at": source.get("checked_at"),
            "note": source.get("freshness_note"),
        },
        "summary": source.get("summary"),
        "supports": supports,
        "constraints": constraints,
        "conflicts": conflicts,
        "limitations": limitations,
        "conflicting": conflicting,
        "weak_source": tier >= WEAK_TIER_THRESHOLD,
    }


def review_sources(sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [normalize_source(source, index) for index, source in enumerate(sources, start=1)]


def source_trust_notes(reviewed_sources: list[dict[str, Any]]) -> dict[str, Any]:
    strong = [source for source in reviewed_sources if source["trust_tier"] <= 2]
    medium = [source for source in reviewed_sources if 2 < source["trust_tier"] < WEAK_TIER_THRESHOLD]
    weak = [source for source in reviewed_sources if source["weak_source"]]
    return {
        "strong_sources": [source["id"] for source in strong],
        "medium_sources": [source["id"] for source in medium],
        "weak_sources": [source["id"] for source in weak],
        "notes": [
            f"{source['id']}: tier {source['trust_tier']} - {source['trust_label']}"
            for source in reviewed_sources
        ],
        "weak_source_handling": (
            "Weak sources are retained as context only and cannot create hard constraints."
            if weak
            else "No weak sources were present in the bounded fixture."
        ),
    }


def freshness_notes(reviewed_sources: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "source_freshness": [
            {
                "id": source["id"],
                "classification": source["freshness"]["classification"],
                "published": source["freshness"].get("published"),
                "checked_at": source["freshness"].get("checked_at"),
                "note": source["freshness"].get("note"),
            }
            for source in reviewed_sources
        ],
        "stale_or_unknown_sources": [
            source["id"]
            for source in reviewed_sources
            if source["freshness"]["classification"] in {"stale", "unknown"}
        ],
        "note": "Freshness is taken from the controlled source records; no live refresh is performed by phase 011.",
    }


def conflict_handling(reviewed_sources: list[dict[str, Any]]) -> dict[str, Any]:
    conflicts = [
        {"source_id": source["id"], "conflicts": source["conflicts"] or ["source stance marked mixed/conflicting"]}
        for source in reviewed_sources
        if source["conflicting"]
    ]
    weak_conflicting = [source["id"] for source in reviewed_sources if source["weak_source"] and source["conflicting"]]
    return {
        "conflicts_found": bool(conflicts),
        "conflicts": conflicts,
        "weak_conflicting_sources": weak_conflicting,
        "handling": (
            "Conflicts remain limitation notes unless stronger primary evidence directly settles the point."
            if conflicts
            else "No explicit conflicts were present in the bounded fixture."
        ),
        "hard_constraint_rule": "Only tier 1-2 non-conflicting source constraints can become hard constraints in this enrichment output.",
    }


def accepted_external_support(reviewed_sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    accepted: list[dict[str, Any]] = []
    for source in reviewed_sources:
        if source["weak_source"] or source["conflicting"]:
            continue
        for claim in source["supports"]:
            accepted.append({"source_id": source["id"], "claim": claim, "trust_tier": source["trust_tier"]})
    return accepted


def hard_constraints(reviewed_sources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    constraints: list[dict[str, Any]] = []
    for source in reviewed_sources:
        if source["trust_tier"] > HARD_CONSTRAINT_TIER_THRESHOLD or source["weak_source"] or source["conflicting"]:
            continue
        for constraint in source["constraints"]:
            constraints.append({"source_id": source["id"], "constraint": constraint, "trust_tier": source["trust_tier"]})
    return constraints


def enriched_topic_summary(topic: dict[str, Any], reviewed_sources: list[dict[str, Any]]) -> dict[str, Any]:
    accepted = accepted_external_support(reviewed_sources)
    constraints = hard_constraints(reviewed_sources)
    weak_context = [
        {"source_id": source["id"], "supports": source["supports"], "limitations": source["limitations"]}
        for source in reviewed_sources
        if source["weak_source"]
    ]
    conflicts = conflict_handling(reviewed_sources)
    if accepted and not conflicts["conflicts_found"]:
        confidence = "externally-supported-with-bounded-limits"
    elif accepted:
        confidence = "partially-supported-with-conflicts"
    else:
        confidence = "local-signal-only-after-source-review"

    return {
        "local_memory_signal": {
            "topic_id": topic.get("id"),
            "title": topic.get("title"),
            "purpose": topic.get("purpose"),
            "why_surfaced": topic.get("why_surfaced"),
            "confidence": topic.get("confidence"),
            "evidence_label": topic.get("evidence_label"),
            "source_signal_ids": topic.get("source_signal_ids", []),
        },
        "external_support": accepted,
        "weak_source_context_only": weak_context,
        "hard_constraints_from_external_support": constraints,
        "conflict_limitations": conflicts["conflicts"],
        "confidence_after_enrichment": confidence,
        "boundary_note": "External support can strengthen the selected topic, but it does not approve candidate packets or mutate RULES.",
    }


def skip_summary(topic: dict[str, Any], reason: str) -> dict[str, Any]:
    return {
        "local_memory_signal": {
            "topic_id": topic.get("id"),
            "title": topic.get("title"),
            "purpose": topic.get("purpose"),
            "why_surfaced": topic.get("why_surfaced"),
            "confidence": topic.get("confidence"),
            "evidence_label": topic.get("evidence_label"),
            "source_signal_ids": topic.get("source_signal_ids", []),
        },
        "external_support": [],
        "weak_source_context_only": [],
        "hard_constraints_from_external_support": [],
        "conflict_limitations": [],
        "confidence_after_enrichment": "local-signal-only-research-skipped",
        "boundary_note": reason,
    }


def boundary_flags(*, enrichment_performed: bool, fixture_used: bool) -> dict[str, bool]:
    return {
        "research_enrichment_performed": enrichment_performed,
        "controlled_source_fixture_used": fixture_used,
        "live_web_access_performed": False,
        "native_agent_orchestration_performed": False,
        "candidate_packet_built": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
        "install_or_publication_performed": False,
    }


def build_enrichment(
    selection_report: dict[str, Any],
    *,
    source_fixture: dict[str, Any] | list[dict[str, Any]] | None = None,
    max_sources: int = 8,
) -> dict[str, Any]:
    topic = selected_topic_from_report(selection_report)
    decision = interpret_research_need(topic)
    plan = source_query_plan(topic, decision)

    raw_sources: list[dict[str, Any]] = []
    fixture_meta: dict[str, Any] = {"provided": False, "source_count": 0, "bounded_subset_only": True}
    if isinstance(source_fixture, dict):
        fixture_sources = source_fixture.get("sources", [])
        if not isinstance(fixture_sources, list):
            raise EnrichmentError("source_fixture['sources'] must be a list.")
        raw_sources = [source for source in fixture_sources if isinstance(source, dict)][: clamp(max_sources, 1, 20)]
        fixture_meta = {
            "provided": True,
            "fixture_name": source_fixture.get("name"),
            "recorded_at": source_fixture.get("recorded_at"),
            "source_count": len(raw_sources),
            "raw_source_count": len(fixture_sources),
            "max_sources_evaluated": clamp(max_sources, 1, 20),
            "bounded_subset_only": len(fixture_sources) > len(raw_sources),
        }
    elif isinstance(source_fixture, list):
        raw_sources = [source for source in source_fixture if isinstance(source, dict)][: clamp(max_sources, 1, 20)]
        fixture_meta = {
            "provided": True,
            "source_count": len(raw_sources),
            "raw_source_count": len(source_fixture),
            "max_sources_evaluated": clamp(max_sources, 1, 20),
            "bounded_subset_only": len(source_fixture) > len(raw_sources),
        }

    if not decision["research_needed"]:
        reason = decision["reason"]
        return {
            "tool": "memory-context-intelligence",
            "mode": "enrich",
            "status": "research-skipped",
            "selected_topic_id": topic.get("id"),
            "enrichment_decision": decision,
            "source_query_plan": plan,
            "source_fixture": fixture_meta,
            "reviewed_sources": [],
            "source_trust_notes": {
                "strong_sources": [],
                "medium_sources": [],
                "weak_sources": [],
                "notes": [],
                "weak_source_handling": "No sources evaluated because the gate skipped research.",
            },
            "freshness_notes": {
                "source_freshness": [],
                "stale_or_unknown_sources": [],
                "note": "No source freshness review was needed because research was skipped.",
            },
            "conflict_handling": {
                "conflicts_found": False,
                "conflicts": [],
                "weak_conflicting_sources": [],
                "handling": "No sources evaluated because the gate skipped research.",
                "hard_constraint_rule": "No external hard constraints are created when research is skipped.",
            },
            "enriched_topic_summary": skip_summary(topic, reason),
            "notes": [
                reason,
                "Candidate packet building has not been performed by enrich mode.",
                "/additional/ emission has not been performed by enrich mode.",
                "Main RULES mutation has not been performed by enrich mode.",
                "Native-agent orchestration is available through orchestrate mode, not enrich mode.",
            ],
            **boundary_flags(enrichment_performed=False, fixture_used=False),
        }

    if not raw_sources:
        reason = "Research is needed, but no controlled/recorded source fixture was provided; live web access is not performed in phase 011."
        skipped_decision = {
            **decision,
            "gate_result": "research-needed-no-sources",
            "skip_reason": reason,
        }
        return {
            "tool": "memory-context-intelligence",
            "mode": "enrich",
            "status": "research-skipped",
            "selected_topic_id": topic.get("id"),
            "enrichment_decision": skipped_decision,
            "source_query_plan": plan,
            "source_fixture": fixture_meta,
            "reviewed_sources": [],
            "source_trust_notes": {
                "strong_sources": [],
                "medium_sources": [],
                "weak_sources": [],
                "notes": [],
                "weak_source_handling": "No sources evaluated; weak-source handling could not run.",
            },
            "freshness_notes": {
                "source_freshness": [],
                "stale_or_unknown_sources": [],
                "note": "No source freshness review was possible without a controlled fixture.",
            },
            "conflict_handling": {
                "conflicts_found": False,
                "conflicts": [],
                "weak_conflicting_sources": [],
                "handling": "No sources evaluated; conflict review could not run.",
                "hard_constraint_rule": "No external hard constraints are created without reviewed sources.",
            },
            "enriched_topic_summary": skip_summary(topic, reason),
            "notes": [
                reason,
                "Provide --sources-fixture with controlled/recorded sources to produce an enriched summary.",
                "Candidate packet building has not been performed by enrich mode.",
                "/additional/ emission has not been performed by enrich mode.",
                "Main RULES mutation has not been performed by enrich mode.",
                "Native-agent orchestration is available through orchestrate mode, not enrich mode.",
            ],
            **boundary_flags(enrichment_performed=False, fixture_used=False),
        }

    reviewed_sources = review_sources(raw_sources)
    return {
        "tool": "memory-context-intelligence",
        "mode": "enrich",
        "status": "research-enriched",
        "selected_topic_id": topic.get("id"),
        "enrichment_decision": decision,
        "source_query_plan": plan,
        "source_fixture": fixture_meta,
        "reviewed_sources": reviewed_sources,
        "source_trust_notes": source_trust_notes(reviewed_sources),
        "freshness_notes": freshness_notes(reviewed_sources),
        "conflict_handling": conflict_handling(reviewed_sources),
        "enriched_topic_summary": enriched_topic_summary(topic, reviewed_sources),
        "notes": [
            "Research enrichment used controlled/recorded sources only; no live web access was performed.",
            "Weak or conflicting sources are limitation/context notes, not hard constraints.",
            "Candidate packet building has not been performed by enrich mode.",
            "/additional/ emission has not been performed by enrich mode.",
            "Main RULES mutation has not been performed by enrich mode.",
            "Native-agent orchestration is available through orchestrate mode, not enrich mode.",
        ],
        **boundary_flags(enrichment_performed=True, fixture_used=True),
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        selection_report = load_json_input(args.selection_report)
        sources, fixture_meta = load_sources_fixture(args.sources_fixture, args.max_sources)
        source_fixture: dict[str, Any] | None = None
        if fixture_meta.get("provided"):
            source_fixture = {**fixture_meta, "sources": sources}
        report = build_enrichment(selection_report, source_fixture=source_fixture, max_sources=args.max_sources)
    except (OSError, json.JSONDecodeError, EnrichmentError) as exc:
        print(f"memory-context-intelligence enrich: {exc}", file=sys.stderr)
        return 2

    json.dump(report, fp=sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
