from django.db import models
from django.urls import reverse


class Order(models.Model):
    title = models.CharField('Название', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    description = models.TextField('Описание', db_index=True)
    img_1 = models.ImageField('Картинка', upload_to='photo')
    img_2 = models.ImageField('Доп картинка', upload_to='photo')
    img_3 = models.ImageField('Доп картинка', upload_to='photo')
    prise_1 = models.IntegerField('1 раза в месяц')
    prise_2 = models.IntegerField('2 раз в месяц')
    prise_3 = models.IntegerField('1 раза в неделю')
    prise_4 = models.IntegerField('2 раз в неделю')
    prise_5 = models.IntegerField('3 раз в неделю')
    prise_6 = models.IntegerField('4 раз в неделю')
    prise_7 = models.IntegerField('5 раз в неделю')
    prise_8 = models.IntegerField('6 раз в неделю')
    prise_9 = models.IntegerField('каждый день(в Сб) - доп ковер')
    status = models.BooleanField('Доступность', default=True)

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
    description = models.TextField('Описание', db_index=True)
    img_1 = models.ImageField('Картинка', upload_to='photo')
    img_2 = models.ImageField('Доп картинка', upload_to='photo')
    img_3 = models.ImageField('Доп картинка', upload_to='photo')
    color = models.CharField('Цвет', max_length=20)
    color_hex = models.CharField('Код цвета', max_length=20)
    prise = models.IntegerField('Цена')
    count = models.IntegerField('Количество')
    status = models.BooleanField('Доступность', default=True)

    class Meta:
        verbose_name = 'Спец предложение'
        verbose_name_plural = 'Спец предложения'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('special_product', kwargs={'special_slug': self.slug})


class LogoOrd(models.Model):
    first_name = models.CharField('Имя', max_length=15)
    last_name = models.CharField('Фамилия', max_length=20)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Адрес электронной почты', max_length=50)
    details = models.TextField('Детали запроса')
    status = models.BooleanField('Статус заказа', default=False)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Лого заказ'
        verbose_name_plural = 'Лого заказы'

    def __str__(self):
        return f'заказ: {self.first_name} {self.last_name}'


class Cart(models.Model):
    first_name = models.CharField('Имя', max_length=15)
    last_name = models.CharField('Фамилия', max_length=20)
    phone = models.CharField('Номер телефона', max_length=13)
    email = models.EmailField('Почта', max_length=50)
    city = models.CharField('Город', max_length=20)
    address = models.CharField('Адрес', max_length=70)
    details = models.TextField('Детали')
    status = models.BooleanField('Статус заказа', default=False)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        ordering = ('-time_create',)
        verbose_name = 'Заказ на оренду'
        verbose_name_plural = 'Заказы на оренду'

    def __str__(self):
        return f'заказ: {self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField('Статья', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    img = models.ImageField('Картинка', upload_to='articles_photo')
    content = models.TextField('Контент', db_index=True)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        ordering = ('-time_create',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'статья: {self.title}'

    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'article_slug': self.slug})
