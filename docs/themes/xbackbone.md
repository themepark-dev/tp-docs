{% set github_link = "https://xbackbone.app" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

`> v3.5.0`

1. Go to the `System` menu
2. Select the theme you want in the `Theme` dropdown menu
3. Click Apply

<p align="center">  
<a href="../site_assets/{{ page.title.split()[0].lower() }}/dropdown.png"><img src="/site_assets/{{ page.title.split()[0].lower() }}/dropdown.png"></img></a>
</p>

`< v3.5.0`

1. Go to the `System` menu
2. Set theme to `Default - Bootstrap 4 default theme`
3. Add the HTML below in the `Custom HTML Head content` textarea. Remember to change `<THEME>` to the theme you want.

```html
<link type="text/css" rel="Stylesheet" href="https://theme-park.dev/css/base/xbackbone/<THEME>.css"/>
```

<p align="center">  
<a href="../site_assets/{{ page.title.split()[0].lower() }}/system_settings.png"><img src="/site_assets/{{ page.title.split()[0].lower() }}/system_settings.png"></img></a>
</p>

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}