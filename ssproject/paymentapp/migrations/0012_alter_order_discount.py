# Generated by Django 4.0.6 on 2023-12-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("paymentapp", "0011_remove_tax_order_order_tax"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="paymentapp.discount",
            ),
        ),
    ]
