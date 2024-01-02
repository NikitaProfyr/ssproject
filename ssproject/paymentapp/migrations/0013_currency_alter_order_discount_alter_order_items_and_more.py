# Generated by Django 4.0.6 on 2023-12-29 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paymentapp', '0012_alter_order_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, verbose_name='Трехбуквенный код')),
                ('name', models.CharField(max_length=12, verbose_name='Наименование')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paymentapp.discount', verbose_name='Купон на скидку'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='items', to='paymentapp.item', verbose_name='Продукты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxes', to='paymentapp.tax', verbose_name='Налог'),
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='paymentapp.currency', verbose_name='Валюта'),
        ),
    ]
