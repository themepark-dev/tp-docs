{% set github_link = "https://github.com/NginxProxyManager/nginx-proxy-manager" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

#### Docker

Download the script from the theme.park repo `docker-mods/nginx-proxy-manager/root/etc/cont-init.d/98-themepark` and save it on your host.

Mount the file to `/etc/cont-init.d/98-themepark` like so:

```yml
    volumes:
      - /your/save/path/98-themepark-npm:/etc/cont-init.d/99-themepark
```

```bash
    -v /your/save/path/98-themepark-npm:/etc/cont-init.d/99-themepark
```

!!! Warning
    Make sure the file is executable! `chmod +x 98-themepark-npm`

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}