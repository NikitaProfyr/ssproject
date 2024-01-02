from typing import Union

import stripe

from stripe.checkout import Session

from paymentapp.models import Item, Order
from ssproject.settings import BASE_URL, STRIPE_SECRET_KEYS


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


def get_price_data_item(item: Item) -> dict:
    """Возвращает информацию о продукте для сессии stripe"""
    data = {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': item.name,
                'description': item.description,
            },
            'unit_amount': int(item.price) * 100,  # цена в центах
        },
        'quantity': 1,
    }
    return data


def create_payment_intent_in_item(item: Item, payment_method_id: str) -> stripe.PaymentIntent:
    """Создает PaymentIntent на основе 1 продукта"""
    stripe.api_key = STRIPE_SECRET_KEYS.get('BASE')
    checkout_params = {
                "payment_method_types": ['card'],
                "amount": int(item.price * 100),
                "currency": item.currency.code,
                "confirm": True,
                "payment_method": payment_method_id
            }
    payment_intent = stripe.PaymentIntent.create(**checkout_params)
    return payment_intent


def create_stripe_session_in_order(order: Order) -> Union[Session]:
    """Создает сессию stripe на основе данных заказа"""
    stripe.api_key = STRIPE_SECRET_KEYS.get('BASE')
    coupon_code = order.discount
    line_items = []
    tax = order.tax
    items = order.get_items_in_order()
    for item in items:
        price_data = get_price_data_item(item)
        if tax:
            price_data['tax_rates'] = [tax.id]
        line_items.append(price_data)
    checkout_params = {
        "payment_method_types": ['card'],
        "line_items": line_items,
        "mode": 'payment',
        "success_url": BASE_URL + 'success-payment/',
        "cancel_url": BASE_URL + 'failed-payment/',
    }
    if coupon_code:
        checkout_params['discounts'] = [{
            'coupon': coupon_code.pk
        }]
    session = stripe.checkout.Session.create(**checkout_params)
    return session

