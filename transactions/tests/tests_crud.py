import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Transaction, TransactionCategory
from ..serializers import TransactionSerializer


# initialize the APIClient app
client = Client()


class GetAllTransactionTest(TestCase):
    """ Test module for GET all transactions API """

    def setUp(self):
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        Transaction.objects.create(
            title="Transaction 1", price=1.00, transaction_category_id=1)
        Transaction.objects.create(
            title="Transaction 2", price=2.00, transaction_category_id=1)
        Transaction.objects.create(
            title="Transaction 3", price=3.00, transaction_category_id=1)
        Transaction.objects.create(
            title="Transaction 4", price=4.00, transaction_category_id=1)

    def test_get_all_experiments(self):
        # get API response
        response = client.get(reverse('transaction_list'))
        # get data from db
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """

    def setUp(self):
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        self.transaction_1 = Transaction.objects.create(
            title="Transaction 1", price=1.00, transaction_category_id=1)
        self.transaction_2 = Transaction.objects.create(
            title="Transaction 2", price=2.00, transaction_category_id=1)
        self.transaction_3 = Transaction.objects.create(
            title="Transaction 3", price=3.00, transaction_category_id=1)
        self.transaction_4 = Transaction.objects.create(
            title="Transaction 4", price=4.00, transaction_category_id=1)

    def test_get_valid_single_experiment(self):
        response = client.get(
            reverse('transaction_details', kwargs={'pk': self.transaction_2.pk}))
        experiment = Transaction.objects.get(pk=self.transaction_2.pk)
        serializer = TransactionSerializer(experiment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_experiment(self):
        response = client.get(
            reverse('transaction_details', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTransactionTest(TestCase):
    """ Test module for inserting a new experiment """

    def setUp(self):
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        self.valid_payload = {
            "title" : "Transaction 1",
            "price" : 1.00,
            "transaction_category" : 1
        }
        self.invalid_payload = {
            "title" : "",
            "price" : 1.00,
            "transaction_category" : 1
        }

    def test_create_valid_experiment(self):
        response = client.post(
            reverse('transaction_create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_experiment(self):
        response = client.post(
            reverse('transaction_create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTransactionTest(TestCase):
    """ Test module for updating an existing experiment record """

    def setUp(self):
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        self.transaction_1 = Transaction.objects.create(
            title="Transaction 1", price=1.00, transaction_category_id=1)
        self.transaction_2 = Transaction.objects.create(
            title="Transaction 2", price=2.00, transaction_category_id=1)
        self.valid_payload = {
            "title" : "Transaction 1",
            "price" : 10.00,
            "transaction_category" : 1
        }
        self.invalid_payload = {
            "title" : "Transaction 1",
            "price" : 1.00,
            "transaction_category" : 999
        }


    def test_valid_update_experiment(self):
        response = client.put(
            reverse('transaction_update', kwargs={'pk': self.transaction_2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_experiment(self):
        response = client.put(
            reverse('transaction_update', kwargs={'pk': self.transaction_2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTransactionTest(TestCase):
    """ Test module for deleting an existing experiment record """

    def setUp(self):
        TransactionCategory.objects.create(
            name="Category 1",
        )
        TransactionCategory.objects.create(
            name="Category 2",
        )
        self.transaction_1 = Transaction.objects.create(
            title="Transaction 1", price=1.00, transaction_category_id=1)
        self.transaction_2 = Transaction.objects.create(
            title="Transaction 2", price=2.00, transaction_category_id=1                                                                )

    def test_valid_delete_experiment(self):
        response = client.delete(
            reverse('transaction_delete', kwargs={'pk': self.transaction_2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('transaction_delete', kwargs={'pk': 9999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)