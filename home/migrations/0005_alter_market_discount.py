# Generated by Django 4.2.17 on 2025-01-29 16:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_market_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='discount',
            field=models.IntegerField(default=0, verbose_name=django.core.validators.MaxValueValidator(99)),
        ),
    ]
