from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Order, SpecialOffer, FillUrl
from .forms import *
from .sendScript import send_for_email


def get_search_context(is_ord=False, is_spec=False, **kwargs) -> dict:
    ord, spec = '', ''
    if not is_ord:
        ord = Order.objects.all()
    if not is_spec:
        spec = SpecialOffer.objects.all()

    context = {
        'orders': ord,
        'specials': spec,
        'static_urls': {
            'главная': reverse('index'), 'оренда': reverse('order'), 'лого': reverse('logo'),
            'спец предложения': reverse('special'), 'корзина': reverse('cart'), 'про нас': reverse('about'),
            'контакты': reverse('contacts'), 'производитель': reverse('maker')
        }
    }
    kw = kwargs['kwargs'] if kwargs else kwargs
    return context | kw


def index(request):
    return render(request, 'main/index.html', context=get_search_context())


class LatkrokOrder(ListView):
    model = Order
    template_name = 'main/order.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(is_ord=True, kwargs=context)


class LatkrokOrderProduct(DetailView):
    model = Order
    template_name = 'main/order_product.html'
    slug_url_kwarg = 'order_slug'
    context_object_name = 'order'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prise_fields'] = [f'prise_{i}' for i in range(1, 10)]

        return get_search_context(kwargs=context)


class LatkrokSpecial(ListView):
    model = SpecialOffer
    template_name = 'main/special.html'
    context_object_name = 'specials'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(is_spec=True, kwargs=context)


class LatkrokSpecialProduct(DetailView):
    model = SpecialOffer
    template_name = 'main/special_product.html'
    slug_url_kwarg = 'special_slug'
    context_object_name = 'special'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(kwargs=context)


class LatkrokLogo(CreateView):
    form_class = LogoForm
    template_name = 'main/logo.html'
    success_url = reverse_lazy('logo_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(kwargs=context)


class LatkrokCart(CreateView):
    form_class = CartForm
    template_name = 'main/cart.html'
    success_url = reverse_lazy('cart_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(kwargs=context)


def cart_success(request):
    return render(request, 'main/success.html', context={'redirect_from_cart': True})


def logo_success(request):
    return render(request, 'main/success.html', context={'redirect_from_cart': False})


def about(request):
    return render(request, 'main/about.html', context=get_search_context())


def contacts(request):
    return render(request, 'main/contacts.html', context=get_search_context())


def maker(request):
    field_name = 'url'
    obj = FillUrl.objects.first()
    field_value = getattr(obj, field_name) if obj else ''
    return render(request, 'main/maker.html', context=get_search_context(kwargs={'url': field_value}))
