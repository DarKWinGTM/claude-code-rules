#!/usr/bin/env python3
"""Internal signal and topic generation for memory-context-intelligence.

This helper consumes bounded intake JSON and emits an internal-only analysis
report. It does not run a choose flow, perform external research, write
/additional/, or mutate main RULES.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

GROUP_KEYS = ("recurring_patterns", "corrections", "blockers", "evidence_gaps")
GROUP_LABELS = {
    "recurring_patterns": "recurring pattern",
    "corrections": "correction",
    "blockers": "blocker",
    "evidence_gaps": "evidence gap",
}
KIND_TO_GROUP = {
    "recurring_pattern": "recurring_patterns",
    "correction": "corrections",
    "blocker": "blockers",
    "evidence_gap": "evidence_gaps",
}
GROUP_TO_KIND = {group: kind for kind, group in KIND_TO_GROUP.items()}
KIND_PRIORITY = ("evidence_gap", "blocker", "correction", "recurring_pattern")
SOURCE_CLASS_ORDER = (
    "trace_evidence",
    "recall_evidence",
    "durable_memory_context",
    "governance_context",
)

STOPWORDS = {
    "a",
    "about",
    "after",
    "all",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "but",
    "by",
    "can",
    "do",
    "does",
    "for",
    "from",
    "has",
    "have",
    "in",
    "into",
    "is",
    "it",
    "its",
    "keep",
    "must",
    "not",
    "of",
    "on",
    "only",
    "or",
    "rather",
    "should",
    "than",
    "that",
    "the",
    "this",
    "to",
    "use",
    "when",
    "with",
    "without",
    "yet",
}

KIND_PATTERNS = {
    "evidence_gap": (
        "unverified",
        "not verified",
        "insufficient",
        "stale",
        "no evidence",
        "missing evidence",
        "evidence gap",
        "not found",
        "unchecked",
        "hypothesis",
        "needs recheck",
        "needs verification",
    ),
    "blocker": (
        "blocked",
        "blocker",
        "cannot",
        "can't",
        "missing",
        "unavailable",
        "denied",
        "fails",
        "failed",
        "error",
        "stop gate",
        "approval",
        "needs approval",
    ),
    "correction": (
        "do not",
        "don't",
        "avoid",
        "instead",
        "prefer",
        "must",
        "should",
        "wrong",
        "overstate",
        "claim",
        "verify",
        "feedback",
        "correct",
    ),
    "recurring_pattern": (
        "recurring",
        "repeated",
        "always",
        "each time",
        "whenever",
        "pattern",
        "workflow",
        "keep",
        "use",
    ),
}

PURPOSE_BY_KIND = {
    "recurring_pattern": "Review repeated workflow behavior against the intended RULES/workflow purpose so future responses stay aligned to design intent.",
    "correction": "Convert repeated user corrections into a candidate behavior adjustment without treating the correction as doctrine yet.",
    "blocker": "Expose recurring blockers that may need clearer workflow gates, recovery paths, or ownership boundaries.",
    "evidence_gap": "Highlight places where weak, stale, or missing evidence should keep future claims cautious.",
}

IMPACT_BY_KIND = {
    "recurring_pattern": "Future behavior could stay closer to the intended RULES/workflow-review purpose instead of drifting into generic trace-pattern mining.",
    "correction": "Future behavior could avoid repeating the corrected mistake if the topic later becomes a vetted candidate.",
    "blocker": "Future workflow could surface stop gates earlier and reduce blocked or unsafe continuation.",
    "evidence_gap": "Future responses could downgrade confidence sooner and ask for or gather evidence before strong claims.",
}

MECHANISM_BY_KIND = {
    "recurring_pattern": "Cluster similar bounded intake records, then frame the result as a review issue against the intended workflow/design purpose instead of a generic recurring-pattern summary.",
    "correction": "Cluster correction-shaped records, preserve evidence labels, and propose an internal topic only when the pattern is repeated enough.",
    "blocker": "Cluster blocker-shaped records and map them to a possible workflow gate or recovery-path improvement.",
    "evidence_gap": "Cluster evidence-gap records and cap promotion when the source input is stale, weak, or single-observation only.",
}

OUTPUT_BY_KIND = {
    "recurring_pattern": "A reviewed design/workflow issue candidate describing what drifted from the intended purpose and what behavior could change.",
    "correction": "A reviewed topic candidate that can later be presented for user selection before any candidate packet is built.",
    "blocker": "A reviewed topic candidate for clearer stop-gate, blocker, or recovery handling.",
    "evidence_gap": "A reviewed topic candidate for evidence discipline, confidence labeling, or recheck behavior.",
}

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_\-]{2,}", re.IGNORECASE)
WHITESPACE_RE = re.compile(r"\s+")


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="memory-context-intelligence signals",
        description=(
            "Consume a bounded intake JSON report and emit an internal-only "
            "signal/topic analysis report."
        ),
    )
    parser.add_argument(
        "--intake-report",
        default="-",
        help="Path to bounded intake JSON. Use '-' or omit to read JSON from stdin.",
    )
    parser.add_argument(
        "--max-records",
        type=int,
        default=50,
        help="Maximum intake records to analyze from the already bounded report, capped at 100.",
    )
    parser.add_argument(
        "--max-topics",
        type=int,
        default=8,
        help="Maximum promoted internal topic candidates, capped at 20.",
    )
    return parser.parse_args(argv)


def load_json_input(path_value: str) -> dict[str, Any]:
    if path_value == "-":
        return json.load(sys.stdin)
    path = Path(path_value).expanduser()
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_text(text: str) -> str:
    normalized = text.lower().replace("’", "'")
    normalized = re.sub(r"https?://\S+", " ", normalized)
    normalized = re.sub(r"[`*_\[\](){}<>#:\\/@|]+", " ", normalized)
    normalized = WHITESPACE_RE.sub(" ", normalized)
    return normalized.strip()


def stem_token(token: str) -> str:
    token = token.lower().strip("-_")
    if len(token) > 6 and token.endswith("ing"):
        return token[:-3]
    if len(token) > 5 and token.endswith("ed"):
        return token[:-2]
    if len(token) > 4 and token.endswith("es"):
        return token[:-2]
    if len(token) > 4 and token.endswith("s"):
        return token[:-1]
    return token


def extract_tokens(text: str) -> list[str]:
    tokens = [stem_token(match.group(0)) for match in TOKEN_RE.finditer(normalize_text(text))]
    return [token for token in tokens if token and token not in STOPWORDS and not token.isdigit()]


def classify_kind(content: str) -> str:
    lowered = normalize_text(content)
    scores: dict[str, int] = {}
    for kind, patterns in KIND_PATTERNS.items():
        scores[kind] = sum(1 for pattern in patterns if pattern in lowered)
    if not any(scores.values()):
        return "recurring_pattern"
    return max(KIND_PRIORITY, key=lambda kind: (scores[kind], -KIND_PRIORITY.index(kind)))


def jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def should_merge(cluster: dict[str, Any], kind: str, tokens: set[str], normalized: str) -> bool:
    if cluster["kind"] != kind:
        return False
    cluster_tokens = set(cluster["token_counts"].keys())
    token_overlap = jaccard(cluster_tokens, tokens)
    text_overlap = max(
        SequenceMatcher(None, normalized, item).ratio() for item in cluster["normalized_examples"]
    )
    shared_tokens = len(cluster_tokens & tokens)
    return token_overlap >= 0.42 or text_overlap >= 0.62 or (shared_tokens >= 4 and token_overlap >= 0.30)


def record_source_classes(record: dict[str, Any]) -> list[str]:
    raw = record.get("source_classes")
    if isinstance(raw, list):
        values = [str(item) for item in raw if item]
        if values:
            return list(dict.fromkeys(values))
    return ["trace_evidence"]


def cluster_source_classes(cluster: dict[str, Any]) -> list[str]:
    return [source_class for source_class in SOURCE_CLASS_ORDER if cluster["source_class_counts"].get(source_class)]


def source_mix_label(cluster: dict[str, Any]) -> str:
    classes = cluster_source_classes(cluster)
    return " + ".join(classes) if classes else "trace_evidence"


def trace_record_count(cluster: dict[str, Any]) -> int:
    return int(cluster["source_class_counts"].get("trace_evidence", 0))


def unique_trace_shards(cluster: dict[str, Any]) -> set[str]:
    values: set[str] = set()
    for record in cluster["records"]:
        if "trace_evidence" in record_source_classes(record) and record.get("shard"):
            values.add(str(record.get("shard")))
    return values


def parse_shard_day(record: dict[str, Any]) -> date | None:
    shard = str(record.get("shard") or "")
    if not shard.endswith(".md"):
        return None
    try:
        return datetime.strptime(shard[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def trace_session_ids(cluster: dict[str, Any]) -> list[str]:
    return sorted(
        {
            str(record.get("session_id"))
            for record in cluster["records"]
            if "trace_evidence" in record_source_classes(record) and record.get("session_id")
        }
    )


def latest_trace_day(cluster: dict[str, Any]) -> date | None:
    days = [parse_shard_day(record) for record in cluster["records"] if "trace_evidence" in record_source_classes(record)]
    valid_days = [day for day in days if day is not None]
    return max(valid_days) if valid_days else None


def historical_strength_label(cluster: dict[str, Any]) -> str:
    return (
        f"{trace_record_count(cluster)} trace record(s) across "
        f"{len(trace_session_ids(cluster)) or 1} session(s) and "
        f"{len(unique_trace_shards(cluster)) or 1} shard(s)"
    )


def current_session_confirmation_label(cluster: dict[str, Any], current_session_id: str | None) -> str:
    if current_session_id and any(
        record.get("session_id") == current_session_id and "trace_evidence" in record_source_classes(record)
        for record in cluster["records"]
    ):
        return "confirmed-in-current-session"
    return "historical-only"


def make_cluster(record: dict[str, Any], index: int) -> dict[str, Any]:
    content = str(record.get("content", "")).strip()
    tokens = extract_tokens(content)
    kind = classify_kind(content)
    return {
        "id": f"signal-{index:03d}",
        "kind": kind,
        "group": KIND_TO_GROUP[kind],
        "token_counts": Counter(tokens),
        "source_class_counts": Counter(record_source_classes(record)),
        "records": [record],
        "normalized_examples": [normalize_text(content)],
    }


def add_to_cluster(cluster: dict[str, Any], record: dict[str, Any]) -> None:
    content = str(record.get("content", "")).strip()
    cluster["records"].append(record)
    cluster["token_counts"].update(extract_tokens(content))
    cluster["source_class_counts"].update(record_source_classes(record))
    cluster["normalized_examples"].append(normalize_text(content))


def cluster_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    clusters: list[dict[str, Any]] = []
    for record in records:
        content = str(record.get("content", "")).strip()
        if not content:
            continue
        kind = classify_kind(content)
        tokens = set(extract_tokens(content))
        normalized = normalize_text(content)
        target = next(
            (cluster for cluster in clusters if should_merge(cluster, kind, tokens, normalized)),
            None,
        )
        if target is None:
            clusters.append(make_cluster(record, len(clusters) + 1))
        else:
            add_to_cluster(target, record)
    return clusters


def confidence_for_cluster(cluster: dict[str, Any], intake_report: dict[str, Any]) -> str:
    status = str(intake_report.get("status", "unknown"))
    freshness = intake_report.get("freshness", {}) if isinstance(intake_report.get("freshness"), dict) else {}
    freshness_class = str(freshness.get("classification", "unknown"))
    trace_count = trace_record_count(cluster)
    recall_count = int(cluster["source_class_counts"].get("recall_evidence", 0))
    durable_count = int(cluster["source_class_counts"].get("durable_memory_context", 0))
    governance_count = int(cluster["source_class_counts"].get("governance_context", 0))
    unique_shards = unique_trace_shards(cluster)
    breadth = trace_session_ids(cluster)
    current_confirmation = current_session_confirmation_label(cluster, os.environ.get("CLAUDE_CODE_SESSION_ID"))

    if status != "available" or freshness_class == "stale":
        return "low"
    if trace_count >= 3 and len(unique_shards) >= 2:
        return "high"
    if trace_count >= 2:
        if current_confirmation == "historical-only" and len(breadth) == 1 and len(unique_shards) == 1:
            return "low"
        return "medium"
    if trace_count >= 1 and (recall_count > 0 or durable_count > 0 or governance_count > 0):
        return "medium"
    return "low"


def evidence_label_for_cluster(cluster: dict[str, Any], intake_report: dict[str, Any], confidence: str) -> str:
    status = str(intake_report.get("status", "unknown"))
    if status == "stale":
        return "stale-observed-local-low-confidence"
    if status in {"insufficient", "unavailable"}:
        return "insufficient-input"
    if trace_record_count(cluster) == 0:
        return "bounded-context-only-low-confidence"
    if confidence == "high":
        return "bounded-repeated-multi-shard"
    if confidence == "medium":
        return "bounded-repeated-observed-local"
    return "bounded-single-observation-low-confidence"


def score_cluster(cluster: dict[str, Any], confidence: str) -> float:
    trace_count = trace_record_count(cluster)
    breadth = len(trace_session_ids(cluster))
    unique_shards = unique_trace_shards(cluster)
    recall_count = int(cluster["source_class_counts"].get("recall_evidence", 0))
    durable_count = int(cluster["source_class_counts"].get("durable_memory_context", 0))
    governance_count = int(cluster["source_class_counts"].get("governance_context", 0))
    latest_day = latest_trace_day(cluster)
    recency_boost = 0.0
    if latest_day is not None and (date.today() - latest_day).days <= 7:
        recency_boost = 0.05
    current_session_boost = 0.04 if current_session_confirmation_label(cluster, os.environ.get("CLAUDE_CODE_SESSION_ID")) == "confirmed-in-current-session" else 0.0
    kind_boost = {
        "evidence_gap": 0.12,
        "blocker": 0.10,
        "correction": 0.10,
        "recurring_pattern": 0.05,
    }[cluster["kind"]]

    if trace_count == 0:
        score = 0.18 + min(durable_count + governance_count + recall_count, 4) * 0.04 + kind_boost
        return round(min(score, 0.45), 3)

    score = 0.20 + min(trace_count, 6) * 0.12 + min(breadth, 4) * 0.06 + min(len(unique_shards), 4) * 0.04 + kind_boost
    if recall_count > 0:
        score += 0.04
    if durable_count > 0:
        score += 0.03
    if governance_count > 0:
        score += 0.04
    score += recency_boost + current_session_boost
    if confidence == "medium":
        score += 0.04
    elif confidence == "high":
        score += 0.10
    return round(min(score, 1.0), 3)


def top_keywords(cluster: dict[str, Any], limit: int = 5) -> list[str]:
    return [token for token, _count in cluster["token_counts"].most_common(limit)]


def label_for_cluster(cluster: dict[str, Any]) -> str:
    keywords = top_keywords(cluster, limit=4)
    keyword_text = ", ".join(keywords) if keywords else "unclear pattern"
    return f"{GROUP_LABELS[cluster['group']].title()}: {keyword_text}"


def record_refs(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    refs: list[dict[str, Any]] = []
    for record in records:
        content = str(record.get("content", ""))
        refs.append(
            {
                "shard": record.get("shard"),
                "section": record.get("section"),
                "session_id": record.get("session_id"),
                "source_classes": record_source_classes(record),
                "content_preview": content[:220] + ("..." if len(content) > 220 else ""),
            }
        )
    return refs


def infer_review_focus(signal: dict[str, Any]) -> str:
    keywords = {str(item).lower() for item in signal.get("keywords", [])}
    if keywords & {"evidence", "boundari", "observ", "workaround", "support", "expectation", "refresh", "wait", "retry"}:
        return "evidence-boundary"
    if keywords & {"plugin", "harness", "user", "surface", "cli", "mcp", "bin"}:
        return "surface-boundary"
    return "workflow-review"


def source_session_ids(cluster: dict[str, Any]) -> list[str]:
    values = sorted({str(record.get("session_id")) for record in cluster["records"] if record.get("session_id")})
    return values


def source_scope_label(cluster: dict[str, Any], intake_report: dict[str, Any]) -> str:
    if trace_record_count(cluster) == 0:
        return "non-trace-context-only"
    basis = (intake_report.get("scope") or {}).get("basis")
    current_label = current_session_confirmation_label(cluster, os.environ.get("CLAUDE_CODE_SESSION_ID"))
    if basis in {"explicit-session", "explicit-day-and-session"}:
        return "explicit-current-session-slice"
    if basis == "explicit-day":
        return "explicit-day-slice"
    if current_label == "confirmed-in-current-session":
        return "historical-default+current-session-confirmed"
    return "historical-default"


def provenance_note(cluster: dict[str, Any], intake_report: dict[str, Any]) -> str:
    latest_day = latest_trace_day(cluster)
    strength = historical_strength_label(cluster)
    current_label = current_session_confirmation_label(cluster, os.environ.get("CLAUDE_CODE_SESSION_ID"))
    latest_text = latest_day.isoformat() if latest_day else "unknown"
    note = (
        f"Historical trace evidence is the primary signal. {strength}. Latest seen: {latest_text}. "
        f"Current-session confirmation: {current_label}. Source mix: {source_mix_label(cluster)}."
    )
    source_policy = intake_report.get("source_policy") if isinstance(intake_report.get("source_policy"), dict) else {}
    policy_note = str(source_policy.get("policy_note") or "").strip()
    if source_policy.get("policy_limited") and policy_note:
        return f"{note} {policy_note}"
    return note


def ranked_signal_from_cluster(
    cluster: dict[str, Any], intake_report: dict[str, Any], rank: int
) -> dict[str, Any]:
    confidence = confidence_for_cluster(cluster, intake_report)
    evidence_label = evidence_label_for_cluster(cluster, intake_report, confidence)
    return {
        "rank": rank,
        "id": cluster["id"],
        "kind": cluster["kind"],
        "group": cluster["group"],
        "label": label_for_cluster(cluster),
        "score": score_cluster(cluster, confidence),
        "confidence": confidence,
        "evidence_label": evidence_label,
        "record_count": len(cluster["records"]),
        "keywords": top_keywords(cluster),
        "review_focus": infer_review_focus({"keywords": top_keywords(cluster)}),
        "source_session_ids": source_session_ids(cluster),
        "source_scope_label": source_scope_label(cluster, intake_report),
        "source_classes": cluster_source_classes(cluster),
        "source_mix_label": source_mix_label(cluster),
        "trace_record_count": trace_record_count(cluster),
        "historical_strength": historical_strength_label(cluster),
        "latest_seen": latest_trace_day(cluster).isoformat() if latest_trace_day(cluster) else None,
        "current_session_confirmation": current_session_confirmation_label(cluster, os.environ.get("CLAUDE_CODE_SESSION_ID")),
        "provenance_note": provenance_note(cluster, intake_report),
        "records": record_refs(cluster["records"]),
    }


def signal_keyword_set(signal: dict[str, Any]) -> set[str]:
    return {str(item).lower() for item in signal.get("keywords", []) if item}


def record_text_blob(signal: dict[str, Any]) -> str:
    return " ".join(str(record.get("content_preview", "")).lower() for record in signal.get("records", []))


def contains_any(text: str, fragments: tuple[str, ...]) -> bool:
    return any(fragment in text for fragment in fragments)


def doctrine_trace_example(signal: dict[str, Any]) -> str:
    record_text = record_text_blob(signal)
    if contains_any(record_text, ("supplierapidomainprobe", "passstatuscodes", "opera_fallback")):
        return "Trace example: `supplierApiDomainProbe` / `passStatusCodes` was inspected while `404` and `opera_fallback` were being used to reason about fallback behavior."
    if contains_any(record_text, ("progress summary", "operator-facing", "runtime context")):
        return "Trace example: `/memory-context-intelligence:analysis` returned progress-summary or runtime-context wording instead of operator-facing proposal output."
    if contains_any(record_text, ("claim completion before verification", "completion before verification")):
        return "Trace example: completion wording was being used before matching verification evidence existed."
    if contains_any(record_text, ("approval", "stop gate")):
        return "Trace example: approval remained a blocker while the stop gate or recovery path stayed underspecified."
    if contains_any(record_text, ("refresh", "15s wait", "wait guidance")):
        return "Trace example: refresh or wait guidance was stated more strongly than the supporting evidence."
    if contains_any(record_text, ("private/operator disclosure", "customer-facing", "operator-facing", "disclosure wording", "audience boundary")):
        return "Trace example: surfaced proposal wording mixed audience boundaries without clearly separating direct-user explanation from audience-limited copy."
    if contains_any(record_text, ("task-oriented", "decision-ready proposal", "actionable proposal", "workflow owner", "goal-level proposal", "goal framing", "goal-oriented")) or "goal" in signal_keyword_set(signal):
        return "Trace example: recurring workflow findings were described as weak goal-level observations instead of being turned into a decision-ready proposal."
    return ""


def proposal_before_behavior_for_signal(signal: dict[str, Any]) -> str:
    record_text = record_text_blob(signal)
    keywords = signal_keyword_set(signal)
    if contains_any(record_text, ("supplierapidomainprobe", "passstatuscodes", "opera_fallback")):
        return "See `passStatusCodes`, add `404`, and conclude the existing config is sufficient without first checking whether that control surface actually governs fallback eligibility."
    if contains_any(record_text, ("approval", "stop gate")) or signal.get("kind") == "blocker" and "approval" in keywords:
        return "State that approval is needed but leave the stop gate or recovery path underspecified, so the user still has to guess what unblocks the work."
    if contains_any(record_text, ("private/operator disclosure", "customer-facing", "operator-facing", "disclosure wording", "audience boundary")) or keywords & {"private", "public", "customer", "operator", "disclosure"}:
        return "Surface a proposal that mixes direct-user explanation with operator/public-facing detail without making the disclosure boundary explicit."
    if contains_any(record_text, ("task-oriented", "decision-ready proposal", "actionable proposal", "workflow owner", "goal-level proposal", "goal framing", "goal-oriented")) or keywords & {"task", "todo", "phase", "plan", "goal"}:
        return "Summarize recurring workflow findings as observations or trace wording without turning them into a decision-ready proposal."
    if contains_any(record_text, ("progress summary", "operator-facing", "runtime context")):
        return "Open with progress-summary or runtime-context wording so the user still has to translate the trace into a proposal manually."
    if contains_any(record_text, ("refresh", "15s wait", "wait guidance")):
        return "State refresh/wait guidance as if the wait itself proves the claim, without keeping the evidence boundary visible."
    title = topic_title(signal)
    if title == "Clarify evidence wording before strong claims":
        return "Let answers drift toward stronger claims before separating what is a verified fact, what is an inference, and what is still only a working hypothesis."
    if title == "Clarify which surface owns the user-facing analysis result":
        return "Let the result drift toward a generic trace-pattern summary so the user still has to infer which analysis surface owns the answer."
    if title == "Turn recurring workflow findings into decision-ready proposals":
        return "Surface workflow findings as blocker-shaped observations without turning them into a decision-ready next step the user can act on immediately."
    return ""


def proposal_after_behavior_for_signal(signal: dict[str, Any]) -> str:
    record_text = record_text_blob(signal)
    keywords = signal_keyword_set(signal)
    if contains_any(record_text, ("supplierapidomainprobe", "passstatuscodes", "opera_fallback")):
        return "Check whether the existing control surface really owns the runtime behavior; if it does not, keep `404` as evidence and lift the recommendation to control ownership or strategic fix scope instead of reusing the nearest config field."
    if contains_any(record_text, ("approval", "stop gate")) or signal.get("kind") == "blocker" and "approval" in keywords:
        return "Name the stop gate clearly, explain why approval-sensitive work cannot continue yet, and state the exact safe next action or approval needed."
    if contains_any(record_text, ("private/operator disclosure", "customer-facing", "operator-facing", "disclosure wording", "audience boundary")) or keywords & {"private", "public", "customer", "operator", "disclosure"}:
        return "Keep the direct-user explanation explicit, but separate audience-limited copy and disclosure notes so the proposal shows what can be surfaced safely to each audience."
    if contains_any(record_text, ("task-oriented", "decision-ready proposal", "actionable proposal", "workflow owner", "goal-level proposal", "goal framing", "goal-oriented")) or keywords & {"task", "todo", "phase", "plan", "goal"}:
        return "Convert the recurring finding into a goal-level proposal the user can act on immediately: what should change, why it matters, and what the safer next move is."
    if contains_any(record_text, ("progress summary", "operator-facing", "runtime context")):
        return "Open with operator-facing proposal wording, recommend the strongest topic, and show the corrected behavior without requiring a manual rewrite pass."
    if contains_any(record_text, ("refresh", "15s wait", "wait guidance")):
        return "State wait/refresh as a limited next check while keeping the evidence boundary explicit instead of letting the wait read like proof."
    title = topic_title(signal)
    if title == "Clarify evidence wording before strong claims":
        return "Keep the confidence wording explicit so the user can distinguish verified fact, inference, and working hypothesis before treating the claim as settled."
    if title == "Clarify which surface owns the user-facing analysis result":
        return "Keep the analysis result clearly owned by the intended user-facing analysis surface, with proposal framing as support instead of a generic summary replacing the main answer."
    if title == "Turn recurring workflow findings into decision-ready proposals":
        return "Turn the workflow finding into a decision-ready proposal with a clearer gate and a more usable next step instead of leaving it as a loose observation."
    return ""


def proposal_bad_example_for_signal(signal: dict[str, Any]) -> str:
    return proposal_before_behavior_for_signal(signal)


def proposal_good_example_for_signal(signal: dict[str, Any]) -> str:
    return proposal_after_behavior_for_signal(signal)


def proposal_evidence_examples_for_signal(signal: dict[str, Any]) -> list[str]:
    trace_example = doctrine_trace_example(signal)
    before_behavior = proposal_before_behavior_for_signal(signal)
    after_behavior = proposal_after_behavior_for_signal(signal)
    if not any((trace_example, before_behavior, after_behavior)):
        return []
    examples: list[str] = []
    for record in signal.get("records", []):
        preview = str(record.get("content_preview") or "").strip()
        if not preview:
            continue
        if preview not in examples:
            examples.append(preview)
        if len(examples) >= 3:
            break
    return examples


def proposal_evidence_summary_for_signal(signal: dict[str, Any]) -> str:
    provenance = str(signal.get("provenance_note") or "")
    trace_example = doctrine_trace_example(signal)
    if provenance and trace_example:
        return f"{provenance} {trace_example}"
    return provenance or trace_example


def topic_title(signal: dict[str, Any]) -> str:
    keywords = signal_keyword_set(signal)
    review_focus = signal.get("review_focus") or infer_review_focus(signal)
    record_text = record_text_blob(signal)

    if "/memory-context-intelligence:analysis" in record_text and contains_any(
        record_text,
        (
            "progress summary",
            "operator-facing",
            "runtime context",
            "analysis context",
            "first-respon",
            "proposal-first",
            "rewrite",
        ),
    ):
        return "Rewrite /memory-context-intelligence:analysis first response into operator-facing proposal output"

    if contains_any(
        record_text,
        (
            "claim completion before verification",
            "claiming completion before verification",
            "completion wording behind real verification",
            "completion before verification",
            "verification evidence exists",
        ),
    ) or {"completion", "verification"} <= keywords:
        return "Stop completion wording from outrunning verification"

    if contains_any(
        record_text,
        (
            "needs config shape plus code path work instead of config-only change",
            "code path work instead of config-only change",
            "config-only change",
            "code-path change",
            "code path work",
        ),
    ):
        return "Separate symptom evidence from strategic fix scope"

    if contains_any(
        record_text,
        (
            "grep over",
            "grep -r",
            "coordinator settings",
            "checked source",
            "read config/supplier-pricing-calculator.json",
        ),
    ) or {"bash", "grep", "source"} <= keywords:
        return "Require source-backed behavior verification before choosing config-only remediation"

    if contains_any(
        record_text,
        (
            "config field",
            "retry config",
            "supplierapidomainprobe already has",
            "passstatuscodes",
            "opera_fallback",
            "404 away from opera_fallback",
            "404 into a pass",
            "fallback config",
        ),
    ):
        return "Verify semantic fit before reusing an existing control surface"

    if signal["kind"] == "blocker" and ("approval" in keywords or "approval" in record_text):
        return "Clarify stop-gate handling before approval-sensitive work"

    if signal["kind"] == "evidence_gap" or review_focus == "evidence-boundary":
        if contains_any(record_text, ("refresh", "15s wait", "wait guidance")) or keywords & {
            "refresh",
            "wait",
            "guidance",
        }:
            return "Clarify refresh and wait guidance before strong evidence claims"
        return "Clarify evidence wording before strong claims"

    if review_focus == "surface-boundary":
        return "Clarify which surface owns the user-facing analysis result"

    if keywords & {"private", "public", "customer", "operator", "disclosure"} or contains_any(
        record_text,
        (
            "private/operator disclosure",
            "customer-facing",
            "operator-facing",
            "disclosure wording",
            "audience boundary",
        ),
    ):
        return "Keep audience disclosure boundaries explicit in surfaced proposals"

    if keywords & {"task", "todo", "phase", "plan", "goal"} or contains_any(
        record_text,
        (
            "task-oriented",
            "decision-ready proposal",
            "actionable proposal",
            "workflow owner",
            "goal-level proposal",
            "goal framing",
            "goal-oriented",
        ),
    ):
        return "Turn recurring workflow findings into decision-ready proposals"

    if signal["kind"] == "correction":
        return "Reduce repeated correction around workflow wording and review boundaries"

    return "Turn recurring workflow findings into decision-ready proposals"


def advisory_focus_suffix(signal: dict[str, Any]) -> str:
    record_text = record_text_blob(signal)
    if contains_any(record_text, ("grep over", "grep -r", "grep")):
        return "grep verification"
    if contains_any(record_text, ("retry config", "fallback config")):
        return "retry-vs-fallback config"
    if contains_any(record_text, ("config field", "already has a config field", "supplierapidomainprobe already has")):
        return "config support"
    if contains_any(record_text, ("passstatuscodes", "404 into a pass", "opera_fallback", "404 away from opera_fallback")):
        return "404/fallback semantics"
    if signal.get("review_focus") == "surface-boundary":
        return "surface boundary"
    if contains_any(record_text, ("private/operator disclosure", "customer-facing", "operator-facing", "disclosure wording")) or {"private", "public", "customer", "operator", "disclosure"} & signal_keyword_set(signal):
        return "disclosure boundary"
    if contains_any(record_text, ("task-oriented", "decision-ready proposal", "actionable proposal", "workflow owner", "goal-level proposal", "goal framing", "goal-oriented")) or {"task", "todo", "phase", "plan", "goal"} & signal_keyword_set(signal):
        return "goal framing" if "goal" in signal_keyword_set(signal) or contains_any(record_text, ("goal-level proposal", "goal framing", "goal-oriented")) else "workflow owner"
    keywords = [keyword for keyword in signal.get("keywords", []) if keyword not in {"claude", "code", "said", "would", "read", "ran", "check"}]
    return str(keywords[0]) if keywords else "narrow historical signal"


def topic_from_signal(signal: dict[str, Any], topic_rank: int, *, promotion_tier: str = "promoted-candidate") -> dict[str, Any]:
    kind = signal["kind"]
    return {
        "rank": topic_rank,
        "id": f"topic-{topic_rank:03d}",
        "title": topic_title(signal),
        "purpose": PURPOSE_BY_KIND[kind],
        "why_surfaced": (
            f"{signal['record_count']} bounded intake record(s) clustered as a "
            f"{GROUP_LABELS[signal['group']]} signal with evidence label {signal['evidence_label']}."
        ),
        "expected_behavior_impact": IMPACT_BY_KIND[kind],
        "high_level_mechanism": MECHANISM_BY_KIND[kind],
        "expected_output": OUTPUT_BY_KIND[kind],
        "evidence_examples": proposal_evidence_examples_for_signal(signal),
        "before_behavior": proposal_before_behavior_for_signal(signal),
        "after_behavior": proposal_after_behavior_for_signal(signal),
        "example_bad": proposal_bad_example_for_signal(signal),
        "example_good": proposal_good_example_for_signal(signal),
        "evidence_summary": proposal_evidence_summary_for_signal(signal),
        "provenance_note": signal.get("provenance_note"),
        "source_scope_label": signal.get("source_scope_label"),
        "source_mix_label": signal.get("source_mix_label"),
        "source_classes": signal.get("source_classes", []),
        "source_session_ids": signal.get("source_session_ids", []),
        "historical_strength": signal.get("historical_strength"),
        "latest_seen": signal.get("latest_seen"),
        "current_session_confirmation": signal.get("current_session_confirmation"),
        "same_day_widened": signal.get("source_scope_label") == "widened-same-day",
        "confidence": signal["confidence"],
        "evidence_label": signal["evidence_label"],
        "promotion_tier": promotion_tier,
        "source_signal_ids": [signal["id"]],
    }


def build_signal_groups(ranked_signals: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {key: [] for key in GROUP_KEYS}
    for signal in ranked_signals:
        grouped[signal["group"]].append(signal)
    return grouped


def source_summary(intake_report: dict[str, Any]) -> dict[str, Any]:
    records = intake_report.get("records", [])
    source_policy = intake_report.get("source_policy") if isinstance(intake_report.get("source_policy"), dict) else {}
    return {
        "intake_mode": intake_report.get("mode"),
        "intake_status": intake_report.get("status"),
        "intake_evidence_strength": intake_report.get("evidence_strength"),
        "freshness": intake_report.get("freshness", {}),
        "records_received": len(records) if isinstance(records, list) else 0,
        "bounded_subset_only": bool(
            isinstance(intake_report.get("scope"), dict)
            and intake_report["scope"].get("bounded_subset_only")
        ),
        "policy_limited": bool(source_policy.get("policy_limited")),
        "policy_note": source_policy.get("policy_note"),
        "effective_source_classes": source_policy.get("effective_source_classes"),
    }


def build_report(
    intake_report: dict[str, Any], *, max_records: int = 50, max_topics: int = 8
) -> dict[str, Any]:
    safe_max_records = clamp(max_records, 1, 100)
    safe_max_topics = clamp(max_topics, 0, 20)
    raw_records = intake_report.get("evidence_records")
    if not isinstance(raw_records, list):
        raw_records = intake_report.get("records", [])
    records = raw_records[:safe_max_records] if isinstance(raw_records, list) else []

    clusters = cluster_records(records)
    ranked_signals = [ranked_signal_from_cluster(cluster, intake_report, 0) for cluster in clusters]
    ranked_signals.sort(key=lambda item: (-item["score"], -item["record_count"], item["id"]))
    for index, signal in enumerate(ranked_signals, start=1):
        signal["rank"] = index

    promotable_signals = [
        signal
        for signal in ranked_signals
        if signal["trace_record_count"] > 0 and signal["confidence"] in {"medium", "high"} and signal["score"] >= 0.5
    ]
    promoted_slice = promotable_signals[:safe_max_topics]
    topic_candidates = [
        topic_from_signal(signal, index, promotion_tier="promoted-candidate")
        for index, signal in enumerate(promoted_slice, start=1)
    ]

    minimum_topics = min(3, safe_max_topics) if safe_max_topics > 0 else 0
    promoted_ids = {signal["id"] for signal in promoted_slice}
    fallback_signals = [
        signal
        for signal in ranked_signals
        if signal["trace_record_count"] > 0 and signal["id"] not in promoted_ids
    ]
    fallback_needed = max(0, minimum_topics - len(topic_candidates))
    selected_fallback_signals = fallback_signals[:fallback_needed]
    advisory_fallback_topics = [
        topic_from_signal(signal, index, promotion_tier="advisory-fallback")
        for index, signal in enumerate(selected_fallback_signals, start=len(topic_candidates) + 1)
    ]
    title_counts: dict[str, int] = {}
    for topic in advisory_fallback_topics:
        title = str(topic.get("title") or "")
        title_counts[title] = title_counts.get(title, 0) + 1
    for topic, signal in zip(advisory_fallback_topics, selected_fallback_signals):
        title = str(topic.get("title") or "")
        if title_counts.get(title, 0) > 1:
            topic["title"] = f"{title} — {advisory_focus_suffix(signal)}"

    source = source_summary(intake_report)
    has_trace_ranked_signal = any(signal["trace_record_count"] > 0 for signal in ranked_signals)
    if source["intake_status"] == "available" and ranked_signals and has_trace_ranked_signal:
        status = "available"
    elif ranked_signals:
        status = "low-confidence"
    else:
        status = "insufficient"

    return {
        "tool": "memory-context-intelligence",
        "mode": "signals",
        "status": status,
        "internal_only": True,
        "source": source,
        "ranked_signals": ranked_signals,
        "signal_groups": build_signal_groups(ranked_signals),
        "topic_candidates": topic_candidates,
        "advisory_fallback_topics": advisory_fallback_topics,
        "limits": {
            "max_records_analyzed": safe_max_records,
            "max_topics": safe_max_topics,
            "records_analyzed": len(records),
            "signals_ranked": len(ranked_signals),
            "topics_promoted": len(topic_candidates),
        },
        "notes": [
            "Internal analysis only; no user-facing choose flow has been performed.",
            "External research has not been performed by signals mode.",
            "/additional/ emission has not been performed by signals mode.",
            "Main RULES mutation has not been performed by signals mode.",
            "Weak, stale, insufficient, or single-observation inputs stay low-confidence and do not produce promoted topics by default.",
        ],
        "choose_flow_performed": False,
        "external_research_performed": False,
        "additional_emission_performed": False,
        "main_rules_mutation_performed": False,
    }


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        intake_report = load_json_input(args.intake_report)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"memory-context-intelligence signals: failed to read intake JSON: {exc}", file=sys.stderr)
        return 2

    report = build_report(
        intake_report,
        max_records=args.max_records,
        max_topics=args.max_topics,
    )
    json.dump(report, fp=os.sys.stdout, ensure_ascii=False, indent=2)
    os.sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
