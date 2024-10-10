# How-To

{% if build == "slides" %}
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 2
:caption: How-To

./structure
./combining
./conditional_content
```
{% else %}
<!-- BUILDING THE PAGES -->
```{include} ./structure.md
```
```{include} ./combining.md
```
```{include} ./conditional_content.md
```
{% endif %}

