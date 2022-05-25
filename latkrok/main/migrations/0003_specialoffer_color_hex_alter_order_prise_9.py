# Generated by Django 4.0.4 on 2022-05-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_is_available_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='color_hex',
            field=models.CharField(max_length=20, null=True, verbose_name='Код цвета'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prise_9',
            field=models.IntegerField(verbose_name='Цена каждого дня(в Сб) - доп ковер'),
        ),
    ]