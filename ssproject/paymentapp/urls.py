from django.urls import path

from paymentapp.api import (
    GetStripeSessionIdInItemAPI,
    GetStripePublishedKeyAPI,
    GetStripeSessionIdInOrderAPI,
)
from paymentapp.views import (
    ItemDetailView,
    SuccessPaymentView,
    FailedPaymentView,
    ItemsListView,
    OrdersListView,
    OrderDetailView,
    DiscountsListView,
    TaxesListView,
)

app_name = "paymentapp"

urlpatterns = [
    # REST API
    path(
        "buy/<int:id_item>",
        GetStripeSessionIdInItemAPI.as_view(),
        name="GetStripeSessionId",
    ),
    path(
        "buy/order/<int:id_order>",
        GetStripeSessionIdInOrderAPI.as_view(),
        name="GetStripeSessionIdInOrder",
    ),
    path("get-key/", GetStripePublishedKeyAPI.as_view(), name="GetStripePublishedKey"),
    # Template View
    path("item/<int:pk>", ItemDetailView.as_view(), name="ItemDetailView"),
    path("success-payment/", SuccessPaymentView.as_view(), name="SuccessPaymentView"),
    path("failed-payment/", FailedPaymentView.as_view(), name="FailedPaymentView"),
    path("", ItemsListView.as_view(), name="ItemListView"),
    path("orders/", OrdersListView.as_view(), name="OrdersListView"),
    path("order/<int:pk>", OrderDetailView.as_view(), name="OrderDetailView"),
    path("discounts/", DiscountsListView.as_view(), name="DiscountsListView"),
    path("taxes/", TaxesListView.as_view(), name="TaxesListView"),
]
