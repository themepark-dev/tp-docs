# Readarr Darker

A darker theme for Readarr that uses the same accents and colors as the default theme

<p>
<a href="screenshot1.png" rel="noopener"><img src="screenshot1.png" alt="Screen Shot 1" /></a>
</p>

## Setup

### Docker mod

`-e TP_ADDON=readarr-darker`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/readarr/readarr-base.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/readarr/readarr-darker/readarr-darker.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/readarr/readarr-base.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/readarr/readarr-darker/readarr-darker.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/readarr/readarr-base.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/readarr/readarr-darker/readarr-darker.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/css/base/readarr/readarr-base.css";
@import "https://theme-park.dev/css/addons/readarr/readarr-darker/readarr-darker.css";
```

### Traefik

>
!!! warning
    Added in traefik-themepark version `v1.2.0`

Use <a href="/setup/#traefik" rel="noopener">traefik-themepark middleware</a>. 

```yaml
middlewares:
    readarr-darker:
        plugin:
            themepark:
                app: readarr
                theme: base
                addons:
                    - darker
```
