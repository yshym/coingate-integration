from django.db import models
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .coingateapi_interface import CoingateAPIClient


class Order(models.Model):
    order_id = models.IntegerField(verbose_name=_('order id'))
    price_amount = models.FloatField(verbose_name=_('price amount'))
    price_currency = models.CharField(
        max_length=3,
        choices=(
            ('EUR', 'Euro'),
            ('USD', 'US Dollar'),
            ('BTC', 'Bitcoin'),
            ('ETH', 'Ethereum'),
            ('BCH', 'Bitcoin Cash'),
            ('LTC', 'Litecoin'),
        ),
        verbose_name=_('price currency')
    )
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(max_length=500, verbose_name=_('description'))
    payment_url = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('payment url')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def save(self, *args, **kwargs):
        client = CoingateAPIClient(settings.COINGATE_API_TOKEN)
        current_order_json = client.create_order(
            self.price_amount,
            self.price_currency,
            self.title,
            self.description
        )
        current_order_id = current_order_json.get('id')
        current_order_payment_url = current_order_json.get('payment_url')
        if not self.order_id:
            self.order_id = current_order_id
        if not self.payment_url:
            self.payment_url = current_order_payment_url
        super(Order, self).save(*args, **kwargs)

    def status(self):
        client = CoingateAPIClient(settings.COINGATE_API_TOKEN)
        current_order_json = client.get_order(self.order_id)
        return current_order_json.get('status')
