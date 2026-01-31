# How-To

To make this web course template your own all you have to do is to
{% if slide %}- {% endif %}**customize** the looks
{% if slide %}- {% else %}and to {% endif %}add your own **content**.
{% if slide %}- {% endif %}
{% if page %}
To make this web course template your own all you have to do is to customize the
looks and to add your own **content**.
{% else %}
All you have to do is:

- **customize** the looks
- add your own **content**.
{% endif %}

{% if build == "slides" %}
<!-- BUILDING THE SLIDES -->
```{toctree}
:hidden:

./customization
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

