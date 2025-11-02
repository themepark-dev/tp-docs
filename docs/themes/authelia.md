{% set github_link = "https://github.com/authelia/authelia" %}

{% include-markdown "../themes/title.md" %}

{% include-markdown "../themes/installation.md" %}

!!! warning "Subfilter CSP"
    As Authelia will block the theme with its content security policy, you need to modify or remove the default CSP header.
    Removing the CSP header can leave your Authelia instance open to attacks such as clickjacking or cross-site scripting (XSS). This is especially dangerous if your Authelia instance is publically accessible. As Authelia already supports modifying the CSP header, it is not advisable to remove it.

### Custom CSP Headers in Authelia Configuration

To modify the Authelia Content Security Policy Header, change this line in the Authelia configuration.yml, and restart Authelia.

```authelia
server:
  headers:
    csp_template: "default-src 'self'; style-src 'self' 'nonce-${NONCE}' 'sha256-47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;"
```

If you are self-hosting theme-park, instead replace 'theme-park.dev raw.githubusercontent.com' with the domain of your self-hosted theme-park instance.

{% include-markdown "../themes/addons/addons.md" %}

{% include-markdown "../themes/screenshots.md" %}