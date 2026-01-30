> ℹ️ You are {% if slide %}viewing the 📊 presentation for{% else %}reading the 📚 documentation of{% endif %} the

```{include} ../README.md
:end-before: <!-- include-upper -->
```
```{toctree}
:caption: Course Template Docs
{% if slide %}
:hidden:
{% else %}
:maxdepth: 2
{% endif %}

content/howto/index
content/examples/index
```
