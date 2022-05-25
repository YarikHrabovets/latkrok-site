import re

from .models import LogoOrd, Cart
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError


class LogoOrdForm(ModelForm):
    class Meta:
        model = LogoOrd
        fields = ['name', 'lastname', 'email', 'phone', 'details']
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


class CartForm(ModelForm):

    class Meta:
        model = Cart
        fields = ['name', 'lastname', 'phone', 'email', 'city', 'addr', 'details']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'validationServer01'}),
            'lastname': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'validationServer02'}),
            'phone': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'validationServer03'}),
            'email': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'validationServer04'}),
            'city': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'validationServer05'}),
            'addr': TextInput(attrs={'class': 'form-control', 'id': 'validationServer06 is-invalid'}),
            'details': Textarea(attrs={'style': 'visibility: hidden; width: 1px; height: 1px;', 'id': 'basket_dt'})
        }

    def clean_email(self):
        pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
        email = self.cleaned_data['email']
        if re.match(pattern, email) is not None:
            return email

        raise ValidationError('Введите коректную почту')
