"""Generates docs from defined data files in repository."""
import json
import os
import sys
from glob import glob
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

_scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)

from emm_definitions import load_model
from emm_json_paths import item_generator

EMM_UPDATE = "EMM_UPDATE"


def _field_paths(spec: Any) -> list[str]:
    if isinstance(spec, list):
        return [p for p in spec if isinstance(p, str)]
    if isinstance(spec, str):
        return [spec]
    return []


def _field_display(spec: Any) -> str:
    paths = _field_paths(spec)
    return ", ".join(paths)


def _md_cell(s: str, max_len: int = 200) -> str:
    text = s.replace("|", "\\|").replace("\n", " ")
    if len(text) > max_len:
        return text[: max_len - 1] + "…"
    return text


def _values_for_spec(example_data: dict, spec: Any) -> list[Any]:
    out: list[Any] = []
    for path in _field_paths(spec):
        if path == EMM_UPDATE:
            continue
        out.extend(item_generator(example_data, path))
    return out


def _sample_snippet(example_path: str, mapping: dict, model: dict) -> str:
    try:
        with open(example_path, "r") as f:
            data = json.load(f)
    except OSError:
        return "—"
    parts: list[str] = []
    for attr_key, spec in (mapping.get("attributes") or {}).items():
        if spec == EMM_UPDATE:
            continue
        if isinstance(spec, list) and spec and spec[-1] == EMM_UPDATE:
            continue
        vals = _values_for_spec(data, spec)
        if not vals:
            continue
        label = model["attributes_by_key"].get(attr_key, {}).get("name", attr_key)
        parts.append(f"{label}={_md_cell(str(vals[0]), 60)}")
        if len(parts) >= 5:
            break
    return "; ".join(parts) if parts else "—"


def build_event_source_doc(data: dict, model: dict, root: str, event_source_path: str) -> dict:
    product_name = data["product"]["name"]
    parts = event_source_path.replace(os.sep, "/").split("/")
    product_dir_name = parts[parts.index("products") + 1]

    mapping_rows: list[dict[str, str]] = []
    example_rows: list[dict[str, str]] = []

    parent_path = os.path.dirname(os.path.dirname(event_source_path))

    for mapping in data.get("mappings") or []:
        cat_key = mapping.get("category", "")
        et_key = mapping.get("event_type", "")
        cat_item = model["categories_by_key"].get(cat_key, {})
        et_item = model["event_types_by_key"].get(et_key, {})
        cat_name = cat_item.get("name", cat_key)
        et_name = et_item.get("name", et_key)

        for attr_key, spec in (mapping.get("attributes") or {}).items():
            if spec == EMM_UPDATE:
                continue
            if isinstance(spec, list) and spec and spec[-1] == EMM_UPDATE:
                continue
            attr_item = model["attributes_by_key"].get(attr_key, {})
            mapping_rows.append(
                {
                    "category": cat_name,
                    "event_type": et_name,
                    "attribute": attr_item.get("name", attr_key),
                    "attribute_key": attr_key,
                    "source_field": _md_cell(_field_display(spec), 120),
                }
            )

        for ex in mapping.get("examples") or []:
            loc = ex.get("location", "").lstrip("./")
            rel = f"/products/{product_dir_name}/{loc}"
            link = f"[{ex.get('type', 'example')}]({rel})"
            full_path = os.path.normpath(os.path.join(parent_path, ex.get("location", "")))
            sample = _sample_snippet(full_path, mapping, model)
            example_rows.append(
                {
                    "category": cat_name,
                    "event_type": et_name,
                    "example": link,
                    "sample_values": sample,
                }
            )

    out = dict(data)
    out["emm_doc"] = {
        "mapping_rows": mapping_rows,
        "example_rows": example_rows,
        "product_dir_name": product_dir_name,
    }
    return out


def generate():
    root = os.getenv("GITHUB_WORKSPACE", os.getcwd())

    docs_path = os.path.join(root, "docs")
    docs_templates_path = os.path.join(docs_path, "templates")

    attributes = os.path.join(root, "attributes.yml")
    categories = os.path.join(root, "categories.yml")
    event_types = os.path.join(root, "event_types.yml")

    model = load_model(root)

    env = Environment(
        loader=FileSystemLoader(docs_templates_path),
        autoescape=select_autoescape(),
    )

    t = env.get_template("base.template.md")

    with open(attributes, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(os.path.join(docs_path, "attributes.md"), "w") as out:
            out.write(result)

    with open(categories, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(os.path.join(docs_path, "categories.md"), "w") as out:
            out.write(result)

    with open(event_types, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(os.path.join(docs_path, "event_types.md"), "w") as out:
            out.write(result)

    t = env.get_template("product.template.md")
    for product in glob(os.path.join(root, "products", "*", "*.product.yml")):
        with open(product, "r") as f:
            data = yaml.safe_load(f)
            result = t.render(object=data)
            path = os.path.join(docs_path, data["name"].lower())
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, f"{data['name']}.md"), "w") as out:
                out.write(result)

    t = env.get_template("event_source.template.md")
    for event_source in glob(os.path.join(root, "products", "*", "event_sources", "*.yml")):
        with open(event_source, "r") as f:
            data = yaml.safe_load(f)
            doc = build_event_source_doc(data, model, root, event_source)
            result = t.render(object=doc)
            path = os.path.join(docs_path, data["product"]["name"].lower())
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, f"{data['name']}.md"), "w") as out:
                out.write(result)


if __name__ == "__main__":
    generate()
