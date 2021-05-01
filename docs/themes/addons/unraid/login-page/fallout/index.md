# Fallout

Custom Fallout themed css for the Unraid login page.

<p align="center">
<a href="screenshots/dirty_terminal.png" rel="noopener"><img src="screenshots/dirty_terminal.png" alt="Screen Shot 1" width="49.15%" /></a>

<a href="screenshots/terminal.png" rel="noopener"><img src="screenshots/terminal.png" alt="Screen Shot 3" width="49.15%" /></a>

<a href="screenshots/dirty_terminal2.png" rel="noopener"><img src="screenshots/dirty_terminal2.png" alt="Screen Shot 2" width="49.15%" /></a>


<a href="screenshots/terminal2.png" rel="noopener"><img src="screenshots/terminal2.png" alt="Screen Shot 4" width="49.15%" /></a>
</p>

## 🛠️ Installation

**Recommended way:**

Install using the [bash script](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/custom_login.sh) and the plugin [CA User Scripts](https://forums.unraid.net/topic/48286-plugin-ca-user-scripts/)

Add a new user script by clicking `Add new script`

![addnew](../assets/addnew.png)

Give it a name and click OK

![addnewname](../assets/addnewname.png)

Click or hover over the gear icon and click `Edit Script`

![edit](../assets/edit.png)

Paste the contents of the bash script: [custom_login.sh](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/custom_login.sh)

Below the shebang(`#!/bin/bash`) are the variables you need to change for the different themes.

![shebang](../assets/shebang.png)

The values are the ones below. For the Fallout themes, remember to change the `TYPE` variable to `fallout`. The default value in the bash script is `retro-terminal`

Remember to also set `ADD_JS` to `false` if you are not using the `fallout_video.css` theme.

```bash
TYPE="fallout"
THEME="dirty_terminal2.css"
DOMAIN="gilbn.github.io"
ADD_JS="false"
JS="please_stand_by.js"
DISABLE_THEME="false"
```

### Available theme colors

See [screenshots](#screenshots) at the bottom.

Available wallpapers [Wallpapers](https://github.com/gilbN/theme.park/tree/master/CSS/addons/unraid/login-page/fallout/wallpaper)

```css
terminal.css
terminal2.css
dirty_terminal.css
dirty_terminal2.css
fallout_video.css
custom.css /* Make it your own */
```

Set the values to what you like, and click `Save Changes`

To have the script applied at every boot, set the schedule to `At Startup of Array`

Now just click `Run Script` and it will print some text in the window.

![log](../assets/log.png)

Thats it.. logout and have a look at your new theme :)

### Javascript

You can also  inject an animated video wallpaper.

1. Set `THEME` to `fallout_video.css`
2. Set `ADD_JS` to `"true"` to enable.
3. Choose the video you want. See: [videos](https://github.com/gilbN/theme.park/tree/master/CSS/addons/unraid/login-page/fallout/video)
    * Available js: `please_stand_by.js`, `vault-tec-crt.js`, `vault-tec-crt_no-scanline.js`
4. Set `JS` to the one you want.

⚠️⚠️⚠️

***HEY! You are injecting javascript into the login page for your precious server!***

***You should probably have a look at the content of that file, and probably host it yourself 💀***

[please_stand_by.js](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/fallout/js/please_stand_by.js)

[vault-tec-crt.js](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/fallout/js/vault-tec-crt.js)

[vault-tec-crt_no-scanline.js](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/fallout/js/vault-tec-crt_no-scanline.js)

⚠️⚠️⚠️

![fallout](../assets/fallout.gif)

## FAQ

### Backups

The script will create a backup of the login.php file if one does not exist.

### Uninstall/Restore the original

To uninstall the theme set the variable `DISABLE_THEME` to `"true"`

### Can I selfhost this?

Of course!  Just clone the repo into your webserver. Remember to change the `DOMAIN` variable in the bash script.

### My server is not connected to the internet! How can I add this?

With the current version of the bash script, that is not possible as it injects the stylesheet using the a URL and not a file path.
However, nothing is stopping you from just doing some small changes to the script and replace the `href` urls to the path you stored the files.
I will try and create a version of the script that is made for local hosting in the future.

### 🤬 I don't like XYZ !! 🤬

To change the colors,background, logo ect you need to edit the css file. Now since you don't have any control over those files, you'll need to fork it and setup Github pages or selfhost the files. You can't use the raw link from Github, as they don't pass the mime types.

If you use stylus you can just replace a variable you want to change.

```css
@import url(https://theme-park.dev/CSS/addons/unraid/login-page/fallout/terminal.css);
:root {
--logo: url(https://domain.com/your-snowflake-logo-here.png) center no-repeat;
}
```

#### Available CSS variables

```css
:root {
    --main-bg-color: url(https://theme-park.dev/CSS/addons/unraid/login-page/fallout/wallpaper/rocky-wall.png),
    url(https://theme-park.dev/CSS/addons/unraid/login-page/fallout/wallpaper/terminal.png) center center/cover no-repeat fixed;
    --logo: url(https://theme-park.dev/CSS/addons/unraid/login-page/fallout/logo/vault-tec_green.png) center no-repeat;
    --text-color: #14F074;
    --input-color: #14F074;
    --link-color: #14F074;
    --link-color-hover: #0C833D;
    --case-color: #14F074;
    --button-text-color: #14F074;
    --button-text-color-hover: #FFFFFF;
    --button-color: #14F074;
    --button-color2: #0C833D;
    --input-font: 'Share Tech Mono', monospace;
    --text-font: 'Share Tech Mono', monospace;
    --div-background-color-15: rgba(0, 0, 0, 0.25);
}
```

***

The themes can also be added using the Stylus plugin or subfiltering with a webserver.

Link to wiki: [Setup](/setup)

#### Screenshots

<p align="center">
    <a href="../fallout/screenshots/dirty_terminal.png" rel="noopener"><img src="../fallout/screenshots/dirty_terminal.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../fallout/screenshots/dirty_terminal2.png" rel="noopener"><img src="../fallout/screenshots/dirty_terminal2.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../fallout/screenshots/terminal.png" rel="noopener"><img src="../fallout/screenshots/terminal.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../fallout/screenshots/terminal2.png" rel="noopener"><img src="../fallout/screenshots/terminal2.png" alt="Screen Shot 1" width="49.15%" /></a>
</p>
