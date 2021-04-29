<h1 align="center"> <img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title }}</h1>

Custom [{{ page.title }}](https://github.com/morpheus65535/bazarr) CSS

<p align="center"> Organizr Dark Theme </p>

![]({{ config.site_url }}site_assets/{{ page.title.lower() }}/organizr-dark.png)

```css
https://gilbn.github.io/theme.park/CSS/themes/{{ page.title.lower() }}/XXX.css
aquamarine.css
hotline.css
plex.css
dark.css
space-gray.css
organizr-dark.css
```

## 🛠️ Installation

### [Setup]({{ config.site_url }}setup)

{% set addons = extra.addons %}
{% set title = page.title.lower() %}
{% for app, addon_name in addons.items() %}
    {% if app  ==  title %}

### Addons

        {% for el in addon_name.items() %}
            {% set name =  el[0]  %}
            {% for p in el[1].items() %}
            {% set path = p[1] %}

### [{{ name }}]({{ config.site_url }}{{ path }})

            {% endfor %}
        {% endfor %}
    {% endif %}
{% endfor %}

## Screenshots

<p align="center">  
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/dark.png">Dark Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/dark.png"></img>
</p>

<p align="center">  
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/space-gray.png">Space Gray Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/space-gray.png"></img>
</p>

<p align="center">  
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/plex.png">Plex Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/plex.png"></img>
</p>

<p align="center">
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/organizr-dark.png">Organizr Dark Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/organizr-dark.png"></img>
</p>

<p align="center">
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/hotline.png">Hotline Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/hotline.png"></img>
</p>

<p align="center">
<a href="{{ config.site_url }}site_assets/{{ page.title.lower() }}/aquamarine.png">Aquamarine Theme<img src="{{ config.site_url }}site_assets/{{ page.title.lower() }}/aquamarine.png"></img>
</p>
