{% set github_link = "https://github.com/go-gitea/gitea" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! info
    Tested on `Version: 1.21.11`

If you want to add the theme with subfilter ect, click here: [https://docs.theme-park.dev/setup/#methods](https://docs.theme-park.dev/setup/#methods)

The theme is built on top of the `Gitea` theme, so make sure that is selected in user settings if using **subfiltering**.
![select](../site_assets/gitea/select_theme.png)

#### ⚙️ Adding the themes in Gitea

Follow the directions in the [Gitea docs](https://docs.gitea.com/administration/customizing-gitea?_highlight=tmpl#customizing-the-look-of-gitea)

In the `theme-<theme>.css` files you create, add the following: `@import "https://theme-park.dev/css/base/gitea/<theme>.css";`

### example

**theme-nord.css**

```css
@import "https://theme-park.dev/css/base/gitea/nord.css";
:root {
  --is-dark-theme:true;
}
```


If it's a dark theme you are using add the following CSS to the file.

```css
:root {
  --is-dark-theme:true;
}
```

In the `..gitea/conf/app.ini` file add the following.

```ini
[ui]
THEMES = gitea,arc-green,plex,aquamarine,dark,dracula,hotline,organizr,space-gray,hotpink,onedark,overseerr,nord
DEFAULT_THEME = gitea
```

Restart Gitea and you should now be able to select a theme in `Settings`->`Account`->`Select default theme`.

Then click the `Update Theme` button.

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}