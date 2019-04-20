from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_id',
        'price_amount',
        'price_currency',
        'title',
        'description',
        'payment_url',
    )

admin.site.register(Order, OrderAdmin)
