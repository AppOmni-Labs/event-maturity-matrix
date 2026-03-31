#!/usr/bin/env python3
"""Write tests/mapping_snapshots from resolved event_source mappings."""
import os
import sys
from pathlib import Path

_scripts = Path(__file__).resolve().parent
if str(_scripts) not in sys.path:
    sys.path.insert(0, str(_scripts))

from emm_mapping_snapshots import (
    build_snapshot_payload,
    canonical_json,
    iter_event_source_paths,
    load_event_source,
    remove_orphan_snapshots,
    repo_relative_posix,
    snapshot_path_for_source,
)


def main() -> int:
    root = Path(os.getenv("GITHUB_WORKSPACE", os.getcwd())).resolve()
    sources = iter_event_source_paths(root)
    expected: set[Path] = set()

    for yml in sources:
        data = load_event_source(yml)
        rel = repo_relative_posix(yml, root)
        payload = build_snapshot_payload(rel, data)
        out = snapshot_path_for_source(root, yml)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(canonical_json(payload), encoding="utf-8")
        expected.add(out.resolve())

    removed = remove_orphan_snapshots(root, expected)
    print(f"Wrote {len(sources)} snapshot(s) under tests/mapping_snapshots/")
    if removed:
        print(f"Removed {len(removed)} orphan snapshot(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
