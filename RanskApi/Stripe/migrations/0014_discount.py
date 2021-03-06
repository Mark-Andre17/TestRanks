# Generated by Django 4.0.4 on 2022-05-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stripe', '0013_remove_order_quantity_remove_order_total_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('item', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_discount', to='Stripe.orderitem', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]
