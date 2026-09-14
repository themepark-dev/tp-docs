<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/jellyfin/jellyfin) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)


## 🛠️ Installation

Choose one method below. Use subfiltering if you want the dashboard
themed too.

### Built-in Custom CSS

These screenshots show Jellyfin 12.0.

Open **Dashboard > Branding** and add this to **Custom CSS code**, replacing
`<THEME>` with a [theme option](/theme-options/). Save your changes.

```css
@import url("https://theme-park.dev/css/base/jellyfin/<THEME>.css");
```

For example, Nord:

```css
@import url("https://theme-park.dev/css/base/jellyfin/nord.css");
```

### Subfiltering, including the dashboard

Jellyfin 12 does not load its Custom CSS setting in the admin dashboard.
To theme those pages too, use [subfiltering](/setup/#subfiltering) instead of
the built-in method. Remove any theme.park import from **Custom CSS code**
and save before switching.

Follow the setup guide for your reverse proxy and inject this stylesheet into
the web client HTML, replacing `<THEME>` with your selected theme option:

```text
https://theme-park.dev/css/base/jellyfin/<THEME>.css
```

Keep injection out of API, media, and WebSocket responses. Subfiltering themes
both regular pages and the dashboard without a second import in Jellyfin.

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
