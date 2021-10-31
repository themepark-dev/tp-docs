<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/qbittorrent/qbittorrent) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)

```css
{% set themes = config.extra.themes %}
https://theme-park.dev/css/base/{{ page.title.split()[0].lower() }}/XXX.css
{% for theme in themes %}
{{ theme }}.css
{% endfor %}
```

## 🛠️ Installation

### [Setup](/setup)

!!! warning "Subfilter CSP"
    As Qbittorrent will block the theme with its content security policy you need to change or remove the CSP header.
    Add this in your reverse proxy to remove the headers:

```nginx
proxy_hide_header "x-webkit-csp";
proxy_hide_header "content-security-policy";
proxy_hide_header "X-Frame-Options";
```

#### Nginx variable example

```nginx
location /qbt/ {
    proxy_pass              http://192.168.1.34:8080/;
    proxy_set_header        X-Forwarded-Host        $server_name:$server_port;
    proxy_hide_header       Referer;
    proxy_hide_header       Origin;
    proxy_set_header        Referer                 '';
    proxy_set_header        Origin                  '';
    add_header              X-Frame-Options         "SAMEORIGIN";

    set $app qbittorrent;
    include /config/nginx/theme-park.conf;

    proxy_hide_header   "x-webkit-csp";
    proxy_hide_header   "content-security-policy";
  }
```

#### ⚠️ Issues

If you get errors in the browser console, and the RSS tab stop working (See https://github.com/gilbN/theme.park/issues/132)
You need to subfilter the `<noscript>` tag instead of the `</head>` tag.

#### example

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'<noscript>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/qbittorrent/qbittorrent-base.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/theme-options/<THEME>.css">
<noscript>';
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

{% set themes = config.extra.themes %}
{% for theme in themes %}
<p align="center">  
<a href="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png">{{ theme.capitalize() }} Theme<img src="/site_assets/{{ page.title.split()[0].lower() }}/{{ theme }}.png"></img>
</p>
{% endfor %}
