## Customization

The customization is done in the `source/config.py` file.

 ```{admonition} Practical Example
 :class: tip

The `source/config.py` file used to build this web-content can be found
[here](https://github.com/t4d-gmbh/web-course-template/blob/public/source/conf.py).

```

{% if slide %}
The following settings need to be adapted:
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 1

./repo_info
./logo
./course_info
```
{% else %}
<!-- BUILDING THE PAGES -->
```{include} ./repo_info.md
```
```{include} ./logo.md
```
```{include} ./course_info.md
```
{% endif %}
