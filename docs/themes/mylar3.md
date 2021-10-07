<h1 align="center"> <img src="/site_assets/mylar3/logo.png" alt="logo" width="30" height="30"> Mylar 3</h1>

Custom [Mylar 3](https://github.com/mylar3/mylar3) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/mylar3/organizr-dark.png)

```css
{% set themes = config.extra.themes %}
https://theme-park.dev/CSS/themes/mylar3/XXX.css
{% for theme in themes %}
{{ theme }}.css
{% endfor %}
```

## 🛠️ Installation

### [Setup](/setup)

!!!note
    Set `Interface` to `carbon`
![](/site_assets/mylar3/settings.png)

{% set addons = extra.addons %}
{% set title = mylar3 %}
{% for app, addon_name in addons.items() %}
    {% if app  ==  title %}

### Addons

        {% for el in addon_name.items() %}
            {% set name =  el[0]  %}
            {% for p in el[1].items() %}
            {% set path = p[1] %}

### [{{ name }}](/{{ path }})

            {% endfor %}
        {% endfor %}
    {% endif %}
{% endfor %}

## Screenshots

{% set themes = config.extra.themes %}
{% for theme in themes %}
<p align="center">  
<a href="/site_assets/mylar3/{{ theme }}.png">{{ theme.capitalize() }} Theme<img src="/site_assets/mylar3/{{ theme }}.png"></img>
</p>
{% endfor %}
