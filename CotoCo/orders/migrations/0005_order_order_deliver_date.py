# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_order_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_deliver_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de entrega'),
        ),
    ]
