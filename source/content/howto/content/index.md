## Content

The actual content shown in the web-course must be written in Markdown and
reside under `source/content`.

A notable exception to this setup is the "landing page" of the web-course that
is defined in `source/index.md`.

This file 

{% if slide %}
The following settings need to be adapted:
<!-- BUILDING THE SLIDES -->
```{toctree}
:maxdepth: 1

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
