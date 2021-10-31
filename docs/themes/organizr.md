<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/causefx/Organizr) CSS

<p align="center">Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/dark.png)

```css
{% set themes = config.extra.themes %}
https://theme-park.dev/css/base/{{ page.title.split()[0].lower() }}/XXX.css
{% for theme in themes %}
{{ theme }}.css
{% endfor %}
```

## 🛠️ Installation

The themes can be found in the `Marketplace` menu in Organizr.

1. Go to `Settings`-> `Marketplace` -> Click install on wanted theme.

2. To activate a theme go to `Settings` -> `Customize` -> `Appearance` -> `Colors & Themes` -> Select the theme in the dropdown.

3. If you want to use a theme option that's not in the marketplace you can a theme using `Custom CSS`

e.g.

```css
@import url("https://theme-park.dev/css/base/organizr/organizr-base.css");
@import url("https://theme-park.dev/css/theme-options/overseerr.css");
```

{% set addons = extra.addons %}
{% set title = page.title.split()[0].lower() %}
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
<a href="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png">{{ theme.capitalize() }} Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png"></img>
</p>
{% endfor %}