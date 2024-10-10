> ℹ️ You are {% if slide %}viewing the 📊 presentation for{% else %}reading the 📚 documentation of{% endif %} the

```{include} ../README.md
:end-before: <!-- include-upper -->
```
```{toctree}
:maxdepth: 2
:caption: Course Template Docs
{% if build == "slides" %}:numbered:{% endif %}

content/index
```
