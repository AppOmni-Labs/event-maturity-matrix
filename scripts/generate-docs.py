"""Generates docs from defined data files in repository."""
import os
from glob import glob

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate():
    root = os.getenv("GITHUB_WORKSPACE", os.getcwd())

    schema_path = os.path.join(root, "schema")
    docs_path = os.path.join(root, "docs")
    docs_templates_path = os.path.join(docs_path, "templates")

    attributes = os.path.join(root, "attributes.yml")
    categories = os.path.join(root, "categories.yml")
    event_types = os.path.join(root, "event_types.yml")

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
            result = t.render(object=data)
            path = os.path.join(docs_path, data["product"]["name"].lower())
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, f"{data['name']}.md"), "w") as out:
                out.write(result)


if __name__ == "__main__":
    generate()