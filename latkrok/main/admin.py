from django.contrib import admin
from django.forms import Textarea
from .models import *

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'style': 'font-size: 17px;',
        })}
    }


@admin.register(LogoOrd)
class LogoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
            'style': 'font-size: 17px;',
        })}
    }

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('name', 'info')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SpecialOffer)
class SpecialAdmin(admin.ModelAdmin):
    search_fields = ('name', 'info')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(FillUrl)
