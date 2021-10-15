<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }} (Deprecated)</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/grafana) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)

```css
https://theme-park.dev/CSS/themes/{{ page.title.split()[0].lower() }}/XXX.css
aquamarine.css
hotline.css
plex.css
dark.css
space-gray.css
organizr.css
```

## 🛠️ Installation

### [Setup](/setup)

Can be installed with reverse-proxy/ Stylus ect. (See wiki)

#### Grafana Plugin

Or use the theme plugin: [https://grafana.com/grafana/plugins/yesoreyeram-boomtheme-panel](https://grafana.com/grafana/plugins/yesoreyeram-boomtheme-panel)

#### Organizr

For panel integration on the Organizr homepage you can use `organizr-dashboard.css`. The theme is an "internal" theme that is meant to be used in an Organizr iframe as the background is set to transparent.
NOTE: When viewing Grafana in Organizr iframe using `organizr-dashboard.css` it will follow the Organizr theme. When viewing it outside of Organizr iframe the background will be white ect. If you don't want this you can create two reverse proxies. One for grafana organizr homepage integration and one for the regular grafana theme.

!!! info "Guide"
    Check out [https://technicalramblings.com/blog/spice-up-your-homepage-part-ii/](https://technicalramblings.com/blog/spice-up-your-homepage-part-ii/)

<img src="/site_assets/grafana/orgdash.jpg" height="500px"></img>

!!! note
    Click the `kiosk` button and use that link if you don't want to show the top bar and side bar inside Organizr! There are two modes, one where the side menu and variables ect disappear and one where just the panels are visible.

![view](/site_assets/grafana/view.png)

Check out my Varken dashboard here: https://grafana.com/dashboards/9558

### Custom HTML for Organizr Homepage

![](/site_assets/grafana/3.png)

??? info "Expand"

    Change the **Panel name** to what you want and the **src** to the panel URL.

    ```css
    <h5><span>Panel name</span></h5>
    <div class="overflowhider"><embed id="grafanadwidget1" src='https://graforg.domain.com/panel-embed-link'/>**
    ```

    The URL can be found by clicking **share** on the panel you want to add.

    ![embed](/site_assets/grafana/4.png)

    If you dont want the ***Panel name*** text, just remove the `<h5><span>` line entirely.

    ```css
    <style>
    .flex {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center;
        background: transparent;
        margin-top:10px;
        box-shadow: none !important;
    }
    .flex-child {
        flex: 1 1 1 1;
        padding: 1px 1px 1px 1px;
    }
    #flex-grafanadwidget1 {
        min-width: 25%;
    }
    #flex-grafanadwidget2 {
        min-width: 25%;
    }
    #flex-grafanadwidget3 {
        min-width: 25%;
    }
    #flex-grafanadwidget4 {
        min-width: 25%;
    }
    @media only screen and (max-width: 1374px) {
        #flex-grafanadwidget1, #flex-grafanadwidget2, #flex-grafanadwidget3, #flex-grafanadwidget4 {
            min-width: 50%;
        }
    }
    @media only screen and (max-width: 640px) {
        #flex-grafanadwidget1, #flex-grafanadwidget2, #flex-grafanadwidget3, #flex-grafanadwidget4 {
            min-width: 100%;
        }
    @media only screen and (max-width: 400px) {
        .flex-child>h5 {
        margin-left: 15px;
        }
    #announcementRow {
        background-color:transparent !important;
    }
    .flex-child>h5 {
        text-transform: uppercase;
        font-weight: 600 !important;
        font-size: 15px;important;
        color: #eee;
    }
    .overflowhider {
        height: 100%;
        overflow: hidden;
    }
    #grafanadwidget1 {
        position: relative;
        height: calc(250px);
        width: calc(100%);
    }
    #grafanadwidget2 {
        position: relative;
        height:calc(250px);
        width:calc(100%);
    }
    #grafanadwidget3 {
        position: relative;
        height: calc(250px);
        width: calc(100%);
    }
    #grafanadwidget4 {
        position: relative;
        height:calc(250px);
        width:calc(100%);
    }
    </style>

    <div id="announcementRow" class="row">
        <div class="content-box flex">
    <div class="flex-child" id="flex-grafanadwidget1">
    <h5><span>Panel name</span></h5>
    <div class="overflowhider"><embed id="grafanadwidget1" src='https://graforg.domain.com/panel-embed-link'/></div>
    </div>
    <div class="flex-child box-shadow" id="flex-grafanadwidget2">
    <h5><span>Panel name</span></h5>
    <div class="overflowhider"><embed id="grafanadwidget2" src='https://graforg.domain.com/panel-embed-link' /></div>
    </div>
    <div class="flex-child" id="flex-grafanadwidget3">
    <h5><span>Panel name</span></h5>
    <div class="overflowhider"><embed id="grafanadwidget3" src='https://graforg.domain.com/panel-embed-link'/></div>
    </div>
    <div class="flex-child box-shadow" id="flex-grafanadwidget4">
    <h5><span>Panel name</span></h5>
    <div class="overflowhider"><embed id="grafanadwidget4" src='https://graforg.domain.com/panel-embed-link' /></div>
    </div>
        </div>
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

{% set themes = config.extra.themes %}
{% for theme in themes %}
<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png">{{ theme.capitalize() }} Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png"></img>
</p>
{% endfor %}
