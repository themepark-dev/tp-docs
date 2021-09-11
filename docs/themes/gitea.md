<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/go-gitea/gitea) CSS

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

!!! info
    Tested on `Version: 1.14.0`

### [Setup](/setup)

If you want to add the theme with subfilter ect, click here: [https://docs.theme-park.dev/setup/#methods](https://docs.theme-park.dev/setup/#methods)

The theme is built on top of the `Gitea` theme, so make sure that is selected in user settings.
![select](/site_assets/gitea/select_theme.png)

In the `templates` folder create a folder called `custom` and add a file called `header.tmpl` with the contents: 

```html
<link rel="stylesheet" href="{{StaticUrlPrefix}}/css/theme-{{DefaultTheme}}.css">
<link rel="stylesheet" href="{{AppSubUrl}}/css/{{.SignedUser.Theme}}.css">
<link rel="stylesheet" href="https://theme-park.dev/CSS/themes/gitea/gitea-base.css">
<link rel="stylesheet" href="https://theme-park.dev/CSS/variables/{{.SignedUser.Theme}}.css">
```
<link rel="stylesheet" href="{{AppSubUrl}}/styles.css">
<link rel="stylesheet" href="{{AppSubUrl}}/css/gitea.css">
<link rel="stylesheet" href="{{AppSubUrl}}/css/{{.SignedUser.Theme}}.css">
<link rel="stylesheet" href="https://theme-park.dev/CSS/themes/gitea/gitea-base.css">
<link rel="stylesheet" href="https://theme-park.dev/CSS/variables/{{.SignedUser.Theme}}.css">
In the ..conf/app.ini add the following.

```ini
[ui]
THEMES        = gitea,arc-green,plex,aquamarine,dark,dracula,hotline,organizr-dark,space-gray,hotpink,mind,onedark,overseerr,power,reality,soul,space,time
DEFAULT_THEME = gitea
```

Restart Gitea and you should now see the theme being loaded.

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