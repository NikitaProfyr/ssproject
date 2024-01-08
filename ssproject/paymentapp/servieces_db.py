from typing import Union

from paymentapp.models import Item, Order


def get_current_item(id_item: int) -> Union[Item, None]:
    """Возвращает продукт по id из бд либо None"""
    try:
        current_item = Item.objects.get(id=id_item)
        return current_item
    except Item.DoesNotExist:
        return None


def get_current_order(id_order: int) -> Union[Order, None]:
    """Возвращает заказ по id из бд либо None"""
    try:
        order = Order.objects.get(id=id_order)
        return order
    except order.DoesNotExist:
        return None
