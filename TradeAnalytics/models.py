import uuid

from django.db import models


# Create your models here.
class Broker (models.Model):
    broker_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    broker_name = models.CharField(max_length=50)
    broker_notes = models.TextField(max_length=512)


class Account(models.Model):
    account_number = models.CharField(max_length=25, primary_key=True)
    broker_id = models.ForeignKey(Broker, on_delete=models.CASCADE)
    account_alt_number = models.CharField(max_length=25)
    account_name = models.CharField(max_length=50)
    account_notes = models.TextField(max_length=512)
    currency = models.CharField(max_length=14)
    account_balance = models.FloatField(default=0)


class Trade(models.Model):
    broker_id = models.ForeignKey(Broker, primary_key=True, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    trade_id = models.CharField(max_length=32)
    currency = models.CharField(max_length=14)
    side = models.CharField(max_length=3, choices=[("BUY", "BUY"), ("SELL", "SELL")])
    open_period_datetime = models.DateTimeField()
    open_price_ask = models.FloatField()
    open_price_bid = models.FloatField()
    close_period_datetime = models.DateTimeField()
    close_price_ask = models.FloatField()
    close_price_bid = models.FloatField()
    gross_profit_loss = models.FloatField()
    commission = models.FloatField()
    net_profit = models.FloatField()


