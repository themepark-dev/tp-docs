## Setup

### Docker mod

`-e TP_ADDON={{ addon_name }}`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/{{ addon_app }}/THEME.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/{{ addon_app }}/{{ addon_name }}/{{ addon_name }}.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/{{ addon_app }}/THEME.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/{{ addon_app }}/{{ addon_name }}/{{ addon_name }}.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/<APP_NAME>/<THEME>.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/{{ addon_app }}/{{ addon_name }}/{{ addon_name }}.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/css/base/{{ addon_app }}/THEME.css";
@import "https://theme-park.dev/css/addons/{{ addon_app }}/{{ addon_name }}/{{ addon_name }}.css";
```

### Traefik

>
!!! warning
    Added in traefik-themepark version `v1.2.0`

Use <a href="/setup/#traefik" rel="noopener">traefik-themepark middleware</a>.

```yaml
middlewares:
    {{ addon_name }}:
        plugin:
            themepark:
                app: {{ addon_app }}
                theme: base
                addons:
                    - {{ addon_name }}
```
