from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

from paymentapp.models import Item, Order, Discount, Tax


# Create your views here.


class ItemDetailView(DetailView):
    model = Item
    template_name = "item-detail.html"
    context_object_name = "item"


class SuccessPaymentView(TemplateView):
    template_name = "success-payment.html"


class FailedPaymentView(TemplateView):
    template_name = "failed-payment.html"


class ItemsListView(ListView):
    model = Item
    template_name = "items-list.html"
    context_object_name = "items"


class OrdersListView(ListView):
    model = Order
    template_name = "orders-list.html"
    context_object_name = "orders"


class DiscountsListView(ListView):
    model = Discount
    template_name = "discounts-list.html"
    context_object_name = "discounts"


class TaxesListView(ListView):
    model = Tax
    template_name = "taxes-list.html"
    context_object_name = "taxes"


class OrderDetailView(DetailView):
    model = Order
    template_name = "order-detail.html"
    context_object_name = "order"
