{% set github_link = "https://unraid.net" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

#### Theme Engine

1. Install the [Theme Engine](https://forums.unraid.net/topic/87126-plugin-theme-engine-a-webgui-styler/) plugin from the CA appstore and open it.
2. Set `Base Theme` to black
3. Enable `Advanced View`
4. Set `Enable Theme Engine:` to `No`
5. Scroll down and set `Enable custom styling (below):` to `Yes`
6. Add the HTML below in the `Custom styling (advanced):` textarea. Remember to change `<THEME>` to the theme you want.

7. **Optional:** Go to `Settings` -> `Display Settings` and set `Header custom text color:` to `FFF` and `Header custom background color:` to `000`

```html
</style>
<link type="text/css" rel="Stylesheet" href="https://theme-park.dev/css/base/unraid/<THEME>.css" />
```

#### Local Theme-Park CSS

This documentation provides instructions on how to use the Theme-Park Theme CSS Synchronization script to synchronize the CSS files needed for the theme-park.dev Unraid theme. The script ensures that the CSS files are correctly placed in the Dynamix CSS styles folder and updates references in the CSS files so they can be loaded locally in the Unraid GUI.

##### Installation

1. Download the script file from the [GitHub repository](https://github.com/themepark-dev/theme.park/tree/master/css/addons/unraid/local.sh).
2. Save the script file to a location on your Unraid server.

##### Usage

1. Open the downloaded script file in a text editor.
2. Locate the `root_source_folder` variable and change it to point to your desired source directory for the CSS files.
3. Save the changes to the script file.

##### Running the Script

###### Using User Scripts Plugin

1. If not already installed, install the `User Scripts` plugin from the Unraid Community Applications.
2. Open the "User Scripts" plugin and create a new script.
3. Give the script a name (e.g., "Theme-Park CSS Sync").
4. In the script content section, paste the script code and update the variable for your specific system.
5. Save the script and configure it to run on array start or as needed.

###### Manually Running the Script

1. Open a terminal or SSH session to your Unraid server.
2. Navigate to the location where you saved the script file.
3. Make the script file executable with the command: `chmod +x local.sh`
4. Update the script for your specific file system.
5. Run the script with the command: `./local.sh`
6. The script will perform the synchronization and update references.

##### Using the Theme Engine Plugin

After running the script to synchronize the CSS files, you can use the `Theme Engine` plugin to customize the styling of your Unraid web interface. Here's an example of how you can include the copied CSS files in your HTML head using the `Theme Engine` plugin:

```html
<!-- Example for Theme Engine plugin -->
<style>
  <link type="text/css" rel="stylesheet" href="/webGui/styles/theme-park/css/base/unraid/nord.css" />
</style>
```

Simply add this code snippet within the HTML `<head>` section of your web interface to apply the custom styling.

For more information about using the `Theme Engine` plugin, refer to the plugin's documentation.

---

**Note:** Always make sure to back up your files and configurations before making any changes to your Unraid setup.

For the latest updates and more information, you can visit the [GitHub repository](https://github.com/themepark-dev/theme.park/tree/master/css/addons/unraid/local.sh).

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}