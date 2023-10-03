{% if object -%}
# {{ object.name }} ({{ object.version }})

{{ object.description }}

{%- if object.collection %}
## Collections
{%- for c in object.collection %}

## {{ c.name }} ({{ c.id }}) Collection

{{ c.description }}

{% if c.references is not none -%}
{% for r in c.references -%}
### {{ r.name }} ({{ r.id }}) Reference

{{ r.description }}

{%- if r.url -%}
URL Reference: [{{ r.url }}]({{ r.url }})
{% endif %}

{%- endfor -%}
{%- endif -%}


{%- endfor -%}
{%- endif -%}

{%- endif -%}