from django.db import models
from django.urls import reverse

from tinymce import models as tinymce_models


class Order(models.Model):
    title = models.CharField('Назва', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    description = tinymce_models.HTMLField('Опис', db_index=True)
    img_1 = models.ImageField('Картинка', upload_to='photo')
    img_2 = models.ImageField('Доп картинка', upload_to='photo')
    img_3 = models.ImageField('Доп картинка', upload_to='photo')
    prise_1 = models.IntegerField('1 раз на місяць')
    prise_2 = models.IntegerField('2 рази на місяць')
    prise_3 = models.IntegerField('1 раз в тиждень')
    prise_4 = models.IntegerField('2 рази на тиждень')
    prise_5 = models.IntegerField('3 рази на тиждень')
    prise_6 = models.IntegerField('4 рази на тиждень')
    prise_7 = models.IntegerField('5 разів на тиждень')
    prise_8 = models.IntegerField('6 разів на тиждень')
    prise_9 = models.IntegerField('кожен день(в Сб) - додатковий килим')
    status = models.BooleanField('Доступність', default=True)

    class Meta:
        verbose_name = 'Оренда килимових покриттів'
        verbose_name_plural = 'Оренда килимових покриттів'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_product', kwargs={'order_slug': self.slug})


class SpecialOffer(models.Model):
    title = models.CharField('Назва', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    description = tinymce_models.HTMLField('Опис', db_index=True)
    img_1 = models.ImageField('Картинка', upload_to='photo')
    img_2 = models.ImageField('Доп картинка', upload_to='photo')
    img_3 = models.ImageField('Доп картинка', upload_to='photo')
    color = models.CharField('Колір', max_length=20)
    color_hex = models.CharField('Код кольору', max_length=20)
    prise = models.IntegerField('Ціна')
    count = models.IntegerField('Кількість')
    status = models.BooleanField('Доступність', default=True)

    class Meta:
        verbose_name = 'Спеціальна пропозиція'
        verbose_name_plural = 'Спецпропозиції'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('special_product', kwargs={'special_slug': self.slug})


class LogoOrd(models.Model):
    first_name = models.CharField("Ім'я", max_length=15)
    last_name = models.CharField('Прізвище', max_length=20)
    phone = models.CharField('Номер телефону', max_length=17)
    email = models.EmailField('Адреса електронної пошти', max_length=50)
    details = models.TextField('Деталі запиту')
    status = models.BooleanField('Статус замовлення', default=False)
    time_create = models.DateTimeField('Час створення', auto_now_add=True)

    class Meta:
        ordering = ('-time_create', )
        verbose_name = 'Замовлення на лого килим'
        verbose_name_plural = 'Замовлення на лого килими'

    def __str__(self):
        return f'Замовлення: {self.first_name} {self.last_name}'


class Cart(models.Model):
    first_name = models.CharField("Ім'я", max_length=15)
    last_name = models.CharField('Прізвище', max_length=20)
    phone = models.CharField('Номер телефону', max_length=17)
    email = models.EmailField('Адреса електронної пошти', max_length=50)
    city = models.CharField('Місто', max_length=20)
    address = models.CharField('Адреса', max_length=70)
    details = models.TextField('Деталі запиту')
    status = models.BooleanField('Статус замовлення', default=False)
    time_create = models.DateTimeField('Час створення', auto_now_add=True)

    class Meta:
        ordering = ('-time_create', )
        verbose_name = 'Замовлення на оренду'
        verbose_name_plural = 'Замовлення на оренду'

    def __str__(self):
        return f'Замовлення: {self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField('Стаття', max_length=75, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True, db_index=True)
    img = models.ImageField('Картинка', upload_to='articles_photo')
    content = tinymce_models.HTMLField('Контент', db_index=True)
    time_create = models.DateTimeField('Час створення', auto_now_add=True)

    class Meta:
        ordering = ('-time_create',)
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return f'Стаття: {self.title}'

    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'article_slug': self.slug})
