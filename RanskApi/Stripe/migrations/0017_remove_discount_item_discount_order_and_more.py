# Generated by Django 4.0.4 on 2022-05-18 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stripe', '0016_alter_discount_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='item',
        ),
        migrations.AddField(
            model_name='discount',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_discount', to='Stripe.orderitem', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.IntegerField(choices=[('0', '0 %'), ('5', '5 %'), ('10', '10 %'), ('15', '15 %')], default='0', verbose_name='Скидка'),
        ),
    ]
