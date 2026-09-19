{% set github_link = "https://github.com/pi-hole/pi-hole" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! note
    Tested on Web Interface v5.5
     Set theme to dark in the Web  interface menu.

!!! warning "Subfilter CSP"
    Because Pi-hole uses CSP it will block any attempts to inject stylesheets.
    This will add `https://raw.githubusercontent.com` and `https://theme-park.dev` to the CSP meta tag in the HTML. Allowing you to load the custom css.

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/pihole/<THEME>.css">
</head>';
sub_filter_once on;
proxy_hide_header Content-Security-Policy;
add_header Content-Security-Policy "default-src 'none'; base-uri 'none'; child-src 'self'; form-action 'self'; frame-src 'self'; font-src 'self'; connect-src 'self'; img-src 'self' https://raw.githubusercontent.com; manifest-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' https://raw.githubusercontent.com https://theme-park.dev 'unsafe-inline'";
```

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}