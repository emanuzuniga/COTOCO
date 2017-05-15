# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-17 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0006_auto_20161115_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='pay_dollars',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Monto en Dolares'),
        ),
        migrations.AddField(
            model_name='pay',
            name='pay_exchange_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Tipo de Cambio'),
        ),
    ]