# Generated by Django 4.0.4 on 2022-05-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_description_en_order_description_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=75, verbose_name='Статья')),
                ('title_uk', models.CharField(db_index=True, max_length=75, null=True, verbose_name='Статья')),
                ('title_en', models.CharField(db_index=True, max_length=75, null=True, verbose_name='Статья')),
                ('title_ru', models.CharField(db_index=True, max_length=75, null=True, verbose_name='Статья')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('img', models.ImageField(upload_to='articles_photo', verbose_name='Картинка')),
                ('content', models.TextField(db_index=True, verbose_name='Контент')),
                ('content_uk', models.TextField(db_index=True, null=True, verbose_name='Контент')),
                ('content_en', models.TextField(db_index=True, null=True, verbose_name='Контент')),
                ('content_ru', models.TextField(db_index=True, null=True, verbose_name='Контент')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('-time_create',),
            },
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description',
            field=models.TextField(db_index=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description_en',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description_ru',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='description_uk',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
    ]