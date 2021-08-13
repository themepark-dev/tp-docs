<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://xbackbone.app/) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr-dark.png)

```css
{% set themes = config.extra.themes %}
https://theme-park.dev/CSS/themes/{{ page.title.split()[0].lower() }}/XXX.css
{% for theme in themes %}
{{ theme }}.css
{% endfor %}
```

## 🛠️ Installation

### Setup

1. Go to the `System` menu
2. Set theme to `Default - Bootstrap 4 default theme`
3. Add the HTML below in the `Custom HTML Head content` textarea. Remember to change `<THEME>` to the theme you want.

```html
<link type="text/css" rel="Stylesheet" href="https://theme-park.dev/CSS/themes/xbackbone/xbackbone-base.css"/>
<link type="text/css" rel="Stylesheet" href="https://theme-park.dev/CSS/variables/<THEME>.css"/>
```

<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/system_settings.png"><img src="/site_assets/{{ page.title.split()[0].lower() }}/system_settings.png"></img>
</p>

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
