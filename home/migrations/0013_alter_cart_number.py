# Generated by Django 4.2.17 on 2025-01-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_customers_purchase_cart_customers_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='number',
            field=models.IntegerField(auto_created=True),
        ),
    ]
