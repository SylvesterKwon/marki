from distutils import extension
import markdown
import bleach
#from bleach_whitelist import markdown_tags, markdown_attrs
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["fenced_code", "codehilite", "wikilinks", "toc"]
    extension_configs = {
        "codehilite":{
            "use_pygments": "True",
        },
        "wikilinks":{
            "base_url": "/wiki/",
        },
        "toc":{
            "title": "목차",
        }
    }
    return mark_safe(bleach.clean(markdown.markdown(value, extensions=extensions, extension_configs=extension_configs),
    tags=['p', 'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul'],
    attributes={'a': ['href', 'title'], 'abbr': ['title'], 'acronym': ['title']}))