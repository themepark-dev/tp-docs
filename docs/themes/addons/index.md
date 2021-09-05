{% set addons = extra.addons %}
{% set title = page.title.split()[0].lower() %}
{% for app, addon_name in addons.items() %}
### {{ app.capitalize() }}
    {% for el in addon_name.items() %}
        {% set name =  el[0]  %}
        {% for p in el[1].items() %}
            {% set path = p[1] %}
<a href="/{{ path }}">{{ name }}</a>
        {% endfor %}
    {% endfor %}
{% endfor %}
