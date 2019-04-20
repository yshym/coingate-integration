from django.urls import path, include

from .views import OrderCreateView, OrderListView


app_name = 'coingate'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('list/', OrderListView.as_view(), name='order_list'),
]
