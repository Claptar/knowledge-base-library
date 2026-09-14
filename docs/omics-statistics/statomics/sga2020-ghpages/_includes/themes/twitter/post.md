---
title: Post
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/_includes/themes/twitter/post.html
source_file: sources/statomics-sga2020-ghpages/_includes/themes/twitter/post.html
licence: CC0-1.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Post

**Source:** [`_includes/themes/twitter/post.html`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/_includes/themes/twitter/post.html) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.html` (good)

# {{ page.title }} {% if page.tagline %}<span class="small">{{page.tagline}}</span>{% endif %} {#page.title-if-page.tagline-page.tagline-endif}

{{ page.date \| date\_to\_long\_string }}

{{ content }}

{% unless page.categories == empty %}

-
  {% assign categories\_list = page.categories %} {% include JB/categories\_list %}

{% endunless %} {% unless page.tags == empty %}

-
  {% assign tags\_list = page.tags %} {% include JB/tags\_list %}

{% endunless %}

------------------------------------------------------------------------

- {% if page.previous %}
- [← Previous](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/_includes/themes/twitter/%7B%7B%20BASE_PATH%20%7D%7D%7B%7B%20page.previous.url%20%7D%7D "{{ page.previous.title }}")
  {% else %}
- ← Previous
  {% endif %}
- [Archive](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/_includes/themes/twitter/%7B%7B%20BASE_PATH%20%7D%7D%7B%7B%20site.JB.archive_path%20%7D%7D)
  {% if page.next %}
- [Next →](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/_includes/themes/twitter/%7B%7B%20BASE_PATH%20%7D%7D%7B%7B%20page.next.url%20%7D%7D "{{ page.next.title }}")
  {% else %}
- Next → {% endif %}

------------------------------------------------------------------------

{% include JB/comments %}

---

[Up: contents](../../../index.md)
