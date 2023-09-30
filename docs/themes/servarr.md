!!! warning
    If using regular subfiltering, you need to subfilter the `</body>` tag.
    See the example below. 

#### Example

```nginx
proxy_set_header Accept-Encoding "";
sub_filter
'</body>'
'<link rel="stylesheet" type="text/css" href="https://theme-park.dev/css/base/<app>/<theme>.css"></body>
sub_filter_once on;
```


