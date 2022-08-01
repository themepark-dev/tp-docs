<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/NginxProxyManager/nginx-proxy-manager) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)

## 🛠️ Installation

### [Setup](/setup)

#### Docker

Download the script from the theme.park repo `docker-mods/nginx-proxy-manager/root/etc/cont-init.d/98-themepark` and save it on your host.

Mount the file to `/etc/cont-init.d/98-themepark` like so:

```yml
    volumes:
      - /your/save/path/98-themepark-npm:/etc/cont-init.d/99-themepark
```

```bash
    -v /your/save/path/98-themepark-npm:/etc/cont-init.d/99-themepark
```

!!! Warning
    Make sure the file is executable! `chmod +x 98-themepark-npm`

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
