# Theme Options

{% set themes = config.extra.themes %}
<p align="center">
{% for theme in themes %}
<a href="/theme-options/{{ theme }}"><img src="/theme-options/{{ theme.replace('-',' ') }}_banner.png"/></a>
{% endfor %}
</p>
