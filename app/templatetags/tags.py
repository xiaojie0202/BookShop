from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def filter_handel(filter_data, t):
    ss = ''
    for k, v in filter_data.items():
        if k != t:
            ss += '&%s=%s' % (k, v)
    return ss

@register.simple_tag
def chengfa(*args):
    b = 1

    for a in args:
        b = b * a
    print(args)
    return b
