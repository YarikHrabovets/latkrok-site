from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SpecialOffer)
class SpecialOfferTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Article)
class SpecialOfferTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
