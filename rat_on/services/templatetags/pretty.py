"""Custom Django template filters."""

from django import template


register = template.Library()

@register.filter
def pretty(value: str) -> str:
    return value.replace('_', ' ').title()
