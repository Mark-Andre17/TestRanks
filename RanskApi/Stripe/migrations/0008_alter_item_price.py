# Generated by Django 4.0.4 on 2022-05-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stripe', '0007_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
