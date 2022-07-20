from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail
from latkrok.settings import EMAIL_HOST_USER, RECIPIENTS_EMAIL, EMAIL_HOST_PASSWORD
from django.template import loader
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
            'головна': reverse('index'), 'оренда': reverse('order'), 'лого': reverse('logo'), 'статті': reverse('articles'),
            'спецпропозиції': reverse('special'), 'кошик': reverse('cart'), 'про нас': reverse('about'),
            'контакти': reverse('contacts'), 'виробник': reverse('maker')
        }
    }
    kw = kwargs['kwargs'] if kwargs else kwargs
    context.update(kw)
    return context


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

    def form_valid(self, form):
        first_name, last_name, mail, content = [
            form.cleaned_data['first_name'], form.cleaned_data['last_name'],
            form.cleaned_data['email'], form.cleaned_data['details']
        ]
        html_message = loader.render_to_string(
            'main/mail.html',
            {
                'first_name': first_name,
                'last_name': last_name,
                'mail': mail,
                'content': content
            }
        )
        send_mail(
            'Вашу заявку на замовлення успішно відправлено',
            '', EMAIL_HOST_USER, [mail, *RECIPIENTS_EMAIL],
            auth_user=EMAIL_HOST_USER, auth_password=EMAIL_HOST_PASSWORD,
            fail_silently=False, html_message=html_message
        )

        return super(LatkrokLogo, self).form_valid(form)


class LatkrokCart(CreateView):
    form_class = CartForm
    template_name = 'main/cart.html'
    success_url = reverse_lazy('cart_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(kwargs=context)

    def form_valid(self, form):
        first_name, last_name, mail, content = [
            form.cleaned_data['first_name'], form.cleaned_data['last_name'],
            form.cleaned_data['email'], form.cleaned_data['details']
        ]
        html_message = loader.render_to_string(
            'main/mail.html',
            {
                'first_name': first_name,
                'last_name': last_name,
                'mail': mail,
                'content': content
            }
        )
        send_mail(
            'Вашу заявку на замовлення успішно відправлено',
            '', EMAIL_HOST_USER, [mail, *RECIPIENTS_EMAIL],
            auth_user=EMAIL_HOST_USER, auth_password=EMAIL_HOST_PASSWORD,
            fail_silently=False, html_message=html_message
        )

        return super(LatkrokCart, self).form_valid(form)


class LatkrokArticle(ListView):
    model = Article
    template_name = 'main/list_article.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_search_context(kwargs=context)


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


def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)
