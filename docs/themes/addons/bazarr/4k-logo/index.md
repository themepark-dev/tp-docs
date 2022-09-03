# Bazarr 4K logo

Adds a 4K logo to your Bazarr css.

<div class="row">
<p><a href="desktop.png" rel="noopener"><img src="desktop.png" alt="Screen Shot 1" width="49.5%" /></a>
<a href="mobile.png" rel="noopener"><img src="mobile.png" alt="Screen Shot 1" width="24%" /></a></p>
</div>

## Setup

### Docker mod

`-e TP_ADDON=bazarr-4k-logo`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/bazarr/THEME.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/bazarr/bazarr-4k-logo/bazarr-4k-logo.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/bazarr/THEME.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/bazarr/bazarr-4k-logo/bazarr-4k-logo.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/<APP_NAME>/<THEME>.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/bazarr/bazarr-4k-logo/bazarr-4k-logo.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/css/base/bazarr/THEME.css";
@import "https://theme-park.dev/css/addons/bazarr/bazarr-4k-logo/bazarr-4k-logo.css";
```

### Traefik

>
!!! warning
    Added in traefik-themepark version `v1.2.0`

Use <a href="/setup/#traefik" rel="noopener">traefik-themepark middleware</a>. 

```yaml
middlewares:
    bazarr-4k-log:
        plugin:
            themepark:
                # The name of the supported application listed on https://docs.theme-park.dev/themes.
                app: bazarr

                # The name of the supported theme listed on https://docs.theme-park.dev/theme-options/ or https://docs.theme-park.dev/community-themes/
                theme: dark

                # This currently only supports '4k-logo' and 'darker' addons. Future addons that follow a similar syntax will work as well.
                # For refernce: https://docs.theme-park.dev/themes/addons/
                addons:
                    - 4k-logo
```
