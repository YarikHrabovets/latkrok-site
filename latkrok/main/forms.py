from .models import LogoOrd, Cart
from django.forms import ModelForm, TextInput, Textarea


class LogoOrdForm(ModelForm):
    class Meta:
        model = LogoOrd
        fields = ['name', 'lastname', 'email', 'phone', 'text']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer01'
            }),
            'lastname': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer02'
            }),
            'email': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer03',
                'aria-describedby': 'inputGroupPrepend'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer04'
            }),
            'text': Textarea(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer05'
            })
        }

class CartDataForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['name', 'lastname', 'phone', 'mail', 'city', 'addr', 'products']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer01'
            }),
            'lastname': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer02'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer03'
            }),
            'mail': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer04'
            }),
            'city': TextInput(attrs={
                'class': 'form-control is-invalid',
                'id': 'validationServer05'
            }),
            'addr': TextInput(attrs={
                'class': 'form-control',
                'id': 'validationServer06 is-invalid'
            }),
            'products': Textarea(attrs={
                'style': 'visibility: hidden; width: 1px; height: 1px;',
                'id': 'basket_dt'
            })
        }