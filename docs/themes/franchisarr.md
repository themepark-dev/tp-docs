{% set github_link = "https://github.com/prophetizer/franchisarr" %}

{% include-markdown "../themes/title.md" %}

Franchisarr reads theme.park's variables natively, so the simplest install is its own
environment variable — no Docker mod or proxy injection needed:

```yaml
environment:
  TP_THEME: nord
  # TP_DOMAIN: theme-park.dev     # or your self-hosted copy
```

{% include-markdown "../themes/installation.md" %}

{% include-markdown "../themes/screenshots.md" %}
