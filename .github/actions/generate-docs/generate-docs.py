"""Generates docs from defined data files in repository."""
import os
from glob import glob

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate():
    if not os.getenv("GITHUB_WORKSPACE"):
        attributes = os.path.join(os.getcwd(), "attributes.yml")
        categories = os.path.join(os.getcwd(), "categories.yml")
        event_types = os.path.join(os.getcwd(), "event_types.yml")
        out_path = os.path.join(os.getcwd(), "docs")
    else:
        attributes = os.path.join(os.getenv("GITHUB_WORKSPACE"), "attributes.yml")
        categories = os.path.join(os.getenv("GITHUB_WORKSPACE"), "categories.yml")
        event_types = os.path.join(os.getenv("GITHUB_WORKSPACE"), "event_types.yml")
        out_path = os.path.join(os.getenv("GITHUB_WORKSPACE"), "docs")

    templates_path = os.path.join(out_path, "templates")

    env = Environment(loader=FileSystemLoader(templates_path), autoescape=select_autoescape())

    t = env.get_template("base.template.md")

    with open(attributes, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(f"{out_path}/attributes.md", "w") as f:
            f.write(result)

    with open(categories, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(f"{out_path}/categories.md", "w") as f:
            f.write(result)

    with open(event_types, "r") as f:
        data = yaml.safe_load(f)
        result = t.render(object=data)
        with open(f"{out_path}/event_types.md", "w") as f:
            f.write(result)

    t = env.get_template("product.template.md")
    for product in glob("./products/*/*.product.yml"):
        with open(product, "r") as f:
            data = yaml.safe_load(f)
            result = t.render(object=data)
            path = out_path + "/" + data["name"].lower()
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}/{data['name']}.md", "w") as f2:
                f2.write(result)

    t = env.get_template("event_source.template.md")
    for event_source in glob("./products/*/event_sources/*.yml"):
        with open(event_source, "r") as f:
            data = yaml.safe_load(f)
            result = t.render(object=data)
            path = out_path + "/" + data["product"]["name"].lower()
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}/{data['name']}.md", "w") as f2:
                f2.write(result)


if __name__ == "__main__":
    generate()
