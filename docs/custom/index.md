# Custom Themes

To create your own theme options you only need the change the color variables. You dont need the edit the `<app>-base.css`. You can find the theme variables here [https://github.com/themepark-dev/theme.park/tree/master/css/theme-options](https://github.com/themepark-dev/theme.park/tree/master/css/theme-options)

You can either fork the repo and setup a [Github pages](https://pages.github.com/) site or clone it to your web server and serve the files that way.

You can't use the raw link from Github as Github doesn't pass the mime types. That's why all my theme urls use the https://theme-park.dev site.

## Docker

See [docker](../setup#docker) for more information on selfhosting a docker image

***

## Custom Github Setup

1. Start with forking the the repo to the account you want.

2. Next head over to your theme.park fork and change the domain in the  [CNAME](https://github.com/themepark-dev/theme.park/blob/master/CNAME) file to a custom domain if you have one or `<user>.github.io` ie `gilbn.github.io`

    1. Click on `Settings`, then select `Pages` on the left side menu.
        Set your Source as `Deploy from a branch` and select the `live` branch.

        ![](build.png)

    2. If you don't have a branch named `live` in your drop down, head over to the `Actions` tab, select `Minify CSS and deploy to live branch` and click on `Run workflow` select `master` and click run.

        ![](minifyanddeploy.png)

        !!! Warning
            Make sure the workflow has read and write write permissions to the repo. Go to: Repo -> Settings -> Actions -> General, scroll down to `Workflow permissions`and check `Read and write permissions` then hit `Save`

        This [workflow](https://github.com/themepark-dev/theme.park/blob/master/.github/workflows/minify-and-deploy.yml) will in short:

        1. Run the [themes.py](https://github.com/themepark-dev/theme.park/blob/master/themes.py) script.

        2. [Minify](https://developer.mozilla.org/en-US/docs/Glossary/minification) the css files.

        3. Deploy the all the files it creates (> 1500 files) to the `live` branch.

        !!! Note
            If you add a custom domain, you access the files with `custom.com/css/base...` if you use the default `github.io` domain you will need to append `theme.park` or whatever you named the repo when you forked it. ie `gilbn.github.io/theme.park/css/...`

            You can read more about how to add a custom domain here: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

    3. The execution of the themes.py script is important as it creates all the theme files in all the base folders -> https://github.com/themepark-dev/theme.park/tree/live/css/base/. These files contains css `@imports` to both the base.css file and the theme-option.css file. By doing this you can easily use the files by using `user.github.io/theme.park/css/base/<app>/<theme-option>` ie https://gilbn.github.io/theme.park/css/base/radarr/plex.css. If you compare the `master` and `live` branch you can see master only contains the base css file.

3. After the deploy action is finished, you should be able to access https://username.github.io/theme.park/css/base/radarr/nord.css.

4. If you want to add a custom theme option, copy one of the files in `/css/theme-options/` and start editing the color variables. Commit and push new file and the themes.py script will create a `your-custom.css` file in all the `/css/base/<app>` folders. 

    !!! Warning
        If you see variables that look like this: `--some-var: 123, 123, 123` don't change this syntax. If you do you will break how the base css files uses that variable.

## Custom theme option example

Open the theme css file you  want to change and look at the variables available.
Copy them to a new file.

Add the theme to your service and load the page.
If you press `F12` and go to the `Elements` tab and scroll down you should see the variables in the root pseudo-class.
Try and disable one of them and you'll see what each variable does.

![custom](../site_assets/custom_themes.png)

!!! note "Tip"
    If you want to have persistent changes while testing out color options, you can use the [stylus](../setup/#stylus-method) plugin for testing.
    Just add the content from the theme-option file and start changing stuff.

The `--main-bg-color` will "always" be the  background color.
And the `--modal-bg-color` will "always" be the background for the popup modals.

!!! info
    If you click on the color a color picker will pop up and you can change the color live.

If you add a gradient from one of the links below, remember to not overwrite the `center center/cover no-repeat fixed` in the variables. Doing so might make the colors look a little wierd on small objects like drop down menus.

![custom](../site_assets/custom_themes.gif)

When you're done add the theme like you normally would.
[theme.park Setup](../setup)

***

## Resources

The links below are some great resources on finding cool gradients.

If you find a particular colored theme you feel should be added to the repo let me know on discord!

<a href="https://discord.gg/HM5uUKU" rel="noopener"><img class="alignnone" title="theme.park!" src="https://img.shields.io/badge/chat-Discord-blue.svg?style=for-the-badge&logo=discord" alt="" height="37" /></a>

[https://cssgradient.io/](https://cssgradient.io/)

[https://uigradients.com/](https://uigradients.com/)

[https://mycolor.space/gradient](https://mycolor.space/gradient)

[https://www.css-gradient.com/](https://www.css-gradient.com/)

[https://gradienthunt.com/](https://gradienthunt.com/)

[https://www.gradientmagic.com](https://www.gradientmagic.com)
