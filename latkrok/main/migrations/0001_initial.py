# Generated by Django 4.0.4 on 2022-05-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('city', models.CharField(max_length=20, verbose_name='Город')),
                ('addr', models.CharField(max_length=70, verbose_name='Адрес')),
                ('details', models.TextField(verbose_name='Детали запроса')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='FillUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Url',
            },
        ),
        migrations.CreateModel(
            name='LogoOrd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=50, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('details', models.TextField(verbose_name='Детали запроса')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заказа')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Лого заказ',
                'verbose_name_plural': 'Лого заказы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=75, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(db_index=True, verbose_name='Описание')),
                ('img_1', models.ImageField(upload_to='photo', verbose_name='Картинка')),
                ('img_2', models.ImageField(upload_to='photo', verbose_name='Доп картинка')),
                ('img_3', models.ImageField(upload_to='photo', verbose_name='Доп картинка')),
                ('prise_1', models.IntegerField(verbose_name='Цена 1 раза в месяц')),
                ('prise_2', models.IntegerField(verbose_name='Цена 2 раз в месяц')),
                ('prise_3', models.IntegerField(verbose_name='Цена 1 раза в неделю')),
                ('prise_4', models.IntegerField(verbose_name='Цена 2 раз в неделю')),
                ('prise_5', models.IntegerField(verbose_name='Цена 3 раз в неделю')),
                ('prise_6', models.IntegerField(verbose_name='Цена 4 раз в неделю')),
                ('prise_7', models.IntegerField(verbose_name='Цена 5 раз в неделю')),
                ('prise_8', models.IntegerField(verbose_name='Цена 6 раз в неделю')),
                ('prise_9', models.IntegerField(verbose_name='Цена каждого дня(в Сб - доп ковер)')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступность')),
            ],
            options={
                'verbose_name': 'Аренда ковровых покрытий',
                'verbose_name_plural': 'Аренда ковровых покрытий',
            },
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=75, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('img_1', models.ImageField(upload_to='photo', verbose_name='Картинка')),
                ('img_2', models.ImageField(upload_to='photo', verbose_name='Доп картинка')),
                ('img_3', models.ImageField(upload_to='photo', verbose_name='Доп картинка')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('prise', models.IntegerField(verbose_name='Цена')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступность')),
            ],
            options={
                'verbose_name': 'Спец предложение',
                'verbose_name_plural': 'Спец предложения',
            },
        ),
    ]
