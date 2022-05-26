from django.contrib import admin
from django.forms import Textarea
from .models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'time_create')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'phone', 'email', 'city', 'address',
                       'details')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'style': 'font-size: 17px;',
        })}
    }


@admin.register(LogoOrd)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'time_create')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'style': 'font-size: 17px;',
        })}
    }


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('first_name', 'description')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'img_1', 'img_2', 'img_3',
                       'prise_1', 'prise_2', 'prise_3', 'prise_4', 'prise_5', 'prise_6', 'prise_7', 'prise_8', 'prise_9')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )


@admin.register(SpecialOffer)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('first_name', 'description')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'img_1', 'img_2', 'img_3',
                       'color', 'color_hex', 'prise', 'count')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )


admin.site.register(FillUrl)
