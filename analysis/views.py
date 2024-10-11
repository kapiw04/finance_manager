from typing import List

from django.db.models import QuerySet
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.models import Transaction
from user_prefs.models import Prefs


# Create your views here.
class BudgetStatusView(APIView):
    def get(self, request):
        budget_amount = Prefs.objects.get(pk=1).budget_amount
        budget_period = Prefs.objects.get(pk=1).budget_period_in_days

        transactions_within_period: QuerySet[Transaction] = Transaction.objects.filter(
            made_at__gt=timezone.now() - timezone.timedelta(days=budget_period),
        )
        is_in_budget = (
            sum(transactions_within_period.values_list("price", flat=True))
            <= budget_amount
        )

        return Response({"is_in_budget": is_in_budget})
