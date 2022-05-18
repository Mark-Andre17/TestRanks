# Generated by Django 4.0.4 on 2022-05-18 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stripe', '0014_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_discount', to='Stripe.order', verbose_name='Товар'),
        ),
    ]