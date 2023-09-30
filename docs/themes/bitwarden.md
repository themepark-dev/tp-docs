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

#### Vaultwarden

For Vaultwarden you can edit your webserver config with the following:

##### Nginx Example

```nginx
proxy_hide_header "content-security-policy";
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' develop.theme-park.dev theme-park.dev; img-src 'self' data: https://haveibeenpwned.com/ https://www.gravatar.com ; child-src 'self' https://*.duosecurity.com https://*.duofederal.com; frame-src 'self' https://*.duosecurity.com https://*.duofederal.com; connect-src 'self' https://api.pwnedpasswords.com/range/ https://2fa.directory/api/ https://app.simplelogin.io/api/ https://app.anonaddy.com/api/ https://relay.firefox.com/api/; object-src 'self' blob:; frame-ancestors 'self' chrome-extension://nngceckbapebfimnlniiiahkandclblb chrome-extension://jbkfoedolllekgbhcbcoahefnbanhhlh moz-extension://*" ;
```

This removes the header set by Vaultwarden and replaces it with the one below.

The CSP policy Vaultwarden uses was found using [https://securityheaders.com/](https://securityheaders.com/)

!!! warning
    As the policy Vaultwarden uses might change in the future, I recommend getting the policy from securityheaders.com and adding `theme-park.dev` or your own domain if you are selfhosting to the `style-src` section.
    (See below for an example.)

```nginx
style-src 'self' 'unsafe-inline' theme-park.dev somedomain.com ...
```

<img src="/site_assets/{{ page.title.split()[0].lower() }}/csp.png"></img>

##### Selfhosting

Another option is to selfhost the CSS files on the same domain as you host Vaultwarden. e.g vaultwarden.domain.com/themepark or domain.com/themepark

By hosting the files on the same domain, the CSP rule will allow the css files to be loaded.

###### Subdomain example

The example below reverse proxies the [theme.park docker container](/setup/#selfhosting) to be available at `vaultwarden.domain.com/themepark`.

!!! note
    The example below is a modified config from the LSIO SWAG image. I have removed several location blocks for demonstration purposes.
    Add your domain to the `set $tp_domain` part of the config or edit the `sub_filter` line directly.

```nginx
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name vaultwarden.*;

    include /config/nginx/ssl.conf;

    client_max_body_size 128M;

    location / {
        include /config/nginx/proxy.conf;
        include /config/nginx/resolver.conf;
        set $upstream_app vaultwarden;
        set $upstream_port 80;
        set $upstream_proto http;
        proxy_pass $upstream_proto://$upstream_app:$upstream_port;

        set $app bitwarden;
        set $theme nord;
        set $tp_domain vaultwarden.domain.com/themepark; # You can also do: $scheme://$host/themepark

        proxy_set_header Accept-Encoding ""; 
        sub_filter
        '</head>'
        '<link rel="stylesheet" type="text/css" href="https://$tp_domain/css/base/$app/$app-base.css">
        <link rel="stylesheet" type="text/css" href="https://$tp_domain/css/theme-options/$theme.css"></head>';
        sub_filter_once on;

    }

    # ...snip... 
    # removed multiple location blocks for demonstration purposes.

    location /themepark {
        return 301 $scheme://$host/themepark/;
    }
    location ^~ /themepark/ {
        set $upstream_app theme-park;
        set $upstream_port 443;
        set $upstream_proto https;
        proxy_set_header Host $host;
        proxy_pass $upstream_proto://$upstream_app:$upstream_port;
    }

}
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
