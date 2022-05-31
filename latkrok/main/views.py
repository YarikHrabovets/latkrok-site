from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *


def get_search_context(is_ord=False, is_spec=False, **kwargs) -> dict:
    ord, spec = '', ''
    if not is_ord:
        ord = Order.objects.filter(status=True)
    if not is_spec:
        spec = SpecialOffer.objects.filter(status=True)

    context = {
        'orders': ord,
        'specials': spec,
        'articles': Article.objects.all(),
        'static_urls': {
            'главная': reverse('index'), 'оренда': reverse('order'), 'лого': reverse('logo'), 'статьи': reverse('articles'),
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


class LatkrokArticle(ListView):
    model = Article
    template_name = 'main/list_article.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(is_spec=True, kwargs=context)


class LatkrokDetailArticle(DetailView):
    model = Article
    template_name = 'main/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
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
    return render(request, 'main/maker.html', context=get_search_context())
