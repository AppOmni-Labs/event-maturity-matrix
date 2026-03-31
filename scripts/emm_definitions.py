"""Load EMM root definitions and resolve category / event_type / attribute keys."""
from __future__ import annotations

import copy
import os
from typing import Any

import yaml

# Reserved path value in YAML mappings (must match validate-definitions).
EMM_UPDATE = "EMM_UPDATE"


def _load_yaml(path: str) -> dict[str, Any]:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_model(base: str) -> dict[str, Any]:
    """Load categories, event_types, attributes and build lookup tables by ``key``."""
    categories_path = os.path.join(base, "categories.yml")
    event_types_path = os.path.join(base, "event_types.yml")
    attributes_path = os.path.join(base, "attributes.yml")

    categories_data = _load_yaml(categories_path)
    event_types_data = _load_yaml(event_types_path)
    attributes_data = _load_yaml(attributes_path)

    categories_by_key: dict[str, dict[str, Any]] = {}
    for item in categories_data.get("items", []):
        k = item.get("key")
        if not k:
            raise ValueError(f"Category missing key: {item!r}")
        categories_by_key[k] = item

    event_types_by_key: dict[str, dict[str, Any]] = {}
    for item in event_types_data.get("items", []):
        k = item.get("key")
        if not k:
            raise ValueError(f"Event type missing key: {item!r}")
        event_types_by_key[k] = item

    attributes_by_key: dict[str, dict[str, Any]] = {}
    attributes_key_order: list[str] = []
    for item in attributes_data.get("items", []):
        k = item.get("key")
        if not k:
            raise ValueError(f"Attribute missing key: {item!r}")
        attributes_by_key[k] = item
        attributes_key_order.append(k)

    return {
        "categories": categories_data,
        "event_types": event_types_data,
        "attributes": attributes_data,
        "categories_by_key": categories_by_key,
        "event_types_by_key": event_types_by_key,
        "attributes_by_key": attributes_by_key,
        "attributes_key_order": attributes_key_order,
    }


def validate_mapping(model: dict[str, Any], mapping: dict[str, Any], *, path: str) -> None:
    """Raise ValueError if mapping category / event_type / attributes are invalid."""
    cat_k = mapping.get("category")
    et_k = mapping.get("event_type")
    if cat_k not in model["categories_by_key"]:
        raise ValueError(f"{path}: unknown category key {cat_k!r}")
    if et_k not in model["event_types_by_key"]:
        raise ValueError(f"{path}: unknown event_type key {et_k!r}")

    et = model["event_types_by_key"][et_k]
    allowed_cats = et.get("categories") or []
    if cat_k not in allowed_cats:
        raise ValueError(
            f"{path}: event_type {et_k!r} is not in category {cat_k!r} (allowed: {allowed_cats})"
        )

    for ak in (mapping.get("attributes") or {}).keys():
        if ak not in model["attributes_by_key"]:
            raise ValueError(f"{path}: unknown attribute key {ak!r}")


def validate_mapping_defaults(model: dict[str, Any], data: dict[str, Any], *, path: str) -> None:
    """Raise ValueError if mapping_defaults references unknown category keys."""
    md = data.get("mapping_defaults")
    if not md:
        return
    categories_block = md.get("categories") or {}
    if not isinstance(categories_block, dict):
        raise ValueError(f"{path}: mapping_defaults.categories must be a mapping")
    for ck in categories_block:
        if ck not in model["categories_by_key"]:
            raise ValueError(f"{path}: mapping_defaults.categories has unknown category key {ck!r}")


def validate_raw_mapping_delta(model: dict[str, Any], raw_mapping: dict[str, Any], *, path: str) -> None:
    """Ensure delta attribute keys (before merge) are known; ``null`` values are allowed (removals)."""
    for ak in (raw_mapping.get("attributes") or {}).keys():
        if ak not in model["attributes_by_key"]:
            raise ValueError(f"{path}: unknown attribute key {ak!r} in mapping delta")


def merge_mapping_attributes(data: dict[str, Any], raw_mapping: dict[str, Any]) -> dict[str, Any]:
    """
    Merge mapping_defaults (source → category) with raw_mapping.attributes (delta).
    Delta keys set to YAML null remove that attribute from the merged result (even if set in defaults).
    """
    md = data.get("mapping_defaults") or {}
    src_layer = (md.get("source") or {}).get("attributes") or {}
    cat_key = raw_mapping.get("category")
    cat_block = (md.get("categories") or {}).get(cat_key) or {}
    cat_layer = cat_block.get("attributes") or {}
    delta = raw_mapping.get("attributes") or {}

    merged: dict[str, Any] = {}
    merged.update(copy.deepcopy(src_layer))
    merged.update(copy.deepcopy(cat_layer))

    for attr_key, value in delta.items():
        if value is None:
            merged.pop(attr_key, None)
        else:
            merged[attr_key] = value
    return merged


def resolved_mapping_for_examples(raw_mapping: dict[str, Any], merged_attrs: dict[str, Any]) -> dict[str, Any]:
    """Build a mapping dict like the on-disk YAML but with resolved attributes (for validation / docs)."""
    out = dict(raw_mapping)
    out["attributes"] = merged_attrs
    return out


def resolve_event_source_mappings(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return one resolved mapping dict per ``mappings`` item (same order) with merged attributes."""
    return [
        resolved_mapping_for_examples(m, merge_mapping_attributes(data, m)) for m in data.get("mappings") or []
    ]


def count_mapped_attributes_for_examples(attrs: dict[str, Any]) -> int:
    """Attributes that participate in example coverage (exclude EMM_UPDATE placeholders)."""
    n = 0
    for v in attrs.values():
        if isinstance(v, str) and v == EMM_UPDATE:
            continue
        if isinstance(v, list) and len(v) > 0 and v[-1] == EMM_UPDATE:
            continue
        n += 1
    return n
