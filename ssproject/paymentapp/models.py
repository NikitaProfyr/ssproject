from typing import List

import stripe
from django.db import models

from ssproject.settings import STRIPE_SECRET_KEYS

stripe.api_key = STRIPE_SECRET_KEYS.get("BASE")

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=3, verbose_name="Трехбуквенный код")
    name = models.CharField(max_length=12, verbose_name="Наименование")
    country = models.CharField(max_length=100, verbose_name="Страна")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Item(models.Model):
    name = models.CharField(max_length=40, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, verbose_name="цена продукта"
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, verbose_name="Валюта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Discount(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50, verbose_name="Наименование")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Размер скидки %"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id == "":
            discount = stripe.Coupon.create(name=self.name, percent_off=self.amount)
            self.id = discount.id
        else:
            stripe.Coupon.modify(
                self.pk,
                name=self.name,
            )
        super(Discount, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        stripe.Coupon.delete(self.id)
        super(Discount, self).delete(using=using, keep_parents=keep_parents)

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"


class Tax(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=50, verbose_name="Наименование")
    description = models.TextField(default="описание", verbose_name="Описание")
    jurisdiction = models.TextField(default="юрисдикция", verbose_name="Юрисдикция")
    rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ставка")
    inclusive = models.BooleanField(
        default=False, verbose_name="включенный или отдельный от цены"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk == "":
            tax_rate = stripe.TaxRate.create(
                display_name=self.name,
                description=self.description,
                jurisdiction=self.jurisdiction,
                percentage=self.rate,
                inclusive=self.inclusive,
            )
            self.id = tax_rate.id
        else:
            stripe.TaxRate.modify(
                self.pk,
                display_name=self.name,
                description=self.description,
                jurisdiction=self.jurisdiction,
            )
        super(Tax, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        stripe.TaxRate.modify(self.id, active=False)
        super(Tax, self).delete(using=using, keep_parents=keep_parents)

    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"


class Order(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания заказа"
    )
    items = models.ManyToManyField(Item, related_name="items", verbose_name="Продукты")
    discount = models.ForeignKey(
        Discount,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Купон на скидку",
    )
    tax = models.ForeignKey(
        Tax,
        null=True,
        on_delete=models.CASCADE,
        related_name="taxes",
        verbose_name="Налог",
    )

    def __str__(self):
        return f"№{self.pk} от {self.created_at}"

    def get_total_price(self) -> int:
        total_price = 0
        for item in self.items.all():
            total_price += item.price
        return total_price

    def get_items_in_order(self) -> List[Item]:
        items = self.items.all()
        return items

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "заказы"
