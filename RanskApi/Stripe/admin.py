from django.contrib import admin
from .models import *


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount',)


admin.site.register(Discount, DiscountAdmin)


class OrderItemInlines(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    inlines = [OrderItemInlines, ]


admin.site.register(Order, OrderAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency',)
    list_filter = ('price',)


admin.site.register(Item, ItemAdmin)
