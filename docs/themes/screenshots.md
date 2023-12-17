## Screenshots

{% set themes = config.extra.themes %}
{% for theme in themes %}
<p align="center">  
<a href="/site_assets/{{ page.file.name }}/{{ theme }}.png">{{ theme.capitalize() }} Theme<img src="/site_assets/{{ page.file.name }}/{{ theme }}.png"></img>
</p>
{% endfor %}