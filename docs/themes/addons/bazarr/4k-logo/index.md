# Bazarr 4K logo

Adds a 4K logo to your Bazarr css.

<div class="row">
<p><a href="desktop.png" rel="noopener"><img src="desktop.png" alt="Screen Shot 1" width="49.5%" /></a>
<a href="mobile.png" rel="noopener"><img src="mobile.png" alt="Screen Shot 1" width="24%" /></a></p>
</div>

## Setup

### Docker mod

`-e TP_ADDON=bazarr-4k-logo`

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
