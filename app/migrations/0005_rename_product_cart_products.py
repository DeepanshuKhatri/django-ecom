# Generated by Django 4.2.11 on 2024-04-19 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='products',
        ),
    ]