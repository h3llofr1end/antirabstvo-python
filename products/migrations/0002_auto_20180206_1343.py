# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180206_1310'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='give_access_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course', verbose_name='Продукт даёт доступ к курсу:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/products/images/', verbose_name='Картинка продукта'),
        ),
    ]