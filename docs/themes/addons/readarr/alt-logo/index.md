# Readarr Alternative Logo

Adds a audiobook logo to your Readarr css.

<p>
<a href="desktop.png" rel="noopener"><img src="desktop.png" alt="Screen Shot 1" width="50%" /></a>
<a href="mobile.png" rel="noopener"><img src="mobile.png" alt="Screen Shot 1" width="50%" /></a>
</p>

## Setup

### Docker mod

`-e TP_ADDON=readarr-alt-logo`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/readarr/THEME.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/readarr/readarr-alt-logo/readarr-alt-logo.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/readarr/THEME.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/addons/readarr/readarr-alt-logo/readarr-alt-logo.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/<APP_NAME>/<THEME>.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/addons/readarr/readarr-alt-logo/readarr-alt-logo.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/css/base/readarr/THEME.css";
@import "https://theme-park.dev/css/addons/readarr/readarr-alt-logo/readarr-alt-logo.css";
```
