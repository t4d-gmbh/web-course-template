# Examples

Here you can find some projects that use this template:

{% if build == "slides" %}
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 2

./working-with-git
```
{% else %}
<!-- BUILDING THE PAGES -->
```{include} ./working-with-git.md
```
{% endif %}

