from django import template
from main.models import *

register = template.Library()


@register.filter(name='name')
def get_verbose_name_from_field(field_name):
    return Order._meta.get_field(field_name).verbose_name


@register.simple_tag(name='value')
def get_value_from_field(field_name, slug):
    return getattr(Order.objects.get(slug=slug), field_name)
