---
layout: tag
tag: "linux"
title: "Linux tag"
---

<h1>Posts with "{{page.tag}}" tag</h1>
    
<ul>
{% for post in site.posts %}
{% if post.tags contains page.tag %}

<li class="post">
    <a href="{{ post.url }}">{{ post.title }}</a>
    <br>
    {% if post.description %}
    {{ post.description }}
    {% else %}
    {{ post.excerpt }}
    {% endif %}

    <p>Author: {{post.author}}</p>
    <p>Categories: {% for category in post.categories %} <a class="tag" href="/category/{{category}}">{{ category }}</a> {% endfor %}</p>
    <p>Tags: {% for tag in post.tags %} <a class="tag" href="/tag/{{tag}}">{{ tag }}</a> {% endfor %}</p>
    <p>Date: {{post.date | date: "%-d %B %Y"}}</p>
    <p>Reading time: {{post.reading_time}}</p>
</li>

{% endif %}
{% endfor %}
</ul>