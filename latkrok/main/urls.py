from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('order/', LatkrokOrder.as_view(), name='order'),
    path('order-products/<slug:order_slug>/', LatkrokOrderProduct.as_view(), name='order_product'),
    path('logo/', logo, name='logo'),
    path('special/', LatkrokSpecial.as_view(), name='special'),
    path('special-products/<slug:special_slug>/', LatkrokSpecialProduct.as_view(), name='special_product'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('maker/', maker, name='maker'),
]