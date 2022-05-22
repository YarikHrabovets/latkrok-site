from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Order, SpecialOffer, FillUrl
from .forms import LogoOrdForm, CartDataForm, LogoOrd, Cart
from .sendScript import send_for_email


def index(request):
    return render(request, 'main/index.html')


class LatkrokOrder(ListView):
    model = Order
    template_name = 'main/order.html'
    context_object_name = 'orders'


class LatkrokOrderProduct(DetailView):
    model = Order
    template_name = 'main/order_product.html'
    slug_url_kwarg = 'order_slug'
    context_object_name = 'order'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prise_fields'] = [f'prise_{i}' for i in range(1, 10)]

        return context


def logo(request):
    err = ''
    if request.method == 'POST':
        form = LogoOrdForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                field_email = 'email'
                field_fn = 'name'
                field_ln = 'lastname'
                field_text = 'text'
                obj = LogoOrd.objects.last()
                value_email = getattr(obj, field_email)
                value_fn = getattr(obj, field_fn)
                value_ln = getattr(obj, field_ln)
                value_text = getattr(obj, field_text)
                send_for_email(value_email, value_fn, value_ln, value_text)
            except:
                return render(request, 'main/error.html')
        else:
            err = 'form is not valid'
    form = LogoOrdForm()
    context = {
        'form': form,
        'error': err
    }
    return render(request, 'main/logo.html', context)


class LatkrokSpecial(ListView):
    model = SpecialOffer
    template_name = 'main/special.html'
    context_object_name = 'specials'


class LatkrokSpecialProduct(DetailView):
    model = SpecialOffer
    template_name = 'main/special_product.html'
    slug_url_kwarg = 'special_slug'
    context_object_name = 'special'


def basket(request):
    err = ''
    if request.method == 'POST':
        form = CartDataForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                field_email = 'mail'
                field_fn = 'name'
                field_ln = 'lastname'
                field_text = 'products'
                obj = Cart.objects.last()
                value_email = getattr(obj, field_email)
                value_fn = getattr(obj, field_fn)
                value_ln = getattr(obj, field_ln)
                value_text = getattr(obj, field_text)
                send_for_email(value_email, value_fn, value_ln, value_text)
            except:
                return render(request, 'main/error.html')
        else:
            err = 'form is not valid'
    form = CartDataForm()
    context = {
        'form': form,
        'error': err
    }
    return render(request, 'main/basket.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def maker(request):
    field_name = 'url'
    obj = FillUrl.objects.first()
    field_value = getattr(obj, field_name)
    return render(request, 'main/maker.html', {'url': field_value})
    