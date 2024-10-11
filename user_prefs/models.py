from django.db import models


# Create your models here.
class Prefs(models.Model):
    budget_amount = models.FloatField(default=0)
    budget_period_in_days = models.IntegerField(default=0)
    account_currency = models.CharField(max_length=50, default='USD')

    def save(self, *args, **kwargs):
        if Prefs.objects.exists() and self.pk is None:
            raise Exception('Prefs object already exists')
        else:
            super(Prefs, self).save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        return instance