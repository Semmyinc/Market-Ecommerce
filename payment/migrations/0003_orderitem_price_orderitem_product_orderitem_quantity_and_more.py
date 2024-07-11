# Generated by Django 4.2.13 on 2024-07-02 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0010_remove_category_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("payment", "0002_order_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=7),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gallery.product",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payment.order",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
