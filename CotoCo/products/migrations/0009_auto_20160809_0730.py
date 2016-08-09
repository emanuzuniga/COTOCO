# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20160809_0717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsubdepartment',
            options={'ordering': ['productsubdepartment_department'], 'verbose_name': 'Sub-Familia', 'verbose_name_plural': 'Sub-Familias'},
        ),
        migrations.AddField(
            model_name='product',
            name='product_subdepartment',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductSubDepartment', verbose_name='Sub-Familia'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_department',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductDepartment', verbose_name='Familia'),
        ),
    ]
