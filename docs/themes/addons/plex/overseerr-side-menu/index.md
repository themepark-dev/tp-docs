# Overseerr Side Menu

Extra CSS that makes the side menu look like it does in Overseerr.

<p>
<a href="side_menu.png" rel="noopener"><img src="side_menu.png" alt="Screen Shot 1" width="66%" /></a>
</p>


## Setup

### Docker mod

`-e TP_ADDON=overseerr-side-menu`

If adding multiple mods, enter them in an array separated by  `|`. `-e TP_ADDON=addon1|addon2`

### Nginx

Examples of how to add it:

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</head>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/plex/overseerr.css">
<link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/addons/plex/overseerr-side-menu/overseerr-side-menu.css">
</head>';
sub_filter_once on;
```

### Apache

```nginx
AddOutputFilterByType SUBSTITUTE text/html
   Substitute 's|</head> '<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/plex/overseerr.css">
   <link rel="stylesheet" type="text/css" href="https://theme-park.dev/CSS/addons/plex/overseerr-side-menu/overseerr-side-menu.css">
</head>';|'
```

### Caddy

```nginx
filter rule {
    content_type text/html.*
    search_pattern </head>
    replacement "<link rel='stylesheet' type='text/css' href='https://theme-park.dev/css/base/plex/overseerr.css'><link rel='stylesheet' type='text/css' href='https://theme-park.dev/CSS/addons/plex/overseerr-side-menu/overseerr-side-menu.css'></head>"
}
```

### Stylus

Just add another import line.

```css
@import url("https://theme-park.dev/css/base/plex/overseerr.css");
@import url("https://theme-park.dev/CSS/addons/plex/overseerr-side-menu/overseerr-side-menu.css");
```
