{% set github_link = "https://github.com/NginxProxyManager/nginx-proxy-manager" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

The theme targets NPM's React UI, introduced in 2.13.0, and was verified with
**Nginx Proxy Manager 2.15.1** in both native light and dark modes. Older UI
versions are not supported by this rewrite.

#### Docker

For the official `jc21/nginx-proxy-manager` image, download the
[theme.park startup script](https://github.com/themepark-dev/theme.park/blob/master/docker-mods/nginx-proxy-manager/root/etc/cont-init.d/98-themepark)
and make it executable:

```bash
curl -fsSL https://raw.githubusercontent.com/themepark-dev/theme.park/master/docker-mods/nginx-proxy-manager/root/etc/cont-init.d/98-themepark -o 98-themepark-npm
chmod +x 98-themepark-npm
```

Add the script mount and theme settings to your existing NPM service:

```yaml
    environment:
      TP_THEME: organizr
    volumes:
      - /your/save/path/98-themepark-npm:/etc/cont-init.d/99-themepark:ro
```

Use the absolute path where you saved the script. Keep your existing NPM ports,
data volumes and other settings. Recreate the container after adding the mount
or changing a theme setting. Restarting the same container does not replace
stylesheet links already inserted into its HTML.

This image uses the mounted startup script, not the LinuxServer `DOCKER_MODS`
environment variable.

| Variable | Default | Purpose |
| --- | --- | --- |
| `TP_THEME` | `organizr` | Theme option name, such as `aquamarine` or `nord`. |
| `TP_COMMUNITY_THEME` | `false` | Set to `true` for a [community theme](/community-themes/), such as `catppuccin-latte`. |
| `TP_DOMAIN` | `theme-park.dev` | CSS host, without a scheme. Set this when self-hosting theme.park. |
| `TP_SCHEME` | `https` | Scheme used to fetch the CSS. |

The script inserts two stylesheet links: the NPM base CSS and the selected theme
option. Both must load. If the theme does not appear, check the container logs,
the script's executable permission, and the browser's stylesheet requests.
The CSS host must be reachable from your browser.

{% include-markdown "../themes/addons/addons.md" %}

NPM 2.15.1 with sample hosts and the rewritten theme.

{% include-markdown "../themes/screenshots.md" %}
