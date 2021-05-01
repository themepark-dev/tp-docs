# Retro Terminal

Animated custom css for the Unraid login page.
<a href="screenshots/green.png" rel="noopener"><img src="screenshots/green.png" alt="Screen Shot 1" width="100%" /></a>
<p align="center">
<a href="screenshots/red.png" rel="noopener"><img src="screenshots/red.png" alt="Screen Shot 1" width="49.15%" /></a>
<a href="screenshots/blue.png" rel="noopener"><img src="screenshots/blue.png" alt="Screen Shot 2" width="49.15%" /></a>
<a href="screenshots/white.png" rel="noopener"><img src="screenshots/white.png" alt="Screen Shot 3" width="49.15%" /></a>
<a href="screenshots/amber.png" rel="noopener"><img src="screenshots/amber.png" alt="Screen Shot 4" width="49.15%" /></a>
</p>

## 🛠️ Installation

!!! warning
    Looks best on a Chromium browser. Firefox does some wierd rendering on the animated cursor.

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

The default values are the ones below

```bash
TYPE="retro-terminal"
THEME="green.css"
DOMAIN="gilbn.github.io"
ADD_JS="true"
JS="custom_text_header.js"
DISABLE_THEME="false"
```

## Available theme colors

See [screenshots](#screenshots) at the bottom.

```css
amber.css
red.css
green.css
blue.css
white.css
custom.css
```

Set the values to what you like, and click `Save Changes`

To have the script applied at every boot, set the schedule to `At Startup of Array`

Now just click `Run Script` and it will print some text in the window.

![log](../assets/log.png)

Thats it.. logout and have a look at your new theme :)

## Javascript

You can also  inject an animated `<pre>` tag with javascript for that ultimate alien feel 👽
 It’s inspired by a blog post by [Stephen Brennan](https://brennan.io/2017/06/14/alien-computer-card/). If you want something else, there are a ton of ACSII generators out there.

Set `ADD_JS`to `"true"` to enable or `"false"` to omit the javascript.

⚠️⚠️⚠️

***HEY! You are injecting javascript into the login page for your precious server!***

***You should probably have a look at the content of that file, and probably host it yourself 💀***

[custom_text_header.js](https://github.com/gilbN/theme.park/blob/master/CSS/addons/unraid/login-page/retro-terminal/js/custom_text_header.js)

⚠️⚠️⚠️

![nostromo](../assets/nostromo.gif)

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

### 🤬 I hate the flickering!! 🤬

To remove the background flickering you need to edit the css file. Now since you don't have any control over those files, you'll need to fork it and setup Github pages or selfhost them. You can't use the raw link from Github, as they don't pass the mime types.

The background flickering can be disabled by setting the `--body-animation` root variable to `none`

The `<pre>` tag flicker can be disabled by setting `--custom-text-header-animation` to `none`.

### 🤬 I hate the CRT lines!! 🤬

Set the `--body-before` and `--body-after` root variables to `none`

### 🤬 I want my own logo!! 🤬

Fork it and change the `--logo` variable or if you're using stylus ect, just add a new `--logo` root variable below the import line.

```css
@import url(https://theme-park.dev/CSS/addons/unraid/login-page/retro-terminal/red.css);
:root {
--logo: url(https://domain.com/your-snowflake-logo-here.png) center no-repeat;
}
```

#### Available CSS variables

```css
:root {
--main-bg-color:black;
--body-before:#00ff771a;
--body-after: #00ff7733;
--body-animation: flicker;
--logo: url(https://theme-park.dev/CSS/addons/unraid/login-page/alien/logo/wings_green.png) center no-repeat;
--text-color: #37f592;
--input-color: #37f592;
--link-color: #37f592;
--link-color-hover: #68ffff;
--case-color: #37f592;
--button-text-color: #37f592;
--button-text-color-hover: #000;
--button-color: #37f592;
--button-color-hover: #68ffff;
--selection-color: #68ffff;
--custom-text-header:#37f592;
--custom-text-header-shadow:#37f592;
--custom-text-header-animation: textflicker;
--input-font: 'Share Tech Mono', monospace;
--text-font: 'Share Tech Mono', monospace;
--loginbox-background-color: transparent;
--text-shadow: 0 0 8px;
--text-shadow-color: #37f592;
--box-shadow: 0 0 15px;
}
```

***

The themes can also be added using the Stylus plugin or subfiltering with a webserver.

Link to wiki: [Setup](/setup)

#### Screenshots

<p align="center">
    <a href="../retro-terminal/screenshots/green.png" rel="noopener"><img src="../retro-terminal/screenshots/green.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../retro-terminal/screenshots/red.png" rel="noopener"><img src="../retro-terminal/screenshots/red.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../retro-terminal/screenshots/amber.png" rel="noopener"><img src="../retro-terminal/screenshots/amber.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../retro-terminal/screenshots/blue.png" rel="noopener"><img src="../retro-terminal/screenshots/blue.png" alt="Screen Shot 1" width="49.15%" /></a>
    <a href="../retro-terminal/screenshots/white.png" rel="noopener"><img src="../retro-terminal/screenshots/white.png" alt="Screen Shot 1" width="49.15%" /></a>
</p>
