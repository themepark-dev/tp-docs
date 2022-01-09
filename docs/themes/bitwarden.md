<h1 align="center"> <img src="/site_assets/{{ page.title.split()[0].lower() }}/logo.png" alt="logo" width="30" height="30"> {{ page.title.split()[0] }}</h1>

Custom [{{ page.title.split()[0] }}](https://github.com/bitwarden) CSS

<p align="center"> Organizr Dark Theme </p>

![](/site_assets/{{ page.title.split()[0].lower() }}/organizr.png)


## 🛠️ Installation

### [Setup](/setup)

Due to Bitwarden's `Content-Security-Policy` header, it is necessary to adjust this policy to include the domain(s) to load stylesheets from. Open `bwdata/config.yml` and add the domain name(s) to the `nginx_header_content_security_policy` property in the `style-src` policy directive.

```yaml
...
nginx_header_content_security_policy: "default-src 'self'; style-src 'self' 'unsafe-inline' [domainnamehere]; ..."
...
```

!!! warning "nginx_header_content_security_policy was trimmed"
    The `nginx_header_content_security_policy` was trimmed for brevity. Adjust your own copy from Bitwarden or it might lead to unexpected results.

Where `[domainnamehere]` should be replaced with `theme-park.dev raw.githubusercontent.com` or your own custom domain. This will allow stylesheets sources to load from the specified domain(s).

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
