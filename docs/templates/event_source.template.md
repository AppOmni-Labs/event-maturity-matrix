{% if object -%}
# {{ object.product.name }} - {{ object.name }} ({{ object.version }})

> Entity Name: {{ object.entity_name }}

{{ object.description }}

{# BEGIN REFERENCES #}
{%- if object.references is not none -%}
## References

{%- for reference in object.references %}
* [{{ reference.name }}]({{ reference.url }})
{%- endfor -%}

{%- endif -%}
{# END REFERENCES #}

{# BEGIN RETENTION #}
{%- if object.retention -%}
## Retention

Based on our research, {{ object.product.name }} retains audit logs for {{ object.retention.duration }}.

{% if object.retention.comments %}
### Comments
{{ object.retention.comments }}

{%- endif %}

{%- endif -%}
{# END RETENTION #}

{# BEGIN LATENCY #}
{%- if object.latency %}
## Latency

Based on our research, {{ object.product.name }} has a latency of {{ object.latency.duration }}.

{% if object.latency.comments -%}
### Comments
{{ object.latency.comments }}

{%- endif -%}

{%- endif -%}
{# END LATENCY #}

{# BEGIN LICENSING #}
{%- if object.licensing %}
## Licensing

{{ object.licensing.comments }}

{%- endif -%}
{# END LICENSING #}

{# BEGIN MAPPINGS #}
{%- if object.mappings -%}
## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
{%- for mapping in object.mappings %}
| {{ mapping.category }} | {{ mapping.event_type }} | {%- for attribute, value in mapping.attributes.items() -%}{{ attribute }} -> {{ value }}<br />{%- endfor -%}| {%- if mapping.examples -%}{%- for example in mapping.examples -%}[{{ example.type }}](/products/{{ object.product.name|lower }}{{ example.location|replace('./','/') }})<br />{%- endfor -%}{%- endif -%} |

{%- endfor -%}

{% endif %}
{# END MAPPINGS #}

{% endif %}