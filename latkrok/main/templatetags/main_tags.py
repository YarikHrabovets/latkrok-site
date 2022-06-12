from django import template
from main.models import *
import datetime

register = template.Library()


@register.simple_tag(name='current_year')
def get_current_year():
    return datetime.datetime.now().year


@register.filter(name='name')
def get_verbose_name_from_field(field_name):
    return Order._meta.get_field(field_name).verbose_name


@register.simple_tag(name='value')
def get_value_from_field(obj, field_name):
    return getattr(obj, field_name)
