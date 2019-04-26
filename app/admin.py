from django.contrib import admin
from app import models


# Register your models here.


@admin.register(models.Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'unite']


@admin.register(models.OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'order_status', 'total_price']
    search_fields = ['order_id']
    list_editable = ['order_status']


@admin.register(models.OrderGoods)
class OrderGoodsAdmin(admin.ModelAdmin):
    list_display = ['get_order_id', 'sku', 'count']


admin.site.site_header = '书籍屋'
admin.site.site_title = '书籍屋'
