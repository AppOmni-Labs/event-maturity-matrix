{% if object -%}
# {{ object.entity_name }} ({{ object.version }})

{{ object.description }}

{%- if object.entity_name == 'attributes' %}
## Items

| Name | ID | Type | Description | Categories | Include | Exclude | Examples |
| ---- | -- | ---- | ----------- | ---------- | -------- | -------- | -------- |
{% for item in object["items"] -%}
| {{ item.name }} | {{ item.id }} | {{ item.type }} | {{ item.description|trim }} | {% if item.categories %}{% for category in item.categories %}{{ category }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} | {% if item.include %}{% for include in item.include %}{{ include }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} | {% if item.exclude %}{% for exclude in item.exclude %}{{ exclude }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} | {% if item.examples %}{% for example in item.examples %}{{ example }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} |
{% endfor %}

{% endif -%}

{%- if object.entity_name == 'categories' %}
## Items

| Name | ID | Description |
| ---- | -- | ----------- |
{% for item in object["items"] -%}
| {{ item.name }} | {{ item.id }} | {{ item.description | replace('\n','\\n') }} |
{% endfor %}

{% endif -%}

{%- if object.entity_name == 'event_types' %}
## Items

| Name | ID | Description | Categories |
| ---- | -- | ----------- | ---------- |
{% for item in object["items"] -%}
| {{ item.name }} | {{ item.id }} | {{ item.description|trim }} | {% if item.categories %}{% for category in item.categories %}{{ category }}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %} |
{% endfor %}

{% endif -%}

{% endif %}
{# end #}
