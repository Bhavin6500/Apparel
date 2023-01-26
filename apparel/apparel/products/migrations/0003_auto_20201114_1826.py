# Generated by Django 3.1.2 on 2020-11-14 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201114_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=50, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]