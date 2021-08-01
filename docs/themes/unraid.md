<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://unraid.net) CSS

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

### [Setup](/setup)

#### Theme Engine

1. Install the [Theme Engine](https://forums.unraid.net/topic/87126-plugin-theme-engine-a-webgui-styler/) plugin from the CA appstore and open it.
2. Set `Base Theme` to black
3. Enable `Advanced View`
4. Set `Enable Theme Engine:` to `No`
5. Scroll down and set `Enable custom styling (below):` to `Yes`
6. Add the HTML below in the `Custom styling (advanced):` textarea. Remember to change `<THEME>` to the theme you want.

7. **Optional:** Go to `Settings` -> `Display Settings` and set `Header custom text color:` to `FFF` and `Header custom background color:` to `000`

```html
</style><link type="text/css" rel="Stylesheet" href="https://theme-park.dev/CSS/themes/unraid/<THEME>.css" />
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
