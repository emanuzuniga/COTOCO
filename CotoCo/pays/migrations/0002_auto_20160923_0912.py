# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='pay_details',
            field=models.ManyToManyField(blank=True, to='pays.PayDetail', verbose_name='Detalles de Pago'),
        ),
    ]