{% set github_link = "https://github.com/qbittorrent/qbittorrent" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! info "ENV"
    - Use `QBITTORRENT_VERSION`=`x.x.x` if you need to use a specific version of the qbittorrent UI.
    - Use `TP_DISABLE_THEME`=`true` to revert and restore all changes if something is broken. 

!!! warning "Subfilter CSP"
    As Qbittorrent will block the theme with its content security policy you need to change or remove the CSP header.
    Add this in your reverse proxy to remove the headers:

```nginx
proxy_hide_header "x-webkit-csp";
proxy_hide_header "content-security-policy";
proxy_hide_header "X-Frame-Options";
```

#### Custom headers in QbitTorrent Settings

If you don't want to remove the headers using a webserver, you can also override the CSP header with a custom one.

Add the following in `Add custom HTTP headers` on the `Web UI` section.

```nginx
content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;
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

!!! warning "Subfilter"
    If you get errors in the browser console, and the RSS tab stop working (See [https://github.com/themepark-dev/theme.park/issues/132](https://github.com/themepark-dev/theme.park/issues/132))
    You need to subfilter the `</body>` tag instead of the `</head>` tag.

#### Example

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</body>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/qbittorrent/<THEME>.css">
</body>';
sub_filter_once on;
```

![](../site_assets/{{ page.title.split()[0].lower() }}/CSP.png)

This will allow stylesheets and image sources from theme-park.dev and raw.githubusercontent.com domains.

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}