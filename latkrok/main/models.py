from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    title = models.CharField(_('Название'), max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание', db_index=True)
    img_1 = models.ImageField(_('Картинка'), upload_to='photo')
    img_2 = models.ImageField(_('Доп картинка'), upload_to='photo')
    img_3 = models.ImageField(_('Доп картинка'), upload_to='photo')
    prise_1 = models.IntegerField(_('Цена 1 раза в месяц'))
    prise_2 = models.IntegerField(_('Цена 2 раз в месяц'))
    prise_3 = models.IntegerField(_('Цена 1 раза в неделю'))
    prise_4 = models.IntegerField(_('Цена 2 раз в неделю'))
    prise_5 = models.IntegerField(_('Цена 3 раз в неделю'))
    prise_6 = models.IntegerField(_('Цена 4 раз в неделю'))
    prise_7 = models.IntegerField(_('Цена 5 раз в неделю'))
    prise_8 = models.IntegerField(_('Цена 6 раз в неделю'))
    prise_9 = models.IntegerField(_('Цена каждого дня(в Сб) - доп ковер'))
    status = models.BooleanField(_('Доступность'), default=True)

    class Meta:
        verbose_name = _('Аренда ковровых покрытий')
        verbose_name_plural = _('Аренда ковровых покрытий')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_product', kwargs={'order_slug': self.slug})


class SpecialOffer(models.Model):
    title = models.CharField(_('Название'), max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    description = models.TextField(_('Описание'))
    img_1 = models.ImageField(_('Картинка'), upload_to='photo')
    img_2 = models.ImageField(_('Доп картинка'), upload_to='photo')
    img_3 = models.ImageField(_('Доп картинка'), upload_to='photo')
    color = models.CharField(_('Цвет'), max_length=20)
    prise = models.IntegerField(_('Цена'))
    count = models.IntegerField(_('Количество'))
    status = models.BooleanField(_('Доступность'), default=True)

    class Meta:
        verbose_name = _('Спец предложение')
        verbose_name_plural = _('Спец предложения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('special_product', kwargs={'special_slug': self.slug})


class LogoOrd(models.Model):
    name = models.CharField('Имя', max_length=15)
    lastname = models.CharField('Фамилия', max_length=20)
    email = models.CharField('Адрес электронной почты', max_length=50)
    phone = models.CharField('Номер телефона', max_length=20)
    details = models.TextField('Детали запроса')
    status = models.BooleanField('Статус заказа', default=False)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Лого заказ'
        verbose_name_plural = 'Лого заказы'

    def __str__(self):
        return f'заказ: {self.name} {self.lastname}'


class Cart(models.Model):
    name = models.CharField('Имя', max_length=15)
    lastname = models.CharField('Фамилия', max_length=20)
    phone = models.CharField('Номер телефона', max_length=13)
    email = models.CharField('Почта', max_length=50)
    city = models.CharField('Город', max_length=20)
    addr = models.CharField('Адрес', max_length=70)
    details = models.TextField('Детали запроса')
    status = models.BooleanField('Статус заказа', default=False)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'корзина: {self.name} {self.lastname}'


class FillUrl(models.Model):
    url = models.URLField('Url')

    def __str__(self):
        return 'url'

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Url'
