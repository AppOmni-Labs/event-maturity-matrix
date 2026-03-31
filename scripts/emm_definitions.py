"""Load EMM root definitions and resolve category / event_type / attribute keys."""
from __future__ import annotations

import os
from typing import Any

import yaml


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
    for item in attributes_data.get("items", []):
        k = item.get("key")
        if not k:
            raise ValueError(f"Attribute missing key: {item!r}")
        attributes_by_key[k] = item

    return {
        "categories": categories_data,
        "event_types": event_types_data,
        "attributes": attributes_data,
        "categories_by_key": categories_by_key,
        "event_types_by_key": event_types_by_key,
        "attributes_by_key": attributes_by_key,
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
