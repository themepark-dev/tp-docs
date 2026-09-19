{% set github_link = "https://github.com/MediaBrowser/Emby" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

### Docker Mod

!!! note  "Docker Mod 🐳"
    Set the theme to `Light` as the [mod](https://github.com/themepark-dev/theme.park/blob/master/docker-mods/{{ page.title.split()[0].lower() }}/root/etc/cont-init.d/98-themepark) changes the `/dashboard-ui/modules/themes/light/theme.css` file

### Subfilter

!!! warning Subfiltering
    Subfiltering can make your Emby instance unavailable remotely. Seems like they have some security features, or something breaks when changing the HTML.

    You need to subfilter the `</body>` instead of the `</head>` tag. See example below.

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</body>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/emby/dracula.css">
</body>';
sub_filter_once on;
```

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}