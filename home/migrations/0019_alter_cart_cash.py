# Generated by Django 4.2.17 on 2025-02-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_price_cart_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cash',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
