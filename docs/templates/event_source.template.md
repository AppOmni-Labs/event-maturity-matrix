{% if object -%}
{% set ret_t = (object.retention.comments | default('') | trim) if object.retention else '' %}
{% set ret_ok = object.retention and ret_t and ret_t | lower != 'n/a' %}
{% set lat_t = (object.latency.comments | default('') | trim) if object.latency else '' %}
{% set lat_ok = object.latency and lat_t and lat_t | lower != 'n/a' %}
{% set lic_t = (object.licensing.comments | default('') | trim) if object.licensing else '' %}
{% set lic_ok = object.licensing and lic_t and lic_t | lower != 'n/a' %}
# {{ object.product.name }} — {{ object.name }}

📌 **v{{ object.version }}**{%- if object.retention %} · 🗄 **Retention:** {{ object.retention.duration }}{% endif %}{%- if object.latency %} · ⚡ **Latency:** {{ object.latency.duration }}{% endif %}

{% if ret_ok -%}
🗄 {{ object.retention.comments }}
{% endif %}

{% if lat_ok -%}
⚡ {{ object.latency.comments }}
{% endif %}

{% if lic_ok -%}
📜 **Licensing:** {{ object.licensing.comments }}
{% endif %}

{{ object.description }}


{%- if object.references is not none %}
## References
{%- for reference in object.references %}
* [{{ reference.name }}]({{ reference.url }})
{%- endfor %}
{%- endif %}

{%- if object.mappings and object.emm_doc.mapping_rows %}
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
{%- for row in object.emm_doc.mapping_rows %}
| {{ row.category }} | {{ row.event_type }} | {{ row.attribute }} | {{ row.source_field }} |
{%- endfor %}

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
{%- for row in object.emm_doc.example_rows %}
| {{ row.category }} | {{ row.event_type }} | {{ row.example | safe }} | {{ row.sample_values }} |
{%- endfor %}
{% endif %}

{% endif %}
