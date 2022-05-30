# Generated by Django 4.0.4 on 2022-05-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description_en',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='order',
            name='description_ru',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='order',
            name='description_uk',
            field=models.TextField(db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='order',
            name='title_en',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='order',
            name='title_ru',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='order',
            name='title_uk',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='title_en',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='title_ru',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='title_uk',
            field=models.CharField(db_index=True, max_length=75, null=True, verbose_name='Название'),
        ),
    ]
