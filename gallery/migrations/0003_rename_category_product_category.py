# Generated by Django 4.2.13 on 2024-05-24 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="Category",
            new_name="category",
        ),
    ]
