---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

<link rel="stylesheet" href="{{ '/assets/css/home.css?v=' }}">

<ul>
    {% for post in site.posts %}
        <li class="post">
            <a href="{{ post.url }}">{{ post.title }}</a>
            <br>
            {{ post.excerpt }}

            <p>Author: {{post.author}}</p>
            <p>Categories: {{post.categories | join: " - "}}</p>
            <p>Tags: {{post.tags | join: " - "}}</p>
            <p>Date: {{post.date | date: "%-d %B %Y"}}</p>
        </li>
    {% endfor %}
</ul>