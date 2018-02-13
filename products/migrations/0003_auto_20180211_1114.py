# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180206_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gift_order',
            field=models.BooleanField(default=False, verbose_name='Курс в подарок'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Создан'), ('wait', 'Ожидается оплата'), ('cancel', 'Отменен'), ('success', 'Выполнен')], default='new', max_length=20, verbose_name='Статус'),
        ),
    ]
