# Generated by Django 5.0.6 on 2024-07-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_price_alter_product_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
