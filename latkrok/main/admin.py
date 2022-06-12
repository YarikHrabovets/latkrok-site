from django.contrib import admin
from django.forms import Textarea
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'time_create')
    readonly_fields = ('first_name', 'last_name', 'phone', 'email', 'city', 'address', 'details')
    list_filter = ('first_name', 'last_name', 'status', 'time_create')

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
    readonly_fields = ('first_name', 'last_name', 'phone', 'email', 'details')
    list_filter = ('first_name', 'last_name', 'status', 'time_create')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'phone', 'email', 'details')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )


@admin.register(Order)
class OrderAdmin(TranslationAdmin):
    list_display = ('title', 'get_html_image', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', )

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'img_1', 'img_2', 'img_3',
                       'prise_1', 'prise_2', 'prise_3', 'prise_4', 'prise_5', 'prise_6', 'prise_7', 'prise_8', 'prise_9')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )

    def get_html_image(self, obj):
        if obj.img_1:
            return mark_safe(f'<img src={obj.img_1.url} width="50">')

    get_html_image.short_description = 'Картинка'


@admin.register(SpecialOffer)
class SpecialAdmin(TranslationAdmin):
    list_display = ('title', 'get_html_image', 'status')
    search_fields = ('title', 'color_hex', 'description', 'prise', 'count')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'color_hex')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'img_1', 'img_2', 'img_3',
                       'color', 'color_hex', 'prise', 'count')
        }),
        ('Статус', {
            'fields': ('status',)
        }),
    )

    def get_html_image(self, obj):
        if obj.img_1:
            return mark_safe(f'<img src={obj.img_1.url} width="50">')

    get_html_image.short_description = 'Картинка'


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'get_html_image', 'time_create')
    search_fields = ('title', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('time_create', )

    def get_html_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src={obj.img.url} width="50">')

    get_html_image.short_description = 'Картинка'


admin.site.site_title = 'Latkrok адміністрування'
admin.site.site_header = 'Latkrok адміністрування'
