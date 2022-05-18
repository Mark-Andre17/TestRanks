from django.db import models
from django.db.models import Sum, F


class Item(models.Model):
    CURRENCY = (
        ('rub', 'RUB'),
        ('usd', 'USD'),
    )
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=15, choices=CURRENCY, default='rub', verbose_name='Валюта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name='Почта')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE, related_name='item_order')
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='order_item')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    total_price = models.IntegerField(verbose_name='Общая стоимость', null=True, blank=True)


class Discount(models.Model):
    DISCOUNT = (
        ('0', '0 %'),
        ('5', '5 %'),
        ('10', '10 %'),
        ('15', '15 %'),
    )
    order = models.ForeignKey(OrderItem, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Заказ',
                              related_name='order_discount')
    discount = models.IntegerField(choices=DISCOUNT, default='0', verbose_name='Скидка')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
