{% set github_link = "https://github.com/jellyfin/jellyfin" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

Go to `Dashboard` -> `General` and scroll down to `Branding`

In the custom CSS input field add:

```css
@import url("https://theme-park.dev/css/base/jellyfin/<THEME>.css");
```

and hit save.

i.e.

```css
@import url("https://theme-park.dev/css/base/jellyfin/nord.css");
```

<img src="/site_assets/{{ page.title.split()[0].lower() }}/example.png"></img>

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}