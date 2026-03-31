# Scripts

Short overview of Python modules and runnable tools in this folder.

- **`check_mapping_snapshots.py`** — Verifies that every event source’s resolved mappings match the committed JSON under `tests/mapping_snapshots/` (used in CI); run `update_mapping_snapshots.py` when you intentionally change mappings.

- **`create_product.py`** — Interactive helper that scaffolds a new product under `products/` with the expected directories and starter YAML files for contributions.

- **`emm_definitions.py`** — Shared library that loads `categories.yml`, `event_types.yml`, and `attributes.yml`, then resolves an event source’s rows into fully merged mappings (`mapping_defaults` plus per-row deltas).

- **`emm_json_paths.py`** — Shared library that evaluates EMM “field paths” (including JMESPath and escaped-dot rules) against example JSON, used when generating docs and checking paths.

- **`emm_mapping_snapshots.py`** — Shared helpers to build canonical snapshot payloads, map YAML paths to snapshot JSON paths, and compare on-disk snapshots to resolved definitions.

- **`generate-docs.py`** — Renders Markdown under `docs/` from Jinja templates and the matrix YAML (categories, event types, products, and event sources with resolved mappings).

- **`update_event_sources.py`** — Pulls mapping columns from a published Google Sheet (CSV export) and updates attributes in a chosen `event_source` YAML file using semantic keys (`category.event_type.attribute`).

- **`update_mapping_snapshots.py`** — Regenerates all files in `tests/mapping_snapshots/` from the current YAML and removes orphan snapshot files when sources are deleted.
