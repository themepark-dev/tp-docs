<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/jellyfin/jellyfin) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)


## 🛠️ Installation

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

### Include the dashboard

Jellyfin 12 does not load its Custom CSS setting in the admin dashboard.
To theme those pages too, use [reverse-proxy subfiltering](/setup/#nginx).
For nginx, inject the chosen theme into the web client HTML:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter '</head>' '<link rel="stylesheet" href="https://theme-park.dev/css/base/jellyfin/nord.css"></head>';
sub_filter_once on;
```

Add this to the location that serves the web client. Keep API, media, and
WebSocket proxy configuration separate. Use one injection method to avoid
loading duplicate themes.

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
