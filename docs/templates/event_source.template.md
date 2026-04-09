{% if object -%}
# {{ object.product.name }} — {{ object.name }}

📌 **v{{ object.version }}**{%- if object.retention %} · 🗄 **Retention:** {{ object.retention.duration }}{% endif %}{%- if object.latency %} · ⚡ **Latency:** {{ object.latency.duration }}{% endif %}

{% if object.retention and object.retention.comments -%}
🗄 {{ object.retention.comments }}
{% endif %}

{% if object.latency and object.latency.comments -%}
⚡ {{ object.latency.comments }}
{% endif %}

{% if object.licensing -%}
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
