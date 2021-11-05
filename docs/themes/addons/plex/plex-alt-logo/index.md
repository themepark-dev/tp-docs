# Plex Alternative Logo

Extra CSS that replaces the plex logo with your own.
To be able to switch the default logo you must host this file your self and change the image url in the css. (See [Custom](/custom))

<p>
<a href="plex-alt-logo.png" rel="noopener"><img src="plex-alt-logo.png" alt="Screen Shot 1"/></a>
</p>

## Setup

### Docker mod

`-e TP_ADDON=plex-alt-logo`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/plex/plex-base.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/theme-options/overseerr.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/plex/plex-alt-logo/plex-alt-logo.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/plex/plex-base.css">
   <link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/theme-options/overseerr.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/plex/plex-alt-logo/plex-alt-logo.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/plex/plex-base.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/theme-options/overseerr.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/plex/plex-alt-logo/plex-alt-logo.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import url("https://theme-park.dev/css/base/plex/plex-base.css");
@import url("https://theme-park.dev/css/theme-options/overseerr.css");
@import url("https://theme-park.dev/css/addons/plex/plex-alt-logo/plex-alt-logo.css");
```
