# Sonarr 4K logo

Add a 4K logo to your Sonarr css.

<p>
<a href="desktop.png" rel="noopener"><img src="desktop.png" alt="Screen Shot 1" width="33%" /></a>
<a href="v3-desktop.png" rel="noopener"><img src="v3-desktop.png" alt="Screen Shot 2" width="33%" /></a>
</p>
<p>
<a href="mobile.png" rel="noopener"><img src="mobile.png" alt="Screen Shot 1" width="33%" /></a>
<a href="v3-mobile.png" rel="noopener"><img src="v3-mobile.png" alt="Screen Shot 2" width="33%" /></a>
</p>

## Setup

### Docker mod

`-e TP_ADDON=sonarr-4k-logo`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/themes/sonarr/THEME.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/addons/sonarr/sonarr-4k-logo.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/themes/sonarr/THEME.css"><link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/addons/sonarr/sonarr-4k-logo.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/CSS/themes/<APP_NAME>/<THEME>.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/CSS/addons/sonarr/sonarr-4k-logo.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import "https://theme-park.dev/CSS/themes/sonarr/THEME.css";
@import "https://theme-park.dev/CSS/addons/sonarr/sonarr-4k-logo.css";
```
