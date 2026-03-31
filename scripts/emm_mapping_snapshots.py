"""Build and compare resolved mapping snapshots for event sources."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from emm_definitions import resolve_event_source_mappings


def repo_relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def snapshot_path_for_source(root: Path, source_yml: Path) -> Path:
    """tests/mapping_snapshots/<mirror of products/.../*.json>"""
    rel = source_yml.resolve().relative_to(root.resolve())
    return root / "tests" / "mapping_snapshots" / rel.with_suffix(".json")


def build_snapshot_payload(source_rel_posix: str, data: dict[str, Any]) -> dict[str, Any]:
    resolved = resolve_event_source_mappings(data)
    mappings_out: list[dict[str, Any]] = []
    for m in resolved:
        attrs = m.get("attributes") or {}
        mappings_out.append(
            {
                "category": m.get("category"),
                "event_type": m.get("event_type"),
                "attributes": dict(sorted(attrs.items(), key=lambda kv: kv[0])),
            }
        )
    return {"source": source_rel_posix, "mappings": mappings_out}


def canonical_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, indent=2) + "\n"


def load_event_source(path: Path) -> dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def iter_event_source_paths(root: Path) -> list[Path]:
    return sorted(root.glob("products/*/event_sources/*.yml"))


def remove_orphan_snapshots(root: Path, expected_json: set[Path]) -> list[Path]:
    """Delete JSON files under tests/mapping_snapshots/products not in expected set. Returns removed paths."""
    snap_products = root / "tests" / "mapping_snapshots" / "products"
    removed: list[Path] = []
    if not snap_products.is_dir():
        return removed
    for p in sorted(snap_products.rglob("*.json")):
        if p.resolve() not in expected_json:
            p.unlink()
            removed.append(p)
    return removed
