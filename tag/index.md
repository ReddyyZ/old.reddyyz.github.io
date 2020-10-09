---
layout: default
title: "Tags list"
---

<link rel="stylesheet" href="{{ '/assets/css/y.css' }}">

# Search by tags: 

<div class="list">
    {% for tag in site.tags_ %}
        <a href="/tag/{{tag}}">{{tag}}</a>
    {% endfor %}
</div>