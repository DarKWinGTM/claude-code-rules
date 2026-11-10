"""MCI-owned progress; preparing evidence never acknowledges semantic analysis."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import stat
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any

MAX_STATE_BYTES = 1048576


class CheckpointConflict(ValueError):
    pass


def default_state_path() -> Path:
    return Path.home() / ".claude" / "memory-context-intelligence" / "progress.json"


def scope_identity(memory_root: Path, source_classes: list[str], *, window: dict[str, Any] | None = None) -> str:
    value = [str(memory_root.resolve()), sorted(source_classes), "ordered-trace-v1"]
    if window is not None:
        value.append(window)
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def _validate_position(position: Any) -> None:
    if position is None:
        return
    if not isinstance(position, dict) or not isinstance(position.get("completed"), dict):
        raise CheckpointConflict("Invalid cursor shape; progress was preserved.")
    for name, bound in position["completed"].items():
        if (
            not isinstance(name, str) or Path(name).name != name
            or not isinstance(bound, dict) or type(bound.get("offset")) is not int or bound["offset"] < 0
            or not isinstance(bound.get("prefix_digest"), str) or len(bound["prefix_digest"]) != 64
        ):
            raise CheckpointConflict("Invalid cursor prefix; progress was preserved.")


def _read_document(path: Path) -> dict[str, Any]:
    if path.is_symlink():
        raise CheckpointConflict("Progress state must not be a symlink.")
    try:
        with path.open("rb") as handle:
            data = handle.read(MAX_STATE_BYTES + 1)
    except FileNotFoundError:
        return {"schema_version": 1, "scopes": {}}
    if len(data) > MAX_STATE_BYTES:
        raise CheckpointConflict("Progress state exceeds its bounded schema size.")
    try:
        document = json.loads(data)
    except (ValueError, UnicodeError) as exc:
        raise CheckpointConflict("Invalid progress JSON; existing state was preserved.") from exc
    if (
        not isinstance(document, dict)
        or type(document.get("schema_version")) is not int
        or document["schema_version"] != 1
        or not isinstance(document.get("scopes"), dict)
    ):
        raise CheckpointConflict("Invalid progress schema; existing state was preserved.")
    for key, entry in document["scopes"].items():
        if (
            not isinstance(key, str) or not isinstance(entry, dict)
            or not {"version", "position", "pending", "last_completed"}.issubset(entry)
            or type(entry.get("version")) is not int or entry["version"] < 0
            or (entry.get("position") is not None and not isinstance(entry["position"], dict))
            or (entry.get("pending") is not None and not isinstance(entry["pending"], dict))
            or (entry.get("last_completed") is not None and not isinstance(entry["last_completed"], dict))
        ):
            raise CheckpointConflict("Invalid progress entry; existing state was preserved.")
        _validate_position(entry.get("position"))
        for field in ["pending", "last_completed"]:
            binding = entry.get(field)
            if binding is None:
                continue
            if not isinstance(binding.get("batch_id"), str) or not isinstance(binding.get("source_binding"), dict):
                raise CheckpointConflict("Invalid batch binding; progress was preserved.")
            if field == "pending":
                if type(binding.get("expected_version")) is not int or type(binding.get("coverage_complete")) is not bool:
                    raise CheckpointConflict("Invalid pending completion; progress was preserved.")
                _validate_position(binding.get("expected_position"))
                _validate_position(binding.get("next_position"))
            if binding.get("run_id") is not None and (
                not isinstance(binding["run_id"], str) or binding.get("mode") not in {"incremental", "catch-up"}
                or not isinstance(binding.get("endpoint"), dict)
                or not isinstance(binding["source_binding"].get("prefixes"), dict)
                or not isinstance(binding["source_binding"].get("memory_root"), str)
            ):
                raise CheckpointConflict("Invalid run binding; progress was preserved.")
            if binding.get("run_id") is not None:
                _validate_position({"completed": binding["source_binding"]["prefixes"]})
                for name, bound in binding["endpoint"].items():
                    if (
                        not isinstance(name, str) or Path(name).name != name or not isinstance(bound, dict)
                        or type(bound.get("size")) is not int or bound["size"] < 0
                        or not isinstance(bound.get("digest"), str) or len(bound["digest"]) != 64
                    ):
                        raise CheckpointConflict("Invalid run endpoint; progress was preserved.")
    return document


def _entry(document: dict[str, Any], scope_key: str) -> dict[str, Any]:
    return document["scopes"].setdefault(scope_key, {
        "version": 0, "position": None, "pending": None, "last_completed": None,
    })


def load_progress(path: Path, scope_key: str) -> dict[str, Any]:
    return copy.deepcopy(_entry(_read_document(path), scope_key))


@contextmanager
def _locked(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    lock_path = path.with_suffix(path.suffix + ".lock")
    flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0)
    if lock_path.is_symlink():
        raise CheckpointConflict("Progress lock must not be a symlink.")
    fd = os.open(lock_path, flags, 0o600)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise CheckpointConflict("Progress lock is not a regular file.")
        if os.name == "nt":
            import msvcrt
            if os.fstat(fd).st_size == 0:
                os.write(fd, b"\0")
            os.lseek(fd, 0, os.SEEK_SET)
            msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        yield
    except BlockingIOError as exc:
        raise CheckpointConflict("Another invocation is updating this progress state.") from exc
    finally:
        os.close(fd)


def _write_document(path: Path, document: dict[str, Any]) -> None:
    data = (json.dumps(document, ensure_ascii=False, sort_keys=True) + "\n").encode()
    if len(data) > MAX_STATE_BYTES:
        raise CheckpointConflict("Progress state exceeds its bounded schema size.")
    if path.is_symlink():
        raise CheckpointConflict("Progress state must not be a symlink.")
    fd, name = tempfile.mkstemp(prefix=".progress-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def prepare_batch(path: Path, scope_key: str, binding: dict[str, Any]) -> dict[str, Any]:
    with _locked(path):
        document = _read_document(path)
        entry = _entry(document, scope_key)
        if (
            type(binding.get("expected_version")) is not int
            or entry["version"] != binding["expected_version"]
            or entry["position"] != binding.get("expected_position")
            or not isinstance(binding.get("batch_id"), str)
            or not binding["batch_id"]
        ):
            raise CheckpointConflict("Prepared batch does not match current progress.")
        # A new preparation supersedes an unacknowledged batch, never its progress.
        entry["pending"] = copy.deepcopy(binding)
        _write_document(path, document)
        return copy.deepcopy(entry)


def complete_batch(
    path: Path,
    scope_key: str,
    batch_id: str,
    outcome: str,
    *,
    source_binding: dict[str, Any],
    validate_source=None,
) -> dict[str, Any]:
    if outcome not in {"analyzed", "no-topics", "failed"}:
        raise CheckpointConflict("Completion requires analyzed, no-topics, or failed.")
    with _locked(path):
        document = _read_document(path)
        entry = _entry(document, scope_key)
        last = entry.get("last_completed") or {}
        if last.get("batch_id") == batch_id:
            if last.get("source_binding") != source_binding or outcome == "failed":
                raise CheckpointConflict("Completion does not match the acknowledged batch.")
            return dict(copy.deepcopy(entry), status="already-complete")
        pending = entry.get("pending")
        if (
            not pending or pending.get("batch_id") != batch_id
            or pending.get("source_binding") != source_binding
            or pending.get("expected_version") != entry["version"]
            or pending.get("expected_position") != entry["position"]
        ):
            raise CheckpointConflict("Stale or mismatched batch; progress was not advanced.")
        if outcome != "failed":
            if pending.get("coverage_complete") is not True or pending.get("next_position") is None:
                raise CheckpointConflict("Incomplete evidence cannot advance progress.")
            if validate_source is not None:
                validate_source(source_binding)
            entry["position"] = pending["next_position"]
            entry["version"] += 1
            entry["last_completed"] = {
                "batch_id": batch_id, "source_binding": source_binding,
                "run_id": pending.get("run_id"), "endpoint": pending.get("endpoint"),
                "mode": pending.get("mode"),
            }
        entry["pending"] = None
        _write_document(path, document)
        return dict(copy.deepcopy(entry), status="failed" if outcome == "failed" else "completed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="memory-context-intelligence complete")
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--outcome", choices=["analyzed", "no-topics", "failed"], required=True)
    parser.add_argument("--state", type=Path, default=default_state_path())
    args = parser.parse_args(argv)
    try:
        document = _read_document(args.state)
        matches = [
            (key, entry)
            for key, entry in document["scopes"].items()
            if any((entry.get(field) or {}).get("batch_id") == args.batch_id for field in ["pending", "last_completed"])
        ]
        if len(matches) != 1:
            raise CheckpointConflict("Batch was not found uniquely in MCI progress.")
        scope_key, entry = matches[0]
        bound = entry.get("pending")
        if not bound or bound.get("batch_id") != args.batch_id:
            bound = entry["last_completed"]
        from intake import validate_progressive_source
        result = complete_batch(
            args.state, scope_key, args.batch_id, args.outcome,
            source_binding=bound["source_binding"], validate_source=validate_progressive_source,
        )
        print(json.dumps({
            "status": result["status"], "version": result["version"],
            "batch_id": args.batch_id, "checkpoint_advanced": result["status"] == "completed",
            "semantic_completion": "caller-attested; not independently inferred from preprocessing",
        }))
        return 0
    except (CheckpointConflict, OSError, ValueError) as exc:
        print(json.dumps({"status": "blocked", "checkpoint_advanced": False, "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
