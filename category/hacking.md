---
layout: tag
category: "hacking"
---

<h1>Posts with "{{page.category}}" category</h1>
    
<ul>
{% for post in site.posts %}
{% if post.tags contains page.category %}

<li class="post">
    <a href="{{ post.url }}">{{ post.title }}</a>
    <br>
    {% if post.description %}
    {{ post.description }}
    {% else %}
    {{ post.excerpt }}
    {% endif %}

    <p>Author: {{post.author}}</p>
    <p>Categories: {{post.categories | join: " - "}}</p>
    <p>Tags: {{post.tags | join: " - "}}</p>
    <p>Date: {{post.date | date: "%-d %B %Y"}}</p>
</li>

{% endif %}
{% endfor %}
</ul>