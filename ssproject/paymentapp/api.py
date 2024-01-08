from rest_framework.response import Response
from rest_framework.views import APIView

from paymentapp.servieces_db import get_current_item, get_current_order
from paymentapp.servieces_stripe import (
    create_payment_intent_in_item,
    create_stripe_session_in_order,
)
from ssproject.settings import STRIPE_SECRET_KEYS


class GetStripeSessionIdInItemAPI(APIView):
    """ "Возвращает сессию stripe на основе продукта"""

    def post(self, request, id_item: int):
        item = get_current_item(id_item=id_item)
        if item is None:
            return Response(
                {"msg": "Продукт с указанным идентификатором не найден"}, status=400
            )
        payment_method_id = request.data.get("paymentMethod")
        payment_intent = create_payment_intent_in_item(
            item=item, payment_method_id=payment_method_id
        )
        return Response({"session": payment_intent.client_secret})


class GetStripeSessionIdInOrderAPI(APIView):
    """ "Возвращает сессию stripe на основе заказа"""

    def get(self, request, id_order):
        order = get_current_order(id_order=id_order)
        if order is None:
            return Response(
                {"msg": "Заказ с указанным идентификатором не найден"}, status=400
            )
        session = create_stripe_session_in_order(order=order)
        return Response({"session": session.id})


class GetStripePublishedKeyAPI(APIView):
    """ "Возвращает публичный ключ stripe"""

    def get(self, request):
        return Response({"key": STRIPE_SECRET_KEYS.get("PUBLISHABLE")})
