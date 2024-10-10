{% if slide %}### A page `📄index.md` example


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

:::{card} `📂mypage/📄index.md`
    # myPage
    {% raw %}
    {% if slide %}
    <!-- BUILDING THE SLIDES -->
    ```{toctree}
    :maxdepth: 2
    ./slide1
    ...
    ```
    {% else %}
    <!-- BUILDING THE PAGES -->
    ```{include} ./slide1.md
    ```
    ...
    {% endif %}
    {% endraw %}
:::
