# Generated by Django 4.0.6 on 2023-12-27 18:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("paymentapp", "0005_alter_discount_options_alter_discount_amount_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tax",
            options={"verbose_name": "Налог", "verbose_name_plural": "Налоги"},
        ),
    ]
