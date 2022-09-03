# Sonarr text logo

Add a text logo to your Sonarr css.

<p>
<a href="desktop.png" rel="noopener"><img src="desktop.png" alt="Screen Shot 1" /></a>
</p>

## Setup

### Docker mod

`-e TP_ADDON=sonarr-text-logo`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/sonarr/THEME.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/sonarr/sonarr-text-logo/sonarr-text-logo.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/sonarr/THEME.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/sonarr/sonarr-text-logo/sonarr-text-logo.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/<APP_NAME>/<THEME>.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/sonarr/sonarr-text-logo/sonarr-text-logo.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/css/base/sonarr/THEME.css";
@import "https://theme-park.dev/css/addons/sonarr/sonarr-text-logo/sonarr-text-logo.css";
```

### Traefik

>
!!! warning
    Added in traefik-themepark version `v1.2.0`

Use <a href="/setup/#traefik" rel="noopener">traefik-themepark middleware</a>.

```yaml
middlewares:
    sonarr-text-logo:
        plugin:
            themepark:
                app: sonarr
                theme: base
                addons:
                    - sonarr-text-logo
```
