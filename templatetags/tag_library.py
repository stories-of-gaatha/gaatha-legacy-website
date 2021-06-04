from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)


@register.filter(name='lookup')
def lookup(dictionary, key):
    """
    Retrives value from dict
    """
    return dictionary.get(key, "")
