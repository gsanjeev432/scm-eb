# Generated by Django 4.2.7 on 2024-11-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customer", "0001_initial"),
        ("manufacturer", "0002_manufacturer_location_alter_product_manufacturer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Placed", "Placed"),
                            ("Processed", "Processed"),
                            ("Shipped", "Shipped"),
                            ("Delivered", "Delivered"),
                        ],
                        default="Placed",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manufacturer.product",
                    ),
                ),
            ],
        ),
    ]
