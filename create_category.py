print("""
""")

category_content = \
f"""---
layout: tag
category: "{{categoryy}}"
title: "{{titlee}}"
---

<h1>Posts with "{{{{page.category}}}}" category</h1>
    
<ul>
{{% for post in site.posts %}}
{{% if post.categories contains page.category %}}

<li class="post">
    <a href="{{{{ post.url }}}} post.title }}}}a>
    <br>
    {{% if post.description %}}
    {{{{ post.description }}}}
    {{% else %}}
    {{{{ post.excerpt }}}}
    {{% endif %}}

    <p>Author: {{{{post.author}}}}</p>
    <p>Categories: {{% for category in post.categories %}} <a class="tag" href="/category/{{{{category}}}}">{{{{ category }}}}</a> {{% endfor %}}</p>
    <p>Tags: {{% for tag in post.tags %}} <a class="tag" href="/tag/{{{{tag}}}}">{{{{ tag }}}}</a> {{% endfor %}}</p>
    <p>Date: {{{{post.date | date: "%-d %B %Y"}}}}</p>
    <p>Reading time: {{{{post.reading_time}}}}</p>
</li>

{{% endif %}}
{{% endfor %}}
</ul>
---
"""

tag_content = \
f"""---
layout: tag
tag: "{{tagg}}"
title: "{{titlee}}"
---

<h1>Posts with "{{page.tag}}" tag</h1>
    
<ul>
{{% for post in site.posts %}}
{{% if post.tags contains page.tag %}}

<li class="post">
    <a href="{{{{ post.url }}}}">{{{{ post.title }}}}</a>
    <br>
    {{% if post.description %}}
    {{ post.description }}
    {{% else %}}
    {{ post.excerpt }}
    {{% endif %}}

    <p>Author: {{{{post.author{{{{</p>
    <p>Categories: {{% for category in post.categories %}} <a class="tag" href="/category/{{{{category}}}}">{{{{ category }}}}</a> {{% endfor %}}</p>
    <p>Tags: {{% for tag in post.tags %}} <a class="tag" href="/tag/{{{{tag}}}}">{{{{ tag }}}}</a> {{% endfor %}}</p>
    <p>Date: {{{{post.date | date: "%-d %B %Y"}}}}</p>
    <p>Reading time: {{{{post.reading_time}}}}</p>
</li>

{{% endif %}}
{{% endfor %}}
</ul>
"""

file_type = int(input("Category(1) or Tag(2):\nelliot@fsociety~# "))
c_t = input("\nTag (str):\nelliot@fsociety~# " if file_type == 2 else "\nCategory (str):\nelliot@fsociety~# ")
title = input("\nTag title (str):\nelliot@fsociety~# " if file_type == 2 else "\nCategory title (str):\nelliot@fsociety~# ")

print("\nCreating...")

if file_type == 1:
    fd = open(f"category/{c_t}.md","w")
    category_content = category_content.replace("{{categoryy}}",c_t).replace("{{titlee}}",title)

    fd.write(category_content)
    fd.close()
else:
    fd = open(f"tag/{c_t}.md","w")
    tag_content = tag_content.replace("{{tagg}}",c_t).replace("{{titlee}}",title)

    fd.write(tag_content)
    fd.close()

print(f"Done!\nFile created at: {'category/' if file_type == 1 else 'tag/'}{c_t}.md")