from django import template

register = template.Library()

@register.filter
def progress_width(value, max_value):
    if max_value == 0:
        return 0
    return (value / max_value) * 100