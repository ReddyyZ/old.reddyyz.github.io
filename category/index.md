---
layout: default
title: "Categories list"
---

<link rel="stylesheet" href="{{ '/assets/css/y.css' }}">

# Search by categories: 

<div class="list">
    {% for category in site.categorias %}
        <a href="/category/{{category}}">{{category}}</a>
    {% endfor %}
</div>