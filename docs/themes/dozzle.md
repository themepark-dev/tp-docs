{% set github_link = "https://github.com/amir20/dozzle" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! warning  "CSP"
    As dozzle will block the theme with its content security policy you need to change or remove the CSP header.
    Add this in your reverse proxy to remove the headers:

```nginx
proxy_hide_header "x-webkit-csp";
proxy_hide_header "content-security-policy";
```

#### Nginx variable example

```nginx
      server {
        ...

        location / {
            proxy_pass http://<dozzle.container.ip.address>:8080;
            set $app dozzle;
            include /config/nginx/theme-park.conf;
            proxy_hide_header "x-webkit-csp";
            proxy_hide_header "content-security-policy";
        }

        location /api {
            proxy_pass http://<dozzle.container.ip.address>:8080;
            proxy_buffering off;
            proxy_cache off;
        }
    }
```

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}