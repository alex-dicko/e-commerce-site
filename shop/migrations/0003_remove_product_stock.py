# Generated by Django 5.1.5 on 2025-03-12 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
