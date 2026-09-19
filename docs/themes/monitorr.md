{% set github_link = "https://github.com/monitorr/monitorr" %}
{% set deprecated = True %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

Add this in the Monitorr custom css box:

```css
@import "https://theme-park.dev/css/base/monitorr/THEME_NAME.css";
```

The `organizr-dashboard.css` theme will mess with your Monitorr base theme. And it will hide the settings button. Go to /monitorr/settings.php for settings.  
It is created purely for use with "minimum" version of the index.php `https://domain.com/monitorr/index.min.php` for Organizr homepage integration.

!!! warning "organizr-dashboard.css"
    When viewing monitorr in Organizr iframe using `organizr-dashboard.css` it will follow the Organizr theme. 
    When viewing it outside of Organizr iframe the background will be white ect. If you don't want this you can create two reverse proxies.
    One for monitorr organizr homepage integration and one for the monitorr dark/plex theme. And use subfilter on both instead of adding `@import "https://theme-park.dev/css/base/monitorr/organizr-dashboard.css";` in the monitorr custom css.

Add this in the Monitorr custom css box:

```css
@import "https://theme-park.dev/css/base/monitorr/THEME_NAME.css";
```

And add this in custom HTML in Organizr:

```css
<div id="announcementRow" class="row"><h4 class="pull-left"><span>Monitorr</span></h4><hr class="hidden-xs"></div>
<div style="overflow:hidden; height:260px; width:calc(100% + 39px); -webkit-overflow-scrolling: touch; overflow-y: scroll;">
<iframe class="iframe" frameborder="0" src="https://monitorr.domain.com/index.min.php"></iframe>
</div>
```

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}