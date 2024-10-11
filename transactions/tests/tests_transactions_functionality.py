import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from transactions.models import Transaction, TransactionCategory
from user_prefs.models import Prefs

# initialize the APIClient app
client = Client()


class TestBudgetStatus(TestCase):
    def setUp(self):
        prefs = Prefs.get_instance()
        prefs.budget_period_in_days = 1
        prefs.budget_amount = 100
        prefs.save()
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

    def test_setting_budget(self):
        new_budget_amount = 200
        new_budget_period_in_days = 3
        payload = {'budget_amount': new_budget_amount,
                   'budget_period_in_days': new_budget_period_in_days}
        response = client.put(reverse('user_prefs_update'),
                               data=json.dumps(payload),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.get(reverse('user_prefs_update'))
        self.assertEqual(response.data['budget_amount'], new_budget_amount)
        self.assertEqual(response.data['budget_period_in_days'], new_budget_period_in_days)
        response = client.get(reverse('budget-status'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['is_in_budget'], True)
