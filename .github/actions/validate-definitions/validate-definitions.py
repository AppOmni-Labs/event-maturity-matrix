"""Validates EMM data definitions: schema validation and example attribute checks."""
import os
import sys
import json
from typing import Dict, Any
from glob import glob

import yaml
import jmespath
from jsonschema.exceptions import ValidationError
from jsonschema.validators import Draft202012Validator
from loguru import logger

# Clear format for CI and local runs: level + message (no timestamp for less noise in CI)
logger.remove()
logger.add(
    sys.stderr,
    format="<level>{level: <8}</level> | {message}",
    level=os.environ.get("LOGURU_LEVEL", "INFO"),
)


def _path_segments(path_str: str) -> list[str]:
    """Split path string by '.' but not inside brackets. E.g. 'context.session_id' -> ['context', 'session_id']."""
    segments = []
    current = []
    depth = 0
    for c in path_str:
        if c == "[":
            depth += 1
            current.append(c)
        elif c == "]":
            depth -= 1
            current.append(c)
        elif c == "." and depth == 0:
            segments.append("".join(current))
            current = []
        else:
            current.append(c)
    if current:
        segments.append("".join(current))
    return segments


def _path_to_jmespath(path_str: str) -> str:
    """Convert our path format to JMESPath. Our bracket filter key[filter_key=filter_value] becomes key[?filter_key=='filter_value']."""
    segments = _path_segments(path_str)

    jmespath_parts = []
    for seg in segments:
        if "[" in seg and seg.endswith("]") and "=" in seg:
            key = seg[: seg.index("[")]
            filter_part = seg[seg.index("[") + 1 : -1]
            filter_key, _, filter_value = filter_part.partition("=")
            # JMESPath literal: escape single quotes in value
            escaped = filter_value.replace("\\", "\\\\").replace("'", "\\'")
            jmespath_parts.append(f"{key}[?{filter_key}=='{escaped}']")
        else:
            jmespath_parts.append(seg)
    return ".".join(jmespath_parts)


def _values_for_key_recursive(obj: Any, key: str):
    """Recursively find all values for key anywhere in obj (dict/list tree). Used for bare keys like 'user_id'."""
    if isinstance(obj, dict):
        if key in obj:
            yield obj[key]
        for v in obj.values():
            yield from _values_for_key_recursive(v, key)
    elif isinstance(obj, list):
        for item in obj:
            yield from _values_for_key_recursive(item, key)


def item_generator(json_input: Any, lookup_key: str):
    """Yield values for lookup_key in json_input. Uses JMESPath for paths with dots/brackets; recursive search for bare keys."""
    # Bare key (no dots, no brackets): JMESPath only looks at root, but data often has keys nested (e.g. user_id inside action_data)
    if "." not in lookup_key and "[" not in lookup_key:
        yield from _values_for_key_recursive(json_input, lookup_key)
        return
    expr = _path_to_jmespath(lookup_key)
    try:
        result = jmespath.search(expr, json_input)
    except jmespath.exceptions.JMESPathError:
        return
    if result is None:
        # JMESPath returns None for "not found" and for "value is null". For simple dotted paths, try two fallbacks:
        if "[" not in lookup_key:
            segs = _path_segments(lookup_key)
            if len(segs) >= 2:
                # 1) Key exists with null value: parent is dict and has the key
                parent_expr = _path_to_jmespath(".".join(segs[:-1]))
                try:
                    parent_result = jmespath.search(parent_expr, json_input)
                    if isinstance(parent_result, dict) and segs[-1] in parent_result:
                        yield parent_result[segs[-1]]
                        return
                except jmespath.exceptions.JMESPathError:
                    pass
                # 2) Parent is an array: JMESPath needs [*] to project (e.g. target.alternateId -> target[*].alternateId)
                projection_expr = _path_to_jmespath(segs[0] + "[*]." + ".".join(segs[1:]))
                try:
                    proj_result = jmespath.search(projection_expr, json_input)
                    if isinstance(proj_result, list):
                        for item in proj_result:
                            yield item
                        return
                except jmespath.exceptions.JMESPathError:
                    pass
        return
    if isinstance(result, list):
        for item in result:
            yield item
    else:
        yield result


