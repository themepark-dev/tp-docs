<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/pihole/pihole) CSS

<p align="center"> Aquamarine Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/aquamarine.png)

```css
https://gilbn.github.io/theme.park/CSS/themes/{{ page.title.split()[0].lower() }}/XXX.css
aquamarine.css
hotline.css
plex.css
dark.css
space-gray.css
organizr-dark.css
```

## 🛠️ Installation

### [Setup](/setup)

!!! note
    Tested on Web Interface v5.1
     Set theme to dark in the Web  interface menu.

!!! warning "CSP"
    Because Pi-hole uses CSP it will block any attempts to inject stylesheets.
    This will add `https://raw.githubusercontent.com` and `https://gilbn.github.io` to the CSP meta tag in the HTML. Allowing you to load the custom css.

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; base-uri \'none\'; child-src \'self\'; form-action \'self\'; frame-src \'self\'; font-src \'self\'; connect-src \'self\'; img-src \'self\'; manifest-src \'self\'; script-src \'self\' \'unsafe-inline\'; style-src \'self\' \'unsafe-inline\'">'
'<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; base-uri \'none\'; child-src \'self\'; form-action \'self\'; frame-src \'self\'; font-src \'self\'; connect-src \'self\'; img-src \'self\' https://raw.githubusercontent.com; manifest-src \'self\'; script-src \'self\' \'unsafe-inline\'; style-src \'self\' https://raw.githubusercontent.com https://gilbn.github.io \'unsafe-inline\'">';
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://gilbn.github.io/theme.park/CSS/themes/pihole/<THEME>.css">
</head>';
sub_filter_once on;
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
<a href="/site_assets/{{ page.title.split()[0].lower() }}/hotline.png">Hotline Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/hotline.png"></img>
</p>

<p align="center">
<a href="/site_assets/{{ page.title.split()[0].lower() }}/aquamarine.png">Aquamarine Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/aquamarine.png"></img>
</p>
