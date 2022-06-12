from .models import LogoOrd, Cart
from django.forms import ModelForm, TextInput, Textarea
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class LogoForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = LogoOrd
        fields = ['first_name', 'last_name', 'email', 'phone', 'details']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'last_name'}),
            'email': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'email', 'aria-describedby': 'inputGroupPrepend'}),
            'phone': TextInput(attrs={'type': 'tel', 'onkeyup': "javascript:mask('phone', '+38(000)000-00-00', event);", 'class': 'form-control is-invalid', 'id': 'phone'}),
            'details': Textarea(attrs={'class': 'form-control is-invalid', 'id': 'details'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if any(map(str.isdigit, first_name)):
            raise ValidationError("Введіть правильне ім'я")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if any(map(str.isdigit, last_name)):
            raise ValidationError('Введіть правильне прізвище')

        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 17:
            raise ValidationError('Введіть коректний номер телефону')

        return phone


class CartForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Cart
        fields = ['first_name', 'last_name', 'phone', 'email', 'city', 'address', 'details']
        widgets = {
            'first_name': TextInput(attrs={'type': 'text', 'class': 'form-control is-invalid', 'id': 'first_name'}),
            'last_name': TextInput(attrs={'type': 'text', 'class': 'form-control is-invalid', 'id': 'last_name'}),
            'phone': TextInput(attrs={'type': 'tel', 'onkeyup': "javascript:mask('phone', '+38(000)000-00-00', event);", 'class': 'form-control is-invalid', 'id': 'phone'}),
            'email': TextInput(attrs={'class': 'form-control is-invalid', 'id': 'email'}),
            'city': TextInput(attrs={'type': 'text', 'class': 'form-control is-invalid', 'id': 'city'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'address is-invalid'}),
            'details': Textarea(attrs={'style': 'display: none; visibility: hidden; width: 1px; height: 1px;', 'id': 'details'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if any(map(str.isdigit, first_name)):
            raise ValidationError("Введіть правильне ім'я")

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if any(map(str.isdigit, last_name)):
            raise ValidationError('Введіть правильне прізвище')

        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) != 17:
            raise ValidationError('Введіть коректний номер телефону')

        return phone

    def clean_city(self):
        city = self.cleaned_data['city']
        if any(map(str.isdigit, city)):
            raise ValidationError('Введіть коректне місто')

        return city
