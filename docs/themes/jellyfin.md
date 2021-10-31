<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/jellyfin/jellyfin) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)

```css
{% set themes = config.extra.themes %}
https://theme-park.dev/css/base/{{ page.title.split()[0].lower() }}/XXX.css
{% for theme in themes %}
{{ theme }}.css
{% endfor %}
```

## 🛠️ Installation

### Setup

Go to `Dashboard` -> `General` and scroll down to `Branding`

In the custom CSS input field add:

```css
@import url("https://theme-park.dev/css/base/jellyfin/jellyfin-base.css");
@import url("https://theme-park.dev/css/theme-options/<THEME>.css");
```

and hit save.

i.e.

```css
@import url("https://theme-park.dev/css/base/jellyfin/jellyfin-base.css");
@import url("https://theme-park.dev/css/theme-options/dracula.css");
```

<img src="/site_assets/{{ page.title.split()[0].lower() }}/example.png"></img>

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
