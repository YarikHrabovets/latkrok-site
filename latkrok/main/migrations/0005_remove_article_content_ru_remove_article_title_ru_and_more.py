# Generated by Django 4.0.4 on 2022-06-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_fillurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='order',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='title_ru',
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_1',
            field=models.IntegerField(verbose_name='1 раза в месяц'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_2',
            field=models.IntegerField(verbose_name='2 раз в месяц'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_3',
            field=models.IntegerField(verbose_name='1 раза в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_4',
            field=models.IntegerField(verbose_name='2 раз в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_5',
            field=models.IntegerField(verbose_name='3 раз в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_6',
            field=models.IntegerField(verbose_name='4 раз в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_7',
            field=models.IntegerField(verbose_name='5 раз в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_8',
            field=models.IntegerField(verbose_name='6 раз в неделю'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_9',
            field=models.IntegerField(verbose_name='каждый день(в Сб) - доп ковер'),
        ),
    ]
