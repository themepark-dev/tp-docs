
# Organizr Glass

<p align="center">
    <a href="login.png" rel="noopener"><img src="login.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="lockscreen.png" rel="noopener"><img src="lockscreen.png" alt="Screen Shot 2" width="49.15%" /></a>
    <a href="homepage.png" rel="noopener"><img src="homepage.png" alt="Screen Shot 3" width="49.15%" /></a>
    <a href="settings.png" rel="noopener"><img src="settings.png" alt="Screen Shot 4" width="49.15%" /></a>
</p>

* [Full](#full)
* [Login - Lockscreen only](#login-lockscreen-only)

!!! info "Tip"
    If you're on Docker use the `php-fpm` tag to speed up load times, like so: `organizrtools/organizr-v2:php-fpm`

!!! warning "Firefox"
    From version 70: this feature is behind thelayout.css.backdrop-filter.enabled preferences (needs to be set to true) and the gfx.webrender.all preferences (needs to be set to true). To change preferences in Firefox, visit about:config

## Full

1. Set the Organizr theme to either Aquamarine, Hotline or Space Gray

2. Import the `glass-base.css` and root variables in the Custom Theme CSS box like below.
  Replace `--main-bg-color` with a wallpaper you have uploaded to Organizr

```css
@import "https://theme-park.dev/CSS/addons/organizr/glass/glass-base.css"; 
:root {
    --main-bg-color: url(https://theme-park.dev/CSS/addons/organizr/glass/example.jpg) center center/cover no-repeat fixed;
    --mobile-bg-color: radial-gradient(circle, #3a3a3a, #2d2d2d, #202020, #141414, #000000) center center/cover no-repeat fixed;

    --link-color: #fff;
    --custom-buttons-color: radial-gradient(ellipse at center, #3F51B5 0%, #009688 100%) center center/cover no-repeat fixed;
    --hompage-item-hover: radial-gradient(ellipse at center, rgba(0, 150, 136, 0.33) 0%, #b53f3f73 100%) center center/cover no-repeat fixed;
    --notification-box-line: #000;

    --div-background-color-10: rgba(0, 0, 0, 0.15);
    --div-background-color-15: rgba(0, 0, 0, 0.25);
    --div-background-color-25: rgba(0, 0, 0, 0.35);
    --div-background-color-35: rgba(0, 0, 0, 0.45);
}
```

On mobile the background is replaced with `--mobile-bg-color`. Find a background you like here [https://cssgradient.io/gradient-backgrounds/](https://cssgradient.io/gradient-backgrounds/) or just set it to a regualar color e.g. `#1f1f1f`

Here are the other theme colors if you want to use that instead:

<img src="aquamarine_banner.png" width="600px" />

```css
--mobile-bg-color: radial-gradient(ellipse at center, #47918a 0%, #0b3161 100%) center center/cover no-repeat fixed;
```

<img src="hotline_banner.png" width="600px" />

```css
 --mobile-bg-color: radial-gradient(ellipse at center, #F44336 0%, #0b3161 100%) center center/cover no-repeat fixed;
```

<img src="spacegray_banner.png" width="600px" />

```css
--mobile-bg-color: radial-gradient( ellipse at center,  rgba(87,108,117,1) 0%, rgba(37,50,55,1) 100.2% ) center center/cover no-repeat fixed;
```

<img src="dark_banner.png" width="600px" />

```css
--mobile-bg-color: radial-gradient(circle, #3a3a3a, #2d2d2d, #202020, #141414, #000000) center center/cover no-repeat fixed;
```

<img src="plex_banner.png" width="600px" />

```css
--mobile-bg-color: url("https://raw.githubusercontent.com/gilbN/theme.park/master/Resources/blur-noise.png"), url("https://raw.githubusercontent.com/gilbN/theme.park/master/Resources/preset-light2.png") center center/cover no-repeat fixed;
```

!!! note
    Replace the variables if you have a dark background

* Light blur colors for dark backgrounds.

```css
    --div-background-color-10: rgba(255, 255, 255, 0.10);
    --div-background-color-15: rgba(255, 255, 255, 0.15);
    --div-background-color-25: rgba(255, 255, 255, 0.25);
    --div-background-color-35: rgba(255, 255, 255, 0.35);
```

* Dark blur colors for bright backgrounds

```css
    --div-background-color-10: rgba(0, 0, 0, 0.15);
    --div-background-color-15: rgba(0, 0, 0, 0.25);
    --div-background-color-25: rgba(0, 0, 0, 0.35);
    --div-background-color-35: rgba(0, 0, 0, 0.45);
```

## Login - Lockscreen only

If you just want the login and lockscreen css, just add this in custom CSS:

```css
@import "https://theme-park.dev/CSS/addons/organizr/glass/glass-login.css"; 
```

You can change the blur background color by adding the variables above. The default is dark.

```css
@import "https://theme-park.dev/CSS/addons/organizr/glass/glass-login.css";
:root {
    --div-background-color-10: rgba(255, 255, 255, 0.10);
    --div-background-color-15: rgba(255, 255, 255, 0.15);
    --div-background-color-25: rgba(255, 255, 255, 0.25);
    --div-background-color-35: rgba(255, 255, 255, 0.35);
}
```
