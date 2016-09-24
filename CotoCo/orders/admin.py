# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Order, OrderDetail


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def buttonPdf(self, obj):

        return '''<a type="button" class="btn btn-admin pdfBtn" role="button" >Ver</a>'''

    def buttonEdit(self, obj):
        return '''<a type="button" class="btn btn-admin editBtn" role="button" href="/order/edit/">Editar</a>'''

    buttonPdf.short_description = 'Ver'
    buttonPdf.allow_tags = True

    buttonEdit.short_description = 'Editar'
    buttonEdit.allow_tags = True

    list_display = ('id', 'buttonPdf', 'buttonEdit', 'order_date', 'order_supplier', 'order_project', 'order_activity',
                    'order_subtotal', 'order_iv', 'order_total')
    search_fields = ('id', 'order_date', 'order_supplier', 'order_project', 'order_activity')
    filter_horizontal = ('order_product_list',)

    class Media:

        js = ("../static/js/admin/orders/button.js",)


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_detail_product', 'order_detail_product_code', 'order_detail_description', 'order_detail_price', 'order_detail_amount', 'order_detail_total',)
    search_fields = ('id', 'order_detail_product', 'order_detail_price', 'order_detail_amount', 'order_detail_total',)
#   filter_horizontal = ('',)
