from django.db import models
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    made_at = models.DateTimeField(default=timezone.now)
    transaction_category = models.ForeignKey("TransactionCategory", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name