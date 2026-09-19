{% set github_link = "https://github.com/WDaan/VueTorrent" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! info
    Tested on qBittorrent v4.3+

!!! warning Subfiltering
    As the main VueTorrent theme uses inline styling in the HTML, you need to subfilter the `</body>` instead of the `</head>` tag. See example below.

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</body>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/vuetorrent/aquamarine.css">
</body>';
sub_filter_once on;
```

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}