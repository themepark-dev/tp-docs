{% set github_link = "https://github.com/go-gitea/gitea" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! info
    Tested on `Version: 1.15.4`

If you want to add the theme with subfilter ect, click here: [https://docs.theme-park.dev/setup/#methods](https://docs.theme-park.dev/setup/#methods)

The theme is built on top of the `Gitea` theme, so make sure that is selected in user settings if using **subfiltering**.
![select](../site_assets/gitea/select_theme.png)

#### ⚙️ Adding the themes in Gitea

Create a new file called `body_outer_pre.tmpl` and place it in `gitea/templates/custom/body_outer_pre.tmpl`. Create the template and custom folders if they do not exists.

In the `body_outer_pre.tmpl` file add the following:

```html
{{'{{ if .IsSigned }}'}}
  {{'{{ if and (ne .SignedUser.Theme "gitea") (ne .SignedUser.Theme "arc-green") }}'}}
    <link rel="stylesheet" href="https://theme-park.dev/css/base/gitea/{{'{{.SignedUser.Theme}}'}}.css">
  {{'{{end}}'}}
{{'{{ else if and (ne DefaultTheme "gitea") (ne DefaultTheme "arc-green") }}'}}
  <link rel="stylesheet" href="https://theme-park.dev/css/base/gitea/{{'{{DefaultTheme}}'}}.css">
{{'{{end}}'}}
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