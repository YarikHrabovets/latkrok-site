from django import template
#from ..models import Order

register = template.Library()


@register.filter
def get_range(value):
    return range(1, value+1)


@register.filter(name='verbose_name')
def get_verbose_name(field_name):
    return True
    # return Order._meta.get_field(field_name).verbose_name
