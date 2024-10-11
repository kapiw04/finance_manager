from django.db import models


# Create your models here.
class Prefs(models.Model):
    budget_amount = models.FloatField(default=0)
    budget_period_in_days = models.IntegerField(default=0)
    account_currency = models.CharField(max_length=50, default='USD')

