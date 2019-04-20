from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Order


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.djhtml'
    fields = (
        'price_amount',
        'price_currency',
        'title',
        'description',
    )

    def get_success_url(self):
        return self.object.payment_url


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.djhtml'
