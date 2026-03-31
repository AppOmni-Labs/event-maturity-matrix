#!/usr/bin/env python3
"""Fail if resolved mappings differ from committed tests/mapping_snapshots."""
import json
import os
import sys
from pathlib import Path

_scripts = Path(__file__).resolve().parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from emm_mapping_snapshots import (
    build_snapshot_payload,
    iter_event_source_paths,
    load_event_source,
    repo_relative_posix,
    resolved_snapshot_matches_disk,
    snapshot_path_for_source,
)

_FAIL_MSG = (
    "Resolved mapping snapshot mismatch. If this change is intentional, run:\n"
    "  python scripts/update_mapping_snapshots.py\n"
    "Then commit the updated files under tests/mapping_snapshots/."
)


def main() -> int:
    root = Path(os.getenv("GITHUB_WORKSPACE", os.getcwd())).resolve()
    sources = iter_event_source_paths(root)
    errors: list[str] = []

    for yml in sources:
        rel = repo_relative_posix(yml, root)
        snap = snapshot_path_for_source(root, yml)
        if not snap.is_file():
            errors.append(f"Missing snapshot for {rel} (expected {snap.relative_to(root)})")
            continue

        data = load_event_source(yml)
        expected_payload = build_snapshot_payload(rel, data)

        try:
            on_disk_text = snap.read_text(encoding="utf-8")
        except OSError as e:
            errors.append(f"{rel}: read error {e}")
            continue

        if not resolved_snapshot_matches_disk(expected_payload, on_disk_text):
            try:
                json.loads(on_disk_text)
            except json.JSONDecodeError as e:
                errors.append(f"{rel}: invalid JSON in snapshot: {e}")
                continue
            errors.append(f"{rel}: snapshot differs from resolved mappings (see git diff tests/mapping_snapshots)")

    if errors:
        print(_FAIL_MSG, file=sys.stderr)
        print(file=sys.stderr)
        for line in errors:
            print(line, file=sys.stderr)
        return 1

    print(f"OK: {len(sources)} mapping snapshot(s) match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
