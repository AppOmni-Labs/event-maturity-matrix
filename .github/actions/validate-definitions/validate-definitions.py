"""Generates docs from defined data files in repository."""
import os
import json
from typing import Dict
from glob import glob

import yaml
from jsonschema.exceptions import ValidationError
from jsonschema.validators import Draft202012Validator


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v if v else "Null"
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

def load(path: str) -> Dict[str, str]:
    """Loads a YAML file from a path and returns a dict."""
    with open(path, "r") as f:
        return yaml.safe_load(f)

def _schema_validation(data_path: str, schema_path: str) -> bool:
    """Validates a schema file."""
    try:
        Draft202012Validator(schema=load(schema_path)).validate(load(data_path))
        return True
    except ValidationError as ve:
        raise ve
    except Exception as e:
        raise e

def validate():
    """Validates all data files in repository."""
    if not os.getenv("GITHUB_WORKSPACE"):
        attributes = os.path.join(os.getcwd(), "attributes.yml")
        categories = os.path.join(os.getcwd(), "categories.yml")
        event_types = os.path.join(os.getcwd(), "event_types.yml")
        schema_folder = os.path.join(os.getcwd(), "schema")
    else:
        attributes = os.path.join(os.getenv("GITHUB_WORKSPACE"), "attributes.yml")
        categories = os.path.join(os.getenv("GITHUB_WORKSPACE"), "categories.yml")
        event_types = os.path.join(os.getenv("GITHUB_WORKSPACE"), "event_types.yml")
        schema_folder = os.path.join(os.getenv("GITHUB_WORKSPACE"), "schema")

    if not _schema_validation(attributes, os.path.join(schema_folder, "attributes.yml")):
        raise Exception("Attributes schema validation failed.")
    if not _schema_validation(categories, os.path.join(schema_folder, "categories.yml")):
        raise Exception("Categories schema validation failed.")
    if not _schema_validation(event_types, os.path.join(schema_folder, "event_types.yml")):
        raise Exception("Event types schema validation failed.")

    for product in glob("./products/*/*.product.yml"):
        if not _schema_validation(product, os.path.join(schema_folder, "product.yml")):
            raise Exception(f"Product schema validation failed for {product}.")
    for event_source in glob("./products/*/event_sources/*.yml"):
        if not _schema_validation(event_source, os.path.join(schema_folder, "event_source.yml")):
            raise Exception(f"Event source schema validation failed for {event_source}.")

        try:
            data = None
            with open(event_source, "r") as f:
                data = yaml.safe_load(f)
            if data:
                parent_path = os.path.dirname(os.path.dirname(event_source))
                for mapping in data["mappings"]:
                    attribute_names = mapping["attributes"].values()
                    if mapping.get("examples"):
                        try:
                            for example in mapping["examples"]:
                                example_data = None
                                try:
                                    with open(f"{parent_path}/{example['location']}", "r") as f:
                                        example_data = json.load(f)
                                except FileNotFoundError as e:
                                    print(
                                        f"Error: No example found at {parent_path}/{example['location']}: {e}")
                                for attribute_name in attribute_names:
                                    for value in item_generator(example_data, attribute_name):
                                        if not value:
                                            print(f"""
            Could not find attribute in {example['location']}: {attribute_name}
            Example File: {example['location']}
            """)
                        except Exception as e:
                            print(f"Error with example {example['location']}: {e}")
        except Exception as e:
            print(f"Error with {event_source}: {e}")


if __name__ == "__main__":
    validate()