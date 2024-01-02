from django.contrib import admin

from .models import Item, Order, Discount, Tax, Currency

# Register your models here.


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    model = Item


@admin.register(Currency)
class CurrencyModelAdmin(admin.ModelAdmin):
    model = Currency


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    model = Order


@admin.register(Discount)
class DiscountModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    model = Discount

    def get_readonly_fields(self, request, obj=None):  # Администратор имеет доступ к полям amount при создании записи, но не может их менять при редактировании
        if obj:
            return self.readonly_fields + ('amount',)
        else:
            return self.readonly_fields


@admin.register(Tax)
class TaxModelAdmin(admin.ModelAdmin):  # Администратор имеет доступ к полям rate, inclusive при создании записи, но не может их менять при редактировании
    readonly_fields = ('id',)
    model = Tax

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('rate', 'inclusive',)
        else:
            return self.readonly_fields
