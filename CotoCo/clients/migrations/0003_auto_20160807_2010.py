# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20160807_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='Identificaci\xf3n'),
        ),
    ]