import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from transactions.models import Transaction, TransactionCategory
from user_prefs.models import Prefs


# initialize the APIClient app
client = Client()


class TestIfOverBudget(TestCase):
    def setUp(self):
        Prefs.objects.create(
            budget_amount=100,
            budget_period_in_days=1,
        )
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        Transaction.objects.create(
            title="Transaction 1", price=99, transaction_category_id=1
        )

    def test_if_over_the_budget(self):
        response = client.get(reverse('budget-status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_in_budget'], True)
        Transaction.objects.create(
            title="Transaction 1", price=2, transaction_category_id=1
        )
        response = client.get(reverse('budget-status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_in_budget'], False)
