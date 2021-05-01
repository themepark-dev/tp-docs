<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/monitorr/monitorr) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr-dark.png)

```css
https://theme-park.dev/CSS/themes/{{ page.title.split()[0].lower() }}/XXX.css
aquamarine.css
hotline.css
plex.css
dark.css
space-gray.css
organizr-dark.css
organizr-dashboard.css
```

## 🛠️ Installation

### [Setup](/setup)

Add this in the Monitorr custom css box:

```css
@import "https://theme-park.dev/CSS/themes/monitorr/THEME_NAME.css";
```

The `organizr-dashboard.css` theme will mess with your Monitorr base theme. And it will hide the settings button. Go to /monitorr/settings.php for settings.  
It is created purely for use with "minimum" version of the index.php `https://domain.com/monitorr/index.min.php` for Organizr homepage integration.

!!! warning "organizr-dashboard.css"
    When viewing monitorr in Organizr iframe using `organizr-dashboard.css` it will follow the Organizr theme. 
    When viewing it outside of Organizr iframe the background will be white ect. If you don't want this you can create two reverse proxies.
    One for monitorr organizr homepage integration and one for the monitorr dark/plex theme. And use subfilter on both instead of adding `@import "https://theme-park.dev/CSS/themes/monitorr/organizr-dashboard.css";` in the monitorr custom css.

Add this in the Monitorr custom css box:

```css
@import "https://theme-park.dev/CSS/themes/monitorr/THEME_NAME.css";
```

And add this in custom HTML in Organizr:

```css
<div id="announcementRow" class="row"><h4 class="pull-left"><span>Monitorr</span></h4><hr class="hidden-xs"></div>
<div style="overflow:hidden; height:260px; width:calc(100% + 39px); -webkit-overflow-scrolling: touch; overflow-y: scroll;">
<iframe class="iframe" frameborder="0" src="https://monitorr.domain.com/index.min.php"></iframe>
</div>
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

<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/dark.png">Dark Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/dark.png"></img>
</p>

<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/space-gray.png">Space Gray Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/space-gray.png"></img>
</p>

<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/plex.png">Plex Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/plex.png"></img>
</p>

<p align="center">
<a href="/site_assets/{{ page.title.split()[0].lower() }}/organizr-dark.png">Organizr Dark Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/organizr-dark.png"></img>
</p>

<p align="center">
<a href="/site_assets/{{ page.title.split()[0].lower() }}/hotline.png">Hotline Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/hotline.png"></img>
</p>

<p align="center">
<a href="/site_assets/{{ page.title.split()[0].lower() }}/aquamarine.png">Aquamarine Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/aquamarine.png"></img>
</p>
