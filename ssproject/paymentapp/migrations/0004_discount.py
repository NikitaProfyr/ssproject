# Generated by Django 4.0.6 on 2023-12-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("paymentapp", "0003_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("name", models.CharField(max_length=50)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "orders",
                    models.ManyToManyField(
                        related_name="discounts", to="paymentapp.order"
                    ),
                ),
            ],
        ),
    ]
