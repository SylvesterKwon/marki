from distutils import extension
import markdown
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
            "linenums": "True",

        },
        "wikilinks":{
            "base_url": "/wiki/",
        },
        "toc":{
            "title": "목차",
        }
    }
    return mark_safe(markdown.markdown(value, extensions=extensions, extension_configs=extension_configs))