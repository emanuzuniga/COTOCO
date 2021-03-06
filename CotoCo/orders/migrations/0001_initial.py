# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('suppliers', '0001_initial'),
        ('activities', '0001_initial'),
        ('projects', '0002_auto_20160807_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(verbose_name='Fecha')),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Precio Total')),
                ('order_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Activity', verbose_name='Actividad')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_detail_description', models.CharField(default='', max_length=255, verbose_name='Descripci\xf3n')),
                ('order_detail_amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Cantidad')),
                ('order_detail_unit', models.CharField(default='', max_length=255, verbose_name='Unidad')),
                ('order_detail_price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Precio unitario')),
                ('order_detail_total', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Precio Total')),
                ('order_detail_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Producto')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Detalle de la orden',
                'verbose_name_plural': 'Detalles de ordenes',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_product_list',
            field=models.ManyToManyField(to='orders.OrderDetail', verbose_name='Lista de Detalles'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Proyecto'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier', verbose_name='Proveedor'),
        ),
    ]
