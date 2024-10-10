# How-To

{% if build == "slides" %}
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 2
:caption: How-To

./structure
./combining
./page_content
./page_index
./page_example
./page_import
./conditional_content
```
{% else %}
<!-- BUILDING THE PAGES -->
```{include} ./structure.md
```
```{include} ./combining.md
```
To do so we can follow this approach:

```{include} ./page_content.md
```
```{include} ./page_index.md
```
And here is how a full `📂mypage/📄index.md` could look like: 
```{include} ./page_example.md
```
Finally, we still need to include the page:
```{include} ./page_import.md
```
```{include} ./conditional_content.md
```
{% endif %}

