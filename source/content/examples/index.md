# Examples

Here you can find some projects that use this template:

{% if build == "slides" %}
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 2
:caption: Examples

./working-with-git
./combining
./conditional_content
```
{% else %}
<!-- BUILDING THE PAGES -->
```{include} ./working-with-git.md
```
{% endif %}

