# Generated by Django 2.2 on 2019-04-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coingate', '0002_order_price_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]