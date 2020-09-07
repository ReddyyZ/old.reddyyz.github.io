---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<link rel="stylesheet" href="{{ '/assets/css/home.css?v=' }}">

<h1>Posts</h1>

<ul>
    {% for post in site.posts %}
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
        </li>
    {% endfor %}
</ul>