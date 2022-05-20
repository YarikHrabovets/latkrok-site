from django.db import models
from django.urls import reverse

class Order(models.Model):
    title = models.CharField('Название', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    info = models.TextField('Описание')
    img = models.ImageField('Картинка', upload_to='photo')
    img_1 = models.ImageField('Доп картинка', upload_to='photo')
    img_2 = models.ImageField('Доп картинка', upload_to='photo')
    prise_1 = models.CharField('Цена 1 раза в месяц', max_length=20)
    prise_2 = models.CharField('Цена 2 раз в месяц', max_length=20)
    prise_3 = models.CharField('Цена 1 раза в неделю', max_length=20)
    prise_4 = models.CharField('Цена 2 раз в неделю', max_length=20)
    prise_5 = models.CharField('Цена 3 раз в неделю', max_length=20)
    prise_6 = models.CharField('Цена 4 раз в неделю', max_length=20)
    prise_7 = models.CharField('Цена 5 раз в неделю', max_length=20)
    prise_8 = models.CharField('Цена 6 раз в неделю', max_length=20)
    prise_9 = models.CharField('Цена каждого дня(в Сб - доп ковер)', max_length=20)

    class Meta:
        verbose_name = 'Аренда ковровых покрытий'
        verbose_name_plural = 'Аренда ковровых покрытий'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_product', kwargs={'order_slug': self.slug})


class SpecialOffer(models.Model):
    title = models.CharField('Название', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    info = models.TextField('Описание')
    img = models.ImageField('Картинка', upload_to='static/main/admin_img')
    img_1 = models.ImageField('Доп картинка', upload_to='static/main/admin_img')
    img_2 = models.ImageField('Доп картинка', upload_to='static/main/admin_img')
    color = models.CharField('Цвет', max_length=20)
    prise = models.IntegerField('Цена')
    count = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Спец предложение'
        verbose_name_plural = 'Спец предложения'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('special_product', kwargs={'special_slug': self.slug})


class LogoOrd(models.Model):
    name = models.CharField('Имя', max_length=15)
    lastname = models.CharField('Фамилия', max_length=20)
    email = models.CharField('Адрес электронной почты', max_length=50)
    phone = models.CharField('Номер телефона', max_length=20)
    text = models.TextField('Детали запроса')

    def __str__(self):
        return f'заказ: {self.name} {self.lastname}'

    class Meta:
        verbose_name = 'Лого заказ'
        verbose_name_plural = 'Лого заказы'

class Cart(models.Model):
    name = models.CharField('Имя', max_length=15)
    lastname = models.CharField('Фамилия', max_length=20)
    phone = models.CharField('Номер телефона', max_length=13)
    mail = models.CharField('Почта', max_length=50)
    city = models.CharField('Город', max_length=20)
    addr = models.CharField('Адрес', max_length=70)
    products = models.TextField('Детали запроса')

    def __str__(self):
        return f'корзина: {self.name} {self.lastname}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class FillUrl(models.Model):
    url = models.URLField('Url')

    def __str__(self):
        return 'url'

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Url'