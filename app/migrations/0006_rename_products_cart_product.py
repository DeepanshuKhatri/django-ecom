# Generated by Django 4.2.11 on 2024-04-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_product_cart_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products',
            new_name='product',
        ),
    ]