def load(path: str) -> Dict[str, Any] | None:
    """Loads a YAML file from a path and returns a dict."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def _validate_with_validator(validator: Draft202012Validator, data_path: str) -> bool:
    """Validates a data file with an existing validator."""
    try:
        validator.validate(load(data_path))
        return True
    except ValidationError:
        raise


def _validator_for(schema_path: str) -> Draft202012Validator:
    """Build a validator for a schema (reuse for many data files)."""
    return Draft202012Validator(schema=load(schema_path))


def validate():
    """Validates all data files in repository."""
    # Resolve base path once for consistency
    base = os.getenv("GITHUB_WORKSPACE") or os.getcwd()
    attributes_path = os.path.join(base, "attributes.yml")
    categories_path = os.path.join(base, "categories.yml")
    event_types_path = os.path.join(base, "event_types.yml")
    schema_folder = os.path.join(base, "schema")

    logger.info("Validation starting; base path = {}", base)

    # Summary counts for final report
    products_validated = 0
    event_sources_validated = 0
    mappings_checked = 0
    example_files_checked = 0
    mappings_satisfied = 0  # at least one example had all attributes
    mappings_unsatisfied = 0  # no example had all attributes
    example_errors = 0

    # --- Root definition files ---
    logger.info("Validating root definition files...")
    for name, data_path in [
        ("attributes", attributes_path),
        ("categories", categories_path),
        ("event_types", event_types_path),
    ]:
        schema_path = os.path.join(schema_folder, f"{name}.yml")
        logger.debug("Validating {} against {}", data_path, schema_path)
        validator = _validator_for(schema_path)
        if not _validate_with_validator(validator, data_path):
            raise Exception(f"{name} schema validation failed.")
    logger.success("Root definition files validated (attributes, categories, event_types)")

    # --- Product files ---
    product_glob = os.path.join(base, "products", "*", "*.product.yml")
    product_paths = sorted(glob(product_glob))
    logger.info("Found {} product definition(s); validating...", len(product_paths))
    product_validator = _validator_for(os.path.join(schema_folder, "product.yml"))

    for product_path in product_paths:
        logger.debug("Validating product: {}", product_path)
        if not _validate_with_validator(product_validator, product_path):
            raise Exception(f"Product schema validation failed for {product_path}.")
        products_validated += 1
    logger.success("All {} product(s) validated", products_validated)

    # --- Event source files ---
    event_sources_glob = os.path.join(base, "products", "*", "event_sources", "*.yml")
    event_source_paths = sorted(glob(event_sources_glob))
    logger.info("Found {} event source(s); validating and checking examples...", len(event_source_paths))
    event_source_validator = _validator_for(os.path.join(schema_folder, "event_source.yml"))

    for event_source in event_source_paths:
        logger.debug("Validating event source: {}", event_source)
        if not _validate_with_validator(event_source_validator, event_source):
            raise Exception(f"Event source schema validation failed for {event_source}.")
        event_sources_validated += 1

        # Derive product id from path (e.g. .../products/appomni/event_sources/foo.yml -> appomni)
        _parts = event_source.replace(os.sep, "/").split("/")
        product_id = _parts[_parts.index("products") + 1] if "products" in _parts else "?"

        try:
            data = load(event_source)
            if not data:
                continue
            product_name = data.get("product", {}).get("name", product_id)
            event_source_name = data.get("name") or os.path.basename(event_source)
            parent_path = os.path.dirname(os.path.dirname(event_source))

            for mapping in data.get("mappings", []):
                mappings_checked += 1
                attribute_names = list(mapping.get("attributes", {}).values())
                examples = mapping.get("examples") or []

                # Validation passes for this mapping if at least one example has all attributes
                mapping_satisfied = False
                found_in_any_example = set()  # display_name of attributes found in at least one example
                all_display_names = set()
                example_locations_checked = []  # example files checked for this mapping (for warning context)

                for example in examples:
                    example_location = example.get("location", "")
                    example_full_path = os.path.normpath(os.path.join(parent_path, example_location))
                    logger.debug("Checking example: {} (mapping attributes: {})", example_full_path, attribute_names)

                    try:
                        with open(example_full_path, "r") as f:
                            example_data = json.load(f)
                    except Exception as e:
                        logger.error(
                            "[{}] {}: Error loading example {}: {}",
                            product_name,
                            event_source_name,
                            example_location,
                            e,
                        )
                        example_errors += 1
                        continue

                    example_files_checked += 1
                    example_locations_checked.append(example_location)
                    example_has_all = True

                    for attribute_name in attribute_names:
                        # Attribute may be a single path (str) or a list of paths (any of these)
                        if isinstance(attribute_name, list):
                            paths = attribute_name
                            values = []
                            for path in paths:
                                if isinstance(path, str):
                                    values.extend(item_generator(example_data, path))
                            is_missing = not values
                            display_name = ", ".join(str(p) for p in paths)
                        else:
                            if attribute_name == "FIXME":
                                continue  # don't require FIXME for "all attributes" check
                            values = list(item_generator(example_data, attribute_name))
                            is_missing = not values
                            display_name = attribute_name

                        all_display_names.add(display_name)
                        if is_missing:
                            example_has_all = False
                        else:
                            found_in_any_example.add(display_name)
                            logger.debug(
                                "Found in {}: {} ({} value(s))",
                                example_location,
                                display_name,
                                len(values),
                            )

                    if example_has_all:
                        mapping_satisfied = True

                if mapping_satisfied:
                    mappings_satisfied += 1
                else:
                    mappings_unsatisfied += 1
                    never_found = all_display_names - found_in_any_example
                    category = mapping.get("category", "?")
                    event_type = mapping.get("event_type", "?")
                    logger.warning(
                        "[{}] {} | mapping {} / {} | {} | attributes not found in any example: {}",
                        product_name,
                        event_source_name,
                        category,
                        event_type,
                        example_locations_checked,
                        sorted(never_found) if never_found else "(none)",
                    )

        except Exception as e:
            logger.error(
                "[{}] {}: Error processing event source: {}",
                product_id,
                os.path.basename(event_source),
                e,
            )
            example_errors += 1

    logger.success(
        "All {} event source(s) validated; {} mapping(s), {} example file(s) checked",
        event_sources_validated,
        mappings_checked,
        example_files_checked,
    )

    # --- Final summary (confidence that every module and event type was checked) ---
    logger.info("--- Validation summary ---")
    logger.info("Products validated: {}", products_validated)
    logger.info("Event sources validated: {}", event_sources_validated)
    logger.info("Mappings with examples considered: {}", mappings_checked)
    logger.info("Example files loaded and checked: {}", example_files_checked)
    logger.info("Mappings where at least one example had all attributes: {}", mappings_satisfied)
    logger.info("Mappings where no example had all attributes: {}", mappings_unsatisfied)
    logger.info("Example load/processing errors: {}", example_errors)

    if mappings_unsatisfied > 0 or example_errors > 0:
        logger.error(
            "Validation failed: {} mapping(s) with no example having all attributes, {} error(s)",
            mappings_unsatisfied,
            example_errors,
        )
        sys.exit(1)
    logger.success(
        "Validation complete. Every product and event source was checked ({} products, {} event sources, "
        "{} example files, {} mappings). At least one example had all attributes per mapping.",
        products_validated,
        event_sources_validated,
        example_files_checked,
        mappings_checked,
    )


if __name__ == "__main__":
    validate()
