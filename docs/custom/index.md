# Custom Themes

To create your own theme options you only need the change the color variables. You dont need the edit the `<app>-base.css`. You can find the theme variables here [https://github.com/GilbN/theme.park/tree/master/css/theme-options](https://github.com/GilbN/theme.park/tree/master/css/theme-options)

You can either fork the repo and setup a [Github pages](https://pages.github.com/) site or clone it to your web server and serve the files that way.

You can't use the raw link from Github as Github doesn't pass the mime types. That's why all my theme urls use the https://theme-park.dev site.

***

## Example

Open the theme css file you  want to change and look at the variables available.
Copy them to a new file. Remember to also include the `@import` line.

!!! info
    If you have forked the repo and want to stay up to date with any changes I make, use the `https://theme-park.dev` URL and not your own!

Add the theme to your service and load the page.
If you press `F12` and go to the `Elements` tab and scroll down you should see the variables in the root pseudo-class.
Try and disable one of them and you'll see what each variable does.

![custom](/site_assets/custom_themes.png)

The `--main-bg-color` will "always" be the  background color.
And the `--modal-bg-color` will "always" be the background for the popup modals.

!!! info
    If you click on the color a color picker will pop up and you can change the color live.

If you add a gradient from one of the links below, remember to not overwrite the `center center/cover no-repeat fixed` in the variables. Doing so might make the colors look a little wierd on small objects like drop down menus.

![custom](/site_assets/custom_themes.gif)

When you're done add the theme like you normally would.
[theme.park Setup](/setup)

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
