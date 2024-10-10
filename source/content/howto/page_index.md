### Creating a page `📄index.md`
{% if slide %}
 ```{admonition} Folder structure
 :class: tip, margin

 ```markdown
 📂content
 ┣ 📄index.md
 ┗ 📂 mypage
    ┣ 📄index.md
    ┣ 📄slide1.md
    ┣ 📄slide2.md
    ┣ 📄slide3.md
    ┗ 📂figures
      ┗ 📊figure1.png
```
{% endif %}

- Add the pages title (e.g. `# myPage`)
- Use the `{% raw %}{% if slide %}...{% else %}...{% endif %}{% endraw %}` to separate
  single slides and the page content
- Within the `{% raw %}{% if slide %}...{% else %}{% endraw %}` create a `toctree` and import the slides:

      ```{toctree}
      :maxdepth: 2
      ./slide1
      ...
      ```
- Include the slides in the `{% raw %}{% else %}...{% endif%}{% endraw %}`

      <!-- BUILDING THE PAGES -->
      ```{include} ./slide1.md
      ```
- Optionally add further content to the page in `{% raw %}{% else %}...{% endif%}{% endraw %}`

      <!-- BUILDING THE PAGES -->
      This is some additional text to introduce content from slide1
      ```{include} ./slide1.md
      ```
      ```{margin}
      and some site note we want to add in the page
      ```
